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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6f33ded-6cd9-3d20-a4a1-f6dd2d8d4fb8 | -18.7472 | -46.93 | 2026-09-22 02:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| effc41dc-5a32-38d9-869f-9731510bb060 | -6.467 | -59.9902 | 2026-09-22 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dea182aa-7b60-3d4c-9bb1-f6d3478e89c0 | -5.7382 | -45.0853 | 2026-09-22 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 0ad44a5d-fc5a-3034-ae17-3b4bb815460f | -12.574 | -45.9576 | 2026-09-22 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6f887771-5658-384d-95d1-a0e75ac2e2f0 | -6.0928 | -57.6262 | 2026-09-22 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bc8eb4c8-4d3b-3726-b0df-8ab2c42f2583 | -9.2383 | -46.1668 | 2026-09-22 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 92f79574-74e0-3465-a362-f1b3a55ef431 | -9.2573 | -46.1647 | 2026-09-22 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| b2b2b38c-11cc-3fe3-8f2b-e01b9cf4e85a | -3.2211 | -53.9623 | 2026-09-22 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 255.0 |
| 261a7453-7e34-3450-ad3e-4b01be0ad85c | -11.3257 | -54.0282 | 2026-09-22 02:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| da6a2f1a-a429-36b9-a9a7-128b52a98378 | -9.4773 | -40.3116 | 2026-09-22 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 318.6 |
| 9198fb0d-d92d-3ee2-a856-ba2cefbe1893 | -10.6283 | -53.9885 | 2026-09-22 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2441f0f8-9a9f-38c5-a2fb-7e3e0cb6ec8a | -3.2212 | -53.9422 | 2026-09-22 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 353aa717-7116-38c5-baf3-930443434cab | -7.5889 | -57.6757 | 2026-09-22 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| db1043ef-ad11-3bf4-a42e-666aeb576749 | -3.2396 | -53.9417 | 2026-09-22 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 8d0239cb-0e6d-394f-8b9f-e94a24278ddc | -7.5704 | -57.6766 | 2026-09-22 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2a0a73cc-b6c0-346c-b760-95b6967133db | -2.8608 | -57.7994 | 2026-09-22 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 46c4a862-3a08-3109-9efa-35fe52fc50a7 | -10.5906 | -53.9918 | 2026-09-22 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f3da6aef-362a-38e2-82e0-ed394e2b3193 | -2.6669 | -54.9757 | 2026-09-22 02:30:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4436a24d-e1ed-3796-aabe-75001a7b155f | -3.2395 | -53.9618 | 2026-09-22 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 224.5 |
| 7ced781e-c6a2-3fdd-be4e-b0981e6535e1 | -6.0928 | -57.6262 | 2026-09-22 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b1758ab5-38a2-3168-8e16-d2302a00d008 | -6.6148 | -59.908 | 2026-09-22 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| d1dd1fe8-1b4c-372c-8b08-a4e21cca8502 | -5.7567 | -45.1067 | 2026-09-22 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2f2d14fc-0eef-3121-91be-a1290f1435ea | -3.2211 | -53.9623 | 2026-09-22 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8d63d374-2aab-3242-b645-b591cb515b07 | -3.2395 | -53.9618 | 2026-09-22 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 88e11f16-0369-32ea-8ff5-d3e3bd6aa2af | -10.6285 | -53.968 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| fd518773-28de-34c7-936d-2856a7da4dfe | -10.5908 | -53.9713 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1d2dca85-6922-384b-a5c4-af5d3007aa28 | -6.6331 | -59.9265 | 2026-09-22 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 174.5 |
| ef5d177b-73b1-3696-9ca2-1f53c8cb8daf | -7.5704 | -57.6766 | 2026-09-22 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e699693d-b18c-3824-981d-37219ca934a1 | -6.6515 | -59.9258 | 2026-09-22 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 80f2a98c-a38b-3102-a976-2864094f17bd | -2.6669 | -54.9558 | 2026-09-22 02:40:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f1c3d6c5-33ce-3125-b338-d083b5767295 | -9.4964 | -40.3088 | 2026-09-22 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 191.1 |
| 52f7f56c-eb26-3c91-b4f4-26cf7ca1a28e | -6.6516 | -59.9066 | 2026-09-22 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3fde97b0-2ef3-3ce9-9e6b-ff4c2dde1bff | -9.496 | -40.3337 | 2026-09-22 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.4 |
| f9c93a3c-3051-32a5-987c-08693c5042fa | -11.3257 | -54.0282 | 2026-09-22 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c6d228bf-93ea-382e-82f1-c6d993d1b746 | -5.7569 | -45.084 | 2026-09-22 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 212.0 |
| f3e36bc1-3239-3890-b671-4a8e135690f0 | -6.0925 | -57.6847 | 2026-09-22 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f3f71834-4714-3c0b-a5a0-1ee6aace7642 | -9.4769 | -40.3365 | 2026-09-22 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 163.7 |
| 7a9a12b0-a1df-3e7f-a04b-106ae37c673c | -5.7382 | -45.0853 | 2026-09-22 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3ebd6f26-564e-396c-86a6-9949ab5765b0 | -9.4773 | -40.3116 | 2026-09-22 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 318.7 |
| 6d0bdeb6-ba9c-31d1-afe8-4dc6cc313fab | -9.2573 | -46.1647 | 2026-09-22 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 57ff3d30-9de7-364d-867c-c0c7ae69db8b | -12.5547 | -45.9605 | 2026-09-22 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 38d5febc-cecf-3fc9-8260-80a3b84be5dc | -11.3255 | -54.0487 | 2026-09-22 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2ff722ed-0082-3a20-be2b-55b87cf0153a | -6.467 | -59.9902 | 2026-09-22 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 12f51734-e8ba-3f04-869d-ad040c4c456c | -18.727 | -46.9345 | 2026-09-22 02:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a7e22d25-401c-397d-a2ac-644df3ef53e0 | -10.5906 | -53.9918 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| acbbdfd3-ce38-3b52-bccb-34b62701bacb | -3.6946 | -60.5835 | 2026-09-22 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| da59af1d-c27f-3487-85be-0e391e8504d3 | -7.5889 | -57.6757 | 2026-09-22 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| cfa91121-362e-32ac-8cdb-316435a8fb85 | -9.4582 | -40.3143 | 2026-09-22 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 8c073b76-2198-3925-9e31-e7dab799b14f | -10.6097 | -53.9697 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| e724de4e-c87a-34bd-91c0-74c21571b538 | -3.2212 | -53.9422 | 2026-09-22 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 370c3c84-38fa-3dcb-a545-08e3672ae808 | -3.2396 | -53.9417 | 2026-09-22 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 232ad18f-07c7-3a0a-81c4-4aff7e579a4d | -7.6621 | -69.9215 | 2026-09-22 02:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| af2e0e0d-ba84-3626-b582-cd0faf03c004 | -12.574 | -45.9576 | 2026-09-22 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a800cd03-230f-3396-90e8-ed335804adda | -10.6283 | -53.9885 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 74bfd348-47a9-3c6b-a48e-2cef52b01b80 | -6.6146 | -59.9272 | 2026-09-22 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 174c14b7-7d2e-3b77-8880-945217a9ccc8 | -2.8608 | -57.7994 | 2026-09-22 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f1cc021f-2e5a-3ab0-bce1-b1ecc1d03e5a | -18.7472 | -46.93 | 2026-09-22 02:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8c99168d-8fcd-3902-b556-27bb7bd73763 | -6.0549 | -57.8227 | 2026-09-22 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c7de0965-7dc0-3ee7-9be0-629a685c2141 | -10.6094 | -53.9902 | 2026-09-22 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 946387bd-f144-3b67-aea7-cd77c6bb7e33 | -6.6332 | -59.9073 | 2026-09-22 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| cdf7a720-fbbd-3f77-bfba-e3c84cd71238 | -9.2383 | -46.1668 | 2026-09-22 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 25f486b6-9be9-3e00-aa8b-aa19e7a8bf88 | -6.6148 | -59.908 | 2026-09-22 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 25b533e2-249a-36f3-bf9c-60265b7dabe5 | -5.7569 | -45.084 | 2026-09-22 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| babeb3ef-b7b5-34eb-a321-0fb8e92ee0d0 | -6.6332 | -59.9073 | 2026-09-22 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a7fa35b5-61d7-3bd7-ace0-f2aad1d0a6ba | -3.2211 | -53.9623 | 2026-09-22 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5e1ae179-b62c-3f7f-8a96-2f6bec750a09 | -12.574 | -45.9576 | 2026-09-22 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6307ac9c-5ad6-325c-adbf-93629adfc03c | -6.6516 | -59.9066 | 2026-09-22 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cf9181aa-d3e9-3fca-a374-305628995216 | -10.6097 | -53.9697 | 2026-09-22 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| b644407c-ad8c-3fd2-bd2d-bd93ee6c5fb8 | -5.7382 | -45.0853 | 2026-09-22 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f7c43bb7-6010-3535-abaf-a18022044f0a | -12.5547 | -45.9605 | 2026-09-22 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 4dfc837e-2fc7-3f4a-91cb-4c53893f6d3f | -11.3257 | -54.0282 | 2026-09-22 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 97f2d174-27d3-3cb5-b015-71eda237a7a1 | -12.1458 | -47.3974 | 2026-09-22 02:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c33d1688-bb6e-3a97-b468-087e79d740c8 | -10.6094 | -53.9902 | 2026-09-22 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 0c9ffc13-8328-32e6-a069-f4510c34a0bc | -2.8608 | -57.7994 | 2026-09-22 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cad9af7b-3fa7-3b4a-9a7b-e3d43e712994 | -7.5889 | -57.6757 | 2026-09-22 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c149087d-b273-3de7-b418-56f605918664 | -11.3255 | -54.0487 | 2026-09-22 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 7515ee4f-07da-3462-90dd-e28f4c8d2d20 | -6.6515 | -59.9258 | 2026-09-22 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 7022088f-7ce6-31e8-963c-aa9cc1717963 | -3.2212 | -53.9422 | 2026-09-22 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 1bbb3825-2ff4-3702-a4a2-c73611dd4bf9 | -3.2395 | -53.9618 | 2026-09-22 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| f0646b92-9203-3d48-a401-b634b66ac428 | -6.6331 | -59.9265 | 2026-09-22 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 151.3 |
| c5a4a5ad-b667-3fd1-b403-be28e182f6c3 | -3.2396 | -53.9417 | 2026-09-22 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| d83f508f-eb1f-3700-a63f-6bb3edadd032 | -3.6804 | -42.9546 | 2026-09-22 02:50:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 45bdb1e4-8949-383f-84d2-ebeec05c4ca6 | -6.467 | -59.9902 | 2026-09-22 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6612b842-8227-3456-b980-48c80b6ecd9c | -18.7472 | -46.93 | 2026-09-22 02:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d68c37af-4e69-30ea-97d9-6b4adc7a72c6 | -6.6146 | -59.9272 | 2026-09-22 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| a25c5796-f467-3a22-af59-c0efa691146a | -11.3066 | -54.0505 | 2026-09-22 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 170b065b-4783-3bd6-8a7b-813f0cfc28aa | -9.5594 | -66.0359 | 2026-09-22 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 332c5f37-6a75-3eae-8b11-f31e3734ee51 | -10.5906 | -53.9918 | 2026-09-22 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3a5080ab-094e-3b2e-b0af-f1fd2d02e09b | -10.6283 | -53.9885 | 2026-09-22 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 378a70af-7059-3692-8750-99b739ace741 | -6.6332 | -59.9073 | 2026-09-22 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bb6a1a77-102b-33d9-8f82-cd33bd3776ec | -10.6097 | -53.9697 | 2026-09-22 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b131706b-3136-348d-a5d9-4ad75de33ba8 | -9.5594 | -66.0359 | 2026-09-22 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 24e73a14-cf6a-31ec-b8f6-3c550d43b0ae | -6.6146 | -59.9272 | 2026-09-22 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 83031109-b509-34df-b2a5-694fa6e60779 | -6.6148 | -59.908 | 2026-09-22 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0f188e47-6d74-3251-97d7-f484da97f12e | -12.574 | -45.9576 | 2026-09-22 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| cb508c71-22d5-305f-a91d-f472df11e358 | -6.6515 | -59.9258 | 2026-09-22 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 37596e38-d5c0-3255-9581-db2a0e8b0c91 | -6.467 | -59.9902 | 2026-09-22 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ddb1622e-c376-31cc-9fb1-c516a9c36042 | -11.3066 | -54.0505 | 2026-09-22 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 22d17621-135b-3ac5-8a5d-ba8cf9206ede | -11.3255 | -54.0487 | 2026-09-22 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| dafec8d1-3c70-3a39-b90e-5ae8c176e9c2 | -2.8608 | -57.7994 | 2026-09-22 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README26.md)
