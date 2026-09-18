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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80652806-33c6-3da6-83d7-a60a2a2b0d4e | -3.36012 | -50.45929 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2fa45ed8-52c5-31f6-a021-95e8f81efebf | -3.3705 | -50.46089 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 89dba99e-d087-32b0-a785-583367ab4c76 | -4.98462 | -37.37521 | 2026-09-18 06:44:00 | AQUA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 1acfd587-f9e4-3764-be93-579a74f73b92 | -5.14127 | -47.60105 | 2026-09-18 06:44:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 982067d6-2a12-3d78-9dd8-273ef45db273 | -4.58636 | -42.95399 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 9579f688-e9f2-3547-be3b-14fcc7155ddc | -3.364 | -50.43436 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e626a27b-e474-3a42-ae58-9e7e11d8138a | -4.56547 | -42.95102 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 172eff57-d6fe-31ca-9c51-21f59afea9eb | -4.55683 | -42.93686 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 97f70cf9-d7b6-3bb2-b27d-0d6bfe81f561 | -4.57591 | -42.95253 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 982ec412-43bc-33ca-94e7-8aedd22b7674 | -2.8151 | -50.46906 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 0c7d5b1b-309c-30a0-bbb4-91218f0c65fe | -4.56729 | -42.93828 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 390030e5-3ea0-3603-b52d-ec9aee2105b9 | -4.35627 | -47.77914 | 2026-09-18 06:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b6c843a0-9950-30b2-983a-011ab1eac9d2 | -1.78685 | -47.83476 | 2026-09-18 06:44:00 | AQUA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f8954888-ecdc-33f6-814e-dbbf23176991 | -3.03304 | -51.37124 | 2026-09-18 06:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 752d640e-2a03-3bf4-aa73-359ab8e2152c | -4.36513 | -47.78046 | 2026-09-18 06:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4fa5b955-db15-3dfb-b3b6-bb782421f9d4 | -2.82756 | -50.45778 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 981b8cc9-3a02-3f6d-b522-7879a44bb8cc | -2.60752 | -54.75468 | 2026-09-18 06:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| cae49ed4-5667-3acd-a15a-011c398b5028 | -10.51632 | -46.72132 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5511f479-23a9-3715-a249-a863a0447a54 | -12.17701 | -46.97775 | 2026-09-18 06:46:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5dae3a3f-479d-3b87-9371-28f28d0511bf | -9.91901 | -46.5717 | 2026-09-18 06:46:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ee82e3bc-31c0-3454-952d-e4e1c643eb10 | -13.23615 | -42.31953 | 2026-09-18 06:46:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 32c0519d-9a26-3199-bcd7-b79a1e538d6c | -10.82232 | -50.17672 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 90767827-bc82-310c-a648-d65b400ccaf8 | -9.76782 | -46.60023 | 2026-09-18 06:46:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b93e0c24-c9fd-3bfc-b3b5-85286dd04580 | -10.48482 | -46.30229 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 321ee18c-5381-33c0-8d77-e94ebb5e7f62 | -10.10051 | -45.64236 | 2026-09-18 06:46:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c57034a6-bef8-3d87-84a6-f7dfc7d6a86b | -12.56693 | -47.08986 | 2026-09-18 06:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e3dfae6-6293-339f-97de-9457478f6076 | -7.78894 | -44.90452 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 565448d9-4c68-34a9-aa7f-4b7631b5df4d | -10.65881 | -50.44965 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 89aa6618-1697-3e42-9782-e7900bd95556 | -7.93007 | -44.83365 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 74798948-e1be-38d8-8230-74aad7f48dbc | -11.55342 | -46.89091 | 2026-09-18 06:46:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7b0d0f2a-f7d6-35d1-852e-a93d1c9fb83e | -12.39059 | -48.46238 | 2026-09-18 06:46:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a7ce2823-428b-3b12-a302-2229748f40e4 | -10.66813 | -50.45115 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1ae1962f-f635-3e72-b4df-b4eb9077ef5d | -7.93166 | -44.82268 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7ab40110-fe7e-3eb3-bd6a-f52d98e4fbd2 | -10.6798 | -50.25823 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9f01cc7f-4f87-3350-9212-e40862334b3b | -8.91014 | -45.00793 | 2026-09-18 06:46:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3635295d-1241-3a02-8478-e808b3b208be | -9.54403 | -45.46199 | 2026-09-18 06:46:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35277cb7-ee7b-3614-b29b-69f674e75eae | -5.74973 | -45.09765 | 2026-09-18 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 14ddd789-606d-3bc4-b355-cc8a6703eefe | -7.00363 | -43.87162 | 2026-09-18 06:46:00 | AQUA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 84342097-a128-3e4d-a362-81ecff5f9a8c | -11.8767 | -47.57825 | 2026-09-18 06:46:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d3f20af2-7e30-3d1d-8e96-63cf2c2b777f | -9.39663 | -46.85913 | 2026-09-18 06:46:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e02e0276-38fa-354b-aa43-fd0340b57286 | -7.81915 | -44.89835 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0903116d-dff5-3337-82dc-63ea7eefa073 | -7.66364 | -46.0861 | 2026-09-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ff78d4c3-5d11-3be2-8a6c-4e9210382f7d | -9.9523 | -46.60148 | 2026-09-18 06:46:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7b04f320-c2ae-327d-912f-e072f1def78c | -10.11701 | -46.29291 | 2026-09-18 06:46:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 944d19e9-dfcb-3c2f-bc33-6610e2f9d8a1 | -10.49684 | -46.28408 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2f9c4f89-519d-3e9e-984f-f37f00d750f7 | -8.48811 | -46.87539 | 2026-09-18 06:46:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 591ba0d2-43c9-3744-9129-200850d344fb | -12.38924 | -48.4713 | 2026-09-18 06:46:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e2c852ef-32a4-31c6-8f8b-243a99bc7cd6 | -10.01879 | -51.10187 | 2026-09-18 06:46:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 9359fa41-810e-3577-91f8-68894af6915a | -12.16815 | -46.97972 | 2026-09-18 06:46:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f7f8b951-7f6d-30f9-960a-42227f5c3fbf | -10.67215 | -50.24687 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| c0ba8423-faf3-3b14-9331-e4a32593e754 | -5.7604 | -45.08926 | 2026-09-18 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c5c8071-7e09-3e25-89e1-beba6f7ffd70 | -10.67057 | -50.25676 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 675c5302-7f9d-3254-b0bc-8edffa799228 | -10.65591 | -50.23854 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fec4cef2-ff57-3f3f-a663-0849fc4cac0c | -10.1297 | -45.57357 | 2026-09-18 06:46:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9f82910b-0296-373a-b003-fb8fe88556ea | -13.24772 | -46.91709 | 2026-09-18 06:46:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 9c72d25b-69e4-3002-b6da-93be91dec12f | -7.67888 | -46.10735 | 2026-09-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7aa93a6-3750-32f6-bfcc-3abef5f38606 | -10.61205 | -46.56841 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f6649daa-7988-366c-b173-dc5483baece9 | -12.5295 | -47.09334 | 2026-09-18 06:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| abd99629-c879-34d0-ae69-ae22682c5e59 | -10.66899 | -50.26665 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 751c24bc-20de-38e6-8127-e600d644d29d | -11.67091 | -54.44748 | 2026-09-18 06:46:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 47646824-d1d0-32fd-a659-486eb48eae05 | -7.00531 | -43.85962 | 2026-09-18 06:46:00 | AQUA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 74f52fe1-496a-3e70-984b-a0b921bafb65 | -7.01835 | -43.63175 | 2026-09-18 06:46:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 13d230e6-e518-34b1-a1c1-7bbad12b17b8 | -7.68165 | -46.08875 | 2026-09-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cae67d37-6011-3a9d-8129-110188bed18b | -10.66134 | -50.25528 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ad0427f9-3cdd-305c-b5cd-6f349b8261a4 | -10.66292 | -50.2454 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 60a436c0-0869-318c-a0e3-aa34409fce45 | -7.79345 | -44.87302 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 03c0a3fe-cb55-33a5-b945-ee5951dc388a | -10.49541 | -46.29387 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 47b271a6-49cd-3ee0-9ad2-ad99b8bdf702 | -12.39801 | -48.47264 | 2026-09-18 06:46:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4e690092-97a5-3f01-a687-2d1b63679f9c | -10.48341 | -46.31193 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f517a787-fff2-3fc7-97f0-a76eeb341e97 | -9.84346 | -48.38584 | 2026-09-18 06:46:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b609e833-5522-3418-8656-16d941197533 | -9.70653 | -54.81778 | 2026-09-18 06:46:00 | AQUA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e8a66e75-16e5-3570-95f6-fc28f44dd4db | -11.05828 | -48.29892 | 2026-09-18 06:46:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c9c49496-dafe-37d0-8eed-cdb559dbcbf2 | -10.67822 | -50.26813 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 98076f7b-2bae-3406-a47b-23cbc4b96f8a | -9.86372 | -48.3708 | 2026-09-18 06:46:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 52dbf66f-46e2-3242-9bda-b0f11cc9d10c | -13.23362 | -42.3395 | 2026-09-18 06:46:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 436ada2c-5d41-3b3a-95bb-2d2ef3c2ea8d | -7.0611 | -46.22487 | 2026-09-18 06:46:00 | AQUA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9386c6fb-8f4c-3a0d-a4c1-99b7618ba28f | -9.46337 | -45.44489 | 2026-09-18 06:46:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3ffeb575-4b9e-30c0-a422-fe8a0ec42060 | -8.45849 | -44.5113 | 2026-09-18 06:46:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 75e9d0cf-376c-35d2-9567-cfb38c873e56 | -7.00803 | -43.63029 | 2026-09-18 06:46:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 677d953f-964e-35d4-b4cf-1c67204c2157 | -10.6572 | -50.45976 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| c080c891-e83c-348c-9163-0bb62746e9c0 | -7.68026 | -46.09806 | 2026-09-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c67b55c2-15d7-34cc-a6b9-36445d524d87 | -9.85359 | -48.37832 | 2026-09-18 06:46:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d1882ae1-b23c-39ca-9aa3-031d80004815 | -10.68903 | -50.2597 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 911c1d3c-c6cb-3f0d-afb8-43a72d1fd438 | -11.07107 | -48.27366 | 2026-09-18 06:46:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f2d8f4a-67b6-34a3-9c25-13cfe57e0173 | -6.12216 | -44.01815 | 2026-09-18 06:46:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1e5af85e-9d38-34cf-976d-809468acdf53 | -10.61344 | -46.55888 | 2026-09-18 06:46:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bb312c45-6be4-306a-94a4-0db608c7f3a5 | -10.59133 | -48.68631 | 2026-09-18 06:46:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81956362-db98-3993-901c-ac5ca2e76429 | -7.86237 | -46.42634 | 2026-09-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 180fa409-5a9d-32c9-bfb0-723dee25d34b | -7.39532 | -44.49831 | 2026-09-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4acacf05-a690-3a40-9a3a-854e520a8e19 | -10.65436 | -50.24843 | 2026-09-18 06:46:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 82fec75f-28e8-3aea-9ccc-25e53e8ca225 | -9.7048 | -54.82261 | 2026-09-18 06:46:00 | AQUA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| add9fa54-6d5f-3b07-872d-92259ccfb635 | -12.53086 | -47.08384 | 2026-09-18 06:46:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5d17ef9e-9570-39d4-9478-c0bfd5efb8a9 | -9.85495 | -48.36945 | 2026-09-18 06:46:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0e8595f8-9c74-33e3-81c7-a68cd2c7d05d | -8.88376 | -45.88805 | 2026-09-18 06:46:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 58bf5a5f-008a-3df0-b0c6-0dc56f0f51aa | -12.31132 | -47.9585 | 2026-09-18 06:46:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 993b5830-c586-33b2-a17e-55a0b14c16c0 | -11.06973 | -48.28252 | 2026-09-18 06:46:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 64cc98c1-fc85-36cb-b541-1537b9799c8c | -11.27909 | -43.35542 | 2026-09-18 06:46:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2903c24d-b678-309b-8e62-212b22fd56fb | -12.16958 | -46.97003 | 2026-09-18 06:46:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 133a7bb0-71b7-32b8-8524-d1516c8e164f | -6.12044 | -44.02983 | 2026-09-18 06:46:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cbcd08b7-50e1-3483-88c5-25f3992eb5d6 | -10.98431 | -48.299 | 2026-09-18 06:46:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README89.md)
