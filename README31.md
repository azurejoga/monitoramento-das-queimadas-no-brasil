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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ae9dc6e-1088-3d7a-b5c6-ecc515001232 | -5.07796 | -47.87101 | 2024-10-24 04:32:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25a9850a-5106-3625-930e-f59f9b06b2a3 | -5.00791 | -47.64504 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffd36ec4-342e-3515-a6c9-a230ff8d6b66 | -5.43232 | -46.5632 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bd0bbb2-8b86-3865-aa69-9add1eaa9790 | -5.43178 | -46.56672 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f81fa0-ac3f-3f2c-bae9-b60754a9b696 | -5.42899 | -46.56268 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53321dd5-963d-37c5-871f-bfbcce482aa2 | -5.42566 | -46.56216 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a554fa81-4bae-342a-b40c-caa1ce767308 | -5.42511 | -46.56568 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abef8fb1-9c73-3218-ae9a-9a9677ec471e | -5.24913 | -46.6923 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63936b2e-cc90-3b6c-a1b3-22426e55847f | -2.1156 | -48.37608 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e17f0e-d5c1-3c51-b235-36f015b9a39c | -2.1128 | -48.37197 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9e10904-02fd-3c1d-a28a-1729ffa82d0d | -2.02554 | -48.40957 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2382b09-8a00-37b0-a07e-b60dcdbfb9cb | -1.8784 | -47.80958 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6793dc89-2f2e-317e-b84e-1845e5d6ba17 | -1.87785 | -47.81308 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eccc538d-82bc-300d-a4a4-d7d45247f70c | -1.87507 | -47.80907 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b12f3855-8553-33bc-8aaf-b1b583ebb1de | -1.87452 | -47.81256 | 2024-10-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72f82f1f-f8ff-36cf-aa71-eeb5592ae334 | -1.80216 | -48.05347 | 2024-10-24 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab4eccf6-cb04-3013-97ee-f4faa21a72b4 | -2.05714 | -48.67895 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 072482e0-d995-3e5c-9dd1-616cc1f1b198 | -2.05432 | -48.67476 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3822b383-6596-35e5-93f2-79ca5b597538 | -3.25476 | -48.78988 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e81a0b2-3ba8-3e4c-8033-859736896ed7 | -3.14687 | -48.56641 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c9f4b68-6756-3456-b4f5-662b78fb466f | -3.14351 | -48.56589 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfec2ac4-4553-3b88-b49c-125b5108bac7 | -3.12241 | -48.65465 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c2d5d61-9792-3163-86df-2c67ffeaf300 | -3.11174 | -48.60156 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7165170f-a1c5-31c4-896c-1a53b06bdf0a | -3.10893 | -48.59745 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88985e91-3de0-39db-be66-3bb20d104357 | -3.10837 | -48.60104 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2485d2ef-fa99-3b4d-b75c-4631e219fc07 | -3.45895 | -47.67089 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 18659f05-1f3d-3904-9f98-41f437568ab9 | -3.45841 | -47.67434 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 826678a6-8971-3b6b-92e0-7ae8f520eb68 | -3.17027 | -48.37659 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 853d2486-5a94-3033-a5a7-e08363f3b811 | -3.04866 | -48.05058 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 01db63b6-2724-3a60-ab8a-cc5b94f705ae | -3.04697 | -48.01809 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0883706-c385-35c6-ae6a-7ebd002423cd | -3.00872 | -48.08738 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 587b75d6-31d0-3d07-b8db-93c3713525f0 | -3.00816 | -48.09089 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55a8a03b-2da8-36c7-88e6-7da3a9b66b2a | -2.92123 | -48.03788 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84a33363-f017-3415-8281-d00783c5ef0a | -2.91069 | -48.06134 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f53ad1c-fc66-38c4-afaa-881ddec985af | -2.91014 | -48.06485 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a7d5602-0248-3a89-9828-9353df643831 | -2.90736 | -48.06083 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a630f1e-6aad-3da5-bdb9-b0f827d04d9a | -2.8928 | -48.28211 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7cbb951-8e5b-33ec-b96b-0e872116441c | -2.88946 | -48.28159 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a377557-64a8-31cf-8809-3591bdda7a69 | -2.18083 | -48.73924 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5be7c02-fee1-32a3-9953-e4bc4d0a8a0f | -2.92218 | -48.95935 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1393fbc5-6d9c-39a0-b3dd-ed4fb198051a | -2.88179 | -48.61327 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ba9cdac-bbd3-39a0-a39b-f927460bafa4 | -2.87841 | -48.61275 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b0483a7-3ce2-3848-bc2d-5dff76a060a6 | -2.77709 | -48.69719 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8d0396b-91f6-3cd1-ac11-a382bedabfc3 | -2.77652 | -48.70082 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01394996-4968-342d-82f8-5875c4ce206a | -2.7737 | -48.69667 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bfbb8f6-7cc8-3d1a-b2fa-cf01840deb3e | -2.77313 | -48.7003 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38525344-4b72-32d8-b3a2-5259fc94d9b0 | -2.6892 | -48.63893 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1f2cdb3-a9e9-349d-a3d1-c7ce29f3874f | -2.65199 | -48.49245 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87b95785-5b47-3bd5-8a5a-f4953fb23d1a | -2.63794 | -48.49394 | 2024-10-24 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65f5d648-3ed8-3170-8b58-1c2dd72762c1 | -2.52205 | -48.51659 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a690c42b-7e74-3c97-a011-1c8780b0e2a4 | -2.52148 | -48.52018 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ccbdf6b-546f-3b04-9760-423573242dc9 | -2.48655 | -48.48913 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39100d1d-23ef-3da5-9e29-21e91243eaa4 | -2.45282 | -48.48389 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 694feb36-0310-38cb-9787-dfba9cfa081a | -2.44944 | -48.48336 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21d47505-4e11-32b1-a8c7-b3e6223befe3 | -2.44664 | -48.47924 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03295927-51a2-3918-b690-890e2c32af16 | -2.44607 | -48.48284 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 587b26d4-4299-320e-9232-068e052a5b35 | -2.43753 | -48.53689 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02747644-ca40-3fa9-a5c7-1fba3bfdd566 | -2.43696 | -48.54049 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab136c87-17c5-3266-bfe2-c705a4719ee1 | -2.43358 | -48.53997 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e165279-831f-3a0f-97a6-3eda69692224 | -2.42241 | -48.50129 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8062d27-49c2-3b3b-b664-87af5bc0a4dd | -2.41903 | -48.50077 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4afc0c1d-9a13-35fd-ba9c-3483582bb1fd | -2.32799 | -48.5415 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 053a17e4-860b-3453-b24a-ce4b5736ac16 | -2.31171 | -48.51307 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40ca753-a9ad-31e4-9d14-26e064590d06 | -2.30833 | -48.51255 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86864ce2-529a-30b2-833d-a4a22f559df4 | -2.57692 | -48.04122 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36c0d737-1038-3a0a-9193-cc24685024a3 | -2.57156 | -47.96861 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 103c60ca-f674-34ff-953b-e801ef2006db | -2.56966 | -48.1301 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3eb38a01-f209-3bbc-bb36-f28ed8fa7482 | -2.46325 | -48.13532 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63baf428-a08c-30b7-a4d6-8a22931c5bc6 | -2.4627 | -48.13884 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4ce2a7c-6233-34bd-9ad4-19fb910b0eec | -2.41577 | -48.45604 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 412f5d04-4279-3465-b5a2-eb3f2bbd1297 | -2.4124 | -48.45551 | 2024-10-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da560c46-d42b-355d-b865-ada1b72c4250 | -2.35626 | -47.90944 | 2024-10-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a594b69c-8c03-346f-b257-b3c56b1ea2a6 | -2.32088 | -47.48433 | 2024-10-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3f5b4c4-4d5e-3336-bb29-9ec6ad0967f4 | -2.27856 | -48.44911 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b4a6ba8-32c8-309c-88b1-92676c62e9d0 | -2.278 | -48.45271 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad592907-b1cb-3a0b-b0fb-268fbff31171 | -2.16669 | -48.4245 | 2024-10-24 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f701e1ef-c62f-3aa7-9ddf-e959e6385a3a | -4.21229 | -48.03155 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8bb119a-c2be-3720-9841-74abd34308ff | -4.21174 | -48.035 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 487cf2ac-8eb7-3486-9678-250f5a79645c | -4.20953 | -48.02756 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eefbb751-8b05-3a6e-a4de-ec5459b432d1 | -4.20898 | -48.03101 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 005ace30-1020-3d1b-a5f2-338f9cbf2812 | -4.20789 | -48.03793 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b8e60b0-b565-3863-a294-8d3d15b65e4c | -4.20622 | -48.02702 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e1dd6c3-da4f-3994-b9c8-80d4db042265 | -4.20457 | -48.03741 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ac7dd6-21c9-3bae-a1fb-d38e31d64bba | -4.20181 | -48.03342 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa6fa3a1-f83d-31e2-80d3-4972bf847f16 | -4.1985 | -48.03291 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9d543a6-7685-3214-8b4c-eb285d1af45a | -4.19486 | -47.9896 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70c91bd1-1789-3e7c-a026-df0e0f4ed230 | -4.18108 | -47.99097 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c7aee3-9aec-364c-aa04-d496353864ed | -4.17777 | -47.99045 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56aa8305-6ad0-35c3-a762-f5f6d7c75c7a | -4.12835 | -48.26078 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 813d21f8-da80-3fd2-b998-1ce3fe3dc472 | -4.10728 | -48.24314 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 281700a4-8bb9-3487-a14a-c433efb7efac | -4.07845 | -48.27451 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7744bdc-3265-3815-975e-b55e03ada892 | -4.07735 | -48.23851 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a3c8916-f0b1-3eba-be8d-7fcee9a8057e | -4.07402 | -48.238 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69b1183e-b149-327c-aa8c-9c7966659c93 | -4.07235 | -48.29147 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff1cc80-53db-33ec-a77e-0335db97cc9a | -4.07013 | -48.28397 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db32a3b7-fad7-375a-a96b-bde8238424b1 | -4.06959 | -48.24445 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac9f184f-a2e6-3905-8aeb-df8014976d45 | -4.06957 | -48.28746 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93f3b460-103c-32c8-a21a-4252762a559d | -4.06904 | -48.24793 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa84853e-e9bf-3b9d-8251-06da8ae2ff00 | -4.06848 | -48.25142 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bf5dfd6-5ce7-3e45-a7e4-68c4fa1b105b | -4.06571 | -48.24742 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
