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

## Dados Diários - Página 213

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a1ca094-2f62-3f12-a7ce-b704bd3d335b | -3.56592 | -59.1013 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40161b81-f65a-3933-93fc-374533e4f629 | -3.47632 | -59.51261 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0927cb9-7aa3-33f1-9583-42f553883e5f | -9.09556 | -61.01163 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d290fd3e-17cf-33a9-b359-166d93afb9af | -3.26108 | -59.60553 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cd106a6-87cd-34df-a753-5bed238a0e9f | -3.77872 | -58.4465 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbf7d46-3151-3cef-a3aa-9838b7025fd8 | -2.88164 | -54.18952 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 123a6dbd-f8d2-3380-b5c8-05b84e7346b3 | -7.00415 | -59.10257 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e84d811-a086-3bf2-a7c0-083817785f19 | -6.48539 | -62.85094 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ebf0967-93da-33f4-9b2d-8fcdba6a6a9c | -3.94203 | -59.79238 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b655d9bc-ba93-38f7-83e6-28b9f0b1eac8 | -2.71055 | -57.46396 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e12978b-492f-33f7-8962-48a9594ce1bb | -3.73581 | -59.46394 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04a27626-0499-31b8-b828-9bd624d7c143 | -2.70509 | -59.51085 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9651e105-a730-31cc-a887-a99f1e29bb51 | -2.78156 | -54.06799 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edfe5f0-d537-396f-9e04-d0ce9696121b | -2.46334 | -56.06475 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7798a5dd-983e-37c3-b013-32dc2c76b492 | -3.73595 | -57.16097 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68962b1f-a9f5-39d1-984b-c23d8c444cbc | -2.22809 | -58.10989 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 60cb6490-522b-3d1c-820b-bc61bebb6381 | -6.72858 | -63.05101 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf66f28c-d01c-33b3-b67f-dbf8dfcb74fb | -3.35623 | -50.40682 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fdfbca6-3a54-3f8b-a626-ea8b6221954b | -3.65289 | -59.70343 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61c96764-aea8-356c-94c5-a38f2f1c9247 | -3.59486 | -54.3126 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8306393-4c34-3d0e-b8d2-ff074bd8c400 | -2.73917 | -54.13868 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86e872c0-e14e-3e77-b97c-db136ab22dc3 | -2.60692 | -57.51907 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 113e07ea-fdc3-3bdb-b0a5-dac65d1afd66 | -3.27197 | -50.39414 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2070cdb1-1736-3b08-a018-ef230182bfbc | -2.74518 | -54.12516 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49e1818b-de4e-3cac-afbc-059bbf08fd0a | -3.92721 | -56.0378 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4761b64f-1720-3b5a-bda7-5e04865ca89f | -3.55703 | -59.50017 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d1a98a8-cbdb-3ae4-b466-f8fc9f23a996 | -3.26652 | -54.026 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25c59f7c-60fb-3829-8e22-afa4efebdd2f | -3.89903 | -55.89034 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9f14699-53c6-3997-b229-2084e9a97217 | -2.584 | -56.14455 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 590ddded-812e-318a-9c9e-30a034cffa85 | -3.18868 | -60.05676 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a75cb29-5c27-3b3b-aa76-5f1804cea6b5 | -9.87472 | -50.49549 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d638c310-09b8-3fcf-851c-368407070692 | -3.92289 | -55.85338 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d64a23b5-3edb-3b89-a87d-78e40435281f | -3.60589 | -54.56675 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f87f9dc-89e9-323f-8ee9-9ad97f2e41c4 | -2.85171 | -59.10629 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845428c9-d9ca-372c-8711-1ccd75a12cad | -3.5077 | -59.33803 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb81b937-4b69-3a19-9721-30236f5efcae | 0.52652 | -50.8993 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6250ecac-fb88-361e-af24-86467c5459bb | -3.59915 | -61.61867 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 398666cc-a227-3c39-9e49-fddc459d9245 | -2.89178 | -54.91196 | 2026-10-09 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec64874-c921-3a61-8795-4d636b947ad9 | -3.11508 | -53.78304 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 468804e2-783a-3e02-82c2-45a932b391f8 | -3.4527 | -59.55948 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60915a42-02a1-3a60-be70-2ab327417b57 | -2.57929 | -56.17058 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d68e1cf-949d-32c7-b60f-96b41891d835 | -3.50319 | -59.26229 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f9e6791-8ea2-38c5-b58d-511f7d665072 | -3.51546 | -59.35357 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a56f319e-1f20-3bce-874e-1520ecdbea51 | -3.17174 | -61.4832 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c124f2f-6649-3e17-b00e-dd648f5e641e | -3.34998 | -50.47999 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eeb0c0b2-8d07-33f9-b141-4d8d81318055 | -1.82506 | -55.03576 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 339a8eab-1b3d-3943-b68f-0391e164a56b | -2.13251 | -56.69511 | 2026-10-09 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42f31995-c123-3f3e-afa8-b6d80096fb17 | -1.42149 | -54.62505 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d6b02b9-e81e-3147-823a-f523ecb692ec | -4.46889 | -55.90343 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f377c35-d385-3d2d-947c-8bea65bc278f | -3.58807 | -54.68421 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f87a393-3208-3cc5-a393-d1d6609ad230 | -2.42967 | -55.98594 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03cfaa53-caf6-365a-9ad9-dcef3ef4e882 | -2.74883 | -54.10166 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbf7d7b6-a4fc-3f3e-9946-a756761b34b8 | -3.79855 | -59.36997 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68550018-111d-39cc-bf3a-5984b701a53d | -4.35906 | -55.22078 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1460f96b-2ec8-30ea-a30f-3d174d17285a | -3.25628 | -50.39751 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9f2f1a2-ae90-346f-b0da-093f00f2cc5b | -3.19049 | -50.555 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca0b930-b58f-38b8-ba07-ef385ae12ed3 | -2.16036 | -59.24446 | 2026-10-09 05:23:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f18a2e0-6725-378a-bc14-9814dfbbd558 | -8.7046 | -62.4196 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dea216f-376b-3213-9f19-ee65a04c2350 | -8.30245 | -54.70174 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c942844f-8c6b-39f1-ad53-3698cc618f69 | -1.10027 | -54.16793 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0bddde9-e9f1-3785-843b-018834f01f19 | 1.17222 | -60.3696 | 2026-10-09 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a66fa49e-a3bd-3d91-bbc5-4d7d69df0624 | -3.3261 | -58.1492 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 806aa3da-8f4a-38a6-9939-ab7a742407c3 | -3.05349 | -54.02873 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcce4ada-0741-33d1-a956-b73ebe9aedc6 | -3.09504 | -58.02084 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f9aca1-786c-3b8d-bcc2-496bf69b1cc2 | -9.27779 | -47.43719 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9cafc77c-5d40-31b3-8029-5c5b93df3a13 | -1.52603 | -56.11807 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee29fda7-de5f-3747-a369-5caa26a40dc1 | -1.52545 | -56.12177 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d20af7b9-bf1d-3f15-a724-b380edc20f01 | -9.88108 | -50.48884 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e0dcd4-ddad-3298-b547-862473e30cc6 | -4.55415 | -54.97083 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c0525ff3-c7af-3200-8b1e-de860b47b2f6 | -2.85116 | -59.10976 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 913b0aef-35c9-33b8-9b40-9ce865d86c12 | -2.84585 | -54.12365 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0f924d7-255d-3b5c-8e6e-c077a69551e2 | -3.03769 | -53.89738 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feb947df-3779-3417-bb33-e4a813d6dd97 | -2.49055 | -56.0645 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debfe672-c95d-33b0-bcf6-e4799e796a0f | -2.9962 | -53.90399 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cb3a310d-e2a7-366b-b53e-f3c54dc6059c | -2.57566 | -57.13462 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81fd6709-1b84-3d0a-b75c-50b5d3e87d6c | -4.55347 | -54.97529 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 911e508c-b276-3354-bae3-6b9b58784f78 | 1.98127 | -60.61423 | 2026-10-09 05:23:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de1b1487-c6f0-3df1-95df-d7534ff16f3d | -3.18378 | -58.64129 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bf3dd22-8361-3aa6-9596-a468c9f68848 | -3.97025 | -59.33612 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6cfe18-265e-36ae-bc09-0e2180e1eeb0 | -9.2285 | -60.87545 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88dc2adc-c49d-3aaf-b48c-800d123bde8c | -3.71218 | -59.65483 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c84345a-0756-3311-b4b3-4305abaea869 | -6.73383 | -63.04263 | 2026-10-09 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eaa9636-8eb0-34e8-919f-9da87af16179 | -3.16538 | -58.62775 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8d55fc8-3bef-3e83-9489-b414256d2170 | -3.59151 | -61.64291 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62b5365b-fedd-3511-a11e-4afb81079c3c | -3.63307 | -60.62925 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92eb002f-03fc-3422-803d-797a6740fb3e | -2.84895 | -54.12895 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6dd3c17-245a-3982-b0b0-6180f427673c | -3.90485 | -55.89928 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dc73c60e-446d-318a-a159-8ea3a41a2761 | -2.58792 | -56.16036 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5e47dd1-7863-38a0-b080-5fd3ede922c6 | -6.49209 | -62.85662 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 722be2c1-b01b-3f25-a0f4-3e89cb9ac2ff | -3.5539 | -58.70676 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 393ba67b-fd77-3b0e-9599-0a53a665e3e8 | -9.21354 | -57.72549 | 2026-10-09 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ef311f2-3f03-3778-9084-b52723676146 | -3.00895 | -57.16549 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71f58367-5ec6-3cac-88ac-c2cfa0d7c2d4 | -3.00887 | -51.00875 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36035769-0c94-379e-b87a-798647e25b76 | -2.74135 | -54.12458 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b314015-fef6-304f-a5bd-61364ff1fee3 | -2.99783 | -53.91914 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 29d31223-73c0-3af5-ae23-07f56bb337cb | -3.0791 | -54.29367 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07df0d56-48fc-35ce-babd-d5b9349f6fd0 | -3.56316 | -59.09732 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a0cd6ce-e470-304d-a423-17083ce4b8b8 | -2.58216 | -56.17485 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbfbb65c-39b9-3e54-8f82-7251640cb9ae | -5.68331 | -53.47761 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95c30000-c353-3397-80c0-9d003f3cad27 | -12.227 | -57.10965 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README214.md)
