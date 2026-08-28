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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb5c8ee-6158-35bf-8add-eec03a8f3e8e | -7.74628 | -44.73441 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cd2075f-f5e2-36fe-a1f5-87ecfe8dc8a0 | -7.27865 | -49.94639 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 626d14f4-ffe9-368d-b9f4-56b568619a0f | -8.16877 | -46.1784 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83954e3b-3fc6-38c4-b276-789b9d742013 | -2.73435 | -47.04316 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04a821d5-7bf3-36e5-a869-6a73988cc319 | -6.90437 | -43.64838 | 2026-08-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b05288dd-e001-362c-b903-4998621408e6 | -7.09638 | -42.16849 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1861f983-e506-3feb-a5e9-383599277532 | -6.59671 | -55.43643 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ac80f5a-ab29-33d1-84f4-d4062e87b972 | -4.84785 | -45.39615 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| e668077e-c202-3218-a193-27e89eda2867 | -2.73355 | -47.04814 | 2026-08-28 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cdc8753c-99d8-320d-a1b0-f124a9d269fe | -8.10202 | -45.81943 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc74bd49-aa0b-38ed-8904-84280693c60e | -1.96402 | -48.37497 | 2026-08-28 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1852a35-1ecb-39b1-90b4-4e49ac1ba54b | -5.29107 | -50.94167 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ee8fc92-d6ed-3f8a-b5c5-a5f8e7596afd | -5.86981 | -49.77536 | 2026-08-28 04:14:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 189819ad-be48-3a64-bb61-74b4d327205a | -7.2106 | -42.75191 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f8d6c9a-9609-332b-92bd-9563c29b5dbc | -8.33536 | -45.72113 | 2026-08-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a60ffcfe-93b8-3d39-afa7-c8846a3175bc | -4.8456 | -45.3878 | 2026-08-28 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cf87733-c1a6-363e-b8fe-56f801a853d9 | -7.27408 | -45.35331 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62b5437e-4280-31f1-88f0-84e759aff407 | -6.90223 | -44.67295 | 2026-08-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e05e471-7e2a-327f-a57d-701cbea2af38 | -5.7607 | -50.22164 | 2026-08-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af925ae6-df02-38e5-8ae1-fc780d54266a | -7.26565 | -45.86159 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5f112c1b-c849-3ca4-90ba-1271bbbf5fa2 | -5.93416 | -52.365 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c1f8b40-4351-3d5c-aac4-bedb76354354 | -7.08757 | -42.8007 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 99d3fb6e-20c0-3571-b9a3-ed50f1a7d6f0 | -6.27949 | -53.37226 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 097b68e6-2fc3-3d52-8e7b-21fd3d3c8de2 | -8.08534 | -45.81298 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824315f8-ba97-3d50-b7cc-1fdac3635cba | -3.4562 | -43.36293 | 2026-08-28 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdc558f9-a5a8-32f5-ba72-99996a653175 | -6.17687 | -45.34188 | 2026-08-28 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9aa810e-d01b-3292-a0be-462831dfc6bb | -1.82854 | -47.8987 | 2026-08-28 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69080dd0-bff1-33fe-b09f-002c5f49d0c9 | -7.07328 | -46.26163 | 2026-08-28 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 698f8bfd-3c5f-3276-8c42-e7f3717d9372 | -6.52984 | -55.25349 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b42559ba-cb19-3ae4-9a7c-7da116541905 | -7.52522 | -44.45898 | 2026-08-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1b24828-5bab-38d7-950d-95fec9a75cd2 | -7.67267 | -45.69335 | 2026-08-28 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b897143-861e-3a8d-a5c8-1abdce8a258b | -6.23504 | -53.47876 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4a027c-73e2-3025-a763-90a6e43edcbb | -7.67484 | -43.94124 | 2026-08-28 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55af5a6f-7232-339d-a830-9409b019e19b | -7.44828 | -41.49084 | 2026-08-28 04:14:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b45384b1-c9f9-32aa-9e05-94e3c504e851 | -7.3631 | -46.66512 | 2026-08-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6309efdf-9b8b-35b8-aba5-1f6dd34da366 | -2.95339 | -43.25157 | 2026-08-28 04:14:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22251236-cd60-36b1-99d4-7cdb48aec5a3 | -5.81755 | -46.22238 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c125b3a-d327-38da-8ada-94e2c6c32c54 | -8.013 | -48.40709 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90b7fc8b-4b44-3f48-a7fc-a16af8cb091e | -6.64384 | -53.18858 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e765cd-28e6-358c-8a9c-81cccea48950 | -8.10141 | -45.8233 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e26ba51-33b8-34e9-9be2-210cb48cad31 | -6.18951 | -45.89594 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f89eefda-7cda-33a2-a92e-a081883fdd0c | -7.16645 | -43.16839 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd9e0cb7-e5ab-39b6-b715-dc7aadbad33d | -7.10979 | -42.83265 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40d41215-647d-3030-b2c0-3e206e8d5abc | -6.93236 | -42.68328 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03fe63e8-e82e-3236-877c-4cf4686cc48e | -6.2763 | -53.34377 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8503326-08fa-3efd-b066-ff02cf0a5ddc | -7.25393 | -45.86764 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 11ac1662-6d94-3585-93d6-e830c8273a5b | -6.6433 | -53.1842 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b376f124-bd83-3db9-b852-589b9ba1df7a | -7.2552 | -45.85989 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f03f6d3d-08f7-317f-a434-d5e30755210e | -7.08703 | -42.20713 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19c67aa0-c65a-38ca-9cc4-f33f9be48cec | -5.34538 | -45.163 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6736a535-0c10-340e-b198-f52eb73dc912 | -7.25171 | -45.85932 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e83932f1-12ce-392b-9628-f46fceb912d0 | -6.83904 | -55.61095 | 2026-08-28 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d1b6c2a-22c5-324e-a916-22b64368b4ae | -7.09985 | -42.8311 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 43289597-fcf4-34c4-94fb-e97a46207522 | -7.16223 | -42.82296 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 81165b13-9f27-3b65-b340-6dc953d6155c | -6.64819 | -53.18894 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e671954f-861d-3f5b-853e-11fefc9937c0 | -8.01335 | -48.01728 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a02415fd-d472-389b-921a-ab492e5de5a5 | -7.19894 | -42.73936 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ab98241b-0d95-3e04-9e19-a779a5730cf1 | -6.27428 | -53.35537 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03e2b001-ba5a-3a11-a9d9-4ba9eb141a55 | -9.01454 | -40.99311 | 2026-08-28 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ccab5925-833b-3c15-b7fb-7d681eca2cce | -8.01254 | -48.0221 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bae29113-8a4c-3e81-b311-576fdccd2320 | -6.63893 | -53.18379 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fd24130-7c8e-3243-a21a-093f3148da42 | -6.87762 | -41.73798 | 2026-08-28 04:14:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d661ca8-eea7-3601-ad39-e91b383a26a6 | -5.25928 | -50.96735 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7fd5632a-8b36-3e0c-9c6a-6aa53bb165a3 | -6.53715 | -55.24941 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b485994e-58c5-3b87-8be2-1311f86b2081 | -7.25045 | -45.86707 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d7c5070a-8907-3229-85e2-0179ebce0f98 | -7.61038 | -45.20561 | 2026-08-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fba00b3-31bd-3532-9162-1270bc3f2175 | -6.26652 | -53.36629 | 2026-08-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7e3b521-4d90-3c02-9d47-d82e26b2297e | -8.2059 | -47.51557 | 2026-08-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bfcc18f-76fd-3de7-968e-d56f3995b0d9 | -7.10035 | -42.18734 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d2f06dd-28cd-3ec2-b0e3-07cfbdacb0a6 | -2.23458 | -47.71494 | 2026-08-28 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aca71ff-262b-331e-8563-85417997e1e4 | -7.25457 | -45.86376 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a1ef269a-42fb-3bea-bbe1-f8e86b694a14 | -5.33908 | -45.15813 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b24f94e4-91b8-3710-a5be-b88a6b08ffe7 | -5.89576 | -52.11242 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c44ac5de-2d53-3fad-ba55-f830c5fb248b | -4.10581 | -47.22069 | 2026-08-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25d6b1bb-9b1c-34a0-adb2-cf9dd0d1ce37 | -5.58911 | -46.24366 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a50fee5-0e95-393a-a2e9-2b8c2b83b601 | -5.16135 | -42.74682 | 2026-08-28 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cc52abc-1d9c-3cd9-af53-6edef94cc96a | -7.13824 | -42.75858 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 248c27ba-461b-396d-afe1-d27e708db510 | -6.93622 | -42.68031 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03dea5da-2b1d-34ca-a1d3-a0d9ae0c445d | -5.93213 | -52.36491 | 2026-08-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c983434-bce9-3e59-ab6f-3e711e6d59d2 | -5.77819 | -46.1695 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc7f0a4-4976-3994-8313-240699673a6d | -5.92241 | -42.98994 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 76f274c5-6ba6-3f23-b280-c01dc816ec7f | -6.90558 | -44.67349 | 2026-08-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afc7037a-9553-391b-9b3c-7a315013615f | -7.08703 | -42.80418 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d2c33c84-ad97-361f-a22f-31afd73c15da | -7.10702 | -42.82866 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5788b9a5-b0cb-34b4-ae8b-502484ed2f22 | -7.26347 | -49.84875 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab240fea-7d5b-39cd-b756-98963a89aa59 | -7.09581 | -42.79128 | 2026-08-28 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 902951b4-d7c0-3a38-85cb-1b5e87c59a39 | -8.07907 | -45.80792 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9123d30-f970-3dda-acc1-cf0ea8cd12c2 | -7.12514 | -43.1726 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3a251f3-c67b-3ae5-9c06-adb0e7aa9de9 | -7.05542 | -42.89898 | 2026-08-28 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 343512e3-ad03-3023-ae6b-acbcae9ecd64 | -6.92303 | -41.62885 | 2026-08-28 04:14:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7e57044-cc45-3dff-9c4c-6172db65eb7c | -7.26793 | -49.84921 | 2026-08-28 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85dcaa32-c944-3918-a57b-5db63480729a | -3.22199 | -48.61018 | 2026-08-28 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14336f4-718c-3953-94cc-0742f6403fdf | -5.81168 | -46.21299 | 2026-08-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daff57ca-f346-3282-b4ad-10a4231e1331 | -7.27468 | -45.34958 | 2026-08-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 626e18a2-04c5-320e-91dc-d5d820b88422 | -7.26502 | -45.86547 | 2026-08-28 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7f5400ef-b1f5-3f2a-9482-b3d6a68dd01a | -8.16525 | -46.17794 | 2026-08-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 534659a8-e01a-370e-bfa5-e7c6338f8aa0 | -8.03268 | -48.02051 | 2026-08-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 533c4f1b-147f-373c-9124-9548d86bccbd | -5.47848 | -45.12167 | 2026-08-28 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa2888c7-0c9e-32c7-889d-0cf89f8e4b1d | -7.07753 | -42.202 | 2026-08-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae28f302-2209-3b9b-bebf-ba2d191910ae | -6.53177 | -55.24298 | 2026-08-28 04:14:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README19.md)
