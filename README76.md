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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7941df37-6f45-3744-beaa-81a2feb7e164 | -10.76199 | -54.04327 | 2026-08-29 12:32:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8327fd05-4aef-38c2-b170-18286175aa61 | -6.97509 | -55.63842 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ae76b9bb-96f8-3044-bd26-48e005afcff5 | -6.75691 | -55.67309 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f05497e8-81b6-3faa-8676-f3e075fe22e0 | -11.17966 | -51.2763 | 2026-08-29 12:32:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c5aeb135-027f-3b31-a1c0-d5dce0d24726 | -6.77761 | -55.66532 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d8b87cf3-386b-3382-ba51-48fedbdd5c4c | -11.01637 | -49.65845 | 2026-08-29 12:32:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d2c8a41a-d135-3803-b4f9-1fd06a9da023 | -10.55655 | -59.61205 | 2026-08-29 12:32:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36380f8b-f6e6-3c3b-bf85-991d5a9ff8e1 | -6.76798 | -55.66382 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| f7b37bbd-f0ac-3f71-8910-027529549a31 | -6.75977 | -55.65177 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 863a9307-56ac-3a8c-8385-d0ad2e23ffc8 | -9.96344 | -53.93482 | 2026-08-29 12:32:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b353a0a8-6fd8-3639-8da9-18933fef6e04 | -6.78873 | -55.65588 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 595c68a6-de60-3b7e-a97a-b7d3dd09ab72 | -8.60056 | -54.79573 | 2026-08-29 12:32:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0c7a633b-4437-3e1c-a7c8-937208fc253a | -6.12716 | -57.82721 | 2026-08-29 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b4d54887-0360-37f4-a4b7-1a97eb1f70dc | -14.39995 | -50.06124 | 2026-08-29 12:32:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 78a4e31f-267d-3f1f-a58f-b88b52e06766 | -6.75268 | -55.67744 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 032f3d67-3cc4-384a-8a0b-1e936ee1d45b | -8.18284 | -54.93444 | 2026-08-29 12:32:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7bbf0f61-4c38-34f6-9a92-5bdac2901db8 | -9.25414 | -57.0774 | 2026-08-29 12:32:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 57ab7e06-08fe-304c-bff0-80f6c8a70415 | -8.66594 | -49.54176 | 2026-08-29 12:32:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8873fb10-e45a-31ac-bd84-63a479d54d2e | -10.81533 | -50.6436 | 2026-08-29 12:32:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 693e9c6d-2b6a-3de3-a793-d1517cf94e77 | -6.5756 | -56.53733 | 2026-08-29 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 40d78367-ac50-3425-afa3-429d35871d25 | -10.48763 | -64.50153 | 2026-08-29 12:32:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| dcd4ae25-559c-3c31-a7d2-7038b086731e | -12.52655 | -57.1864 | 2026-08-29 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb6a4e2a-b11e-363f-8f58-188129e8b4f2 | -7.34449 | -55.17203 | 2026-08-29 12:32:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4e8dac09-60b2-3356-8d8c-57035a58b470 | -7.57519 | -61.38639 | 2026-08-29 12:32:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2ca79963-6a3b-3a23-9c14-204ec94eb337 | -9.87521 | -60.29735 | 2026-08-29 12:32:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e1b7dea6-e4a9-3f1f-b03f-08754fa3782b | -6.75516 | -58.7212 | 2026-08-29 12:32:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| acb29358-68b0-3da1-a6b9-f98362d12434 | -9.6155 | -55.13129 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5f27e3c4-db15-3ad6-b7fc-899fd0ba1264 | -10.50757 | -59.62602 | 2026-08-29 12:32:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d2f1f610-066f-39c6-86aa-58a583a3cff7 | -11.04035 | -57.21797 | 2026-08-29 12:32:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 889ac737-d785-313e-8fd4-17fb24ccd49f | -9.97494 | -53.93625 | 2026-08-29 12:32:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3f4b70e9-bcb2-3f74-9887-843976355093 | -12.53205 | -57.18302 | 2026-08-29 12:32:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3155d206-c003-37a7-ad8d-22f96e3cc4bd | -8.95313 | -63.26126 | 2026-08-29 12:32:00 | TERRA_M-T | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| bdf5404f-c216-3521-a82d-9c9c01d11038 | -11.18152 | -51.28216 | 2026-08-29 12:32:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 90ae0335-35f4-39cf-b0fe-46c225df6b0e | -7.34606 | -55.16054 | 2026-08-29 12:32:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| da738e92-0699-3caf-9452-5a6bedbeba0f | -6.76943 | -55.65309 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 94e2f9fb-7bc3-3402-8c0e-ade872313aaa | -6.77907 | -55.65456 | 2026-08-29 12:32:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 6225c9d9-e194-3bc8-b5e0-4fadf44bb05d | -14.38869 | -50.06522 | 2026-08-29 12:32:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 9efa1977-f815-3269-981a-3bd40279c047 | -10.92635 | -56.41549 | 2026-08-29 12:32:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2d366dfc-0dea-3cb1-a5c3-c4c01e1a71fa | -14.92583 | -56.33682 | 2026-08-29 12:34:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6b02b977-088a-30da-aee5-99aeb55e0f63 | -14.46827 | -58.52638 | 2026-08-29 12:34:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ebc170b4-14bd-3c85-99fe-3b2148183aa2 | -14.47734 | -58.52769 | 2026-08-29 12:34:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d81c29b-2f8b-33c3-90a4-fd4f78f49438 | -21.00168 | -57.82645 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 3a083865-edb7-38b2-b10d-1ed8540a1bcc | -20.88456 | -57.70847 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| a1f587dd-6c24-3447-b03c-5cfd886731ae | -20.93073 | -57.56384 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| ba41e37e-0eba-3786-9ae5-ff1dfdc3b4da | -20.94985 | -57.57957 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 2ba8a2df-2fb4-348c-b66e-b25b8e2fb90d | -20.88612 | -57.69573 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 90a77789-3dbe-3076-b12f-3d8d77470bd2 | -20.93225 | -57.55079 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 56c755af-6801-324b-8305-66f9effe4c1c | -20.94106 | -57.56519 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 0e56cfdf-9428-3ac7-a4a6-e6cb3051b5e4 | -20.89636 | -57.69707 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d6c8f48a-eae5-30d5-8b4b-4d63987cd181 | -20.9426 | -57.55214 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| ce5d886f-e313-34ee-b125-405e4d8211e8 | -20.89479 | -57.70981 | 2026-08-29 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 29.4 |
| 4a8259cf-a8a8-37ca-9f4d-19224c10bdf6 | -6.6317 | -43.73 | 2026-08-29 12:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 360.4 |
| 98432627-c43f-3422-b63d-ad380478d2f4 | -10.8025 | -50.6539 | 2026-08-29 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 84de140d-5e3e-33d2-b0c3-96a79d4832f6 | -20.941 | -57.5694 | 2026-08-29 12:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| f3f0292c-f486-36bd-bf41-cd1b7357be9f | -11.2489 | -45.0732 | 2026-08-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 47fb6359-1c11-39f3-9c0d-da4dc1b62569 | -6.7885 | -55.6436 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e69dc9d9-d519-38d9-b727-b320c9b37351 | -11.7028 | -47.6129 | 2026-08-29 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 02d17050-d6e0-3b1c-b659-aeff980a7b86 | -6.7884 | -55.6635 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 6da3761f-edfb-36fd-b278-59ec34dd49ca | -9.971 | -53.9214 | 2026-08-29 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 4e00ae13-a842-3a3e-9169-5f37ca651298 | -12.2093 | -50.5386 | 2026-08-29 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ead2aed7-cbc0-3d51-bef3-3561801d9ed9 | -10.8804 | -50.4965 | 2026-08-29 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1547a928-3ce9-337b-80c0-eea5d866481b | -6.77 | -55.6445 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 03613e33-ae0b-3ead-996f-c9ca0ade9888 | -7.5137 | -55.3051 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| ea4bda98-fd13-3630-998d-169e94093101 | -9.9708 | -53.9419 | 2026-08-29 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 8073a6be-3fa2-3b97-8c5b-f4a1f26dff06 | -11.211 | -45.0555 | 2026-08-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 910d889f-1c68-368c-aaaa-d1d4acde9c0b | -13.3254 | -46.9333 | 2026-08-29 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 65ab771e-2373-3d0a-a67b-25e1a0c37f5e | -10.8215 | -50.6519 | 2026-08-29 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 63de02b1-68fc-3b85-83e8-175bc7686576 | -12.9027 | -45.8612 | 2026-08-29 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| bfbedcf3-432d-31df-9f0f-f7a38f92423a | -7.4952 | -55.3062 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 19d16cda-d761-3172-83cf-d7f31a44821c | -11.2298 | -45.0759 | 2026-08-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 42106bc9-c99e-3c12-98fa-67b6b4d336a5 | -11.2302 | -45.0528 | 2026-08-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 6fc725b1-1a17-3125-ac7d-e4f55bcf7d36 | -7.495 | -55.3262 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f6662b12-63ef-390e-874b-f7c1e1ba547b | -8.9428 | -63.2797 | 2026-08-29 12:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 08df2579-7b00-3492-937b-011194068d2f | -20.9414 | -57.5484 | 2026-08-29 12:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 997b6120-8e85-3d5e-a20b-3a04bf494289 | -12.2284 | -50.5363 | 2026-08-29 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c0a0c435-d6bc-30e7-81e0-4a0a4649d509 | -8.9613 | -63.279 | 2026-08-29 12:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 5861f940-452f-31a1-bde5-9f1b4399a850 | -6.7699 | -55.6644 | 2026-08-29 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 0de0f449-9dd3-3c80-a6cf-320e46cd66c0 | -12.9221 | -45.8582 | 2026-08-29 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| c54f6b40-8929-3a5f-90c1-b63fb24715de | -10.8235 | -50.5026 | 2026-08-29 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 813ae898-8e61-38a7-9fbd-3835a09f65a2 | -6.6129 | -43.7317 | 2026-08-29 12:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7a8be486-ee48-3287-a0da-f5740766b685 | -20.9414 | -57.5484 | 2026-08-29 12:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 9cbe2d6e-fd11-391c-990c-e1db16f6012d | -12.2284 | -50.5363 | 2026-08-29 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e4815b62-1c4a-3826-8b51-52b958ef207c | -6.7885 | -55.6436 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 656810d9-808d-3cf1-9477-a4aeb36e353b | -9.9708 | -53.9419 | 2026-08-29 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 1c5fcc82-2642-3247-8d7a-339fec5d7a28 | -7.4952 | -55.3062 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 60abee48-3cc7-35de-9bd7-263a530e8cf7 | -9.9896 | -53.9404 | 2026-08-29 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d09cd87e-e2a7-3f0a-84cd-7e244e0690d3 | -9.4728 | -45.6206 | 2026-08-29 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 19d88eb4-376e-384b-b7c2-ae73e909d95b | -6.77 | -55.6445 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 74105104-b780-398c-9dbf-aedd8f633cb3 | -12.2093 | -50.5386 | 2026-08-29 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fed5662e-c310-39a7-8394-c9acec58fda5 | -2.982 | -48.9598 | 2026-08-29 12:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f48e442a-a947-3436-a7aa-0fa7a277c801 | -20.941 | -57.5694 | 2026-08-29 12:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 3378a6f3-7dc4-3e0e-b4b4-684756cd6fd2 | -7.5137 | -55.3051 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 8fca86c1-e2f2-3ece-88a7-52313ecf752d | -9.971 | -53.9214 | 2026-08-29 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| d06621e8-c0ef-3c4c-a691-21d6b50f4d74 | -6.6317 | -43.73 | 2026-08-29 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 592.8 |
| d11c4a74-d1d2-3cfe-9abe-610f5e678aba | -6.7699 | -55.6644 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 0d165531-382e-3a69-968e-72c2c35fe1e0 | -7.9838 | -45.5072 | 2026-08-29 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 0916f558-50b1-3d61-b840-3650e66e196d | -6.6129 | -43.7317 | 2026-08-29 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 3e92030f-6df3-3949-b488-b752f8d3fb07 | -6.7884 | -55.6635 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| fb82d25e-3157-3dbc-a82d-f50339bc101c | -12.9027 | -45.8612 | 2026-08-29 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| addb662b-0868-3718-b5d1-b02750ad7eab | -12.9221 | -45.8582 | 2026-08-29 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 298.5 |


[Clique aqui para ver as próximas entradas](README77.md)
