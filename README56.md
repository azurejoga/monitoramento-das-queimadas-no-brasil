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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5385b5d0-c1c3-38c0-830a-e3afac2b3b9d | -18.27672 | -52.70469 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 48ce53ee-dc13-3869-958d-bf9e91274afa | -18.28581 | -52.6831 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 79df6e3b-d88a-3d04-b8f2-8724359e1762 | -18.2743 | -52.71178 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b23f68a-9b4a-3c79-8f0a-266a3128a32f | -15.61597 | -56.41462 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70a86c34-01f6-35de-a2fa-c2f15055161a | -15.63533 | -50.09822 | 2026-08-31 05:01:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6606f34-a2b1-3657-9da8-fc537c8b4a4b | -17.28085 | -46.00377 | 2026-08-31 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f1812db-3227-35ba-8800-f35490feccd1 | -16.35996 | -51.01007 | 2026-08-31 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c33a8791-756c-396a-89dd-b3a23b51cf94 | -18.28708 | -52.68596 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 774ae749-233d-304a-aec4-50ee5613e0cc | -17.3135 | -54.94315 | 2026-08-31 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fc256d2-bd83-3121-8b32-9e5fd7886db9 | -15.64028 | -56.38934 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfc8ce9b-af55-385e-822d-fbcba48046b4 | -15.23916 | -56.38902 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05bfb3ce-72a8-3ebe-a14a-6cb16d75a6b0 | -20.3725 | -47.46024 | 2026-08-31 05:01:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bf993d9-7d91-39f3-9c92-35d3f9c66c4b | -15.25724 | -53.87804 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1831daf1-c41e-3d8b-9b6e-ff275eb7fcdf | -15.61266 | -56.41407 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cbea5e4-bd03-31ee-b161-7a0bda4794fe | -16.28592 | -42.58112 | 2026-08-31 05:01:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcaeb9da-8efd-36ae-81aa-ddb9e98f8cd2 | -15.24083 | -56.37833 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0480afd-5f36-392e-a408-924ffa34fcb7 | -15.23254 | -56.38792 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6799dc8-9425-3099-a3c9-c5f1d2fbd1d3 | -18.27155 | -52.714 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9a9be1f-c721-34b2-b1ce-515dbb8c6408 | -15.61653 | -56.41105 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9999efad-ab94-3073-8faf-255c6bc7ecbb | -15.26074 | -53.87856 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90412442-a6b9-3397-9658-1b6d028d3356 | -15.2392 | -53.87939 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73af322d-b17d-3750-b4af-6083b81e60a1 | -6.6035 | -58.6166 | 2026-08-31 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b07eac10-de20-3762-95da-8c43426d9a77 | -20.243 | -58.1464 | 2026-08-31 05:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 4a9f14b6-4444-3196-b2c7-3e70c9c0bff9 | -5.2548 | -55.8907 | 2026-08-31 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 62fa4c06-0704-3756-8b0d-309994b9288b | -11.1634 | -50.5727 | 2026-08-31 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 50de2b71-e958-30d0-92f4-db7dd2444906 | -20.2631 | -58.1437 | 2026-08-31 05:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 23d75b9a-d1c0-3c25-b432-dacaa7d35f63 | -5.2363 | -55.8914 | 2026-08-31 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cbb65503-d6da-3803-a260-40999903ae35 | -7.9239 | -44.2327 | 2026-08-31 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 92260bb1-5246-313c-a06b-ef94a6bd905b | -6.1294 | -57.6833 | 2026-08-31 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 4920093a-8ae2-3cba-93f7-5558d21eda0c | -7.9236 | -44.2558 | 2026-08-31 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ff1ae2c0-d33e-3775-b396-4ee02b98a7a7 | -6.6036 | -58.5972 | 2026-08-31 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b24ff031-8fc4-3279-a9bc-9c2fa16576fe | -5.2547 | -55.9105 | 2026-08-31 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| f3b1b477-9dcf-337d-8b46-5730aed61aea | -5.2362 | -55.9112 | 2026-08-31 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5acc9c05-550a-3a4a-9918-c5508fea2f3e | -11.1637 | -50.5513 | 2026-08-31 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 09395b0c-898a-32be-807c-cc504f59a50b | -6.6035 | -58.6166 | 2026-08-31 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8ec1290c-2a07-3488-8b67-cb8c6579f3dc | -5.2362 | -55.9112 | 2026-08-31 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 79f26463-9cf5-390c-a3ce-a050ea892c5b | -6.1294 | -57.6833 | 2026-08-31 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7944336b-920a-37aa-9393-94e3491f82ce | -6.622 | -58.5965 | 2026-08-31 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5194d649-eaab-3112-b8ff-8ff25b5c4540 | -5.2548 | -55.8907 | 2026-08-31 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 06e8e344-ad9e-354a-afa9-5969f073333d | -5.2547 | -55.9105 | 2026-08-31 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 8234784a-689d-3ac0-a1fa-e6e2684f1f37 | -6.6036 | -58.5972 | 2026-08-31 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 61227fa9-933d-3641-bd22-6b4896162324 | -5.2547 | -55.9105 | 2026-08-31 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| e6242654-0882-33cb-90b3-856fe7854531 | -6.6036 | -58.5972 | 2026-08-31 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 3798da45-b37d-3886-a561-4c4fe82e99e7 | -6.622 | -58.5965 | 2026-08-31 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e60fc0a1-4c31-3404-b655-992a74d8ffe9 | -5.2362 | -55.9112 | 2026-08-31 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 13b64ce4-b10c-3e2c-8de7-6b4ac8f69141 | -6.6035 | -58.6166 | 2026-08-31 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 92849fd8-754c-3ff4-b027-3642cf293fc0 | -20.2631 | -58.1437 | 2026-08-31 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 4640c679-f81f-3bfb-b239-84df38a997b6 | -6.1294 | -57.6833 | 2026-08-31 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e51e8611-0000-328b-a931-c773a8b633d9 | -5.2548 | -55.8907 | 2026-08-31 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| eb85ed21-b970-35f9-8c90-d7dc8b27a86a | 1.66305 | -60.1395 | 2026-08-31 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 605d5808-698e-3c01-96a7-a1c4d740fbd4 | 3.23086 | -60.13856 | 2026-08-31 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb8fa82e-f952-3ef3-be9c-3702d5881db4 | 1.76803 | -60.22982 | 2026-08-31 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b50de2b8-6d72-360b-aa46-bc08ddd22c54 | 3.22746 | -60.1391 | 2026-08-31 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9069ee66-2df1-357c-8f8a-9bcd72eefdee | 1.65968 | -60.14003 | 2026-08-31 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21c00820-8160-3342-9b9b-6222642efec2 | 1.76859 | -60.23342 | 2026-08-31 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9885df9-1286-3e74-979b-62a14c33f8ca | -1.59661 | -54.40309 | 2026-08-31 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb62608c-0b8f-3ead-997e-8f5ba9beec65 | -6.61596 | -58.60159 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 569c999f-a51f-30f0-b911-f0532ae414ba | -6.12456 | -57.67418 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7499fc55-18b9-3fe8-8b9c-edb0ba215774 | -3.0856 | -60.71167 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6409df1d-af6a-38e2-82e6-b4e11a6aeb26 | -6.12864 | -57.69573 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a00a46f-e4c7-35f1-b625-02bc88d572ac | -5.89382 | -57.75387 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d20859d-4552-33a4-b4bf-88db9956c46f | -3.79784 | -59.61412 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de2cc375-396a-39dc-b16c-c027fb041391 | -4.92185 | -55.76884 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c777f8f2-9bf4-3eca-81c7-7291b3fe85e4 | -5.24863 | -55.90438 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3284a41a-5ee8-36c6-a0fd-11464de7337f | -5.95884 | -57.68005 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8451142-46d6-3f59-9534-69af1aed8c09 | -5.48476 | -57.14897 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64f3ccfd-0ea5-308a-a708-ba550457c6b4 | -3.62374 | -60.56083 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e8be66d-70c8-3b9b-8a46-f89edaa3ad5b | -4.66651 | -55.92972 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a00b9c84-700a-36ce-8d56-bbc732086ab0 | -6.78639 | -55.67668 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d052e41f-0b07-3810-954a-532661d228fb | -2.66545 | -59.37296 | 2026-08-31 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b3eca1f-96f5-3812-a1c7-2ff122eb6eb2 | -1.24823 | -55.69849 | 2026-08-31 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f92148d-bab4-3200-b4ab-4f2bc8d659e0 | -6.77843 | -55.64604 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4131f3e-761a-388a-b5ec-02a18a837c81 | -6.27666 | -53.32975 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3b0ab57-052b-3490-b3a2-a8139a4bef6e | 0.14629 | -60.3966 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91b51dc6-06ba-363c-928f-ba1c1d72d0ec | -3.1768 | -53.16041 | 2026-08-31 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02d47862-c5a9-3e53-b156-51831d5fd4e5 | -6.92054 | -55.72251 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 692b894d-e27f-32b2-89e8-506d26b6cef3 | -6.86184 | -56.57139 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c87f7ebd-02a2-3204-bc85-12357fc7f88e | -1.62204 | -55.16747 | 2026-08-31 05:33:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48161cd2-8cf7-366a-b4b1-3c3e776f1a38 | 0.00978 | -60.59734 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12b57957-82cf-35ab-9051-ba535c636843 | -6.56242 | -58.55858 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0119548c-bcd0-350d-8254-dd2b9463e9be | -3.03593 | -59.36367 | 2026-08-31 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c058bd1e-bcc1-387d-bce8-aabcc7415fff | -6.91861 | -55.70764 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fae941-f39b-3896-92a1-04d16aee9345 | -6.605 | -58.60378 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 2092dcba-b1f5-372e-a427-ff311b0c1b9b | -6.1067 | -57.86529 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bd753cd-c586-3ff1-bbdd-2c5f831872e1 | -5.94984 | -57.69111 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0844c63-d4ab-3d40-91b8-db7474b1c81e | 0.13914 | -60.40485 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85a2ae4a-1a5d-3ca6-927f-7a12c366334e | -4.15534 | -60.68841 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a87a6dcc-2916-325d-aaac-4f0152cab61a | -5.24547 | -55.89886 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dfe41a10-56c6-3376-9ddd-d644dbdf05a2 | -3.96664 | -60.0236 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d88fb4d-30fb-3c3d-a62e-cb2705d11984 | -3.19915 | -58.99656 | 2026-08-31 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f41c20-c584-3ea1-943c-9e1fe854d21e | -2.66877 | -59.37347 | 2026-08-31 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5247493-7c18-326f-a6bd-a9ff6303ec97 | -4.15534 | -60.70978 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61b1caa1-92f3-35ed-bb06-cd3d4f70bc19 | -4.15478 | -60.69188 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4245e6f4-7799-3f46-8043-5114c32d2d92 | -4.9701 | -55.847 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ccaa4609-ec87-38a7-b1bd-747c9c5c4907 | -6.42759 | -55.52897 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6055eed9-9859-3a1f-bcbf-a78fe2e551ba | -6.9532 | -55.698 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 011125c2-86d0-3e89-bafd-a1fff6bd9ff0 | -6.7607 | -56.33561 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd6fd4fe-c3d4-3f3e-84ec-1c2c18c5669c | -5.9997 | -57.83308 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bc402ce-e885-3718-bca5-a179c72739e4 | -5.86878 | -57.77454 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22530989-d6d7-3a6c-86e5-fffd19f186b8 | -3.09843 | -61.22046 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
