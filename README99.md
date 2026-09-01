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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a79a6fac-19e9-3a0a-a372-0aa8509fe4e6 | -10.8046 | -50.5046 | 2026-09-01 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 279.4 |
| 5c8fc2cd-93f2-3486-8981-f4dfde559721 | -11.5479 | -45.4676 | 2026-09-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 78cd9065-a524-3d0c-b322-eb8d6c7a4dba | -12.9032 | -45.8382 | 2026-09-01 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 5b03cb19-c571-3ca2-b348-aa4643a7240a | -10.8404 | -50.6499 | 2026-09-01 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 721b9fd8-d14f-3f8f-8761-d66760035685 | -6.8009 | -59.5742 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 368602ea-dab2-30c4-a2e3-2bc073b4323d | -8.7817 | -46.4623 | 2026-09-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 270.0 |
| 609c5721-6edf-3c70-b09d-cdf3a706ab90 | -15.4235 | -52.6836 | 2026-09-01 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ed59c193-eded-3ec4-b4f8-fd66b3955b68 | -10.036 | -44.7056 | 2026-09-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c01ed48d-0350-3f1c-a9e7-7aebd2b68107 | -7.182 | -60.6904 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 99cbd682-dd5c-3592-865d-8018810c43e3 | -7.3302 | -60.589 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 410de367-7dd9-3dca-8c7d-76f5c2a46e52 | -10.696 | -46.2646 | 2026-09-01 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 418.4 |
| 1707c5c0-16c3-3e9a-a54a-b4eb67dd46a6 | -6.1659 | -57.7403 | 2026-09-01 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0ed931ae-57e4-370c-8ac7-528754af0132 | -11.2317 | -46.1041 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| bb631ff3-1a87-31fe-8d9b-529cd44480c7 | -14.7108 | -53.599 | 2026-09-01 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e37b2d24-d3e4-3b3c-8d55-ed6073754f38 | -3.2623 | -58.2367 | 2026-09-01 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d6d7a672-9166-31b6-9439-03132f325950 | -7.2934 | -60.5713 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dd81c859-723b-3628-9963-7a69bff7430b | -11.213 | -46.0839 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 36a9b5d7-db7a-38b8-97e2-9f83fa5e1c75 | -11.2478 | -45.1425 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| d983cb93-bb93-36b2-85c4-9e915497ba46 | -10.3574 | -50.0171 | 2026-09-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 983cdaad-650c-3661-801c-983006a03e30 | -6.8036 | -59.0921 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 68ac3411-19f8-33db-a346-0e8e654c6d3b | -10.7856 | -50.5066 | 2026-09-01 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 178.0 |
| d5ec4234-07cc-3f3d-9459-d0b4fd622614 | -11.6841 | -47.5932 | 2026-09-01 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| a79feed7-6879-3fb4-b7b3-494c335a7c50 | -7.571 | -60.4643 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.1 |
| ab638d5a-0916-3c12-9c42-7acf7c5c99a0 | -9.4349 | -45.625 | 2026-09-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ccefe00b-1232-31b6-b99f-975a78a9e24c | -3.8416 | -44.0824 | 2026-09-01 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 14ff8e24-ab1a-3113-96f5-bdf7bd8ef4b5 | -9.4538 | -45.6228 | 2026-09-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| df9ead3a-79bc-36fd-8a81-37ac4c364532 | -13.9477 | -54.3971 | 2026-09-01 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c232031d-7e7a-394e-81e6-ce6969453bf1 | -7.5474 | -61.3818 | 2026-09-01 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b226a3d0-3e61-3963-82fe-5cd13b36f2dc | -10.7409 | -54.0196 | 2026-09-01 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8c280923-92a8-320e-a0ca-2d372a7e3f4a | -3.879 | -44.0576 | 2026-09-01 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 891a706f-78a6-3296-9300-2c09d6dc5520 | -14.6732 | -53.5408 | 2026-09-01 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 0d60b6f4-b631-363b-b157-6a46bc532466 | -7.8716 | -47.0838 | 2026-09-01 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 986a9c9d-8ef7-39c4-b0a9-951207bca7c6 | -13.0892 | -45.1862 | 2026-09-01 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bf03bbd3-05e7-3031-aabb-5102240f3100 | -7.5259 | -44.4565 | 2026-09-01 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 345a1345-b821-3bbe-866e-ebb5a5c0f11e | -13.4519 | -57.039 | 2026-09-01 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 81946573-d136-38d8-8dcc-9085a3fb26e4 | -4.181 | -63.1543 | 2026-09-01 14:10:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 2690e568-7a52-3451-b462-ff64b9f427c4 | -7.5659 | -61.362 | 2026-09-01 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7bdc8640-b66d-3547-9f4d-414566ea5179 | -6.6542 | -59.426 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8b890f64-7adf-3bb8-9eea-151a378491bf | -8.9242 | -63.2804 | 2026-09-01 14:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ac686c81-1705-3247-9b40-518b72801116 | -10.0364 | -44.6825 | 2026-09-01 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ef6a9762-bf45-35e5-b421-ebd599443683 | -7.5709 | -60.4835 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 1b976ffb-c8bf-3ab1-bc12-07133300b39e | -7.3119 | -60.5706 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b8602646-c966-3218-86fa-04acf3987072 | -10.8627 | -45.356 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 2b40e2a7-bffa-3813-ad1c-2cd75742f0be | -14.6535 | -53.5642 | 2026-09-01 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 556ebe90-a384-3e70-ac28-0c94c5c552df | -14.4587 | -52.5151 | 2026-09-01 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 172d48d8-23c9-3166-bdbd-0591cecd4afa | -7.9797 | -44.2962 | 2026-09-01 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6678ae35-e9e8-368c-b2fb-c6740df9491f | -6.6541 | -59.4452 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 29f1f309-16a7-32b9-87b4-9caa362b41db | -7.1786 | -55.4837 | 2026-09-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 1b3b058c-c84d-33cd-ad5e-fb83f78565f9 | -13.967 | -54.395 | 2026-09-01 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 16ea2207-507e-3f87-9e12-6bff93de8171 | -10.8624 | -45.3789 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| dae87e9d-3c18-36db-ac5c-15bb49b0fe7e | -3.1083 | -61.238 | 2026-09-01 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e8f71179-b316-3896-becb-93d8204e56de | -13.0897 | -45.163 | 2026-09-01 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 9f93b7bb-fc93-3da2-a00c-47406125c4f4 | -11.2482 | -45.1194 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 71f4eeef-ed9c-3b4b-9679-613adefeb0cd | -7.5895 | -60.4636 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ab96229f-2315-331a-b3f2-f8bbc0579e2d | -10.358 | -49.9742 | 2026-09-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 4265b20b-a9b0-3bd0-a397-08292930f7e0 | -9.9912 | -46.4409 | 2026-09-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| cc9a6d28-06b7-33ef-9166-b2b9fc434b50 | -7.3685 | -45.066 | 2026-09-01 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| cdf266a2-35ba-3b55-8b09-3c5547cd0c79 | -17.1345 | -46.8516 | 2026-09-01 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ddaf4649-5ae1-3751-8fb7-2385cd5f1bc3 | -7.4262 | -44.9468 | 2026-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 12f62336-c7ea-3499-9788-7456173843fd | -7.5658 | -61.3811 | 2026-09-01 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2da5432f-d8f7-3fb9-b074-42b080687540 | -7.3488 | -60.5691 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 6e8bf4d0-4ee3-3ae1-b3e5-103258706a64 | -3.1266 | -61.2188 | 2026-09-01 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8adca41e-a4a0-3c51-8717-6ee57e3a3221 | -7.3487 | -60.5883 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| cd08a070-ed3e-3c3a-b34d-109e4e934a32 | -9.9931 | -46.3057 | 2026-09-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| af40880e-5b95-3926-bdbd-5f97cd6cf9a2 | -11.2673 | -45.1167 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| e815fba1-1210-3de1-8bfb-ba28706b9ab6 | -7.8443 | -61.1413 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 60ee7863-739d-3832-9605-ad89507cec26 | -14.5214 | -52.2313 | 2026-09-01 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2908283f-702c-32fa-9dc7-df45c7491046 | -6.97 | -59.0465 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 569eddd7-fe36-3453-9b91-2bec23e7afa7 | -14.5021 | -52.2339 | 2026-09-01 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 890983d4-2f9b-3cf9-8da7-220eb86ef011 | -6.9367 | -55.636 | 2026-09-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 41624637-c417-3ff8-aade-220d491496b7 | -3.1083 | -61.2191 | 2026-09-01 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4d458e3b-9c27-3b06-bea3-0baadfc02a92 | -3.9221 | -43.1291 | 2026-09-01 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 2fddf964-a9b4-30f9-85f2-4e6262107369 | -7.2006 | -60.6706 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| ff4a96ae-fff5-32c5-a14e-707bb74e975a | -10.6769 | -46.267 | 2026-09-01 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9d291bb6-4cd7-3e1a-bb21-0a475614d7dd | -10.4261 | -46.5235 | 2026-09-01 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8a0da670-87c1-3ebe-8254-bf4d9c57b917 | -3.8605 | -44.0355 | 2026-09-01 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8370b154-a363-3a21-b5b6-e66831fdd34d | -14.5025 | -52.2126 | 2026-09-01 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ce8f3a66-868b-3a85-8ab5-7a46ddc82778 | -17.1146 | -46.8556 | 2026-09-01 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 53a2ce81-4b53-3d59-bdc3-0b8eed5f1612 | -3.6215 | -60.566 | 2026-09-01 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 979077a2-3c64-3cf0-8899-d105d1bacbd6 | -14.7302 | -53.5966 | 2026-09-01 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2f1b3adb-3d70-3bae-a0fe-6893ed71bb97 | -11.2295 | -51.2667 | 2026-09-01 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 9818ef5b-c6e3-3a69-af86-bf14960dbbb6 | -6.6726 | -59.4445 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5357c963-fd4e-35f2-83f5-c4630651c0bf | -8.5602 | -54.7175 | 2026-09-01 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b613b661-e018-376a-98c6-0f55f7f289a4 | -6.8193 | -59.5734 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d64dd46d-17dc-321f-b75d-3902b7794650 | -9.4606 | -67.4531 | 2026-09-01 14:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ff521899-787d-37a8-b04c-8f2bcee39cfc | -9.1429 | -60.9493 | 2026-09-01 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7d346647-7bd5-30b2-9fd1-1956f11fdfd8 | -3.1265 | -61.2377 | 2026-09-01 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| d6e78de4-02ee-343c-9e35-738bff64712a | -11.84 | -46.02 | 2026-09-01 14:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9ebe3cc-54a9-334c-a2ec-f625a41aeec4 | -8.78 | -46.45 | 2026-09-01 14:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c210428c-be66-34cf-9a6e-d59c9b2ce02b | -3.87 | -44.07 | 2026-09-01 14:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0826cc15-240c-30e1-8378-75d76cdac352 | -3.84 | -44.07 | 2026-09-01 14:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78511e28-38f6-39cf-869d-c72d1fc4f5de | -17.11 | -50.53 | 2026-09-01 14:15:00 | MSG-03 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13861586-1913-3f38-9f31-dde4996f7356 | -3.1265 | -61.2377 | 2026-09-01 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 8a18c22c-738d-3931-93c8-f6614f0975fe | -7.571 | -60.4643 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 2dc7ec5f-60b6-3302-b2d0-625e84912694 | -13.4519 | -57.039 | 2026-09-01 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 5ea9a401-9bda-3e72-9e84-e3067e549625 | -9.9931 | -46.3057 | 2026-09-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1be36573-287d-33bd-bfd6-5c598d921632 | -14.5021 | -52.2339 | 2026-09-01 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6be70fb8-ac06-3231-b475-6681900bd19e | -7.5659 | -61.362 | 2026-09-01 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 31c200cc-cbe4-3b84-a29d-a397f9fbf61c | -6.8193 | -59.5734 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 239.5 |
| dc2a1f62-c094-31b0-9659-133e87aaaad6 | -7.3302 | -60.589 | 2026-09-01 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README100.md)
