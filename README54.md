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
| d722def4-6670-38b7-91d3-89f8f7f51975 | -6.20684 | -43.40189 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f44c97d-1d12-351c-a816-b3f83e60bf05 | -3.53922 | -52.20244 | 2025-09-10 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 386217be-a377-38d2-b060-a3f9623dba45 | -5.50934 | -42.67783 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7c5abe6-2438-3274-a252-5ed1937a3f7a | -5.74481 | -47.47935 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5799d20-4085-35e3-b0fb-5ca65400bc7c | -6.16071 | -43.38588 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3230ecca-dce5-3a20-9f0c-98397bca87c2 | -6.45653 | -43.03918 | 2025-09-10 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5bf34b8-17aa-377e-a39b-5e357b7551e7 | -5.81026 | -45.67713 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ad0ad3d-2e34-3183-b433-1c78f8dc3c4b | -5.91448 | -45.7541 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a36b792-dea7-3983-baa8-289badb9bc4d | -6.2394 | -43.49612 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8fed4d1-e7ee-38bc-b3eb-019673992a10 | -5.75515 | -40.9594 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 978c2e0f-1d51-39c2-a97d-aa9784ef278d | -1.19672 | -46.15495 | 2025-09-10 04:40:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6bbeacf-9653-37d8-9a62-ef3ae61383c0 | -2.91594 | -51.97215 | 2025-09-10 04:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1566b3b4-7104-3765-b3a0-09e9b17bc901 | -6.29601 | -44.22686 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29183584-0d27-344c-9233-45c204707f03 | -6.25375 | -43.41236 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 494a6798-5b56-30ab-b31b-3b14fd60fdd6 | -5.90556 | -45.78866 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65582159-b4a5-3aac-9aa5-2961f37e3681 | -6.25437 | -43.40823 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 3de05a27-7b07-3c6d-9c35-3536f2902f3a | -6.0537 | -43.31322 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3a86063c-2ea1-3d71-ab3b-0b57b539f08e | -5.58076 | -42.91784 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f45a5e7f-a62d-3718-a984-0fd84fec4ea8 | -3.24551 | -52.85185 | 2025-09-10 04:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8780c6f0-ef75-35b6-ad21-61c26540002b | -6.05482 | -43.3162 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e3478608-37d1-39c2-b059-8524ef3835c6 | -5.89081 | -43.94316 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 311c2e3e-03cf-36aa-aef5-18e8abd65afb | -4.83746 | -45.35474 | 2025-09-10 04:40:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58d7d16e-c2e2-3ae4-bd17-a599e5d08ea1 | -5.4221 | -43.4477 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5956320-e6d9-3d07-a086-3b09bc2329b5 | -5.55707 | -45.17859 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb68974e-2f09-334e-9c67-3ad4f3d070dd | -5.44645 | -43.4592 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b05d3574-ccaa-3a53-b3cd-1bc24b7cb5f3 | -5.54746 | -45.3741 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f532885-5de7-3d76-9bcc-37b8967a811b | -6.25808 | -43.41287 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| d6b8f075-d791-3161-9e1f-96c0bdda186a | -5.5074 | -42.67517 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d6a666b-7f53-3f57-addc-f5517d2ffea7 | -5.73874 | -45.25539 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 481fe98d-f1e5-30f3-bdb8-83e79bd848a8 | -5.94924 | -45.7998 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a34e84-8c55-3279-bb9f-b6969d28810a | -3.04486 | -48.96455 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42742acd-2ae5-3c38-8260-668e169366ba | -4.96878 | -43.63428 | 2025-09-10 04:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56091f13-030e-3fcf-8dda-66d7f3b0cb8d | -4.9775 | -48.93904 | 2025-09-10 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8eed18f-4594-3114-832d-aa4d040ac483 | -4.82041 | -43.38755 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96a66e6c-0eb3-35e0-bfbf-973036e3bff5 | -5.6497 | -42.62105 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09ebc274-835b-322f-acac-52811c045c23 | -5.41247 | -43.45421 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d0192684-8691-34f3-806e-dfb536284a18 | -4.86849 | -42.7659 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73f97548-adc1-38e1-a095-88ea7b689eb1 | -6.23661 | -43.49717 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dd70a29-04cd-341f-8ca3-db4e91d0abed | -2.91169 | -48.67411 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 460d0275-b1e5-33dc-be46-8737b9565c98 | -5.41026 | -42.85423 | 2025-09-10 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 240c4366-7f1f-31a3-ad14-fea8ca20665b | -6.35696 | -44.07139 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2be874f-87fc-3254-8e81-2f65bfe5ae2b | 0.71328 | -51.37135 | 2025-09-10 04:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 394378fc-1265-3e24-8690-f506974f0407 | -4.54463 | -43.30035 | 2025-09-10 04:40:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a72a5a5-7b04-3c4f-802c-c596bb89e334 | -6.25474 | -43.41936 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 7f56c2e1-4a00-333b-9571-88effe3592b8 | -5.91599 | -45.79469 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a02d91a1-492f-31c4-a9a5-4227e75f6fbc | -6.33458 | -43.54898 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 83913652-d243-3ddb-bf9e-101f0f38cae7 | -5.82008 | -45.68773 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c3780b1-3dbf-3807-9321-a2a4acf7bf1a | -6.24728 | -43.40992 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12d783c1-e3d2-3cd8-a7c2-6937fcf98573 | -3.63621 | -49.20649 | 2025-09-10 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cc31e6c-099e-3d64-8a99-b5efbd2e3f52 | -5.78608 | -45.45182 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0bbe7b9-8e0a-3d47-87e3-7530a25f9e35 | -3.20797 | -54.96173 | 2025-09-10 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80c29cbe-b2fe-3a97-a344-77bcdbce3dd1 | -5.67913 | -45.46992 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1350d074-21bb-35b2-9f45-e3670bf3b537 | -6.19762 | -43.40474 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93dcf2e1-01fd-3a94-8efc-c09fae637ab3 | -4.1985 | -55.13562 | 2025-09-10 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57cf7a52-6bf1-35f1-8437-f8585b9ced42 | -4.09689 | -41.57131 | 2025-09-10 04:40:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2085fb96-5778-3248-9c87-1378cc644e82 | -5.57002 | -42.92923 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a79a0720-c372-3d2e-9da7-b223a0370046 | -2.09818 | -52.03244 | 2025-09-10 04:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36bf0598-b3fc-3ad0-a65e-03b7265b5ff6 | -5.68379 | -43.33777 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3acd53b0-4769-333d-9385-cacc0de130f5 | -5.45011 | -43.46372 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6908c7c-90c6-3cc0-b786-febd596df5c0 | -6.19205 | -43.50251 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8bf4c78b-bd38-3c86-9cf2-161b41cb5ab0 | -5.57507 | -42.92562 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02cf8b02-2b32-3150-89a3-3ea1cb5f1da1 | -5.74182 | -45.26069 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64933dfe-7ff3-3604-a27a-177a78c772b5 | -3.9691 | -43.23925 | 2025-09-10 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 400d8283-ed52-328d-ae93-807398d4cb90 | -5.66829 | -43.90703 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa71366-2c42-366c-9169-6391e9bfa6ba | -5.67463 | -43.34035 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba2934b-d107-3418-8a07-60f2b60fca3e | -6.33885 | -43.54969 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 42f47263-7c0f-355b-870a-f8a404d5408b | -6.35752 | -44.06767 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa20bee8-3147-3488-a11c-f99275a2fefd | -5.42311 | -45.88212 | 2025-09-10 04:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8144e7-70ad-3e1b-aaae-3afe7513de4a | -5.64329 | -43.92186 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e67d8de6-1adf-38c4-ad4a-906be0ca90aa | -6.29407 | -44.21177 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25623029-de14-374b-a406-7abad0a4f0ac | -6.24552 | -43.42228 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97b9b661-4584-3df9-a0f4-2d74386284ce | -6.19607 | -41.04451 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c471261c-b8d3-3bac-88e4-9e3295ac47bb | -5.74874 | -47.47168 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aab37c9-e768-3e8b-bbf7-0a69905cad1c | -5.75217 | -47.47218 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f1872c2-7e7d-3245-9d73-a5d007d6caec | -5.67225 | -43.35647 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 365f2660-6b98-3cae-b615-5037dc93d0b8 | -6.24495 | -43.42632 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959959b8-116c-35cc-87ee-d99448b829e1 | -3.37032 | -52.79775 | 2025-09-10 04:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c012a87a-e1c6-3b51-a943-86c63325566c | -5.75055 | -47.46511 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 226f4f5a-29b8-3bc9-81e7-8accebbd9e4d | -5.66398 | -44.90948 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0024b522-548f-3bed-8ca4-e075d0e9104c | -6.23508 | -43.49577 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6921de2e-366d-3ce1-96a4-422047f37b8f | -4.50078 | -47.82278 | 2025-09-10 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50cab191-c922-3ff5-8aaf-9ec638d194d2 | -6.17048 | -43.37922 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68baa900-40b4-3d18-a359-5bd0d78aaf78 | -4.94677 | -45.29692 | 2025-09-10 04:40:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7e4ed61-5316-336f-8f5a-462764510b08 | -5.44954 | -43.46758 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 46687d26-c36c-3b3b-bd3a-9865c1ebbf91 | -5.8263 | -44.09724 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1adc20bb-9312-3ad1-b10b-9fdde5868806 | 0.7152 | -51.37343 | 2025-09-10 04:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f99ee8bb-2f50-32c1-a97c-bd873033f5ba | -5.82409 | -43.72542 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2188358-9f3a-3e13-b271-d08296ab837f | -6.26023 | -43.41174 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 4dcebb12-c76b-310b-9560-0547807e30db | -6.26081 | -43.40765 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ea35c722-581a-3caa-a9ff-eaefcb2f215d | -3.9649 | -43.23854 | 2025-09-10 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 678d8bf3-d90a-3c2c-a20f-e84b7d7d6111 | -6.1676 | -42.65297 | 2025-09-10 04:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2dc89ef9-0db1-3879-8ece-aee6c4a03f9c | -6.17923 | -41.05394 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ccb2cfa5-5e23-3fbe-94c0-0fff99154ba4 | -6.251 | -43.41473 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c4241b3-a948-33a3-b528-b21e964887a4 | -5.53118 | -44.33313 | 2025-09-10 04:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdd80b6d-2639-3107-84ce-d1fe4bb45918 | -5.66722 | -43.9143 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28ce7cd5-9742-3cf7-94bf-4b6552c6c07b | -6.19059 | -41.04668 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6d92ba7-0a32-3c98-9e76-27ddd18ae87f | -5.66976 | -43.34361 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 806568e9-a9f0-3ded-92fb-68ffc04198da | -5.58694 | -45.04202 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| df2c171e-7048-37d9-9dc3-3603d6cffd41 | -6.3553 | -42.6087 | 2025-09-10 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b790d7f5-67c4-3a63-b310-1a9581b71b75 | -6.24638 | -43.40269 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
