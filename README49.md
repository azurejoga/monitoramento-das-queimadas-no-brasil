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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 834d099c-a2a1-3fb8-a57b-3971dd39ea8a | -12.11021 | -44.85059 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cac9bd1-eebb-3b7b-93d0-46faae962ba2 | -10.22413 | -48.61522 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f6ff368-58aa-39bc-8b1f-b3fea3416094 | -11.74103 | -46.61453 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 3565e965-8c1a-3d85-a3f1-8999eb06192b | -13.47685 | -48.44549 | 2025-09-13 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f898610-83c5-3d79-b817-6f96038cb216 | -11.47404 | -43.61071 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ad5bc5a-7a72-3ee7-87ed-de7973ffbf2f | -14.61504 | -46.33812 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd32decf-b7dd-36df-a5dd-51da3f688afc | -11.76109 | -51.51073 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4365d40-d83c-3d4d-8972-adb4411d6f0d | -9.24151 | -51.21422 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a6fb685-64af-321d-bdd8-0f4e205fa13b | -11.43278 | -43.55344 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9b91290-c198-367f-9c85-d15c3a6e3d20 | -11.49669 | -43.64017 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61063a76-c9b8-3fa6-b431-6ef58d9a03f5 | -11.37185 | -43.5069 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55f278fa-6bc1-3a61-bcf1-eb7eaa8b0b1f | -11.14615 | -45.31478 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c0854f0-7355-3e31-affd-4c8087d39e12 | -9.2538 | -51.23635 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e30ff141-5d7b-38bc-8af2-5f61f89239a2 | -8.08814 | -50.18286 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8dec13e-93d0-38d1-9b51-88a409020f7c | -11.15628 | -50.71517 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7aaab76c-3e29-3bac-a96e-f0c2e3cf78e1 | -8.4793 | -45.1483 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36238e9a-8509-34a1-9210-32d5a952f8ca | -14.29245 | -46.08164 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9015d877-165b-3adc-b911-634867cd9fad | -10.77767 | -50.52706 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f26c8c5-df98-3be0-b757-c2f9f092b35d | -9.79112 | -47.79396 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fe95cd67-d59c-3310-876e-a44650b97e56 | -8.75181 | -44.231 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1134d92e-8453-303a-bfb5-e162ccf20ec6 | -11.14196 | -45.31816 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 07341a2c-48e4-3643-844e-71214a627852 | -11.14263 | -45.31416 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46d68943-8452-3d44-ad51-3ca815741b5e | -9.79677 | -48.90541 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16042fe5-62e6-31fd-810e-a13dbb154d77 | -8.09139 | -50.19356 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7878fe78-31fe-34c9-b7c9-5ddaf7405bd5 | -13.29429 | -43.76541 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fc0d604-39a7-3916-be7b-edbe2d3c02e4 | -11.73054 | -51.9258 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e30254-db89-3c84-a0bf-8a179dd0b83c | -12.94733 | -48.01135 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c37b182-0b29-31aa-948c-92b4e9e0044c | -12.65596 | -44.24212 | 2025-09-13 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a0c3115-fdb5-351a-8b6c-366b66f974bd | -11.45806 | -43.58243 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d31289-c4b6-3916-a355-9bf0067f1cb7 | -11.47128 | -43.60659 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fe61c1e-d93b-3e34-9500-44a997f3a509 | -10.51109 | -51.5405 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec26df91-8c87-3a57-bf60-2a9b5cba28ec | -15.23479 | -44.03794 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51d36c90-393e-31e4-a87f-dd327606749d | -13.91346 | -48.22384 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d76f86c-8186-373d-a872-73dddfd8eb3d | -11.86178 | -50.57837 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 941d2456-8e62-399b-b89f-1d56a1b65ea4 | -11.53314 | -48.29311 | 2025-09-13 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03bfd1d7-22a0-3ab7-90cc-d544228ebba2 | -14.19758 | -46.2543 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8b060e9-4ba7-340e-8d20-1fa6c5d915fa | -14.43664 | -48.43378 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d521ed54-8978-3516-98a9-3c7a05ca0793 | -10.77667 | -50.53259 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d2af811-8ae6-336e-8f92-af0d4462b38f | -12.95121 | -47.98926 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c15aa59e-359f-30f4-9c6d-0c4d6334461c | -13.26147 | -43.75975 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2193d61c-268c-3acf-bad6-350b8bcf5e06 | -14.22384 | -46.29386 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9449600a-3a48-3acb-8aab-e4d5da675f7d | -11.13874 | -50.70015 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9622dd7b-f2ea-38da-a4f5-1c124bb31c00 | -12.43695 | -43.24199 | 2025-09-13 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d85857ca-1a12-38c2-806b-4ec096cedf4c | -14.19609 | -46.24162 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7f77bdf6-0baa-31b8-8655-376b66fd18ba | -13.77492 | -46.28743 | 2025-09-13 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7622665e-ae7b-36f4-aff1-94cbd711a568 | -10.65116 | -46.28191 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 280f6e46-65f9-3960-aa20-333e7ab2d754 | -12.93273 | -47.97762 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 621b2a28-537d-3a90-ac3a-3bb2296c662d | -14.17909 | -46.27662 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| cfa81959-b772-351a-b29d-615da6e1c950 | -9.51614 | -54.63169 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 74c51d18-7da1-3505-96b3-55214cb5fb59 | -11.86278 | -50.56848 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6f78da17-c5c9-3b12-8e01-1019a33ca423 | -9.73333 | -51.01326 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d4e76411-cab6-356b-a6f9-dfa0154edfbc | -10.36038 | -50.50547 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71ca588d-7f31-3a4f-9179-3f226ceec8ac | -11.10161 | -51.44933 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e0f980-c677-3549-a530-e3472dac26fe | -11.44124 | -45.62811 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f84cb20-e5a2-3f30-afd2-ecff2ef4eb20 | -14.17978 | -46.27256 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 589181fd-d2dd-360a-9620-74de9bb21381 | -12.11016 | -44.88918 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f18ce8e2-f08d-3f93-863f-aa8eed35003b | -12.95317 | -48.00153 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ddae73ea-d049-317f-bd03-f3f8777e5b3f | -14.21884 | -46.28008 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77ce3ecd-0dd7-3a40-9c54-4e082eb0f0f5 | -13.40629 | -46.79878 | 2025-09-13 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a73bf77-2c47-3ed3-98d2-c0401b892839 | -15.65348 | -41.82671 | 2025-09-13 04:08:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ddf2f5f-c790-3ccd-95dd-5de8c77929df | -10.50992 | -51.54692 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 418ba8fa-aa6d-3015-8caa-2ab3d39bac39 | -9.96319 | -50.29612 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9bc1dae7-5945-3b81-8c90-d9db69dafb6f | -13.70185 | -42.69122 | 2025-09-13 04:08:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b99ec325-eb1a-3ead-a1cb-49d1f206c3d6 | -11.82155 | -50.55388 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c24ac2d4-a9a0-33ca-9308-8de00b3c83eb | -9.25722 | -51.24753 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba76fd27-ee9a-37d8-8d12-5f84faffbee8 | -8.92399 | -46.14259 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd005ae1-6911-304c-9b58-2ddf4ce0dc6b | -14.44121 | -47.31564 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| deb45caf-6b85-3289-bd44-76466d80f8a9 | -10.65039 | -46.28647 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14b31d69-abad-369f-9c2c-f5b06d39326b | -11.74024 | -46.61916 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 51e77150-a8fa-376b-9697-bf11578c5c43 | -12.91045 | -47.96442 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a221cf9d-48cb-3511-b409-efa39e92bc62 | -14.4288 | -48.43141 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 569067d1-ce05-3a12-9091-cbb7e6bced04 | -11.42421 | -45.60513 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7efd9f7-ee2e-3a38-8f6d-77d0a7c753a1 | -12.99997 | -46.75401 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2db2ce7b-e288-3fb4-8271-3a71db8e5d95 | -11.44663 | -48.55733 | 2025-09-13 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 448d16a1-d00e-36e7-8a9a-74b8f37f14e3 | -12.93725 | -47.99851 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 209a0888-6f9e-3096-9e89-64b9d5ae39d7 | -12.91613 | -54.75619 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e8335685-8011-3f4b-9e9d-d987677191d5 | -13.9459 | -48.20255 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bf248e3a-7dc3-387b-be7c-ab25c60a1e88 | -10.405 | -50.5942 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48b24b59-4da3-31d9-857f-048e3af12911 | -14.6222 | -46.3605 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91c31a3a-66fd-3f6b-b41d-26c266644f83 | -9.22864 | -51.2253 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73ffdf02-1a3c-3472-a37c-db99ae7c6de5 | -14.18119 | -46.28575 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 28f82011-b3a7-310b-80b3-6f582fd31baa | -11.40616 | -43.6553 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 972816f3-e0e1-3ac6-acc3-227e113f70c2 | -14.43747 | -47.31497 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40f5c59d-2ac4-3478-b111-30a2bc50c2e4 | -15.23741 | -44.06414 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f32a2a11-a00f-3075-b2f6-7a5d785dd227 | -11.50003 | -43.64073 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 542e6c6e-e5b2-3f1e-bb82-6c5967376d83 | -11.37898 | -47.33002 | 2025-09-13 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25a61d14-fd70-34a4-ad0e-db3598d88416 | -12.99843 | -46.7507 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 707192fb-863f-35fa-802a-6d2a05e16dd0 | -15.06361 | -47.99004 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e5e0bba-a5d1-3a88-91d2-0a8c80059242 | -11.77286 | -50.55404 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 97fa8da1-1203-3b0a-9c13-d7cca2161500 | -12.10093 | -47.59863 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2064f857-961e-3b9a-b97f-962416e8dedf | -14.27275 | -45.03645 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8be69434-a840-3de8-9968-daaa4f3612c1 | -9.13746 | -40.24048 | 2025-09-13 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11cce097-74b4-356e-b059-0318f75d2aeb | -9.44641 | -46.40773 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db469f5-8521-3301-92ab-e0685659a219 | -10.34113 | -48.82263 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c1a8c5b-ac96-320a-94dc-f744c4c712e8 | -11.97798 | -46.65864 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7234192d-b99c-3b2c-ba56-d883b264ed67 | -12.8418 | -47.9469 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cdf3632-5abc-37df-9a65-f05abba41586 | -14.19049 | -46.27432 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 60521dde-7cf3-3180-bae1-dc73d52d763c | -10.74922 | -50.54449 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f125910-4902-3615-9850-3f182d6bd173 | -11.56032 | -50.57706 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1f008ce-11a1-30c9-9347-d2bba77acb9e | -12.11832 | -44.84415 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README50.md)
