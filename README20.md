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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e50c5ac-9d94-3550-b3e2-8470da781673 | -5.18734 | -44.95388 | 2025-07-30 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f7a0eaa-d37d-3407-ae8d-04c1e849e720 | -8.07125 | -42.9514 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e327f3b2-9ed4-389b-bfa0-15440189ac13 | -7.22716 | -43.10458 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c183abe5-0977-39ed-b47d-455c297c8deb | -3.11103 | -47.01239 | 2025-07-30 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19f438c7-c338-3fd4-b898-3f99b0d51501 | -10.60958 | -45.2458 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 293bb6e9-b2af-31a0-8243-9df6ee532611 | -9.23666 | -50.04559 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac4d9f8-7cdf-343d-89e5-2ed12064eb15 | -8.33695 | -54.75285 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01eb5a3c-834e-345d-bb55-62fe1eb606be | -8.31413 | -55.1102 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3600cb8-09f7-32f3-bbc4-ec41d2e52b6a | -6.39832 | -44.74659 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14c5a50a-c9f8-3f2d-a7ff-c2b943c68ab6 | -4.3768 | -49.0331 | 2025-07-30 04:27:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c6b376d-d558-3e65-834e-07506a6025df | -6.53001 | -43.33533 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb2fe79c-71c0-3cf5-a38b-3076736d4338 | -7.34737 | -43.76632 | 2025-07-30 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1007d369-3b38-32db-953f-59e663d91879 | -5.40229 | -43.2496 | 2025-07-30 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51f1c287-42dc-342d-a7fa-dc35961dc8b4 | -6.39988 | -44.74276 | 2025-07-30 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6441180-4556-3774-995e-e17c309cd18b | -2.90427 | -52.54826 | 2025-07-30 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 208f1377-a964-3540-9678-4828dca00305 | -9.87294 | -44.69147 | 2025-07-30 04:27:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 460478a4-06ad-3299-9ea3-71dc4f045f0a | -3.88983 | -41.03598 | 2025-07-30 04:27:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5b89875-57e1-3248-ae2d-0aeb31481439 | -7.35505 | -43.76344 | 2025-07-30 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 228a1801-3170-35b1-b258-d755ad6c0a1b | -3.99625 | -43.22713 | 2025-07-30 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2267ab2-59fa-3b14-bcf1-f5f5d98a7f13 | -10.62445 | -45.24045 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c42df315-3eff-3c8c-b4f2-54141eca679b | -6.91763 | -44.73203 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb1e80ee-e08e-3da2-8866-8b68828e59c3 | -7.05702 | -44.96059 | 2025-07-30 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9eaacb9-9b15-379a-8015-10c928053097 | -8.30879 | -47.32889 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8adfcd8a-d117-3713-b421-21b81f4c8109 | -7.65949 | -46.51706 | 2025-07-30 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c189728e-b57b-352a-bc02-72cbae54f144 | -6.56168 | -44.21371 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 398c3330-4d91-385c-b816-17d589877c3d | -9.22589 | -48.59732 | 2025-07-30 04:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f7b07b7-3292-3e07-9ef8-e8266d48b7a2 | -5.40472 | -49.11676 | 2025-07-30 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 653a079b-63e2-3bee-b728-405cca82eade | -7.38051 | -48.16946 | 2025-07-30 04:27:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59609312-ccbd-39aa-9379-5518ef622c14 | -6.62145 | -59.99189 | 2025-07-30 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 553bd819-d315-3600-b772-edfa2045a052 | -10.61645 | -45.24687 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62c0adfe-4313-35ba-a49b-69bf6261190c | -9.04919 | -45.07271 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3c5888f-7c3c-3e7a-ae58-075a240499b1 | -6.55846 | -56.1906 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d650a4e-7703-3110-9056-ed5380255da7 | -7.15341 | -44.04359 | 2025-07-30 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9df2f2e6-5f19-371a-90ee-6abced59ae23 | -3.51071 | -47.22352 | 2025-07-30 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a7b6b2c-8b5e-3538-9118-33a3ae757035 | -7.72379 | -51.10194 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 139ea403-efa9-3910-bbe5-83a5062f4b4c | -5.82163 | -46.34986 | 2025-07-30 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 701425cf-97ad-3792-80f9-2e3327912670 | -6.55016 | -56.19041 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f1c1194-5266-31cc-87ba-3a53836d3625 | -6.49288 | -56.21891 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34e022f4-d746-3e73-b87e-ff15d98e424d | -8.51746 | -43.31117 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 351564a5-c9ef-3833-91c5-91768e077965 | -9.62977 | -48.54568 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 339dbecc-57ef-3073-be7e-2072cc3e519f | -8.63489 | -45.88347 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72f2b0f7-c751-398a-b500-3bcf32bf57c2 | -6.50188 | -56.20096 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99d4480e-b1b8-3a19-a095-b6931517a8dc | -9.39949 | -45.49326 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a63fe408-28c4-3478-afc8-8e93e8fea34e | -5.82108 | -46.35332 | 2025-07-30 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc8a5ee-29ab-3d9a-a8d1-e902fb9a5fa6 | -2.9834 | -48.60398 | 2025-07-30 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1db70c0-a9b3-3257-8950-8015957515b9 | -4.58316 | -48.01524 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3a4c49d-121d-3aaf-93cc-0c1df4b2cd80 | -6.50907 | -43.19862 | 2025-07-30 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 466693f9-78cd-3552-a62c-6c2db01d6652 | -8.94738 | -46.74018 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 694df2ca-b407-35cb-b03f-db2bcb313d4f | -6.03693 | -47.54945 | 2025-07-30 04:27:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ac94234-0d6e-300a-a1c2-87cb3603c9db | -6.25414 | -46.11672 | 2025-07-30 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c49a1381-f5c2-3258-8c3a-65515d29e6b7 | -8.331 | -44.63761 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67db3e9e-2151-3550-94b7-03aaacdf6164 | -3.88666 | -41.03035 | 2025-07-30 04:27:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c2d9a52-2ae0-3299-a757-d53f1145b20b | -6.55643 | -56.18772 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7016b3a5-abf8-3e19-8182-df567b597cb1 | -7.76889 | -45.86329 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede66525-c48d-3839-ae4d-8f8ecc899ece | -8.41611 | -45.68607 | 2025-07-30 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba8ed199-a9d3-3213-9eb9-f53596554cef | -2.91273 | -48.24641 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 516d9fb7-3b86-3599-85f6-e7e5300fa790 | -4.65121 | -43.11719 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c439f4a4-daed-3b63-9330-1566ed9f5435 | -9.57558 | -43.88116 | 2025-07-30 04:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23e0b2e3-0f4c-354c-98f2-da3e0f867899 | -9.62577 | -48.54878 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35326726-636d-366d-85ae-12169572e0d3 | -3.08137 | -52.92582 | 2025-07-30 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 026bf2cc-7666-3401-80eb-4c8c23e1cb99 | -8.6282 | -45.88244 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3d21276b-8735-3aa9-a358-2e941d0b25da | -7.28487 | -44.5458 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f94dab8-55af-31ad-81b6-36f76414349f | -6.2536 | -46.12019 | 2025-07-30 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c90516b-a7b4-380b-93c0-1efc532cf001 | -3.11442 | -47.01292 | 2025-07-30 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e66bc9a4-bea2-3262-aed8-317e9a67d656 | -6.52504 | -56.20131 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23bab374-fb39-3fc4-9f04-d30da41920dd | -9.04977 | -45.069 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 142e49f7-bc7c-3377-b049-3e7514154e9a | -8.95734 | -46.74177 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 989afe69-20d9-3cbe-a5c3-03e15cdf37a1 | -3.33015 | -48.71963 | 2025-07-30 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a4220d7-f0f6-32bc-9d4e-b9145ceff50b | -7.74496 | -51.09596 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84d67272-c2f8-309a-8b20-ef44eca26dd7 | -9.15676 | -49.85322 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbe30550-b3b8-3b41-84b8-5dc22c75c8e7 | -4.89285 | -44.95923 | 2025-07-30 04:27:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8765cf61-9b72-3786-8d8b-c0ba3a64a32d | -3.60223 | -51.48364 | 2025-07-30 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffb37e76-c1ca-3501-a04f-20175573802c | -8.62097 | -45.88495 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f251e901-78c4-3a2b-8e3f-4584a366eaa2 | -6.62073 | -44.04725 | 2025-07-30 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a93b455d-0240-36b0-8b6c-4628c4796560 | -7.72772 | -51.10256 | 2025-07-30 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb298704-e33f-3950-a5cb-8256d74a1b12 | -9.22785 | -50.04983 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16bf722-bd81-33e8-b0a0-4da9624726e5 | -6.7241 | -47.20874 | 2025-07-30 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b56b63a2-0ddd-3081-8dfc-de815a5429fd | -6.55577 | -56.19147 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81a64c9a-c506-3bf0-b0c2-6ae0ff36c48c | -9.16035 | -49.85383 | 2025-07-30 04:27:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6673628b-a190-31e4-b587-4a15e726683d | -7.78284 | -45.00472 | 2025-07-30 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f68ab72a-40dd-3d75-90c6-2992d2a3fc1a | -8.01913 | -47.67748 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9846d394-6e50-397e-9714-25256fdac024 | -9.74705 | -37.0018 | 2025-07-30 04:27:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 973e8865-08a9-3e46-ab7d-a0e819f22abc | -5.83547 | -44.03576 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95b9f0b1-370a-3a1a-adb7-9fd601befcf6 | -3.49362 | -49.04844 | 2025-07-30 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 38896b99-a234-315b-a04d-dc84b8be94e2 | -9.55735 | -40.32708 | 2025-07-30 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| da189fbd-124f-36c7-ade3-5acbe5373ae9 | -10.62159 | -45.23616 | 2025-07-30 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83db14a3-515c-3eb0-8554-b5a205bda610 | -6.53201 | -56.19471 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba057aba-0446-35ae-b8b6-a43ee7bae167 | -9.60161 | -40.56299 | 2025-07-30 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fb0d5bcb-0ea0-3b58-9a6c-238ed5b51ba9 | -4.58146 | -48.01424 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0765d69e-4d2c-3497-a298-6970d544e80b | -8.95679 | -46.74525 | 2025-07-30 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b830663b-a4dc-324b-a9ae-7f49baa86395 | -9.6358 | -43.84783 | 2025-07-30 04:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0a34d68c-1232-3b00-910d-eb014d774002 | -6.5237 | -56.20891 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 119d8b2d-eeea-3559-83e6-826e894a272e | -6.55512 | -56.19524 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55975dda-bc88-31b5-a5eb-f18f90b5fcd9 | -10.32686 | -39.21149 | 2025-07-30 04:27:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04d93ea4-0457-3082-b53e-0cc4b062f525 | -6.49851 | -56.21992 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2921c968-9a25-35ee-9004-9a737da19199 | -7.94649 | -44.09082 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb59a3d-f9ba-3ad0-a77b-076d065eb5f2 | -8.6271 | -45.88955 | 2025-07-30 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 823b6dc7-3a4f-39c8-9f0f-815aafb32618 | -10.61091 | -42.92803 | 2025-07-30 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9cf7a28-58ac-389d-969c-ebaa5dcf3d12 | -9.74063 | -48.57483 | 2025-07-30 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c8db955-83f9-3378-bd6d-f17b39d03895 | -3.51073 | -43.2461 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README21.md)
