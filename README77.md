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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e91fe60-269b-3830-8079-082f79fd0b2d | -3.42871 | -50.43982 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6107cde3-30ae-381c-92d9-5920721d1785 | -2.7667 | -54.07994 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 52a25f6e-3f16-3970-bf86-b8c82b0f6887 | -3.11459 | -53.77073 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4255e8b-22a2-31c6-9435-a5c4c21da55b | -3.285 | -54.03028 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e8265885-2022-319b-b7e6-d59c398c588d | -3.67385 | -55.94566 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1174baca-02d9-3586-8efa-eaf95445b2d4 | -2.76904 | -54.109 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 50358e29-b0a5-32db-8ada-6aeb8f11a56b | -3.04319 | -53.89849 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b1fbe5-0b08-3771-a77c-91b4deb5467d | -3.27119 | -50.39809 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0b4c09d-d665-3dda-adb7-0bbb17a71b70 | -1.28715 | -54.55878 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4135eda0-fe38-386d-970d-aacd0dc13bf6 | -3.0599 | -54.14328 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c5a0f0d-340b-3b21-9334-b5d719fe8279 | -3.66762 | -54.5449 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ac67c64-7868-33a3-b68c-1e4f704c32f8 | -2.93245 | -54.1526 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93ec6967-0193-3504-9382-88bff0164fc4 | -3.86123 | -55.96397 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cb1d388-f26e-3d56-8d89-9f56dc65a2e9 | -3.7156 | -54.23349 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 01eee39c-5ea5-32c2-9e9d-ff1fa7396be0 | -6.94136 | -43.67201 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10a487a6-8db6-3128-9b9f-c4911dc24f27 | -0.42481 | -52.06515 | 2026-10-07 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b96a4ffe-c63e-3f3f-8fd3-f85cb4458643 | -3.27001 | -54.06056 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 04add51f-865b-3784-ab0d-54f68a79deb8 | -3.04133 | -54.26224 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5844960f-440e-37e2-bf36-3fd5070dcd6c | -3.82855 | -59.39344 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f951a30-9978-35ee-b142-2e284fe32e32 | -3.06039 | -54.22591 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4433bdd-8b72-302c-be35-50d025b4f943 | -3.07794 | -54.17839 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b0470c-726c-3b76-b474-634a0155f40c | -1.52375 | -55.54749 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5eb6d7a5-7857-38b6-9bae-d4a888082749 | -3.08929 | -53.71175 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0627d1b9-6443-333b-803d-dedc48f5e812 | -3.18784 | -50.5484 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0cfb4902-1da6-34e7-89bc-63227f6667ee | -3.99554 | -56.25871 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02f6fe97-dc0b-38f2-9625-033032cd9750 | -1.1025 | -52.25922 | 2026-10-07 05:04:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87dad064-580d-3e71-bdb3-e3434c8cf703 | -3.05159 | -54.15279 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46858e2d-5c9a-3b05-98f7-42e97e243371 | -2.7847 | -51.67418 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1ed52db-b0ed-303b-8bda-6d2a83dd5d2a | -3.50916 | -51.68766 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a57437b4-2ff6-37a1-b10b-c501edbf4c29 | -4.26496 | -54.86175 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44afa77a-c5f7-3adc-bf7e-5927b541a258 | -3.02518 | -54.23479 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b8767f7-99f3-3bb6-908f-39b133a80a5c | -2.88807 | -54.15292 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f0fe045-eaf8-3a30-9ee5-e56cd3eb770e | -2.47895 | -56.09892 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d2cdaf-63c3-3935-82b9-f917e357e7ab | -3.84699 | -55.99009 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dccbc4fd-f824-3d08-96bc-08dfc34c55ec | -3.46581 | -54.59575 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccee60d7-b864-3fed-9766-cc848a195d0c | -3.12915 | -53.6995 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a58a868-f28d-36c7-88dd-c0e65397bf60 | -3.67744 | -59.63437 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4070b9dd-0c38-3050-8e32-aa455c4caa94 | -3.08052 | -54.27195 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad596541-e7eb-318f-814f-468cfa85c232 | -3.73979 | -59.41442 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb19a618-04b6-3101-9069-4627da0a0f28 | -3.08439 | -54.26897 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0854ef3c-d629-3339-b75d-9f0516296e07 | -3.09939 | -53.71333 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21290a6b-3e9b-32f3-b136-77f34a8c6315 | -3.53975 | -59.49833 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31d566b7-421c-34e8-a3df-8b06ff5eb4c7 | -3.52234 | -54.66832 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e42e359-840b-3f52-83eb-519e3e689b99 | -2.4677 | -58.0751 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 084d3aa6-3dc3-3864-855d-0618525e737a | -3.27936 | -54.00042 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dedda813-06d6-3bd3-8b9c-8ea91e725cb1 | -3.28051 | -54.01509 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76bd3c1a-81fa-360e-aa2a-8033587c4f9e | -5.37101 | -55.88527 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4009eac8-22f9-3ce4-a6f7-83dae1365463 | -1.96955 | -56.04852 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83910b88-6f1c-3944-850c-ea97744757f8 | -3.1314 | -53.70721 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 170f1a4e-2b1a-3be1-b422-8df3cf86c7c5 | -4.54175 | -54.98308 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f1bc414-05f2-3840-9d42-df252c5afa47 | -3.13783 | -54.36288 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa62c8de-9317-3862-a873-11cfbf36ea33 | -4.14265 | -54.02649 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c121ab8-08f1-300b-a382-af960702afa3 | -3.00099 | -54.12703 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7875d738-99eb-311f-9560-76aa3b499ea0 | -3.01972 | -53.8949 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee6ca7a0-dc2b-332d-ab06-8e0f065d9da9 | -3.05607 | -54.16784 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 804bec63-6359-3176-a3cc-d798ed2bc67b | -3.8358 | -51.3249 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f563f4a5-617e-3118-9fdc-b88b1e25d410 | -3.01603 | -54.14012 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ddd38ff-546e-3f8f-adfe-a81fa3520e15 | -2.87274 | -54.20792 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16beb117-28f8-3a9a-977c-76b19adb725d | -3.52463 | -52.74896 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9c94b28-c254-3185-a93a-df8dcac4a178 | -3.70153 | -50.9807 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9d47ad8-f537-3e43-9a64-231042d56544 | -3.51295 | -54.66333 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ae6c1fb-2d21-3ad0-80e1-5b6ee4fd48b7 | -4.15673 | -55.14154 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8e252cf9-07b0-327d-926a-d270aa5e3e1d | 0.9423 | -60.41013 | 2026-10-07 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15ab0b97-59ec-34c4-87fb-0463ba60e7f2 | -3.99159 | -56.21894 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1309c705-92d7-38a2-8887-5c9080c32d0d | -7.22037 | -55.17091 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 704ea6f9-89e6-399a-9f35-a88c76ca91ff | -4.34668 | -55.16813 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb997942-48fa-3135-bf9a-d50346c2f601 | -3.16887 | -50.43866 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2918b7c9-3038-3194-b480-0150067d525b | -2.77182 | -54.11302 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 376b07e4-360b-34bd-8edc-010ff1bdc07c | -4.30925 | -50.78356 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2e4792c-8187-3229-91e9-741f79ba9070 | -4.25642 | -46.37817 | 2026-10-07 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b58ea6f-b045-3ea8-89f1-315afad7e88e | -3.5272 | -54.63717 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd297d03-39b3-39c1-aef5-82dc7ab5ee42 | -3.45876 | -51.59433 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56692e1f-2b8f-3b1d-9ff3-d13df64044cf | -3.27445 | -54.05401 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f519283e-5aa9-393f-97f9-597bea3c63b4 | -3.50413 | -51.69582 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 03ca2246-9e83-3a8f-b9a4-ba98f982621a | -3.1792 | -50.55225 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 11e1d700-5940-3348-bc04-e29972524eb2 | -3.27661 | -54.01813 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a93b678-30d2-3f87-9a51-5fa727e3c78d | -2.48005 | -56.09194 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821de1fd-46d7-382b-a52a-4085ab50185c | -3.27765 | -54.18409 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b68e7d5-70ec-3378-8b5d-e4cdb220db9e | -5.72696 | -45.1627 | 2026-10-07 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5c71ac06-d90e-3765-89e8-36cf3a2b246f | -3.8972 | -59.3321 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d37effcb-7945-3f04-b9be-d3b7ab1d6f37 | -3.10725 | -53.70717 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b76c1046-49de-34ec-bf0f-bcc99e978515 | -3.18634 | -50.55852 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d28c38bf-7e3d-3d99-8e81-7738c1690d72 | -6.92327 | -43.66709 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ed102918-02b5-3b06-9f55-6dbd8ec35726 | -3.24543 | -57.86602 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31c709ee-4c1a-3837-bab7-9319c5214d7c | -3.72107 | -55.46692 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eac80d8-00ed-301b-bfa3-2b48b725bd37 | -3.89345 | -59.33152 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20b98d82-85af-3d8c-b4a6-a26e1820c7eb | -7.19537 | -46.52542 | 2026-10-07 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b64b42-4381-3a03-99b1-c24e5e1e4394 | -2.3103 | -57.08057 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 694fc032-2bfb-3258-a021-7998ca8b8dd1 | -3.49428 | -59.27579 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53ce1bbe-b908-3ae7-9b43-bcb16375ba9e | -2.95294 | -54.13059 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b0d92a3-4b51-3c12-a1d6-39e28e4374d3 | -1.80423 | -53.75137 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d96fe94e-d45d-3fff-ad61-0445e44f7910 | -2.90281 | -54.07977 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 571eb307-2605-3538-a59a-00b0f46b8205 | -3.29231 | -54.0712 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 659bd0c5-006e-33ef-83ce-834bb3b2933e | -2.94742 | -54.14412 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d8ec0de-3670-3413-8eba-51201f85750c | -3.21253 | -53.88434 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7c1c49-a0d3-3c12-9a09-2875b52b6814 | -2.96108 | -54.1424 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0c6fb50-0b25-3cd8-b953-cf3096a56170 | -2.75246 | -57.65617 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42f32c5e-b4d8-31a8-baf9-cd6d62b94978 | -4.25752 | -55.04088 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41d54bda-aff4-310c-9e91-31d325a10095 | -3.65294 | -55.31946 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d4b1b9e-d4c1-3792-98ff-c751ffc4018a | -3.51188 | -54.67024 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README78.md)
