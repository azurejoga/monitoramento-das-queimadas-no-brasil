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
| 04aad8d2-5d64-3495-b458-400c6101524e | -8.85736 | -62.21489 | 2026-07-05 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 054acb1c-21d3-3189-85f0-925a18fd5041 | -11.8419 | -49.19647 | 2026-07-05 05:04:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521874e9-b239-3769-b4a7-e5a0ba41da91 | -11.43091 | -46.58644 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbae5430-157f-37e0-b044-dc02d2e1f4f2 | -11.88621 | -43.83356 | 2026-07-05 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acb24acd-b8a9-38ad-bba2-15e322b3ad1f | -10.83149 | -48.76743 | 2026-07-05 05:04:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d7947ec-f441-302a-8594-5d9930b512fd | -10.1998 | -54.95131 | 2026-07-05 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c459d34d-d877-3414-b6b0-9c736a5c1bf5 | -10.94226 | -43.04101 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9b1b477-ab01-32c5-a18e-6c4dc3d7c485 | -11.44316 | -46.60327 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ffa912ba-3c5f-321f-b979-0a71b4265db8 | -11.66094 | -46.75346 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff734662-84ca-3ecc-9ca5-1f0f32814a34 | -11.31005 | -54.47392 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10fd5125-1759-3341-bd08-dbfa3690fb06 | -13.19832 | -54.30465 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 137c6e03-d71b-3de5-9f48-06f11b0527ed | -11.43565 | -46.58704 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75028ec8-6563-33ee-bd4b-c138fc842b7b | -10.55681 | -48.02957 | 2026-07-05 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 336b3aa3-f60f-32df-918f-8bdf6bf9e3e7 | -11.35756 | -62.44561 | 2026-07-05 05:04:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90f0a9a5-1ca2-3ab3-bff3-5308403fa3d5 | -10.92927 | -43.04823 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 78b7771d-6adb-358f-9aa1-a61e93255943 | -10.93086 | -43.03515 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dbfc6943-0ca1-397a-a901-a2b4a497bfd3 | -13.23881 | -54.32191 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3627472e-3c3a-38b8-9b91-ec32f9700f2a | -13.2338 | -54.332 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 565858f4-c4ae-33bf-9c2c-5010847926ce | -10.78634 | -54.10667 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43456bcb-397b-3b1b-995b-2d1780c32267 | -13.22715 | -54.3309 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52e009c-698b-3c5d-bc00-9309d7fc4a6b | -10.97202 | -48.13126 | 2026-07-05 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04e88b8d-9e07-38c4-8b05-08d173a41412 | -14.04354 | -53.86825 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2cd54ea-bda5-3a12-911a-5ae8a7226a10 | -11.5226 | -46.47935 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da3d789-d825-3aff-984a-8b494c466a4f | -10.97258 | -48.12732 | 2026-07-05 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ce60227-085e-3de6-8b8f-56a2376387cd | -10.20316 | -54.95187 | 2026-07-05 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6df3f262-913f-31f2-8e36-87a97790680a | -13.21661 | -54.3328 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f214ba9f-c049-3b14-a560-97dc4a241ab8 | -13.21774 | -54.32571 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ac77098-c8e4-387b-972e-724c3d3c38e0 | -13.22763 | -54.37098 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7bfd0c-fddc-385e-81a7-a32e0a5e6d77 | -11.00863 | -55.2438 | 2026-07-05 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db1b114b-9502-3d81-a71d-070d737bccce | -8.60958 | -63.83877 | 2026-07-05 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a660b607-75cc-318e-8213-4525e5d527a7 | -11.84264 | -49.19119 | 2026-07-05 05:04:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f39f328f-8bea-3bce-80b9-37883fd305f7 | -13.21161 | -54.34288 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893aca37-2d92-3c8f-b675-a39b4cb359c4 | -11.6689 | -50.38763 | 2026-07-05 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c50ae213-2531-35cc-829e-1c8b49a6c93b | -10.90603 | -56.85748 | 2026-07-05 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd24d6c-8e88-3b8d-ad76-d8ebacba18da | -11.88547 | -43.83528 | 2026-07-05 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d5a6697-e55d-37fc-94fd-922ea9f108d2 | -8.85794 | -62.21177 | 2026-07-05 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d19054b-f98e-3c98-94ca-e6958072331d | -11.67132 | -50.39714 | 2026-07-05 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2388b36f-4380-301c-b67e-bc821cf451d8 | -11.88597 | -43.83134 | 2026-07-05 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48b5c0d5-da8b-3d70-aff8-cb2a682f115f | -10.1208 | -52.08803 | 2026-07-05 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1abde790-c2ae-3e31-b7c2-ad9f806c258c | -10.94173 | -43.04539 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 40de3f2f-a0b5-36b1-a348-5304badd9faf | -10.93576 | -43.04464 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6d7ca3db-dd81-379a-8dd9-81a913db1443 | -8.61541 | -63.84152 | 2026-07-05 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21bf55bf-75fc-3d3a-927d-9eebf9a18e78 | -14.41684 | -44.59365 | 2026-07-05 05:04:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8a4d51-6f1a-38dd-8252-5a489428f6e4 | -10.93033 | -43.03953 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cb84c693-b1b7-350c-94f3-391fc2a536d6 | -13.21217 | -54.33934 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02133e73-77d4-337a-869c-53f163d72565 | -13.2316 | -54.32436 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1d8b2e-92ce-32ac-b8fa-590ae9ed5a96 | -11.52187 | -46.48052 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31c4cd60-90f7-3dd8-adec-10f39d60c148 | -13.23216 | -54.32082 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f381d2da-a081-3567-be83-ade62ab53f33 | -10.65286 | -49.72081 | 2026-07-05 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca7d97c-db7c-3d60-b642-7a9ef2ec5d4b | -13.2183 | -54.32217 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae7b55a7-730d-38d6-91f1-21a46cd097e8 | -11.89194 | -43.83434 | 2026-07-05 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5efa9f4c-a5e6-3da3-936f-86d01c0196e8 | -10.89956 | -56.85206 | 2026-07-05 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8317764a-f7b9-3435-96ba-98e319b506d0 | -13.2205 | -54.3298 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4162d1e-5998-3211-b40c-70a30f0cfab9 | -11.52741 | -46.47974 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0affeb8-ede7-3185-b202-f3c3021f5dcc | -17.00954 | -48.28402 | 2026-07-05 05:04:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ad87ef-5cde-35cc-8b08-b80547df828d | -10.62307 | -53.90043 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0962c90e-2e86-378b-8374-9d65d3ecf7a7 | -10.93523 | -43.049 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 97d05bfc-b3a6-3740-ba55-ca502f26f963 | -8.60963 | -63.8403 | 2026-07-05 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4896fde0-79b0-3fa2-b292-4ec1833b448f | -10.4969 | -57.6106 | 2026-07-05 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32bb8663-da2d-3c26-9a71-444eb8277cf3 | -10.9298 | -43.04388 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 0b882bd4-e522-3906-befb-4f21bead6799 | -11.91583 | -43.3824 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 351eea0c-ff14-39e7-893f-6d4c5544f243 | -11.35492 | -62.44872 | 2026-07-05 05:04:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b87f9078-f9de-3c19-aa88-25aa4cff2d5c | -13.24822 | -54.3271 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb0472f-2c65-362d-a674-4e730b721eed | -11.67197 | -50.39266 | 2026-07-05 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52381002-5c31-35aa-b909-08110ae28bc1 | -11.91828 | -43.3852 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bf8db62-0561-3721-8e66-82042c11a54f | -13.23825 | -54.32545 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1778855c-6508-3eac-9cc9-04297ba1a256 | -11.92473 | -43.38156 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8f158d4-600b-3f6f-b3d1-82f298585c91 | -8.86199 | -62.21893 | 2026-07-05 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c189c75a-a9e9-3bec-b2b0-342aef9a0781 | -11.32004 | -54.47556 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d0123f6-e79e-3b7e-861b-8cb372fc86db | -9.36271 | -65.74374 | 2026-07-05 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da0cf530-7ce9-36fd-b868-3305c5b798a4 | -13.21549 | -54.33989 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ff10b91-91c1-332e-84b3-e8d00afefad0 | -13.24213 | -54.32246 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c46c7e02-0924-3abd-94eb-e87780650c7f | -11.54568 | -48.26261 | 2026-07-05 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43b3f6a4-4e96-36cb-b048-79a7fbc65300 | -11.01201 | -55.24435 | 2026-07-05 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21692d0e-4196-37e5-bf76-b8b8ccda76c0 | -11.35198 | -62.44753 | 2026-07-05 05:04:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8969ffc-3b09-3c53-a124-68bfcf0fc5cc | -12.16981 | -54.53532 | 2026-07-05 05:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f2766da-1689-38a0-8212-18fd3ee8d24c | -13.21718 | -54.32926 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2de0e807-56a6-3c7d-bbe6-7f6ef309cef2 | -11.92126 | -43.38721 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e254be9-f0ab-36d5-8473-f828e5af73f0 | -13.22106 | -54.32626 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b647ff1-0389-3e1c-9858-f06ce1d81166 | -13.25599 | -54.32111 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c374a2b9-aa52-3af5-842e-680e5b88f1b5 | -13.23104 | -54.3279 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae36758f-827f-370e-b491-77932157b240 | -11.32061 | -54.47203 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d449a135-13dc-3a94-8b87-75d6180f84fd | -11.9188 | -43.38101 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fc2fc30-d455-391f-a107-bd5023e3dbe5 | -11.43846 | -46.60238 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 11a90d96-fad6-3b28-9dcc-7a45694fdafe | -13.21938 | -54.33689 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a644c2a4-b659-326a-87cd-3d0bab0b898f | -13.19499 | -54.3041 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c7bbc6d-92b5-364e-93f9-5ee2ae9b72dc | -11.92176 | -43.38295 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea7dfab0-1d28-3a97-bb5b-624289c92641 | -13.23492 | -54.32491 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3663bac0-a485-3e97-b774-df98c1de1fc2 | -12.16925 | -54.53886 | 2026-07-05 05:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 764032c7-4473-34d9-a8dc-078ae55127bf | -11.43976 | -46.5925 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a868db3-a8ac-3da9-8cec-d81e375f45be | -10.94119 | -43.04977 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b9a07ad3-7520-3255-adcd-4fa470eb38a3 | -8.61536 | -63.83997 | 2026-07-05 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fbe3a55-dcc6-311b-b950-8a2d14871c0a | -10.90176 | -56.861 | 2026-07-05 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3169d075-f26d-3d38-a659-899b061320ef | -17.00497 | -48.28337 | 2026-07-05 05:04:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b95eb95-a97b-3e15-b345-6076068e6898 | -13.21994 | -54.33335 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c42765e-b41b-3dd4-ad49-4986d7eaffd0 | -11.35549 | -62.44576 | 2026-07-05 05:04:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94a20db0-2f6b-3a42-b4c0-184be84ee948 | -13.22431 | -54.37044 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17521ca8-d93c-3c30-91de-85c69876080c | -13.22326 | -54.3339 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f51e222-4ad5-39bd-8726-ec709b6e3b21 | -10.1242 | -52.08857 | 2026-07-05 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 470d41ea-e138-3910-aa1c-5388fbee45ce | -12.06256 | -58.04851 | 2026-07-05 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
