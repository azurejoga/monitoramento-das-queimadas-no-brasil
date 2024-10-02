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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fef7272b-cb4e-30dc-bee0-7426e8438167 | -20.0097 | -55.46602 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4409d3f4-6b54-355d-8593-c487b01b3b42 | -20.00433 | -55.47253 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e67d4d7a-9a33-3d0c-9b91-06820a905105 | -20.003 | -55.46228 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7838fe48-d016-3a18-a053-3c5534cdf386 | -19.99502 | -55.47398 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cf6dbb16-eb2f-3792-adfb-33961b362161 | -19.98569 | -55.47537 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 5479bada-0d38-3d91-8203-13be8ddb3de3 | -19.97636 | -55.4767 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 84c2b9ff-c0de-30dc-a018-55105b616a61 | -19.96837 | -55.48844 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a690b9f5-175e-301e-b6e9-2603bb849b68 | -19.7506 | -54.528 | 2024-10-02 01:24:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b114e86f-ca35-347c-a0a5-cf7baca35534 | -19.74932 | -54.51836 | 2024-10-02 01:24:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ee165379-1d76-329e-96b5-a0f1dea1378a | -21.88988 | -56.10881 | 2024-10-02 01:24:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56cdb104-34ce-31d4-bfd5-ef6951d456d1 | -21.35201 | -55.70176 | 2024-10-02 01:24:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bdd45033-6899-3e39-9495-d22b0bd6b72b | -21.35061 | -55.69041 | 2024-10-02 01:24:00 | TERRA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 149.2 |
| a23cc4c6-cc78-3fe4-9251-451a284b0311 | -21.34243 | -55.70305 | 2024-10-02 01:24:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5631a292-a32f-3198-bb73-9472ca52c3f0 | -21.34104 | -55.69179 | 2024-10-02 01:24:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5efd78e4-832b-3e56-8704-3368da554516 | -20.04882 | -55.96854 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.0 |
| a832e6ae-b975-3177-ada5-6b0edcf6a247 | -20.04064 | -55.98092 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| fe619560-7fe2-3fe3-bdb4-72d7aafc315b | -20.03925 | -55.96991 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 3e4c62c4-8042-3f69-8cbc-973ce361494b | -20.03106 | -55.98229 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| b5e3086d-cd9c-31f5-a5e5-ed7b24968b92 | -20.02968 | -55.97127 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 3cac9102-e906-36ae-8bec-271ebb8de3ed | -19.65442 | -56.47938 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 554be8c8-4676-3f3b-9280-7daa4348b4b0 | -19.65297 | -56.46782 | 2024-10-02 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| eaf5f030-969c-3ed7-bf28-35be838c0573 | -21.42252 | -57.24388 | 2024-10-02 01:24:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7ba9566a-fe13-314f-bfe3-ec87d6157e29 | -19.10604 | -57.4917 | 2024-10-02 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 7eed2c58-9772-3681-9243-87f5b60e15c9 | -19.10771 | -57.5057 | 2024-10-02 01:24:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| c7ba1cc4-cc4b-38c8-9f56-3d27c32d2f43 | -16.66 | -57.191399 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45ea3180-bdc1-3848-a53e-36fa330065a3 | -16.6616 | -57.198898 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a1ecee7-c1c4-3980-a71d-f78dfa68768c | -16.6632 | -57.206299 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 616d9f1b-9c0d-3728-b391-91a5fbbe362a | -16.690599 | -57.333099 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3e4208a-5cc0-3908-a7eb-394eea63509c | -16.6922 | -57.340599 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a243a761-40c7-366d-b255-fdd03e43e6bf | -16.693899 | -57.348099 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15ebd532-ad2f-3f44-87cf-3adfcd585edc | -16.695499 | -57.355499 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8697497f-35a8-3c9c-b487-3994bcb5238a | -16.7003 | -57.378101 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cc0146d-d5f0-3f05-ae54-5820c96c84d9 | -16.718201 | -57.460899 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c47b54b-7d18-30e4-804b-2f23a0f49929 | -16.719801 | -57.468399 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eed8e37c-1b99-3b09-a97f-d7b39833cd34 | -16.726299 | -57.498699 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb2ed724-6b83-3a77-93b2-fd1792a9c8bb | -16.7279 | -57.506199 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ce75533-7a71-3cea-8482-12f1d9e7c94f | -16.793501 | -57.8125 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23a8b5ac-35b2-3b7f-a136-3714a5b8e2d1 | -16.7952 | -57.820301 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79897342-591e-3c09-bf9d-9873ceb9e2f2 | -16.6518 | -57.201099 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4be89db2-cbd9-3569-82b6-bb1b14152846 | -16.6534 | -57.2085 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8ae669b-4bc4-3d32-8799-fbced9ee3749 | -16.655001 | -57.2159 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd67e1c8-9c9f-3232-8c71-82d7a8623fe0 | -16.684099 | -57.3503 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f8a1f0d-eaef-31f6-be2a-e948631d9b54 | -16.685699 | -57.3577 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 050dcf5f-ba5e-3730-84c8-f0b1d90fb205 | -16.6873 | -57.3652 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58f2bc14-0120-3164-95bc-50280059b645 | -16.6889 | -57.3727 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 857cd30b-7bfe-3e03-a37a-7e2795b6eab3 | -16.6905 | -57.380299 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d59b74e8-c91f-3712-844e-c6c2623308de | -16.783701 | -57.8148 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2eca0a07-b342-381a-8bae-4b560080fcad | -16.7854 | -57.822601 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 406cb3d2-8724-3dbf-9a22-df03367a44e9 | -16.3717 | -55.973598 | 2024-10-02 01:24:01 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f90d002c-e4f9-3c97-9014-e0aad4557bbe | -16.6436 | -57.210701 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7f0ef4c-7755-394e-ab01-6a6c8c35bf5a | -16.645201 | -57.218102 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ecfd789-2b94-35a1-9004-9f280d1090d0 | -16.6775 | -57.367401 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6490f5ee-a98c-37fe-9a86-d200894a6cbe | -16.6791 | -57.374901 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 852c05ca-35d4-3a89-8e03-4c67f041d212 | -16.6807 | -57.3825 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fceef3f-1b1f-327e-911d-6da58c32e65c | -16.698601 | -57.465302 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b48314d-ad80-35ca-8e44-75f90e607a8c | -16.700199 | -57.472801 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1bd19532-a82e-37c7-90e4-2adfa65bf585 | -16.701799 | -57.4804 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0018e0c0-3c1c-39d6-9928-c38eb225e3e5 | -16.773899 | -57.817001 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45aa70a0-be17-3291-868b-d66b0b31834a | -16.3619 | -55.975899 | 2024-10-02 01:24:01 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| da0503b0-1f7f-3683-9158-7e979bb5866a | -16.688801 | -57.467602 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5175b1e-4114-335a-afe4-1e1fec5314fa | -16.690399 | -57.475101 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8898f516-eee1-34ae-9810-d09024a36fbf | -16.691999 | -57.4827 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17bc5409-6da6-3563-8857-6359fc9633d8 | -16.7575 | -57.7883 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aeb5da68-9e62-3091-90eb-bee8fe742214 | -16.759199 | -57.796001 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0e69576-8ca1-342a-a283-0c0c9209b1df | -16.760799 | -57.803699 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d7afa04-ee42-38c6-8406-480ec716a2df | -16.762501 | -57.811501 | 2024-10-02 01:24:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba9e864f-5a02-3bfe-b333-74ee04cc74c7 | -16.6257 | -57.222599 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85c3d9b2-cbc8-3870-a27e-3d49506c4f3c | -16.6483 | -57.327 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 046d7548-3d79-3087-ad41-7b01591b340b | -16.653099 | -57.349499 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 94ee94f3-4110-3310-90b9-20f73d776481 | -16.6143 | -57.2174 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9bfc378-90e0-36c5-a4c2-9813e2809034 | -16.6159 | -57.2248 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 064ee230-0867-34a6-bd1a-e2b0ca23bdc3 | -16.6175 | -57.2323 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f87d1b68-ef4a-304b-98c3-bfc447a13a89 | -16.619101 | -57.2397 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ff9dddb-7505-37b9-93dc-b7c8db644754 | -16.635201 | -57.314301 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 043a50c8-c43b-34f1-bae5-46a4230f4026 | -16.6369 | -57.321701 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5dab17f-1271-36c5-99db-12d42c1c8f4c | -16.6385 | -57.329201 | 2024-10-02 01:24:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65dd1766-6720-3d45-a6fa-8d1c4ec601f0 | -16.6045 | -57.2197 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c881b626-2b2d-3e18-8d39-be51cc579649 | -16.6061 | -57.2271 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8699c8e7-efd1-3f78-bde0-cca9204ab48d | -16.6077 | -57.2346 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ec8be88-f514-32e9-b10c-4ceaba4880e3 | -16.609301 | -57.242001 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4bf266ef-00e5-3bcd-a9e7-3fdf50897c99 | -16.611 | -57.2495 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c93c6bc2-9744-399e-96de-37c00077e684 | -16.599501 | -57.244202 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4af1aaff-2963-3c20-9a37-4537900e6292 | -16.6012 | -57.251701 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a565fa6-1fba-3f33-8325-b1244c8fb32b | -16.6157 | -57.318699 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d1e7ef7-8c1d-3e3a-9333-f7721353922a | -16.6173 | -57.326199 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89f5ba27-f690-3984-9366-31929d2b3bc8 | -16.6189 | -57.333698 | 2024-10-02 01:24:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f16d6a3-41b6-3b43-a4f0-f28a38e7c05f | -16.142799 | -55.412998 | 2024-10-02 01:24:03 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d09b754a-8097-3de7-8828-ab6388b34085 | -16.1444 | -55.4202 | 2024-10-02 01:24:03 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc1089bd-1d8a-3864-b23f-b9181db4d196 | -16.131399 | -55.408298 | 2024-10-02 01:24:03 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed917d98-5646-3f75-9be9-b70c9593b50c | -16.132999 | -55.415401 | 2024-10-02 01:24:03 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5ecd6b8-3557-3c66-8598-5678ad892a89 | -16.1346 | -55.4226 | 2024-10-02 01:24:03 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 232f921c-1033-3aff-b2b5-6c165f0e451e | -16.5277 | -57.291901 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9c2b8c4-39df-3215-bc03-d91c65923462 | -16.529301 | -57.299301 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 399fd759-737c-339e-9c15-9b6c8f48a02b | -16.5163 | -57.286701 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51f0c277-ecca-305c-b12b-843a3afa1c19 | -16.5179 | -57.294201 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce50605a-c8c8-3856-9265-8e54c57be206 | -16.519501 | -57.301601 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f541e24-47ca-3a69-83e8-904f9d940105 | -16.5049 | -57.281502 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 238c5898-7c48-3373-9767-cfc22fe9afa2 | -16.5065 | -57.288898 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3414d0a1-567b-3f90-974b-beb58e5cada6 | -16.508101 | -57.296398 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1655523b-31dc-3431-99c8-567dd9fa59e5 | -16.509701 | -57.303799 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README28.md)
