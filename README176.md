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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9839547-c8e8-3bbf-9edb-88326872d1db | -15.59305 | -57.36687 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 90517883-c286-3d79-bccb-b47ddfca6e57 | -15.55124 | -56.64466 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f49f47-37b9-3c26-8cf5-3dbe80299ad8 | -15.54789 | -56.64412 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9bd39fe-fd77-3dc4-b91f-d13f6f0c091b | -15.54509 | -56.63993 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab44f5ea-e9ae-3b26-ac0c-d00a2206e1c6 | -15.54454 | -56.64359 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 819c5f98-2b07-3e20-b343-dd06bc677b6b | -15.65824 | -57.38501 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f94cf6-06ce-31d8-b2c1-decdcec6062b | -15.65492 | -57.38448 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49d8913b-acdb-35ca-b800-3e9ec32c9b46 | -15.64829 | -57.3834 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3800f7ef-f800-396b-b86b-f2e6addb1778 | -15.64554 | -57.37925 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb052535-a6bf-31ca-8646-fd04875f9254 | -15.62068 | -57.36408 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e73ccde-e728-3ce0-ba15-88ef8fc76c2f | -15.61017 | -57.36608 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d97981da-005f-30e7-a99f-f853448f71d2 | -15.59636 | -57.36743 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 987a42e9-d785-31da-a4a9-54044ba67b01 | -15.5936 | -57.36332 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 990d341e-f05d-33c8-b6a1-e156b91a461c | -15.55069 | -56.64831 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eec7e23-9dc6-3798-aefc-e2e343582fdf | -15.54733 | -56.64777 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c17a905-865d-33f5-a101-358467604d3b | -15.54174 | -56.63938 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd757cbf-9b35-3eb2-9827-70290fbf40d0 | -15.54119 | -56.64305 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29b52c39-71df-3cd8-8e08-ba229832b075 | -15.53728 | -56.64616 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3975e2f6-45a2-356d-8e3d-ebcdb7ea7878 | -15.65161 | -57.38395 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3df1a55a-26e8-30f4-abc5-74c2c6cd4b8d | -15.62344 | -57.36826 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 737118e5-3762-3b3a-90f1-5a2ca8780346 | -15.61736 | -57.36355 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64600d85-e4d7-38ae-9c99-bdc229ce64ba | -15.60686 | -57.36554 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08866357-1889-3664-8e80-a1f78dc5106c | -15.60354 | -57.36499 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27412905-f082-3074-8e09-401dcb92b80b | -15.59968 | -57.36799 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| faf4b2c5-a2a8-3aad-a630-7a421b57a154 | -15.59966 | -57.43402 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66651e90-5464-398a-941c-05d96ce32489 | -15.58984 | -57.36624 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bdaeb4f-2dab-34d6-8d41-6267ff5f55c4 | -15.58652 | -57.36569 | 2024-10-09 05:04:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41590c4a-e857-3209-8afa-b19cf379b5ef | -15.52951 | -56.89923 | 2024-10-09 05:04:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27fba205-e57a-3d89-9fab-a6cf12e3a72a | -8.97715 | -57.65646 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c9ed2b1-0ed9-3fe6-9f82-941edc5c97b6 | -8.09383 | -57.67477 | 2024-10-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294ce132-66c6-39a9-b714-6a080100bc1f | -8.09325 | -57.67841 | 2024-10-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3b6a03-223a-3079-a589-c22714b5d3bf | -9.99916 | -57.38652 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb7d162c-63c2-3baa-ad14-46fac5038c2f | -9.93196 | -56.73916 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb50bf2-c5a0-3cc5-9bcc-b824eab354a6 | -9.92664 | -58.12617 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 894b1c37-3967-3b78-90f0-9c9e4768cf51 | -9.92604 | -58.12982 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8d8e50f-6bc0-3b34-94c3-373216afc20e | -9.92554 | -58.1264 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95134a22-8123-39a7-bb50-0f9aba75384f | -11.70028 | -65.01385 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c3fb20cf-47f5-3e74-90bf-b2c48db1cfe2 | -11.69991 | -64.96203 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38099b45-9bdf-3ed9-be01-fd7224aff464 | -11.69888 | -64.96753 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55bf2346-952e-31d2-8c76-4561f5d492a4 | -11.69643 | -65.00741 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9d2ed4d7-1ecb-38f8-8cbe-0078849c4ae6 | -11.6954 | -65.01294 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 7ede3389-947d-36aa-a094-bb1736a7b4aa | -11.69403 | -64.96648 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f54ba2b4-cc2a-37ef-b7c6-b8ff9283a289 | -11.61839 | -64.97929 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 700207b7-0fc8-3a0b-975b-67bbae1e4f3e | -11.61248 | -64.98389 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b1a3e5e-77ab-37df-ad17-89d1f0962f10 | -11.61144 | -64.98949 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aee7873d-7bbb-30a1-b9e4-79aa9a6cb8de | -11.60761 | -64.98289 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cc63faa-e6b8-3034-93a2-fd62613bb9d8 | -11.51951 | -65.15301 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 887abb4a-dd7d-3ef6-b947-b85e72ab3fc2 | -11.51895 | -65.15182 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 714a6275-d9c1-304d-9d77-8b78c70761f5 | -11.51615 | -65.13918 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| da2aaaf7-9db4-3a0c-8107-28a06f75301d | -11.51508 | -65.14499 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 856ecb3f-baf4-3f17-af11-afa29493bbf0 | -11.51403 | -65.15074 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7cad8a4d-877b-3716-9bc9-d63a7dba22d9 | -11.50661 | -65.10773 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddd06233-8d93-3553-8fea-74b2bd2c11f5 | -11.50556 | -65.1134 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0afeaa-a784-36dd-8b23-16669b8559ae | -11.50377 | -65.09545 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f56f1b3-708a-34f5-b496-33fc9d7db199 | -11.50273 | -65.1011 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9db5c900-3b3b-3b36-8cb4-962f028a8a6e | -9.92544 | -58.1335 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aed43dfe-01ed-37ff-b2fa-d311b3d9b73f | -9.92495 | -58.13006 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1cf56c4-9e5d-340a-afcb-5d8428690ec7 | -9.92436 | -58.13374 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bceedc6-64d2-327f-88f6-3795f09b7cbb | -9.92274 | -58.12218 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 643cf128-5fb3-3865-a7da-b391478c1ebe | -9.92216 | -58.12585 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfec073e-b7bb-37e8-9d23-3e4123deb964 | -9.92157 | -58.12951 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10a58ef3-9718-3a8a-818e-fe25697e475a | -9.92098 | -58.13318 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b15137a-895b-3466-a8f4-fdccae0c1d24 | -9.92039 | -58.13686 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b299f263-65d5-3d53-991b-fac6c9cb2260 | -9.91819 | -58.12896 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8367b0db-40f2-307c-a82a-e949ce3c93ff | -9.9176 | -58.13263 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48eaf11d-8965-3416-bed3-3f7d6b604eef | -9.91701 | -58.1363 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d42acc47-a28e-3872-be02-2731d2167322 | -9.89763 | -57.91253 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae8067c-62fc-37a4-b886-8b385d6570d3 | -9.79459 | -57.45545 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 473bf13a-2cfb-36e4-ac1a-c9e4ca910444 | -9.79126 | -57.45492 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a6905f8-271b-3d71-bd8a-173ca57549bb | -9.73412 | -56.97975 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4291210c-0aba-3025-bd86-cec8774bab09 | -9.73357 | -56.98324 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8da419d-2d04-3202-a69a-f45e43cfebf5 | -9.73081 | -56.97921 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed6719bc-8382-3c5a-810b-1ad22f19e42b | -9.73026 | -56.98271 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08ce2cb8-4e8a-31fa-9bf0-431c9b0323d5 | -9.72941 | -57.86348 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3cab26-1a37-3583-a289-0cafa51e8591 | -9.72694 | -56.98217 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10b944f4-644c-384e-85df-bb3c885ab1a7 | -9.72605 | -57.86294 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c84f849-c37d-3865-a6f5-86af04bcfbef | -9.72582 | -57.79987 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df9d054-af59-3025-a830-3c1a0b0ef7ba | -9.72524 | -57.80347 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c62a046-83e3-38dc-b093-8cff70aa8996 | -9.6824 | -57.21959 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33da33a3-61af-3370-ada2-5469dbeac566 | -9.67006 | -57.76117 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69193f14-7b63-3e4a-a162-3150b3b45b3d | -9.65689 | -56.95302 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f02d719-fdfe-3bb3-bf12-92f087c2ec8d | -9.65634 | -56.95652 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b792112c-4f0d-30ff-a0b6-7258bc2b38c1 | -9.65579 | -56.96002 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0bd1d9d-da9d-3cd7-b2c2-abf5cf9fa6d8 | -9.65358 | -56.95249 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3fb13d8-ac2b-3e77-ae2f-c818dcf589c4 | -9.65027 | -56.95196 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1360d2eb-5c74-3603-ab04-163dd793f7e8 | -9.6273 | -57.60696 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3caeef82-f628-3006-951a-3a70e4d42db5 | -9.62219 | -56.74339 | 2024-10-09 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 464aebac-985b-3419-bfed-2108698b9e7f | -9.58233 | -57.56664 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f076352f-a19b-3a8e-8d36-201e9338b176 | -9.58 | -57.56647 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae432fb-8265-332a-b270-e986f08a19d6 | -9.54161 | -57.9032 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b326fb-55ff-39d3-bef7-3590ae22aa80 | -9.54102 | -57.90684 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccac57a-5c45-3f57-a430-3ed0c84908cb | -9.53765 | -57.90628 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 191b52ad-b564-3159-a05e-04aa9d75cd05 | -9.48373 | -57.9314 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41a9324a-8368-3607-86e0-88b5318217c8 | -9.48315 | -57.93505 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdaaaae3-2d97-357c-849b-2e4e7a8b9283 | -9.48036 | -57.93086 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1541a1b6-2d37-368d-8b1f-eacbe401ab44 | -9.47977 | -57.93451 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc716b9f-4b14-3cb2-bbc9-c99172d929dd | -9.47919 | -57.93814 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a55e1f0-9b9e-3a4a-9a1c-4234a9b0bb89 | -9.47815 | -57.92304 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d98bc9f1-dfab-33a8-aca3-b288bf1db8e8 | -9.4764 | -57.93396 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd38610-8d38-31bc-b01c-dd62966bbbdf | -9.47581 | -57.9376 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README177.md)
