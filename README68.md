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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ae146c2-433b-3352-8cbe-aa5384ed4240 | -14.1447 | -51.7062 | 2025-09-05 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| da44e2d2-140f-3363-96b0-7fa9b9e07c06 | -5.608 | -42.8798 | 2025-09-05 14:10:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 808ddc82-e73a-311f-8818-d1b509fb4615 | -15.8584 | -52.3031 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 579b72f3-770f-3836-bd0e-641faf7c0f87 | -6.1493 | -43.165 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 73.4 |
| daff8e42-82e5-3124-a7a3-c9e7fd9cc550 | -8.479 | -45.0704 | 2025-09-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| e7b321a9-a06a-35a3-96fc-aa10a0f4280a | -15.0644 | -50.0651 | 2025-09-05 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0714385d-311c-364a-b573-3ab8a32420b5 | -14.0499 | -53.9914 | 2025-09-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| b5eb476f-b30c-3fa0-9e2e-5627eb32dcc8 | -9.0719 | -50.4394 | 2025-09-05 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a82ede7f-8f12-3c21-b8c5-702b7c1ed44c | -16.4624 | -45.2402 | 2025-09-05 14:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 159.3 |
| e01f2e02-7a3b-3adc-b8f7-0c4ea2ba7bca | -9.7225 | -51.0362 | 2025-09-05 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 3f4d4704-3b26-3d60-918a-f1300f102f0c | -8.5187 | -51.3293 | 2025-09-05 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| c7cee630-32fb-3e2f-b5d9-7a03ed60eeca | -5.1585 | -45.1698 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a16bed6f-36c2-3b56-b02b-6950dc18c18d | -11.864 | -50.7075 | 2025-09-05 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 6a5e80d8-0b70-3253-9969-a9a3b1ae18e1 | -9.7105 | -48.9853 | 2025-09-05 14:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8d92320f-73e8-3fa2-8ed2-a4f68cd0349b | -10.7688 | -45.2769 | 2025-09-05 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a363d25f-d7bb-31e5-8464-4fcc2c761560 | -5.9844 | -44.7489 | 2025-09-05 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 0fd70145-12c5-36db-a59f-2f634b00dbf0 | -15.0445 | -50.0899 | 2025-09-05 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 2f99a805-d5d8-30ee-82b0-bf1953655629 | -11.9796 | -50.6086 | 2025-09-05 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c1aeaaf5-05e9-360c-ba24-67029726164c | -8.885 | -47.2304 | 2025-09-05 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 4919adfe-c85b-3ecc-ade9-0a0087628694 | -6.2421 | -43.2743 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d130335f-a40b-3aad-ad4b-32bacb088aac | -6.1679 | -43.1869 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 98639338-58f1-353d-a012-740e4b93e15a | -9.7031 | -51.0802 | 2025-09-05 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| ca6ec895-6e92-3f1c-ba52-0d42d634411e | -11.171 | -50.0366 | 2025-09-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| d48bae4c-5523-35d1-ac28-0bcf7b533723 | -8.3364 | -47.4824 | 2025-09-05 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f0e79606-b43b-3c5f-9879-07daf8ee5a53 | -5.55 | -43.0719 | 2025-09-05 14:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2a932fc9-a82b-3913-b5d7-c335c0e79063 | -15.7111 | -46.2281 | 2025-09-05 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8b43c80f-a3f0-3896-864f-f49c6cbc9c30 | -14.7465 | -47.4955 | 2025-09-05 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| f29c8e5c-60df-3c7e-9be0-51e47bdc8841 | -6.2606 | -43.2961 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 711f4060-5475-3f12-8a79-ea2e92f3543f | -9.6916 | -48.9872 | 2025-09-05 14:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 00427032-bcf6-3602-b96b-285d5247586f | -10.9864 | -45.9552 | 2025-09-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 92c06944-7fb7-3a54-b637-4e577db2f697 | -7.8923 | -45.2893 | 2025-09-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 738e14dc-01e3-38e8-9445-efa1ece31ed8 | -14.0496 | -54.0122 | 2025-09-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 9e7daa2b-1ac2-339f-8e60-c205fdd5a931 | -15.2156 | -52.372 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f4415b92-0e03-3f5f-b542-b562c09b980b | -5.7923 | -45.3078 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 91b806e0-7ffd-3990-a0ad-abfb0b69dc38 | -15.235 | -52.3693 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 96f3d72a-6b6f-3ead-9be4-43c30292caed | -6.6957 | -44.8062 | 2025-09-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 01736560-c7ad-3c81-a69c-149181b80ca8 | -5.9846 | -44.7261 | 2025-09-05 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 8a24dc54-8f0d-3808-b21e-37732d79ab94 | -10.9867 | -45.9325 | 2025-09-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4efc8912-3b62-3bb9-9481-a7f4de4eae16 | -9.0762 | -47.0113 | 2025-09-05 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f8e2490c-408e-3166-bd5b-31bafd5495bc | -12.1234 | -43.35 | 2025-09-05 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 9d10810e-59f7-3937-98a6-b842d7e81dac | -15.0639 | -50.087 | 2025-09-05 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 45c211d2-26c7-3ac6-910d-a0c465c38dc3 | -8.9037 | -45.7747 | 2025-09-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7c660b31-0168-3665-bfd3-6a0159b26f69 | -13.3192 | -51.6626 | 2025-09-05 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 21ffad51-2cfb-3296-8bf1-5f909dc851b1 | -9.7762 | -46.9132 | 2025-09-05 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c17f6c93-e5a9-313c-8a70-f6fef74af17f | -15.8588 | -52.2817 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d9eab1e1-1e80-3b03-8537-4c7c64d80fa7 | -11.0055 | -45.9527 | 2025-09-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c66f6f52-73e0-3444-ba35-3eb369caa787 | -6.1491 | -43.1885 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 61.7 |
| a1b0ebfb-8b0f-3cc8-a34b-e4c6dfc40dda | -9.7222 | -51.0573 | 2025-09-05 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 11b5ce8a-7071-30ab-a328-bd70d1af0fd6 | -5.5884 | -45.1185 | 2025-09-05 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 64641e73-1342-3d5d-aeea-eee33794b55c | -6.2296 | -42.641 | 2025-09-05 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 86ccf47f-9b2a-3ba5-8a3f-a525ab417fcb | -10.9673 | -45.9578 | 2025-09-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b8ed7363-b2fa-39f9-9d3e-e80086bf724a | -14.0691 | -53.9892 | 2025-09-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9c08c5c9-dbad-35c9-a992-d974fd75da14 | -6.2609 | -43.2727 | 2025-09-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b900b6dc-a5f1-345c-bd5d-a73cb2d253b7 | -10.7682 | -47.7523 | 2025-09-05 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1d13054e-59f3-3f3a-9f64-48f6274887f5 | -10.1491 | -46.0162 | 2025-09-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 75094f9b-51bb-3f65-88c4-3ec693a6ad50 | -10.2373 | -50.5417 | 2025-09-05 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e3fb8b58-c811-31d8-b654-45fa50701246 | -6.2606 | -43.2961 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 706f067c-568b-3c3e-b311-5d7c08b27eb9 | -10.3147 | -46.3571 | 2025-09-05 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9e164ce2-f05c-3bf6-85d6-e162aa69b0c3 | -6.2421 | -43.2743 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ac7a83e9-192b-3a9f-8218-ef72919b8203 | -22.297 | -47.6343 | 2025-09-05 14:20:00 | GOES-19 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 993cd28b-b4a3-30a6-b38b-c805037cfbd5 | -6.1679 | -43.1869 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 72.7 |
| c3ecc2d5-6a53-3f8d-8427-639b309d1b64 | -9.7762 | -46.9132 | 2025-09-05 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3b064ce5-82a9-3429-8152-b5d3b168e1a3 | -9.7105 | -48.9853 | 2025-09-05 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9c0a34f4-c748-3ee0-96c0-c3608f5ae6ed | -11.5961 | -52.176 | 2025-09-05 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| fffd9e08-3718-3baf-b4b5-a132dfa2d311 | -15.6141 | -52.891 | 2025-09-05 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c2365929-7871-31b1-8b41-d3c2c341dc48 | -6.023 | -46.7005 | 2025-09-05 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5396a779-5832-3086-ba78-e97eafd73a06 | -6.0043 | -46.7018 | 2025-09-05 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 30cbc222-d4fa-3e3c-be4f-d1ca460f8445 | -8.0226 | -45.4127 | 2025-09-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ed2fbf75-6e12-3a13-bbf0-9a57db0add4e | -5.7923 | -45.3078 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 048ca31e-fa68-3609-b655-26b10fa2ea2f | -6.6769 | -44.8078 | 2025-09-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 18c0d1f5-d884-3051-8daa-d8df53589743 | -8.3364 | -47.4824 | 2025-09-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 9967fc19-1a01-3caf-bf6a-93c0289b0d9f | -8.3646 | -48.2899 | 2025-09-05 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9e5c22cb-6fe7-3f31-856f-a4929b80ac07 | -15.0644 | -50.0651 | 2025-09-05 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d19c2e76-6a2f-34fa-9894-d7489202d978 | -6.2418 | -43.2976 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 18c77b01-95d3-33ea-9305-6471a5cc0241 | -15.7182 | -53.5954 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 3ac829b5-900a-3f5f-817c-7f01322233be | -15.8584 | -52.3031 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6dd3eb5f-6df4-305c-b5c4-7de0892e2e46 | -6.0045 | -46.6797 | 2025-09-05 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4229ead1-9914-332f-8f1e-9cef57c9ac54 | -5.7925 | -45.2852 | 2025-09-05 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c2b15c33-5c53-31de-b1cb-9e2f80f6ed4a | -9.6412 | -47.1063 | 2025-09-05 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9bccbabf-0947-3889-a187-bc57a9e86b22 | -8.3456 | -48.3133 | 2025-09-05 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c6a0d01e-4de2-3f96-9bf8-863cdd6fe28b | -10.9864 | -45.9552 | 2025-09-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6a47f7ca-2cd1-35f6-a5db-11f38548ec50 | -5.55 | -43.0719 | 2025-09-05 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 662aa358-b114-3622-9e7e-48d351da39d1 | -12.1234 | -43.35 | 2025-09-05 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 7be827d9-6420-3d21-aade-ede796443537 | -8.3367 | -47.4604 | 2025-09-05 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7c249a60-a29c-3fd1-810f-a3db873fe1a6 | -11.0058 | -45.93 | 2025-09-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 02a0f753-8e2c-397b-b044-15a029b3869d | -10.2373 | -50.5417 | 2025-09-05 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 37e8a9e2-bab5-3875-be57-f0223999a947 | -6.1493 | -43.165 | 2025-09-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 9d19dbe0-20e9-3246-9454-1e8400c63a1e | -11.0055 | -45.9527 | 2025-09-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 69442119-23eb-3e6c-b733-68b028a39075 | -5.608 | -42.8798 | 2025-09-05 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 148efca8-24a9-3b18-a71f-a5b79d8b06a0 | -8.0414 | -45.4109 | 2025-09-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 5cbd7236-e386-3b9f-bbf4-cb417f9420de | -5.9846 | -44.7261 | 2025-09-05 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 4169a61b-303f-37d2-b30f-90e2bdc44ecb | -6.9568 | -44.9434 | 2025-09-05 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cbd8a58b-3a90-32ee-bbb1-70c1aa9f89ff | -13.884 | -47.9929 | 2025-09-05 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 934f1d90-09aa-3363-bcb0-57df0c749f5a | -8.9037 | -45.7747 | 2025-09-05 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6d70ea56-5084-3f13-acc9-3ff281dd88c7 | -8.885 | -47.2304 | 2025-09-05 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e7f043de-d6be-3c81-a593-8328da8b1093 | -8.5187 | -51.3293 | 2025-09-05 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 434.6 |
| 6f8d4241-3c81-391e-aeb1-13b7db6d9a05 | -15.7179 | -53.6165 | 2025-09-05 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| cd0c241b-63ae-3a74-b9fa-379d481f1bd4 | -8.3458 | -48.2916 | 2025-09-05 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 2343412b-93ca-3819-9e56-8ec94ed6fa3e | -13.8845 | -47.9705 | 2025-09-05 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 5ad0f07f-5efe-3a64-8f3e-11392a04878b | -9.0762 | -47.0113 | 2025-09-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |


[Clique aqui para ver as próximas entradas](README69.md)
