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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee895ff-f986-344e-9704-4a919b2e7e58 | -6.8057 | -43.75389 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 396623f6-3002-333e-a7ac-16c709beffd0 | -5.72515 | -45.53791 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb19618d-9c6f-329a-a8db-b1dbc11de97c | -6.87197 | -44.44986 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593956d7-65db-3050-90ae-9754baa38b5a | -5.84516 | -42.52754 | 2025-08-30 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94dc2f9f-9e8e-38a9-bd36-e976cd022f60 | -6.31822 | -42.53161 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bd305130-e57e-36de-866c-a451fa54aeb7 | -7.20827 | -44.05523 | 2025-08-30 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ac3d7e4-0323-399c-afa3-85df4ca12280 | -6.50021 | -43.53593 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc19f9ae-b707-3474-a0bf-08cf840b8985 | -6.18683 | -43.31878 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5820073-947a-380e-aca2-bf3c90f09013 | -4.50358 | -47.29108 | 2025-08-30 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 090d232d-c54a-3adc-9fb8-f770e754a5c4 | -5.75151 | -45.37059 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 452aa976-fd86-3bcd-b657-11df4219cbc9 | -5.82266 | -46.36325 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6b3accfb-e627-36ef-8806-ef6b1d8b6eae | -7.21775 | -45.43719 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| def77255-4691-34e4-a01b-5aecea8a664c | -6.80775 | -43.7246 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c20bed-9e6b-3377-815e-327d4504ffe1 | -7.09372 | -44.3138 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ba14603a-4f70-353d-8a8c-2cbdef6184f9 | -6.42193 | -44.17316 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 71d8e636-3dac-301a-86c8-520b12576b1f | -7.08145 | -44.28321 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f299668-d63e-383b-9359-3f079be72f64 | -6.23868 | -41.81271 | 2025-08-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 684b8af1-03dd-315c-b4cb-4ddf7e35827a | -7.90833 | -44.78359 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6fb12d7-cae0-30ed-9dce-45d1d72651ad | -7.40116 | -46.02053 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cabc1eed-f3c5-3325-8268-612cc7509bfb | -7.40683 | -49.51648 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f30a3a77-1cb2-3b0b-980c-4d4c2920e158 | -5.92175 | -43.35912 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b69b733-9649-31b4-a8ef-fa13b95291f9 | -8.05079 | -45.417 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9c78690-b397-3d06-9e5b-3a527f33b58b | -7.40975 | -42.06467 | 2025-08-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0814342f-562f-32d1-ae4c-05058cb2bd73 | -7.64218 | -42.7162 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08a8eb5f-569a-3ac2-ab3c-0d0e1d38789e | -6.52511 | -44.86606 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76146fac-3c9d-3ba4-aba4-5964bad61fe0 | -5.59703 | -46.23845 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72bf19f4-fc15-3abd-b31c-dd6aa2109694 | -7.75489 | -45.46202 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e3b22a8-661c-344b-8efb-0455194a7f33 | -7.60219 | -42.71035 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72e78d0e-5ebe-3621-be15-de0a514cd80b | -6.38203 | -44.69177 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82210dc8-978e-33f6-868e-0c23318b8343 | -7.10896 | -44.5868 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7886a8b4-98ca-3b45-83d0-aa4da9363174 | -3.62668 | -49.19517 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70d87478-b0d3-3b0f-bdf8-d2925b49eaa9 | -6.20619 | -42.7581 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ccbf8881-13cb-32a1-9a49-284da1262a15 | -7.60278 | -42.70646 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aaab095c-8b24-36b7-9000-aa2842a9428b | -5.69297 | -45.95913 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b357ed2-4bce-36a2-8bdf-a4f2794a7a8b | -5.82324 | -46.35961 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b23366f3-0ede-30b7-aaa9-059f2dd8b353 | -8.14237 | -41.1815 | 2025-08-30 04:19:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7cc22f63-befd-37e4-999a-9b918c7aa465 | -7.01729 | -42.03023 | 2025-08-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3af8b16d-d2a3-354f-8ae8-4f5d4b4b77df | -8.47847 | -43.68144 | 2025-08-30 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaaa88ba-3dbd-3991-ba23-51e5212ca39b | -7.11647 | -44.58442 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f03c4316-3967-3212-b903-148910ed08e0 | -6.17283 | -43.34249 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b76d91b-64f9-3926-9adc-2e20736fb8c4 | -6.37916 | -44.33723 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba91262-d6b5-3817-a771-b054760b9b29 | -7.72382 | -50.30483 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48ba3844-e9c2-3b09-9dad-ff1f55239b41 | -5.44999 | -44.82325 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdfa284a-0295-3748-bed4-c0d2cfc06e3d | -8.15893 | -42.30727 | 2025-08-30 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0ff8008c-b296-32cd-8cfc-411e72547380 | -7.77857 | -45.4622 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad02dbd5-55c6-3ecb-b6b8-cdf6b1b49245 | -7.16293 | -45.1584 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aeec068a-0f10-3994-bb2f-7dce1d85347a | -7.68227 | -44.98953 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64be3321-7514-3766-b081-a75a933f15fc | -6.44822 | -43.98045 | 2025-08-30 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7317800b-23cb-3d39-9088-02d878890f1f | -8.45742 | -43.63712 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa8fa6be-de06-3413-8edb-c3a353865cc1 | -5.91894 | -43.35501 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e048ce39-bc38-3f2d-bf2b-0464d454571f | -2.34663 | -47.58452 | 2025-08-30 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ee1483-7f85-32fd-894c-70d71c32e447 | -7.4375 | -44.81596 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92b93fba-2f72-3734-90a1-5aeaa2fa045b | -7.7259 | -50.26847 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d799a05e-660d-3a02-bde8-28997995a7ca | -8.47004 | -43.69134 | 2025-08-30 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a978d35-a5ec-3f52-8200-d716d27dc492 | -5.91839 | -43.35859 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d2d68ba-7055-3f08-b625-10e8c3114fb4 | -6.45166 | -44.63907 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef1c359c-9f3e-30a1-a3e5-cb807a5118bb | -7.15006 | -44.91211 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4caa516-7c02-3563-a5de-e70d6f544466 | -7.63228 | -42.66298 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75496275-0ca8-3943-8ebf-21996703635b | -6.56274 | -43.68031 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e92c529-c311-3274-9419-9648debc6927 | -7.63635 | -42.6596 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d54443b-3131-32d3-965b-bb41a093029a | -8.11193 | -45.00436 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdefca44-8a24-3869-af3e-75fc5b04b460 | -7.58579 | -45.1304 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 624f936c-0002-353a-be6f-816b05fe366e | -5.11248 | -49.7699 | 2025-08-30 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b28548d-dc8e-351c-a3d5-01abedcf644d | -7.60908 | -42.73517 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 756d803a-303f-36f6-85a6-8d47018f2327 | -6.21593 | -42.7634 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 25fb0913-edda-3a07-b867-0fa980acb318 | -6.78166 | -43.78242 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 64a1a1d8-2384-3444-adc2-971a19f4f649 | -7.39954 | -45.92299 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee8d3fcb-0509-34b8-8a27-eb73fe5a932c | -7.34683 | -45.24458 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45d3dfa3-4bdc-39ce-a90b-27d196f7221d | -7.40813 | -49.52428 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36160f80-3ec2-391e-87f6-2d54caab3224 | -6.65624 | -43.93332 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5922f49-1e2f-3fad-acbd-71793f4c05ee | -7.59818 | -42.68982 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be0a4334-959e-3d67-9a28-3e4b97949ef3 | -7.1576 | -45.23549 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a20ddc9-1448-367c-9004-0e3ead2bb8ae | -6.48711 | -44.41081 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80e80d65-4ee3-34b1-b256-740b95fd65b6 | -7.41096 | -42.05642 | 2025-08-30 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91c20eda-cec8-33cf-be25-f3cb413976d0 | -6.90873 | -44.38794 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 315e1ac8-305b-3e07-be7b-f8442507ea2c | -6.23808 | -41.81676 | 2025-08-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d1150ad-f2fa-3175-b237-787e370b15c9 | -5.87629 | -44.33603 | 2025-08-30 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b1b1f01-8d84-3ab5-a56a-025dfa32d7aa | -5.53624 | -36.85295 | 2025-08-30 04:19:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| affcc7f3-f743-3a41-b750-bb26b1f28523 | -5.78752 | -42.56229 | 2025-08-30 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb8707ff-a0ab-3b7f-a1a8-4892f82d4535 | -6.56081 | -44.2197 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1307e0dc-8593-387b-95f0-af0493ebcee7 | -6.34649 | -44.45987 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b674ab1-b10e-3882-bc20-5fe1afa8ebcf | -6.18009 | -43.31772 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d970a04e-b18a-35c0-8863-0302d8fef9e0 | -6.65569 | -43.93683 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 240d349f-6cad-3317-a39b-2547db71b5e7 | -5.58996 | -46.32644 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaed8f52-b9a3-3c84-adb0-31311bb29d4d | -3.11079 | -47.49487 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38a51146-c2cc-32bc-b26b-a742a58c0109 | -6.79215 | -43.73677 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48b1306e-a6a5-3ca1-8e02-a153489470eb | -6.05931 | -44.77498 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50a2dd58-8ed0-364f-9abd-58dc56cc8144 | -6.31944 | -43.60263 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31251293-a6b5-3218-861e-a759cc75dea3 | -6.48903 | -43.54154 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2058ec5e-c8c1-31a5-b99e-b64f41206e1a | -7.72102 | -50.29689 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 657282f3-60e2-3d21-b079-37d58b94173e | -5.62193 | -45.24363 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82a2eceb-6d36-360e-9d67-75beff1698a8 | -5.71107 | -47.42944 | 2025-08-30 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c2e0e83-0b04-3299-b447-879b8e82144a | -6.17554 | -44.79306 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95a1ff69-ed5f-36e6-a272-584523c107a9 | -7.59234 | -42.70484 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22059846-2403-3a01-af48-d6b754dd6429 | -7.21439 | -44.05979 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09dd844a-4bca-3746-8263-44806030f57f | -7.59983 | -42.72582 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59e59fd9-e979-3052-9115-b005e9f1db5a | -7.73857 | -50.26714 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72d7e1f7-202f-3b27-b75f-25f2678e916b | -7.40323 | -44.29068 | 2025-08-30 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8487d461-29aa-32e3-8626-c6aa96554c70 | -7.15422 | -39.42129 | 2025-08-30 04:19:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af90f5e2-67b8-327b-901b-69b26e7c946a | -6.65793 | -43.94438 | 2025-08-30 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
