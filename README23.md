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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e1621b4-ef14-3a32-8c3c-1bc391a26f43 | -10.2659 | -45.8206 | 2026-08-10 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 62737034-9ef7-3401-a783-91deeb4bb880 | -8.3117 | -46.3976 | 2026-08-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 46dfca59-642e-3653-8506-8c2579a21b53 | -8.5507 | -45.3589 | 2026-08-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 17f4cfab-6b89-3fa4-b772-5e54772244d3 | -10.2468 | -45.823 | 2026-08-10 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| bd81378a-9236-3b57-9977-fc7ff34385b0 | -7.6025 | -42.7705 | 2026-08-10 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 2807e3b2-3e51-3ca6-bb0c-73652e581c61 | -7.6214 | -42.7685 | 2026-08-10 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 189.5 |
| 2ba028ba-b59d-3ddf-aa5e-e1e8393ff65a | -10.8407 | -46.7414 | 2026-08-10 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| c1bbb026-5b00-3396-b2fb-80643dc8fdff | -10.2655 | -45.8434 | 2026-08-10 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| cc04a293-e7be-3363-ada1-ea4e78c59170 | -7.6214 | -42.7685 | 2026-08-10 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 131.3 |
| 9849b8f3-926b-3573-a0b7-ad3b36fe0831 | -8.3117 | -46.3976 | 2026-08-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6abc1d66-46f8-37b4-8abd-1fe6e1125362 | -11.4671 | -50.5604 | 2026-08-10 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a153a217-6ab0-3589-9180-35e0b7cc758b | -8.5507 | -45.3589 | 2026-08-10 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0fd15103-dc74-3a21-a8bf-725e11248b7a | -14.2872 | -45.3069 | 2026-08-10 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 691d6a7a-20f7-3a46-8a07-6ae6bf531e58 | -7.6025 | -42.7705 | 2026-08-10 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 0ae49107-0ef6-32ae-9e11-1c4cc390beed | -6.9468 | -51.9209 | 2026-08-10 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 277d3956-5643-33ef-bc09-e8ca9fb2f972 | -10.2455 | -45.9139 | 2026-08-10 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 0b435fc3-95f2-3a87-a2de-4cdd05bee5d1 | -10.2655 | -45.8434 | 2026-08-10 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b0b69fa2-284b-34d1-890f-a17ba82c6bab | -8.5504 | -45.3817 | 2026-08-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 79497b1b-3838-31a9-8cd0-d6df4bae1312 | -7.6025 | -42.7705 | 2026-08-10 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 24fbdc3e-a44c-319e-979c-5723ed6c211f | -11.4671 | -50.5604 | 2026-08-10 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e51249bf-2025-31df-8d4e-0660d68704ee | -10.2659 | -45.8206 | 2026-08-10 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 811f5f33-a228-3c47-a683-49fd53b59de1 | -14.2872 | -45.3069 | 2026-08-10 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 864f3d2c-8228-3309-af88-ee60b24d9a4f | -8.3117 | -46.3976 | 2026-08-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 45c1fa67-9c8b-3ba2-87fd-3ff2cf20fccb | -7.6214 | -42.7685 | 2026-08-10 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 176.9 |
| 723c206b-981b-3d18-acce-93205d295c6f | -8.5507 | -45.3589 | 2026-08-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| be169ff3-1e8a-3b0c-9c0d-9d10e703085b | -14.2677 | -45.3103 | 2026-08-10 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| fd1b8db9-2791-3330-b558-f7d061521c97 | -10.2468 | -45.823 | 2026-08-10 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 13e549fa-6309-31b7-a271-3ca4c7f5316f | -10.2455 | -45.9139 | 2026-08-10 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 74c8e70d-21ba-394e-b20a-e502bdab2edb | -10.2655 | -45.8434 | 2026-08-10 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.4 |
| e2bdd797-9a41-31b1-99da-619803989bae | -7.6216 | -42.7449 | 2026-08-10 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| a860a30b-9303-3bf0-9afc-9d52faf77acf | -7.6214 | -42.7685 | 2026-08-10 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 190.3 |
| 2050b583-2dc4-394d-8132-dfafaac68358 | -10.2659 | -45.8206 | 2026-08-10 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 4cff4e61-64f3-3b8e-b132-d583c1427465 | -7.6025 | -42.7705 | 2026-08-10 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 66f08760-a9a7-330a-bdd2-ba84caa9e85f | -11.4671 | -50.5604 | 2026-08-10 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| c113d80c-f88a-382b-9b17-b85a4102eb15 | -6.1476 | -57.7215 | 2026-08-10 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ef6a1d15-2782-39f4-88b8-581bfff7fb34 | -14.2677 | -45.3103 | 2026-08-10 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3f740d9c-db2b-36ef-9098-5f221b0a04fe | -14.2872 | -45.3069 | 2026-08-10 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 31c91b42-61ac-325f-b809-b7a921c8edb9 | -7.0079 | -42.0225 | 2026-08-10 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| fdd5ccd0-e2da-347c-b350-d0989ec9167f | -8.3682 | -46.3921 | 2026-08-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 97caa81e-eb23-3cc7-b6ae-a8fc2e6c6c75 | -6.1477 | -57.702 | 2026-08-10 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8a53e79c-edf2-3664-81a8-1d06128f1a6f | -14.2677 | -45.3103 | 2026-08-10 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9c4d444a-dcd9-32dd-84c2-3157b1d77665 | -10.2455 | -45.9139 | 2026-08-10 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 2d4836e3-eea5-3ca2-85e3-a38f94e40fbf | -6.1476 | -57.7215 | 2026-08-10 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 1ee0dfa1-01ed-3e8a-877a-282b8fbff475 | -7.6025 | -42.7705 | 2026-08-10 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| 9fbba504-2aa3-3769-86d3-fdc12e00732f | -13.6287 | -46.226 | 2026-08-10 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c8075db3-b153-32ab-b314-ff5b330b784e | -10.2659 | -45.8206 | 2026-08-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 15461944-07f3-390d-9172-fa14c9d4a097 | -7.6216 | -42.7449 | 2026-08-10 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 56ed5c90-3db8-3eb3-be6b-b0ba256c06fe | -10.2655 | -45.8434 | 2026-08-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 206.7 |
| c87b4cc4-f39d-3302-a014-9d568ba6006b | -8.3117 | -46.3976 | 2026-08-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| e700b34e-c8d6-3569-b5d3-f80672ded00e | -7.3891 | -59.9924 | 2026-08-10 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 212ab0f8-7f36-3585-a572-447b9ec05781 | -15.3852 | -53.7652 | 2026-08-10 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5f0778a4-6890-3378-bdd9-da9b9bb6fc0d | -14.2872 | -45.3069 | 2026-08-10 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| aa5e1631-a508-30b2-9b59-1d67ee539220 | -10.2468 | -45.823 | 2026-08-10 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6b91bff3-231d-3a79-ad4d-5c17371d0f55 | -7.6214 | -42.7685 | 2026-08-10 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| 29f569b7-f378-3dbc-95b1-a7c9087726c6 | -11.4671 | -50.5604 | 2026-08-10 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b9c29726-97f0-35f2-8768-475bfad0599c | -8.3117 | -46.3976 | 2026-08-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2353fada-ded2-36f7-a7c4-0427b0920b99 | -14.2872 | -45.3069 | 2026-08-10 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d0f852c6-c66c-3b3a-821a-412ad64527d2 | -10.2659 | -45.8206 | 2026-08-10 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| af03d387-2f1f-3da6-b5d1-636a8c5bde00 | -15.039 | -46.5581 | 2026-08-10 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9dcfeb9b-47cf-36f9-a1d9-1fac4e726dcd | -13.6481 | -46.2229 | 2026-08-10 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| feb1ebca-8c9f-3aa4-8612-8054c80239c3 | -7.6025 | -42.7705 | 2026-08-10 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| c4747da0-57ba-3d5b-817f-17709daa9ba7 | -10.2468 | -45.823 | 2026-08-10 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 88e345e4-f015-34c7-97e3-dd17e9b43ccd | -7.6216 | -42.7449 | 2026-08-10 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 3f41dbb8-fb02-37d2-8b87-59e41b655cd5 | -7.6214 | -42.7685 | 2026-08-10 14:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 252.7 |
| 89813da2-5317-38b5-92ad-359c19fbea93 | -7.3891 | -59.9924 | 2026-08-10 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 123526bd-316c-3e83-b058-d2eda7ab4835 | -7.5488 | -55.5629 | 2026-08-10 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f0168a6e-b906-38a2-ac3b-8999a28f7742 | -6.1476 | -57.7215 | 2026-08-10 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| f20870b6-bfcb-34c8-9698-f3415ba1d6e3 | -6.1477 | -57.702 | 2026-08-10 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| faf88e38-a9f1-3604-8a1f-4bb1f239a3dd | -9.4101 | -47.4415 | 2026-08-10 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7f092550-d135-3225-a793-1750a76eb552 | -13.6287 | -46.226 | 2026-08-10 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 281.3 |
| a151cb0b-4dd6-3fa4-b781-064e4d31833e | -11.4671 | -50.5604 | 2026-08-10 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0e6e7295-6990-3d8d-a417-90f62ef53526 | -15.0937 | -52.6858 | 2026-08-10 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| feafff7e-6e1f-3a97-8e5b-eeb1765b5d3f | -14.2677 | -45.3103 | 2026-08-10 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 30da6655-167f-3694-b422-a946a5a02ce0 | -15.0743 | -52.6884 | 2026-08-10 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 097d5d60-e538-3802-b3fd-b61eb8acd54c | -6.1476 | -57.7215 | 2026-08-10 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| bc24b812-398e-3d64-81a8-49e6416dd462 | -14.2677 | -45.3103 | 2026-08-10 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| dc63fa8c-e158-3820-a9b2-5585b78e39d9 | -10.2455 | -45.9139 | 2026-08-10 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 53f34366-f19d-3d3d-a021-c9e593a1527c | -13.8614 | -53.7636 | 2026-08-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 74af8bbd-b967-3687-9135-cb441a1a50fa | -14.2872 | -45.3069 | 2026-08-10 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 396aed92-2a06-3b27-b774-e847e12c468e | -7.6025 | -42.7705 | 2026-08-10 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 8f1e619c-0fc2-3645-8ee5-27d25e6c3a0e | -10.2659 | -45.8206 | 2026-08-10 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 13ecc245-2247-3e72-b0c6-87eb2e9ab1fc | -7.6214 | -42.7685 | 2026-08-10 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 195.8 |
| a6b98713-8635-3708-a5e1-3c8eb9c2d7cc | -15.1326 | -52.6806 | 2026-08-10 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b9abd073-c3e8-3bf9-9908-9ebfe12815ec | -7.3891 | -59.9924 | 2026-08-10 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2f12f4ed-c413-38ab-81e5-53b36ccb6a49 | -7.5488 | -55.5629 | 2026-08-10 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ac8c5500-b74b-30cb-8a90-c89b129e4668 | -13.6287 | -46.226 | 2026-08-10 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 420.6 |
| 1d697831-001e-37b6-80b0-6ef734f61dd5 | -10.2655 | -45.8434 | 2026-08-10 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 370.8 |
| fb6b23da-7d04-323e-b431-8978390266ac | -8.2929 | -46.3995 | 2026-08-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| cac3e4d8-c712-3ea4-a57b-29f7cd7ba7d3 | -8.3117 | -46.3976 | 2026-08-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9249ce1d-b187-3dfd-affc-09840210e050 | -10.2468 | -45.823 | 2026-08-10 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ba3e5840-ed20-3838-ad08-d449da0465d2 | -11.4671 | -50.5604 | 2026-08-10 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6a5dcae0-82cf-381f-92a5-9aecff18ec17 | -6.1477 | -57.702 | 2026-08-10 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 535f9461-5d3a-39b0-864b-244b4b8d5ff4 | -13.6481 | -46.2229 | 2026-08-10 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 86427201-4a97-3f89-a619-a1e3ca342e62 | -15.0743 | -52.6884 | 2026-08-10 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 30a7d170-b88e-38fd-9afe-1315f7b8b460 | -14.2872 | -45.3069 | 2026-08-10 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| f0b55f1f-d8b9-39aa-abc6-c90eccb40bc6 | -10.822 | -46.7213 | 2026-08-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| da7215ae-9763-3b0a-aad2-f6175dae1630 | -7.6214 | -42.7685 | 2026-08-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 212.0 |
| d7513c53-659a-36d1-b038-8622d758f089 | -13.6287 | -46.226 | 2026-08-10 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 313.5 |
| 8cf3b6da-2a4b-39af-ae22-4355fd9b667a | -10.921 | -50.2999 | 2026-08-10 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 04718c70-4dda-3b28-aafb-ff831b3880ad | -11.9748 | -47.3315 | 2026-08-10 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |


[Clique aqui para ver as próximas entradas](README24.md)
