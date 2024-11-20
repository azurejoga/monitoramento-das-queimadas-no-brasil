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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a7adc46-e394-3de3-b4c2-75f015bd087b | -5.487 | -41.8144 | 2024-11-20 00:09:00 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4782ac4-15a7-3fb6-8102-2d37215941f0 | -9.1602 | -44.723701 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be42015a-525a-3135-b207-5f7435376bc1 | -3.4609 | -50.289299 | 2024-11-20 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94e3c53-cb1c-3d6f-bc7c-c0f5f773acca | -2.2969 | -46.8531 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0835e206-ef0b-3ccf-bfd3-d3783366adca | -1.9822 | -46.598099 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9321fb-8313-3a9e-85be-89d3d5de2cb2 | -4.1572 | -45.505299 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49202836-eba5-3ed4-b8a4-8946bbbc7779 | -2.7065 | -49.3344 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e92dc0-45f1-346f-9275-c054e612196d | -1.3076 | -52.386501 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b4a68a-87c0-38a8-8951-9b09cd8a2b19 | -2.4358 | -46.278801 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7c2a7e-121e-3e74-a483-30103bcfa153 | -3.0369 | -45.744999 | 2024-11-20 00:09:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bab49744-3aba-32d2-94d9-ad8be2072f92 | -5.2433 | -43.827202 | 2024-11-20 00:09:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6031d6b0-52da-3e42-a452-6c3a08e780cd | -2.1731 | -46.990299 | 2024-11-20 00:09:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4318d4bc-2fef-3e21-8d24-25b0ff3f5ff8 | -3.2508 | -45.137699 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c06acf51-30b4-30c5-8ae8-84921e4ad1f3 | -10.9413 | -44.406399 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5ace8aa-52c3-3dd1-9373-1e7ba79d819d | -11.0288 | -44.571999 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43de565f-6302-35fa-ac55-eeda1d4b477f | -5.38 | -45.125401 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfa83c5-4d88-35d2-8739-03497fbecad8 | -3.2508 | -44.177502 | 2024-11-20 00:09:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 160c253c-98d1-34e4-aaf6-bf0563f07656 | -2.255 | -53.616299 | 2024-11-20 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bafdcb00-937d-3b43-8f89-f7f4654a8544 | -3.2331 | -48.4226 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54cffefe-6783-3d9a-8280-0489b2256655 | -4.2428 | -43.004101 | 2024-11-20 00:09:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d650292-f22b-30c5-a221-131580b9411e | -5.3816 | -45.132401 | 2024-11-20 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd8d130c-b502-3a18-85f1-a94e32a9b305 | -2.2897 | -46.4543 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f48b65aa-a839-35fe-a6b4-849393920153 | -4.1062 | -43.583801 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b334f86-d507-39dd-b877-0174dc563f2e | -1.437 | -47.105 | 2024-11-20 00:09:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5629613f-2624-3c59-8a94-0f29c22c0878 | -1.8263 | -46.270802 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d87e6e1-8022-36d5-8bbf-4508d44b48a4 | -2.5448 | -46.5355 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7828182-c07d-34b9-a11c-be5108dcac4d | -7.9835 | -44.3806 | 2024-11-20 00:09:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49e49983-f339-3154-89b5-84df65995be8 | -3.1666 | -45.221199 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a37d664-687c-3449-8240-884ceed6a40f | -1.6905 | -46.308201 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d86f5d-1005-306e-bcf5-c1a99a3139c1 | -4.4399 | -46.588501 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e172c191-2327-348a-994f-241a87863cc1 | -4.5234 | -43.2869 | 2024-11-20 00:09:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5558ad83-028c-38c9-a16a-8c18dddc7997 | -4.0964 | -43.585999 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| feefdd4d-4dc4-3315-b8ff-fea0270ba982 | -3.4635 | -50.301102 | 2024-11-20 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d47c14-6dfc-3a0c-88a2-efeede944750 | -10.3795 | -44.469501 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c3ebeb1-b95a-3a7d-b989-cd2baf74ac89 | -2.1174 | -45.366699 | 2024-11-20 00:09:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b67db8e-f8eb-3008-80a7-993b29c5485b | -1.6213 | -52.647099 | 2024-11-20 00:09:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46840696-4288-3e69-8214-45e787ea477d | -3.2566 | -44.476898 | 2024-11-20 00:09:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8871a5-3f75-3545-83b7-6995c6aaa2da | -7.1616 | -45.036301 | 2024-11-20 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 020708c8-ba71-3446-ae99-50848f7f5d72 | -2.4031 | -45.628899 | 2024-11-20 00:09:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8015c59-deba-3e03-9b39-d9f5d665bf40 | -3.1206 | -49.119202 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8517152d-56bd-34eb-a7ab-e85a5cfb8fd3 | -1.6778 | -46.022701 | 2024-11-20 00:09:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7144ee86-7c69-3e2c-a7f0-4e3dff8e057d | -2.912 | -49.428101 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a43badc-d500-330a-945e-461fbccbd111 | -10.3908 | -44.474701 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1d25b59-aed9-3d37-841b-bca61e31f43b | -1.1237 | -51.6586 | 2024-11-20 00:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9919998e-3856-3486-a8e7-3bcd5550baa5 | -9.1814 | -44.726501 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39b21199-480b-3fa7-aee9-a125eec9dcd1 | -5.3857 | -47.007 | 2024-11-20 00:09:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 14faf2d8-d14a-33e2-8e54-bbb45a60e1ea | -3.0589 | -45.843399 | 2024-11-20 00:09:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fecfc594-3998-333d-a265-046a45a1a003 | -3.1228 | -49.129101 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f5f489-7382-38ad-8f49-42ef6404f861 | -4.2292 | -46.104198 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abef6dc0-55dd-3ac7-8fe4-a5d7dd9e24b9 | -2.9218 | -49.4259 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eaeb2ae-8493-3ec5-986b-5b12531a26fc | -3.2944 | -43.822701 | 2024-11-20 00:09:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1962c6fc-86fa-36a4-9b0a-7a039c38b7c0 | -2.8002 | -46.6646 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03cdf8d4-e84d-3431-b27d-75f54f4dce4e | -2.9764 | -45.429699 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b10f9d49-b910-36f7-b27e-266aa54de0f0 | -4.6355 | -49.012699 | 2024-11-20 00:09:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 648f8e58-3722-3b3a-98d2-8cc9c62a29af | -3.3811 | -44.435001 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e02587b9-1cb5-3301-97de-6a26345ac910 | -4.1588 | -45.512402 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a10ef85b-3bf5-3b1b-98e2-bc7086450cec | -3.1241 | -48.5798 | 2024-11-20 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c94b9ba3-56ca-3427-abd1-b6cec9d54309 | -3.8697 | -46.061401 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64a18798-6d7a-3119-b654-e43a3511b14b | -3.0033 | -50.999401 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748ba831-984e-3f11-92ca-87fd895a58bb | -10.4464 | -45.0611 | 2024-11-20 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4abdfd4-be21-3798-8f51-79791f97aa0a | -2.0183 | -46.529301 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794cb9e3-1809-363e-baa0-cb95158674e6 | -2.9113 | -48.314999 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cea5f896-10e1-3344-9c3d-84029b642938 | -4.1557 | -45.498299 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad6996e2-3a56-3473-8f49-5cd1ebdff767 | -2.9098 | -45.270802 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7feb60b7-ed94-34e4-a719-feb279b557f6 | -3.2493 | -45.130798 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 211e83d7-5435-316c-a18c-5b865f24821b | -8.3091 | -45.1091 | 2024-11-20 00:09:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d12e5035-2cf7-3633-9600-91e77e48c1b2 | -1.9806 | -46.590801 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf9ae12c-1805-3f91-86ab-0a22d2d958f8 | -4.0441 | -46.843899 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90e5ffad-553e-3e16-b3d2-d0adb47b0ccb | -4.2974 | -43.7001 | 2024-11-20 00:09:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5004b686-821f-3a97-bb40-dc956325a414 | -2.9878 | -45.434502 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06ae36b1-979c-3331-9350-b4730d78c19c | -9.17 | -44.7215 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 528f9b1d-cadd-3d8b-86b1-a8aa63673684 | -2.9936 | -51.001499 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cfc4bfd-d0f3-3b82-ad52-b6b73e3b5d9c | -14.8618 | -43.1488 | 2024-11-20 00:09:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8bd45b65-11f0-34fb-a91c-8e2cd5a8a69e | -0.8775 | -47.867001 | 2024-11-20 00:09:00 | METOP-B | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16edef5a-a1b1-3274-b1c2-5f5a52e65f16 | -3.7928 | -47.796299 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35520867-8f43-339b-849b-c05b8f0215d6 | -3.1282 | -49.107201 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e770a8-961e-3416-a072-67e8502f7a14 | -3.3042 | -43.820499 | 2024-11-20 00:09:00 | METOP-B | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b0e72f-8672-3051-940d-7242edf4d95c | -3.5803 | -43.628601 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e48f3842-ef78-3f09-a280-ede1d699ee83 | -3.9596 | -46.094898 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25a02aab-dc86-360b-9e62-bfa4712c975a | -3.2902 | -50.350899 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179e7c94-7711-39fb-9325-526410901eba | -2.504 | -46.399601 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdf6b318-d762-302f-945e-b147eaf6cdf5 | -5.2448 | -43.834 | 2024-11-20 00:09:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc09461d-9509-3593-afbb-187adee509d5 | -1.0872 | -51.723598 | 2024-11-20 00:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4d5cee-56e9-34a4-bf85-ea40efb07da4 | -2.6063 | -45.891399 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3b7567-8057-3e96-9e80-558a2efd005c | -6.9343 | -45.078899 | 2024-11-20 00:09:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 903e7aab-2273-35ae-bea2-0c65c3fbe132 | -3.0761 | -45.965698 | 2024-11-20 00:09:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a17348f-83f0-33b8-9e07-0dc6f64b65c6 | -2.8231 | -46.675098 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f449aeb7-eae0-3bac-b792-8341f78a9df9 | -3.0323 | -45.128399 | 2024-11-20 00:09:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1658c6-e647-3116-8033-03f48a3ca520 | -1.8432 | -47.8144 | 2024-11-20 00:09:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7fb412-2c31-3e91-bd2a-b9b961c7cc14 | -5.5802 | -46.164799 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a99c5a8d-c7c4-34e0-a30e-809d471be5ce | -3.8681 | -46.054199 | 2024-11-20 00:09:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb9b07ab-60a8-3137-b6ed-e8b0e6bd0bd0 | -3.3459 | -45.102299 | 2024-11-20 00:09:00 | METOP-B | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d364d2c-8a0f-3712-9ac5-afe7bb62d049 | -9.6383 | -36.3773 | 2024-11-20 00:09:00 | METOP-B | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97c46ee5-ebe0-355d-8ba7-bf2715799600 | -5.1732 | -45.444401 | 2024-11-20 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3b61f3a-c620-31cc-a3b5-1aaeca043f9c | -2.6794 | -46.217602 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45a6cbf3-d232-36de-823e-2b3279ebb707 | -5.7158 | -39.3288 | 2024-11-20 00:09:00 | METOP-B | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a50ce4eb-7cdc-3dec-919f-cea38711e1db | -2.596 | -46.258499 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f815c81-f700-381f-9f41-4d56548a2768 | -9.9192 | -44.480301 | 2024-11-20 00:09:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 216554ae-1e5a-372b-8402-7508bce685e6 | -2.6688 | -46.077801 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df4e0186-f091-3bf0-9e64-a5980cb27a03 | -5.4088 | -47.3922 | 2024-11-20 00:09:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
