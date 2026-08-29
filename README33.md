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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b12d64d3-cec0-333d-9276-da8c05ceeffd | -9.22833 | -51.56818 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4830dfa2-10ba-3e78-b6a2-3db3bc054782 | -6.17655 | -45.91998 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50e110ae-c423-32ab-804e-0d6cb59f2a1e | -9.46285 | -51.59111 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 750ad427-2377-3f28-88ef-2c1116297e85 | -7.53049 | -44.45214 | 2026-08-29 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a24aa10-e74e-36ea-9855-51d2fc92b004 | -5.94606 | -44.77815 | 2026-08-29 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af0fbc6-8553-3b25-8687-b1e0d552948c | -9.42419 | -51.68382 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cfef61e-ba23-3db6-9370-8f78d958eabf | -9.43141 | -51.69378 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 847e04fe-5d59-3b8a-99fd-12e6991018b7 | -6.49085 | -49.90793 | 2026-08-29 04:32:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13cbc26b-5b6b-319f-a17f-e96b5044f3ba | -7.28871 | -49.95975 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fcc5725-836b-3e53-9641-d4aa680b6f03 | -7.27014 | -45.34894 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1f33144-334d-3b36-ae64-51db9fe1b440 | -10.75693 | -42.10584 | 2026-08-29 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d08cc8c-4f01-3bf1-8c85-c452883c4b1a | -5.86872 | -43.5254 | 2026-08-29 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a23cbe5-d928-3f18-b67e-e6b70c923961 | -10.32522 | -49.9622 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 462633c3-4f9c-3f55-93b8-1775cea160e5 | -7.49657 | -55.2974 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f4c9807-13c3-31e8-810d-2f43ef87f3dc | -9.45925 | -51.5862 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45730cfe-d147-3457-aa75-b5f6ed26c060 | -11.25711 | -45.05445 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01269051-d7f4-3917-bcbc-777a1f977cb5 | -8.59434 | -54.82746 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74d2f3df-9576-33e8-b52e-5d4c516b8a20 | -9.21047 | -51.54295 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e9a06ab-139c-3809-a2ba-38168ed7effb | -10.86017 | -44.80175 | 2026-08-29 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72eb551d-9e75-3dc6-9cdf-fd205e2c95c9 | -6.78152 | -55.69077 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f889d9b2-5153-3a27-b40c-d5113d73c091 | -9.42676 | -51.59354 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37216993-e896-3367-b979-a6ccfc364708 | -8.16319 | -46.17265 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a20571f-20bb-3bbb-b608-d68108b64924 | -4.84837 | -45.40031 | 2026-08-29 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f969e748-cd7d-3de5-a773-6e6b2e6734a0 | -6.1629 | -57.78365 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d96a98-9186-30b0-9e3b-0f4f2f391c28 | -9.15986 | -49.97824 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dd0554d-dbb0-3900-be26-c0018a699cf5 | -3.16139 | -54.6259 | 2026-08-29 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c678078-b5c9-3273-9721-8e0b316f01b9 | -7.07933 | -42.21371 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa525e2f-65a5-35d1-9995-14de2f53e301 | -6.5762 | -56.54869 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07e8dfcc-2b7c-39c1-a320-feb5d4a9cf93 | -11.35726 | -45.15131 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4adbfb82-b0c7-3463-939c-a5603aa12c9c | -6.15954 | -57.80165 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eedfe4d4-fcd1-3a12-bffe-a5d8c5cc840a | -6.74629 | -52.44918 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d66a5c-a158-3b2b-bdaa-c1c153eb361e | -9.15595 | -49.97756 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85f3fc0d-62fe-3e5d-a353-d69a19d0db55 | -7.29086 | -49.97182 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9cd3ec-d40f-37cf-8de5-5b8aeb10e60d | -8.5993 | -54.77121 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 479da3d8-3bb5-3567-a8ac-e32221bc99b1 | -5.89062 | -57.76223 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5dbef186-0989-3633-b262-6d82800284a2 | -8.60306 | -54.77591 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dc78daa-28ad-354f-b776-a2c483fa27c9 | -6.34183 | -44.09369 | 2026-08-29 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a99a1c2-7951-362b-b2ab-72371f8673cb | -5.809 | -43.79837 | 2026-08-29 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d45b54c5-cca8-3ee9-852e-a9a96ae2274e | -5.36709 | -50.56808 | 2026-08-29 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ea11af0-8690-3c28-bf2a-ba02a540f94e | -8.66551 | -49.54444 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53b34ed-f55b-337e-816d-959a83376947 | -6.54643 | -55.24589 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84ff49a1-fc61-3247-b210-10d813c90bf0 | -7.28399 | -45.85357 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6861e981-f3bb-3886-9382-d7209d9f8ba8 | -9.22676 | -51.57705 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521ee196-3c9c-3f96-b607-646858ed3a3a | -5.34411 | -45.1596 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc27d2b5-2db9-38e1-99c9-fc7bc325d990 | -8.668 | -49.54263 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3de6f606-e623-30ea-9606-87bedd3e06e4 | -7.21305 | -42.75165 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d8b679a-251c-3706-9e5d-d886a56eba13 | -11.24041 | -45.07374 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a168cbe-18e8-3f70-9595-511a8162cda1 | -3.43038 | -52.77528 | 2026-08-29 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0084952-d66d-3c27-946f-77a1f979cbc9 | -6.7569 | -46.13679 | 2026-08-29 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3fbff1e-f347-3386-b29d-a254a130a907 | -9.27099 | -45.64151 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 643bea24-5594-38e8-ac6d-665b85c09fb4 | -10.75321 | -42.10528 | 2026-08-29 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 073d3164-2a0d-31bf-8f25-457e2f3f8248 | -6.1754 | -45.92713 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2a295bf-2db0-3d40-8631-acd717a002cd | -8.66468 | -49.54921 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| dd8a94de-ae38-3b17-8d74-def2654dc8ad | -6.01487 | -45.81371 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8a6901-5ad4-38ae-80ac-3b1e5990e8b7 | -7.34898 | -55.1626 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5167b7fa-4fde-38fa-a704-960d299008c0 | -7.50155 | -55.30254 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0a75257a-f072-348e-877e-55fe5b5a3310 | -9.42553 | -51.70167 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5af4dca2-5908-304b-852c-2b336748c275 | -11.38396 | -45.13374 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4da3752-721d-349e-9d34-ff3ba2f3c825 | -8.80045 | -50.49266 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a9c89617-ee0b-38e1-9400-194abed3e0b5 | -6.56991 | -56.54753 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39a4a281-81d6-3272-ba57-541618014b82 | -5.41494 | -43.18835 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1121dbb6-ad35-36a0-aef3-faa0026c10c3 | -7.25498 | -45.86335 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 677c3eaa-8017-3631-b01b-6a09661bedd6 | -8.28333 | -39.97533 | 2026-08-29 04:32:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8e7988bf-bbcb-37de-92ca-06ba5bc504fd | -8.60368 | -54.77245 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc986c44-88cb-33c0-8019-b611eeade786 | -6.57318 | -56.54713 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5567530-86f1-37ae-bea9-5ff9dc0032e4 | -7.13016 | -42.77102 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 799fe29e-327b-3246-8c9c-8beaec4366d6 | -6.62447 | -43.73676 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 79a31507-e99f-318a-9b37-82d716bf89b3 | -8.66337 | -49.54674 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 65a22dad-e7c1-34c1-9906-c538a47811bb | -7.508 | -55.29959 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8de43173-7d73-3f34-91b1-56b2aaf4729c | -6.90628 | -43.64923 | 2026-08-29 04:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a96b718-1416-3478-86ef-2e323184c74a | -4.17053 | -42.43997 | 2026-08-29 04:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4b6e4d8-378c-3b3c-be8e-7f2e5e3754e5 | -6.54716 | -55.24186 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20d508e-fdd3-34bf-92c5-d835be96a869 | -6.48746 | -49.9033 | 2026-08-29 04:32:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84586cd6-3998-351e-9f35-d81fcac26900 | -7.06109 | -42.19035 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e69c0913-229e-3b3d-901f-5ea77baec025 | -8.94646 | -50.80452 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7e02753-f7e6-3728-857d-9fea0a410016 | -5.47564 | -45.11948 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80f636e2-e5cc-3895-9bfd-967fd02ac85b | -11.37283 | -45.13925 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 438f3412-ed85-39ce-8f14-a9fd0ef2f629 | -7.51296 | -55.30488 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0355c27c-1ed1-34d0-a6ea-fe2f8990b422 | -5.82952 | -49.19255 | 2026-08-29 04:32:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f212bebf-41ec-3b46-ba18-91d332f4b0c5 | -5.882 | -57.76755 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d41eb13-9db8-3e45-b6da-5d7da2cd68bc | -6.90291 | -43.64871 | 2026-08-29 04:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f67cc94f-4938-3762-8192-8f5632455b42 | -6.92834 | -42.67829 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e2997fcf-7a13-35a3-be80-f49fb88a00a9 | -5.22496 | -52.01844 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d6133d-d188-3d5b-a4f9-14136ca22f9f | -6.76407 | -55.65197 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3c7e31a-a590-3111-a8ce-e784b0dd8c25 | -11.3606 | -45.15184 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70b0ea99-940d-3cdd-a7f0-82670c903cd5 | -6.37157 | -54.95989 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d506d5-2809-386a-9f39-c1a84abb4aa1 | -5.89232 | -57.74971 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e8119a92-87f9-3773-a679-9fc4aef5ace2 | -6.74534 | -52.45448 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 856d93a3-b2e7-3bf0-8fb8-5073b7c24d1e | -7.34244 | -55.1661 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 360429d0-f8f5-3f3b-a9e7-0143fe3c826e | -5.31173 | -47.04836 | 2026-08-29 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89628c57-2dcd-3efb-8f4d-21bb7d4e2fdc | -6.53991 | -55.24886 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a16ee53-31ee-3dc3-81a3-02269e5332dc | -7.34741 | -55.16434 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d76a5331-2ee2-30da-bc3b-ccc4dfb2c9e0 | -6.42276 | -55.52626 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0960a9-0889-3c93-a8b1-d6b44d3908b4 | -6.95095 | -45.22618 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3263434f-781e-3b51-ba93-9b1884868ef2 | -4.56694 | -44.06367 | 2026-08-29 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f458ee55-b1db-3adb-8989-5df3cfca938e | -6.42866 | -55.52735 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d18d9001-ac10-3c8a-bc27-54e5e98645a8 | -6.16652 | -53.48303 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0692369-37e3-3478-908a-6de997daf3da | -7.20499 | -42.73463 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 571cb536-6536-3f94-9080-26f41e828b20 | -7.34814 | -55.16028 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b3b73e1-15c0-3411-889b-594bb36ba934 | -10.76088 | -54.04406 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README34.md)
