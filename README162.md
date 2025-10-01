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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8c17301-dde9-331d-bbbf-582d37138435 | -16.0225 | -50.8771 | 2025-10-01 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 3ad58331-602e-3468-ba6d-8265ab057bfb | -11.1181 | -49.7629 | 2025-10-01 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 60178d7f-5454-38af-9a91-72fb84eb6f04 | -11.46 | -45.0202 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 83aecdef-4e22-32ba-a1a8-df57f6dea99d | -12.8014 | -50.5304 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 258.0 |
| bac4ac54-40de-3715-b660-d8a2d59c3257 | -11.3486 | -48.3211 | 2025-10-01 14:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 33525c4d-4159-34fd-a0a3-a0009dadfcfc | -9.4458 | -47.5923 | 2025-10-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 93af1c88-ad8a-3c81-83ba-39d3b1c6c779 | -12.122 | -43.4215 | 2025-10-01 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 67f13125-7174-3775-ac87-4d2db343b217 | -13.6703 | -48.07 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| eeebd04b-ff9e-33e2-9967-c5fa777c1e66 | -10.8433 | -45.3815 | 2025-10-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 763a330c-faf0-3f73-8168-07e022ce22a9 | -9.1434 | -47.6457 | 2025-10-01 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c1ed51b7-5d02-30f2-8314-daeb76096628 | -7.1815 | -41.6931 | 2025-10-01 14:20:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 00cac53a-bcaf-39ae-8df5-b59ae1318707 | -15.3596 | -47.0724 | 2025-10-01 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bc02c620-2745-3829-aeec-d7a5cf8c89e5 | -12.7002 | -48.5637 | 2025-10-01 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3bba89e8-a1e3-375f-ae58-508e2bcfc4b5 | -12.2816 | -44.1275 | 2025-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 21da068a-9ff8-3e42-b482-ede592746524 | -15.5379 | -45.2375 | 2025-10-01 14:20:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 9cfcc151-8ad5-318e-a9ff-40225ce44e0e | -9.9035 | -45.9553 | 2025-10-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 958136bb-0828-3c1c-9d4f-c8c3a182176b | -6.5437 | -45.001 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7ca9fc1b-2d16-3ff2-ad2f-4caa73a7d8a8 | -5.937 | -45.8601 | 2025-10-01 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| bffa1ca5-f30f-30fc-9021-724dfcfbc4fd | -6.0602 | -42.6789 | 2025-10-01 14:20:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 133d29fe-7356-3d61-8b55-9eeee4635567 | -8.2102 | -47.0305 | 2025-10-01 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ad715845-8554-3dda-bbaf-32a63da4a7bb | -6.3 | -45.0205 | 2025-10-01 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 83f5e3db-6cc0-3787-9d19-3d90959266b9 | -6.2875 | -42.4941 | 2025-10-01 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| a4b05bfc-f351-3052-a4cb-9ab68077a0f6 | -5.8258 | -45.7559 | 2025-10-01 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 40e269f7-ab17-34c3-899a-a46088791bb8 | -11.383 | -45.0543 | 2025-10-01 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 293.4 |
| 416fb5e1-163c-373d-83e5-8e4c147619fa | -6.214 | -44.2272 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 85da69ca-239e-3820-afcd-a74165c212ae | -12.839 | -50.5686 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| fd1ae6c1-9f84-3d7f-9bb8-eaac21f6db53 | -6.1166 | -42.6742 | 2025-10-01 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 2554aa92-f665-38cc-bfb9-2780bd13b535 | -12.2344 | -47.8086 | 2025-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9b222161-8ac8-39cf-b883-bb3d83234f02 | -8.5584 | -44.7644 | 2025-10-01 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 351f461a-962c-3e1e-8a58-da48a9b1f2c0 | -6.7168 | -44.5758 | 2025-10-01 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| bcad2d84-376c-3b1f-aa0e-6b0d6d9df5c9 | -11.6126 | -45.0443 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 4a453473-f956-39fa-82c7-6e6d9930741b | -5.8064 | -43.728 | 2025-10-01 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| eef95450-0c96-354f-a60b-a3a2cb4246e6 | -11.7984 | -47.6003 | 2025-10-01 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4fa624ec-e759-3753-ae90-76ddb7fd07d0 | -8.483 | -47.7983 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 5dba9236-9267-3627-8e86-2d51686b1623 | -11.3834 | -45.0312 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 94aea385-634e-3369-acd1-2e0b32ebddae | -15.9388 | -43.2979 | 2025-10-01 14:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 472.6 |
| 6c113665-e68b-3a02-b07f-0e24517b0575 | -8.9115 | -46.6276 | 2025-10-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 9f40a885-6d21-3331-b822-88ce89e43049 | -8.9182 | -47.5803 | 2025-10-01 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e2c2766d-4ed4-3a6c-b5be-e8d464e30efb | -8.6908 | -47.7126 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 74dfb3cb-5888-3024-82a1-7e55583faa37 | -12.282 | -44.1039 | 2025-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 287.0 |
| c741b286-ab8d-3a23-947e-261800149b09 | -7.4226 | -46.9904 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 170db4ab-f465-39e3-85bb-698c79f8a604 | -8.1917 | -47.0101 | 2025-10-01 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 52da53c2-d4c7-385c-a658-c087925efcb0 | -14.3519 | -45.9206 | 2025-10-01 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 163.0 |
| f37800c9-3f9f-3c69-bad1-953ed22df95b | -6.5415 | -45.2282 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 31d9ef4d-50c7-3e24-b87e-766fb94356b0 | -9.4007 | -54.6984 | 2025-10-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5020cc91-931e-35f0-9143-4d0fdd439749 | -13.7869 | -51.2404 | 2025-10-01 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 24dd8067-ff52-3514-b34c-2325ab585456 | -13.816 | -47.5107 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a4e32d4c-75ed-31ba-9c1b-9385be9a3e4a | -9.9391 | -43.6012 | 2025-10-01 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 269.2 |
| ba134ced-7fd7-3a99-88b2-ce46924fd208 | -6.544 | -44.9783 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9cf445c2-67f9-3f6f-9110-177fa585b9ad | -9.8848 | -45.9349 | 2025-10-01 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0e9a69a3-d68d-383f-ae97-2e814012c2bb | -5.3061 | -43.1131 | 2025-10-01 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5543486d-3671-3042-8807-fe696175fc69 | -10.0187 | -48.5183 | 2025-10-01 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 88bd75e2-89e3-3fab-8f85-94cf05f46b70 | -5.4964 | -42.7707 | 2025-10-01 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| f7c9ba59-4bdf-37fa-9fc6-a43fc3ba9eda | -8.672 | -47.7144 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 489cdf9a-f561-3d20-8b76-953b04c56ab4 | -10.6432 | -48.5145 | 2025-10-01 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6dcb0bea-4ab6-38fc-ad80-0fba66c93bbd | -8.5587 | -44.7414 | 2025-10-01 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 0b3fb7ff-8ccd-3057-914e-6b08ee4038a6 | -6.7811 | -45.6154 | 2025-10-01 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c476e51e-c988-32e8-a831-7e1983beeca5 | -13.3808 | -48.0908 | 2025-10-01 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 178.2 |
| f68e5352-6606-36d7-94d7-4c6ae4449b2a | -8.5079 | -47.2897 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 61b6cc91-4180-3987-bdfa-a6c775525d59 | -5.3276 | -42.7832 | 2025-10-01 14:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| f5e40bd9-62c6-3ee6-9afc-1bcdc4809eac | -11.9411 | -47.0675 | 2025-10-01 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 6a914cdc-dc16-3ca6-a375-b92ba41d7b63 | -5.4967 | -42.7471 | 2025-10-01 14:20:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 3f433f78-6673-3aef-a8dd-0d06699a82c3 | -11.4294 | -43.507 | 2025-10-01 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7a915ca0-bd63-36a2-ac7b-a961a5ef62cb | -9.8201 | -47.8386 | 2025-10-01 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5d31ea2e-e3a3-3d3c-8d38-f69c683d2323 | -7.8882 | -47.281 | 2025-10-01 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| febdf073-39b3-3ede-bb64-cf4893350e33 | -11.8242 | -44.9901 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4a238356-0f8c-3656-bae9-8d416d7af919 | -11.9081 | -47.8967 | 2025-10-01 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 8da7ee20-1fa9-33ab-b0d1-b0539b0fc3a7 | -12.2156 | -47.7889 | 2025-10-01 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a76b3a93-bb2d-3e34-8027-f416233766b7 | -11.9431 | -50.5058 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| bfd8cf84-9b7c-3a5f-89d7-43fd5967d600 | -8.5267 | -47.2879 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ac8d0c3f-5af8-3e44-a00f-2d248a91457a | -5.17 | -43.7276 | 2025-10-01 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7462b6df-386b-3052-a690-9513b6d2d178 | -7.4412 | -47.0109 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| dc3daed4-f9b0-3b04-bdb2-3dbb80c0cffe | -12.2623 | -44.1306 | 2025-10-01 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 352.6 |
| 173a93f2-8044-357d-8ff2-85560bbad46b | -8.5018 | -47.7965 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 407.4 |
| d4dae84e-40fe-380f-aad9-fac7cdeaa355 | -8.6722 | -47.6924 | 2025-10-01 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a53efae2-53f3-3a58-99a0-a47c3df07ced | -12.3672 | -50.1971 | 2025-10-01 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| b2758d9a-43bb-31b1-a5ef-98864ccb5a16 | -6.0978 | -42.6758 | 2025-10-01 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 9f7c5703-02ef-3c19-b145-133cfd611563 | -11.4796 | -44.9943 | 2025-10-01 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 1726ee80-d4ce-35e2-8bbf-5e124586e41a | -10.8999 | -44.2652 | 2025-10-01 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| ce644789-786a-3695-a3f8-a4a0b8ece7e7 | -8.8929 | -46.6072 | 2025-10-01 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 06997068-70f6-3191-a1f5-3c59f4c3cd70 | -16.0025 | -50.902 | 2025-10-01 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1c1c7ef9-73d8-39b5-b321-64aa7404d1c6 | -12.122 | -43.4215 | 2025-10-01 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 399.3 |
| 0670aa7d-ee56-3402-b468-08c08802d3ab | -8.2105 | -47.0084 | 2025-10-01 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8331c03d-efc7-3f1f-9e7b-02f67c4d362b | -8.5867 | -45.4914 | 2025-10-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 3d2ca395-46ea-3008-91a3-c5f4121fb36d | -12.3863 | -50.1947 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 080323dd-0fe1-3c71-9834-ce5c0ffabe81 | -6.2718 | -44.0612 | 2025-10-01 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f6b85c6e-713c-3053-90b5-dc2ae407f7fa | -14.9084 | -47.1965 | 2025-10-01 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 57e2b393-0996-3334-8a52-14735eed9b86 | -11.3486 | -48.3211 | 2025-10-01 14:30:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 220.7 |
| a904fa03-2c50-3db1-a41f-f3b6aa9ac9dd | -6.1166 | -42.6742 | 2025-10-01 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 59313270-38f4-39ad-ba67-5a473fa8cece | -3.9319 | -41.5917 | 2025-10-01 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 88071b63-6b00-32df-855c-9b754954d49c | -9.1246 | -47.6476 | 2025-10-01 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 440012a0-995d-3b13-b547-283ad298b84e | -10.6155 | -49.1274 | 2025-10-01 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| d54df19c-647a-3647-a515-74dda419e7f0 | -8.5079 | -47.2897 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f7b06280-06c4-3953-845c-6a7a159656e2 | -7.8165 | -46.9781 | 2025-10-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b5423b96-fc15-3bdf-b058-56de4b9ff5be | -15.9388 | -43.2979 | 2025-10-01 14:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 695.8 |
| 5999c595-cbab-388a-813c-8a5ae2b0b1ab | -7.4761 | -47.2508 | 2025-10-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| fcb3ba2d-cf6f-3696-88dd-94ad8e4e4803 | -9.4115 | -47.3308 | 2025-10-01 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ca9c44b0-a4df-381e-95c3-e0f982651385 | -12.282 | -44.1039 | 2025-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 253.7 |
| d840fd5d-93c4-3ea3-92ed-cb3484d029fa | -13.3274 | -47.8536 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| e48ac98e-8d9b-3086-9e52-8e5a39c5bda6 | -7.2996 | -42.8722 | 2025-10-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |


[Clique aqui para ver as próximas entradas](README163.md)
