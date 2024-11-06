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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4146f14c-3054-375c-a2ca-856ebfc93026 | -3.03327 | -53.27323 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fb67b603-f390-35e9-9202-af940213e954 | -2.93425 | -51.05446 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8ab7279b-b48a-390f-8336-09a7ca6047d6 | -1.49524 | -60.37468 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01744ee0-5c87-3e2e-b86d-581981a78060 | -3.32692 | -51.62287 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1ef586a-307e-3730-a6f8-f44c40b24407 | -3.66761 | -50.22673 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7b27541-4da9-3f71-9c54-b2d0a9995e1e | -2.83217 | -52.90316 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 29858bad-a347-3a7b-bf37-e2ad62409834 | -11.7771 | -64.98553 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40217700-52ff-3800-9328-757abc571dab | -2.81599 | -52.90653 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a17b2441-b723-3451-8563-d6868c9ca82e | -3.89482 | -50.25532 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da3d319-90cc-3320-96ff-05b69e162997 | -2.81659 | -52.9376 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0302cf17-44ee-3ce2-95f5-7a87c43ccacd | -2.82766 | -52.93326 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d46eed2f-784d-3889-989f-dd61ae1cbbd9 | -3.59404 | -51.57605 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca9a98c5-1345-3b06-a2cd-feb56349d0d1 | -3.01474 | -53.43646 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 236634f3-2bd3-39c7-9ca4-2c096889bf16 | -2.84193 | -52.90774 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 804f5abe-ed74-387e-b0f3-24cfb8fdfa11 | -3.35666 | -50.25214 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a6c0269-652a-32a6-b5d3-21721a7e6613 | -3.67234 | -50.23747 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7e3cf133-e4a1-3c2d-b7af-7444ad8e37ef | -2.83752 | -51.80618 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c9aaa46-4d63-3d83-842c-e430e380fa1a | -2.82989 | -52.91837 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a75d0c7-b39f-3737-9bcc-96b2601e77e9 | -2.77817 | -54.72937 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6bf0617-bf84-32f3-b07d-e864ab738aed | -3.0287 | -53.26955 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b00f45c-927a-3b6c-be24-9ed387f71b6a | -2.78931 | -52.87473 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 065b1db1-b0b1-338c-b134-1088aa176b3e | -3.21843 | -50.3801 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 06d2cf55-f54c-3771-b48f-e176614c4f54 | -3.66549 | -50.23677 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1bcb6bc2-bd58-37e6-87c9-1aede7906d29 | -2.88648 | -51.66463 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0588d08-43aa-321b-be68-a80e155e2c4c | -1.06648 | -62.6594 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2977273-1f11-3fef-afb5-563036b4a32d | -2.85274 | -51.77901 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c0330ed9-2b03-3eb6-88d3-8d658d300cc3 | -2.97901 | -50.30316 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 464cfc00-6a44-3b44-9521-e07ff396d7e0 | -2.82167 | -52.9385 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac6d4f30-31e1-3a7d-b884-279c3becf391 | -3.15668 | -50.20316 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 90368784-1ef5-3af5-98dc-1943f5415798 | -2.84723 | -51.77814 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 586724fb-be92-326a-9875-ce928e2d38ac | -4.27285 | -50.72153 | 2024-11-06 05:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2983836-902f-3343-8522-d4de6fbe24f6 | -2.8831 | -51.31584 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6481128-6ce9-35af-878a-f08caf1ef87a | -2.9239 | -51.04448 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 262719b4-4813-3ec8-bb30-0026197e461e | -3.17382 | -54.47017 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d2bb8e0-2d9b-389b-8feb-95dc71735b5d | -2.17257 | -53.70481 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 452f3c3d-58b0-3989-bf4f-ad8aa53915ca | -3.12096 | -54.25417 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4410cf6f-c816-3c0f-81b8-b5c2e703b4d6 | -3.97249 | -48.16658 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e90ec240-6169-34b7-82c4-46e669b0d779 | -2.82017 | -52.91355 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8d31c3f-aa64-3da5-b625-e3248c3d0c11 | -3.09107 | -50.26526 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 207f75d7-3ffa-3eb3-88d7-e9d22824b455 | -3.1226 | -51.10764 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f007e6d-1861-3634-a793-0c502997d4ea | -3.29689 | -53.11543 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58ec3225-63ca-3001-9e1f-ed5c9571986b | -3.12839 | -51.10845 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18865ff7-26cb-30dc-a17b-afd22962fa6f | -3.87646 | -52.37955 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 123aade1-2d72-3804-99c6-3f9cfc33d36f | -2.91166 | -51.04859 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| eca57595-ad22-3933-bcd1-41cb0b30e511 | -3.48803 | -52.10192 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a51b931c-f7de-3145-8e25-a586554e09ae | -3.03491 | -53.26109 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af8f6bd3-b2c1-3a82-8d5b-aec5aa0cd2ae | -3.19897 | -53.22632 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 295d39bf-ee9f-305e-bafc-471603238b6e | -2.71606 | -52.95916 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6bca499-67c1-3056-9b8e-0871869efedc | -2.83633 | -52.91023 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fa26a64b-8928-39fc-b62d-859ac6cf2770 | -2.60125 | -51.30215 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d02bb64-51f9-32f3-9bf0-db94b0065b22 | -3.85557 | -52.1398 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a3b6449-1743-33a9-a185-3e958df6e292 | -2.71543 | -60.97095 | 2024-11-06 05:31:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb872b80-6043-3441-9bb4-600bbeabbeb3 | -3.8029 | -51.41446 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fda96e88-90d2-3ef2-91d4-b2b0a3b4c86a | -2.81942 | -52.95359 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 34d3d0cb-d116-3182-9e4d-c152a1494c16 | -2.5792 | -51.33413 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00ebece4-82f8-3855-8647-4cc5624a739c | -4.08869 | -51.04162 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b42ac9d-a808-3d26-8187-78e780886b69 | -9.44948 | -68.53344 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cddc403c-3b81-3652-9286-cef0b4d36b0e | -2.82436 | -52.92046 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48a115b4-822f-35eb-bfd2-d6750b67b1c8 | -2.94214 | -54.80058 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc906286-b166-37dc-a9ec-ebb6c00a96f4 | -8.03167 | -70.92979 | 2024-11-06 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ef94b3-d4e3-330f-a328-8956056407dc | -3.64236 | -50.13899 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dbe11809-1e8f-3670-8f85-444d8f893ee4 | -11.79041 | -64.83755 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4445087c-bdde-3b86-9fce-bdf312e9f3f2 | -3.0205 | -53.43159 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23921f4a-ebda-38cb-8006-63ea5cef35e6 | -9.45036 | -66.63783 | 2024-11-06 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ca33448-b7fe-344e-bcf6-f81377238ec1 | -11.79261 | -64.84538 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6033cc40-777d-3d1c-afc9-13a634c42fa8 | -3.66229 | -52.33949 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 550f81d7-7569-3727-9f5d-b93461443071 | -2.70194 | -61.03577 | 2024-11-06 05:31:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea3aa7d8-ae9b-368e-9b47-a8dda72d2e26 | -3.12169 | -54.24916 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e08ad18d-063c-3ab9-91b1-d6fb8ab5540a | -2.83699 | -51.35234 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b858430-325b-3729-8f3b-7cbf1e574d5b | -4.0986 | -50.50034 | 2024-11-06 05:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf8e58cf-eef8-303e-b4b5-5f89a4f261de | -3.67298 | -50.22824 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ea1c78b-b2da-3f50-bb7e-3815ae642010 | -2.91232 | -51.04269 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cbc8c1ea-0d90-34e7-ba56-ff2cbf700ea6 | -3.20399 | -53.22717 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2b0a3fc-3397-35ef-aedc-c91116ed72eb | -9.60854 | -49.53943 | 2024-11-06 05:31:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26988deb-e5b8-35e5-9b94-14728df542bb | -3.16125 | -50.21355 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 6c7008cf-c226-3825-9661-f94900db708a | -3.00644 | -54.09089 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d5d9747-5638-3f1c-88fd-625f00bb86e3 | -2.84658 | -52.91158 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10226261-3cc4-3924-997e-ca0cde9a9aba | -2.93021 | -51.04306 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55917cea-b557-3796-8457-1e9a7550d5fd | -2.82107 | -52.9075 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a92b53b3-e922-3175-ad74-85bee71a5332 | -3.06185 | -50.50826 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e37841-679b-3a3d-b87f-173a5b3c3197 | -2.81375 | -52.92161 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d375ed6-2ad3-3371-a87c-8f94d397302e | -2.82813 | -52.93013 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0dc0b610-cf5d-3c7e-88c6-257c94bf628b | -3.12364 | -51.10281 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8d534719-64a1-30ca-83a0-578ec6967b60 | -2.72381 | -54.1516 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1747fa32-9cf2-367d-b59d-1405f1f9dfb2 | -1.48861 | -60.37365 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d57e8e-ea8f-300a-9a17-d2a98d96b528 | -12.06988 | -63.14939 | 2024-11-06 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c5f813-788f-396f-a0af-09b331975b82 | -2.91862 | -51.04128 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b58b834a-a2bc-3bea-b9da-096ccec0d810 | -2.97197 | -53.86596 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc689c1a-1a50-381e-98ec-32ab121a5b88 | -2.84208 | -51.35712 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4487042e-2e74-32b5-80a4-5defd7690f75 | -3.0625 | -50.50379 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8157fb-91df-3d0c-83ae-d9db2fba75b5 | -3.77882 | -51.29609 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42092e4d-4b33-366f-8fab-846a3ca0a558 | -2.91686 | -51.05363 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1584001-00eb-3eae-9ae8-43f53edf088a | -11.79481 | -64.85323 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2c77cc-12c8-358e-9b90-24acd2d28004 | -2.91108 | -51.05269 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 739f09a3-5243-3e57-9b38-424a35d44596 | -2.95764 | -53.86349 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aacb6da8-8e17-37d1-9806-65e1af55d578 | -2.80427 | -51.49593 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b256ce0f-2936-3202-b34e-62207e910502 | -3.18048 | -50.59558 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a326719-f4e5-3961-8dca-ea6d8c7d38b0 | -3.03313 | -53.27275 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 75579c2a-6848-3304-89ec-a3c87e1969d7 | -2.93542 | -51.04805 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bb20c8fa-0ab6-3850-8a56-cacd6dee631d | -3.06315 | -50.49937 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README67.md)
