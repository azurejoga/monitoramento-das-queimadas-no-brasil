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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a25ca7d3-a94d-31d9-a10b-83efa5db15c4 | -2.44931 | -49.5701 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 72ffd242-0ff0-3b65-bbb6-3f8a8f7516c1 | -2.44874 | -49.56643 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 866957a7-860c-36ad-834a-fd7c03ca2661 | -2.4459 | -49.57063 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b54eadcc-8ef8-37a5-8308-d2f2b1101231 | -2.44306 | -49.59734 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fe452632-146a-397f-b024-8c54d8385278 | -2.44306 | -49.57482 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7b7d4590-f8bd-30e4-8adc-9e936f72c952 | -2.3893 | -49.38631 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d64cf0ba-071b-3faa-8053-6de9b21a1ad5 | -2.38872 | -49.38259 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c132f026-f303-304a-bbe0-b8e488f37367 | -2.36931 | -49.3932 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fc067e8b-a9cd-383f-9b0c-3cf7085d114e | -2.36646 | -49.39745 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0ac55fb-a068-3c22-a044-d6464839e6d2 | -2.36588 | -49.39373 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3512a314-92e7-306d-964a-32312d5ba618 | -2.33116 | -49.57666 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22212b47-cbc3-33b3-867d-886aa10ff225 | -2.33059 | -49.57298 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a1ae5f0-989e-3599-b966-6a78494fdd2c | -2.32661 | -49.56982 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a2b8c71-8358-3097-8788-5785061117e8 | -2.32604 | -49.56615 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c9052ab-7df0-3df9-b3f1-f4db4932214c | -2.32602 | -49.52088 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd76e394-d6eb-397e-8c65-45a4a420c13d | -2.32433 | -49.55511 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6befd2c1-d3d5-38d3-874d-d22c6344f1e9 | -2.3013 | -49.36119 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9992b571-9835-385f-84d0-572070a80919 | -2.2943 | -49.63114 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0d20e09-c559-3088-95c5-30067c45ab3e | -2.28903 | -49.53035 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c35ee303-af36-3994-b541-bff3c5ae237c | -2.28561 | -49.53087 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31c96ab5-756c-3e85-b7ee-78bcf79cbc1d | -2.27725 | -49.3649 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a00f74c-d2b6-360a-bc57-c755986b104c | -2.24824 | -49.54075 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 23272e06-f9dc-322c-8450-1ee3819923d6 | -2.23456 | -49.33719 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a5ae4e0b-95ae-3aea-988e-7e314b5ab75e | -2.23112 | -49.33772 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 0f0448ac-235f-37d8-be05-9e973a6fb3d6 | -2.23059 | -49.51699 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4ea5c98a-6e2b-383e-8d3c-dae6dad26f35 | -2.22717 | -49.51751 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bc988615-d641-3a1b-ba53-52f222c7d684 | -2.21464 | -49.52701 | 2024-10-25 16:52:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 472a38b6-a812-3324-a62a-7da787af4a5b | -4.95607 | -49.93 | 2024-10-25 16:52:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 48b7c2ac-a819-31fa-8f0a-9b231b42a91f | -4.9509 | -50.4472 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5223a1e-f573-3cd9-bc7b-156639ad1e4e | -4.81243 | -50.63177 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0f868ed-4110-36aa-adcb-fb5fc7526af1 | -4.79868 | -50.54215 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa20921c-83ac-3e83-8085-c8f944366207 | -4.74054 | -50.69212 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d47bcd3b-f4c8-3a98-9268-50ef5174b8bf | -4.72847 | -50.79328 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b16262fb-a02e-3548-94da-83e30e31b03c | -4.72517 | -50.79379 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0071548e-8054-3099-a9c6-6c64ed4e4f9e | -4.68699 | -50.74326 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3985e0ad-baad-3d1d-b1f5-7f644120138c | -3.95329 | -49.99582 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fde08cde-da04-3c35-8154-6097a295f3cf | -4.68422 | -50.7472 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a882109e-4e68-3987-aae1-24e7af22582e | -4.68369 | -50.74376 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 426ef382-da0d-35cc-8db4-4c0faa35e36a | -4.68316 | -50.74032 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9eb8d435-a252-3338-bc57-500371b60213 | -4.67206 | -50.75611 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 53c4cdc4-0a92-3489-90c5-af62f7e1d1b7 | -4.66875 | -50.75661 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fa88a067-9116-327e-8631-733d653a16d2 | -4.66823 | -50.75317 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1f654d2e-f4dc-3839-8ae6-051d58f5ce5b | -4.62152 | -50.65143 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 430d2161-d9fa-3d06-9bec-d24dd05115b2 | -4.61621 | -50.79317 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6790c569-8d50-3a19-9a3f-bcbb390ee786 | -4.61545 | -50.5638 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3969040a-665f-3a3d-a8cd-e574edd766ae | -4.6129 | -50.79368 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c65bdaa-da40-39ce-953f-a3d7cc7dfa68 | -4.47602 | -49.85878 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56ccdb2f-7f3b-3877-a216-4919c6ad8a1c | -4.40944 | -50.73117 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4cc74275-1d0f-35f8-bf97-bcbbf2881dd2 | -4.40338 | -50.53376 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85e7ac2b-195f-3991-803d-382a87ce93df | -4.39399 | -50.53874 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e42f76ed-a6c4-31b1-b45d-2985dbf03b48 | -4.39239 | -50.52837 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97239e3b-b30e-3bb7-a658-baefbcc30647 | -4.3606 | -49.83735 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 563dac23-7619-374c-95d1-4ffbbce48246 | -4.35123 | -50.4399 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e7820404-08c3-358b-8fa9-7dfb62c75864 | -4.3507 | -50.43643 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d22d4f9-5baf-3aa5-96e7-4960873ee235 | -4.34792 | -50.4404 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ac53eda6-cfeb-320e-928d-459cd622f064 | -4.34739 | -50.43694 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71cf44d2-071f-399e-9116-c861d46f01dd | -4.29122 | -50.73537 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2c28e631-93af-338d-a17d-67b3d550d109 | -4.23133 | -50.63167 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7b7b4478-7fd5-3943-a6b5-43bd64f36259 | -4.2308 | -50.62822 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3e489f02-830c-3f9a-92f8-94ade669b4ab | -4.21064 | -49.74866 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e7a6faa-5c58-38fe-bf7d-2b0e1efb60ef | -4.1608 | -50.74918 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ca1aefa8-018b-3fa6-9c7e-983881de0a1b | -4.10711 | -50.42169 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38568e8f-d6dc-300a-ac95-963b0c00b823 | -4.06914 | -50.04226 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c044fb13-9f4f-3ba1-9599-6408f7deaed4 | -3.92985 | -49.86574 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 943a0a0b-c981-3d8f-be37-11d6318226da | -3.88641 | -50.04928 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cfc358da-e189-3b06-84c9-cd98ae58fff5 | -3.88308 | -50.0498 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6fda69ec-ee2b-3f88-a6fd-49929fd2a827 | -3.88029 | -50.05384 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 036871b4-30e2-39ff-9de6-b558a0a2cb02 | -3.87736 | -50.0544 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7c182da9-646a-383d-a3a1-342effbea9b3 | -3.80252 | -50.16635 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c4ab6b4-9de2-3385-8e8f-4ba2699fa60d | -3.79854 | -50.03053 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b260cfb-c3fc-32eb-8e53-633e15d2af15 | -3.77129 | -50.03111 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ce5b9e6-945e-3478-91aa-e4394b66e64c | -3.73004 | -49.8026 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e9bc268d-d79d-33fb-a6ba-39f824c0c504 | -3.72668 | -49.80312 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a9114b1a-29f7-3680-b3b6-8d5c1f2fb5b1 | -2.24047 | -50.53117 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e77acace-519f-38b1-8745-526ab00bf399 | -3.6676 | -50.12747 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48e2e63e-efae-3725-92cb-5759a52fc586 | -3.66427 | -50.12799 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f0f9609-a422-3722-ab39-e88a68bd7a2e | -3.66373 | -50.12447 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2474495b-5241-39e3-ae8d-47b509498d51 | -3.66093 | -50.1285 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8e9e61f-2c43-37a7-a318-fd2f5bee5e47 | -3.6604 | -50.12498 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 470cafbc-d6c9-32c5-8500-8e397854e5cb | -3.65986 | -50.12146 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b3e841c-e190-3e93-9663-350e85b6f76f | -3.65932 | -50.11794 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b8e1521c-3afd-3f72-a5e8-6e019d52d0ff | -3.65706 | -50.1255 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3fe63cb4-2b78-3d8c-80ad-9ac5996ec800 | -3.65652 | -50.12197 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 49021ac9-51b0-36e3-96ed-b4c16f755f4a | -3.65598 | -50.11846 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 102f92fc-adaa-321d-a93b-7dd1a945d07e | -3.65018 | -49.75307 | 2024-10-25 16:52:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 442d490b-1f47-341c-90ca-52a1333fe2da | -4.53063 | -49.59606 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 32d39485-68ef-3f15-8d42-823b2186d672 | -3.93806 | -49.39426 | 2024-10-25 16:52:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba39420c-5b6c-3b7a-85a3-113a8bfe8f4c | -3.76139 | -50.38386 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ebff3bc-79e7-339a-ac28-8047d9cda67c | -5.9146 | -49.77402 | 2024-10-25 16:52:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a047435a-88fc-3a59-999f-b4827da66e1f | -5.8678 | -50.04243 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f07f56e5-cdab-3bca-8d88-b8c7251c3243 | -5.85802 | -49.86928 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 168d9aee-f9b1-38cf-9374-6ddcfaa4a390 | -5.80543 | -50.10196 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a2a2f237-d678-3cf9-a986-a47a2d5e018a | -5.80489 | -50.09849 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a261fdae-3d00-3c88-9c7e-fef6d564d59f | -5.73989 | -49.94127 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 524e4b34-e372-3b61-88d3-7609ef6f1b69 | -5.61477 | -50.01102 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea485d45-7893-368d-a5e5-01e0f638fa43 | -5.57328 | -50.00761 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 568cfa67-e4c8-3edc-b6e2-07b757bb40e6 | -5.51168 | -50.80327 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44c83a91-a3f7-346f-8fb6-0be681b745e2 | -5.45121 | -50.71731 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6635436c-862e-3779-84a6-4171d27a0633 | -5.35552 | -50.7362 | 2024-10-25 16:52:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c6566bd-3ea6-3d25-bfff-8af59472c77f | -5.17452 | -49.9134 | 2024-10-25 16:52:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README155.md)
