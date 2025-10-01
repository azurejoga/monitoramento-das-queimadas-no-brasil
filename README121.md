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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00c64ad5-a0d1-38e9-835a-023dbfb7c7bc | -13.33012 | -47.87537 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2ba78d9f-925b-3f31-b0a3-5d5682c5557c | -10.23696 | -52.70162 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8dbc12-dd04-31d0-859b-10c1c8897b52 | -12.76945 | -50.55587 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8d39d9e-ba26-339f-9343-8cdfddb3e84f | -12.70328 | -46.90107 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 663ea990-f4ec-3ee8-acbc-16b2b3a78126 | -7.39341 | -44.61137 | 2025-10-01 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7681c9b7-bf38-3380-909e-0d20f9932ff7 | -7.0559 | -46.42402 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13aa5bbd-f1ad-3a99-8ab4-4a7d28bddb50 | -11.78316 | -47.58752 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ade9b0ab-23fb-39fc-9a23-1bf634a04910 | -13.32651 | -47.82639 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a4950bb-143c-37ea-91fe-036bb1b82e7b | -11.85636 | -45.00397 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0936d118-de9c-3bfa-8392-87b6eab5d359 | -10.73476 | -45.38382 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f93513d-7af6-3659-8c7b-91be13967d56 | -13.41201 | -48.19798 | 2025-10-01 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dcf0cda-2eef-3eef-ae1b-0db93815031b | -11.75818 | -46.86973 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbc22978-e8ff-3e24-8008-59905cd5dc47 | -11.80362 | -46.62391 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 536e76aa-7115-3db8-a61c-2676ac5ff25b | -11.05771 | -47.82184 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4423cc1a-79b5-34f1-8c8c-b2b1f854d282 | -11.46965 | -45.09081 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6be60733-b623-365d-be15-7f3c55e11220 | -9.42843 | -54.71488 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 119551ef-3ec0-3fc7-9922-41ea17775530 | -8.92475 | -47.5828 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54b8dafb-8716-3b69-b03b-fd1cf3307613 | -9.35146 | -46.33412 | 2025-10-01 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3489be51-fdb4-3372-a048-160a4cb5233b | -11.12554 | -49.79004 | 2025-10-01 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df44326-3e0d-3e5f-93e2-83a800678ea9 | -13.32822 | -47.86359 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6ea33b9-f0ba-35a4-ab30-fba851fe1ad5 | -11.04564 | -47.82396 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe18303c-a86c-3478-baca-533d19ae55fe | -12.95252 | -46.42442 | 2025-10-01 05:10:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 954d1f03-5188-3b65-bdac-90eb94ddec3d | -11.1445 | -54.30395 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6f0ff285-647d-30ca-bc43-ad74c5540b2b | -7.83004 | -47.06039 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65896c8d-fa42-3400-8dbe-8655bb7ad306 | -11.05722 | -47.8258 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd8a6cd3-6746-3151-b83a-553addb9965d | -11.82538 | -44.97635 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f04e9687-90d9-3159-b1a2-0a85b1bc7f24 | -12.90782 | -46.8185 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8427e223-25c0-3fd5-89ee-620c77861031 | -13.13657 | -47.42433 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc127b89-06af-3e49-bab1-94127a505076 | -6.95041 | -63.10409 | 2025-10-01 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 355cb8c6-9245-35cc-9c0d-81bcfc306a44 | -7.82864 | -46.98355 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0c67036-6308-3007-b452-4039693964df | -12.97219 | -48.42714 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e43af7e-8a83-3769-aae6-348148eebc49 | -13.30633 | -48.70316 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 105f3d5e-1f1c-3ee1-a320-425672b5bb3a | -13.36994 | -48.15952 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90cef949-ec3f-3d61-9105-23ee72059bac | -11.33527 | -56.20998 | 2025-10-01 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7554067-f22b-3c59-8eff-81288ead0457 | -13.13046 | -47.42355 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e1bd46a-03a6-30f7-bed2-74cb24aabbb4 | -10.6259 | -48.59201 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25b313d0-0175-3829-9280-df373ee2979c | -7.05108 | -46.41394 | 2025-10-01 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c40a8cd9-be63-3abe-bad0-d67a88f84344 | -8.88009 | -46.60852 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e45714-297f-3038-8e21-834424d96bb9 | -11.62781 | -47.49273 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5d0a435-c6c5-329b-9a8f-e531b2adb73f | -8.54357 | -44.64236 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63daf85b-0db3-385a-8fec-d3c97fe24aa6 | -11.84633 | -44.97878 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24e64924-ab40-3bad-8d17-8853cab3db37 | -13.32303 | -48.15395 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb73a49d-5d7c-3b5b-a1a4-f5d8663a2024 | -12.83794 | -46.87002 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b675e99b-d011-308b-8198-709e5f092265 | -12.85182 | -47.03065 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ae0ed07-95e1-3d3b-87db-acb0dc948f77 | -11.47124 | -45.0773 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64b65d24-f8cc-3fa9-bc59-6c196d1e9677 | -10.28368 | -50.46355 | 2025-10-01 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fae97e60-ba4d-3466-90f8-85b07c380ede | -7.76696 | -47.39053 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1323c337-b953-37d5-88c3-40ed85a175dd | -9.43259 | -54.71863 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5cccd7e-ee0c-3a38-989d-3d99a0d7bd93 | -13.31035 | -47.21474 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b2fbe72-fe92-3f42-90f4-792b5e519d0d | -9.5183 | -54.74005 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b17270a0-b47f-3647-9e69-092af60e7779 | -13.22954 | -48.45205 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f90e127b-d5ae-3024-9002-e34f7b82ca90 | -11.81833 | -44.97618 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3635aefa-8df4-335d-a31a-b5f2b8d75292 | -12.78321 | -46.8714 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f8909c0-1899-3bef-83aa-e296af97fc67 | -9.47084 | -67.89323 | 2025-10-01 05:10:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4dcfbca-b170-36ba-a184-68f03898cb97 | -12.85042 | -46.8729 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad162e3-8198-3ba9-8e0b-0bd9234e32ef | -8.97407 | -50.26744 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c9fa30-d650-3f9c-b004-3853524686a7 | -9.29994 | -54.52686 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb553f94-b59c-3f10-92e1-9a61e3328ab1 | -10.03607 | -52.10297 | 2025-10-01 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7cce7d3f-d176-3ae2-85f8-8f4379571a98 | -11.14828 | -54.30453 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 25189f58-3b4d-359c-ba27-5a3d07c1159e | -13.36812 | -47.30283 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5097f2c5-5a37-3053-a112-8827d099fc4d | -9.85334 | -44.60365 | 2025-10-01 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2e5bfc6-9ee5-3add-8332-f5c087ae6dc0 | -11.81613 | -44.99602 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a02520df-12e9-3e84-bb24-77c722108437 | -11.46944 | -45.09121 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea5cdd8e-e633-3247-9668-64fbe725f3a2 | -7.8835 | -47.2802 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bec3dbf-4eb6-30fe-8159-bc173c7a79fc | -7.82766 | -47.07147 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cd2398d-cd91-3870-bb79-b78f353c9495 | -7.83082 | -48.19468 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fe810d2-fea0-39db-b460-587b30705a2b | -12.69164 | -48.55859 | 2025-10-01 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2e59180-f7f9-3764-b3d8-bfe585153ed9 | -11.65106 | -47.50137 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b634ef4-e2b6-3280-9d0c-10b7ced180c4 | -10.81213 | -45.36581 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8e638bb-737a-3393-8738-4703be735654 | -12.8743 | -46.7737 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7947a25-bff8-3ff7-8680-aade8e2f6cae | -10.81284 | -45.36002 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee824e58-a74d-303a-9fa8-46c72fce1043 | -12.80603 | -46.89521 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10b9b2b6-d18d-36b1-ade3-a762c83606c2 | -11.46206 | -44.97572 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8074080c-9c70-39c6-a884-2cbed51e852a | -13.30928 | -47.22399 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0776af9-399f-3f67-bbcd-fbd881527673 | -8.22341 | -55.20256 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9fb81cb-5c8f-3b33-aa8d-4dc6a7803681 | -12.87487 | -46.76863 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb946a48-be8f-3afd-b8fe-6c81967903a9 | -7.7184 | -47.22957 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2938ffb-bc9a-3766-9469-8c322a643c94 | -8.55206 | -44.73323 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 111ae028-d01e-3cd3-ae78-12c22736a1b1 | -11.79353 | -47.60151 | 2025-10-01 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7749f403-9b0e-3aa0-9cd0-5bf851e20593 | -11.46347 | -45.08378 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ae646ac-9828-3b02-9821-1653982060d3 | -8.75447 | -45.93028 | 2025-10-01 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0743cc6d-ff99-393d-a8c6-d250e3d2308c | -12.77482 | -46.88898 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d8fc9e3-0dc1-383d-860f-e59451e3ce51 | -8.55326 | -44.73375 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ba4f947-881c-33ae-822c-5367977928dc | -9.47556 | -45.50107 | 2025-10-01 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58f014fc-465c-33dc-946c-a38a93238a73 | -11.79668 | -46.62855 | 2025-10-01 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a1d96f02-b7c7-3e7f-ba76-67b8b377d29b | -12.82439 | -47.01041 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c55ce5ef-d450-3016-a59f-3e7e590bed44 | -11.83927 | -44.97864 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53d3c48e-785a-30f9-9fdc-009c69d0730d | -13.21455 | -47.34248 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40f880ca-677a-3152-85d1-78681ca96c0f | -12.94442 | -48.41629 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 669cc015-05e3-32aa-b072-b522941c7eb1 | -12.9784 | -48.42397 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7c82f39-9140-3a17-8c93-277fc5786fab | -12.21476 | -47.80656 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68b40364-de7f-31b8-99c5-7d05e03c174f | -9.5085 | -54.65644 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0213e7f8-bbea-3147-b7c2-f8642bb060f3 | -12.16075 | -47.77387 | 2025-10-01 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd2020d7-8fd0-3e3b-94a2-66a1c1bec472 | -11.43646 | -55.05051 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c73d0b6-b237-3b10-868a-2201dce9742b | -11.75754 | -46.86177 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab60886b-c4c8-3cbd-8cc8-fccce137d0fd | -11.76216 | -46.87674 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbeae940-9292-3606-9887-a7fc5e623369 | -12.8377 | -47.0435 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ad2822d-130a-3296-bdfe-8d9de76a820b | -13.03108 | -48.67241 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c7831db-84d1-3293-878f-685c8ca21f5c | -8.54884 | -44.65041 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 964900f5-b3d4-30a7-96fc-62c4a007cb47 | -10.77288 | -45.3714 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README122.md)
