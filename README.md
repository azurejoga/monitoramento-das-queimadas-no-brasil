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
| b260eba2-1742-3e0d-87e6-4d48587fadb3 | 3.601 | -61.4184 | 2025-01-21 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9fb87746-ec73-3dca-b270-5363a1bce90a | 3.601 | -61.4184 | 2025-01-21 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 918d63a1-b1c4-3cbc-bf0b-16f1da8e914d | 3.601 | -61.4184 | 2025-01-21 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| dd7fa59b-6c65-3d31-9548-126f249178e7 | -6.5407 | -35.1917 | 2025-01-21 00:20:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 8b44d798-51e2-3e04-9bff-481e6c1a571f | -14.2142 | -44.7132 | 2025-01-21 00:26:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc93f2ff-8f01-3f22-8032-897ad0829a13 | -21.3708 | -48.974602 | 2025-01-21 00:26:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 861b0bc0-411c-3363-afb3-92b9f43ed0b0 | 0.7574 | -59.593498 | 2025-01-21 00:26:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 57b06040-a9d2-3cfc-869a-0b8c2c7abdc3 | -11.0275 | -45.041801 | 2025-01-21 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d08856c-e9b3-3a14-a605-2df07b80f0a9 | -16.6724 | -40.0686 | 2025-01-21 00:26:00 | METOP-B | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec268c00-dbfb-3d1c-9d8e-9385a6f04587 | -22.9219 | -43.717602 | 2025-01-21 00:26:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1cea072-aa16-3a30-b4bd-81ff5d09535e | 3.6094 | -61.369999 | 2025-01-21 00:26:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfc1ec3-3b8c-38a3-be8b-ce5705a6167b | -11.0373 | -45.039501 | 2025-01-21 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddc07d80-d782-391e-b71d-60f1e0bbd6b6 | -2.4289 | -48.049301 | 2025-01-21 00:26:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9134ad2-b4a9-38ae-90c4-3d625c0fb124 | -11.0353 | -45.031101 | 2025-01-21 00:26:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6cd5c9-0bf1-3428-9b1a-b02c652ba4ad | -21.369101 | -48.9659 | 2025-01-21 00:26:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 308c9583-e287-3375-92bc-32c32be9103d | 0.753 | -59.612202 | 2025-01-21 00:26:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1215aa10-07a9-32a7-87a8-45397c36936b | -19.216299 | -45.369301 | 2025-01-21 00:26:00 | METOP-B | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f9c9deb-5f7e-3096-928e-a753a12bc8eb | 3.5997 | -61.367699 | 2025-01-21 00:26:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 03bb466f-b6bd-31c7-b649-14f11d050b84 | -3.3833 | -52.7038 | 2025-01-21 00:26:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2196fdf4-4333-34bb-ac9c-a2dd37e2e6c9 | -2.4272 | -48.041801 | 2025-01-21 00:26:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8cd4e9-96e7-3d0d-8858-514685025bbb | -4.5577 | -50.1731 | 2025-01-21 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b88b78f2-6f95-3c11-9569-ab0c4113c355 | -22.9319 | -44.7365 | 2025-01-21 00:26:00 | METOP-B | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bff7add1-d6e2-3280-934d-a24eebe4eb4c | 3.6147 | -61.347599 | 2025-01-21 00:26:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c1af839-50bf-3afb-8a91-9a5c560093c6 | 3.601 | -61.4184 | 2025-01-21 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| db5bbf50-3d65-34bf-ba3c-924029c94647 | 3.601 | -61.4184 | 2025-01-21 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0df2a6d3-4947-3a96-892a-6401d7f3704d | 3.601 | -61.4184 | 2025-01-21 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9f7d7047-da0a-3815-a80f-b331b934d79a | -11.0201 | -45.059 | 2025-01-21 01:10:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e8680148-2c49-3e92-a951-8c4f889e33c6 | -10.1424 | -36.2761 | 2025-01-21 01:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| eb624bab-5b4a-35b1-a3fe-a053173fa2c5 | -11.0201 | -45.059 | 2025-01-21 01:20:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3c52c30d-58c3-3fe8-839f-e11c8b1d00fc | -11.0393 | -45.0564 | 2025-01-21 01:20:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1bf545ad-b549-3c57-a559-5f8145d9b921 | 0.7476 | -59.640999 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dfa27b18-8d30-3bc2-9009-b2babb8c1c82 | -21.1068 | -56.265598 | 2025-01-21 01:22:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 65b9f6f9-f4ea-3adc-9bc6-8959ab8f57f7 | 0.9975 | -60.5746 | 2025-01-21 01:22:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0d589a4c-c738-3b02-a4dc-9af05fdf59f5 | 2.646 | -60.4907 | 2025-01-21 01:22:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9b212eec-a12d-33e4-865a-75222788aa20 | 0.7362 | -59.645699 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 31d22153-a29e-3a61-88b9-1499ba9ec158 | -28.6605 | -56.054199 | 2025-01-21 01:22:00 | METOP-C | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 8bdd0f24-440e-3928-b14b-c70307a81029 | 3.6016 | -61.406502 | 2025-01-21 01:22:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4be97580-b902-3736-88f2-4f858bf1a9dd | 2.1472 | -61.002701 | 2025-01-21 01:22:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f5cd48eb-9a4e-3844-9313-faa23cd3b1cf | 0.8523 | -59.678902 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ba8e37cf-111a-3372-91c2-acfe72467038 | 3.5886 | -61.4179 | 2025-01-21 01:22:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1387da52-8f88-3ae6-b55c-38d4bff9f95f | 0.7378 | -59.638802 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 28904afe-1312-3611-a456-0cc6a066a374 | 3.6 | -61.4133 | 2025-01-21 01:22:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 162f2274-a7f5-3bd9-8966-6a25cc0f03ca | -21.1084 | -56.272999 | 2025-01-21 01:22:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| afdb262b-2eea-3c6a-a316-4a1b56119109 | 2.1456 | -61.009602 | 2025-01-21 01:22:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 63fc869c-0e59-3e31-bdb5-3f6a7dd704bf | 2.6444 | -60.497501 | 2025-01-21 01:22:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e63e0d5-58ed-344f-bcd3-c661e206a6e2 | 3.5918 | -61.404301 | 2025-01-21 01:22:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2a34d8-23d9-3cb9-91c3-777867ece8b9 | 0.746 | -59.6479 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8a50e20d-84f4-34ab-8cd5-86ee8459a29f | 2.1559 | -61.818298 | 2025-01-21 01:22:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f83ae15c-2012-3348-9cf9-2dacbeafd1d7 | 1.1307 | -59.543598 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 489d5810-db86-3a44-9cd7-0777e25efcb0 | 1.1209 | -59.5415 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7442de69-3649-34be-a3e0-c41dd77d88ed | -28.662201 | -56.062698 | 2025-01-21 01:22:00 | METOP-C | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 6caf00d9-d6f9-33a7-9de8-8e9ecaeafa8c | 0.9991 | -60.567799 | 2025-01-21 01:22:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2333cdc8-9cc9-3c14-8c60-f91118df4e6b | 2.1575 | -61.811401 | 2025-01-21 01:22:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d18ad1b8-d62c-352f-a3b3-04cb634d5904 | 2.8162 | -60.873001 | 2025-01-21 01:22:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21be8fd4-5963-3380-90cf-6f4d4db42cc3 | 1.915 | -60.485699 | 2025-01-21 01:22:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5acad967-27fb-388a-bb6f-6b1b65808302 | 1.1121 | -59.399601 | 2025-01-21 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ec4ca107-2d39-3993-999e-9f676b15b2c6 | 3.5902 | -61.411098 | 2025-01-21 01:22:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6d319b-be5e-37c3-a332-f5f858c73050 | -11.0201 | -45.059 | 2025-01-21 01:30:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6e04312c-a0c5-3adc-aaf9-d06a46e3c61f | -11.0205 | -45.036 | 2025-01-21 01:30:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d8618b87-8d9b-340d-a80f-ead2b6ff4996 | -28.65295 | -56.06649 | 2025-01-21 01:32:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 17.1 |
| fa9e9264-3c2e-3550-802e-57e9c0493a50 | -21.09443 | -56.27621 | 2025-01-21 01:34:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b240cc95-ecdf-3741-93e2-a155f90af717 | 0.93068 | -60.32729 | 2025-01-21 01:38:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 72764214-b97a-3ba3-a40f-4e482b6d08df | 1.00609 | -60.58322 | 2025-01-21 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6d0d2a5e-46b5-3c52-8e43-c304e45ba434 | 0.74837 | -59.64439 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 98f64ff9-b6da-34ec-a3a1-5ad911db1417 | 0.74698 | -59.65452 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 97293ed6-dbf9-3732-bab1-caecd98bcde6 | 0.86342 | -59.687 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2c5ed8a4-1a15-3564-bef4-43ee9cfb6e00 | 2.16969 | -61.8238 | 2025-01-21 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 3a8c47fd-3249-328d-934c-a78880bf95bb | 2.82611 | -60.88454 | 2025-01-21 01:38:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 77e82482-d19a-3f1e-86bc-fdddf87b467d | 0.75781 | -59.64575 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 77b95e54-3e0d-30c9-aa3b-2b62012f54f8 | 1.13848 | -59.55666 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0b1e6e92-98cb-3061-baa2-4ea3736e66ac | 1.12534 | -59.40992 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d7bdae02-ca23-315d-9e2c-8a9fad0e85ca | 1.13991 | -59.5463 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d81cc581-28e5-3f5e-b4bd-979501935a1a | 1.00738 | -60.57394 | 2025-01-21 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c11b92c-762a-33d6-8321-2c59d9731f90 | 0.75641 | -59.65592 | 2025-01-21 01:38:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 11a8abc5-438e-327d-95cb-b7bbc8337a21 | 2.17092 | -61.81499 | 2025-01-21 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbfdefb2-3157-36d1-950d-8479d1c5badb | -11.0393 | -45.0564 | 2025-01-21 01:40:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ba23b70d-068b-3933-87d0-1ac3ccd5e3f8 | 3.59924 | -61.42372 | 2025-01-21 01:41:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 80dd184d-6529-32f4-b585-4aeb2087082b | 3.6005 | -61.41462 | 2025-01-21 01:41:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 31.7 |
| ed1c4839-47c4-325e-b35f-b35d85d95056 | 3.60947 | -61.41586 | 2025-01-21 01:41:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f80515ce-6ef2-350b-8258-c1c5e6468198 | -11.0393 | -45.0564 | 2025-01-21 01:50:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| cf99d185-fdc5-3b46-9a6d-8a228e30802b | -11.0393 | -45.0564 | 2025-01-21 02:00:00 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e813d505-3093-3e8c-9499-604027ab18fd | -10.10517 | -36.25992 | 2025-01-21 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ede36385-c706-373e-8620-bf87ab82b462 | -11.1451 | -40.61345 | 2025-01-21 03:23:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bde9e50e-54ee-3e14-ae35-83a0a15fc941 | -8.91281 | -35.42788 | 2025-01-21 03:23:00 | NOAA-21 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 56c82c03-8b87-3e2e-888e-912f395d4759 | -6.82412 | -34.94792 | 2025-01-21 03:23:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9c3da47f-b512-34c4-ad82-459c768731b6 | -9.94352 | -36.638 | 2025-01-21 03:23:00 | NOAA-21 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b86d5db-6713-3ae3-b5ea-d9aa577ea751 | -9.11653 | -35.4872 | 2025-01-21 03:23:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1c84b63f-450a-3455-90c0-8b01b15ec5f9 | -7.84898 | -35.20045 | 2025-01-21 03:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ef6f486f-622e-30d1-952d-b4c0a667ed96 | -6.16286 | -39.43826 | 2025-01-21 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 224ebb71-a1b1-3cdf-bdd1-6d80506a3f5d | -6.79459 | -35.172 | 2025-01-21 03:23:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e86124b6-61ba-3b54-a3e8-8de608ff6245 | -7.95192 | -35.24337 | 2025-01-21 03:23:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9ac9b5fb-408c-3f90-b65f-d5973fc3f14d | -7.95052 | -35.24492 | 2025-01-21 03:23:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ed3e39ed-1e07-392e-af41-4365ca02b0b6 | -10.11989 | -36.27014 | 2025-01-21 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d688234d-a89c-3a0d-bd1f-a662c4add132 | -9.48413 | -35.95345 | 2025-01-21 03:23:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 60b0a501-f999-30cf-9afa-db05bf10a22a | -7.52062 | -35.17116 | 2025-01-21 03:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7c6949a-3fda-3840-981d-0300a39db2be | -7.81896 | -35.16534 | 2025-01-21 03:23:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 46c9fedf-90d0-30d2-931b-830762e4cfbb | -11.14448 | -40.6167 | 2025-01-21 03:23:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f33f4ca9-981f-341f-bc3b-8c50adc43db3 | -8.49792 | -35.66259 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 146b0dc9-ab5c-3c36-ac26-d8c34fe8def1 | -8.5057 | -35.66459 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e2a1c0ce-fad3-337c-92c6-9bf4ee171943 | -6.82024 | -34.9473 | 2025-01-21 03:23:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
