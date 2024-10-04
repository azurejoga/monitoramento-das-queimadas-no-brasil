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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0312a3e7-28c2-37ac-952b-ac423296f4ac | -11.2783 | -43.388 | 2024-10-04 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 0edf9af0-aaeb-36dd-b357-d88cf441ed79 | -11.2779 | -43.4118 | 2024-10-04 14:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| fa1cc61c-f0da-30ba-bc49-94837981cc8b | -11.2963 | -46.8174 | 2024-10-04 14:06:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ccb3e1e4-7c23-392f-9ab6-7258fd93bbc9 | -11.404 | -47.2287 | 2024-10-04 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1ceba3e6-e3e8-3651-b606-2cae883ee56a | -11.3853 | -47.2088 | 2024-10-04 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| cbe8ef6d-be11-375e-90a0-6689bcdd2ef9 | -11.3849 | -47.2312 | 2024-10-04 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| daf06b53-bd22-3817-8ccf-afbe167e9bd4 | -11.275 | -46.9548 | 2024-10-04 14:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 16b2a919-20d8-3edb-bafe-ad73c91ce455 | -11.4622 | -50.9021 | 2024-10-04 14:06:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d9a533df-5558-36d6-81a7-a6827809c07d | -11.6804 | -47.8156 | 2024-10-04 14:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 10a9cd6f-7064-38c4-9a7f-5e1c05eb51de | -11.7228 | -49.9732 | 2024-10-04 14:06:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 789f0512-c9fe-3cd9-8315-937ef334d7b6 | -11.7045 | -45.2614 | 2024-10-04 14:06:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 08d8c5f7-2016-3240-9bd3-430bf3dff69d | -11.7038 | -49.9755 | 2024-10-04 14:06:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| f5c2b104-305c-3377-8457-0f84b86aceba | -11.7415 | -49.9925 | 2024-10-04 14:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 97640ae8-c747-3f85-abf4-6eca66f4af15 | -11.7412 | -50.0141 | 2024-10-04 14:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b4e3e426-a053-3947-8a8d-b2bb8511a06b | -11.9862 | -50.1787 | 2024-10-04 14:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ca94dc41-88f9-3a8b-a1eb-b9dcaabbe632 | -11.9296 | -50.1425 | 2024-10-04 14:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 4a021b6b-204d-364a-8da2-eab6dedede20 | -11.9487 | -50.1402 | 2024-10-04 14:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 31eb2592-d9a7-3ee1-a5f7-510dae01080c | -12.6826 | -54.6763 | 2024-10-04 14:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1022b685-f7e7-3fd7-b5f4-681930c65716 | -12.7623 | -50.5782 | 2024-10-04 14:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d96bded5-fd81-3acf-879b-1c451c222211 | -12.7815 | -50.5758 | 2024-10-04 14:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 9573e71e-579d-3c9c-8d33-07457cd268d7 | -12.7812 | -50.5973 | 2024-10-04 14:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 78196c9a-bbae-3f75-b449-5214d283efc1 | -13.199 | -45.492 | 2024-10-04 14:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e55b5e76-8db1-315a-9199-6f0d1057163b | -13.1787 | -48.6295 | 2024-10-04 14:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2a970382-ed96-31a2-8dcd-90cef56ef528 | -13.1447 | -46.3033 | 2024-10-04 14:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 9292ded1-9640-3933-ae22-8fb32edb8481 | -13.1443 | -46.3261 | 2024-10-04 14:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 2f5aa4ae-ec2a-3770-a3b9-1467590511cd | -13.1779 | -48.6737 | 2024-10-04 14:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 931ab0d7-dcd5-3027-81f5-c950a5c56c8a | -13.5058 | -48.6268 | 2024-10-04 14:06:22 | GOES-16 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 56779e86-5790-3bce-83b2-23efcc124fdc | -13.5255 | -48.6018 | 2024-10-04 14:06:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 097c840d-b198-35aa-8767-bc8790f4ed03 | -14.5876 | -40.7321 | 2024-10-04 14:06:27 | GOES-16 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 181.8 |
| 20982b0c-a536-3574-91e6-a76419f1efff | -14.7939 | -48.0275 | 2024-10-04 14:06:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e48134cc-4c00-3140-8374-e63e4f489ad1 | -14.8024 | -53.9014 | 2024-10-04 14:06:30 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1c8f70cc-4a65-36cf-87d1-328ec3a42798 | -15.1626 | -48.0786 | 2024-10-04 14:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c87c41fd-4e7e-3e4d-9b0e-53ff226e28eb | -15.6304 | -47.2063 | 2024-10-04 14:06:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7792d07d-dd75-3178-9785-c2da91dfd35b | -16.9296 | -47.1455 | 2024-10-04 14:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 70d9c628-4fac-32a9-971b-b6ff6164ee07 | -16.7862 | -57.3606 | 2024-10-04 14:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| adc880d8-2cc3-3f53-9462-16e0fc6009c5 | -16.7985 | -57.8284 | 2024-10-04 14:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| b9c2491c-3718-35f4-94ed-a81b7e9dfdee | -16.9495 | -47.1416 | 2024-10-04 14:06:41 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| defc6f5f-6026-31db-a048-d2f1687bcbf7 | -16.8626 | -57.4744 | 2024-10-04 14:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 6f40424e-70bc-305d-b909-a4791d4344df | -18.8613 | -43.5837 | 2024-10-04 14:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.1 |
| c9a62846-bc4d-3951-898b-f53c7cc5f4bc | -19.6122 | -46.2632 | 2024-10-04 14:06:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 66d2ff17-2977-33a8-bdee-a966282d983f | -5.8254 | -43.7034 | 2024-10-04 14:15:39 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 55c27a44-5133-35bb-a682-4391bf5fc58a | -5.8446 | -43.6555 | 2024-10-04 14:15:39 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fe2f8dbe-c9c9-3297-8ce0-0e2069b0845c | -5.898 | -41.9803 | 2024-10-04 14:15:39 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| a7b05e07-527d-32fc-a857-5c6eed17e316 | -5.9786 | -45.3847 | 2024-10-04 14:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 83245b4a-e1e6-348b-93ec-88637fb8e3a7 | -5.9788 | -45.3621 | 2024-10-04 14:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a1f3fb7c-8f49-3b11-9a95-4c0e702997ea | -6.0782 | -44.719 | 2024-10-04 14:15:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2b28f6a3-af67-3d30-bd18-ffcd1965e99d | -6.097 | -44.7175 | 2024-10-04 14:15:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3be2fcf1-b0dc-349b-8122-76385b2a7a62 | -6.1325 | -44.9199 | 2024-10-04 14:15:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 949ea08e-a1af-32ae-823e-dcca48278067 | -6.1468 | -47.4846 | 2024-10-04 14:15:41 | GOES-16 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| d7259909-a0ae-3adc-beeb-aff2bffb69f7 | -6.2249 | -45.0491 | 2024-10-04 14:15:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c3faf89b-f8b8-35ba-bae7-4403168c9e0e | -6.2436 | -45.0477 | 2024-10-04 14:15:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| bb222828-6f24-326d-a6ea-6f8c0d3a5ec8 | -6.5618 | -45.0677 | 2024-10-04 14:15:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 41fce741-909b-3b9c-a357-108ca928b149 | -6.9477 | -47.6887 | 2024-10-04 14:15:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| de6fa45b-b85c-35d8-bd72-cff2b2330740 | -6.9479 | -47.6668 | 2024-10-04 14:15:46 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0b469c48-e008-3d41-8c9d-c1753149376c | -6.9666 | -47.6653 | 2024-10-04 14:15:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 393a3984-110e-3235-a166-8d0e02a984e3 | -6.9701 | -59.0272 | 2024-10-04 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d188804a-7f95-3025-863f-3856ec19da5a | -6.9882 | -59.0844 | 2024-10-04 14:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e833b359-27ae-344b-b3b4-6656894ef936 | -8.1241 | -44.8101 | 2024-10-04 14:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9324b783-0ddb-3c5f-9bc6-c9dde40b7ff6 | -8.157 | -43.6977 | 2024-10-04 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 0932467d-12c8-3203-a896-91c47c5319bf | -8.1759 | -43.6957 | 2024-10-04 14:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9959ef15-c0af-3463-8fef-3286f7f3eba5 | -8.2862 | -45.409 | 2024-10-04 14:15:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| a0fc5b0e-473e-3551-8011-f39318d14b6c | -8.5212 | -44.7225 | 2024-10-04 14:15:54 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e5b0a41c-dffe-3dff-8a5d-044a4b8fc88a | -8.5675 | -44.0713 | 2024-10-04 14:15:54 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8abf92b6-4602-30a1-b224-85d77cdfd88d | -8.742 | -45.1563 | 2024-10-04 14:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 82523e23-b269-3015-afa1-2e7527f441c8 | -8.7423 | -45.1334 | 2024-10-04 14:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| af2c4094-820d-326e-8537-ad839ceab925 | -8.7609 | -45.1542 | 2024-10-04 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ddeeeba5-7ca6-3773-a233-e26726cf1547 | -8.8179 | -45.1252 | 2024-10-04 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5f9990d2-c6ed-36a7-b698-9335f4fdd4d7 | -8.8362 | -45.1688 | 2024-10-04 14:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| c9b27788-64bf-36de-8ef7-ce0e15f6cbaf | -8.9665 | -49.81 | 2024-10-04 14:15:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c29e10fc-a8cb-315e-aa0f-2b96405103a8 | -9.1158 | -51.5315 | 2024-10-04 14:15:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d4aee136-4c59-311e-996b-f345f4fceb91 | -9.5962 | -46.2618 | 2024-10-04 14:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1e520b78-40a8-36f3-9ac5-24b4a380e314 | -9.9826 | -42.0735 | 2024-10-04 14:16:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 806f90ea-45e9-3e75-a9cb-f1220727d474 | -10.2195 | -47.6839 | 2024-10-04 14:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| bacd5f82-4db8-3399-a555-e0fd4d54814a | -10.2574 | -47.6796 | 2024-10-04 14:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 133c7e04-8f9c-3513-a131-32648adb36f2 | -10.2188 | -47.7281 | 2024-10-04 14:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 672e37f1-3508-3aae-8279-51c3701648a6 | -10.2192 | -47.706 | 2024-10-04 14:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 8f538108-c319-3002-9850-9744e891be75 | -10.6981 | -46.1287 | 2024-10-04 14:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 47f01ba5-1427-3d5c-b94b-ac93cf1b8175 | -10.6985 | -46.106 | 2024-10-04 14:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 59420d60-7dda-39ad-ad49-789ac78f6052 | -10.6123 | -48.0355 | 2024-10-04 14:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| cb36c610-70b9-3f18-b2a7-cea71928de43 | -10.7359 | -46.1465 | 2024-10-04 14:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 16fa8a9a-6139-3cc7-a76d-47e073f91ee9 | -10.7445 | -45.6002 | 2024-10-04 14:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 0a18fc4c-f9e6-331a-83a5-23c70dcd3898 | -10.7549 | -46.1441 | 2024-10-04 14:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 2f43bdc1-8bc0-307f-b269-89650e30e193 | -10.8216 | -45.5444 | 2024-10-04 14:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 857de3db-a583-3712-bfc8-6c23bca9d502 | -10.7322 | -47.6239 | 2024-10-04 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ac3a00b0-6275-37d3-9e5c-98ab80edc6b7 | -10.7309 | -47.7126 | 2024-10-04 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 2816479c-d72e-308a-97f5-9fe66dcf2682 | -11.2779 | -43.4118 | 2024-10-04 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| a079903c-24af-37c5-a576-940c5cdf7360 | -11.2783 | -43.388 | 2024-10-04 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 3e76d2d0-6034-3d58-a28f-b904faee525a | -11.3853 | -47.2088 | 2024-10-04 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 66deabf9-2306-3884-99ef-402245cb6e58 | -11.3849 | -47.2312 | 2024-10-04 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| ff5ee617-10a4-30af-8576-bdd0e967b401 | -11.2963 | -46.8174 | 2024-10-04 14:16:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 723d2372-1b20-32f5-9c01-73ab9afccd86 | -11.2768 | -46.8424 | 2024-10-04 14:16:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2d580fa6-e7f1-3ca3-a472-7994f94d5c21 | -11.275 | -46.9548 | 2024-10-04 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 81ee125c-8ae4-37af-98b7-6f78a1f010b1 | -11.2114 | -51.2052 | 2024-10-04 14:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c8d92e91-70ce-3fe5-b395-3e164a0b9cfb | -11.4622 | -50.9021 | 2024-10-04 14:16:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 64594614-8783-30a3-8742-54696a8905f0 | -11.7228 | -49.9732 | 2024-10-04 14:16:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 07341e73-8666-31c1-939c-4039b883e476 | -11.7028 | -50.0402 | 2024-10-04 14:16:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 019b602d-07b8-3e4a-bf45-a8b0ab0b2a87 | -11.6804 | -47.8156 | 2024-10-04 14:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 296.6 |
| 8549dbb1-a574-3f31-9ded-82f7c6f17f1b | -11.7415 | -49.9925 | 2024-10-04 14:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2e6ae24a-f94e-3343-a164-922f699884a8 | -11.7412 | -50.0141 | 2024-10-04 14:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1578c801-27c0-3391-a067-543097a15a5a | -11.9862 | -50.1787 | 2024-10-04 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |


[Clique aqui para ver as próximas entradas](README196.md)
