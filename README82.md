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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77aafde5-eaa4-37de-bfc7-6752fe88b4ef | -3.50509 | -62.85215 | 2024-11-29 04:59:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab37465-23c3-3e76-a876-47c7a16085aa | -7.80075 | -50.00209 | 2024-11-29 04:59:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e9c0a71-e588-313e-9686-9eacaa1a3b26 | -8.13233 | -47.9835 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb940b37-4aca-3115-89a7-b7220df43a5b | -6.23329 | -55.62769 | 2024-11-29 04:59:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdfb3985-69f9-3d7b-ba7b-0dbe3f8ff749 | -6.7527 | -46.5243 | 2024-11-29 04:59:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0565daf-d7f5-39e6-bda9-675b789d46bf | -10.71641 | -57.10781 | 2024-11-29 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 316660f7-b894-3ac8-a82b-d811df2c78dd | -8.72065 | -48.28962 | 2024-11-29 04:59:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70150983-2f89-3c3b-9172-ab4dc9f78088 | -6.93609 | -43.49461 | 2024-11-29 04:59:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| af8855b4-858e-3931-a760-ec31bac137d7 | -10.82225 | -56.23396 | 2024-11-29 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 093b5582-9717-3b0a-91fa-2fd7fda2e56b | -5.18264 | -60.2631 | 2024-11-29 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b476fdba-8701-3c97-8831-34831b56b118 | -7.61165 | -47.09787 | 2024-11-29 04:59:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80d11ab1-8d8d-3f49-b5cf-330d64ade987 | -7.83513 | -48.19425 | 2024-11-29 04:59:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9843a118-8b61-379b-84be-a0b397dc9586 | -4.51528 | -59.8118 | 2024-11-29 04:59:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9608d400-32e4-3251-94fe-3bcfd3f7765c | -6.80082 | -46.46865 | 2024-11-29 04:59:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6faae81d-3321-3ce0-928e-004159d280b7 | -6.48606 | -44.68595 | 2024-11-29 04:59:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51049b63-15af-3c5e-a936-1abb12128e74 | -9.86736 | -57.3192 | 2024-11-29 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78491666-b8ad-3bab-b13a-b13aacf41aec | -5.61868 | -51.28056 | 2024-11-29 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fba83d2-054c-3944-9ad8-3f759c72b464 | -5.0075 | -56.17719 | 2024-11-29 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3c4a65-4be2-3035-85a9-42030a23b951 | -8.4728 | -63.93754 | 2024-11-29 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c5814d-4b01-33f9-a80a-751bb698dbbf | -6.48655 | -44.68233 | 2024-11-29 04:59:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dd0317d-06cc-3c79-929d-0cbacd971fff | -9.20761 | -62.37821 | 2024-11-29 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 583b0ec7-5325-3944-8c22-101d9ff9d7e2 | -7.97891 | -55.30434 | 2024-11-29 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba1d531-5a3b-3811-807e-696a74411b40 | -9.28849 | -64.24228 | 2024-11-29 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54afe118-95fd-335a-9d9c-bdb572f1d75f | -7.97945 | -55.30086 | 2024-11-29 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef893e02-8ead-30e6-9ea1-802187bff253 | -7.58486 | -47.11525 | 2024-11-29 04:59:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c41de42-e558-3c3e-8186-2e2b9eff3536 | -8.27921 | -48.03505 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 619c01bc-e0de-368d-890a-c7bd1ef46d75 | -5.69737 | -55.74796 | 2024-11-29 04:59:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2712d149-6258-35cd-9645-fe99b7ab06cc | -9.31247 | -46.22627 | 2024-11-29 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 013f5c2c-5f0c-387f-bfeb-66d87ae900e1 | -7.8313 | -48.18908 | 2024-11-29 04:59:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4464f154-818d-36ae-8417-67d544b8dc80 | -8.12627 | -47.98597 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f823580f-3df0-3441-a470-a96b648a1eaa | -7.56742 | -47.38887 | 2024-11-29 04:59:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34a6060-6152-3f01-a60f-54966f50cd2e | -5.01495 | -56.17462 | 2024-11-29 04:59:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d295aa1d-2125-3db2-bdce-ff227f247c58 | -3.51093 | -62.84974 | 2024-11-29 04:59:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf6cb52-1bad-3367-b4b9-a10b5c082080 | -4.7786 | -46.1131 | 2024-11-29 05:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0b5db5f2-70b8-3694-9079-90b311493e9f | -3.259 | -53.6388 | 2024-11-29 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bf683417-6f67-38f5-a175-364e49c11e9f | -17.5805 | -42.7483 | 2024-11-29 05:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 339e5224-3bac-360b-82fd-c6675ae61c01 | -1.6997 | -52.4535 | 2024-11-29 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 061d2d1f-fe7f-36e6-b7cb-ddb3652a5549 | -1.5897 | -52.2915 | 2024-11-29 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7bf405d5-1314-373f-a0f5-1556b90892f9 | -2.6498 | -48.7986 | 2024-11-29 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 0a7c4d96-88b5-3ef6-9a34-d88a1f9f4752 | -2.966 | -53.3027 | 2024-11-29 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 74c62c02-a282-3293-9809-370c626ec48f | -2.966 | -53.2824 | 2024-11-29 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7a90a4a5-dd70-3819-b6d8-82576248d161 | -2.9844 | -53.2819 | 2024-11-29 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| e279baec-f246-37e0-84cc-f7b1961d0eae | -2.6684 | -48.7767 | 2024-11-29 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| dab4b685-a206-3388-8a07-ba3b53fe5f2a | -2.6683 | -48.7981 | 2024-11-29 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| dfad869e-5df8-3d07-8baf-eb427ee9f0f7 | -2.6499 | -48.7772 | 2024-11-29 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| cd5cb841-0c53-3193-a26a-15ead07499d5 | -2.9844 | -53.3022 | 2024-11-29 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 3935ca44-f6c6-3e12-b8fc-056678975f99 | -2.67 | -48.79 | 2024-11-29 05:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28a8f0e-0ee0-326d-96f6-4fbec8467d6c | -15.06609 | -59.65371 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e53b9f85-ee99-3215-8cab-e14778ca8d65 | -17.65258 | -57.56783 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 897b912f-3d79-39a5-8fdc-e7440bf13257 | -17.6432 | -57.56249 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 07463d10-619f-373c-bcc5-1bfe71e5ab34 | -17.70314 | -57.59121 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7db91d52-c414-3bb7-8c2e-50c737088a2c | -15.08699 | -59.63984 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93174da4-0fde-3e06-81f3-29670dc68b8f | -9.88106 | -63.1112 | 2024-11-29 05:01:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5e04688-a91a-3329-9ddc-15b8dd28be7f | -17.62784 | -42.74737 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 238334b9-d659-321a-8e1e-e9cd91beb1bd | -17.54378 | -57.43789 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 16b99713-dc0a-32e6-807b-80d95db241d8 | -14.59653 | -55.49017 | 2024-11-29 05:01:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aca369a-f8c2-38ee-a045-79faf87c375d | -17.64927 | -57.56725 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6ed2e37c-671b-38c3-87a6-88dbbaf541a5 | -17.64537 | -57.5703 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0e383982-994c-3636-aa8c-0c94807fb4f3 | -17.58688 | -42.76437 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 117487ce-5ee0-3e58-915e-fe849a97cef9 | -15.5699 | -47.85679 | 2024-11-29 05:01:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643ef971-f228-3ec4-b4ce-21cce002bfb4 | -17.6543 | -57.55695 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ae988be3-7380-3d02-93b3-3e2fde35f576 | -17.63759 | -57.57642 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 019d37f8-3596-313e-9702-7507657af49b | -17.64263 | -57.56611 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 88587091-d3cf-33c8-a519-742a971ea8ce | -17.65099 | -57.55639 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9b365e93-0d80-352c-b1a3-f458cd0b5a6c | -15.09058 | -59.64049 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fc5c24e-5700-34c6-98a3-32338007037c | -9.64823 | -65.74002 | 2024-11-29 05:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a995078-a71a-3fa9-917c-9e95e14a2a1f | -11.88247 | -58.52146 | 2024-11-29 05:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3df4011c-3b96-3bec-811d-1f06a47fcbdd | -17.65488 | -57.55333 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3353a94c-198f-3c15-bf0b-0f743768f47a | -17.65635 | -57.58711 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9837e03d-5a70-390f-8e39-28a0394e9da5 | -17.65156 | -57.55276 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 61b86908-0a74-3d0f-99a9-7d2e711155c6 | -11.7631 | -54.68975 | 2024-11-29 05:01:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c9cbc8e-e420-3a81-9463-b0b507a8e483 | -17.65188 | -57.5938 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 07e7209b-2601-372a-904e-eac27b979bfb | -17.6337 | -57.57948 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 88ebaaa1-1992-3dc4-b567-3cd3f3b24a4b | -17.65979 | -57.56535 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2d3ddfc0-8354-3993-aa0c-996660780f8c | -16.08533 | -60.11049 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0603481-a8bb-31e4-8068-02120f03b7cb | -17.64422 | -57.57756 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f332cae3-203d-3aac-af75-31ec99d456f2 | -16.08171 | -60.10983 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14aaf05b-434b-3c3c-983c-2e5cafd22e3f | -17.64869 | -57.57088 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ed65132f-5e13-3d26-98ca-2793739a7293 | -16.39583 | -51.61091 | 2024-11-29 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17be4cd4-f874-3a52-82ed-840c212289fe | -17.70372 | -57.58757 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31a558d8-5c48-33ec-acf2-4bd4dac3a172 | -17.6513 | -57.59742 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f134eda-8dbe-348c-ba95-be31310f7adb | -17.58747 | -42.7574 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1fbc765a-83c6-3a1b-9994-37f3bd3e5ee9 | -11.91525 | -55.9028 | 2024-11-29 05:01:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ca2832d-d25e-37e2-afb3-9c311e4aad28 | -15.08626 | -59.64412 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 360ad973-1376-33d8-adaf-b326cffeda14 | -12.30928 | -56.70329 | 2024-11-29 05:01:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2606819-d762-321f-aa87-5bcf33b8a80e | -15.08267 | -59.64347 | 2024-11-29 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe04b873-bfa1-3d29-8d28-7f83318fe7cc | -17.64595 | -57.56668 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 451495a7-5e15-345c-8fd7-394865e27170 | -17.63701 | -57.58005 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6404593a-28e6-3451-8eb6-2262667bcbc6 | -11.72653 | -57.44429 | 2024-11-29 05:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de06598c-de8c-3310-9268-9a072674d3f8 | -12.30376 | -56.69504 | 2024-11-29 05:01:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3d0b857-9fbf-3cfb-8d00-89b294ee8d0d | -16.35229 | -43.69491 | 2024-11-29 05:01:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17e18aaa-0c0a-3247-b1bf-0ab36225887b | -17.56458 | -57.47862 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 089c0321-cdc8-3363-8a37-75c26bbe141c | -17.65577 | -57.59073 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2d39d52a-7f1b-3e58-aa66-b26356cf7484 | -12.30709 | -56.69559 | 2024-11-29 05:01:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a84260c3-35aa-3a26-a9f3-bf6f3d963ae6 | -17.70703 | -57.58815 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d8d5020-52ea-3089-9308-d9c5345afa0e | -17.57815 | -57.60718 | 2024-11-29 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 70442804-dc20-3993-9ad0-3670ae1f1bac | -12.41111 | -63.71411 | 2024-11-29 05:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a408bd18-3894-3854-937c-d371326c4aad | -17.62727 | -42.75452 | 2024-11-29 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f14939a-5a0d-3c34-8a56-07895281d8f4 | -11.3635 | -56.21006 | 2024-11-29 05:01:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26f7ba02-bba8-30de-bc34-bac4bdab6c3d | -17.64091 | -57.57699 | 2024-11-29 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |


[Clique aqui para ver as próximas entradas](README83.md)
