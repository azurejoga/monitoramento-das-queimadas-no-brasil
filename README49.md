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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2070f0fd-3577-3b93-b31d-856715746304 | -8.64915 | -66.61092 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 296c68db-596b-3a62-9eec-adb08475f9cd | -9.37155 | -65.84177 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d0d79ceb-bb35-3125-900b-d41d5cbc569e | -8.4033 | -66.08786 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| feea44ac-198d-37b4-8009-ea66d865826e | -9.31635 | -66.63293 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 28874fff-ec2b-3a71-8e3f-b0d702a406e3 | -9.31511 | -66.62386 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ee19c16-52f7-3f21-8215-b5553a55ca02 | -9.30619 | -66.62513 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 823d381e-0901-30e1-bbc5-32d75fd7dce1 | -9.17052 | -67.32127 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 61e77fd8-4741-34ed-bfd0-3d3d1ff34103 | -8.66968 | -67.02426 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0c1822e8-169e-35bb-8d72-49c7147d6c49 | -8.65992 | -66.61221 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1c2c900-2b41-3a9a-8311-f2266becccda | -8.65912 | -66.68293 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 26053819-65d5-3b9b-9511-154f1bd2e613 | -8.65869 | -66.60323 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 210f5249-154c-326b-9638-b3aae5c3027c | -8.65787 | -66.67392 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 2448ec5e-e4c5-3b61-8cf0-dcf0fdfaa540 | -8.6463 | -66.72156 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| cd38230c-7ccb-3a01-9867-82056fa08d02 | -8.64506 | -66.71252 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 8da2e52f-e0d5-3148-86d2-71ae75253776 | -9.98492 | -66.87865 | 2024-10-03 02:09:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9dac60d8-92c6-3b00-86a0-42aa5dafe9df | -9.98367 | -66.86937 | 2024-10-03 02:09:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69a895f5-02c2-3282-ba23-544f17e35c7e | -9.95492 | -66.729 | 2024-10-03 02:09:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0f710a6-8788-3fcf-a9fd-40752e213863 | -9.92531 | -66.78008 | 2024-10-03 02:09:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5021b636-57c8-3e34-b75c-d6bae6e13917 | -9.90849 | -67.33413 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2cae3a2a-72f7-3b43-a369-47340cec7663 | -9.90063 | -67.34502 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e8ef849e-4fe8-3511-aae1-4d9f2172e3df | -9.89934 | -67.33541 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 48e77a80-e0ee-3de2-8f44-cb7deebda353 | -9.89018 | -67.3367 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f1d3a3a2-341a-32e0-9fb3-5d52fd333375 | -9.88232 | -67.3476 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 582fcde5-18a8-3d8a-9b17-76e6d314e34d | -9.75908 | -66.84411 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38c73586-ee44-36db-b01c-7802eda25425 | -9.63512 | -66.81121 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d7a586ff-9432-3b67-9b1b-c48672d7b1a5 | -9.56031 | -66.60461 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a238b3d1-6f8a-3a72-a6d3-9cd2af8a4ecf | -9.47472 | -66.58555 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3c845458-c6c0-339b-858a-4eff09db11f8 | -9.4261 | -67.23846 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d29d298f-8e1f-3686-a96d-9d726b51d0d3 | -9.42482 | -67.22903 | 2024-10-03 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1c15b039-2ee4-346b-818c-b1df9e3c0914 | -9.42323 | -67.35475 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c7a68e00-2694-354b-8978-36ad037a239e | -7.6441 | -67.19833 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d04a175f-2436-348a-b65c-4e91a85ecc68 | -7.63638 | -67.20873 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8165c13a-c7fd-3b4e-8041-8019efbb24a6 | -7.63514 | -67.1996 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 21bd9a10-6b3b-3c27-a381-14b49ba12934 | -7.37684 | -68.01421 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ef5b59c2-c2a8-34d5-bf27-c079d6dbf01b | -7.37019 | -68.02142 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 442019d4-7ccc-3a08-8d6f-51003e4870d0 | -7.36886 | -68.01175 | 2024-10-03 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d05dec57-447c-3853-90e0-ded79157fcb8 | -8.83065 | -67.39325 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8821527f-b65b-3525-99d4-e4b232e9c512 | -8.77094 | -67.69965 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e60f4b51-09d8-3909-95dc-fb65a7ff3037 | -8.76963 | -67.68999 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0aa34f29-7fed-3582-9415-6e8c6cad7d99 | -8.76305 | -67.71062 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 32752513-6a2f-37c7-b108-a2d026600c65 | -8.76174 | -67.70094 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 63df67e9-ffbd-3494-8d94-ccf12b702a0c | -9.42391 | -67.62537 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eff022c3-964f-3f42-983d-67e352b12c1f | -9.42259 | -67.61567 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e07fb934-c596-309a-a2e1-daa694fa8445 | -9.38677 | -67.84121 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 92788466-4ecf-3e17-94ae-6bf7999bacdf | -9.38546 | -67.83125 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9cec259-49da-3bbb-a946-f28c07fdbfbf | -9.36499 | -67.39792 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f35354ee-2961-3156-b1c2-dc3e1c75197d | -9.3637 | -67.38835 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3de45645-cb36-3104-848d-99d552673039 | -9.35586 | -67.39922 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 23f93a43-025d-3ae1-88a0-df27323f6b07 | -9.35457 | -67.38963 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4fe16d77-64da-3dbc-9d11-90620079dce7 | -9.2963 | -67.50158 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82e651c8-eb68-3311-bb21-21c9b6b46c4d | -9.28176 | -67.60195 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 393449a6-80e3-3553-8a20-541e6cd3d62a | -9.27385 | -67.61294 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 27451640-698e-3213-b274-a1860c78441e | -9.27255 | -67.60322 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 55a04c14-8e04-3300-9b9b-af5a69834e12 | -9.26334 | -67.60452 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 924e2205-5a17-3967-a46d-c8629b9286e9 | -9.26205 | -67.59483 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1c783389-b2b8-3f90-abc5-0021974f50c1 | -9.23171 | -67.63462 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f0f6341-9cff-34e1-89fd-88965bfeb59e | -9.1173 | -67.47043 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03fa53d2-7c96-3976-ad72-ef02dfc91ad9 | -9.10419 | -67.5112 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cc9c43c3-9762-3c4f-9dda-f86af1314ba6 | -9.10151 | -67.56047 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d2ea229a-7f86-3ca7-a2a9-6ae27bf4c394 | -9.10021 | -67.55085 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e5a8756d-5bef-3efd-856f-c479a36e78a8 | -9.09632 | -67.52204 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ad4d7f14-54a7-3b27-98a0-abdd1d1308d9 | -9.09503 | -67.51247 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f59635e1-ff60-38fb-a5d0-eba6b654dfee | -9.08975 | -67.54253 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4325fb5-da20-3638-a147-8d9f2f99f238 | -9.08832 | -67.60159 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b15f7e2a-eb75-3ca3-afe0-80deab8557bb | -9.08574 | -67.58229 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b7ef139d-ea91-3412-b036-bb6a0df45883 | -9.08445 | -67.57265 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d9228fd5-2e9f-30df-aa6d-f09f97e307e1 | -9.07896 | -67.67197 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 7bb76c21-c6f1-3868-b96f-80a3ba93a05f | -9.07767 | -67.66226 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 364175a6-4adf-387e-a17f-3127e41da2a0 | -9.05713 | -67.508 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3f1b7a6c-5b85-32ce-a948-b26436faca74 | -9.05002 | -67.51489 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 33b941d6-c1b3-37bd-9e76-b780d2ad6d9a | -9.04871 | -67.50533 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f8bf9c0-5a45-3e3c-aab4-b6cc86c8325c | -9.03826 | -67.49706 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b42f7e9b-0063-3a83-86ea-6fe447d00520 | -9.01356 | -67.38428 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1578dcb2-f928-3356-8d8b-5099ba388257 | -9.00556 | -67.53088 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 805c7808-c498-3254-9e61-6facea289be9 | -8.99151 | -67.35851 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c935208-c78d-3adf-a368-4d067704f7e2 | -8.9901 | -67.41653 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| da92163a-2366-3172-af89-80b22464d81b | -8.98882 | -67.40705 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3bb2bd31-7e20-3235-a236-727a6fc1dc3e | -8.98099 | -67.41782 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 390a6f05-d90f-395a-8d5b-2ded570d0dd6 | -8.97971 | -67.40833 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3c1f839e-1378-3253-be39-fd481e384e14 | -9.39415 | -68.15575 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0ce9bd7a-08ec-399e-874b-3188dc151191 | -9.37122 | -68.2009 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ba7aa19e-e7b8-3689-8a34-f16fb12b01d5 | -9.36869 | -68.32858 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7dc88fa6-81e3-3b85-882a-7f48b315306b | -9.36309 | -68.21253 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 835e134e-7253-327d-b29f-ec28dd9aca4e | -9.36173 | -68.20221 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 14.8 |
| fbe0fb37-2706-3d07-9603-ee3831515474 | -9.35223 | -68.20351 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87563b49-1635-3714-99a9-36046fa924f2 | -9.32387 | -68.24489 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5134d14c-5f3e-3796-bb97-1dd02d2eefbc | -9.28664 | -67.85124 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5044a547-fb69-33f7-b83d-8250f887cea2 | -9.28533 | -67.84134 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e9c4ea8f-3e83-3901-b972-2e017fde9474 | -9.28402 | -67.83141 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 937bccbd-c96f-3fbd-ac0d-96505df49788 | -9.28193 | -68.36767 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ca072ba1-99a3-3515-8fb0-1145e0fd4c82 | -9.28094 | -67.8578 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e074fa3-fc40-3266-a657-3ca00111d3b7 | -9.27958 | -67.84789 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1d1bcb08-c53c-33e6-8ec9-d76198f927d8 | -9.27824 | -67.83799 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3f88b529-b0f4-3a8c-a440-9362d9fa7107 | -9.27568 | -67.88898 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 72cc89c2-c9ca-30eb-bc61-3667f33ae5fa | -9.27432 | -67.87899 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fc4c5811-2fe6-3ce3-a37f-38e5c7a2a7d2 | -9.26624 | -67.81944 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 71567dad-cf00-3ba5-9b52-97b525559378 | -9.265 | -67.88029 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6795fe47-1d0d-347b-85dd-d0e4a0e0271b | -9.25694 | -67.82074 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 37c0f10f-d68a-3bc6-bc4f-74df791fb6d5 | -9.2506 | -68.83104 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 67a7b800-ba57-3ea4-ab89-dc83059b71c5 | -9.24631 | -67.81213 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README50.md)
