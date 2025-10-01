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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 547278e0-e05d-304b-918f-01e925aae951 | -3.68815 | -49.04592 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4683688c-da00-3146-bf2e-1bc3e98a1876 | -6.29273 | -43.9133 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f89c46-afe1-3def-b117-584fe2a09b5b | -3.25369 | -50.11486 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 124c20ad-6427-38fa-a9b6-1e5db8909ab1 | -7.39011 | -44.60822 | 2025-10-01 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dda9e786-d79e-3f1f-99b1-430811eb28c3 | -6.68006 | -42.80262 | 2025-10-01 04:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7f182ee-8e1e-3955-8587-e6b0885b9d62 | -8.58815 | -44.73498 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68a8cc42-d8df-3eaa-8ee0-f70b2d152d44 | -7.54327 | -46.11385 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73940082-3760-391c-9770-0c574e1442df | -7.62653 | -46.68054 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba1790b5-de48-351d-b878-5f1538407b32 | -8.58967 | -44.72734 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dbf152f-92db-3e38-a8c8-8bbd6544be79 | -7.8734 | -47.27199 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89254b52-78c6-30cd-9c0a-d574ee6b6ba5 | -3.46772 | -50.08788 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5bab071-b6eb-38f9-bf21-9a34ea9f8ad0 | -7.02089 | -44.45563 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60cbad2f-a1c2-37c1-83ae-2fbd38793646 | -7.02304 | -44.47352 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd53164-003a-305f-804c-e1a09cb661f9 | -8.55367 | -44.71795 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4a9e4d7-c958-31b8-bb49-de7f8c6e68d1 | -3.68476 | -49.0454 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1032f0e8-ef6c-3114-9512-41d4721b842e | -2.69628 | -54.76745 | 2025-10-01 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ec2c5492-a1fa-3dd9-a812-28499bdc7c2a | -5.76787 | -43.30193 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64e01b2f-625f-3386-82e5-99949c0fc22a | -6.11776 | -43.22158 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34008ca3-2051-3e29-a666-e68eca6f0c13 | -5.91775 | -43.70904 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e184f36-aed2-3068-a649-49d5cbef2846 | -5.41413 | -41.32632 | 2025-10-01 04:49:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1e67518-b595-3a80-8fa8-f336da5213db | -8.15868 | -46.25771 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9899692b-f719-3fb4-9392-dc370a8797a9 | -6.0907 | -42.47874 | 2025-10-01 04:49:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16070a65-bc0a-37ed-ac53-e68d7ba1ddc6 | -5.50434 | -42.73177 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e3e05328-15f4-339e-9a13-5b9e0121ab9d | -3.85849 | -40.43311 | 2025-10-01 04:49:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84c3f57e-2c80-39db-a996-389f1dfcefa6 | -7.83204 | -47.07103 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d5ceeb5-204f-3d8f-b2b7-5033b3a3ff0b | -4.58438 | -45.61409 | 2025-10-01 04:49:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10bb89f1-8d38-3046-8381-7572c069ed41 | -4.29452 | -48.27262 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2948ce36-6fdd-3479-9104-377bf83671cf | -6.875 | -44.52885 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f058581-6e37-3789-b579-bb62330f7fc2 | -8.75099 | -45.92403 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8affc55b-cb40-326c-bfa7-fe3d77a7ddc2 | -4.74353 | -43.60867 | 2025-10-01 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82f79626-5d7a-34ab-8b11-f15cb3e6ad8a | -7.39807 | -46.98137 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a55746c9-8a66-34cb-aca1-44992c9e5c0e | -8.92301 | -47.59001 | 2025-10-01 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6909d1e5-0257-334e-8c9e-f238475fae21 | -5.89792 | -43.31128 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c2e6fe6-d0a3-3cb3-b351-14a9fce869ce | -3.59625 | -48.98731 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 768fb13c-7fc3-3281-98ac-be752b5b393e | -7.63212 | -45.45481 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cde09b1f-904b-3956-aa41-1bf1fab199fe | -6.98697 | -44.39661 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c533be1-45e2-316d-8560-c06fb5f5eecb | -6.28053 | -43.65594 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48d2a496-fe90-3ce0-b9a1-4248b8ea582d | -3.46275 | -50.09774 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d11108b1-24aa-3591-9fc3-73fe4a98ef4c | -8.92819 | -47.58136 | 2025-10-01 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 484845bb-87f2-3cd5-836f-8144ed782b2b | -5.63516 | -43.91629 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 47c4dec7-8adc-3a3e-a5c5-3aec3dbfa47b | -5.89935 | -43.93207 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75b27d8b-0435-32f0-a253-727eb6b4d40e | -5.21844 | -44.83869 | 2025-10-01 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81248c43-59d3-3d4d-bf3c-bec2e942b613 | -4.03699 | -54.13744 | 2025-10-01 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709ab405-b319-307e-ad4e-e6b53bfe331f | -6.20894 | -44.23603 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6eacb1b-24d9-3aee-9cea-c625be5eea15 | -2.59397 | -48.11682 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5acc7ad1-d206-3caa-be19-17c63557284d | -8.51911 | -44.66417 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 914cf3c5-2b4a-35f2-a59f-9a455d172b24 | -4.68749 | -50.4816 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 914c371d-da17-3c9c-bcd4-c77e57eb3e5e | -5.95002 | -45.86628 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f2abb76-693a-3162-81d9-b8c27d3aa6c3 | -8.73462 | -45.91902 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cebf238a-562c-3739-9e78-22a71cd66276 | -7.02729 | -46.97817 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b843642-ebfc-3f40-b70f-bfd868a3c73e | -6.46331 | -43.93492 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a598ca7e-1bfd-3a32-9bc1-7755e3da6997 | -3.09064 | -47.01521 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d35897f5-47b2-3f42-8100-ac2e67fc6080 | -5.79209 | -43.29039 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73266f99-37f8-30b5-8eca-ca8444173529 | -8.23554 | -45.51017 | 2025-10-01 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1672175a-5b12-328c-a615-28e4549dbfdc | -6.11971 | -43.2262 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 040809b4-a491-3a2f-ae89-2d2c206de0fe | -7.8218 | -47.05965 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9196d6c1-c41e-353d-a256-e3f9b65f6ef2 | -8.5818 | -44.7497 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9109c2ee-ae4e-3130-b7d7-ba16ccd1318b | -6.25605 | -43.65723 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ccb5cf69-523d-3f87-b3f7-d3b5a8e16acb | -7.39978 | -44.60529 | 2025-10-01 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01c7ed7c-3113-3cbc-8b1a-52642f4db4d8 | -5.73081 | -42.82061 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 1dff8bc1-1ddd-37fe-98ff-803acb8d26b3 | -3.10107 | -47.01502 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db00f28-3e3b-3bb8-b8ee-425fae4490e1 | -4.40238 | -50.85196 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a7c44c57-d53b-3ccb-a375-77b967eab77c | -7.02389 | -44.46288 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 678227b1-521a-372b-8c94-af71f293febd | -3.80971 | -52.33782 | 2025-10-01 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 875d4139-dcef-3aae-a221-b0b418b36a8c | -5.94536 | -43.31557 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c45bbf3d-c52e-3fdf-993f-aeff81ed336a | -2.82203 | -54.029 | 2025-10-01 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fc79d30-5369-3594-9c67-220ee57d17c8 | -3.46106 | -50.08684 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 954629ba-0e10-3a65-b2bb-945fa19fa85d | -7.05204 | -46.41415 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3887c9f-9687-36c2-b3ed-feb8c01a1457 | -5.76592 | -42.86086 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 33d5df69-f886-3225-9e45-1cb193928684 | -5.76501 | -42.86549 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f3acedf5-9e34-3aff-b499-fb4d84959e68 | -3.04977 | -51.10215 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ca64838-d8c9-3c44-8643-5254f319bdce | -3.85913 | -40.43536 | 2025-10-01 04:49:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30028318-daca-3e29-8a85-0d174ad072dc | -5.91377 | -43.70328 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc4c0dde-eb3d-361f-9312-d5dc8a398570 | -7.02029 | -44.45995 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14e3110a-9d81-385f-b3d3-2b355328adf0 | -5.70784 | -42.69528 | 2025-10-01 04:49:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 47361d0f-532b-37ec-a679-741baa1114f1 | -8.22047 | -45.79355 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ef64734-f089-33ef-98b5-d7a8c6589ded | -7.20167 | -46.87916 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef2333ac-1a49-3d1d-8037-bd15d4169da5 | -3.67174 | -49.01759 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c6ac57-2d62-34c2-87e8-3ea10c6b0ef3 | -3.93932 | -41.59117 | 2025-10-01 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f001b664-7c14-3f6b-b6aa-5a26b4230e47 | -3.50655 | -53.45604 | 2025-10-01 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bb2889d-b521-36c6-91b1-49d818a617cb | -6.63537 | -51.18995 | 2025-10-01 04:49:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f874c7f8-2fe8-32df-a46f-e55de6bfff87 | -4.25569 | -48.5568 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f4152be-c75b-3455-a149-7d75880bbbf1 | -8.54525 | -44.64455 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ed1f91d-2822-3b97-973e-e7c98210d7a7 | -5.53369 | -43.87504 | 2025-10-01 04:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 09750377-538c-371e-a527-db10ec9ce4b9 | -4.80882 | -50.7387 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76bf1c54-5cfd-35c5-887d-cc4218618e04 | -5.85587 | -45.77872 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b7cff9a7-e386-3920-bd5e-ef90e3b23589 | -7.83715 | -47.25233 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d61dc214-f748-334c-a809-6d3dd383aff8 | -5.85841 | -47.63306 | 2025-10-01 04:49:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 019d7e29-69a1-3180-a13d-83835d8bacbd | -5.91848 | -43.70405 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 093285f6-51ee-3d1f-abb1-b8b8be250b8e | -6.1012 | -42.67823 | 2025-10-01 04:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7e70be5-27c5-3630-a067-fa715c1f87d6 | -7.56308 | -46.78384 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc411ee0-15d7-3e0f-9802-93e3ed52d79f | -3.45231 | -53.8357 | 2025-10-01 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51e686f0-0de8-3462-a345-bab2f30c7449 | -6.11482 | -43.22547 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2377668-a0c6-3ed1-9a83-93ae1a0d0bbd | -6.80751 | -44.47581 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d544cf50-6da8-349d-9314-8da31afc68aa | -7.82798 | -47.06863 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fbdaae-0fb2-3ba4-9b5b-533a6c6e9229 | -6.1107 | -45.89749 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ca55d85-ff6f-3ef9-ad3f-bd61ecb0ad96 | -6.32089 | -47.22438 | 2025-10-01 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 145be199-fc33-3ce2-a715-993b135d35a2 | -7.47626 | -46.46812 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c7d1a4-b252-3656-8b4c-d3c9cfbf7846 | -5.98049 | -43.61195 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69aae80c-767c-3f60-8d21-14ccec1e08c2 | -5.76957 | -43.62313 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README84.md)
