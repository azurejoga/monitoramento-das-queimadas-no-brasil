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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f370870-988b-300a-af09-3b90ca936cb8 | -4.36102 | -54.75659 | 2025-09-10 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e00d1a6-f0ec-3669-ac8d-984fd74a16b5 | -5.74598 | -47.47845 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46fe151-159a-351b-80be-70623ede185c | -5.66563 | -43.35079 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e3133c48-e46a-363d-bcba-dd3401021750 | -6.20524 | -45.62414 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1865fe71-1ba2-3b71-9473-d786e4bc5db3 | -5.67716 | -43.36404 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43032860-0317-38a1-a91b-3a03e2780e40 | -6.56541 | -43.15006 | 2025-09-10 05:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd20856c-6bd9-3137-94f6-266bfd14b418 | -3.96459 | -43.24331 | 2025-09-10 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29936578-d087-3701-ae52-90a8a60cd445 | -5.58037 | -42.92169 | 2025-09-10 05:01:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d68a8a72-09fd-3b2e-9460-1ff027b0c1cd | -5.1205 | -44.674 | 2025-09-10 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 841cee7f-fdc7-351f-840f-ecb736f998f2 | -5.57695 | -45.04268 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1d10c4a0-c6cf-3f6c-bb46-a0287205a57e | -6.25447 | -43.4049 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 02970629-cffd-3784-9bff-6469d40d00a9 | -5.63963 | -43.92181 | 2025-09-10 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f46f01c9-f1be-37b9-be2d-59e88dcfce21 | -5.66747 | -43.34428 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 075cc0cd-c522-3e2e-938c-0935c382d362 | -5.66773 | -43.9051 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 253702bf-d184-3bd9-9bb7-dc4da602ec59 | -4.28156 | -56.33344 | 2025-09-10 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4dcc161-1781-3ee8-8ff0-d24fa380a41d | -5.67212 | -43.35207 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 652da3e4-cc1b-3a6a-a322-20e99b3c678e | -3.20867 | -54.95761 | 2025-09-10 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50c5415c-7602-3f86-aeeb-18976842a246 | -5.71986 | -45.41859 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9e56b3c-285f-3bfd-952c-bb723eeb9385 | -5.57753 | -45.03856 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 137cc7c5-c37e-3882-859c-a59113a209c9 | -5.54759 | -45.37646 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa6ea0ed-b2ef-3ecc-a1ce-920b2d3bcadb | -5.86386 | -48.15979 | 2025-09-10 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45fd30fb-ad25-3143-a05c-83fbd3a260ef | -6.25289 | -43.4164 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 95e7cc45-88c3-3a1e-8d43-200eeb887521 | -4.83805 | -45.35523 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c47276f-6345-333e-b0d1-80c1b5fd12d4 | -5.67363 | -43.34092 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d783170-24e1-3c13-8627-9a6e974f60ca | -5.45065 | -43.47176 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 583b5c52-aa8c-3b7d-be05-2c54f688391e | -5.4125 | -43.46125 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 371567f9-e3bf-35ed-99f5-582bf2b3859a | -2.09757 | -52.02942 | 2025-09-10 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5875771e-7558-3574-9243-0ec0c6449242 | -6.19486 | -43.50011 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 339b4b54-93e8-3f31-8bc0-aa966deeca9d | -6.20577 | -45.62046 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b82e12f0-7df9-34aa-ac4b-372cfdc9a8d9 | -5.6874 | -43.33773 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19b53dde-61d8-307e-a14c-46306a2a0970 | -6.20714 | -45.6235 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53579619-86ae-3e95-a56c-f043f6fbc181 | -4.9749 | -48.942 | 2025-09-10 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 94210770-4949-3477-98c5-73041e0e376d | -6.21331 | -45.62094 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67936e8e-5d09-340e-9b85-a5c205ec4827 | -4.35742 | -50.62225 | 2025-09-10 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77942a6c-0b92-3d73-ae15-ca9c8b33e49f | -4.09356 | -55.80645 | 2025-09-10 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce1e05b-a167-347d-828c-c954c3139b62 | -5.66076 | -43.90885 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 392b67a2-d3fc-3ede-b07c-b8d13d4c1a13 | -5.66485 | -43.90224 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a42fc6e3-2cc2-32dc-b816-4ec08a7ced15 | -5.54702 | -45.3805 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1773f6a5-1044-3b38-8437-daddf6b37ca4 | -5.66845 | -43.89999 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5deeee32-bba2-3a7e-ad46-89ae6b9ae459 | -6.20782 | -43.5026 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f84baefd-9938-309b-ae37-3b68dafcde04 | -5.93882 | -42.78681 | 2025-09-10 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77afd469-11ad-31a5-861d-50a026378151 | -1.9967 | -56.49607 | 2025-09-10 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4104c241-8293-3710-9326-4125f3157069 | -5.22792 | -43.69115 | 2025-09-10 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e7416f1-864c-302a-9438-143edf5bd9e4 | -6.26029 | -43.41124 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c963f218-9b96-3598-b31f-f05395ba2ec7 | -4.50013 | -47.82469 | 2025-09-10 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dea0f46-8072-33a9-8608-7a9db38f50fd | -5.42039 | -43.45166 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b67ed30d-141c-3840-9297-164c40263bc2 | -6.25878 | -43.41217 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| b254b401-e810-3a20-8134-7a8583cd4686 | -5.58342 | -45.03927 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 26e1b883-6dcc-32df-9b5e-52c693b684ca | -6.25366 | -43.4108 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8e641cdd-7da6-3f0a-b65e-5727e3d83efd | -5.68124 | -43.34124 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef25bc2-efe9-3472-a414-8c6d199fb991 | -5.67136 | -43.35767 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7057661-7c86-3109-b524-64248880a711 | -3.04447 | -48.96192 | 2025-09-10 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d5f350-c226-30f3-a949-6635bf2b2073 | -5.6755 | -43.89575 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0ebaf87-9f1e-34dc-bc69-e5aed1c9713b | -5.67186 | -43.89798 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 740ecd5c-1c01-37a1-9691-3257ee8de65e | -6.29751 | -44.21662 | 2025-09-10 05:01:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 794a8000-e7ca-35b7-aca2-daf1454ad03d | -4.20296 | -55.13472 | 2025-09-10 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b006210a-9cc8-37d2-8ccc-2b91a8cad86f | -4.27452 | -48.19139 | 2025-09-10 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f439d6aa-fd91-30ae-8ffc-24333dc5a6e6 | -5.74216 | -47.46932 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dc01d8c-4c62-381b-8fbb-d867703c5db8 | -5.53256 | -42.6567 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fc43ab6f-dcac-330e-bf3c-335e9a9a6dc0 | -5.41968 | -43.45693 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d41d55b0-50a6-31fb-8b03-f6962baccd06 | -5.67474 | -43.34008 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aff941fc-4e04-32d8-ac2f-6d3cb81614f8 | -5.57289 | -42.92635 | 2025-09-10 05:01:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d287fea0-5686-37ff-bd85-107dc0b2d8f2 | -6.24712 | -43.40969 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3d17b7ae-4c68-3cca-a0dc-f40337900826 | -4.09301 | -55.80992 | 2025-09-10 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96cccca1-b5fb-3fb3-8830-0daaafd5b331 | -4.24391 | -48.26991 | 2025-09-10 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 558b663d-c0aa-35af-9b1e-1b709bb0f991 | -4.83463 | -45.35462 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8647865-d782-3681-b3bd-c09bec8c3b1f | -3.49063 | -51.25287 | 2025-09-10 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f638c94-6c91-3f82-b2ea-a3f77887e1bc | -11.11304 | -48.41397 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 470dfba3-5bfe-38b2-8705-bbdea613569f | -8.4451 | -47.28132 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839ae528-09e9-32bb-8fbe-06cd8df377f6 | -11.44941 | -43.62899 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8419f0d-9925-3dbd-8d12-f1afb6245ddf | -10.9643 | -46.80243 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80767c24-dd5a-34fe-997a-628f9d69e017 | -7.30546 | -44.1498 | 2025-09-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e8619cd-da59-30ce-8c6c-1af738a71692 | -9.80735 | -47.76826 | 2025-09-10 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92ca1bee-8c21-321f-a266-34bf68982418 | -10.72295 | -48.28318 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e72183c3-ea4b-3f28-a04c-9716e2292bbc | -9.44796 | -46.73797 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d0017f8-25c9-3072-979c-73868fc192c6 | -9.82781 | -46.06187 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e19435da-ebb4-3c9e-90c2-3af3ee31af60 | -9.6126 | -48.03938 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34ae63f-acd2-3a7d-8077-672b9b90486c | -9.68018 | -46.897 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 924d581d-8b4e-3db0-aaf8-63439a0b5580 | -9.07012 | -45.71545 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f886539-8c98-3c85-8b6c-bb9967103682 | -12.86189 | -47.96444 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77b6149c-1779-3c34-84c6-361f6f104581 | -11.20842 | -54.98627 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0bb3258-06b4-3aef-b39a-175b8ef5fc6f | -9.98246 | -50.30308 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68c096a7-f87f-3688-b346-c2e8498f63bc | -9.1021 | -46.97474 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 76d105f7-0094-3a8b-b059-6c2e9eaf20e0 | -9.75652 | -51.06096 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e01b7243-133c-3943-a2b2-8b9c6b0d4eca | -9.07032 | -50.47984 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ef5a267-a73a-3ace-a9c1-6ccf7ccb91b3 | -9.51818 | -46.54343 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b093af7-6bd4-3ca8-bec1-930861f5aef1 | -12.00288 | -50.97739 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ec878097-cff6-3cb8-bb15-056d5d94f607 | -12.06601 | -51.0621 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1568d129-3558-36c7-b660-544c49a7d670 | -7.08141 | -45.20609 | 2025-09-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34ae90d8-d4e3-3cca-a107-a9004087a6fa | -11.75342 | -50.62626 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eb73ddba-e4d3-3671-93c8-3c88939de49f | -9.06175 | -46.98698 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 60247996-9849-3660-9776-d3721404c107 | -7.67321 | -50.27299 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db0128da-9af0-3eea-bfb5-0073cf92370b | -9.34447 | -46.75981 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bff4cd6-ca23-3777-8420-523fc1acdf1c | -11.45024 | -43.62426 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f51996d2-1635-36c7-87be-6a3680760864 | -7.18784 | -44.93494 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 784c082d-ec84-3a41-8e57-84a10d5036b5 | -12.20726 | -53.86856 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a3c67911-5b1c-3fad-8b7c-eae6f66500fe | -12.19764 | -53.8584 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b24f8bec-1b93-3129-b587-a649cff5d524 | -10.17983 | -46.22042 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3187fbaa-9c0b-3758-8e63-601a5b8fd257 | -7.77316 | -50.77456 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5990e8f6-1aff-333f-96e7-84f6e3000027 | -11.54457 | -47.32176 | 2025-09-10 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README86.md)
