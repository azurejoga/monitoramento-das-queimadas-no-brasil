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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49aac5d2-e078-3265-94dd-b457cfff2f31 | 3.9792 | -60.47324 | 2026-09-26 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6007b55c-b95b-3b09-97b6-4f313cdc5a21 | 2.94022 | -61.26647 | 2026-09-26 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 366ea674-d55d-39f1-a376-91cbd296e084 | 2.35805 | -50.77378 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4083d03d-26a9-3d37-bf37-0ca9bb0afcc5 | 2.11149 | -50.84507 | 2026-09-26 05:08:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eb135de-47c5-3669-80e7-258fd0a124e6 | 1.30033 | -50.83213 | 2026-09-26 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78e9d587-98e9-3111-a5d9-442a41d6eb4d | 2.62133 | -50.88945 | 2026-09-26 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c76c4147-8fc2-3fcf-b421-72b8ed95d0ab | 3.97512 | -60.47384 | 2026-09-26 05:08:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 756325ff-47ef-3105-9015-c7f4d37a1581 | 2.7157 | -60.68722 | 2026-09-26 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aff3587e-a613-3f64-93e3-5b2c74ac797e | -3.27292 | -50.14246 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d652c763-c15d-37ef-a094-a46f2cca3a99 | -3.50226 | -50.74328 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39d5b36a-1772-3ebe-8d49-1b4c4a4034d2 | -3.20194 | -53.41231 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f1aa413-c612-31de-8bd9-144737592d1d | -4.48893 | -56.09092 | 2026-09-26 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 766656c8-dd51-36f1-a551-47388a4e0735 | 1.61085 | -55.85019 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 381e7929-7074-3c2c-9cac-83e76ef4e17a | -6.00397 | -44.91102 | 2026-09-26 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02716c5e-6e47-3723-867e-08128ec2c995 | -4.44531 | -55.03038 | 2026-09-26 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e80bd599-329c-35b2-94dd-8beae5af1a02 | -1.33635 | -55.47435 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc171feb-6cca-3587-be2a-ec8ae2167288 | -3.56576 | -54.50115 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 958aa689-68ab-32c4-9be0-5571d5df22c4 | -2.89285 | -54.19284 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb993b20-540a-3c87-b746-d5cd0bfec84a | -2.90072 | -54.09367 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 42455231-b355-3d67-bd98-50a862d82ffa | -1.14256 | -54.08608 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c1bf3db-0d12-3a0c-be5b-eabb4702f21b | -1.33913 | -55.47835 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ca32a0d5-c9a2-3d3e-819a-a43374f58b65 | -2.79892 | -57.67727 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c574fd8-5894-36e2-9253-a2ab32a08139 | -1.11472 | -57.06801 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99391fcd-23c4-3942-9beb-6aa69bc63a25 | -3.14252 | -54.57909 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba9f827-07a9-35b6-a4d4-08885d2fdb7b | -5.73891 | -45.05668 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0b488a72-d496-34b2-a0e6-689c9375b719 | -5.06839 | -56.06118 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0536854c-8382-3d86-abda-e4c920343f75 | -3.26915 | -50.14836 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7f7ee883-34f8-3a93-8d17-e44e26ca9606 | -1.14964 | -54.10189 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4891ef65-1e9b-35ea-9c52-b8dedfb25096 | -4.30857 | -49.12001 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cbaf0bb-7868-3044-b459-a5a4e779e2b9 | -1.98326 | -56.69377 | 2026-09-26 05:10:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4e52273-3cec-387d-ba15-fb46860549da | -3.41381 | -51.66363 | 2026-09-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a7c2560-80b9-3a22-afbd-1d8aeaff619a | 1.58631 | -56.06082 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4ac6a1a-5aa0-3182-8a96-2e42f2879992 | -3.06639 | -54.02836 | 2026-09-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 061b2ffb-ea84-3209-a608-face9e13587b | -1.343 | -55.47537 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a0f071c-5b9f-3fd5-8020-498cbc40ea13 | -2.93296 | -56.5794 | 2026-09-26 05:10:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e6e2bfc-c456-3b7e-a93d-ad7f10218e8c | -3.01512 | -54.19838 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc297ab-05b4-3221-8ae8-91d805aa10f9 | -1.3035 | -54.22245 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47f87985-6c40-3ed1-b3ff-6e8c0a757f1e | -3.00108 | -50.47442 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1546324f-ff0c-312e-af90-9bb983106503 | -2.90829 | -54.11502 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 03b8c11c-0b61-3d97-8814-e785fd94ecce | -3.26385 | -54.27504 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1330f9d-46e6-358e-b60a-a1e46210690f | -3.7139 | -54.65168 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6083112f-8c4e-3cff-803c-af7de5a05d4b | -3.50288 | -50.73902 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b9fec19-f623-3d0e-96bc-37d7a5e51606 | -1.1391 | -54.08556 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 42062189-518a-38f3-ab4d-801a324c4600 | -1.14676 | -54.09755 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 059f8c3a-5666-3cec-9507-1bdd34f3a4fe | -2.9965 | -50.47584 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fda5f92-dc0a-3371-a45b-800a136f41ff | -5.77767 | -45.11193 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a5d6015d-c116-3089-8647-712fd0af71c2 | -5.0673 | -56.06825 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee626716-6543-361a-bf85-ab39c795bb10 | -2.99712 | -50.47156 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c130124-aa09-3da5-a114-921fe8becdf1 | -5.74477 | -45.06279 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0ef41d47-8fcc-3122-9f00-7278b39686da | -2.46601 | -50.22966 | 2026-09-26 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3577b2c0-0bbf-31b0-97c9-92d83c593ae7 | -3.69023 | -54.2602 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 480dcea4-5504-314a-af02-b822cf0ef208 | -2.4689 | -57.93862 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7487ec-fd3f-353c-97fe-f2d19dc2b058 | -1.68952 | -55.5653 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb9852e-8b84-3c40-accb-27048caf593c | -5.68553 | -45.8662 | 2026-09-26 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b279e3a-f1e5-357c-a602-346aeb4d9356 | -3.22747 | -54.32517 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0828aea3-c81b-347d-8ad5-27a291f209f0 | -5.37158 | -56.05673 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22342876-6fa6-3565-be11-3ee8a8759f93 | -3.80362 | -51.02076 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23c6a81c-4c67-3017-92bc-5c051a89e1ef | -1.31577 | -54.57343 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f78e3596-79a8-33e0-9d77-7fc8b390e7a4 | -1.14423 | -54.09798 | 2026-09-26 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6eb5121-92bb-31cd-a0a4-155a21af892c | -4.44818 | -55.03456 | 2026-09-26 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c2dd93-3ac6-39d4-87c0-728376c89753 | -3.00752 | -54.20116 | 2026-09-26 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48cdb0d9-dcb7-35a7-b9b6-bdb9629f73a8 | -2.15112 | -53.71282 | 2026-09-26 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4eccdf17-9dee-3963-85cd-ccb9707b2ec9 | -3.69374 | -54.26078 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 140cb3a3-1d36-3b0d-aab4-fe00ceecef20 | -4.38581 | -55.02873 | 2026-09-26 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76eab92c-9ed7-3964-af17-162ecabd04a6 | -3.5022 | -53.45724 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 330bd9a7-0b86-3fde-a37f-180bf48982a2 | -3.21914 | -48.81835 | 2026-09-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ca90f7c-1f5b-3842-9d69-a24e46c7ee9a | -3.96615 | -56.12813 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f1f32f-c8f6-3787-97d3-6556e4dfc282 | -3.72141 | -54.64895 | 2026-09-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08c77cf5-8eb6-3301-8c7c-ceb2b5b61089 | -2.15803 | -51.97759 | 2026-09-26 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01b725f3-3e48-3505-b15d-893a39a75f70 | -4.47134 | -54.90699 | 2026-09-26 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc74626-5b88-3afc-880c-f58272cd0b4a | -5.73819 | -45.06206 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ab050ad-69ee-38f4-ba73-53c54304a499 | -2.84027 | -51.38067 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5058b760-c0bb-3c80-accb-f67b9843f458 | -3.98809 | -48.42944 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8aef46f-9365-3a8d-917a-42e4e45a8171 | -1.74562 | -55.24654 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d99e3a7d-7e46-3426-8dbd-c05f1dc1131e | -2.00904 | -56.94381 | 2026-09-26 05:10:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45ccc91b-21ae-32b8-ab28-db055cacce2a | -3.22688 | -54.32904 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4bd573c-1746-34a2-b8b8-081dc00a921c | -3.80684 | -49.17845 | 2026-09-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0ceb9b1-67f2-3a6f-adaa-56a14c764d4f | -5.23614 | -56.0066 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a684ffa-c851-3d41-9b7e-6eb1172fa559 | -3.83594 | -55.91463 | 2026-09-26 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c6efcd0-19b2-314a-b95e-ae4cf50252a7 | -3.50106 | -50.74112 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d26cb3fd-0a06-30b0-b31f-1f4ccdddb67b | -4.87942 | -55.8539 | 2026-09-26 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d63ea753-16fa-3fdd-9a27-e59801a764fc | -2.47281 | -57.9356 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 197c2263-a1f5-3163-a40b-bca74918af8c | -3.22978 | -54.33344 | 2026-09-26 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ebbe503-a765-3af5-9ac1-a4a8e606aa32 | -4.12211 | -51.06084 | 2026-09-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21787cd8-fb65-3fb8-9523-7f46594c1f22 | -4.4574 | -47.9211 | 2026-09-26 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d57cd85f-5002-3bf9-ac03-21f8159935fb | -2.72838 | -57.52015 | 2026-09-26 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61a1572a-62f1-3001-b61a-bc809f9e4e82 | -5.6864 | -45.87141 | 2026-09-26 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fec66eb6-e0a7-30ca-b51a-fe9ea021fba9 | -3.27223 | -50.14698 | 2026-09-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 040c4387-8dcb-39d0-86d4-bf6886976753 | -1.94568 | -56.32301 | 2026-09-26 05:10:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8bfb912-ac2f-352a-aaa5-e185e7031be0 | -1.69284 | -55.56582 | 2026-09-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de946072-d699-3a70-b37d-15d175bcd249 | -2.88377 | -54.0834 | 2026-09-26 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9fad3f-79ce-3f66-96b2-66da7f4a49be | -2.27885 | -57.00026 | 2026-09-26 05:10:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 026a5c42-0ebd-3bda-be0c-5115e9cc2920 | -5.74329 | -45.0738 | 2026-09-26 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a006a251-da71-349d-a928-7e5f10e4792a | -0.49783 | -49.15534 | 2026-09-26 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af6152f5-4670-39fc-9c73-e9200fb7834a | -2.46611 | -57.93457 | 2026-09-26 05:10:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea30849f-52b0-3613-94a4-b7e9f68d1308 | 0.07599 | -51.14517 | 2026-09-26 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46662c8e-e992-3e5d-ac83-76b90289d185 | 1.63996 | -55.97188 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ad10df7-8acb-3c76-ac16-55fc7b5dcca6 | -3.49919 | -53.45242 | 2026-09-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67bb8d79-3639-3c31-b05e-ac3bffa844fe | 1.60809 | -55.85412 | 2026-09-26 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3718f18-01d3-3bb8-83b2-f6199dcfbfcf | -4.44474 | -55.03405 | 2026-09-26 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
