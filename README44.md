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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b05d861a-72b6-3c13-a6a5-8ac265c5a4fe | -2.63262 | -46.87944 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a69c23fd-d2a8-3ecc-b71a-5df2f4aa8afe | -3.28292 | -50.60624 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 622ed415-ff53-3cc0-97d1-d2afcef1f190 | -2.71206 | -48.65821 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daabb57c-b5e3-3149-a186-2368fbd740dd | -3.48837 | -53.81071 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c9750e6-ee2b-3080-8ec9-5b08bc65e28e | -3.49127 | -53.80534 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11f45158-220d-3042-8dfd-d588acd122ee | -2.65626 | -51.87034 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 059c9692-0fed-302e-bee1-c2c3d5c0b19d | -3.09477 | -53.72223 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de9e12d4-5130-35fb-83a6-3dfea7af47e5 | -2.80384 | -54.04045 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88c85a1a-f9f8-3650-8239-d5dbb5ba4002 | -3.9851 | -49.97285 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8417d5-3db8-3cf0-a96e-c1edd5aed8ee | -4.69113 | -42.39843 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61ee00b9-c199-3706-8405-1274438ca96f | -3.21589 | -54.23592 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffa4b613-1e09-3560-97fd-2c7a6af595f6 | -3.93029 | -51.17408 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98f9723d-b77c-3a0e-9547-7e5dd912f9e0 | -2.91118 | -53.99822 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50fec268-5751-3635-82c9-8734cc5e2697 | -2.76186 | -51.68878 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76258e3d-ca4f-3539-a3a8-2f9b9e686009 | -2.91073 | -54.11896 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2134520-2018-37d2-b2f1-b29351d0688e | -2.32046 | -50.65742 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a492f635-a068-3867-a24f-2b6d72e83da8 | -1.97011 | -46.46385 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d526a1-8c6d-338f-b9ec-4ab0200b2ccf | -3.8952 | -46.68399 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acde6608-9fc7-3565-b6e8-d173b9e64d4a | -3.08837 | -53.23136 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20612943-d8cc-347e-b71a-6a7c3c82b1a1 | -2.98434 | -45.58047 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 14b0078f-628c-33cc-b6b0-9458a794b0ea | -2.9648 | -53.72693 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ca6e19-ead6-3e55-a9d9-22fa8cbb62b6 | -1.36616 | -52.86636 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1d68ce7-22e6-3206-b4ae-fa711161f103 | -3.41457 | -50.24126 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e66a02c1-ffdb-379f-b54b-30cae6ed77e7 | -1.36214 | -55.15342 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09641985-9476-3930-b309-ce38bc1bea40 | -2.89217 | -54.16459 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9519eb2-c8dd-30f8-8962-d3bf4fde3931 | -1.34579 | -51.38872 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e910139-0925-3d3f-854f-2632ac9e1b58 | -2.98294 | -51.45925 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e82f603-4821-332d-9dbf-3de80fb3b000 | -1.658 | -52.49762 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84fd0b7a-533e-37c0-9ec1-a719eaaf36be | -3.49198 | -53.80101 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c35b445-0e00-32cb-945f-ba4fcde76713 | -4.79941 | -44.9987 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a4b8640-21dc-3047-874a-e2e5f96f4722 | -3.43905 | -54.12332 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fae7dae2-45e6-332a-8bc6-0271eef58ebc | -2.62475 | -54.21738 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e2c3174-b02d-379f-bbda-75efed6e0f53 | -4.2818 | -46.29373 | 2024-12-01 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f26ee4cb-1576-3c4d-8d60-2792535cefab | -3.94581 | -51.09787 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68dd80da-cc03-31cd-948e-aaecd50ef104 | -3.32882 | -50.18563 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b7f43dd-0ee6-3129-8881-68a376ddbc43 | -3.22141 | -51.71961 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0efe12b3-a6d5-3e6b-9dd5-73182dcf69c4 | -3.01891 | -51.43535 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8b9f81b-1c0b-35da-a973-4c7a31edb574 | -3.08728 | -51.07042 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62199fed-8485-3668-9f7f-88c585a6258a | -2.93622 | -54.29883 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29c77abf-91c6-31e2-9be3-4995a6a427ec | -4.06609 | -51.06675 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c8caf9-654d-366b-b15c-f332e3ec1ab7 | -1.99284 | -53.29303 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42695c21-f79c-3a2a-b73b-cfdc05315b63 | -1.64176 | -55.06998 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a11146f-4002-3563-abd5-d38f348dfe6e | -3.07453 | -50.9649 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 584c5420-be11-3e21-97d9-54e3043696a7 | -1.32783 | -55.66649 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0725fdb8-edc3-33ca-8b9e-90700ace5fc6 | -3.46043 | -50.23074 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d283f30-be04-3236-9d1b-88604b258e51 | -3.06638 | -50.32787 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3abd4498-23f4-3148-900a-3b5e73659922 | -2.82589 | -54.06946 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dba26121-2e49-380a-bb67-dafa16fb2baf | -1.24662 | -51.79423 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eccb5285-31f1-3fcf-8265-458714b07caf | -2.96349 | -53.72566 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8966acce-71da-3cb1-b264-98a48eefcd38 | -2.80475 | -54.05923 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ade785cf-f098-387f-9ad4-038ee101a6a7 | -2.04769 | -54.66829 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c94e5dd-682a-3fd3-a4d6-4c5d047f74fd | -6.71553 | -47.27237 | 2024-12-01 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a13ef35a-1ee3-39c3-b165-0a55b2eb068b | -2.08573 | -50.64232 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c37f825c-87eb-3311-a70b-a9bae013dd29 | -2.33719 | -53.86806 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23a52ade-de35-3f23-9e82-5b28522e52ff | -3.3765 | -50.42276 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c46e45c4-4865-31ad-8ffa-b3ab1730063e | -3.21967 | -54.23654 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9abfcac7-a22e-3808-b6a5-055def7b3ea5 | -3.90808 | -42.42137 | 2024-12-01 04:44:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 495df278-1f4b-3a17-be05-c48fd5a7d806 | -2.15339 | -50.62442 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e55f3d-4454-3f5f-b2de-f706b1b39d21 | -3.14588 | -53.82928 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d972d1b2-7926-3636-935b-5964f5613400 | -4.82242 | -48.48142 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47852331-9ec2-3f79-a95c-eb0bf1c924e2 | -3.32828 | -50.18908 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 253b6fd5-5a90-31d8-bef3-eb49a34eec7f | -1.26461 | -51.74749 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3b240a9-545e-3bcd-abf6-8ea6896f0694 | -3.54921 | -54.81573 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0def75e-86f4-3e67-9573-54a3e765d9bd | -1.04869 | -51.81036 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86bb7634-d3bf-3eac-9a0d-9dcc7d006fb0 | -2.44247 | -53.62421 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d73977-c4ae-33a5-a46e-a822dd8b2756 | -2.01484 | -51.19915 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c7137c-68c7-3d7d-b0b3-164129204675 | -3.9359 | -46.71762 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de9e7103-1208-3fbc-a0ff-78058150d99e | -3.7776 | -46.69555 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f624f50-f4fc-3569-9695-f5db16d454d3 | -4.41575 | -50.69903 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd65d70-95c5-3ec8-94c0-f07529789787 | -1.27232 | -52.70564 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47e69b00-6a6e-33a5-9d6a-4d49f38fb854 | -4.20921 | -50.69498 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5954c06-53f4-3cbb-a6a4-0e3882aa02ea | -3.31932 | -50.03208 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2c21c13-b305-34fb-81c7-c1182eb42675 | -2.26283 | -50.71963 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afbd5a05-0e9e-3749-8a50-9333ead7166d | -1.5105 | -52.56551 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bfe38b6-6f88-3646-b27c-cfa098cc5a49 | -1.32488 | -51.67733 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e01c8fe-d090-3579-8ce5-260f151ec1a4 | -3.05975 | -54.05656 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0d3d08-c94a-3bba-8ee6-75fbe21c0b0d | -1.66718 | -45.7513 | 2024-12-01 04:44:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0297f9d-1b10-3a54-a817-bf6b2a8a2182 | -2.99677 | -51.06727 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 544eca2c-b88e-31a0-8845-d6c89281ddff | -1.43799 | -55.24849 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b340638-2400-3c33-8404-06d680b2b8fc | -2.63204 | -46.19563 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2806753f-9ed6-3e59-b573-5c49d5d5caa3 | -2.41573 | -50.35332 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee2ee56-1507-3125-a9b4-4fb7bb26e90b | -1.27493 | -47.86859 | 2024-12-01 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f1c61e6-5ee4-3d9b-b5ea-080cbd114760 | -2.46606 | -46.56417 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb50a7f6-de9a-357d-a3df-45130417c74a | -2.99343 | -51.06675 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6a1fe87-9bcb-3507-8eb2-dbbb584f28d0 | -2.80399 | -54.06129 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c8c5224-bda7-3926-9214-8a60be820966 | -4.08596 | -49.56359 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01e01c6a-a1a6-3247-8074-15e0fdd1aa2f | -2.97051 | -53.89327 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5191cb52-16c4-32b6-89b3-2b6a00151000 | -2.47605 | -54.01333 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcc27300-71eb-3d80-a4ba-c9373332eb59 | -3.24537 | -53.64751 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5efa4bbf-1ef6-3f17-94d8-6bcbdef5848c | -4.89696 | -41.31753 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0db45cbb-5525-3907-a83e-447b214e7163 | -3.54457 | -50.40704 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbde0eb0-2573-3d00-a599-6d6650ee18d1 | -3.03564 | -54.03881 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 799005d8-3503-3e5e-add9-4b5cc544fbba | -4.97488 | -49.99871 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f714f5a-8325-3050-898d-2193a82ea698 | -3.09786 | -51.06849 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f8b944d-cd7e-3559-8071-64bcbbf2fad5 | -1.07409 | -53.20924 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4edf76a-718d-35c6-bc30-1377e9a88787 | -4.25599 | -50.59257 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 126a4651-e7f4-35aa-90e4-e5a3bce5b8fe | -2.23339 | -53.62606 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 479ea2bb-2da9-3df8-adf2-178bf2101d66 | -3.11063 | -53.27682 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee70efa-4d36-33dc-90d3-d017eec07b71 | -4.53655 | -45.70108 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5c7ebccf-15ea-3799-b3c4-74ec7f4ea015 | -2.82285 | -54.06431 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README45.md)
