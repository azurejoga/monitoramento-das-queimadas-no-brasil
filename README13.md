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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40e5f625-e8a9-37d6-923d-e0ab18ff33c2 | -1.87484 | -54.68693 | 2024-12-12 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6088a244-2e14-3fac-849d-ff34714f205d | -3.79408 | -50.1065 | 2024-12-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57d99032-affd-3a4d-a4dc-bd91ee4b3705 | -3.24058 | -46.88123 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 413c1a87-0904-369a-b6f4-81ad7180ebf4 | -3.00709 | -48.04871 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5fe0b1-110f-3f75-8d34-63091b99949e | -4.90171 | -47.14513 | 2024-12-12 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8ddad68-61a7-3f39-9363-4c5b5e6be5f0 | -4.90578 | -42.07621 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2b6615a3-98b3-3cce-8477-8ae582bf6a3b | -4.10008 | -46.67845 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b63d9f73-6bcc-3423-9dd1-27f18a4cc8f3 | -6.12737 | -42.55203 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 60155f59-4f5f-335b-87ad-36e28bd9b45a | -4.3575 | -45.92049 | 2024-12-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f376629-e012-362b-9a62-a0cba110d2b2 | -4.38764 | -42.1497 | 2024-12-12 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 124409bd-a9b6-3d04-92d5-46267bc6c529 | -4.50481 | -43.62136 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f59e3416-bf5c-3ab0-acc5-f35c326b98c5 | -3.98505 | -43.40051 | 2024-12-12 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7802529-6134-3121-b009-2dfd616bf6f0 | -6.20624 | -44.82883 | 2024-12-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e095480-2de7-3ca0-815a-15e52e801d1b | -5.23899 | -38.50028 | 2024-12-12 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7cdd9dc2-cb1f-39cc-b051-ab4179431e3b | -2.96327 | -48.61346 | 2024-12-12 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2d48a47-ce8c-3cdf-89d8-d313f2478fd4 | -4.01618 | -47.0323 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93fd0a0b-2a70-3633-863c-2979ebf75f9e | -3.24591 | -46.87249 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bf1949b7-724a-3b38-a100-f30f523e9b09 | -3.98301 | -46.89686 | 2024-12-12 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77c58d5e-17b3-39e4-8f71-afa95f6d39ca | -3.43053 | -42.98775 | 2024-12-12 04:14:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94904719-9431-360d-ade6-ec1d3269898d | -4.09332 | -46.67276 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cdbc6a0-c027-3a62-9df7-579b16d69abd | -3.83921 | -44.10767 | 2024-12-12 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad97fe0f-22f3-3063-bd62-69ace23e44a1 | -6.80302 | -40.63204 | 2024-12-12 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 683781a5-85bf-30e6-9a73-482ea22c1ad3 | -5.34899 | -44.19959 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 906071b8-c426-30b4-95b1-a123368656f1 | -4.80007 | -50.82074 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2189d79-6e8e-3a7b-9452-ed4d13580f0e | -4.49935 | -46.06063 | 2024-12-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc0e6373-8933-365c-9254-bc88bfcffbf8 | -3.41443 | -44.45653 | 2024-12-12 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee3540f-1d04-3701-a015-c9b7aa9442c9 | -2.08142 | -52.28103 | 2024-12-12 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97e226b0-b011-3a9e-84e1-1ccd37240e66 | -4.0514 | -46.66328 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b42d673-aedd-30fc-b2fa-3e652596d02e | -4.38871 | -42.14275 | 2024-12-12 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a697c6f2-f98f-3733-bd2d-06f8ef2d1958 | -2.96222 | -41.82473 | 2024-12-12 04:14:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7451285d-3900-344f-b375-0c368d8bea33 | -3.35451 | -43.17024 | 2024-12-12 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9878ff3-9718-360b-af5a-3e7068d6392c | -3.40683 | -39.16861 | 2024-12-12 04:14:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 746fb997-1bab-3c93-becc-b85ab74a3ee4 | -2.5298 | -51.78595 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dd3d43e-1315-3713-a9c6-59f9c6162cdf | -2.74162 | -47.679 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9eafd67e-40af-378c-9dd5-757b375aec7d | -6.1012 | -44.04847 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f56bb1d2-e6ff-3b98-876f-a3baab469b26 | -4.56912 | -48.47758 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f707902-f6cb-310f-af5c-85fa66ed91aa | -4.3757 | -48.75628 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c8f8522-c021-33d6-aeef-04c49bf53f97 | -3.72393 | -49.21365 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d543db6b-b525-3f5e-8c49-45a75bada5a0 | -5.87673 | -35.41491 | 2024-12-12 04:14:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b39455a9-091d-36bb-b91a-884550c6dffe | -5.08911 | -47.88894 | 2024-12-12 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c4452ca-deab-3419-b1a3-8340c2154601 | -6.1229 | -42.53706 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 366c6fad-852d-3955-8038-c17f7a7c7f28 | -6.68857 | -39.25726 | 2024-12-12 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9e9a08b-6bf3-3882-86d4-baca43f94c58 | -6.09787 | -44.04794 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8449714e-d049-30eb-808d-8ca09b0725be | -2.86547 | -46.72238 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6271dc36-bcb6-3d5e-ac3e-ac80a3970bca | -1.13941 | -47.70594 | 2024-12-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09ef8881-0de0-3d57-b699-b82b80e51fe3 | -4.19189 | -42.42368 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52cf7e82-02bd-3bd4-905e-71def574be7c | -5.16036 | -44.36236 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6c41f26-78b2-3532-839c-98daa64365d3 | -4.51148 | -44.07472 | 2024-12-12 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 280ee82b-7d90-372b-b1a7-b088a374ab9c | -4.5539 | -43.56847 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1a36f3c-b0c6-3ecc-9146-b218fb8cfc8c | -3.85657 | -40.44994 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 810eff76-fd38-31a3-8449-6f894e62cc20 | -3.7868 | -47.09632 | 2024-12-12 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d73fdda-1d91-3420-bada-41980671976a | -5.98962 | -43.47956 | 2024-12-12 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb20043e-217b-36a3-b23c-db7871acf7ed | -5.29076 | -44.91361 | 2024-12-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad0b898f-fa55-35bb-a6bf-c05e9b1f2730 | -5.07367 | -46.99487 | 2024-12-12 04:14:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f308431b-a50a-352f-8d26-438474316b6c | -2.52442 | -51.78494 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0be0c0fa-75fe-3f4f-a628-02076c06ee0d | -6.34007 | -41.54108 | 2024-12-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b7f3891d-aadd-371a-bdea-62e8a97bbfa1 | -5.37876 | -46.28941 | 2024-12-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb7982d4-de0c-322f-9d74-dd96e79d5d12 | -5.87604 | -40.17477 | 2024-12-12 04:14:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6809d573-d66d-39d6-9972-2aa1de4d9ff4 | -6.12513 | -42.54455 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e76eb515-20a5-31ab-906c-79787d1c6f97 | -5.1626 | -44.37001 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20a33d2c-c8c4-3473-84c9-8193240827eb | -5.17206 | -44.41917 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e54a4744-966d-36da-9ba1-bd18dbbe7f03 | -4.32965 | -43.67548 | 2024-12-12 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8104cd7-2a3b-3470-860d-14de29371303 | -6.77517 | -35.21809 | 2024-12-12 04:14:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d002f137-5938-3173-bc9e-2f4bf04111ae | -4.32917 | -48.72012 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24c41e25-375a-3e6f-91f4-71afa5a112e7 | -2.96554 | -41.82524 | 2024-12-12 04:14:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8061fcb4-2922-3a50-81fc-484f8aa776c7 | -3.41784 | -44.45706 | 2024-12-12 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8093495e-069a-3c77-9cb4-a55bb3f99d83 | -4.60614 | -46.498 | 2024-12-12 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d69a93e-8b58-3d3c-845b-769286ee6137 | -4.55335 | -43.57195 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63345599-1a26-3d21-aa0e-e35d6a1ac0d4 | -3.85529 | -40.44897 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cb1821bd-edd1-3f88-96eb-03bf2bbe5c7a | -5.35233 | -44.20011 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8399f857-0b73-36f1-aef7-5b7117265791 | -5.39023 | -40.66242 | 2024-12-12 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 35a52826-6610-3c69-ab35-b68999412b23 | -6.12676 | -42.53408 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 75b81e4a-5f12-3142-96a9-cfbfb07070f8 | -2.56932 | -51.88445 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98c256b1-eb7a-3cc8-a049-ba88cbab1fe2 | -4.08071 | -46.72639 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ac5b4f-9e35-3d4e-ab6d-c6719a4c91e1 | -6.07503 | -42.34 | 2024-12-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f007718-59b7-30bc-bd5e-052517cc1bb4 | -6.58542 | -38.45237 | 2024-12-12 04:14:00 | NOAA-21 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ec6e36f-987a-3f42-a6fe-1486e24c3a0c | -5.26121 | -44.04473 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03767d5b-39e0-3afc-965c-37a9263895bb | -4.86498 | -40.75378 | 2024-12-12 04:14:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87cc0109-efba-3977-a737-0b27a54f3ff5 | -4.06736 | -47.09677 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7891ab59-eb91-37ee-a47b-961643f6e7e7 | -5.84882 | -39.04626 | 2024-12-12 04:14:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8cf3b7b3-1d21-376f-a9b7-1704873defc8 | -4.08986 | -46.61411 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc2f78f4-3c0b-3735-839d-daed9262efe1 | -3.83092 | -41.57233 | 2024-12-12 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 56a7569c-0730-3fb8-912f-975715adecb9 | -6.71425 | -39.18869 | 2024-12-12 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cfd59868-3fcc-3046-bb4d-9bfb39337e8a | -4.06966 | -48.95107 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a13ac97-9908-3220-935d-5bb3f34ca059 | -4.9385 | -44.27976 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5fefd5-e23e-3812-814c-c14769c575e0 | -4.38486 | -42.14572 | 2024-12-12 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e87ad6b-145f-307b-a3a3-ff64e50fff47 | -2.5233 | -51.7917 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c94278c4-adf4-3573-80e8-7377466adcc9 | -4.18693 | -49.28302 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84302354-7644-3188-a072-2f47bbd5a668 | -5.88158 | -35.41569 | 2024-12-12 04:14:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a5813613-22a5-3389-a392-5778fffe69aa | -2.30967 | -46.9937 | 2024-12-12 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6292f464-2301-3180-afce-904bda64d99e | -5.38237 | -46.29001 | 2024-12-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e38df689-c7ea-31c4-a829-9e78069b08d0 | -4.1628 | -45.5288 | 2024-12-12 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02fa9d62-33e0-3d35-b17d-304b94a230e6 | -5.70835 | -43.25843 | 2024-12-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b88aa47d-c9e4-32cd-b4ac-eaba71b602c6 | -5.1598 | -44.36593 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 876257f5-4dcd-34e3-8039-1cf530b42283 | -5.79484 | -40.42852 | 2024-12-12 04:14:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09e9438d-d2ce-32e9-b908-5648abc0ef43 | -4.18858 | -42.42318 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54cf0c5a-fb13-3e6b-b824-51a4055f91f3 | -6.11256 | -41.87799 | 2024-12-12 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3522105e-4c3a-348d-b608-396158f1f87d | -4.35662 | -49.74989 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7c82c17-e23a-3fb8-b20a-4f19ffa35cee | -2.56989 | -51.88092 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bd4868d-4709-34dc-9ec5-2c1153dfa0e8 | -4.09634 | -46.6778 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README14.md)
