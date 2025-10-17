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
| 48754cbb-c687-3cc7-b2f4-b14de158ab20 | -14.3227 | -51.4475 | 2025-10-17 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1d238f14-3db5-30f3-8753-f35774728229 | -14.342 | -51.4449 | 2025-10-17 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d61d66e6-ea0c-31a4-8dee-e9165d07d384 | -10.5337 | -49.5687 | 2025-10-17 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 10505356-0259-3221-9a00-161268b1f0a6 | -10.4941 | -43.4315 | 2025-10-17 02:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 679798dc-0ab6-3a33-b03b-fe79ac9328c1 | -10.9472 | -49.782 | 2025-10-17 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ddb9f39a-7923-3225-8ede-ea3bbe1a6a10 | -11.398 | -44.1933 | 2025-10-17 02:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| f86ad7aa-cb72-3282-8434-763cd8ff2279 | -10.9665 | -49.7583 | 2025-10-17 02:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 18478a99-186e-3d8a-90ed-31b574d2931b | -10.1528 | -44.5289 | 2025-10-17 02:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7049390a-c4cc-39c9-88ea-51234ef7071c | -10.2935 | -44.0455 | 2025-10-17 02:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 690ec8d2-1018-3633-b810-086897eef72d | -10.5132 | -43.4289 | 2025-10-17 02:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| f8bc572e-58be-3752-998f-36c10b084aa4 | -11.4172 | -44.1904 | 2025-10-17 02:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 66b87509-0afb-3798-8ef3-074a99f52115 | -10.2745 | -44.0481 | 2025-10-17 02:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 43a6af1b-bcc3-32f6-8361-2a89beeaedda | -10.534 | -49.5471 | 2025-10-17 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 87338144-2e31-336d-b5ac-766985a92842 | -8.4641 | -46.2482 | 2025-10-17 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| cc203b39-9c88-392e-b53d-fb08289a5ca5 | -11.3976 | -44.2167 | 2025-10-17 02:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 213.0 |
| e92adb75-74d5-32a3-b7be-e8d85c674862 | 1.7668 | -55.7439 | 2025-10-17 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 80ff7279-6a9e-39ce-9a60-838b4f8f6462 | -11.5152 | -44.0588 | 2025-10-17 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ef488c03-76c3-3020-aa13-5e09bd6b5037 | -10.9475 | -49.7605 | 2025-10-17 02:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8e381f3e-2fc3-339c-855e-4fddfb8325c3 | 1.7851 | -55.7436 | 2025-10-17 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7e9cd2bb-a1c2-36be-aa44-45c9c203ee5f | -10.2748 | -44.0247 | 2025-10-17 02:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 60161443-0615-3a9e-9aaf-17a1a914fe08 | -10.2939 | -44.0221 | 2025-10-17 02:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 30d61112-d76f-3bea-aa2c-d021bf1cc7cf | 1.7852 | -55.7239 | 2025-10-17 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 92823f48-2375-3347-a8e3-7270728b11bc | -11.4748 | -44.1819 | 2025-10-17 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ee5a4c12-c9a4-3995-bf0c-4d5e7043fd62 | -11.4168 | -44.2139 | 2025-10-17 02:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 94718b8c-4e36-3e96-af43-9ec2a65a8d7e | -11.4939 | -44.179 | 2025-10-17 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c78aff80-4a77-3053-b161-ef5ec7a6f566 | -11.4735 | -44.2522 | 2025-10-17 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9269e275-62cc-3efe-8539-8ac61c4b15c0 | -11.3784 | -44.2195 | 2025-10-17 02:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8310a52a-e691-3ab5-be01-11413e24af90 | -10.5337 | -49.5687 | 2025-10-17 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 80182d59-5c99-3ffb-a13f-164d7a2d581b | -3.5028 | -52.4938 | 2025-10-17 03:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 848b35cd-0768-34e3-ae40-0edf57d4ecd8 | -14.3223 | -51.4689 | 2025-10-17 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4d54a531-c54a-3aaf-a9f9-307584be7bbd | -14.3227 | -51.4475 | 2025-10-17 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b0a7c71e-5bf5-390f-90ec-8659ee1fe6fc | 1.7665 | -55.9017 | 2025-10-17 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8a7a995c-1c56-3351-9b66-54a9f0596b5e | -4.4059 | -43.4049 | 2025-10-17 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| bff32e02-9d0b-3c5a-918c-47396df935b6 | -9.1378 | -46.6261 | 2025-10-17 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 880abb38-d62b-3e0a-9d1b-993ac5a9f844 | -14.342 | -51.4449 | 2025-10-17 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4f9fb6cb-6b86-3bdd-aef2-a71bfbe2e1e9 | -10.4941 | -43.4315 | 2025-10-17 03:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 2d610a11-891a-3691-89d0-0547f9722254 | -10.9475 | -49.7605 | 2025-10-17 03:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e3bc32f5-1cf6-3cdf-b5a9-0b12a4e222eb | -10.2745 | -44.0481 | 2025-10-17 03:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 66e3b537-0e6a-339e-9c74-f126fb57ca4d | -12.1278 | -47.3329 | 2025-10-17 03:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 67a8c71f-9a0f-3b55-afb7-d55966ae4d1c | -11.4168 | -44.2139 | 2025-10-17 03:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 0b708284-d16d-3ef5-a89a-71b34a20d0d9 | -10.2939 | -44.0221 | 2025-10-17 03:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| a0224aad-cc79-39c3-be62-8e7eec2d5227 | -10.534 | -49.5471 | 2025-10-17 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 00198581-0c48-3ac5-8641-333c717b908c | -10.5136 | -43.4052 | 2025-10-17 03:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b76c7be0-fb12-3d5b-b47a-d0845170fc49 | -3.236 | -45.9639 | 2025-10-17 03:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c4345641-ee84-3a53-a073-b49990f31b38 | 1.7848 | -55.9014 | 2025-10-17 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 58a267d5-5d53-3507-ab8e-ac7f22023187 | 1.7848 | -55.9211 | 2025-10-17 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| feb73d9b-e567-3ab3-9264-dd8eab148b9c | -10.1528 | -44.5289 | 2025-10-17 03:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 53eba64b-2f97-37ac-acc5-f0adb80b7c7a | -9.1609 | -41.0458 | 2025-10-17 03:00:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 498257b1-b158-3baf-bc73-c9979de574e9 | -9.1564 | -46.6465 | 2025-10-17 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 71d5a076-3040-327c-9b05-efc61941f21d | -3.2546 | -45.9632 | 2025-10-17 03:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.6 |
| df4ccd48-03c3-35cc-94ce-18915386fa2f | -10.9472 | -49.782 | 2025-10-17 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c6dad0e4-52ec-3267-a4e1-a379916ae231 | -10.9662 | -49.7799 | 2025-10-17 03:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 54248d40-f896-388d-b82b-7284724246a7 | -11.496 | -44.0617 | 2025-10-17 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f69ff779-c8e2-3872-ad25-ab385f0b821a | -3.2359 | -45.9862 | 2025-10-17 03:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b212bb23-531c-3cb3-a8ca-0fc64823438b | -9.1375 | -46.6485 | 2025-10-17 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| f72b1d52-fdd5-35c4-90c2-fad7bea3d55d | -10.2935 | -44.0455 | 2025-10-17 03:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 228d3d2d-e5fa-32bb-995f-72056c002821 | -11.3976 | -44.2167 | 2025-10-17 03:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 3cd3da15-5688-3003-8701-8e69db8da976 | -11.3972 | -44.2401 | 2025-10-17 03:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1c9f511e-23d8-381b-95c6-8fa3d89dfa64 | -4.9735 | -44.9549 | 2025-10-17 03:00:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 661870d8-68e0-38d2-a86e-5ecdbf704b4b | -10.515 | -49.5492 | 2025-10-17 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 60447b61-1b2c-3aea-914b-f77727ed0eb9 | -10.9665 | -49.7583 | 2025-10-17 03:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b2d7bd22-a999-3ca1-8285-8d8e5fff867d | -11.398 | -44.1933 | 2025-10-17 03:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d1cc6ce7-3728-3a0b-a7d7-b516a30c7a35 | -10.5132 | -43.4289 | 2025-10-17 03:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ab5aa0e5-5fcf-3195-be90-772b5206705f | -10.2748 | -44.0247 | 2025-10-17 03:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 76610944-fa5f-3a03-bd29-d9a7898a04ef | -11.4172 | -44.1904 | 2025-10-17 03:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 63cf7d48-7a24-33c0-b027-eec165c66f62 | -3.2545 | -45.9855 | 2025-10-17 03:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 84e90439-2640-3271-ac6b-562a33db7c46 | -8.1996 | -43.3189 | 2025-10-17 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 71d6c0f3-23a6-3170-a86c-6b6dfde1f9ed | -12.1086 | -47.3355 | 2025-10-17 03:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bf9a21ef-1854-3525-bf1e-af0ee7068228 | -11.4748 | -44.1819 | 2025-10-17 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cd83ccd7-5703-3f45-84b7-abdcc4354a61 | -5.86274 | -35.47239 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3ff093a6-6b8c-3b2a-9fe4-b586c46dddf6 | -6.98973 | -39.23132 | 2025-10-17 03:08:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e1039657-d33a-3ab8-9373-d0c664b48062 | -8.6074 | -40.20018 | 2025-10-17 03:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5fe17cd0-7f7a-3bf3-8021-ae313e8092a9 | -10.02049 | -37.3911 | 2025-10-17 03:08:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b87be5a-c4db-3117-b7d4-f72bd5116648 | -5.86051 | -35.47124 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 8dd59939-fe10-3739-b610-4f448cc311e2 | -7.54793 | -35.23463 | 2025-10-17 03:08:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62a8209d-a0a3-3937-a348-bbe3c6bd15b2 | -5.29892 | -35.98138 | 2025-10-17 03:08:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e65b859a-3016-3eb7-aafe-f2573e05a9c7 | -8.61095 | -40.20497 | 2025-10-17 03:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 42e6b437-754d-3adc-94a3-aa6b97d705ab | -5.85648 | -35.47514 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 09715986-7c57-349f-8dbc-99f0c7b2004d | -5.86208 | -35.47619 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 186f82a3-2621-3e4d-a697-d632ff581fd3 | -8.60524 | -40.19628 | 2025-10-17 03:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07ff85ac-77d4-33ef-84e8-a6d211606528 | -6.99119 | -39.23246 | 2025-10-17 03:08:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e181362c-20bf-33c9-aae8-9f443be939dd | -5.29965 | -35.97722 | 2025-10-17 03:08:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 176b4b34-8860-3b0c-bea6-552bfcea098e | -6.99676 | -39.23207 | 2025-10-17 03:08:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 10bff2cd-1455-3393-964d-43170fc73b29 | -7.54732 | -35.23798 | 2025-10-17 03:08:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d82a9149-ce21-35b7-ad53-ce7145432483 | -5.85714 | -35.47136 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b9ecc64c-d8d1-353e-a583-3f277933c176 | -9.30625 | -40.22931 | 2025-10-17 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 50f7f82b-19e6-31cc-b8a8-7541c306bed7 | -5.85983 | -35.47502 | 2025-10-17 03:08:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 751a98a1-a3df-3b7f-86b5-a2c4df5f8800 | -8.60384 | -40.20345 | 2025-10-17 03:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3098f6e2-3bc6-3faa-a9ba-b05d4187c228 | -6.99819 | -39.23338 | 2025-10-17 03:08:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6735706e-356f-35bb-801d-2a148271fb1d | -8.61231 | -40.19793 | 2025-10-17 03:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c04f967-5d69-36eb-953b-48ddf435c1f9 | -11.4748 | -44.1819 | 2025-10-17 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 260a6dec-1351-377e-adc6-28ce2615f4b8 | -10.5136 | -43.4052 | 2025-10-17 03:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 439935f8-e280-3e83-aa37-cc44fce87f4f | -9.1372 | -46.6708 | 2025-10-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 22474d68-d2f7-375a-907b-f9b0972d7e46 | 1.7301 | -55.8035 | 2025-10-17 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a29ac81b-6cbe-35a6-af14-2ec50106da86 | -9.1564 | -46.6465 | 2025-10-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 1e86afef-1518-379b-ba8f-32c9977d20c4 | -11.4172 | -44.1904 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| cc838464-e576-3cc3-8635-e924573f719b | -9.1375 | -46.6485 | 2025-10-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 379.7 |
| ea9b746e-6e6d-3433-b6eb-8afd04148466 | -10.2935 | -44.0455 | 2025-10-17 03:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b38bc185-eba5-32ac-9c0a-c815a893b19b | 1.7668 | -55.7439 | 2025-10-17 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| dfb15767-49bd-3b1d-b807-9bd504a89d10 | -14.342 | -51.4449 | 2025-10-17 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |


[Clique aqui para ver as próximas entradas](README21.md)
