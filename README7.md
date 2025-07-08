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
| 86540561-8802-3e68-9303-921be97924d4 | -6.9333 | -43.05276 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ce10d55-7c00-32cd-97e2-7ff000abe70e | -6.76052 | -43.4184 | 2025-07-08 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4169dde8-25e4-3abd-ab35-00b172153ec7 | -6.85502 | -44.07236 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b71dbd5-ab75-3358-9058-423643597d7c | -9.37848 | -48.95562 | 2025-07-08 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 255a2cc6-0ef9-3ae8-9023-6c778e79dbdc | -7.09674 | -44.15754 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6a5ddd-e6e2-3f41-bcc6-6d0d9b454e2b | -9.20589 | -45.34093 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd2c42a-2bfa-3e0b-aed8-23a0719e894e | -7.10503 | -44.16964 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c29885d-ee97-33be-9870-790792e67a3e | -7.10779 | -44.17368 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20d329f4-a10c-38fe-b77d-32c5ec4ec658 | -9.17899 | -50.18139 | 2025-07-08 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 442d85a3-fa84-3876-9075-f01794f05754 | -6.73221 | -44.33289 | 2025-07-08 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91bf6509-46dc-33e9-92cd-58897e59e128 | -5.73726 | -49.13616 | 2025-07-08 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 694b527f-ef14-3d14-8143-812edd174e91 | -5.73296 | -49.13548 | 2025-07-08 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f995127-673a-37c2-b6ee-1e3eecce33db | -7.43719 | -45.41871 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14be561c-511e-35bc-8d27-31c1789fbc4a | -7.19587 | -43.13692 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd153450-a196-38cc-87de-3b6fe83c843f | -5.25443 | -44.46357 | 2025-07-08 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80171770-a848-3491-a368-45904766dffa | -7.2579 | -43.08633 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ce574b4c-fe18-3047-8898-b7744e8ff62c | -8.21505 | -44.93413 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa1b5d2d-9301-31cd-a19e-2f41df0de3b5 | -4.37122 | -48.22888 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29cf78da-5596-3ef6-92b0-00152ae43a94 | -6.34694 | -46.36728 | 2025-07-08 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa15cfdd-87aa-31e9-9231-c35206c2509b | -6.86276 | -44.06642 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51323fb1-a48e-3382-b436-af7379c9abd6 | -8.22568 | -44.93216 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfa4f519-ccd9-3f0e-97ae-ac88c9bf6a53 | -4.29077 | -48.05565 | 2025-07-08 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 427c8d4f-2515-32f0-8a30-6644a7df6837 | -7.22277 | -43.11632 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 997ab25d-3e6a-3df9-925d-1f397da4d7a2 | -7.28105 | -44.64575 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8cfc768-24b6-34ab-9288-91e6d1f926cb | -7.10337 | -44.15858 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5053c27a-b82b-311b-b9c8-211ff2a03ab9 | -6.67721 | -43.86247 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 882915ed-0e16-3ece-9ce8-2befc50d4e9d | -7.19418 | -43.12604 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8e2e32f2-654c-3b44-8ba4-2d6a144f8919 | -6.68204 | -43.76731 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7682085f-5196-3345-aebe-3a26b9a4bdf3 | -7.25236 | -43.07837 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 94359a83-09b4-31b4-b7f4-43c5bf4c5b97 | -6.88632 | -45.24006 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc74ce5a-cab6-3f8e-9657-432e183dd1b9 | -6.53039 | -43.5408 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 918e83cd-795e-3b74-a18b-d8666257fcf8 | -5.41684 | -46.07153 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05723ae8-90b3-35bb-bca0-ccfbfdae6e1c | -7.27714 | -44.64875 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e983ac2-6ad6-394c-9b06-f323ccb1bf29 | -6.68073 | -43.36276 | 2025-07-08 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a992e56c-5f6b-370d-acf4-b81f6021da6a | -7.20079 | -43.12707 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2b1a3e05-09c1-38a3-b7ed-ac708b44c2ed | -8.71303 | -50.00015 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753185c4-ea9f-35ed-9e6d-c6df05badee3 | -6.88572 | -45.2438 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 127bfa61-60ed-3725-be3d-3e82a30edd9d | -8.70143 | -50.01539 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03cbf9c9-5600-395b-93fc-723708e194b7 | -6.93978 | -41.94987 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e39f75d0-b0ab-330c-ac48-54501839b08b | -5.65688 | -46.59022 | 2025-07-08 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b15ab36d-1858-3c8b-8da8-b990ff9198b0 | -7.20463 | -43.12412 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07602495-a9b2-3d76-bbf7-191418529c38 | -18.64458 | -55.73246 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e04f8030-eec7-3c66-9412-5da27ca1b2d8 | -11.43086 | -45.10955 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab8bfecc-0794-3e1b-8130-38e1eef36518 | -10.96243 | -48.20767 | 2025-07-08 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 941aa5e3-e83b-3c60-aa0d-d9863798c4df | -10.63283 | -49.45428 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6ac78a03-4b8a-3231-990f-b6debbf14cbc | -21.03965 | -55.99825 | 2025-07-08 04:17:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd08424-cea6-33a0-9507-ac3fae19472e | -15.25002 | -51.53652 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa9a7c53-2fb9-36f9-8841-6d960b1367ce | -13.89718 | -42.12936 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3653238a-f95f-365d-a443-06b1c2b0a288 | -13.01975 | -46.29646 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10d77976-33a1-36c6-a243-2f73e6689d2e | -10.65183 | -49.46509 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5d5bb8ac-6762-3be5-b343-0f44bb3a8d03 | -17.78032 | -42.80914 | 2025-07-08 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04681f18-3955-3ac0-8069-7f20cb45547b | -13.01044 | -46.75903 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc62e586-1593-3a1b-9154-d0dbfdfb5fd9 | -10.64308 | -49.46731 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3820feb7-d543-3abe-9592-73801af46ceb | -16.58513 | -43.6462 | 2025-07-08 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a7efb11-9877-3fc6-8017-888d3b246170 | -10.41558 | -49.76622 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee8f45da-b12d-3569-a516-9e801f524a9e | -15.25755 | -51.53051 | 2025-07-08 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ccd4f13-cd14-31e0-8827-89f521303954 | -10.23632 | -47.45997 | 2025-07-08 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1789fe73-ad83-393f-8703-1f59df571d15 | -12.99039 | -44.88498 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 719d60d5-61db-31f4-877a-3f82c3156e21 | -20.37778 | -45.60312 | 2025-07-08 04:17:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99f41d22-03e5-3e66-b2ee-0c1627629b1d | -18.64004 | -55.72781 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8c8f7d14-a3fe-3e5a-9cba-6501e48b81d5 | -11.9536 | -46.74965 | 2025-07-08 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fc6620f-e6c6-37fc-adfa-a0c5e6708cc8 | -21.62547 | -43.46671 | 2025-07-08 04:17:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3776c43f-b71f-3b9f-9a70-b3a6d8d20be4 | -22.24375 | -49.61147 | 2025-07-08 04:17:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dff72b88-404d-3969-a1fd-badc0fc5596a | -13.90013 | -42.13404 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 80c72b39-9571-3a0a-85aa-1b0f28de48e3 | -10.94766 | -49.2533 | 2025-07-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0f738b0-40bb-3fdb-85b6-205e6ad7833c | -17.63084 | -42.13152 | 2025-07-08 04:17:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0273f8b6-e416-3267-ba93-f3e5fa54ba98 | -13.02834 | -46.28631 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3f59fc8-14cb-3404-923f-1c76851709d9 | -11.44856 | -45.10518 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cbeafbb-9137-3432-becf-7db8d413c50e | -10.64905 | -49.45707 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e2aa7b0-bc40-3261-bd1f-1ac30efc04b8 | -21.19529 | -44.9384 | 2025-07-08 04:17:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fb03c6d8-4003-397d-9cbe-ee15816caa68 | -11.8998 | -44.91946 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db03c3a2-ec70-3de6-978f-951a0230ec9d | -20.76531 | -46.77007 | 2025-07-08 04:17:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c500eb0b-5507-3125-9d34-fea6bf4e0ae0 | -13.896 | -42.13763 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 708c7a53-ea34-3da0-a02b-bc6551a1e5ab | -16.04743 | -43.80158 | 2025-07-08 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| db584a52-7b58-335d-b175-a9d321f2dc95 | -10.21463 | -52.15679 | 2025-07-08 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8f41b8-b85a-3f77-a2df-7152bb4c6988 | -11.42091 | -45.10793 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6da7278-53e5-3a05-bafe-83616ccba6f8 | -13.65177 | -46.81288 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d6d5745-71fb-3867-8b31-65aa3b593b53 | -13.29042 | -49.1569 | 2025-07-08 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 171726de-07d4-3361-9804-d945aa348f1b | -10.4121 | -49.76166 | 2025-07-08 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6af3035c-a6d8-3ed3-ae88-5297079fa769 | -19.20612 | -55.75834 | 2025-07-08 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 560825fb-0db3-33a9-aee9-8ff930de6a19 | -21.2777 | -46.05162 | 2025-07-08 04:17:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0e7c6a4-935a-3373-8f20-f9bb83815f4b | -10.64842 | -49.46071 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e901c076-0c3b-3fe9-a45d-e527e4a8ac93 | -11.45177 | -45.10627 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf698808-8344-3ebf-8ba8-37a032589b34 | -15.73313 | -46.1935 | 2025-07-08 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4fa46290-d950-36e5-9a27-f69eaed55baa | -20.72794 | -56.65488 | 2025-07-08 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2d2e1fe-81e9-3423-9903-8c7759b16533 | -11.29652 | -45.26967 | 2025-07-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80eca7b5-667f-3406-b076-7bda674471e4 | -20.87916 | -43.91097 | 2025-07-08 04:17:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5e6ebc6-6f37-3b7f-b71d-1900d5930116 | -15.62112 | -46.46487 | 2025-07-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c3cac09-13b4-3469-a0b7-171eb1c96905 | -15.15023 | -41.82816 | 2025-07-08 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cf88d51-8033-3196-b4a5-e6790190e9af | -12.98653 | -44.88796 | 2025-07-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a33aa98e-f8f3-334b-a7e2-81f7c71ca97e | -13.28968 | -49.15411 | 2025-07-08 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c4ceeb8-59a2-3cb0-bed0-462e523467d6 | -11.88877 | -44.92488 | 2025-07-08 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1ea21fa-b33d-333f-a9af-09499308dcd9 | -20.87859 | -43.91512 | 2025-07-08 04:17:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d96641a-a43c-3140-a15f-49432502cb8d | -13.02434 | -46.28958 | 2025-07-08 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4755cbb2-1457-36fc-ba94-6b1a0dfc1f89 | -11.00589 | -42.78543 | 2025-07-08 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b013a04b-364a-33c1-b5a0-e50117db177b | -10.63625 | -49.45858 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcd0ee37-a6d5-32b9-a0d5-1e23799f2af1 | -18.65271 | -55.71991 | 2025-07-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f0a34831-adb8-31a5-97b3-674402ac0b6c | -13.90131 | -42.12579 | 2025-07-08 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 149b58c7-b4b7-3e27-a37a-86a3c069454a | -16.0542 | -43.80267 | 2025-07-08 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d039a3b-4777-3aad-b481-7114e9ee2682 | -10.63347 | -49.45065 | 2025-07-08 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README8.md)
