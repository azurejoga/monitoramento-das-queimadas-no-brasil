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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 426af56f-0171-3780-9b8f-ba21cc7ccea8 | -1.4945 | -54.1962 | 2024-10-24 01:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 379dbae0-ba86-3817-828a-283db4b18c57 | -1.4945 | -54.1761 | 2024-10-24 01:45:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| e18795cd-5dd8-333e-82e2-60fab9d71182 | -1.5504 | -53.6931 | 2024-10-24 01:45:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 17aaf15b-50e6-39a9-9b35-b9f0c3a343d1 | -1.5878 | -53.3089 | 2024-10-24 01:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8dd31f25-d32e-3708-bac5-b4a4f0cbc3bb | -1.6062 | -53.3087 | 2024-10-24 01:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 1c743c81-210f-3e53-8427-f40af59f06f5 | -2.9578 | -50.4198 | 2024-10-24 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a8719894-2a73-3a84-8e7c-7cdcc498f069 | -2.9763 | -50.4193 | 2024-10-24 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 36df2998-7caa-35ae-973f-d86b0344df77 | -3.0745 | -53.8252 | 2024-10-24 01:45:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5d4e0eb0-dfd4-3c5b-a287-a92256e3813e | -3.1101 | -54.1661 | 2024-10-24 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| aa58b7bc-604b-3c72-9f05-d7355b214d04 | -3.1102 | -54.146 | 2024-10-24 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a155967b-596f-3aa6-b191-7550db58a74e | -3.1606 | -50.4766 | 2024-10-24 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| cd03086c-078d-311c-aa21-0a6b08714a52 | -3.1607 | -50.4556 | 2024-10-24 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 37ae973c-c35b-3d36-a096-610951cb2ce0 | -3.7066 | -41.6997 | 2024-10-24 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 0a8962cd-b730-33fb-84b5-3b0d5d48bfe9 | -3.7068 | -41.6758 | 2024-10-24 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| b492111a-5040-3445-8697-aa6080e9a6e7 | -3.7254 | -41.6987 | 2024-10-24 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 002b2587-994a-3402-96aa-79301ea46f36 | -3.7255 | -41.6748 | 2024-10-24 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 0c16fdf2-7ad7-309a-b93e-80b29afc4d4c | -3.6612 | -54.2715 | 2024-10-24 01:45:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b4f9aba1-2442-38c2-8907-ecc1f55c8488 | -3.9396 | -46.4229 | 2024-10-24 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 97e5c3d5-63f3-33e6-8d35-725fc21f97a2 | -4.758 | -46.4033 | 2024-10-24 01:45:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 66eac21d-4ff0-39c8-aa38-7fada7d74067 | -7.481 | -63.5577 | 2024-10-24 01:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 21ee51d9-d2b9-39a0-bf5d-d68a88e73899 | -10.1969 | -53.8822 | 2024-10-24 01:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 16606dee-46d9-3f80-bf41-98eed306622a | -10.1971 | -53.8617 | 2024-10-24 01:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a7a295eb-d5f4-34a5-8d4b-46e0da84d481 | -12.6914 | -43.8484 | 2024-10-24 01:46:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ee0b2472-f5ee-341e-8aa4-55e41c46705b | -13.7417 | -54.0682 | 2024-10-24 01:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 95ab6bd5-ee43-3a06-b246-bb40c95a98c1 | -13.742 | -54.0475 | 2024-10-24 01:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 9d334dc5-86f9-3203-b0ab-6b8b06e6a92e | -13.7609 | -54.0661 | 2024-10-24 01:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| fa5507a4-caed-39ac-9b51-c100732fb5ee | -13.7612 | -54.0453 | 2024-10-24 01:46:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5693881a-6c3f-3bda-a8a0-8bf24131f1fb | -16.9596 | -57.5245 | 2024-10-24 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 7eaedd23-aaa4-3bcc-93a1-308bee319ffc | -17.0011 | -57.3766 | 2024-10-24 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| af376754-d8a6-33bc-9d57-8249d5b157d8 | -17.0207 | -57.3743 | 2024-10-24 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| e46866d5-108b-37ab-937d-4bb9b85c36d2 | -17.2383 | -57.2462 | 2024-10-24 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| e0947623-fd23-3136-85b3-7bcc78bd3378 | -17.2579 | -57.2439 | 2024-10-24 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 4307904d-9206-331b-98ee-d03f48c8f3bb | -17.7062 | -57.4774 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 85071ede-8830-3d75-b8c4-e1cc8efc6825 | -17.7637 | -57.5732 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| d62b0061-9d67-35d0-b029-6dca04024d24 | -17.765 | -57.4909 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 69fcb15d-e6ff-3656-8340-36ff155e52b2 | -17.7831 | -57.5914 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 2e0fbd64-bcd6-319d-89ab-86f97135239e | -17.7834 | -57.5708 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 7be18b8e-e79c-3870-bf56-115dc53485fd | -17.7841 | -57.5296 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 2be9240a-2a1a-3b14-b2e4-e3d3c025ed9b | -17.7844 | -57.5091 | 2024-10-24 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 9d2fe31c-81d3-331c-8694-bd5dc33b3b64 | -18.0837 | -57.3076 | 2024-10-24 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 49226eb9-6190-3384-84a2-254c55de099d | -19.548 | -56.6143 | 2024-10-24 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 336f0142-06be-315d-9a58-8a60758c9562 | -19.5681 | -56.6114 | 2024-10-24 01:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 28c5230e-53d1-3e7e-b0aa-330a5727ef75 | -23.795 | -55.2753 | 2024-10-24 01:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| c21ff25a-cd36-3d23-9d1b-cc7b786e493c | -23.8155 | -55.2933 | 2024-10-24 01:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| b581211d-a325-3a18-a53a-5ed8436e1d0a | -23.816 | -55.2713 | 2024-10-24 01:47:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |
| 39970648-b5e5-3b98-9bf6-7ecfb60c6ace | -23.8371 | -55.2673 | 2024-10-24 01:47:17 | GOES-16 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 52.3 |
| 543be162-84e9-335b-9ef7-1441762b0b4d | -1.4762 | -54.1964 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 66dbbc28-681e-3161-b4c4-9f336f364008 | -1.4762 | -54.1763 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9d86ab46-0523-394b-8189-57b2f14664e4 | -1.4945 | -54.1962 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 225a2216-0e44-35d3-be92-6259fab97e96 | -1.4945 | -54.1761 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 53f577dc-02cb-39f2-b2e8-99c1f38dd79e | -1.5129 | -54.1959 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 0b5ef9db-a951-346c-a6cc-bfcd771d50b5 | -1.5129 | -54.1759 | 2024-10-24 01:55:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 965b17e3-9352-36dc-84bc-e39effcc58d9 | -1.5504 | -53.6931 | 2024-10-24 01:55:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 9111a73f-a147-36ff-b6c3-610d21e0abbc | -1.5878 | -53.3089 | 2024-10-24 01:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fc834e4d-e4c3-3a7f-b359-b8b2ab60abcb | -1.6062 | -53.3087 | 2024-10-24 01:55:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| c2b0b805-afa1-3149-a45a-d8e1e7376bca | -2.9578 | -50.4198 | 2024-10-24 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0e59c8bb-84fc-3c00-bfe0-ddc8c3391126 | -2.9763 | -50.4193 | 2024-10-24 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ffc1f4ed-ffdd-336f-a5f5-bcd29a4d43b9 | -3.0745 | -53.8252 | 2024-10-24 01:55:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2818be94-10ab-3596-bfe3-e046fa524768 | -3.1101 | -54.1661 | 2024-10-24 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b75154fd-4177-3cb1-9f3b-c05d2c5c1f0b | -3.1102 | -54.146 | 2024-10-24 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5a2191b2-92c4-34c8-989c-170c9ff8bc8f | -3.1607 | -50.4556 | 2024-10-24 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ca3228ee-bad1-3ab4-903c-bfe6aca18f7d | -3.7066 | -41.6997 | 2024-10-24 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 76882355-9dc1-3f95-a232-0fb43ed703ef | -3.7068 | -41.6758 | 2024-10-24 01:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| b554dd26-c813-32f6-8ae3-d5ee9001fa56 | -3.6612 | -54.2715 | 2024-10-24 01:55:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 38498dc3-0f8c-327b-a260-17f92b5574d4 | -3.9396 | -46.4229 | 2024-10-24 01:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d0e668ae-079f-35e2-94d4-7155ffbd3d5d | -7.481 | -63.5577 | 2024-10-24 01:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 75a0f44b-aeed-3106-b6e2-9eae5349e824 | -12.6914 | -43.8484 | 2024-10-24 01:56:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3227e306-e3eb-3ea1-9ff4-10396b36bfa5 | -12.6918 | -43.8247 | 2024-10-24 01:56:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9372bef2-4a74-30f2-b8bb-d00d270dacd1 | -13.7609 | -54.0661 | 2024-10-24 01:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a8ac5857-9834-371f-899a-0b3704bf6ea1 | -13.7612 | -54.0453 | 2024-10-24 01:56:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 61dad8b7-4d1c-3c4e-8ca6-6262f8030a46 | -16.94 | -57.5268 | 2024-10-24 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| aa06a16b-715d-3667-94d4-7e377d0fd911 | -16.9596 | -57.5245 | 2024-10-24 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 185f2a80-5b40-35b7-ada0-530c21f4e309 | -17.0207 | -57.3743 | 2024-10-24 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 7d81f9ca-b222-39f9-899a-a69407d67d35 | -17.2383 | -57.2462 | 2024-10-24 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| a2531119-924d-3d05-a071-f917acfae9c2 | -17.2579 | -57.2439 | 2024-10-24 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 0b67627d-55ff-3240-b922-5d1f68ba224b | -17.7844 | -57.5091 | 2024-10-24 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| b517a2e0-ee32-32fc-8390-32cb2a8bf3cf | -17.7831 | -57.5914 | 2024-10-24 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| ffff39a3-6e05-3d5c-8c72-df288e456ccd | -17.7834 | -57.5708 | 2024-10-24 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 9d344b7e-9242-30f1-bd82-ee6619444a16 | -18.0639 | -57.3101 | 2024-10-24 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 92e7c623-fbc2-3d5e-be6e-ab115570b6e9 | -18.0837 | -57.3076 | 2024-10-24 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 2cd45693-c2cd-3ab0-965e-b2ee5398ad35 | -18.0841 | -57.287 | 2024-10-24 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| b63057f3-5db2-30b8-bb35-2a403e849e38 | -18.1032 | -57.3258 | 2024-10-24 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 0a050d8d-0f61-31cb-8e50-11ed46165560 | -23.795 | -55.2753 | 2024-10-24 01:57:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 672076db-bde7-32f8-ad28-3a92c3d7e428 | -23.816 | -55.2713 | 2024-10-24 01:57:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 71603c81-d063-3503-af10-af46e31cbb0f | -23.8371 | -55.2673 | 2024-10-24 01:57:17 | GOES-16 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 79ee75f1-b1ff-3fac-8f9a-64da65769680 | -1.4762 | -54.1964 | 2024-10-24 02:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a999e90f-4be2-3886-8b0a-196f101fec30 | -1.4762 | -54.1763 | 2024-10-24 02:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1acb37e8-19bf-3c93-be82-596672a7e3c6 | -1.4945 | -54.1962 | 2024-10-24 02:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 102e4c17-ed50-3bed-b6bd-f9df796cb2cc | -1.4945 | -54.1761 | 2024-10-24 02:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 352ba128-2f2b-317c-b011-56191966f786 | -1.5129 | -54.1759 | 2024-10-24 02:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 14fbf6cb-d717-3623-939f-ccfa71d5b17b | -1.5504 | -53.6931 | 2024-10-24 02:05:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b9fc442d-e61a-3bee-baca-fad60ea4b9ba | -1.5878 | -53.3089 | 2024-10-24 02:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2617c7ca-61a8-3550-bc52-f7e1391b9510 | -1.6062 | -53.3087 | 2024-10-24 02:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 06d9ce04-ad77-36a5-89f8-034b1a502618 | -2.9578 | -50.4198 | 2024-10-24 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a3fefcd4-849d-317f-9f5f-364d8031605e | -2.9763 | -50.4193 | 2024-10-24 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 936fda56-d16c-3ad5-9a7f-1e926ad688a7 | -3.0745 | -53.8252 | 2024-10-24 02:05:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7b44239f-2799-35cb-b82b-ad9af4b60fad | -3.1101 | -54.1661 | 2024-10-24 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 37c35e18-f352-3503-a662-e696eaaf85c2 | -3.1102 | -54.146 | 2024-10-24 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4abd506d-f5fa-3f48-8549-802b0a2859a5 | -3.1607 | -50.4556 | 2024-10-24 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b75940a9-5280-384e-8be6-266b8122c232 | -3.7066 | -41.6997 | 2024-10-24 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |


[Clique aqui para ver as próximas entradas](README13.md)
