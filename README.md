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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c6f7f7-249a-3130-8d03-896f3700012b | -2.8031 | -47.4119 | 2025-11-29 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5c87f688-954e-3a08-ac55-1e1b9ef966df | -1.4923 | -45.7903 | 2025-11-29 00:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4e2fb2d3-d150-3a2d-a458-179a1d4a37b6 | -3.5083 | -47.212 | 2025-11-29 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 85ed0f7f-99d3-39e2-954b-9da6913e50de | -3.5269 | -47.2113 | 2025-11-29 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 13758eaf-dd60-3f75-81e7-c913bbd180e9 | -20.2256 | -47.5285 | 2025-11-29 00:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0e229463-f7d2-370d-8241-8be125f532c8 | -17.6155 | -46.6607 | 2025-11-29 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ab27a9f7-7d8e-3da6-b538-4e54cd0455a5 | -2.9793 | -45.2341 | 2025-11-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 11410baf-86c6-3c39-a4bb-8a027b02ece6 | -8.1633 | -43.2055 | 2025-11-29 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 0139e866-4ba4-3168-a461-92ef388e7ee7 | -20.99 | -48.6293 | 2025-11-29 00:00:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 06f058b0-0ffe-312e-a7bb-6f306e62a82b | -2.6323 | -48.5205 | 2025-11-29 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a1775d3e-97d3-34f2-aa4a-adcea423da46 | -1.4737 | -45.7907 | 2025-11-29 00:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 22ba15bb-11eb-3bd6-9935-d60cb0dc8618 | -20.1807 | -52.3975 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 85be6e2d-bae6-3227-aa78-2265258cf76c | -3.8822 | -54.2046 | 2025-11-29 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 65384ff2-9ac9-33ac-89b3-431be35bb844 | -20.1609 | -52.3791 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ecd407ac-76c7-3bea-a37d-92cdaf5e6fa4 | -2.6322 | -48.542 | 2025-11-29 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 179.1 |
| de3b0359-4fb0-3ef2-986f-62b146b3b0ad | -2.3459 | -45.7036 | 2025-11-29 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 74188ed0-b6a5-3137-8436-5ed8d7780822 | -4.1161 | -44.9129 | 2025-11-29 00:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 800a60bd-43c1-3a9a-b983-c7c7e842fab4 | -2.9777 | -45.5937 | 2025-11-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 08bfe28b-0226-3661-adc0-79068dec8f33 | -2.9626 | -49.1949 | 2025-11-29 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 50732651-849b-3060-ae75-ad4b9d7df2dd | -2.7845 | -47.4125 | 2025-11-29 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 2ccb2766-54e9-3db8-8687-fe45e0d9e4e8 | -4.3914 | -45.5528 | 2025-11-29 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5f53fda8-e904-3387-8b6a-2c1fb52e1a5a | -3.1069 | -45.768 | 2025-11-29 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b450ac03-fe22-3b40-a3c2-5e7e82ebefe2 | -2.9778 | -45.5713 | 2025-11-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.3 |
| d9aa38a5-2469-3dc9-8aba-6f7937123a09 | -4.3727 | -45.5538 | 2025-11-29 00:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b342b561-fce8-318b-a732-53b7f145a8ce | -20.201 | -52.3937 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c3ffeb0c-ab78-3cef-9077-5266eb018c49 | -2.7845 | -47.4343 | 2025-11-29 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 3f9f7e0b-617b-3bd9-a7a7-9116ae1d56e2 | -20.1813 | -52.3754 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 373.3 |
| 4fe9688f-acd2-31b9-b377-9c2e0ae86a0f | -8.1822 | -43.2034 | 2025-11-29 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 037c0676-9213-3989-a512-6a922b723ee1 | -3.0882 | -45.791 | 2025-11-29 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f63ff665-6518-350c-bf43-02eeeb187a36 | -2.6322 | -48.5634 | 2025-11-29 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fd4f9fbe-20f8-3179-88be-660bd052ddad | -3.1068 | -45.7903 | 2025-11-29 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 53148579-5bcd-3d7e-8949-d7ed51444f85 | -20.1818 | -52.3533 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 913e5108-079e-3d12-9cc9-c90cc9cfb9e9 | -2.9592 | -45.572 | 2025-11-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 44168d0b-5146-3821-a471-85c33371ee33 | -2.803 | -47.4337 | 2025-11-29 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 09c6dc71-9f1c-3e44-b0d0-279a54f6c566 | -2.2287 | -47.5152 | 2025-11-29 00:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6d2ecc35-c5ef-388a-aee0-49653ca134e9 | -2.9626 | -49.1736 | 2025-11-29 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a521fb83-6f7e-33f6-b88f-5b6fe78cd625 | -2.9792 | -45.2567 | 2025-11-29 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c7ce471d-cacf-352d-8a24-71e9d4e9dbea | -20.2016 | -52.3717 | 2025-11-29 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 131.6 |
| c9cd9fe0-5463-3ff0-9b8f-e3ad6c4e1bb8 | -20.2256 | -47.5285 | 2025-11-29 00:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9f0a601f-e43b-332b-9d89-2549467230d5 | -2.7845 | -47.4125 | 2025-11-29 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f57c23cc-9eba-32cb-bdcc-9a458d3981ae | -2.9777 | -45.5937 | 2025-11-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1c22b904-af8d-3cca-b70a-61ba307a58cd | -8.1633 | -43.2055 | 2025-11-29 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 2a82f58f-d033-3ad7-96f0-65c020563183 | -2.9606 | -45.2574 | 2025-11-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 94b30727-d0f3-38c9-ba32-9d03f33bee37 | -6.5344 | -38.8736 | 2025-11-29 00:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 86879d42-4cf3-32e5-8ada-5debb3287532 | -1.4923 | -45.7903 | 2025-11-29 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 136e40be-a9b0-3bf5-89b0-b2fa33122bbd | -3.527 | -47.1894 | 2025-11-29 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b68b4e1b-8840-31a6-b2ca-c9d7a6ab02dc | -2.9626 | -49.1736 | 2025-11-29 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 200866a1-3814-3b17-b1cd-e7050f69f7f9 | -1.4737 | -45.7907 | 2025-11-29 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 08180e09-c3e7-3352-ad39-f4b54229b1fb | -2.3458 | -45.7259 | 2025-11-29 00:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c46e6504-1f3c-35b4-b5de-6352eec15aa2 | -2.9626 | -49.1949 | 2025-11-29 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2fbe1b64-eed8-3969-a4dc-5dda8e950d33 | -2.7845 | -47.4343 | 2025-11-29 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| d915248f-727f-398d-8c1a-8c1d0aabe5ea | -3.8822 | -54.2046 | 2025-11-29 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0ffc7fed-2ac1-31c9-b790-45967154a723 | -2.6322 | -48.542 | 2025-11-29 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 193e1983-f633-389a-aa5b-8aa3c17d9d8d | -3.1069 | -45.768 | 2025-11-29 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 73a81b57-39a3-3a50-ac2b-4c814a81e68b | -2.9778 | -45.5713 | 2025-11-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 89ca5375-2902-354e-9a11-a8200a1b8872 | -2.803 | -47.4337 | 2025-11-29 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 688abb55-a1c5-3ed7-bd40-b61ba4b5841e | -3.1068 | -45.7903 | 2025-11-29 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 8bd7ad5e-a121-33fb-a05e-75f475e9ed8f | -3.0882 | -45.791 | 2025-11-29 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8a7faf0e-cec4-385a-989e-07e841a413fe | -2.3459 | -45.7036 | 2025-11-29 00:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 152.2 |
| fa51298f-e7cb-3b77-b8b1-48c851412b57 | -20.99 | -48.6293 | 2025-11-29 00:10:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| 01e02630-9624-36af-9a23-0a932f9dade7 | -4.3914 | -45.5528 | 2025-11-29 00:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6e13f657-f15c-30bb-b677-43743024274c | -2.6322 | -48.5634 | 2025-11-29 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0e234835-0752-3683-8cf3-a145dcaabd0d | -3.5269 | -47.2113 | 2025-11-29 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bcdad3dc-65df-3f3f-9e09-258cea6974c6 | -2.3645 | -45.7031 | 2025-11-29 00:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 40e41015-b493-3786-8907-56da35688ac0 | -2.6507 | -48.5414 | 2025-11-29 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| f80a15c0-67b3-3667-bcb4-b241caca6e97 | -2.9792 | -45.2567 | 2025-11-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d63af321-6713-38b4-b33a-35f2926fb28f | -20.2051 | -47.5333 | 2025-11-29 00:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5b87c780-7891-301e-889c-144f8bf7d589 | -2.9607 | -45.2348 | 2025-11-29 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 258e5dee-3808-3f48-a46f-b95dc07a481c | -4.1161 | -44.9129 | 2025-11-29 00:10:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1a1b600f-a696-3eda-b51d-36b94f3117d5 | -17.6155 | -46.6607 | 2025-11-29 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 551135e4-d590-3077-86c5-20143c71e55b | -3.1069 | -45.768 | 2025-11-29 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 59089a80-c9d1-32ec-80d8-56de8c7153a8 | -2.9626 | -49.1949 | 2025-11-29 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f44567b0-cad5-3b43-9ea2-d465c9971de2 | -3.1068 | -45.7903 | 2025-11-29 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 25b7eed8-3fda-3bae-b101-eae87b64c0bc | -20.2256 | -47.5285 | 2025-11-29 00:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 7e9d0e1a-68b8-309d-978f-fa7286c6becb | -3.0882 | -45.791 | 2025-11-29 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7bdfea67-c41d-3ed7-a149-3fd5fd7522d5 | -20.201 | -52.3937 | 2025-11-29 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3646a937-b5b6-307c-a5ee-6c7466b92333 | -1.4923 | -45.7903 | 2025-11-29 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| fdd7df71-a961-3f8e-a714-3c3f3f102eed | -2.9793 | -45.2341 | 2025-11-29 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b961a20c-5dd6-304b-b24d-acef48050306 | -3.5083 | -47.212 | 2025-11-29 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b1fc1be6-3ba3-3d91-a938-5f0da886140c | -8.1822 | -43.2034 | 2025-11-29 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 0eb19a18-7468-3602-ab6d-65288bfaf95a | -1.4737 | -45.7907 | 2025-11-29 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2dabc21b-43d1-36da-808e-f7313d34d3a8 | -8.1633 | -43.2055 | 2025-11-29 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 6e880aad-204b-3ba6-a5da-1e85c83a2c03 | -2.6323 | -48.5205 | 2025-11-29 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 037b7877-2cd2-3c3c-8589-567d259257ce | -2.9626 | -49.1736 | 2025-11-29 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 96b67edf-e953-37bb-9847-5627275dd840 | -20.1818 | -52.3533 | 2025-11-29 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1d422027-3b19-32e9-8448-d7ae58c1c224 | -2.3459 | -45.7036 | 2025-11-29 00:20:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 5b42db17-e5a5-32ee-bd73-329fd7a3d950 | -2.6322 | -48.542 | 2025-11-29 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| eafcddd4-aabe-31fa-b984-829ab853762d | -20.1813 | -52.3754 | 2025-11-29 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 302.0 |
| c79c0f55-0919-33e7-b2c7-de0bfa222570 | -3.4692 | -47.6282 | 2025-11-29 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| ad2e8da6-e6c7-3e77-a5b5-6e5e50cf9db6 | -20.1807 | -52.3975 | 2025-11-29 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c84d692b-b775-3e49-b104-ba10bda25668 | -20.2016 | -52.3717 | 2025-11-29 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a5105724-89ea-3763-bb7c-d364d8baa64c | -2.6322 | -48.5634 | 2025-11-29 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| eccbae56-39a5-33c2-853a-9fe046b63355 | -17.6155 | -46.6607 | 2025-11-29 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a1c61b73-5346-39b9-afdb-b8a42554403f | -20.99 | -48.6293 | 2025-11-29 00:20:00 | GOES-19 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| b64ebe3c-b84e-3277-bd46-5f0cbba6676a | -3.0883 | -45.7687 | 2025-11-29 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6129cd49-915d-3152-8b78-edb11377e75e | -2.9778 | -45.5713 | 2025-11-29 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 32460caa-ab0e-370c-adb3-0a9cfb1e0ad4 | -2.7738 | -45.4887 | 2025-11-29 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 053d536f-d3e3-3b6f-8a28-45224a944e0f | -4.1161 | -44.9129 | 2025-11-29 00:20:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 15db2e5d-9082-376e-b4ad-8934be70ac52 | -2.6507 | -48.5414 | 2025-11-29 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bb19e1d0-7261-32e9-9cee-b8c7cbb69e2b | -2.9792 | -45.2567 | 2025-11-29 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README2.md)
