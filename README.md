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
| 42995ace-9d1a-3842-9c7d-834a660c2d58 | -2.8326 | -40.302101 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 565416da-7510-354e-a803-140091615605 | -2.1955 | -45.6768 | 2024-12-24 00:04:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49d64786-ce5b-3e06-af98-d2e518925f4d | -12.181 | -41.3428 | 2024-12-24 00:04:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6c2345ce-bc5c-3b1a-87ca-aee1dffaa8c5 | -1.4631 | -45.807899 | 2024-12-24 00:04:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78330ef9-231e-30a3-8eda-fa523d828e95 | -4.9389 | -41.312302 | 2024-12-24 00:04:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6344bb4-441b-3ff9-b546-3e7c02f69c69 | -2.8027 | -48.673698 | 2024-12-24 00:04:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13c94065-c631-38b9-9edd-ad1a9183dbd4 | -2.1939 | -45.669601 | 2024-12-24 00:04:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93ddc870-66e2-3c07-a25e-d9ad36156897 | -3.5284 | -40.776901 | 2024-12-24 00:04:00 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d6d9ff97-2161-30cd-8659-75c823bfd8a3 | -10.8544 | -37.230202 | 2024-12-24 00:04:00 | METOP-B | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3f9b6de-d6eb-300d-8f36-7627831b29f9 | -3.9168 | -46.892101 | 2024-12-24 00:04:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| becd8889-e224-361f-9dc8-dd5dce86bbcd | -2.8549 | -46.738098 | 2024-12-24 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e355d83-e6f0-33df-ac20-507b6d2d143c | -2.9619 | -40.282101 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80ea540b-2858-3f8a-8233-7c4a17f84c72 | -3.8967 | -46.106998 | 2024-12-24 00:04:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 262883e0-451a-36ba-a60b-14e55dae50b5 | -2.1923 | -45.662399 | 2024-12-24 00:04:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d89ecf51-d7ae-307a-a837-da47a7ab2894 | -2.2129 | -45.432701 | 2024-12-24 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75aff6bf-3133-35ca-b3a8-0c984f84da52 | -2.9973 | -40.391399 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7543c706-ad86-3662-be2b-fe593a86b34d | -3.1852 | -45.960201 | 2024-12-24 00:04:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98387f35-a194-3dac-ad5a-ffa1134d40f3 | -6.997 | -43.257401 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f0e9b64-f250-3e86-b8f5-78ff21f44d24 | -4.9441 | -41.334702 | 2024-12-24 00:04:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a16f51e9-96cf-3f87-a6e6-e4157d3f8493 | -6.9688 | -43.546101 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58c359be-f276-3524-ac88-a75a7ffbf4e7 | -6.9544 | -43.5275 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d21c6e0d-52ab-3047-946b-c567621be751 | -5.963 | -39.183399 | 2024-12-24 00:04:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 18650000-3760-3df3-a072-95b8ad4eaed6 | -3.9048 | -46.097198 | 2024-12-24 00:04:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bad3c51f-43b1-35a2-9441-9e367540cb55 | -6.9679 | -42.989601 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2ff0b0de-38a0-3c0b-b4bc-af30d843e336 | -4.146 | -43.6325 | 2024-12-24 00:04:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe20aadd-36ef-3a15-a6f0-ec3f8c949aee | -12.7163 | -40.199001 | 2024-12-24 00:04:00 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cb35bde2-a301-3615-a53b-27218d63cb0a | -6.7892 | -43.571499 | 2024-12-24 00:04:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edf97fe2-5ffb-3441-97ff-bc4b2ed80e5c | -3.5265 | -40.768799 | 2024-12-24 00:04:00 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dd1b2087-fd00-381c-8562-56da74d315b8 | -1.5811 | -47.341599 | 2024-12-24 00:04:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e92f6e-ff4f-34a6-b15a-8690b77ad08f | -1.2198 | -46.8321 | 2024-12-24 00:04:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c4c9a5-23dd-3357-810b-7e8defba183e | -6.9673 | -43.5392 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57c48014-3119-3c09-a629-a095fdb721ab | -6.9777 | -42.9874 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| af791f5e-9773-381d-a382-c33f9fe35eda | -1.1818 | -45.976002 | 2024-12-24 00:04:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa02b389-1d30-3e48-9ab8-8403aab2a1cb | -2.7577 | -45.705299 | 2024-12-24 00:04:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a81f07e0-f461-3cd8-bb1c-ae33227588e4 | -10.8569 | -37.240501 | 2024-12-24 00:04:00 | METOP-B | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e18fb10-080d-3320-b8c5-32de2843bf33 | -2.8385 | -40.2826 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4c715a59-2ef4-3dfc-96d4-3bf683fec76f | -3.537 | -43.581299 | 2024-12-24 00:04:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a39d7923-30bc-3773-af6d-93ce113b1a2e | -2.7637 | -45.089001 | 2024-12-24 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acd90169-e9ec-3307-9ecf-7c6952320171 | -10.1311 | -36.5429 | 2024-12-24 00:04:00 | METOP-B | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 6765b827-f424-351f-903f-9f83f63865d5 | -2.9855 | -40.385201 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 51886cda-761e-3ad6-aa89-ace5cc56c4d6 | -3.895 | -46.0993 | 2024-12-24 00:04:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 083b6035-ce8d-312f-abab-fceebdecd5f4 | -2.3101 | -45.591202 | 2024-12-24 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb3efd59-22b4-3c36-a2bb-aa1a338cbf56 | -2.8404 | -40.291302 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c42bb56d-97d3-3345-95ab-cd067f28728f | -12.7179 | -40.206299 | 2024-12-24 00:04:00 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4cfa447f-1bda-3c6d-a9ae-e18836c68b64 | -9.3682 | -35.993401 | 2024-12-24 00:04:00 | METOP-B | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb233fa7-4b4b-34b3-8ee0-f2c8d8aaba9f | -1.5792 | -47.333401 | 2024-12-24 00:04:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a207921c-97ba-3185-95a2-8ed6085fd18c | -8.6127 | -35.097 | 2024-12-24 00:04:00 | METOP-B | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c04d34a1-db4b-3d18-b8cd-5acbca490cbd | -2.8287 | -40.284801 | 2024-12-24 00:04:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 41e2aad1-d390-34a4-98fc-cfdd60e46005 | -2.8647 | -46.736 | 2024-12-24 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b427dbec-3beb-3e92-beda-7de0b052fa66 | -10.5355 | -37.020401 | 2024-12-24 00:04:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8583d48-531b-3a16-bf30-b3706b407e0d | -2.9354 | -49.412102 | 2024-12-24 00:04:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7012390d-bc99-364a-ba9a-d10eca46f6a7 | -4.5329 | -45.823399 | 2024-12-24 00:04:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d17f59ff-7461-3843-90ac-a0d295a75470 | -2.6491 | -46.093498 | 2024-12-24 00:04:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0221cd5-65af-31d4-b612-2953800b5a35 | -13.3986 | -40.434101 | 2024-12-24 00:04:00 | METOP-B | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b6d604d-1fce-3925-9cab-b94a23f86c43 | -12.1826 | -41.3498 | 2024-12-24 00:04:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3edbade0-abca-396d-81d3-bcaed5d14a05 | -6.9446 | -43.529701 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c31a973-0817-3c43-adda-a723cc068ca6 | -5.9609 | -39.174198 | 2024-12-24 00:04:00 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5e586205-04bd-30fc-a11b-86ff404a2614 | -2.7653 | -45.096001 | 2024-12-24 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 060f8ef4-5f86-355c-9b6c-a5dfbd284dfb | -2.8049 | -48.683899 | 2024-12-24 00:04:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 452baf1e-d5fb-31a5-b995-e37a36ea50cf | -0.932 | -46.8792 | 2024-12-24 00:04:00 | METOP-B | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd0c776-4546-3349-9418-8f28e04186fe | -6.9663 | -42.9828 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e337b61f-2b83-36de-9400-32a88cffce31 | -2.8531 | -46.730099 | 2024-12-24 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2955b0-7124-3133-b812-c45a2755e7de | -1.4648 | -45.815102 | 2024-12-24 00:04:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7fe7f1cf-0cac-3f8e-a901-5fc551c86fdb | -2.7622 | -45.081902 | 2024-12-24 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da534940-f1b2-370f-bd94-0c67de86debb | -0.3223 | -48.419601 | 2024-12-24 00:04:00 | METOP-B | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3228891-a439-3ae2-9974-076dd597ffe2 | -12.7146 | -40.1917 | 2024-12-24 00:04:00 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a74e8ff3-b2f5-32fa-9e7e-07dced78b1fe | -6.1963 | -42.628201 | 2024-12-24 00:04:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1db2c2ce-c350-3d01-8f61-fce031b66faf | -3.1869 | -45.967701 | 2024-12-24 00:04:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 025cf25c-1954-3edd-b90d-832ade72c5b0 | -6.9771 | -43.536999 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4e71ffb-b2ce-37ad-af21-44ece78afdb1 | -6.9887 | -43.266399 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e9fc77f1-089f-3635-9aec-553f8a25791c | -6.2061 | -42.625999 | 2024-12-24 00:04:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f654ee5-0ce3-38ec-8049-c89fc7d19cc2 | -7.2395 | -37.4263 | 2024-12-24 00:04:00 | METOP-B | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 466fc970-4004-325f-8638-b9c7175116cf | -1.4517 | -45.802898 | 2024-12-24 00:04:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b82d06f4-13dc-322f-8db0-00ea19c319cf | -6.1566 | -38.953201 | 2024-12-24 00:04:00 | METOP-B | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca99dc78-90da-331e-a7be-76f1f76d7e56 | -4.5312 | -45.8158 | 2024-12-24 00:04:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1b652ee-b86e-356b-827f-eb174e652925 | -1.2181 | -46.824299 | 2024-12-24 00:04:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ceaead-47d0-36f2-a934-9ad67f6a3aa6 | -6.9657 | -43.532299 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a389dd2d-b58f-3257-a4e0-f2d862d9abc8 | -2.9638 | -40.290699 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e0accf33-0936-34f0-a296-93f8dedfdeef | -6.6902 | -39.119499 | 2024-12-24 00:04:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 55e54888-2a12-363b-a325-a716074407b7 | -6.9761 | -42.980598 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2f60edd5-7ef6-3799-b7b3-98542d92ad19 | -9.365 | -35.980499 | 2024-12-24 00:04:00 | METOP-B | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4790361a-8d85-3177-909a-35d8b8d81719 | -6.9431 | -43.5228 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3542431-83a9-33c2-8549-b3cb0aefd6a3 | -6.9872 | -43.259602 | 2024-12-24 00:04:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1062c5ea-165b-3a51-ba5e-7c05e78a0d7f | -1.4729 | -45.805698 | 2024-12-24 00:04:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44da615c-3c64-3405-be92-3408131cab29 | -2.9953 | -40.3829 | 2024-12-24 00:04:00 | METOP-B | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5b42c62c-15ba-3bb1-bddb-0e17facb4738 | -6.1979 | -42.635101 | 2024-12-24 00:04:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a202108c-79c0-3027-9854-dc2656d0d8fa | -6.686 | -39.101398 | 2024-12-24 00:04:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f0610f43-fa43-3091-8c4e-19c051f9ea7c | -5.2634 | -40.659199 | 2024-12-24 00:04:00 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 578da578-d2a9-3cad-af99-a5adaf9d41d5 | -10.5329 | -37.009701 | 2024-12-24 00:04:00 | METOP-B | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 963b2bd2-f3de-3e00-b419-412fc53d0792 | -6.9786 | -43.5439 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6f5fe3-4fed-36ae-84ae-85fda498b3b3 | -4.5114 | -42.059502 | 2024-12-24 00:04:00 | METOP-B | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 293360cc-4c58-31ed-a97e-852b4932a413 | -6.9559 | -43.534401 | 2024-12-24 00:04:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e614da17-e66e-3f83-9115-0548177d4c55 | -2.8874 | -40.271599 | 2024-12-24 00:04:00 | METOP-B | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 74e5f6b9-563b-3c2d-a9e7-685ea2dd4e49 | -4.1475 | -43.639301 | 2024-12-24 00:04:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 674a7c83-732c-3de2-b6d2-c558cbe22bd6 | -3.2944 | -45.850101 | 2024-12-24 00:04:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea462bd6-f28a-3bfd-8951-b8f0b07c4349 | -2.3117 | -45.5984 | 2024-12-24 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4120bc-5ca3-3e3b-9ff5-cddb6a7fe552 | -4.9424 | -41.327202 | 2024-12-24 00:04:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 976a40be-d90b-3fbf-84dc-b780d4dac798 | -2.0412 | -46.457298 | 2024-12-24 00:04:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 663e6385-8fc3-3ee9-ba29-0c19824e28b8 | -6.2077 | -42.6329 | 2024-12-24 00:04:00 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8e6373a-7d4c-3f57-9f01-e96dadad6d36 | -2.352 | -54.567501 | 2024-12-24 00:04:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
