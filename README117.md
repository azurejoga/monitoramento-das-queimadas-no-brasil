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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c41ef7d-7b88-3672-b121-67f7f1b752fb | -12.2344 | -47.8086 | 2025-09-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 988ad8bf-2032-38bd-9976-2441c7651263 | -7.0181 | -44.4807 | 2025-09-30 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 22d01b7e-84f3-3f16-b504-976e0b58adff | -5.8612 | -43.8858 | 2025-09-30 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9e66d264-6f1d-3198-8694-391ad97e9972 | -7.8538 | -46.9969 | 2025-09-30 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 6b4e7016-2aab-3445-a039-33f6b128301e | -15.9273 | -46.2101 | 2025-09-30 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 273ac6bc-fadc-3510-9bc8-9a315733bf19 | -16.7571 | -51.37 | 2025-09-30 13:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 0d68ecb3-77de-31fe-a639-56c5a19a8f8c | -13.162 | -47.4309 | 2025-09-30 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ecf34112-e63c-3322-b8f1-3b0aee7f65e7 | -9.1246 | -47.6476 | 2025-09-30 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8546671f-ede1-351f-a79e-40dfa5c0518a | -11.7537 | -46.8461 | 2025-09-30 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| cce9fc4e-929f-3dad-bf09-819b87f92573 | -15.2746 | -49.263 | 2025-09-30 13:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 153.9 |
| abdd3d76-68cb-3962-b835-9929a286357e | -7.281 | -42.8505 | 2025-09-30 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a1d1a08b-e872-3f0b-9f19-c412e88b37bc | -8.1428 | -46.3693 | 2025-09-30 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 58ec4be6-f485-33ad-9689-bf287356f3fe | -10.823 | -46.6538 | 2025-09-30 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 8ae3a9e6-68f3-3b7b-9f28-5c17c52652ae | -10.0528 | -50.2192 | 2025-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 444c0955-4830-3e31-9975-bc2e4be22891 | -7.4958 | -45.4402 | 2025-09-30 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 91c0dc58-dc12-387e-a7a0-e825b5aebdbd | -6.5042 | -45.2085 | 2025-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| b7761b16-dc05-3a67-a8c0-112a9c39e83d | -5.7601 | -42.6561 | 2025-09-30 13:50:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| f1497765-77d2-328a-9197-1a96702af416 | -5.9189 | -43.7193 | 2025-09-30 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 056985dd-2d07-37a1-b9cc-ba1aad150ff1 | -5.4562 | -43.0788 | 2025-09-30 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| a50b7232-423a-3f88-a4b9-ab66d9a5ce2f | -17.9016 | -57.577 | 2025-09-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 73f57834-2219-3f39-9d10-41d978f45d46 | -12.7018 | -45.2947 | 2025-09-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| bb078774-03be-3e70-be3c-7d85c671515d | -12.7022 | -45.2715 | 2025-09-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 22b70cb2-05fd-31f4-b54d-a69eeabf7b75 | -10.0342 | -50.1997 | 2025-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f25e8515-1f98-3aef-bfb9-2c63da1e21ae | -11.1944 | -47.2334 | 2025-09-30 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 99a6e87f-736d-3538-bc26-024e19e5308f | -15.1688 | -52.8241 | 2025-09-30 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f9144a19-903b-3891-8898-a1eb61d1db9e | -15.7917 | -43.6672 | 2025-09-30 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 217.9 |
| b9aa9a0b-084d-3797-8053-1a3eb88b7b92 | -6.504 | -45.2312 | 2025-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| eec8d95a-8a34-337c-bc8c-14c6ad6d21b4 | -5.826 | -45.7334 | 2025-09-30 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| f92d8a0a-1423-3d3f-9005-e89ac958dbb3 | -15.7719 | -43.6714 | 2025-09-30 13:50:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 411.7 |
| ab6a59ab-a125-3a8e-9c43-f911ede09124 | -9.4007 | -54.6984 | 2025-09-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 28ce99d1-274e-39d6-9086-07783b527e46 | -14.7166 | -45.2525 | 2025-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 376.2 |
| e7d88a6d-a6aa-31e5-8fa2-c28add0d71fa | -14.7171 | -45.2291 | 2025-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 2499e96e-fa74-3d2f-ac2e-8538a0a6e420 | -19.6026 | -43.8334 | 2025-09-30 13:50:00 | GOES-19 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 6ec0959b-0de3-370f-896d-74ad852367ed | -7.9194 | -44.6016 | 2025-09-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 5a188349-d73c-335e-ac52-d80d812e740a | -5.8615 | -45.9551 | 2025-09-30 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b707e530-0311-3026-b3bd-0b2475f1ec70 | -18.2171 | -53.3392 | 2025-09-30 13:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c56db82f-a1ab-3b4e-86f1-9461f490b6b4 | -14.3847 | -47.1486 | 2025-09-30 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 219.5 |
| a0e79134-97eb-3057-b3d4-8e117a5ed6de | -14.5853 | -45.0197 | 2025-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| a1902a61-7034-31fe-9299-2074a11f124d | -5.7599 | -42.6797 | 2025-09-30 13:50:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 4b72ca41-caf0-3711-8806-45f6271d82e8 | -11.071 | -47.8262 | 2025-09-30 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 0f578c78-8bae-3ef0-87cc-28408bfebdfc | -12.8774 | -45.1742 | 2025-09-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 383708cd-da5c-39a5-9852-cf13eb80f51e | -6.6981 | -42.7882 | 2025-09-30 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 286ed049-8ee5-35ff-b795-a49d3f5aa6f9 | -7.8188 | -46.7783 | 2025-09-30 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 859f0fb9-ddd7-3c76-ba4a-9686172271f3 | -8.9287 | -49.8348 | 2025-09-30 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| cfb9c589-fc64-3afe-a863-e07c1180e1b4 | -18.4862 | -44.0191 | 2025-09-30 13:50:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 31c86721-0c66-353e-ba89-f68ac719005e | -7.2996 | -42.8722 | 2025-09-30 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| f9bf68f0-0dc9-3b34-b7b8-710a782bd5a1 | -7.9191 | -44.6245 | 2025-09-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 622ff1b1-b627-3a90-8b73-1acf4d577af4 | -11.1948 | -47.211 | 2025-09-30 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1ee070a5-9276-3b01-9c6c-ee26f81479c0 | -6.098 | -42.6521 | 2025-09-30 13:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 44df327e-52a3-35e8-859f-7151c2bc707a | -17.9214 | -57.5746 | 2025-09-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.9 |
| e81cb189-979b-3e78-a53b-1ee9d0c562be | -12.2153 | -47.8112 | 2025-09-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8468ecd9-bfce-3bb3-bde7-61c7f269cf5e | -11.1548 | -54.1054 | 2025-09-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 6a20bc9b-7bdf-330f-965c-5cc2e60a5f42 | -11.1941 | -47.2557 | 2025-09-30 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0cf968c4-9b87-3ee3-a2fc-b6b7a0e8fa36 | -7.8696 | -47.2606 | 2025-09-30 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 0bb30193-61a0-3e52-9576-d2f1d9105cc3 | -10.1855 | -44.8709 | 2025-09-30 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 53b839f8-ec85-3b76-9d61-6c542fc3e787 | -6.4131 | -43.0724 | 2025-09-30 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 28f49067-909c-3f0a-b2fc-c584c87e195d | -7.115 | -47.785 | 2025-09-30 13:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 416be46f-d58c-3145-9cef-281168167392 | -10.0717 | -50.2173 | 2025-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d773af14-f438-3b24-99bd-0382e548dbef | -11.1546 | -54.126 | 2025-09-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| b85c12b1-57c2-3e05-8a8d-dc231dfc57d3 | -5.7223 | -42.6826 | 2025-09-30 13:50:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 229.1 |
| a279aed6-d388-3e5d-9032-0192c707255c | -9.9585 | -43.5752 | 2025-09-30 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2ca4c15c-05ac-361e-a5e7-11073632d2a8 | -11.4596 | -45.0433 | 2025-09-30 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 89be63bd-cf77-378b-b84e-d3234ff779e7 | -8.1616 | -46.3675 | 2025-09-30 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ac053e15-a383-36a1-b8fb-61be03947990 | -6.5227 | -45.2297 | 2025-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 289.6 |
| 7aee4526-5cf8-320b-9a8a-6765cb620690 | -9.4206 | -54.5753 | 2025-09-30 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 307.7 |
| 003e6987-f8fb-31a2-912c-9041f0ede456 | -5.7413 | -42.6576 | 2025-09-30 13:50:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 727d0b3e-412a-3b41-9bbc-cd624d12f08e | -13.7502 | -47.924 | 2025-09-30 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 728d69be-41f4-3fe5-828c-724aec96d7a7 | -6.2759 | -43.6442 | 2025-09-30 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 37f4244b-ba15-37bd-85c3-14d1255a6942 | -14.4041 | -47.1454 | 2025-09-30 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| ce868153-050b-38dc-89d9-52d31eb13085 | -9.939 | -55.1632 | 2025-09-30 13:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ea056ebf-a938-37ab-9700-62cd0ef8a3f1 | -11.1753 | -47.2358 | 2025-09-30 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| bacca7f1-7832-38e8-989c-8980e7334216 | -11.1735 | -54.1242 | 2025-09-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 08d367a4-af19-3d96-a72f-f1b1fd399e66 | -14.6603 | -46.9663 | 2025-09-30 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 493ddc62-651d-37c5-923c-b9628d69abba | -14.5517 | -48.4907 | 2025-09-30 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 257a71d9-72f7-38b4-ae2b-840760d93684 | -11.6835 | -44.2908 | 2025-09-30 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 50c386c7-b683-3b80-8697-6f7c368bdbf2 | -12.8429 | -47.0063 | 2025-09-30 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 18ad4fba-a224-385b-84c4-b6f0358b6b63 | -7.4129 | -44.4673 | 2025-09-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f7491089-8b6c-3906-bfd8-df9eef09ebe4 | -7.8378 | -46.7544 | 2025-09-30 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d61db2b5-44de-37c4-9a7e-8b6d11407a46 | -9.4005 | -54.7186 | 2025-09-30 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c577b1f8-7316-32d7-a750-2d71e4c98101 | -5.7411 | -42.6812 | 2025-09-30 13:50:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 266.3 |
| d5060b28-baa7-3cbb-b929-0be9b7e76a35 | -10.1042 | -47.8072 | 2025-09-30 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d5099b06-b188-38d9-8fc8-949f3be79959 | -13.8264 | -47.9794 | 2025-09-30 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8d0b6e40-6c83-35ec-83a8-29339b2061d5 | -12.952 | -48.4185 | 2025-09-30 13:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 043e4954-7b59-3709-beac-32c6628bd704 | -8.874 | -46.6092 | 2025-09-30 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5cab4691-6789-3b2c-987e-9798f1109d73 | -5.9004 | -43.6976 | 2025-09-30 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ef27bd87-00d2-354e-b22b-9958353875eb | -9.7681 | -46.1519 | 2025-09-30 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 14a56772-f18f-3f0d-bc46-3f5e9b62a789 | -12.1265 | -44.199 | 2025-09-30 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 115be54c-61e7-3dae-9a47-7f85fd322b05 | -7.4131 | -44.4443 | 2025-09-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 54c25eab-227f-3ba7-a69c-dce5185dd7cf | -10.6423 | -48.5802 | 2025-09-30 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 77eeb177-d98e-374f-9e67-46c991a64e19 | -19.6033 | -43.8086 | 2025-09-30 13:50:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 5e7a197c-ef37-312e-beef-e245232ca0fd | -17.921 | -57.5952 | 2025-09-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| db4babe0-e26f-350c-a690-b1e1bafc361c | -7.8375 | -46.7766 | 2025-09-30 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 00ecb4c0-5d8e-357d-8b5d-e310099a2fdb | -10.1045 | -47.7851 | 2025-09-30 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d0fd721b-6e72-365c-b073-629c529a6fed | -8.9182 | -46.1115 | 2025-09-30 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d83603fd-14fe-3c93-8408-fdf6e8422aef | -7.2999 | -42.8486 | 2025-09-30 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 63670944-75ab-385d-a8bc-d3aeb3368778 | -10.0531 | -50.1978 | 2025-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 70d9cc97-4f8a-3df6-9142-0bb89161daa5 | -17.9408 | -57.5928 | 2025-09-30 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 50508367-95fe-369b-b38b-ae7cef239a58 | -7.5146 | -45.4385 | 2025-09-30 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ec2c4d6b-20f2-3c3a-b37b-27dc040c55ac | -10.6419 | -48.6021 | 2025-09-30 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 883469c0-3774-3079-8c04-8c480f072991 | -5.8616 | -45.9327 | 2025-09-30 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |


[Clique aqui para ver as próximas entradas](README118.md)
