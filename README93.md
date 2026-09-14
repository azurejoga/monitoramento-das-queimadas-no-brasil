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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11b8b238-f873-3a2d-9d75-359642de72f9 | -10.5481 | -51.3156 | 2026-09-14 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e038aa1a-718e-3697-a1a1-914c42ad36be | -3.1096 | -60.6512 | 2026-09-14 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 375a1f93-a551-38ad-a4df-18db4ce7df0d | -7.1012 | -42.1088 | 2026-09-14 15:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 210.1 |
| c4b98c0e-9bf2-3330-b897-c3584e36f264 | -13.3182 | -51.7264 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 62f0e5b6-c946-3bd5-a632-8ba4863a71e4 | -3.3306 | -54.1805 | 2026-09-14 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 89966ac0-33e0-34c9-8343-506448c2189f | -6.0925 | -57.6847 | 2026-09-14 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| f87eeba6-0662-39d7-9b25-9af5b9adb400 | -13.3055 | -51.3235 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 97745862-e198-3130-aede-f29fe1b1bdc8 | -3.05844 | -41.22173 | 2026-09-14 15:50:00 | NOAA-20 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 33c25f93-975c-3bdd-8fb2-3791360684d7 | -3.45237 | -42.88157 | 2026-09-14 15:50:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f564eb6-0c09-31c4-8ed8-24383e3a9508 | -2.89036 | -39.99699 | 2026-09-14 15:50:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d4725b2d-5be1-380e-9981-828687ba3eca | -3.34222 | -43.23352 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4230ab9-b6da-3d9b-ab5b-465888d4b3e8 | -3.2276 | -43.03155 | 2026-09-14 15:50:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0192ae6-3a1e-3b03-b386-e6506726f1f8 | -3.34322 | -43.24039 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3bf7aa97-27c0-37cd-9f11-89317044cff4 | -3.9079 | -44.47756 | 2026-09-14 15:50:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d6262b47-696d-38e4-9f2f-d25258a1c4b5 | -3.23339 | -43.03404 | 2026-09-14 15:50:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5505ec3a-f21b-37c8-ad2e-0e3432887123 | -3.38734 | -42.84126 | 2026-09-14 15:50:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b26d3f56-5216-3c22-85dc-b337d2a5c32f | -3.60149 | -43.05445 | 2026-09-14 15:50:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd4f9042-7783-3e3e-9ff5-2ba98068f3b9 | -1.78786 | -44.98601 | 2026-09-14 15:50:00 | NOAA-20 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 74ca2a08-8af5-35c2-acb4-d156570f4f41 | -3.12255 | -40.16561 | 2026-09-14 15:50:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cca553e3-e847-3488-9c79-2cfef5b5f445 | -3.33634 | -43.23089 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c3ec5bc1-1594-3946-acd4-06f8cd454fc5 | -3.34272 | -43.23695 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e740a598-fbf4-3e39-8870-77a82dfd7114 | -3.60867 | -43.0295 | 2026-09-14 15:50:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed556ff1-04b4-36da-aa97-2ef49badf864 | -1.21134 | -46.85876 | 2026-09-14 15:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| e9411632-43d6-3ec5-983a-92c43b3b29ba | -2.95956 | -42.84932 | 2026-09-14 15:50:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fa4d314-4f6f-3e85-88f6-32bd03e1a074 | -2.95433 | -42.85007 | 2026-09-14 15:50:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3712d4d8-6b27-3d36-86f8-a39c3404e389 | -3.80094 | -44.10969 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8e9b4af8-47eb-3915-a6aa-dfb3a54da01b | -3.2217 | -40.10555 | 2026-09-14 15:50:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| fd747711-8f36-3a74-93ef-05f27a98ebe6 | -3.33683 | -43.23431 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37f3ba3e-d14b-3768-b44b-b73549241825 | -3.58355 | -42.86492 | 2026-09-14 15:50:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f72c7a51-ebcf-3087-8f08-5ceaabaa360f | -3.33144 | -43.23511 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c050635-469f-374b-93a4-920917cca302 | -3.22728 | -40.1133 | 2026-09-14 15:50:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d0d0a179-9056-3b66-b93f-37cee331ea3c | -3.14653 | -42.30567 | 2026-09-14 15:50:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6eb19cd5-1516-3577-b946-b080d869159b | -1.5797 | -45.4441 | 2026-09-14 15:50:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68f142a3-54e0-3553-aa86-fe7507f20467 | -3.14127 | -40.80024 | 2026-09-14 15:50:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c1159a0c-5957-372d-850c-0db99d30f50c | -3.2403 | -40.11142 | 2026-09-14 15:50:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d9e862fe-4aff-36a0-8df0-56ad68980d65 | -3.32929 | -42.29782 | 2026-09-14 15:50:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e905f7cc-b58c-3022-b1f9-7f251929fb41 | -3.3886 | -42.55907 | 2026-09-14 15:50:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59548429-608d-37c2-9378-0968cf21485c | -3.58399 | -42.8651 | 2026-09-14 15:50:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48c753ee-4e48-323b-8f12-84a702a55126 | -2.9591 | -42.84618 | 2026-09-14 15:50:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 426254f4-fd4e-31a4-9fa7-d269328e3a89 | -1.55254 | -46.4828 | 2026-09-14 15:50:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 93c9110b-f5c3-3c7d-9afa-ee14f64b463c | -3.90852 | -44.48184 | 2026-09-14 15:50:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d0f068f3-35dd-3202-8050-acf68fc6cb2d | -1.33182 | -47.69992 | 2026-09-14 15:50:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bbecbd31-96b4-3049-981f-daad4d9da029 | -2.77379 | -45.4996 | 2026-09-14 15:50:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e6b97c4a-1f20-39aa-89b3-f882fe9aad73 | -3.79462 | -44.10653 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3f7ac05-0605-376c-a031-24d25bc242b9 | -3.14058 | -40.79562 | 2026-09-14 15:50:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 32c54648-d034-3ba6-a532-4b7851acc0ee | -1.33159 | -47.70055 | 2026-09-14 15:50:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d0c4af09-6306-3ade-91c2-b6b7c93cbb9f | -3.23291 | -43.03078 | 2026-09-14 15:50:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17c7995f-dc3c-3329-93d1-12f7a8fea228 | -1.7885 | -44.99028 | 2026-09-14 15:50:00 | NOAA-20 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 79638ce3-3eed-3883-97b6-694d452c53fd | -3.38815 | -42.55605 | 2026-09-14 15:50:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e66ca3c5-435d-31d1-a94a-65fef4e7643a | -3.23775 | -43.02683 | 2026-09-14 15:50:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a8e8411-f472-34df-83da-0e458434a63b | -3.80669 | -44.10884 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2220d10f-23f2-3e0c-af1c-6a9d919bb1d9 | -3.33783 | -43.24119 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47dec195-3711-30dd-89ab-750c2aeaa6e8 | -3.23165 | -40.02394 | 2026-09-14 15:50:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6351f416-c76a-3892-a6c8-3c6026d33f73 | -3.43556 | -42.84072 | 2026-09-14 15:50:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c00eb95-eb01-3894-ab08-e0bfb1f81d5e | -3.34421 | -43.24727 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 20a7babb-d31f-3225-80c8-46fa965f204d | -3.31023 | -43.40514 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 76127024-700f-37d0-ab02-7197122377f1 | -3.36008 | -40.7212 | 2026-09-14 15:50:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 48b75ccb-5b25-3a7d-a2e1-6eeb8073894f | -3.42602 | -42.84882 | 2026-09-14 15:50:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95e28357-1aae-3a86-bf23-f5b1e7c91592 | -2.95864 | -42.84305 | 2026-09-14 15:50:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89fe7cc2-0832-35e6-bfad-868aefaa0cba | -1.5526 | -46.47915 | 2026-09-14 15:50:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb773106-45d2-3b14-b282-3416da3373b1 | -3.42554 | -42.84555 | 2026-09-14 15:50:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d8e1b15-9f36-3041-8b7e-af84ffd8d1da | -1.60781 | -45.12813 | 2026-09-14 15:50:00 | NOAA-20 | APICUM-AÇU | MARANHÃO | Brasil | 2100832 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 65bbc0da-d682-3f9f-a563-2466df54a632 | -3.59964 | -43.05476 | 2026-09-14 15:50:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f89f63bb-fc02-3cac-8038-fc456c448d52 | -2.73159 | -45.25701 | 2026-09-14 15:50:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e21e6252-1a0b-3c00-9b6d-33064a56c132 | -3.80151 | -44.11364 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| deb1f5b1-8068-3f00-a0fe-3f17d9994892 | -2.88976 | -39.99295 | 2026-09-14 15:50:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8e57d4fc-12b9-38de-b616-f4feb919fa86 | -3.80037 | -44.1057 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a3ff52f6-7560-3dcd-b940-3e8c66767634 | -3.60199 | -43.05779 | 2026-09-14 15:50:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b69c0a-f343-3a82-b6fe-c6da145fb8af | -3.597 | -43.02433 | 2026-09-14 15:50:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6bd5b1f7-07ad-311b-a3cb-6052d553e1e0 | -3.79979 | -44.10169 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 164ac321-49cd-363c-bc76-f08a5f43546d | -3.34372 | -43.24384 | 2026-09-14 15:50:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8824aef9-3c55-38fb-b85c-839b78e8f101 | -3.79518 | -44.11049 | 2026-09-14 15:50:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cb562822-0311-3ba0-bb45-beaf0dac7d6e | -3.36347 | -40.72015 | 2026-09-14 15:50:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 09598c79-2a0b-3eed-91d6-516c4dc80c14 | -1.21217 | -46.86427 | 2026-09-14 15:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2476a517-e28e-3b56-a41f-256a2ab89a53 | -1.24142 | -46.79137 | 2026-09-14 15:50:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c9adb5c6-5758-3ba1-ab60-770513320934 | -13.3059 | -51.3022 | 2026-09-14 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 334.7 |
| 92c1c12f-3ff5-3a00-b6cb-b10f7b7c74b9 | -11.5095 | -50.2559 | 2026-09-14 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 1e3bd9a8-589e-3265-bc17-a621c28692f8 | -13.3185 | -51.7051 | 2026-09-14 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c7574f91-90ed-3776-85e4-290ed0831128 | 1.3634 | -56.1228 | 2026-09-14 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 15ac61e8-731e-3e50-b56e-b3a84eb8697c | -6.1108 | -57.7035 | 2026-09-14 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 08f0bb91-123a-33f9-b66d-7d118eb44fda | -12.0273 | -49.9799 | 2026-09-14 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3c07de68-e924-370e-b787-773becca3579 | -9.3763 | -50.1139 | 2026-09-14 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 881d3f96-778e-3559-bd41-08e35bd81273 | -6.2917 | -55.2695 | 2026-09-14 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6ebc91d6-11f7-381a-a058-71ad1b1f9984 | -10.6335 | -50.5651 | 2026-09-14 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f437420a-48a6-3ce6-8318-1626a0af3634 | -3.6077 | -59.0577 | 2026-09-14 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| c629631a-2df5-3663-9696-05f8620fe88e | -10.5667 | -51.3349 | 2026-09-14 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a9a577f4-c0b9-36f2-a105-ada093a78a77 | -7.1012 | -42.1088 | 2026-09-14 16:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 236.2 |
| aa97aa01-058d-3ca9-bed1-e9fe896000bf | -6.1111 | -57.6645 | 2026-09-14 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 8f9e139e-db3b-3f0d-b36c-21f765bf5d57 | -8.5604 | -54.6973 | 2026-09-14 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0c94bfc4-a21e-3c99-813a-a4d489de9bf0 | -3.1633 | -61.1238 | 2026-09-14 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3409e1e8-1071-305b-a59d-57ecad196b5f | -13.2863 | -51.326 | 2026-09-14 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7ef91a7b-61be-3c01-bdea-fc40e8bd41f3 | -8.5417 | -54.6985 | 2026-09-14 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 032c273c-c375-30ca-aa6f-e561f4c4de4f | -13.5719 | -51.4605 | 2026-09-14 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 63963ad2-d408-3f2c-973b-e7c3bd671866 | -9.3765 | -50.0925 | 2026-09-14 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 9dd7be0f-8761-3eae-b325-41b7004a5194 | -8.7445 | -46.4213 | 2026-09-14 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 95a2b120-4b86-3c4b-9f70-72fa9295b38d | -3.1462 | -60.6317 | 2026-09-14 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 97b24130-e969-3644-971f-ebe6cbc2c2a4 | -3.3639 | -61.2715 | 2026-09-14 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e5a85258-0f1e-39b0-8afa-300a9545be59 | -9.3758 | -50.1565 | 2026-09-14 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 62271846-5d82-3f42-bd34-034a615dc948 | -2.6601 | -57.5702 | 2026-09-14 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b758b0b6-65e6-33a5-9d49-b3584799c8d9 | -13.3251 | -51.2997 | 2026-09-14 16:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |


[Clique aqui para ver as próximas entradas](README94.md)
