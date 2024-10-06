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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2240215-c78d-3ac9-ad6a-c5610063a5b6 | -13.40524 | -61.9522 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4e285e2-a56a-3cd1-af3c-7af5641b7fb9 | -13.40458 | -61.94811 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d065ab3-3a85-36bc-ac6e-68270c2bf4a7 | -13.39935 | -61.95511 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f70b18-1aa5-3a87-a88b-a4b5fd2d2329 | -13.39911 | -61.94744 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07224156-8ea4-3203-9ffc-7e868d38516c | -13.39894 | -61.95871 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8450c2fc-6a91-3914-b058-83d2e25ec459 | -13.39365 | -61.94676 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d8f098b-a7c9-3037-b093-d90daf37221b | -13.38818 | -61.94606 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8e811c1-2348-310d-a2a6-380f7a7a955b | -13.38774 | -61.94965 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 060ea295-2e54-3787-aae1-01d661f0cc8e | -13.38731 | -61.95322 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d81b72a6-f8c9-3e0f-8027-05fa7d8b4395 | -13.38688 | -61.95682 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a2a5127e-72ac-3a62-a399-5f20f7f17497 | -13.38644 | -61.96041 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 36d5786f-11e9-300d-99b3-53fea3809341 | -13.38601 | -61.96399 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24a0e43e-17e9-33a2-9bf8-0354a3aca5a1 | -13.38184 | -61.95256 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ef0dd20-f554-36e1-952d-66244acca278 | -13.38141 | -61.95614 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8dce8910-820d-3750-8388-5fa43cf2c27b | -13.38098 | -61.95972 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a32b187a-8d8d-345b-acc6-9a45a9c716ef | -13.38055 | -61.9633 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bee2bd8b-8c3c-3520-b2c6-554c21b74c84 | -13.42541 | -61.92176 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c50e8b3a-e8bc-3bd6-b2cd-3cda6d85b412 | -13.42499 | -61.92537 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0c52484-45de-3a9c-b62a-c06aefb68c86 | -13.42456 | -61.92123 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3463f44f-3e4e-3685-9361-c9df78081ace | -13.42411 | -61.92484 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 422f252d-ab34-372b-96c8-bfcd91180636 | -13.41227 | -61.93073 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8178dbf-95bf-36fb-9488-1cfb1d9f1a45 | -13.41183 | -61.93432 | 2024-10-06 06:01:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ae09c97-e722-39e1-a438-9cdfa0c21419 | -12.87314 | -60.51532 | 2024-10-06 06:01:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5351e1fa-1cf1-361d-9b96-77b0fdfdebec | -12.87255 | -60.52052 | 2024-10-06 06:01:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8aa8c30-5ee8-3cad-9764-3e64d046b8d6 | -12.98328 | -62.67997 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47aee8c8-f4a7-3475-9562-6f11eeb9668d | -12.98288 | -62.68315 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf39758e-19e4-33bb-a6e0-f1216473bc64 | -12.9773 | -62.68567 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03ea5988-d59d-3da8-914a-05066d8c7e77 | -12.97173 | -62.68819 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b62e7457-9c72-3996-afa2-e784c9ba0400 | -12.95934 | -62.66084 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 546b7092-8059-3d0e-8abd-90db3f6961ce | -12.94442 | -62.47917 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 981d9d52-2d78-385b-be16-0dd47e6a9b3e | -12.93957 | -62.47521 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 853d828d-7d85-3e68-ac08-6a4043ecd85e | -12.93918 | -62.47849 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e742b648-7acb-3c83-8169-6d760fd391c1 | -12.93879 | -62.48175 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4c05908-1a1f-3283-9497-0034ff23d7d2 | -12.93354 | -62.48107 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1897fc3c-d23b-3b0f-a1d7-3982fa2a092f | -12.93315 | -62.48433 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f8732ab-ca47-34df-ba20-54060e76260e | -12.88373 | -62.45065 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fa36d7a-93c8-3e2a-9dcc-cbda8c84e5ba | -12.87848 | -62.44999 | 2024-10-06 06:01:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25278072-649f-34c9-aa7e-bc86383bce6b | -12.71443 | -62.95303 | 2024-10-06 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9157e8f0-97c7-3879-83fa-9c0cf84ce41e | -12.70936 | -62.95237 | 2024-10-06 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5b0914e-e8f2-3484-af06-f17650d081d3 | -12.70899 | -62.95537 | 2024-10-06 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82e575d5-701a-3330-b314-35afeaf1b7c4 | -12.70655 | -62.93369 | 2024-10-06 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85cca99f-3bc1-37db-aa0e-bf0046ef13bd | -12.70617 | -62.9367 | 2024-10-06 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60e8be3d-175a-3c2c-b995-6e986dd8c17e | -10.45 | -50.7 | 2024-10-06 06:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d45a4f8-834c-3c50-ba54-e6cdb656fc6b | -10.42 | -50.69 | 2024-10-06 06:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d49f47b1-9ce6-3267-ab90-d4b922158733 | -10.45 | -50.76 | 2024-10-06 06:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18b1d7b7-cbf2-3a50-ade8-712d686cbf4d | -10.42 | -50.75 | 2024-10-06 06:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea5dc0a-d352-3acd-a654-a9cd8f541af8 | -13.3786 | -61.9582 | 2024-10-06 06:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 72fcd40d-df34-38fb-b1f8-59235f8c48b4 | -17.1182 | -57.4039 | 2024-10-06 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 3733e532-88d6-3df3-91ee-0b6fd817b198 | -17.1185 | -57.3834 | 2024-10-06 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| e98441be-1567-34a1-9b5f-f25b604a85e4 | -18.6387 | -57.2785 | 2024-10-06 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 031eb004-a593-343c-a924-f00d5629bbfa | -18.6586 | -57.2759 | 2024-10-06 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| e882dfdd-515c-325f-a642-64d3fcea1c69 | -18.659 | -57.2552 | 2024-10-06 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| f5f63fc2-b97a-34a9-bd4c-6d0c59c404de | -13.3976 | -61.957 | 2024-10-06 06:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 115f4550-7d4a-3ea9-9dd4-0516dfe14a6c | -17.0116 | -56.7186 | 2024-10-06 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| a94d8e65-c998-3e30-8ae9-f1614780d00f | -17.012 | -56.698 | 2024-10-06 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 3eb7cf2c-53c0-39bc-bf00-ad717ca8a94c | -17.1185 | -57.3834 | 2024-10-06 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| e4b5a5c1-fbc4-324b-a779-d776b2dac9eb | -17.1182 | -57.4039 | 2024-10-06 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 963dd8f9-ba24-313d-8084-d8f850db4903 | -17.0985 | -57.4062 | 2024-10-06 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| cf521d4a-ba66-3102-ab40-27738786ac8b | -18.6387 | -57.2785 | 2024-10-06 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 075f103e-14c8-3202-85a5-b6f7e50f0517 | -18.6391 | -57.2578 | 2024-10-06 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| eca636f7-0029-3c9e-8d67-426873642d7b | -18.6586 | -57.2759 | 2024-10-06 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| a68b0f75-b365-3488-8432-8e763df8360d | -18.659 | -57.2552 | 2024-10-06 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 70ed0a4d-b708-35ff-ac31-eabc84d91d14 | -13.3976 | -61.957 | 2024-10-06 06:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f5cc03fb-1fe1-3f78-9a6a-6475aa551f13 | -16.8238 | -57.4584 | 2024-10-06 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 6994fbee-9f34-39c2-ab4c-c28d8e619908 | -16.8241 | -57.438 | 2024-10-06 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 4de50d4e-85d0-3fa3-a8bf-df78d5b87e81 | -17.0003 | -55.0817 | 2024-10-06 06:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a8f7ec23-41fe-35e3-ad4e-ffac1db297f1 | -17.0007 | -55.0607 | 2024-10-06 06:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 150.4 |
| e0cb2b97-e9b9-3315-9680-b89b4756b418 | -17.02 | -55.0791 | 2024-10-06 06:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 60d3e9cf-ce0b-3d20-ac5e-f3a1c65a8a5e | -17.0203 | -55.0581 | 2024-10-06 06:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 754d552b-9db1-3765-9139-6e80f8b50681 | -17.0207 | -55.0371 | 2024-10-06 06:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c2decf31-7f79-3b7f-88f2-a73e33152c84 | -17.0116 | -56.7186 | 2024-10-06 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 1e440786-d221-3ebc-8781-ee0dcbc29b33 | -17.012 | -56.698 | 2024-10-06 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| d73c9563-0bb4-3642-afc9-26bfd4488ce4 | -17.0989 | -57.3857 | 2024-10-06 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| a4d4c793-ce09-3b2b-96fc-e15e7f7b23a1 | -17.0985 | -57.4062 | 2024-10-06 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 4811f0ed-51ec-360e-807d-c4d5bd866e8a | -17.1185 | -57.3834 | 2024-10-06 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 61e9afe5-ff6d-3032-8cf9-3888863283f5 | -17.1182 | -57.4039 | 2024-10-06 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 2dc6210d-1803-3222-9176-0f5625cf755f | -17.812 | -53.7859 | 2024-10-06 06:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f08839c4-8c03-3c81-a464-c166ffbf8d28 | -18.6391 | -57.2578 | 2024-10-06 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 69eb780f-0fbb-3b3c-b4d0-88d5ce26211c | -18.659 | -57.2552 | 2024-10-06 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 3c86b2ce-9e64-3c3e-8ce7-2dfbdbf34a29 | -18.6387 | -57.2785 | 2024-10-06 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| f3a6dbcd-29fb-3e5b-a97e-7e78e500c747 | -18.6586 | -57.2759 | 2024-10-06 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 29e5c477-70f3-333b-b49a-d49ed28d194a | -20.4503 | -51.307 | 2024-10-06 06:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 245.8 |
| c7ef0fda-8a26-3418-b87b-5f41cc52d0e9 | -20.4707 | -51.303 | 2024-10-06 06:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 676.1 |
| ee8c2db0-b116-370e-ae76-a90094bea11c | -20.4712 | -51.2806 | 2024-10-06 06:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 357.0 |
| 4cf37500-24da-32a7-ad4e-27efc08200f9 | -20.4508 | -51.2846 | 2024-10-06 06:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 182.1 |
| 58848e31-9139-368b-b37b-065db4967133 | -7.46769 | -72.68573 | 2024-10-06 06:52:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f7dd53d-f243-355c-879d-9168fdd6cc16 | -7.46716 | -72.68976 | 2024-10-06 06:52:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9f083b60-4dd1-3e62-98d1-8625f3fc5609 | -7.46192 | -72.68515 | 2024-10-06 06:52:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f36322f0-37f5-3abb-8a08-53e17f579164 | -13.3976 | -61.957 | 2024-10-06 06:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 58380407-df55-3dfb-9b6d-b846be277cf7 | -16.8238 | -57.4584 | 2024-10-06 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| b85cd99c-0bdf-337e-ae6f-75e921193e3e | -17.0003 | -55.0817 | 2024-10-06 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| b52d9aa4-0cfb-3826-905e-bcd3610cc4fb | -17.0007 | -55.0607 | 2024-10-06 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 250.7 |
| f9ee3ea0-479f-3d5f-8d51-b3ca27715672 | -17.02 | -55.0791 | 2024-10-06 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 331.3 |
| fd964b18-4b02-3cc7-b6cd-b9ce24d45491 | -17.0203 | -55.0581 | 2024-10-06 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 600.8 |
| 5dd8db49-c2fc-300a-a3a4-6ea8047d0019 | -17.0207 | -55.0371 | 2024-10-06 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| a673b54b-f1ef-324c-b8d1-60909a31a825 | -17.0116 | -56.7186 | 2024-10-06 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 70ce1bf6-51b7-388a-a0d7-6ac48aa87d52 | -17.012 | -56.698 | 2024-10-06 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 3491e1a9-278b-3255-aaad-7e085104d632 | -17.0989 | -57.3857 | 2024-10-06 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| b9083242-54eb-333c-985f-e058e6f010c3 | -17.1182 | -57.4039 | 2024-10-06 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| a0a61085-553a-3a93-a02a-0fe7cd704522 | -17.1185 | -57.3834 | 2024-10-06 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |


[Clique aqui para ver as próximas entradas](README156.md)
