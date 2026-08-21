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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 939514b6-8ff9-31ab-914b-18a43f40f584 | -6.4336 | -52.7578 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c76bd462-fe55-30cb-a10a-3ee0a0af776a | -10.80614 | -50.27579 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6af226dd-4fba-32c8-b3cd-07c6ac09ace4 | -12.75118 | -48.45811 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8d25c9df-6b41-34e5-bd71-a0962d9a5933 | -6.16819 | -55.44358 | 2026-08-21 07:03:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 613143ab-4454-3b9e-ba6e-dfe6835fa80e | -6.66345 | -56.34468 | 2026-08-21 07:03:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| faa3f349-7a26-3ec4-a44d-9c809d3250eb | -12.79116 | -48.4006 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 986ebf22-98e8-3f65-85c0-22b44f7e44ce | -6.87503 | -59.41534 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 71d6fead-3b5e-32f4-943c-bec0c0ef3e8d | -10.77158 | -50.2991 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 5c68bc05-370d-3284-b3d4-03cc981cc414 | -6.8619 | -59.41306 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 64c75263-db34-31da-bedf-6017c1dcec00 | -8.57652 | -54.77572 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dbb791e8-cb32-36d3-8953-a48d4afffce9 | -6.87145 | -59.43655 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 97ca6a4a-df18-3541-91ad-c074b9661b88 | -6.38285 | -54.94421 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0dea72a8-78c0-3e6d-866b-f2bb83ca2ad9 | -8.17163 | -54.99782 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 589119be-3317-368e-9172-bc61015e235e | -8.58103 | -54.74685 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 73b14f5d-5c99-3cb5-b9b9-dd817990c66b | -9.44428 | -51.61313 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed5fc493-9d77-37dd-ae3d-74cf289c4455 | -9.40484 | -60.41705 | 2026-08-21 07:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 198.1 |
| 5d909aa2-3b34-3bcf-bb1b-881b1c27a229 | -6.86061 | -59.42942 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7d74396d-cb2d-3807-80a0-b4df1922b5fd | -8.08943 | -51.65914 | 2026-08-21 07:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c8b209e9-6246-3296-b5fb-bbf8e456d04e | -9.21543 | -59.76009 | 2026-08-21 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 83e5b7f1-4d02-3b7f-9225-538a9ddeef2e | -10.76172 | -50.29771 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| db7394a2-5d88-339c-a3bf-459aef42f53d | -8.08809 | -51.66827 | 2026-08-21 07:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8c3578c2-c689-3cf1-9d18-a20999a99826 | -11.17441 | -54.01068 | 2026-08-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e252123f-fedd-3735-ac4a-14c7440eddc6 | -9.44565 | -51.60381 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a4f277e9-196e-3280-8b3f-a4fea95c14b7 | -10.77182 | -50.30577 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cf834779-6870-3ee5-bdb2-f104b490cc77 | -12.80316 | -48.40022 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| d2cbb5af-1486-32d3-9c68-78b39894e95a | -7.36171 | -45.80466 | 2026-08-21 07:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 72cfa904-e822-3eaa-9b30-463410d92983 | -8.59015 | -54.74826 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 73b95f7e-4770-3b8d-a1f5-c4ddaee9a7e9 | -8.5192 | -55.32463 | 2026-08-21 07:03:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a5f2e2ac-f4b3-3703-9b9a-613bc0b72efe | -11.17167 | -54.02853 | 2026-08-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 371ff325-c203-3a84-9cda-fc784ffef505 | -8.51762 | -55.3348 | 2026-08-21 07:03:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b43792a9-ca6c-327a-825c-edfc9b2aced5 | -9.40882 | -60.394 | 2026-08-21 07:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 37baf644-11a3-3ff2-a461-dd4782a46394 | -10.80774 | -50.26437 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 07b2d78e-e079-3e49-95d8-ab04779e52f6 | -8.59164 | -54.73872 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 868477fe-dbea-3452-8e66-cca0ad6d44cc | -12.00328 | -53.42296 | 2026-08-21 07:03:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a526bdb4-a3d7-34e2-9b68-99626f10e4fa | -6.22562 | -55.60717 | 2026-08-21 07:03:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| c0d9e1e8-dded-3fc0-84f8-307d6b8735ae | -6.82459 | -59.40171 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 57f792ae-79f1-3f48-a540-4f36ce229ead | -7.37053 | -45.81316 | 2026-08-21 07:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 3ff48273-cc06-3d8a-a8ff-976d08656645 | -6.85829 | -59.43434 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| dcdba6ea-a78d-323c-aa6b-9c678ad315a8 | -9.40084 | -60.44016 | 2026-08-21 07:03:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 54e7f659-5d68-3aec-a6ed-7b35903f6e89 | -7.25639 | -49.89346 | 2026-08-21 07:03:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 93ede476-7ce5-3f4a-aabd-2decd8654b22 | -11.17305 | -54.0196 | 2026-08-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d8ee0090-0b70-3da4-9cad-3b80f9c6c1a6 | -9.39266 | -55.98529 | 2026-08-21 07:03:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f3ecc5c0-d00f-34fc-be67-94b04df60c48 | -6.22383 | -55.61854 | 2026-08-21 07:03:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| da9886ae-ebee-3b6d-b220-74d8606ca6c8 | -12.72583 | -48.47006 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c15b77fc-4927-3413-bb71-85d009f214a5 | -10.52287 | -50.77233 | 2026-08-21 07:03:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 78b74240-7bb0-3f0d-b9aa-ff1fbfe8e4f2 | -9.44293 | -51.62234 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 491929db-e382-3b3e-bb35-1b7e6d742cc3 | -7.24677 | -49.89206 | 2026-08-21 07:03:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 491d6bee-6fa4-3a32-8f01-066a28f65013 | -9.21259 | -59.7757 | 2026-08-21 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 44f49ed1-5a08-39d7-9175-dac0cadf20c8 | -6.88817 | -59.41756 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 92ae37ce-7f69-3c3d-aeda-ebbdc1fcbb51 | -6.37767 | -54.94717 | 2026-08-21 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 818ca805-2f42-3d6d-a192-332e32f7601a | -7.35727 | -45.81137 | 2026-08-21 07:03:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8a713987-8d72-35e5-8913-c0bbca152105 | -10.79626 | -50.27442 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1de8feb3-5050-3902-952c-093b69737f74 | -8.89574 | -60.5368 | 2026-08-21 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5efe059d-1a25-3e6f-906d-8f0bb6ac1260 | -11.16426 | -54.01823 | 2026-08-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 53a1e38b-2b75-30a9-9439-f96b78bea9e8 | -6.4275 | -52.73897 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6828e2b2-63d7-3b27-b17c-29552e0bfdd1 | -10.51824 | -50.77573 | 2026-08-21 07:03:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3f599e98-fb81-3703-a857-c05b56ec02fd | -6.88462 | -59.43874 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 62ba22fa-4004-321e-a11c-ac40ca77ab2c | -12.49351 | -54.75257 | 2026-08-21 07:03:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3dc4ca74-5a1f-3f6b-9c06-4915035a4850 | -10.77338 | -50.29441 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 2d3d67d0-1677-3f66-984b-f183e8019a05 | -10.81723 | -50.99246 | 2026-08-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 33779878-0c64-377b-adfb-a965ba5037a5 | -6.87376 | -59.43171 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9f6e79db-2d30-3f1a-a85a-de3cb879f478 | -8.37805 | -62.70006 | 2026-08-21 07:03:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7c3ade6b-7f61-38c4-9865-996e8c9ba188 | -10.7601 | -50.30906 | 2026-08-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 892fab71-e1c3-3455-950d-5f5c2b98de65 | -12.80096 | -48.41747 | 2026-08-21 07:03:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fbfb239e-e86b-38fc-a983-3a23c308d024 | -6.69225 | -58.92758 | 2026-08-21 07:03:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 80396fe7-d17b-3ddc-a16b-0e2c1f33b021 | -8.38195 | -62.70855 | 2026-08-21 07:03:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 6d6ae84b-fa93-361a-a6dc-0f9780e99751 | -7.25483 | -49.90438 | 2026-08-21 07:03:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 26e7294c-e70e-3342-a906-ebbb576d82f8 | -12.00194 | -53.43188 | 2026-08-21 07:03:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 37518295-5c25-31bf-8c1c-c85282ccd959 | -13.39202 | -54.37657 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| de177b30-7e3b-3cce-a046-12db3aa0e6f5 | -14.57051 | -52.99083 | 2026-08-21 07:05:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d91772d-13b0-3042-9eba-d05a4225a469 | -13.40216 | -54.36896 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 30167bbf-39bc-32fc-ad2c-1d15fa5dd330 | -14.31412 | -51.88728 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 469b698a-4040-306e-9531-ffec44be61ac | -13.43869 | -51.80901 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7921c649-de33-3433-8996-c4aa6145c0e5 | -13.37309 | -54.3828 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 5891cdb8-fcde-3fb1-9f39-6632747fdaf7 | -13.38324 | -54.3752 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 63d31a14-f3ae-328d-9c53-07361a959ad8 | -13.38187 | -54.38418 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 13b03543-3a46-3464-898e-dd42ce40143c | -13.38461 | -54.36622 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 741978a4-8f83-3641-b878-9d3673f1408b | -14.31264 | -51.89762 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6e4f5f0d-ac51-39e0-a4b1-042f905b139e | -14.01534 | -53.68396 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 23d16339-5888-3e0d-96ca-5423f57c0687 | -14.32201 | -51.89903 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cec6a06e-8872-3dfd-8be8-306284c33425 | -14.30621 | -51.87553 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d49368fb-75e1-32c1-86a2-3a3db716c71e | -13.43081 | -51.79731 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| afab8dcb-712b-33a6-bb17-e6650f2c23c9 | -13.37583 | -54.36485 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| fd5d4db1-84c8-3f26-84cb-8f8bd9319b34 | -13.67336 | -48.76127 | 2026-08-21 07:05:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9ffc4300-84b5-3f11-9dfd-bcb0d3472b4d | -13.93334 | -53.8582 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d281c94e-88cc-35d6-95aa-46950097a24b | -13.37446 | -54.37383 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6430d069-951f-38f7-8c43-03d736ff0b37 | -13.43225 | -51.78702 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 425cd1c9-a326-3c29-8e67-b53b804c7541 | -13.66376 | -51.79097 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 82fb0bc3-f6da-3676-99ef-869c29aee5c9 | -13.45381 | -51.76929 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 724c74b8-613e-3670-8bc0-5649f5ea65d1 | -13.39338 | -54.36759 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 9dda7364-f68c-3e96-89ac-9854f2f52770 | -13.73747 | -51.85027 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4a9749c7-ecd3-39fc-bab4-fde0ee6be470 | -14.30474 | -51.88589 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 582082c4-bcd5-3af9-8695-6e1a70f33515 | -13.42937 | -51.80764 | 2026-08-21 07:05:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aee1dd1a-6a75-3429-af53-042921e37832 | -14.30327 | -51.89622 | 2026-08-21 07:05:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c6db5849-04ba-3e33-92d2-704538a84781 | -13.39065 | -54.38556 | 2026-08-21 07:05:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 113f09cf-4537-35bf-8e26-9fba755c0a46 | -7.3603 | -45.8136 | 2026-08-21 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f2e24f1b-7d5e-3c5f-9a99-f1a3706d37d3 | -9.4069 | -60.4362 | 2026-08-21 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 289c4d53-94cd-3ca9-8403-f710b04b3203 | -6.8755 | -59.4364 | 2026-08-21 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f02fcb25-a06e-3585-88d6-ead5f56982b6 | -9.4257 | -60.416 | 2026-08-21 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 13aa8d25-33a6-3be9-9c59-dc335a85abab | -9.4071 | -60.417 | 2026-08-21 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |


[Clique aqui para ver as próximas entradas](README87.md)
