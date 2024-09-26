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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5762be0b-5076-368b-8c74-31981a45c58c | -12.79012 | -51.17891 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 574d49d7-886c-357a-847c-f4ecd4ab7aa3 | -12.78945 | -51.18383 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7cdf9e58-d924-36b5-91f3-c4e0b9d656fd | -12.78878 | -51.18876 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 98454566-f8a7-32aa-8225-b200e8534ffc | -12.78723 | -51.18687 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e61f0743-191f-3dbe-a41b-08621fd9ba25 | -12.78492 | -51.18818 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53f2f68b-ef54-322e-a669-e96b6b6e6caf | -14.91925 | -52.8598 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 359434be-6289-37cf-a127-daa6a8a95d3f | -16.10008 | -51.99854 | 2024-09-26 04:59:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 858debff-429c-389e-a8ad-ff2974867bea | -16.09625 | -51.99784 | 2024-09-26 04:59:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 825924f5-5684-33c6-8821-1321320ca80f | -15.68245 | -52.50689 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b589aaab-0870-3773-a3f7-5fac14081df2 | -10.07234 | -53.46983 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 216ca33c-d586-384b-938d-d807420e4cc6 | -10.07179 | -53.47348 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdda200a-9fbe-3cfd-8eb7-36ef862baf48 | -10.06952 | -53.46565 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d6b804-57f6-3f24-bcb5-0be004ee136c | -10.06897 | -53.4693 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d497e0e4-e4a4-38c1-8172-253bc4b00eee | -10.06842 | -53.47295 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7719d9a-e8fe-30ac-9f26-c17ae1d1fb5b | -10.06787 | -53.47661 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e5b4bde-a17c-327b-ad34-49697ecc6b50 | -10.06782 | -53.46574 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807e829c-2597-3a5a-9c6e-fbd7662ac820 | -10.06726 | -53.46939 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4f02fe2-728f-325f-b7d0-0fa229b91e6c | -10.0667 | -53.47304 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c216437-e3a5-3c9c-a121-e127bc875a0c | -10.06614 | -53.47669 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d1839e-0b38-3724-8166-7243de75e33b | -10.06558 | -53.48034 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02112a7b-21b7-38f5-8545-efbaa1f64cc1 | -10.06445 | -53.46521 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea6c8c0-942d-364e-a33e-42801cc00638 | -10.06389 | -53.46887 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3391caa-12d6-3e6d-8a27-1cf4c8603b47 | -10.06333 | -53.47252 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 073c2445-296c-32c9-93f1-9a0242c5d3a4 | -10.06277 | -53.47618 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbf342c2-6056-3f6a-92a7-c6db165980f4 | -10.06221 | -53.47983 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9e90a7-39d2-3c6e-9367-5a62efc3d01a | -10.06165 | -53.48348 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddc00c65-3b63-38b9-9a80-0e979cc7769f | -10.06109 | -53.48712 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4559d4c0-440f-35da-8235-c1f39c9f1a77 | -10.06052 | -53.46835 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8b8a102-7616-31d8-9e5d-30a5daeda3a2 | -10.05996 | -53.472 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d7b262d-5780-3f3a-95e6-0505a5077607 | -10.0594 | -53.47566 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de4af609-3318-3371-af34-9a8251be3db9 | -10.05884 | -53.47931 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0a26b61-7504-37f9-8a1c-c8ad8f3ae9f3 | -10.05828 | -53.48296 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49430454-47a9-3b51-966a-5eee96694f7a | -10.05715 | -53.46783 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ede2575-00bb-3bab-a629-d1685996d1c6 | -10.05659 | -53.47149 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fbbbd55-e7a1-3dc1-be58-bf59b27e64f1 | -10.05603 | -53.47514 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3455a78d-9c94-3b55-aebe-2a88462bb44b | -10.05547 | -53.47879 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40dcca2d-72b0-34e8-95e3-a681598a6edd | -10.05491 | -53.48243 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cc059f7-c77b-3d3c-aad3-4e42e06631a2 | -10.05378 | -53.4673 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 27531171-a21b-369e-84b2-63ac577e78c4 | -10.05322 | -53.47096 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b5bf781f-0868-3087-bc80-7a9428440f73 | -10.05266 | -53.47461 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 587b1aa9-6372-3b2b-b375-abf414821fa1 | -10.0521 | -53.47826 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c3485e6-8c0f-38fd-b366-920a0231f205 | -10.05154 | -53.4819 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0df6083c-823f-3e05-9ff6-70159d93a036 | -10.05041 | -53.46677 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e3d4005-ddf0-37a7-b1dd-caf2b86a607e | -10.04985 | -53.47043 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7a71107-9261-39ab-a82d-87fe9ade017a | -10.04929 | -53.47408 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bea43d8-bb3c-3094-9ff4-c00dae49d125 | -10.04873 | -53.47773 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c834177-dbe7-3c73-acf5-d8961ac1f094 | -10.04817 | -53.48137 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff172b9-f60d-3871-abb8-1e21cdb06534 | -10.04762 | -53.485 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9b45a60-9f41-3697-9e86-f407eb24ea65 | -10.04704 | -53.46625 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da9d6250-a8c7-31a9-a501-8f1ead914d55 | -10.04648 | -53.4699 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fd76ef3-8ffb-3bdd-8b9a-4b29c3d581e1 | -10.04592 | -53.47355 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e40263a-30ea-398a-9801-b95328117841 | -10.04536 | -53.47719 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b41274b0-9de4-3c61-b642-983a22f10a3b | -10.04481 | -53.48083 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e52287bc-66b7-35e7-9e60-abe5294af655 | -10.04367 | -53.46572 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ff552cb-754f-3a1a-874f-1a1dd9ef2067 | -10.04311 | -53.46938 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c1e7f4dd-0c55-37b3-92ab-2b0ca0b64cdf | -10.04255 | -53.47302 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 40fbb424-1623-341e-ba28-8041da3fbbad | -10.042 | -53.47666 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6ae35693-feab-3188-bb1c-340cd3bae0d5 | -10.04144 | -53.4803 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ada0458-4e1f-3fea-bb50-e4d5527d2227 | -10.03974 | -53.46885 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.0 |
| c6f83cf6-3428-3811-822c-105bffe60876 | -10.03918 | -53.47249 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b35d76eb-5f96-388e-8ae3-75bbfd341a04 | -10.03863 | -53.47613 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d67a8641-8f60-3333-8892-8b579945015b | -10.03807 | -53.47977 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fffa6dc7-8faa-36bf-99cf-c793ec50882d | -10.03637 | -53.46833 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 66ec87e1-462c-394d-b6e1-968db481d189 | -10.03584 | -53.49434 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 196fe1b9-5791-3c96-9b0d-2c56c9652da8 | -10.03581 | -53.47197 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d8fe764-21aa-3456-abb7-71ce4b49d6f6 | -10.03526 | -53.47561 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59990adf-a92b-3649-89ec-a704455c5284 | -10.0347 | -53.47925 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9bf5930-41a4-3497-a9f5-8db32477e76d | -10.03359 | -53.48654 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| be964a71-5cbd-3cfd-8653-bd1a0e8eae63 | -10.03303 | -53.49018 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 37806fe6-a7ca-3034-94b2-0f5a5fd1a184 | -10.033 | -53.46782 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 630b9677-05c8-3cb3-a99c-726ff64a88db | -10.03247 | -53.49383 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 0b235bef-11ba-33c0-b544-411b08e18dc6 | -10.03244 | -53.47146 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21e740fa-321d-3c37-8f81-63e2619e9e2a | -10.03192 | -53.49746 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5c605c66-cdf5-3cbf-a487-a09df6a8168f | -10.03189 | -53.4751 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91b34527-4c62-3e33-8366-c924114603c0 | -10.03137 | -53.50107 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7adc74f0-51ab-30ff-bb46-93315b3259fb | -10.03133 | -53.47874 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 191bf4e6-5d2f-3f79-91ed-087e10a0aaf7 | -10.02966 | -53.48966 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 85d1058a-d0a4-3371-bdfd-3365997a7c19 | -10.02963 | -53.4673 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 890c0bb3-e607-3ec7-ad38-d47f9edb8bb1 | -10.02911 | -53.49331 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54c7971d-9b78-34db-8f46-556785b9b9ee | -10.02907 | -53.47095 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd15d194-b309-3d32-831a-ec9eaf7ebbf2 | -10.02851 | -53.47459 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56d358ce-652d-3e5b-a1c7-fbdbc821c92c | -10.02796 | -53.47823 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e864ec9b-2ce8-38e9-a8be-d98e0604b3c4 | -10.02629 | -53.48914 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1954551e-9d0b-34e5-8ddc-e1465fab7159 | -10.02625 | -53.4668 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9388072-7b85-3d9f-b3c1-5534a43352c2 | -10.0257 | -53.47044 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff321999-db78-3041-8869-3d25cf482b1f | -10.02514 | -53.47408 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06ecfe5-d6b5-36cd-ac38-80c43ef75871 | -10.02459 | -53.47772 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18eab312-4cd3-3990-ab29-fc35f89413f7 | -10.02403 | -53.48135 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5165c8e-14fe-3308-92f2-fa7299ad30ef | -10.02348 | -53.48499 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0260edd6-9f10-3b5f-87a1-5549d585e264 | -10.02292 | -53.48862 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0dc642b-d29d-3193-bee6-1138c9b33ac3 | -10.02288 | -53.46629 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31200bc1-312f-38d6-938a-a037e7cb9561 | -10.02233 | -53.46993 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f4056a-32ab-3110-8bf9-f66bdc0244a3 | -10.02177 | -53.47357 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1625e3-7810-3268-9d09-d14d883fe6dd | -10.02122 | -53.47721 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8d70b65-ed8b-329b-b90f-21f30d36b018 | -10.01951 | -53.46576 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 894fb566-f993-3bd1-93fd-950fe7fcbc4b | -10.01896 | -53.46941 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c552e85-8c47-34d5-a31f-1b6349b80b45 | -10.01167 | -53.47197 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e81a0e-ebed-3d00-969a-6addffc11923 | -10.0083 | -53.47143 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825ee73d-d15f-3448-9864-ff668e020b07 | -10.00438 | -53.47453 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1feb7199-8c8a-3602-ba10-09ce5425577c | -10.43923 | -53.67857 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README122.md)
