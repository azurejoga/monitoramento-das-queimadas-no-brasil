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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac02c955-267b-33ac-aa2a-cbd8fcd4cbde | -8.55609 | -44.89996 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe9f1b68-96c2-382a-8159-941209bed9f3 | -9.18541 | -45.68834 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9bc7a6e-4813-3a99-b735-6c897c4bd501 | -10.88697 | -53.99718 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e97230ba-8247-310e-86d0-2499cabb1b03 | -12.52666 | -47.09254 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d147eae6-e9f6-39e1-bc53-f2d62582d0e5 | -10.66663 | -50.47246 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4640d265-96b5-3e18-ab8a-a1bc0232bd14 | -6.44722 | -44.95178 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c61a9242-3bad-3615-8aa5-49772a917a20 | -9.24446 | -45.90803 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd6575f0-3721-3e81-998e-adf82477d5c7 | -9.91139 | -46.53762 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7c71f24-0cfa-3333-9d59-d2e249d1ebb6 | -11.0264 | -54.15273 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 061d1c41-5ff0-305f-9876-093b97b8cb02 | -13.24661 | -46.90814 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 445e136c-7d5c-3d24-a7cb-340ec7bda0c9 | -8.53681 | -44.54365 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23e0abf8-216d-32cc-a801-d8c3685ae684 | -8.30489 | -50.96254 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eabc848-7107-3a57-9d82-393641b97ae0 | -9.5805 | -46.56911 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94dd5a04-bec8-3950-a8c7-35ae1b15bdb6 | -9.39606 | -46.84729 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070d9b0a-c21a-3e4c-a980-e9bddfa09f98 | -9.86396 | -57.9668 | 2026-09-18 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73894e7-8d9b-350c-8a82-7d9474163efc | -7.80987 | -45.11656 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fa7301c-43f4-3a9b-bb3b-d50a65b11cef | -7.60596 | -46.62457 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 911ee153-6b00-3061-8b9a-5e0c95576d1f | -10.66039 | -50.46771 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b988386-f702-3d89-8bd7-fb50999b6e71 | -10.09503 | -48.85509 | 2026-09-18 04:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6aac5f6-3dca-332c-95db-2b975f50c2e9 | -9.95583 | -45.45578 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8506e7e7-6c03-3660-8f5a-02323caa4a82 | -8.84438 | -45.91529 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 294a059e-aa10-3224-bfa5-cc6ae24a5a11 | -7.52209 | -44.93574 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 018ac201-95c4-3eb3-a0cf-8b2fbff6f884 | -12.28973 | -50.75374 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1263af5-2e6f-3f3c-a1c9-cae97a81e167 | -7.94348 | -44.81441 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e6bc107-cc61-3ac5-bfca-8471b07153ca | -9.73977 | -46.1091 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eb6a186-9ed2-370d-a246-121af25e8c95 | -12.3028 | -50.73672 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aaa5e28-dcf9-379b-b6b6-bceb36448102 | -11.87819 | -47.58344 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4782cb73-63a1-3662-b6ec-531e2ecf541e | -9.54457 | -45.45765 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c01f0ee9-6b90-3659-a251-0c69df3fc693 | -9.83449 | -49.2293 | 2026-09-18 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b7c1cb-517d-362f-82ae-5b428e1a6e91 | -10.40263 | -46.62526 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80ff57e6-37b0-3051-a95b-ec78f9f3e4a1 | -5.8286 | -49.95513 | 2026-09-18 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7af1e1b-1ec3-3060-b18b-1bc9e2b3587e | -12.05553 | -47.50801 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6dcfe47-a1ff-314e-aab2-9c4a3eae3fc6 | -6.66066 | -50.92029 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f39527fe-e6fc-35e4-9039-23432d694bf2 | -10.5406 | -44.84741 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51e67561-ea7b-30d3-8ba4-492c966f02f0 | -10.83702 | -44.96088 | 2026-09-18 04:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ead3fb88-3d60-3215-bb55-2f0523ab4866 | -9.9114 | -46.56712 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7ee1d1a-961d-378e-93a7-44f878f2806a | -11.8881 | -43.81718 | 2026-09-18 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ef95ec7-5c23-30a6-907c-ee8aaf8aeeb3 | -5.86423 | -51.94881 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97ea715e-e1af-3c8b-a067-1615fb8fc228 | -11.0195 | -54.15154 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18dc575d-f368-3732-9844-996ee6f20b23 | -9.1867 | -46.74589 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 836dbd11-686e-3e07-a6d7-0f5ce29d3f92 | -12.27444 | -50.78559 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acca836d-ce6c-33b0-a9a6-3793a86cbfb4 | -10.66379 | -50.46824 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 00662e28-0cc4-3bfc-b5b4-ac04d08b37ed | -10.52072 | -46.72657 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a30f05fb-fd98-3e65-ad04-0316b5493c21 | -6.47601 | -44.1929 | 2026-09-18 04:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0c27779-3937-301e-bb92-c3406fc61db9 | -10.66839 | -50.27935 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3536186-74b9-326a-ba63-d1d2a8779ef4 | -7.61915 | -44.79712 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 286a0058-c9dc-3ab0-8cc6-41a16c0ecf7c | -11.5546 | -46.89141 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 497f6752-9e50-36aa-a9aa-a451692b41ba | -9.95549 | -45.68279 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b4f8758-fa84-3a06-80ad-08d7cfa90c15 | -4.77302 | -55.71148 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72751a17-aa5d-3a33-800a-a2e97c8e1a10 | -7.39685 | -44.49731 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba857091-ef70-35de-b314-289bba0887d1 | -10.64441 | -50.22974 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84648430-dbce-39da-b2e0-40e905550f71 | -12.99217 | -46.92142 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7807c16e-93fc-3495-8e9f-7cef0fabba0c | -9.71232 | -54.82259 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd87eecf-c5a5-33cf-a600-169623998da6 | -8.51461 | -48.49988 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0425ebc4-8f00-3e8e-a994-6fefaf615b0d | -7.08045 | -41.75739 | 2026-09-18 04:57:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4cc41bc8-db01-351f-84da-b9d069f06074 | -11.47568 | -45.72306 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad6337ce-b42a-3181-98ea-66b5bfa55e2f | -7.79989 | -44.84208 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62c60d18-4a39-337d-af81-a7ac4a8b1c41 | -6.66249 | -43.63276 | 2026-09-18 04:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14262f63-76ee-377f-87b2-6fd766e287d7 | -9.94699 | -45.45439 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 297225be-76f2-3b07-b0c5-a7c6cece61e2 | -9.39002 | -55.97047 | 2026-09-18 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dca73ae-4d65-379a-a43d-c87cfffc4f52 | -5.85731 | -52.03502 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca840ef8-c4c3-3585-8aa7-6593c112ad37 | -12.30054 | -50.75163 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc098b11-ad40-3412-954f-0709b8c72158 | -7.67649 | -46.10251 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 236ef64e-e7f6-3963-8bf7-dec76afe0874 | -8.64983 | -47.37937 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 337fd9a8-a304-33e8-9152-86621b5d545b | -11.63546 | -51.58443 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e0bee6-0591-3d0f-8ff7-4ed8e0f865b5 | -9.08696 | -45.72112 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8460f8f5-ecfb-3a38-9fe6-10585d751d78 | -9.74452 | -46.106 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87d2afbf-bbd5-3b69-a0f0-b5e0be718873 | -7.28299 | -49.08046 | 2026-09-18 04:57:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4d9c992-7b43-3ffc-b2f3-77ec04584e10 | -7.06083 | -47.47447 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cc6fef1-92fa-3d02-a3b7-df358a103c48 | -6.96554 | -42.57262 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e194b1b5-4ab4-3004-8a5e-67d4ac866fea | -11.98147 | -52.45981 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 085c37c6-7ab0-3343-abcb-75c848b1c018 | -9.9366 | -46.53772 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61bea688-dcf2-3331-8b9f-42b3d7c83516 | -5.14474 | -55.94599 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d78e2dd-d221-39e1-b605-fbb1c2861346 | -10.67466 | -50.28413 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91dd45a6-d23c-3156-aca2-92434a5f9ba2 | -6.72593 | -55.62753 | 2026-09-18 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f264fdc7-e8f7-30cd-a165-f9b96e435459 | -9.70881 | -48.15058 | 2026-09-18 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73a39e36-e7ea-35e2-825a-ba7c97c9b93f | -8.99021 | -54.43162 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28a4c525-9938-3028-9f30-3fedc2b4a7ee | -10.49595 | -46.29197 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0962fd48-d29d-30e2-9310-2013ab0db226 | -10.67181 | -50.27987 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b743bbaf-7e33-304a-af50-a75145699958 | -9.60596 | -45.84285 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b88c8c-afb0-3fbe-84bf-5bb614dbfdd5 | -8.23768 | -50.65661 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921eb5b7-9d95-36b6-8c7f-46307b67a89e | -10.02054 | -45.50922 | 2026-09-18 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b09ed2a4-6dbd-3c58-85b4-bce78f9117fa | -11.52858 | -46.85331 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c7df8ec-0333-331a-8c24-487ff6874d74 | -11.47351 | -45.72081 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b82aa86b-f751-36cb-99e3-a891048b8377 | -12.16671 | -46.98779 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27022384-90cd-3b7c-be20-ade535b9d6d0 | -5.86454 | -52.05445 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ffe0f0f-10d3-3eca-a1ce-35a27157ad85 | -8.85289 | -46.97429 | 2026-09-18 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac8680e5-47b3-37e5-a929-4f2380ab384b | -6.13944 | -57.69117 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6975f70-1450-3bb1-acc6-47beb0f4e7d5 | -6.32987 | -45.66954 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec66eb43-9094-3dee-a988-aec81b655183 | -12.39073 | -48.46796 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 07e3086d-8df3-30d8-b3db-680f60203f3c | -10.12942 | -43.95608 | 2026-09-18 04:57:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47703ec3-593d-37a0-8348-b42bfe1ce221 | -9.93356 | -46.52959 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 335d3b69-5931-3c6f-8f19-90b0bda5ac27 | -7.34842 | -44.63692 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98d5d3b7-923d-3051-9cda-ecc510704e0a | -10.59218 | -48.68687 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4933cc63-4051-3a9c-b4f4-6a109bfebd64 | -9.91151 | -46.50705 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1a2ed90-8e50-3def-bf65-5f5cdd739f5c | -11.81048 | -46.80666 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 505ce199-28c6-30e9-84f6-851766a66bb1 | -6.01888 | -51.76742 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c0bcc5-9074-3950-a0da-ed2564a20fe4 | -11.77238 | -47.42923 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81b768c4-e817-3335-9402-635c494dd7cb | -5.57503 | -51.47104 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44ad2bdf-948d-35c6-83e8-25cf665b38a6 | -9.95338 | -46.59599 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README60.md)
