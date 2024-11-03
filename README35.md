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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6747071f-4ab0-37f0-b28b-50f3c7f0a8ac | -1.27225 | -45.74164 | 2024-11-03 04:44:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b158eb28-7000-337d-880c-5bd377ccfed7 | -1.27141 | -45.7434 | 2024-11-03 04:44:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41abfa2b-e604-3ec8-8561-82c5e063aba9 | -2.62114 | -46.14697 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b35b6b4-ed5b-3a47-8ce9-bba9710788c3 | -2.61695 | -46.14909 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c250e4f1-6758-3c74-b3f9-833199e943df | -2.58974 | -46.14974 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb9725a4-ac1b-311d-b2d8-98427eb61373 | -2.57813 | -46.12425 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e137f20-c4c5-33f3-86a5-20540158b039 | -2.57505 | -46.11906 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8da31516-b2cf-36be-a29b-f1188bcdb648 | -2.57334 | -46.10476 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2483005d-3dec-35f7-bea1-1e13350d3768 | -2.50322 | -46.18135 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ceb10ca-0f90-33a8-8fa4-9e49c137e851 | -2.49945 | -46.18076 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e686d2d0-f3e9-330a-8828-480403fef545 | -2.49896 | -46.36786 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3373773-137f-3168-ba88-496dbe54d31e | -2.49447 | -46.28716 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68d7a0b-f818-3c5d-a2af-9a735ebe10c2 | -2.49168 | -46.28865 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06884bf3-0e70-3e39-be2c-26991b161946 | -2.44227 | -46.35245 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf488837-7670-3940-9ce7-00f6618794a4 | -2.4287 | -46.71044 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6e6a89f-49eb-3afb-997d-032455572668 | -2.42821 | -46.71247 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75fd32ee-2225-3083-96b0-24ec2d36b616 | -2.42806 | -46.71472 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a770d7-cff5-3d42-ade7-a82237decc31 | -2.41989 | -46.69373 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71808113-e804-3ac0-9b79-8ebdd9986706 | -2.4145 | -46.43449 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 049c0e41-590e-3c71-9cca-b849c35e171a | -2.41383 | -46.43889 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ff1f656-67d9-3522-b1e6-1f748b74dfa8 | -2.40026 | -46.69952 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbfa16fe-4478-346a-bdaf-9b339fe47532 | -2.39242 | -46.57924 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e853998-70cb-30e3-8066-a637b208b3da | -2.3911 | -46.58791 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36ad43b3-8f04-30e1-a766-ca20fcec883e | -2.38808 | -46.58302 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88366e20-e9a8-32d3-9ba7-5a1dd79d6abe | -2.38572 | -46.57376 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37eb197b-8ba2-3e6d-9950-7e487db84682 | -2.38506 | -46.5781 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f07ad54f-516b-3f30-aa2d-fc00078849f6 | -2.3844 | -46.58244 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e4c617a-1da6-3e11-8be3-cd1825840798 | -2.38072 | -46.58186 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60bbf60d-e897-3e71-8f3c-077e745839ea | -2.37444 | -46.47347 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe8a6aa-716d-3e9d-9fec-0a58bf105802 | -2.36652 | -46.5261 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5321890-fa65-3e40-b0f8-f4d586ca3baf | -2.3426 | -46.65997 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19e22bc3-248d-3640-99bb-9c8943185338 | -2.33846 | -46.51877 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0020a651-314c-3cae-8d6f-b6cf475a5c3d | -2.19468 | -46.4271 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9885d6-ab6d-3d92-8ef7-f9c051ea73f9 | -2.19102 | -46.47588 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1fdaff3-e16a-32c0-9041-98deaf3a1152 | -2.18363 | -46.47475 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19c988ad-5be5-33f6-989c-babf6e22f42f | -2.18296 | -46.47911 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738582b0-48cf-3fc4-93da-ad02c19cd6c5 | -2.17993 | -46.47418 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d52b7852-7b6f-3866-8342-c496ab300637 | -2.17927 | -46.47855 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6631fe4-b98e-391f-9a3b-5d50bf2e5474 | -2.17558 | -46.47797 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32d67ef2-c20c-36f0-a62e-77dc758dc288 | -2.31263 | -46.56378 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 999d5408-cc40-3724-812f-60d3c22da47a | -2.30759 | -46.52298 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97619568-d1c7-3354-98bd-418ef862285f | -2.30692 | -46.52734 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fd92022-45f4-3e26-9523-f685155b1862 | -2.30565 | -46.68182 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3640550-e367-3e33-9f25-376db11f265d | -2.28108 | -46.69559 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d75372f1-eef2-301f-84cb-55bd8b28c2c7 | -2.27939 | -46.68223 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ad5664-1d90-3f02-a296-f4dafa58954a | -2.27742 | -46.69502 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c1db8c5-fffa-3622-8c80-4a62df2e976d | -2.27666 | -46.47794 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e31a6c6-82ce-3020-83d0-2aaa3234a46a | -2.27599 | -46.48232 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 823e2c2c-b432-354b-9d35-fd9d96981927 | -2.27573 | -46.68165 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a773bfd2-fff5-38b3-ac05-d017cd34e9be | -2.27508 | -46.68591 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50515802-7f62-3073-bb1a-33f2a6d067af | -2.27443 | -46.69017 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6566833-2a91-3329-8ea3-09ff0b0b3f3d | -2.27143 | -46.68532 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efb3792a-2746-312d-a350-dfc4d636c12b | -2.26412 | -46.6842 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3e425f6-f052-3ac6-9d89-a003b4d6cd4b | -2.26111 | -46.67937 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ea0822-5793-3534-a94c-ea372cbcb8da | -2.26058 | -46.60896 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de3e7a8e-28ab-3675-9475-eb97a47a0946 | -2.25756 | -46.60408 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e8ec246-c12d-3de0-a274-c364a1c457d9 | -2.25746 | -46.67881 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20537273-1c7f-3299-a025-2a4f6402809b | -2.25469 | -46.64774 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46ccfa22-f7f9-39f9-a739-01dfaf3d0ad2 | -2.25454 | -46.59919 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d8064c-4f65-38b7-afb5-81a6d4f37a4e | -2.25445 | -46.67399 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f72db403-d4f2-3a79-aa5b-994b044a959a | -2.2538 | -46.67825 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ba4a6dc-04ce-3b9e-811c-4f7a30195e2e | -2.25149 | -46.10482 | 2024-11-03 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23bd9f77-98a0-3dd9-b199-16793e258744 | -2.25144 | -46.66914 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb170119-2006-329c-91c1-84414c718847 | -2.25103 | -46.64717 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 500724f5-9e18-3434-ba74-353db04d7cdc | -2.2508 | -46.67342 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b648820c-d314-31a0-87b0-ba346d27d820 | -1.12774 | -48.37024 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b15caf8a-22df-3348-ab63-745a67c4c10a | -2.25039 | -46.65143 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 981c6ada-8dcc-39be-b48a-7666beeb0472 | -2.24844 | -46.66426 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c21e2abc-7b5a-3db0-b67d-f9f52d888203 | -2.24779 | -46.66856 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89ad2604-31ed-395b-a9d7-3d4480bf3c26 | -2.24714 | -46.67284 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c90f666d-04a7-3b03-a678-407c5ceba4c0 | -2.24525 | -46.61101 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c2407a1-e579-36e0-be81-a1793816c143 | -2.24349 | -46.67226 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9069e2a2-0451-3f53-91fd-667b20f3b238 | -2.24093 | -46.61476 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee20c13-6da3-36c3-bd02-17bc3fef8264 | -2.23924 | -46.52578 | 2024-11-03 04:44:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3598c9-14a7-3135-80b0-276848bd5dcf | -2.23295 | -46.6925 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64ba1b2a-df13-3044-a64c-e502675a8fa2 | -2.2293 | -46.69194 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4af44dbf-a116-3729-ad2c-e0ba52a82bdc | -2.22564 | -46.69136 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 417e7d22-3629-3d86-8dc1-3e96bd860af9 | -2.22199 | -46.69079 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecd887f1-96c2-3076-aa49-bc83046a09a1 | -2.22139 | -46.69263 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cedbe6a-3aa9-36a4-8206-dbd07b8ee011 | -2.22135 | -46.69505 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93ee02f1-f3a4-397b-97c8-727e0de525ca | -2.45402 | -46.88786 | 2024-11-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89fcbeba-6191-3ca3-91fa-d45ca3c2d7fe | -2.45104 | -46.88311 | 2024-11-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab3e6e5a-4644-363a-8a8f-bac48df88a06 | -2.45039 | -46.88734 | 2024-11-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 363cf084-2ef1-3064-95d7-923ad1c0311c | -2.4346 | -46.89367 | 2024-11-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc580fef-af2c-32a7-885d-c41fdd19d0b9 | -2.40098 | -46.74329 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 476fb432-e73d-35d3-98d8-5da92d50d35d | -2.40033 | -46.74754 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e64c9562-62d7-32ad-923b-9123ac5c9921 | -2.39799 | -46.73849 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e6ace33-bb73-3fd4-a317-a9997c84eca3 | -2.39499 | -46.73369 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75317ec1-1074-3336-897d-2ed90fa86ea6 | -2.37452 | -46.76972 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa29675-aeb3-3b69-bc57-b07006cd51e7 | -2.37153 | -46.76491 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b9000cc-0a7c-3043-a6c6-8e5dd1ec9a61 | -2.37088 | -46.76916 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c31c6328-5862-353b-90d6-6d8ab8b660c7 | -2.36091 | -46.85843 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644c0d0d-50d2-362b-bb12-e555ac910aa9 | -2.31577 | -46.73901 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c0be14a-9e40-31c5-8c2a-d66add307f80 | -2.29771 | -46.73303 | 2024-11-03 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cfa1cc2-4d4c-32c8-9965-b624bca44985 | -1.2755 | -53.4138 | 2024-11-03 04:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| df623f92-e216-3cbf-9d86-ca9095e2db22 | -1.2755 | -53.3936 | 2024-11-03 04:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| a5c135e5-0f1e-3ccf-ae7b-24d4c3222444 | -1.2756 | -53.3734 | 2024-11-03 04:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b3328038-c5c2-3c6e-83cd-575a252f182b | -2.5797 | -53.3724 | 2024-11-03 04:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cfc67b9a-5d3a-33a0-89d2-d4ab85044643 | -2.7419 | -54.4353 | 2024-11-03 04:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 000cae46-9822-35fa-8a7c-8ab27273c5d6 | -2.7419 | -54.4153 | 2024-11-03 04:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |


[Clique aqui para ver as próximas entradas](README36.md)
