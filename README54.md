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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3bb0bf-4f1d-30c0-ba9b-065d101f504f | -16.6598 | -55.5219 | 2024-10-05 04:06:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| b83ffba8-de98-3913-ac15-dd3b47f10b21 | -16.7644 | -57.5061 | 2024-10-05 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| bdd7c1e9-fdf9-3df9-b842-f69a43b46e51 | -16.7647 | -57.4856 | 2024-10-05 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |
| 7e249de2-9efe-38ea-8863-a0f0d2fe6637 | -16.7843 | -57.4834 | 2024-10-05 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 558d1342-59f0-3eae-b8f9-f8e8371a470f | -17.1178 | -57.4244 | 2024-10-05 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 6d8423e4-5b8d-3d7b-9d8b-2923067a1b1e | -17.1182 | -57.4039 | 2024-10-05 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 4d33925f-1bda-30cd-94e1-7ebf62404aad | -17.1378 | -57.4016 | 2024-10-05 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.1 |
| 125c78fd-880e-3da9-9440-cca55eb6e24a | -17.1375 | -57.4221 | 2024-10-05 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.9 |
| 476cd58a-07c1-3659-90d4-5e12c820b786 | -18.8809 | -43.6032 | 2024-10-05 04:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| dfdb5286-7d9f-3962-966e-23407837b056 | -18.8816 | -43.5785 | 2024-10-05 04:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 56006eed-b5c5-3524-b100-bef383ba512d | -18.6582 | -57.2967 | 2024-10-05 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 8c1a5acf-6cd5-32aa-ac1b-1a41c4045b02 | -18.6586 | -57.2759 | 2024-10-05 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 946fa7b5-6db1-3197-9d40-b662f4daef6f | -18.6782 | -57.2941 | 2024-10-05 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 2a69c2a6-e167-3e8d-b20f-cbaea4008196 | -18.6785 | -57.2734 | 2024-10-05 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 1fce8c4f-93a1-3d16-a9c1-dd1b60aa7815 | -18.6981 | -57.2915 | 2024-10-05 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 51f5b280-317e-32f2-b7ae-529e7a288683 | -6.69798 | -43.04984 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9887a99e-6a25-3b89-87da-aca4c98a87d2 | -6.66075 | -43.05471 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3b941e-9c1b-3817-95ca-1ef858c5770b | -6.6602 | -43.05819 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 181e333d-5e16-3da1-887e-a8e33529e931 | -6.64968 | -43.06009 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0428f7f2-ab5a-3fbe-a415-4fce5bd1f6aa | -6.64691 | -43.05609 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f818f30e-d6df-36ed-a434-23d3fb250113 | -6.54205 | -43.22448 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfbb35c3-3f6c-3ee2-96aa-40088e6ecf9c | -4.00028 | -43.25587 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38a9a327-8015-3e9e-a40d-57aa34a1d365 | -3.99972 | -43.25938 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6135c5c4-df9b-34ea-adc8-5c172cdc03ff | -3.99804 | -43.24834 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b98e40d-a8af-3813-ba7f-9275152b4a07 | -3.99694 | -43.25535 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c56a1e-5d65-3c36-b30f-d543c7fe7fcf | -5.97929 | -43.94238 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b877177-d726-3df7-a0df-64d60163539d | -5.93793 | -43.89954 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e80f9ecb-ec20-3f7e-8399-fdc3d40d1abb | -5.88274 | -43.71762 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c29121a-0b9c-3cd5-bae7-d83d027b4a37 | -5.85818 | -43.8292 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbba42d4-9b2b-3154-a850-9bb99323ddbb | -4.94212 | -43.77549 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c65ce925-f3b4-3ac7-b258-38015635cf9d | -4.94155 | -43.77904 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| acc5e54f-47ef-3b30-a24d-fe4506d0d0d2 | -4.93819 | -43.7785 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bed3e710-f9bb-3171-b8da-3433dde03f68 | -4.93483 | -43.77796 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 63725375-e2da-3fc6-b3cb-ff6e9d584629 | -4.93148 | -43.77741 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5965c17c-58ae-355b-a512-379153b3b470 | -4.92869 | -43.77332 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec396cd8-ecd3-35bb-9bec-ce82205f7488 | -4.01475 | -43.25097 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3686ee24-e03b-3faa-baf0-df401bf63f98 | -4.01141 | -43.25045 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c2bf0de-8337-327a-8d63-cbf126385f14 | -4.00473 | -43.2494 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 105bd5c5-1bb8-3429-b6ea-1ff2113a2ceb | -3.9986 | -43.24485 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ae1e5bd-65c0-3db6-ba14-1df1950b00fc | -3.99749 | -43.25185 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbf1e97e-2e06-3b50-b252-3abcaed71162 | -3.99638 | -43.25885 | 2024-10-05 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80964ed7-ba29-320a-9291-010f1f649f7a | -3.47331 | -43.35983 | 2024-10-05 04:12:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bf804c0-643c-3b7c-99b8-ca92a5e5c95b | -3.21831 | -42.70161 | 2024-10-05 04:12:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38681a0-1efa-3eea-bae2-3bfb971f8c0b | -3.21498 | -42.70108 | 2024-10-05 04:12:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| edc2389f-2196-357e-bd19-9ecc54e4ac89 | -6.32569 | -43.48267 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7889e87-ec9f-334d-9ff6-bef9ab4ff0af | -6.29015 | -43.4485 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e77364c-2699-3ba5-97b5-61bf7b055970 | -6.28682 | -43.2585 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5f6ba8c-d385-307f-afef-6a04731410b0 | -6.2054 | -43.27772 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 661e5a52-308c-3313-aec1-e99c7f25f488 | -6.07019 | -43.0861 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b9e8045-a898-3a9d-9cf7-04070da04239 | -5.88484 | -43.42382 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1983c04e-7574-3fb3-b3d2-efbf6a66cb3f | -5.8833 | -43.71409 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a87e48a7-fef3-3b57-91ac-28c369661490 | -5.85483 | -43.82867 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81faace4-3adf-3972-9ea0-365b9448ba0b | -5.71784 | -43.79202 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63e51249-e8b7-3429-a609-a451337fa91e | -5.66599 | -43.61105 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dbd74d9-969d-3d2a-9b53-14b7c75dc4cf | -5.49943 | -43.65307 | 2024-10-05 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cecce2fa-a4df-3881-9ba1-1e76ee3696cc | -5.3694 | -43.34597 | 2024-10-05 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30b22561-5b06-32c6-a0ce-8bcf172cbae7 | -5.36884 | -43.34946 | 2024-10-05 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa608109-8bed-34ff-b769-0541feea28cd | -5.11215 | -43.32302 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6ad5358-24d7-39c7-ad0c-75305cb86d50 | -5.1077 | -43.32947 | 2024-10-05 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaa6d31d-9221-3a8b-a2d4-245e76aad5d9 | -6.68406 | -43.99576 | 2024-10-05 04:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78dbc65b-47b5-3427-afcb-34601b40a9a6 | -6.68215 | -43.51745 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae276ba2-b4d5-3076-a735-5b284683000d | -6.6816 | -43.52094 | 2024-10-05 04:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c038cf12-d983-3376-8b06-d1b0ab7b9eca | -6.65688 | -43.05766 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd447ac8-c395-3cde-93af-d439eec9e308 | -6.65355 | -43.05714 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 327828a2-124d-3dfd-bcbb-31a6d88a64aa | -7.45688 | -35.23353 | 2024-10-05 04:12:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30504191-b6a5-3557-9942-a2f5720b7af4 | -7.37803 | -35.2166 | 2024-10-05 04:12:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b34f707d-5f96-3c83-83cd-9de81719223e | -7.37309 | -35.21574 | 2024-10-05 04:12:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fdc2582-b8d9-392d-9c44-ccf4baa1f1e3 | -6.65301 | -43.06061 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b453926a-7412-3b34-8a73-5891d49e4387 | -6.65023 | -43.05661 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 348651dc-3feb-308b-88a5-93e046fd7e12 | -6.64636 | -43.05957 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40cf31b4-7ed7-3b49-b56a-6ed451318b18 | -6.47424 | -43.42033 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90987113-141a-3b81-a86f-1c41ad2f2f4c | -6.4736 | -43.35958 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ad5b1a2-90b0-36ed-8eb5-422a97b3ae28 | -6.47091 | -43.41981 | 2024-10-05 04:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3285244-f95d-35c8-bba1-3a186a2e4c10 | -6.47028 | -43.35905 | 2024-10-05 04:12:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c3d0feb-a03d-3b5b-b610-fc698c867dc5 | -6.84482 | -42.8274 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48f0cc98-7cb5-3c69-b779-0e23035eef89 | -6.84428 | -42.83088 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bd566d0-c7dd-3382-b4dc-4a96e222c460 | -7.35097 | -41.94691 | 2024-10-05 04:12:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbef4790-c1b4-3e03-a4fa-df39aef22813 | -7.35041 | -41.9505 | 2024-10-05 04:12:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 574d1f90-0911-3dcc-ae66-5c6da95675fa | -7.34759 | -41.9464 | 2024-10-05 04:12:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07cd2b5a-6742-37bc-944d-be1a0d7463de | -7.34339 | -42.64833 | 2024-10-05 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0198addb-04b4-3ce5-a1af-8099f18d00ff | -7.2978 | -42.2669 | 2024-10-05 04:12:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5dda1bf2-a05d-3c8c-8309-00e2c7653ef6 | -7.2972 | -42.24868 | 2024-10-05 04:12:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d76e283-afea-317e-ac77-dc2693b46cad | -7.15534 | -39.31471 | 2024-10-05 04:12:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 084dc9dc-a868-3761-a7fd-8efb0746b172 | -7.12916 | -42.61161 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6641f817-e4e2-3bae-815d-4fe9b3f0b1c3 | -7.12862 | -42.6151 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9f12f9f-0c36-3ba1-9cf6-10eeda644b38 | -7.12638 | -42.60759 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 204ba605-742a-3c96-b789-14a3a8952e90 | -7.12474 | -42.61808 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4d79dec-527d-30fa-afb9-c7a3baa033fc | -7.1225 | -42.61055 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c83f1378-8641-3f0d-830f-61e767b2ab7a | -7.12195 | -42.61405 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60807fa0-b081-3e94-a972-94081dd3f86e | -7.12141 | -42.61755 | 2024-10-05 04:12:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76f68b04-dace-396e-a34a-ffa030b6b46f | -6.84329 | -41.68938 | 2024-10-05 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e352b9c8-04e0-3d24-b4bc-7e4a90d4da12 | -6.84259 | -42.81992 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b56b96c-6275-3503-8c79-ed886f65e12e | -6.84204 | -42.82341 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b45ee0b-5e66-3938-b664-9256d0bebf92 | -6.83926 | -42.8194 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30159ed9-862d-3cd0-ba93-14006b534081 | -6.83872 | -42.82288 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8478660c-6c16-3242-b778-f2590c25ff53 | -6.83261 | -42.81836 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c4bd3ed7-af43-3970-ac90-8892a0ab3e7b | -6.82929 | -42.81783 | 2024-10-05 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b362fbb-f58f-351e-93bc-207ed403a58f | -6.65053 | -41.98958 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8ecc0bf0-467c-3852-887f-49038c2cea2a | -6.64717 | -41.98906 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 620b75f9-9aa5-30c0-b459-4d5859fcb2b3 | -6.64326 | -41.9921 | 2024-10-05 04:12:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README55.md)
