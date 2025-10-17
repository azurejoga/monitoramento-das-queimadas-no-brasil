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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0b3ab87-9e53-3224-8c19-fff2480feb75 | -7.64596 | -47.65192 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da6e5843-a847-37b1-a2ca-5b34c96aeefb | -5.83365 | -42.2443 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e532bff-6dca-383a-8cef-15eb81c90a98 | -6.87473 | -44.70961 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed95a487-7f59-3013-9fca-a83e415ce6f7 | -4.83372 | -48.07968 | 2025-10-17 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31ee5d01-7d79-319a-ac9e-b77c607e760e | -5.85102 | -43.87903 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa19d499-24ba-3e2d-b89c-342482258e00 | -5.54856 | -41.31694 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9aab077d-9010-3e3c-a1f3-61d4dd3feef5 | -3.49476 | -51.60188 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6877df99-afdb-30f0-b107-f5c8c20c176d | -5.28613 | -47.92653 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9b2767b-04fa-33b0-93a0-d8927e0b53e3 | -7.1725 | -42.51176 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da75bbe8-78e9-3aa5-85bf-223e6ac33d44 | -4.71773 | -49.62524 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5f281d-6966-390c-bcc4-7f1a67724c4a | -7.95032 | -44.11101 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb7170f9-2285-35e8-b7df-dfd742bb6cd1 | -4.96813 | -44.95803 | 2025-10-17 04:49:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 720ebc59-4f84-3515-89c1-6d68579d65f3 | -4.10811 | -48.01888 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 499b04bb-b616-348e-a014-6cac5acf911f | -3.62883 | -42.77199 | 2025-10-17 04:49:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33e2eb6b-1ee2-3eca-a9bb-bf8535fcca94 | -4.27972 | -48.58823 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd6fee0-19a0-3be3-8c6b-e1385fbaccf1 | -4.11163 | -48.01943 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d62b01-db1c-3493-b463-30dbd4f2b8fa | -3.98365 | -42.4892 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e1b1a37-e5d2-3bd0-b2f7-966cfe0466c0 | -4.43956 | -50.55016 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c91562f4-edf4-3920-a9e1-bb2b33dc46d9 | -6.28861 | -45.50619 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d3a1b8e-583f-3a31-89b4-2a81ae196e90 | -2.86908 | -50.7249 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 025e3bb7-b75c-306e-98c0-be44927f6744 | -4.24925 | -48.55664 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccaf9a3f-f356-30a0-895c-15f46bfd3742 | -6.38831 | -41.47402 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1b63250-8756-35bd-b8e4-6e73efbf0322 | -1.60536 | -55.72694 | 2025-10-17 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bff67376-4565-31df-9d65-76a751c88adc | -7.3427 | -43.86222 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85481bc3-3eaa-32ad-956c-3ba46b6808c2 | -5.52034 | -43.30363 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00f5f4da-37d6-3506-b882-905129e6b2c6 | -6.58104 | -47.07378 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 211e19d8-9cf5-32bd-86f4-a410e86ff3ed | -2.87076 | -50.73581 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a93077bd-8249-3e8c-a784-c03f22b64cbe | -5.87712 | -44.84055 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e7c2174-90fe-3392-8972-c296342ae138 | -7.2055 | -45.49646 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11866a8d-45dd-3793-be43-458f03098765 | -6.31508 | -45.52969 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3af0e9-8238-399a-a408-87f394a8bb51 | -3.5112 | -52.48609 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2c9b04b2-7b7a-31c4-9191-d22baeb766d7 | -4.54113 | -48.41055 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec59c4b1-eaf0-3c0a-824a-453038034a6a | -4.88686 | -49.94765 | 2025-10-17 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53b7a308-5f7a-31ce-ab20-93f43bc90821 | -6.13144 | -41.7515 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5742f62-bf4e-36c1-9877-7add64a9d276 | -3.84337 | -49.93153 | 2025-10-17 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a78b3fa-86b0-3741-b45b-953e96e8585f | -5.6951 | -43.5421 | 2025-10-17 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8df88e20-7319-30e2-aa47-4a4bc5062f6e | -6.067 | -49.38963 | 2025-10-17 04:49:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b968bd-add1-39b4-aa5d-a0a1bd49d050 | -2.92573 | -48.30165 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa148a74-7694-3c5f-bd56-be22a59f0227 | -3.47329 | -50.02649 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d76efa4-939e-36a1-82f0-9e18afdc59a5 | -7.18502 | -42.1903 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 079c669b-80a4-363e-9b90-6e2da0f11f2f | -7.05805 | -45.05692 | 2025-10-17 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 197fbdff-b42a-3c8d-8565-3b70c70ae0b2 | -8.25348 | -44.02868 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfc14a5a-4e74-3aca-b5c0-3d02151dfdf7 | -5.44478 | -44.17594 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f300b3-e4e6-3e7c-9051-a5620b6296d0 | -5.28676 | -47.92246 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75140206-030a-3c00-a00d-ed80b8036866 | -5.46272 | -44.64523 | 2025-10-17 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e27928a-2f10-3229-9101-84a62f14fafa | -8.4517 | -41.26678 | 2025-10-17 04:49:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16e7892d-7d1c-347f-acf7-d0ce78edf2fb | -2.88463 | -50.73444 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bf05c79-f8c4-3345-a112-f1fccbd44f4b | -2.7327 | -48.31113 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8426433-8873-3ec5-8cef-7330ab0c054e | -7.16994 | -42.18126 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4998bca-45de-33cc-acb0-b5a4ef4d3c49 | -2.88075 | -50.73738 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b87482af-559c-3db5-a373-79463986ac5b | -6.74987 | -42.36734 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e79c669-ed6b-3615-998e-20048774916b | -7.33929 | -44.15879 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47f32c71-dfe8-3117-be72-7aa33f02b603 | -3.07543 | -49.50441 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f19e3249-5ec7-3de0-911a-ff47c7d827d9 | -4.0481 | -47.50154 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e97b4de6-91cb-30e8-b646-4c1f67c65409 | -8.30422 | -43.42304 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c44ca4b5-f936-390f-84f6-4b2410b2bea0 | -7.03586 | -42.73167 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bd7398f-5d7e-34a0-8a5d-9e9480013eff | -5.85171 | -43.87427 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96da4e2-4b4d-35d4-8820-c59aa65dccd3 | -5.84707 | -43.87343 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50fed8c1-711d-3668-a080-92c8d628ac3c | -7.2065 | -45.3796 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1999f000-ad20-38e7-9458-e845683f8a69 | -8.21868 | -43.31061 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7df340ff-3812-3989-9c20-596ceacb800b | -4.63926 | -50.93302 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13028dea-902f-3d06-92c3-9046838b88ae | -5.8729 | -44.83757 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 551142d9-7f8c-3128-9dbf-f7ec64aa225f | -6.29833 | -45.52722 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a29f634-e450-39e1-8aa0-c602fc11a44f | -7.35968 | -41.90516 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92469ead-5a85-3a87-bc1f-371230ef2d16 | -3.23717 | -45.9768 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 616f2426-78dc-38d4-9490-87475799f83d | -4.612 | -50.82893 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2621a124-44b4-351a-9728-7d2afc0878a1 | -4.10693 | -48.02658 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffa010b1-c004-3ef3-af8c-9ba164779abe | -2.87907 | -50.72646 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b28bbe7f-cd02-3873-a7ea-fce258b89090 | -7.35292 | -43.85872 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 83bbebbb-7854-32de-b69b-83f55454b294 | -4.56064 | -46.62595 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d28dbd-a9e0-34a1-8581-b99dc8d1c09c | -7.18057 | -42.37617 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3db65ba3-bc56-3466-bafa-6c3ad984ae20 | -5.75258 | -50.00249 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06f4805c-b769-33ea-93be-18fda765d16d | -3.23389 | -45.96931 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 53386320-da4a-3332-895c-543f66495497 | -7.17663 | -42.36602 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c244a514-cf5c-3a1c-ac03-19a13ff1423f | -7.94944 | -44.15208 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bd2bc7b-2ba6-3a35-a2be-279f60952f8d | -5.28981 | -43.54817 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9aa54506-ff47-3d22-b667-bc6c3e7fd6eb | -8.16054 | -44.00158 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5e0bd01-bf90-39b0-adc2-625ccec36fd4 | -6.3591 | -41.48907 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e20cc2bb-8d5d-3cc6-a8fb-c70a43d51fc8 | -6.31402 | -42.64727 | 2025-10-17 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44c5826b-25b6-3fa2-bf25-831244b14e36 | -5.84103 | -43.88238 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 602bc1b6-4fd3-37f7-aa26-b0ea98a7c4de | -4.3941 | -43.41587 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a81a5ed-bd25-3eeb-899d-394beac51f7b | -7.34199 | -43.86726 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4a4e089-b45b-3650-81c0-748f2a7676c0 | -3.77202 | -49.13701 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9e161e4-4ead-3fdc-8719-0b6e17f5916a | -6.96025 | -47.72062 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe10e08-538a-347b-82c1-321a49ea3c59 | -3.27005 | -53.25898 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 530170fa-3cb5-3b20-aaf7-b9fb23c5b2b6 | -2.92043 | -51.93995 | 2025-10-17 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b913115c-0d44-3388-9386-843e16edc62e | -3.84004 | -49.93102 | 2025-10-17 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 275cdc00-b256-3108-b6cc-f1f79886dd82 | -6.93424 | -45.13963 | 2025-10-17 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c51ad46-685f-34b9-a8ca-89212d599432 | -6.58555 | -47.0697 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9a65a0a2-dade-33f8-aa36-fd110614ea42 | -3.41783 | -48.88009 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fd35b6f-bb27-3b6e-93c9-598e80881f01 | -6.29308 | -45.53374 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a1a698ee-1434-370c-9818-cf7db8819802 | -5.4084 | -47.78861 | 2025-10-17 04:49:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05e5b825-48e4-3358-a2f4-b805f8f44ffc | -7.22006 | -47.869 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22b2e777-2fdf-386e-89b0-f19a61d23992 | -4.9505 | -44.95928 | 2025-10-17 04:49:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 125d8134-caf9-3b13-9ead-465f95e5e576 | -6.34951 | -41.51669 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e3fb0a5-c5b8-38a2-95e5-796f433eb864 | -5.58125 | -47.46298 | 2025-10-17 04:49:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fc55612-76dd-3364-b45d-89b7718db62f | -8.30761 | -43.43519 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6edc34de-d973-3f97-bb87-f12444d56fc4 | -4.41925 | -40.18205 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 910b7e03-b791-3baf-95d4-2059f174f0e4 | -6.76778 | -42.84793 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8474ce6b-e649-34fa-9094-2dc9e11c55ee | -1.23772 | -49.01843 | 2025-10-17 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README77.md)
