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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19e0e12c-95a6-3e78-9343-8d82fd97584d | -13.68118 | -43.00555 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11b9c802-c0a4-387f-8f4a-a4f2e0a10463 | -12.07536 | -47.88713 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee4f8d1f-a4e2-3484-b85f-88adad156a44 | -13.68589 | -43.0057 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9696d6b6-132d-3069-a44e-a36cb33783ef | -12.66378 | -46.75199 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a22863c8-0649-3332-ae5e-10fcb6e5fa03 | -7.84059 | -44.29058 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a66b320-5d22-3ba7-93af-6624d9f62a3c | -10.06034 | -44.76938 | 2025-11-14 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 563b9dd4-5d1f-327c-b3f0-e38680ef5807 | -8.94282 | -49.81585 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45897aa1-0acc-3d5f-8375-1e9a3394687f | -10.10361 | -40.89643 | 2025-11-14 04:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 90df1665-adc2-36d2-afd3-e556793c62db | -12.71384 | -45.42524 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9070946a-bd0e-3b98-809c-3e9f49dadba2 | -12.70465 | -45.42401 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0506876-be74-39b5-88c4-ad280a1ea300 | -11.0934 | -43.17085 | 2025-11-14 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2074a128-d6be-3027-94f9-06d088a5ae88 | -11.93328 | -43.94913 | 2025-11-14 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc6e534c-5925-333e-8f1e-e3b72f261b1a | -10.75954 | -44.91478 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ba52b4f-6f93-3491-ab53-605f2cbcc7a7 | -7.88067 | -44.88047 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef5943f6-218b-3582-a9a6-b1f686767ebe | -12.03993 | -49.44302 | 2025-11-14 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46505685-050c-3d25-b4cf-6a014aa5a1cd | -7.7721 | -46.32354 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de69e7db-8898-3229-9eb6-5ae014a801d9 | -10.9236 | -44.5893 | 2025-11-14 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90c2d935-c784-3146-b867-c6aec5de57a2 | -7.38799 | -48.65221 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f40437e2-28b0-3ca3-a4fc-74b0df2c54e1 | -11.73608 | -48.53882 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbfaab1e-f039-33c7-bc92-47ac8dc45fb4 | -12.9951 | -43.8443 | 2025-11-14 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5b947e6-46e9-3b0d-b874-42973dba8dc8 | -7.9382 | -44.33387 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e9022d-1838-3246-b984-a44ad2b9b3b9 | -9.05174 | -48.71635 | 2025-11-14 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c56d490-c2d1-3760-bfd7-82dac5b9c9ae | -11.7282 | -48.51475 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32c4fc7d-2c28-35f9-8bdc-f25b544934a0 | -7.85048 | -44.29486 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fec010e2-bfd8-3fdf-be30-8cde33cd1134 | -7.85314 | -44.30217 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0f14eeb-6154-345e-ae4a-883b8b94dccf | -8.90417 | -44.43987 | 2025-11-14 04:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 295a31d5-9d98-3c71-b577-5947fce91794 | -11.84983 | -49.21409 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a5352b04-12a8-3e80-bc37-b44d8143b4b3 | -13.50029 | -43.64222 | 2025-11-14 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 745ffb8a-6125-3cd7-a8e7-249b62039d63 | -10.70146 | -44.49295 | 2025-11-14 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7bf2c0-109c-3a91-9ccc-355271720138 | -9.3481 | -46.59501 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86d87ef5-3efa-340d-96df-6b24bd1829aa | -7.87029 | -44.31441 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74fab928-a7c3-30b7-afc1-ed2a7c236836 | -9.00283 | -44.17387 | 2025-11-14 04:46:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d1ecf83-8df6-3f7d-872e-ccf57cae58c9 | -13.47231 | -46.49413 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43f1dee1-4fdf-3cad-96fd-8ce4a5db1a65 | -7.73089 | -47.25583 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3912d2aa-fbc8-3e3f-a17e-fdaea00bad4c | -9.68148 | -47.893 | 2025-11-14 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 860c1400-e7ca-3f0e-8bed-397f7d5e3053 | -14.69659 | -46.61242 | 2025-11-14 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9634a92c-6247-397d-ad40-b835429f4488 | -7.94315 | -44.32753 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4adc1252-9ac6-34b0-a6b2-f1cf72c346c2 | -9.24874 | -45.20232 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aee062c6-c798-3457-9434-60a0513685c9 | -10.63042 | -45.01009 | 2025-11-14 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6651db63-cf95-33ef-a0fa-d44d76321376 | -9.11615 | -43.95417 | 2025-11-14 04:46:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b993e8c-8154-3140-becb-3f442d790381 | -7.93958 | -44.32433 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79ae0904-6ab4-3e23-8bc6-0e09c7e00f24 | -7.38388 | -48.65558 | 2025-11-14 04:46:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5731f3a3-d373-3249-b834-104028bbd84a | -12.67192 | -46.75012 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 439d1546-5b28-3184-b74b-ddda70972a0a | -12.08215 | -47.8861 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34419fdf-c0fd-3f00-bea0-1469059bde78 | -12.68962 | -45.43166 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1fa7b294-5e78-3b28-81ed-f2d590863e98 | -9.93647 | -45.09447 | 2025-11-14 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01463d45-2ba5-3220-8edd-4b1bd746f52f | -7.02397 | -46.43712 | 2025-11-14 04:46:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca996ec2-c01a-3d71-aff0-d0a379f61fbc | -10.75492 | -44.91403 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da1e5844-fa66-3bce-a770-c5f98ec1a9f2 | -9.91417 | -47.86385 | 2025-11-14 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95971e72-6e3c-3eee-9159-7a7240aeea8b | -9.68082 | -47.89749 | 2025-11-14 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 921acde8-391a-3032-89fb-52a69bfbb7f6 | -9.11686 | -43.94896 | 2025-11-14 04:46:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11b37e3a-84bf-3906-a313-1d840eec511d | -8.91076 | -41.07465 | 2025-11-14 04:46:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c4b43a7-e99c-377d-95e5-9aae638ca448 | -13.68327 | -48.4242 | 2025-11-14 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad4d0888-fa56-3d57-ba13-cc04a3c69af6 | -12.69088 | -45.42211 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4c96f45-2c19-32eb-be2e-cd8ac53c4719 | -13.68542 | -43.00949 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59b39c38-989d-3a64-ad6c-f9b42819bb4e | -13.50051 | -43.6404 | 2025-11-14 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9151b51-caad-339d-bc1e-3a2797430c12 | -9.95281 | -44.94167 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f72aa4eb-320d-3288-9920-86441661d944 | -7.92828 | -44.33731 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b2eccd7-c720-3278-9f83-41ff3046b1c1 | -13.96609 | -47.05727 | 2025-11-14 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70654cc7-defa-31ec-9251-85653f16568c | -7.84585 | -44.2942 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2050472-2569-34cc-ad0f-606c36f333ec | -7.49477 | -47.33356 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c569abce-3e12-3e7d-befd-88bfd5adec1e | -11.59609 | -55.55656 | 2025-11-14 04:46:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48169019-cfc0-35be-99b5-d6511fcc887b | -9.1405 | -45.17497 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a45dec13-eaf6-3230-a0d0-718d046ef094 | -12.66745 | -46.75657 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d6a9e04e-49aa-3965-9d63-741b83ddc375 | -12.68191 | -44.14855 | 2025-11-14 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b15bfaf0-b9c4-3086-a39e-5c7646c452b8 | -8.53721 | -49.58352 | 2025-11-14 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93b64ab5-8353-3b47-8836-f3a0c695fa86 | -11.85639 | -49.21933 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7eb2feea-3e70-3b26-85ad-8bf2dbaeac53 | -12.66409 | -46.74495 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c581bef-b6ac-3a52-91d0-51e75d777f81 | -13.91889 | -42.88458 | 2025-11-14 04:46:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24d9d111-0bfb-3ae6-8cdc-f27e39b9e1fb | -7.93564 | -44.31891 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da7ee9e2-33e5-33bc-8b54-198b088d2240 | -13.00025 | -43.84489 | 2025-11-14 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a5992da-5aa2-3641-b4d0-16376588cc3f | -9.02489 | -48.75438 | 2025-11-14 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b77f64-45ba-397d-912b-d05608d933c3 | -9.35287 | -46.59601 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6475a427-e2d0-3cdb-810c-51d0f05d948e | -11.17063 | -43.57409 | 2025-11-14 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b5aced-3887-3ad0-9e85-a3eaeb5b496a | -10.75147 | -44.91282 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d8c6f71-4b28-31b1-b259-9bbbc29b5edd | -9.21877 | -45.18999 | 2025-11-14 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1903bf5e-da3e-3af0-8050-f1545aa2825e | -12.66326 | -46.75595 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c5813743-8569-3f01-b84a-4ea7f65a41a7 | -12.65934 | -46.74828 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2097b54-1707-3deb-933e-9fcbaaf74ea1 | -11.74175 | -48.52592 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca3ef44a-112b-326a-96c5-6ba339fd46f5 | -7.85777 | -44.30283 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b846c6c5-375a-3c2f-9d57-16145c8797f3 | -12.01788 | -46.77005 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27cea9d5-0219-3672-bd2e-79a1b4a920d8 | -7.93456 | -44.32143 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd4ca18e-d29f-3a9e-8923-5b87a36a9fc4 | -8.93942 | -49.81533 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4648b9-bce4-3d21-8f17-7e27ee82006a | -7.66983 | -45.88047 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ef9b797-8881-307b-9f17-1626dd6aa5ff | -7.73103 | -47.25304 | 2025-11-14 04:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a792565-b89d-3484-862d-8185ad9b9c79 | -8.90975 | -41.07713 | 2025-11-14 04:46:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c1940def-a530-3b92-a15d-9148415ed623 | -12.00488 | -46.77218 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6da640a2-c116-3308-96de-264639999952 | -12.07603 | -47.88234 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82e8976c-94f6-373b-ab77-56ab39988132 | -9.58328 | -46.6391 | 2025-11-14 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf975343-1faa-3f1e-bfd5-09c4d4dd9cb1 | -7.84522 | -44.29124 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ac8f8f9-65cd-3e66-be87-f0d9382e5253 | -8.54063 | -49.58403 | 2025-11-14 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb3f6c97-20ae-391a-8c42-86a076e2d1af | -11.85516 | -49.22764 | 2025-11-14 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 599181c1-081e-354c-9d28-93dd301ff52e | -12.00957 | -46.76891 | 2025-11-14 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ad0bb9-d7b1-3d1a-8d1f-89f02be394db | -7.84984 | -44.2919 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaa6ad38-d199-3ed9-ad6c-000e13ec0976 | -12.06107 | -48.21376 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e129def9-0be0-326f-8897-b2c3d3ee9cb7 | -11.80745 | -44.26263 | 2025-11-14 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5feef55-38c8-3b03-97d4-f62aad051ba9 | -9.95737 | -44.94233 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c86b96b-3def-36f1-9a01-7fa488528063 | -7.84852 | -44.3015 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 535fc4ca-4e21-3c9e-b52d-98057efae574 | -13.2742 | -44.25764 | 2025-11-14 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267fb12e-0ff7-39b9-913b-702e753a8fa2 | -11.66502 | -48.46579 | 2025-11-14 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README48.md)
