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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2303af10-0f02-3256-a156-2ffdca090d37 | -3.03023 | -49.43917 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0233b91-a2ed-3c27-a7e1-f62edbb7ad76 | -2.17582 | -48.0216 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 031e77c6-8a3a-3f2c-9155-d213bd4b8f7a | -1.48753 | -46.09719 | 2025-12-30 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda260b9-d6ef-398a-afef-24efeaa096f3 | -6.23641 | -40.29586 | 2025-12-30 04:31:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0deeab53-5ae6-3d85-a2ce-0a28726d1f71 | -6.97997 | -35.1243 | 2025-12-30 04:31:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ec92c470-eb28-3797-a810-fe78ba38a8f4 | -4.34284 | -44.12463 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bac42142-e08f-3d13-ac72-7ea28cea0560 | -4.59611 | -48.78484 | 2025-12-30 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d22f2e5c-8111-378b-9290-a2152d5cd70a | -2.89674 | -49.5047 | 2025-12-30 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef1c394-1df8-3622-849b-a7906fbc959d | -5.9536 | -38.63063 | 2025-12-30 04:31:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 64d433c5-c7a8-30ae-b284-7ada69d0b0d0 | -3.60996 | -41.92023 | 2025-12-30 04:31:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ca7da05-2557-3752-a206-5bdf12fddbe4 | -3.55547 | -43.59807 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc4b6abf-56f6-36dc-a93a-286ec217d11c | -5.47351 | -44.69597 | 2025-12-30 04:31:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8cca256-3cda-3b01-9d4c-afbc9341be47 | -2.90326 | -49.80317 | 2025-12-30 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5e847d-6686-3567-8894-d431d6988fc5 | -3.09018 | -46.92086 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe17ece9-1c82-3aaa-8973-c1e54885fa06 | -2.29297 | -45.62001 | 2025-12-30 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c75e9b5d-9003-3e43-9198-16c449309d5b | -3.02677 | -49.43863 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd50bc65-d37a-399c-9199-e1369b2804a9 | -3.54595 | -43.6103 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0d478af-819a-3374-a78b-a6dae68c4a39 | -12.59353 | -43.97725 | 2025-12-30 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e9653be-455b-34dd-a376-38f8f2a8c1cb | -10.05066 | -36.27086 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0999fa60-3ee1-3d01-a3c7-d02c836db250 | -13.21154 | -44.56406 | 2025-12-30 04:33:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b08e3652-1dc6-361b-84b4-42345f954bdb | -6.93269 | -44.56933 | 2025-12-30 04:33:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6210f689-efbd-3cb5-bdd4-aeff429b4bf1 | -5.93949 | -44.45673 | 2025-12-30 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 902b347d-d5c3-3b19-82e3-e598c941ba93 | -10.04472 | -36.26437 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 9a3b88d3-a15c-3a3b-988d-bf5417c34a85 | -10.04406 | -36.27006 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| fa2810e0-03b1-3ab7-b784-0dd8dafc265c | -13.48027 | -44.01648 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f5a21df-ea1f-3c28-8a19-0463996bee67 | -11.76436 | -43.30462 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cac19c44-dbf2-351b-b93f-6186fdb091dd | -6.93505 | -44.57871 | 2025-12-30 04:33:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 897d6ed1-654c-3703-9d72-571b3f09ec48 | -7.15373 | -38.66886 | 2025-12-30 04:33:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdd6ff2d-1d39-3d8f-b09e-e491fe8a60fd | -6.18369 | -43.41805 | 2025-12-30 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fbd6613-01aa-312e-9bc7-b6404d9fff23 | -11.75957 | -43.30801 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d63876bc-4480-3f40-be53-f6a006b76321 | -10.78493 | -44.42511 | 2025-12-30 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee56665d-a87d-3b57-bad6-93dff1572a32 | -13.47199 | -44.01513 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e8a1ac7-ee3d-365b-80ec-937c6f838ac4 | -7.80283 | -42.69899 | 2025-12-30 04:33:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0f80ca6-20d9-3139-a906-82434a867a03 | -13.47976 | -44.02035 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97415aa6-6e7f-302d-959d-ecf55cdbea98 | -6.98792 | -43.83591 | 2025-12-30 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caec21b8-467b-316f-af23-6f2b2e1914ec | -7.06667 | -47.39571 | 2025-12-30 04:33:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 775abf20-440b-3b84-b599-ce8f2f59f01e | -7.06721 | -47.39221 | 2025-12-30 04:33:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8cb5484f-8bd2-35aa-ba00-f6ac065badd1 | -6.63474 | -47.57019 | 2025-12-30 04:33:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fb27d6f-f5c5-3dd6-93a3-cae43a2e4052 | -6.06376 | -43.25499 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f497ba40-2942-3007-8b25-4cc16acd60e0 | -9.88215 | -36.02284 | 2025-12-30 04:33:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 40138678-0999-3cf8-86d3-9c060878f3df | -6.9861 | -43.83761 | 2025-12-30 04:33:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e896d92-fa34-3d8e-b2b1-9907fe81ca9d | -11.76757 | -44.61796 | 2025-12-30 04:33:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b2df951-645f-38f2-a8f2-5c24f48f261a | -13.216 | -44.56116 | 2025-12-30 04:33:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 757a4cfa-fd36-393c-aff4-7baf12671dc1 | -10.04346 | -36.27521 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 0cb8540e-c99b-3667-afaa-0d812ccb1f8d | -11.74946 | -43.31882 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 948585e2-fe0c-3030-9200-1c29e92e0b27 | -11.75262 | -43.32747 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c100a90e-a949-3dcd-ab41-9a8730286342 | -8.3271 | -37.70827 | 2025-12-30 04:33:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f226df17-2dd3-33d1-a514-83dbbc96c4e7 | -5.80405 | -46.55019 | 2025-12-30 04:33:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53b57c70-dd33-3559-a2ef-39948e614ef5 | -5.58899 | -50.40863 | 2025-12-30 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ee0fad-e3e8-38cc-8a13-1fbf12786c17 | -13.42756 | -43.8587 | 2025-12-30 04:33:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3c3c205-091c-315a-957b-0e1ccd5f7794 | -7.01739 | -45.96098 | 2025-12-30 04:33:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47ff39fc-0742-3469-a171-afe585e213b5 | -13.47613 | -44.01579 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 755ea1ed-3296-36ca-a142-e941b130521c | -6.17981 | -43.4174 | 2025-12-30 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05c2dde8-8dcd-3522-a906-98f8e29d4a31 | -5.94076 | -44.4482 | 2025-12-30 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 543c1e1d-e7ad-3400-b78c-5851d0878c2a | -10.05132 | -36.26523 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e8789359-e10c-3fea-ac5e-ad85908f736d | -6.94621 | -40.81176 | 2025-12-30 04:33:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c95d097-7a64-3e8d-93b2-308389842d5d | -5.93584 | -44.4562 | 2025-12-30 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b62579b-393f-36c1-9032-38678f10d4ea | -13.4725 | -44.01126 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 883acf7e-dc5b-3bbb-91da-cf95cdf6479b | -12.59403 | -43.97348 | 2025-12-30 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9f0b515-7c8d-39bf-9f0c-9f809c98b897 | -11.76011 | -43.304 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 619d674c-0fcf-3844-af9c-22ff380e2999 | -7.14828 | -38.6681 | 2025-12-30 04:33:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fee1da14-b124-3090-9a0f-ddb7a406f7a2 | -6.60622 | -47.62253 | 2025-12-30 04:33:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca60510c-f9cf-3246-ac0d-b95e0117095a | -11.75316 | -43.32346 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67657bd0-ee25-30de-913a-ba1f9cd8500d | -6.18102 | -43.41423 | 2025-12-30 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 923fc139-e1d1-3be4-a74c-cab7395fd5ad | -6.93139 | -44.5781 | 2025-12-30 04:33:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e451c1e-854f-30e4-8298-ed4a3c654d7f | -7.36196 | -47.02699 | 2025-12-30 04:33:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c822cb0-f948-3cf3-939d-276f4aaade1d | -7.8034 | -42.6951 | 2025-12-30 04:33:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39b30087-bcf9-3c68-9795-a093b6779adb | -6.1803 | -43.41923 | 2025-12-30 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 474807dc-169b-343b-9267-3d1c166d8e16 | -7.02083 | -45.96151 | 2025-12-30 04:33:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 251491e6-88d9-385b-a940-f919357215da | -11.7537 | -43.31944 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42af1819-b687-3931-b177-d65b8c602a59 | -6.60676 | -47.61906 | 2025-12-30 04:33:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01aa531f-381c-3fd1-aba7-ed0ac9ec795d | -12.51384 | -43.69016 | 2025-12-30 04:33:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd51afcf-8ccd-3ea9-a149-fc26fb220033 | -7.8043 | -42.69799 | 2025-12-30 04:33:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c74dd91-f0fa-336b-8bf0-a962f21f671f | -7.09867 | -38.78826 | 2025-12-30 04:33:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61381238-84c6-393c-827e-f134f3491320 | -7.04005 | -38.26249 | 2025-12-30 04:33:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b614ff08-4360-324f-834b-eea817088614 | -13.08599 | -44.20595 | 2025-12-30 04:33:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8153a5c-f267-3c4c-9ca0-986d6c8f1b85 | -10.78421 | -44.43009 | 2025-12-30 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e359ccc-32ec-3abd-9fae-c1f469a996a2 | -10.04501 | -36.27414 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 4c8b4c69-1422-319f-8a5b-cba6b0db4bde | -11.75587 | -43.30338 | 2025-12-30 04:33:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8e7481d-e92d-3603-88d4-cb0c62ff049e | -13.47664 | -44.01192 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c35149a-dd33-321d-b64e-026ee76f0243 | -5.65963 | -46.69154 | 2025-12-30 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d8718b4-a44a-3fb2-8b00-754c4b8965cd | -7.37743 | -46.22187 | 2025-12-30 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c215faf-fc8b-3275-8c61-f55eee15d633 | -10.04566 | -36.26889 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 40244f97-713d-3584-b6bf-2cf40f1eb424 | -10.04636 | -36.26317 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| b466fa62-f323-30ce-aee3-8cb02ed1dbd3 | -10.05226 | -36.26969 | 2025-12-30 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8f550cf0-e92e-3d1a-aa99-8ac1a7facb44 | -5.95901 | -46.32003 | 2025-12-30 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea85ab00-dc05-30aa-9af2-273b8fde513b | -7.49002 | -42.72065 | 2025-12-30 04:33:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 194a7f33-41bf-3300-9f36-345b0001d1e4 | -13.42809 | -43.85478 | 2025-12-30 04:33:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04a16ff4-f48f-3fa8-8601-5462aa80348a | -7.15422 | -38.66529 | 2025-12-30 04:33:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea13cc27-3df3-3e9a-b10e-7c18abe4a4e0 | -9.88884 | -36.02367 | 2025-12-30 04:33:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 73374d8b-ec5c-3292-8624-0af536592dce | -13.52454 | -43.51244 | 2025-12-30 04:33:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b43d042-b5be-352f-8b49-65b718fec384 | -13.47562 | -44.01966 | 2025-12-30 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb285c7c-9837-3623-9881-f5a04a1ca078 | -15.12604 | -52.94428 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 07432f8e-59a0-322d-bba2-47472ed12ce6 | -15.74985 | -52.29974 | 2025-12-30 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4321740c-268f-3ce4-aa31-b918076a4ee0 | -13.51202 | -46.70736 | 2025-12-30 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcd8fa7b-b5ae-3d39-b267-78e24a99ec9e | -14.87553 | -52.81203 | 2025-12-30 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e322d5fe-3b10-3aea-aa20-e23fb74a3d7c | -19.45626 | -45.45097 | 2025-12-30 04:36:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd5e03b4-5142-38f7-994e-db2b746dfe9e | -16.38382 | -46.28113 | 2025-12-30 04:36:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2026bf0d-d4c0-3d87-8441-6d85cbe5503a | -19.77724 | -41.90864 | 2025-12-30 04:36:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2819ab7-347c-3154-b93a-541b76ca919c | -13.50591 | -46.70374 | 2025-12-30 04:36:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README7.md)
