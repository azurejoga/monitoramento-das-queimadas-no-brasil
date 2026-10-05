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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4e6659d-f7ad-335c-a89b-377d10c0d2eb | -2.94824 | -54.14494 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 35526c8b-be0b-3f1c-958e-f5e29c23a799 | -7.44277 | -63.56201 | 2026-10-05 07:41:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b64aaa30-9cb7-3e58-8fc8-5ca802889c81 | -2.95296 | -54.15071 | 2026-10-05 07:41:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f6dde118-350f-39ad-9120-a7b66b3b4775 | -3.95353 | -56.044 | 2026-10-05 07:41:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 31e3d3ca-e560-3fe0-8386-ba6499c57a70 | -3.09176 | -53.71865 | 2026-10-05 07:41:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2a51d86c-14e9-3ea6-8722-16fb6c61c14d | -12.87266 | -61.71334 | 2026-10-05 07:44:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f70fe2ed-defe-3e39-8ff9-5fe2ce1d6a7c | -11.6758 | -43.658 | 2026-10-05 11:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 2058c163-9ca1-369e-8ded-056943988897 | -8.871 | -45.3928 | 2026-10-05 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 54dedd20-1b7d-3aac-9369-e2936c92a36a | -11.6763 | -43.6343 | 2026-10-05 11:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bfdbd71a-ac7f-3ce8-a793-e1b654b2234e | -8.871 | -45.3928 | 2026-10-05 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 62d9c218-4f26-38f3-b106-a91c57f3be8e | -11.6763 | -43.6343 | 2026-10-05 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 0e8ef5e0-5e8d-3d1b-83a6-6a4029bdc2b8 | -11.6763 | -43.6343 | 2026-10-05 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6cae65fd-782b-3d33-ab08-a227353ecce6 | -3.30532 | -44.22427 | 2026-10-05 12:00:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3e8a373e-61cb-34da-be3c-6e8ef102f696 | -0.63597 | -49.20242 | 2026-10-05 12:00:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a8206f3-83cc-3ec6-afec-8359ca7d4906 | -6.05897 | -53.47892 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7e86490f-0ade-362c-b203-b12039a4f52e | -1.8679 | -50.60385 | 2026-10-05 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c4402fc8-ef3c-3798-8f10-831c5a3b98b5 | -4.46213 | -54.96098 | 2026-10-05 12:00:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 12f7415b-691e-3d98-8840-ef54ef5a2bab | -1.33261 | -54.22309 | 2026-10-05 12:00:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ffa2a869-c8ef-3069-8e39-755d17445884 | -6.92987 | -43.6772 | 2026-10-05 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c7a59f90-8c10-36d5-968b-92c9951ebf5d | -2.31835 | -48.39735 | 2026-10-05 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 592ead87-81d8-34db-9ddf-ee0fddb89321 | 2.00914 | -50.91945 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 994c9262-1505-3d86-9274-e6d310200832 | -3.37783 | -54.09704 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4b246fb2-8df1-34c5-9f6d-87d46f9a9b31 | -2.28862 | -48.74215 | 2026-10-05 12:00:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4d20dba9-3908-3de2-b6ba-85a56f58a2a7 | -3.47052 | -54.59164 | 2026-10-05 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 63af3238-812e-3780-adee-bb130a3367e0 | -2.16183 | -53.66603 | 2026-10-05 12:00:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f2974888-90fe-3868-a816-7c5ddd4a30b8 | -2.68134 | -49.02562 | 2026-10-05 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 0d5acde7-a882-377e-a56c-55ba59855c61 | -3.50921 | -54.60299 | 2026-10-05 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9134261f-c6c7-3e77-b67c-ba444c3d2cb6 | 2.07094 | -50.89579 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 53c46624-e8b1-3179-a987-cc066b2be40f | -3.10641 | -53.71885 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 275954e6-081b-380e-9a13-cb8a030b5752 | -3.28013 | -50.0108 | 2026-10-05 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 2c1908af-3760-37d6-b0a9-c1d65c79e940 | -3.06054 | -54.17015 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 34fe5eec-5657-33c2-9e72-422447aff8c3 | -3.18587 | -54.08016 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cc309ef7-de0c-3853-827f-e23e29930f72 | -1.46387 | -53.59581 | 2026-10-05 12:00:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6d9e99aa-1847-32f0-9f57-34ae58913250 | -3.27885 | -50.01982 | 2026-10-05 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 1a8c3a85-4112-36db-a929-0e672044b0d1 | 2.06967 | -50.88684 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2afaf376-ec8d-3de1-8d1e-c9a0f1c47f24 | -2.69841 | -49.03778 | 2026-10-05 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| dc78c64b-bc40-3891-b031-cddc4e53953d | -0.63467 | -49.21157 | 2026-10-05 12:00:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 565eb707-d949-3850-b20c-b4d1ef1572a9 | -2.22363 | -53.71875 | 2026-10-05 12:00:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 948877ee-4a0f-3edd-845f-c64ab4eddd57 | -3.08037 | -54.17296 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 732a48bf-6312-31d4-b633-128e50fdd2b9 | -2.58017 | -51.87087 | 2026-10-05 12:00:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 24b8b64b-e506-3aae-b0ff-15df8e604494 | -2.22518 | -53.70792 | 2026-10-05 12:00:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0c719fc2-87f6-3ce3-90f1-fcb5d20038af | -3.07839 | -49.54538 | 2026-10-05 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 274c1794-1d0f-3a63-855c-79c757140fb1 | -3.46956 | -50.10439 | 2026-10-05 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f2b6e3e-1340-3411-a8be-f7727eebf3a5 | -1.35884 | -47.43218 | 2026-10-05 12:00:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 70ebc4d7-f4ab-3983-be4c-77d7530fb58b | -0.38487 | -52.05742 | 2026-10-05 12:00:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 94a35389-56d4-3f96-80d5-440bb440457a | -7.33911 | -47.26805 | 2026-10-05 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1c573155-3866-3d6c-98e3-8cc7f836c7cb | -6.90001 | -43.66704 | 2026-10-05 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 45fac8b8-5187-34d8-9d74-7afb0a201141 | -3.47084 | -50.0954 | 2026-10-05 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b122b88e-2e4b-371e-b2e7-d5992f5dd7bf | -1.4767 | -54.77549 | 2026-10-05 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 17ee1f79-c1e0-30ee-b3b9-8f6928c9c65a | -6.91511 | -43.67541 | 2026-10-05 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a320c497-ef91-3d8a-9997-0456f56cf752 | -3.10796 | -53.70826 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d5a25e90-8851-3820-9d6e-a92f781ed930 | -2.97915 | -54.09515 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d66edfc2-52aa-35de-9137-978ffcb306f0 | -3.3289 | -53.39348 | 2026-10-05 12:00:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 379174f2-d378-3d98-a4ce-9b82c11738ed | -1.51543 | -54.80775 | 2026-10-05 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1e4a353a-90e2-33ec-82b1-7dcb16e5894a | -2.25766 | -51.93567 | 2026-10-05 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e4fd9b4e-9546-3892-a73c-528bf0f1800b | -2.98902 | -54.09655 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 55d17339-f8b3-3513-9c9f-1b501d975b89 | -1.18295 | -49.24933 | 2026-10-05 12:00:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 099cdee7-e8c4-3688-bd92-bdd96d8e8f18 | -2.6892 | -49.03652 | 2026-10-05 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5f2d8287-e726-34d4-81b9-4d1980f915ea | -3.07045 | -54.17156 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 9c218858-bd0d-3613-b8fd-5c27fc6a5478 | -1.21959 | -46.89335 | 2026-10-05 12:00:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 65d274bc-a05c-320b-aff3-cc15b774e056 | -5.68835 | -53.48982 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1ef8abef-d16b-3852-8c98-a7e421f5699e | -2.94448 | -54.19403 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| db72e533-6cec-3aa8-975f-d47f2a503fda | -3.04865 | -52.14803 | 2026-10-05 12:00:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4dab2e75-63be-362e-b4c3-e523c32db0c5 | -0.85727 | -48.6814 | 2026-10-05 12:00:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| df7f6824-3e73-37c7-a46c-4476aebd61cd | -4.12662 | -54.01913 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0358a2e6-3ae5-367c-9695-7fd8dda8c361 | -3.07208 | -54.16033 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| c8dab226-671d-31d6-a4ab-74ade3eac71e | -3.11139 | -53.75206 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 35cf22e1-acbd-34b2-91db-129452a18321 | -5.99031 | -53.62745 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 14e5cbff-7fe9-337b-84a1-267c1b8d794a | -5.68695 | -53.49955 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b58ffc08-f4d5-3bfe-a600-a16f810d31ca | 2.00025 | -50.92066 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1df5df23-0b2c-3821-a5ad-149f13ef63ad | -3.80203 | -42.95053 | 2026-10-05 12:00:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e2a7cd62-6afb-3624-bc6e-e2f9e07bd68a | -2.97813 | -53.26766 | 2026-10-05 12:00:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d583c08d-c58e-3de3-b8dc-4d8dfe4c5b15 | -0.40974 | -52.01325 | 2026-10-05 12:00:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7a34f77f-8082-3b77-bf09-a5c190e3bee6 | -6.92957 | -43.67033 | 2026-10-05 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 019c619a-4ab3-3448-81ef-b4545a5a6c25 | -2.9079 | -54.09008 | 2026-10-05 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3a6473dc-ef41-33e9-883b-afdd6beec771 | -6.006 | -53.52045 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9930016e-9331-3bc9-a6b3-ae5db1b55992 | -1.26436 | -54.55493 | 2026-10-05 12:00:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 68b42c74-90dd-3535-a439-d94df64fd573 | -2.90305 | -54.12379 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 701b400a-9a30-3b4b-a84b-2cb07be354e6 | -4.46923 | -54.96846 | 2026-10-05 12:00:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7132a12a-4343-3678-b558-1015b07a4342 | -1.21787 | -46.90569 | 2026-10-05 12:00:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ba493296-62c2-3ccc-9347-4d9b04943f5f | -6.91481 | -43.66855 | 2026-10-05 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 78acc619-f0c5-3c1b-8059-a991d16438da | 3.43054 | -51.31375 | 2026-10-05 12:00:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ccf8b4a5-bf79-36f8-8a27-0c970eadd80d | -3.68585 | -42.57227 | 2026-10-05 12:00:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| d3f46160-82e5-30cc-ad27-0674cade516f | -5.98886 | -53.63731 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b864de1c-7570-36ea-8555-00347af2a089 | 2.00152 | -50.92963 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4f5f09b7-3a32-37bf-862f-0ad5530ad841 | -2.28721 | -48.75204 | 2026-10-05 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 32c6e4fd-53a0-3617-97ec-1b760d80ca6b | -6.00741 | -53.5108 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| f2f3b105-aa4a-34d4-828e-8df41574a1c9 | -2.90143 | -54.13512 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 344c7350-a723-3ad1-8848-ae804ab0c1dd | -5.99955 | -53.62889 | 2026-10-05 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b7fa23f5-f60e-33a2-baee-b6e93a128e9c | -3.78717 | -42.94863 | 2026-10-05 12:00:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| fe59669e-5dc0-3024-ba09-ce96456c0c51 | 2.10389 | -50.74577 | 2026-10-05 12:00:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2fb7c976-5093-3f71-96d4-7e862fc8593b | -3.0523 | -54.22686 | 2026-10-05 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1a009bef-058c-3b29-9d61-8fa78a836cca | -8.68363 | -54.57132 | 2026-10-05 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| f293bf11-368f-325a-8d76-a92278512e71 | -10.48973 | -46.04056 | 2026-10-05 12:02:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0c2738c9-df57-3fdd-8a07-da04db1efa09 | -8.67419 | -54.56996 | 2026-10-05 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 19773f58-7a95-3c4d-a7d3-3daa2b0fd4e6 | -7.21409 | -55.19363 | 2026-10-05 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 59630ea9-2ec0-3f4e-92c9-5a69e6e95327 | -11.67727 | -43.63216 | 2026-10-05 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7dca41ac-6ade-3b3a-9e7b-c5bdcf20642a | -7.22412 | -55.19495 | 2026-10-05 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6ce67dbb-e42d-3fd1-9456-574aa5cce710 | -8.87438 | -45.38544 | 2026-10-05 12:02:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 63b4e4f8-0619-382b-9c6c-d129461bb3fd | -7.72835 | -45.46554 | 2026-10-05 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |


[Clique aqui para ver as próximas entradas](README63.md)
