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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee93754-5fc2-340b-87f9-1db253be6c5d | -19.645 | -56.7891 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| ec48d7d2-91d6-354f-ac1d-f4ea095349ab | -19.6453 | -56.7681 | 2024-10-23 04:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| d0ce0508-25f8-36aa-900b-0129fdcd5f7e | -3.1101 | -54.1661 | 2024-10-23 04:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 11d17732-a7eb-3683-8d03-a404952a3f6a | -3.1102 | -54.146 | 2024-10-23 04:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cb801d06-27a4-378b-bc7f-3ccc28e4b869 | -3.5491 | -54.7351 | 2024-10-23 04:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 57e3bbb4-c41f-3fca-a634-2790324c0ec0 | -4.1119 | -45.5897 | 2024-10-23 04:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 72d4218c-ad52-375c-be9d-40d707dea98e | -4.1305 | -45.5888 | 2024-10-23 04:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 0a128cc6-3fd3-35f0-82f9-822385c0cb04 | -4.1491 | -45.5878 | 2024-10-23 04:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 20894d77-f318-3a67-a618-30030884b108 | -4.1304 | -45.6112 | 2024-10-23 04:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 172c8f30-5ed2-388d-afbe-f896f468a21c | -4.1905 | -47.9885 | 2024-10-23 04:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9f393573-8450-3e4b-a0b0-80f23e8415e7 | -5.5858 | -43.2562 | 2024-10-23 04:45:36 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8c026ece-d1bf-3e04-bd6f-c2ec46d68406 | -15.9081 | -51.7383 | 2024-10-23 04:46:34 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9854d8c0-b023-3972-880e-ba179313cf37 | -17.0188 | -57.4973 | 2024-10-23 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 01a7cb24-9fd2-397d-a87b-64e7a4faf083 | -17.0184 | -57.5178 | 2024-10-23 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| ae0e69f0-0cca-3f02-98d6-900f4a5b1fd8 | -17.7848 | -57.4885 | 2024-10-23 04:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 05c6db74-0540-3e53-8bb6-1f67fa4015ec | -18.3004 | -56.2222 | 2024-10-23 04:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| ab86f571-9031-3b28-99b1-3dfa4b2a3af5 | -18.3203 | -56.2195 | 2024-10-23 04:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.7 |
| 579837aa-87cc-34cb-802b-085b280bafca | -2.16208 | -45.33888 | 2024-10-23 04:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf2e8699-5a27-366a-ac3f-a784f577c1ff | -2.03637 | -46.97152 | 2024-10-23 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 487e007a-5072-335c-a010-31d336c90459 | -2.1607 | -46.03988 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f2e90db-4df1-3454-9205-b4bc5072f65a | -2.04029 | -46.97215 | 2024-10-23 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 248d8f41-9408-334a-8a50-8b706faa5ad7 | -2.03953 | -46.9771 | 2024-10-23 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c44a9adc-bd47-3440-b20f-424ef8298635 | -1.89773 | -47.03886 | 2024-10-23 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b51f5e-f1c9-3e0b-97cb-7b48c5bc7548 | -1.6829 | -47.07732 | 2024-10-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 059f2f7a-92e5-31ee-806d-9adfea67a826 | -1.5363 | -45.78683 | 2024-10-23 04:49:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91917091-7fcf-32fd-8c6f-b9dfa155ba2a | -1.53578 | -45.78707 | 2024-10-23 04:49:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72ca4128-27e2-38bf-8f35-19eecc5e753c | -1.22184 | -46.5435 | 2024-10-23 04:49:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a4010c9-5136-3ea3-ab6f-716b44c80f79 | -2.48268 | -46.28474 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e33452-7d8a-30e4-ba77-abbfe46c7a3b | -2.37292 | -46.97791 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519f4f30-f388-3aa1-b7b2-f15bb43d3d2e | -2.36349 | -46.54593 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52fd27cf-a952-3fa5-a2ce-2067160755ac | -2.33685 | -46.4757 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0145db85-e5fa-337d-aee4-5df102a98278 | -2.33063 | -46.23792 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8bee45f-eabe-3235-81fe-60e7c68a5827 | -2.28834 | -46.43925 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47169e3e-6691-3076-83b1-fa5c560fe6a9 | -2.28313 | -46.44593 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 239ddbbc-cd4b-3c88-967b-d6e21cc06813 | -2.26538 | -46.75747 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d93f5b-6fbb-36f3-9a76-b5329e7ffdd0 | -2.2588 | -46.77409 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d0e14a-ef6f-3c51-b21d-8b37edf9e0a2 | -2.25482 | -46.77346 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55a617e7-3584-3204-90f2-8f7311896eeb | -2.2543 | -46.77689 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4cbcb1-52a5-3672-8661-0e8752024a89 | -2.19219 | -46.71455 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5de10228-1c8c-3d13-a58a-4155508ecce1 | -2.18503 | -46.7347 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d125486d-e102-3c65-84e7-ee078c326f7b | -2.18156 | -46.73063 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1eb892-4458-31f7-a093-cbf028564007 | -2.47855 | -46.2841 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f69417-96c8-3b5b-9417-437f4be0b446 | -2.47769 | -46.03466 | 2024-10-23 04:49:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58561774-5ef5-3813-94a6-42c026c2cfc4 | -2.38245 | -46.42329 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aa75284-e047-3862-ab94-ca9f3d793230 | -2.37685 | -46.97857 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a927cf6-228b-38a9-8bcc-b06375480cd6 | -2.36674 | -46.16669 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdd345e3-9e07-33d6-a019-c7d33be20baa | -2.3363 | -46.47933 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f02192ed-f99d-304e-b985-32b530bb2743 | -2.33007 | -46.24165 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46e7e10-94f8-3981-8fba-11cd18845378 | -2.32808 | -46.23854 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38b213c9-8df3-3e76-898d-3090c423a9c8 | -2.32749 | -46.24227 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4d4aefe-bf17-3413-8ac2-d83f1c85035a | -2.32594 | -46.241 | 2024-10-23 04:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad115061-183f-31e6-9f1f-eb25399db77a | -2.32408 | -46.47747 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb4d812-1d1b-3bba-84d1-baedc826e834 | -2.28891 | -46.43559 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b175e1-c7e5-39be-9b5b-6541b43e77b6 | -2.28426 | -46.43864 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a71e2ab-8290-35aa-9af5-a73425bdced3 | -2.27597 | -46.74144 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ecf819a-030b-3458-9344-7492abc40374 | -2.27545 | -46.74491 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 930dfc14-f0f0-3e72-a738-2485369a9997 | -2.26678 | -46.77531 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90ee9ddc-5bc0-30aa-b4f3-d52e23134de4 | -2.26486 | -46.76094 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4afef4df-c9ce-31b5-9d38-b74218a5ab1a | -2.26279 | -46.7747 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88a3b153-f1e1-321c-8014-838bbc1305cd | -2.25829 | -46.77752 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3808cc99-0f30-35ec-9ecb-0866d7e7734f | -2.18766 | -46.71741 | 2024-10-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2db1f470-01f3-3427-abca-e7488fd4905c | -2.13938 | -47.91725 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 01085538-e2ed-39bf-8dfd-355e53dd8e05 | -2.04318 | -48.65461 | 2024-10-23 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc0d81fc-5e13-3d74-8426-88a5026a001c | -1.97578 | -48.68967 | 2024-10-23 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eda407a9-c7ac-3ed6-b5f7-5d61411c9779 | -1.87353 | -47.81254 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40570c44-8347-3723-afef-6cbcde04fe22 | -1.87214 | -47.80931 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3daec2dd-de62-399d-ad27-3daadf6b31cb | -1.27593 | -48.04667 | 2024-10-23 04:49:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d511ca7-7bfd-311f-aa9f-9e8675898dfb | -1.27162 | -48.05034 | 2024-10-23 04:49:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6aa85aa-9e8e-306b-89c5-a152eb4208a2 | -2.13567 | -47.91666 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c5729e9d-21ce-3e95-8c63-3828cf196d55 | -2.1162 | -48.25906 | 2024-10-23 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fe5631a-d83a-30a4-a73d-e0006e883295 | -2.11256 | -48.25849 | 2024-10-23 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64c10a7-b900-3926-a855-2ea5814d860c | -1.97702 | -48.68159 | 2024-10-23 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad5f4df-1d90-3384-8c8b-886f8f323780 | -1.9764 | -48.68563 | 2024-10-23 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c41c1f10-f3ba-34f0-8ab0-efad3102eb41 | -1.87586 | -47.80988 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0242767-82a4-32b1-8c57-5e212e545269 | -1.87421 | -47.80809 | 2024-10-23 04:49:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f8a83c9-610c-3287-bdde-6465f59a704c | -1.69583 | -48.166 | 2024-10-23 04:49:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b662bb4-969c-3759-a24b-9c920635711c | -1.59625 | -47.84331 | 2024-10-23 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6469abb6-79b4-3da0-988b-40ebb403991a | -1.38215 | -47.82259 | 2024-10-23 04:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c77f9fc3-7712-326e-89b8-20c45dafdc55 | -1.27526 | -48.05091 | 2024-10-23 04:49:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3967ad9-7ba0-356f-a605-d9eca66c3671 | -2.25665 | -47.66204 | 2024-10-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14ad97ab-9698-338f-b3d2-e10fd1f88b44 | -2.28263 | -47.91529 | 2024-10-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d7e4be-f174-3297-88d4-127064481cd4 | -2.27891 | -47.91473 | 2024-10-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b7a8a5b-4cd3-398a-8305-b4b2fafbed7c | -2.18594 | -48.55489 | 2024-10-23 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e450a95-6327-3c90-97f3-f921fa25b221 | -2.18235 | -48.55433 | 2024-10-23 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 846b6047-a58a-3109-b4b1-dbe13d7e66ba | -0.37466 | -49.91931 | 2024-10-23 04:49:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ee7fd4e-71d6-3110-a1f6-84b03203c279 | -1.69954 | -50.02141 | 2024-10-23 04:49:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee3e997b-7ba7-3ad1-8f1e-d14702a68c37 | -1.17833 | -48.85671 | 2024-10-23 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c57cc6cf-72b1-3ce8-996e-8c979927f17a | 2.62207 | -50.88567 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6d2b8381-8c1c-3327-a22e-a8e87435df6b | 2.62099 | -50.87881 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 561bd37a-6ae6-32f2-bcf1-bf5be3f5ab2e | 2.61769 | -50.87931 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76c2f1f7-9234-35f2-90e7-cfde9d383e7d | 2.61218 | -50.8872 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 155bfa1c-fae7-3aee-b513-c2c3c380a1fe | 2.61164 | -50.88377 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8e6a329-51d3-32d0-b7cf-5ae3175b080d | 2.56264 | -50.91592 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ab175c1-ad73-3f1d-a854-97fb904cd035 | 2.35956 | -50.75165 | 2024-10-23 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 655581da-7cc6-3a16-bc95-ca00cb5cbbb4 | 1.80247 | -50.47855 | 2024-10-23 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12b6ac0a-7b27-30da-a2e6-2466e012b102 | 1.79971 | -50.48249 | 2024-10-23 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16945fe9-0d8a-3835-8784-12222f04eb1e | 0.98538 | -51.14692 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d08de8a7-6d7b-3bb1-9ec5-e028ba14a660 | 0.98209 | -51.14743 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a92e95-9788-3b8c-a61d-91e1bcc06415 | 0.98155 | -51.14401 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55565672-33ff-36a3-b0af-bfb2be0c4102 | 0.97933 | -51.15136 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
