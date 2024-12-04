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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76910022-672b-32d1-8262-0dfbbaf55597 | -2.57426 | -54.8066 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 319fe670-c7e6-35af-98ef-0da83f099bea | -2.85182 | -46.69 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64391403-c025-3e5c-bba8-adbad9574ba8 | -3.29984 | -53.67381 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb1825ab-e016-33a0-a9e7-7ffa6a404d52 | -3.15193 | -54.48258 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16fdba49-d16b-3aa0-a2a9-b36ae3559229 | -3.25492 | -53.57415 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ccaec7-2950-3453-b7fb-c17f72e85587 | -2.78501 | -55.37449 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c4fd03d-80d1-34e0-8516-66e100b722ba | -2.67297 | -52.45636 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37460ae9-5ee8-3486-a84b-0772f6516028 | -2.69613 | -52.91967 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b843c441-f326-36f2-9e7d-c81ad7003732 | -2.73394 | -54.04174 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68e7fb7-71fb-3ce1-b63b-75994531d3fa | -2.86359 | -54.01806 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32a54e5f-1b9a-392f-88c0-314da6477fda | -1.99816 | -53.28331 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fa0ac7f-14b2-31c3-b91e-98e511ee86e4 | -2.81214 | -53.05673 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbddfaae-55fe-30f9-b4f1-5e3758b7d45e | -1.90263 | -52.90192 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be5b4c1c-70af-325f-b76f-9f81651fd724 | -2.99282 | -54.91417 | 2024-12-04 05:03:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcc7bd15-9af6-3e39-8306-3c0e7f3225dd | -3.86445 | -52.31006 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2699e114-c0df-33de-996c-fef7d8d59d92 | -2.45026 | -53.96539 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 942639a3-acdc-3aa3-ad10-2ea30569d4a1 | -3.2512 | -54.21472 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dafdb97-ac6e-3b06-a45d-7122712e55d8 | -2.57043 | -54.00198 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| deafa4ae-5e3f-32b7-ad19-558a6d593484 | -3.18421 | -54.34104 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef19395-cfd6-3b45-98c7-fd4ae551231c | -3.07533 | -53.76521 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db569f8c-ed9e-33be-890c-40bf3e22cb45 | -1.75548 | -52.62827 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9e34e0c0-010c-3370-a1fb-0dd7387aa155 | 2.42224 | -60.65245 | 2024-12-04 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38285b88-8cfe-38d2-a76c-ed13112bb991 | -3.26305 | -53.83489 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fc3ec3d-619b-35fa-b526-07eda38ac82c | -3.36794 | -50.39011 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed00715-fd33-3bb6-b89d-882f3c23935c | -2.79491 | -53.05407 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e40c8a8-7bd4-3567-895b-b175e9020f53 | -2.46096 | -45.15017 | 2024-12-04 05:03:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f572883e-59ed-3b5d-a8b7-d39fbe8d16c7 | -1.33905 | -54.96175 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54cae7d8-9164-30f4-8e49-4a8bbc17e022 | -2.87478 | -54.03428 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 368e44e7-9f3b-32a4-9fda-626986b84b89 | -1.73807 | -52.64906 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e132fac-30b8-3f26-a6ba-0f4f0d8641d4 | -1.32729 | -52.5615 | 2024-12-04 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d1219ba-d2a2-3aa4-8519-d258712135cd | -2.23534 | -53.65945 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61aaeab6-4079-3a9c-9568-c784a4427624 | -2.79893 | -53.05083 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5780d4a-567a-3d3e-81a7-2b558774b201 | -3.74007 | -51.69319 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cb54a9-e6dc-3a39-8a22-78445e67b3d9 | -1.69757 | -52.6438 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c7474ed-03e8-3e4f-9848-53ef8b348592 | -1.95409 | -53.34363 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a2eece-f522-3069-873a-2d197584730b | -1.07329 | -62.64059 | 2024-12-04 05:03:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f6dd8aa-f126-31de-9239-73fd0c36daf9 | -2.36791 | -53.66132 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32bef8cb-7277-32c9-a3b5-43f82eb08a30 | -2.81617 | -53.05349 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303039df-bcca-3b68-bb09-d444b2fc47cb | -3.25669 | -50.57479 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4798623-9dad-34ef-8389-fd9130a5d6ad | -3.68238 | -50.25977 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a63da5f-d914-3e1e-9b3a-46a79cc9da46 | -3.05737 | -52.76064 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731b6fa2-073a-3fee-9319-e97929f71f15 | -3.39188 | -50.31123 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df5f625-bdc8-3fe7-aa86-449a112c2509 | -2.97662 | -53.87892 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 549d5620-9234-3391-a7bd-85ed1be413b7 | -3.25098 | -54.14958 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34a1586c-4c77-38c0-979e-75c804f133b3 | -2.81098 | -53.06425 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5731ee52-6c84-39e5-a510-a9c6850903d5 | -1.51457 | -54.55676 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bce37dab-1f50-3694-b408-71387892d361 | -3.90162 | -52.16191 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f44f321c-7b8e-374a-bb03-73221954e7ca | -2.54607 | -53.41518 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54e62b16-1d04-358e-a37a-f45da3548187 | -2.7843 | -55.3357 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08427ee3-718c-3541-8bcb-405f272979b7 | -3.8139 | -51.65894 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d249f81c-94ae-3eef-8033-f5adfa28ddd5 | -2.61416 | -60.02647 | 2024-12-04 05:03:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 251b9791-11e9-3a58-a7c2-7870f133f4a1 | -3.13529 | -54.17183 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcf93dd6-4693-3a6c-8756-6d49206d7dab | -1.69826 | -52.61653 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29272b41-a33d-3920-8c84-ca13be1ea244 | -2.80738 | -54.04922 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5367efbf-4d1a-3124-953e-e69bf6e3db61 | -3.80139 | -50.98239 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9646a18b-6149-3fb6-8f5b-d927917320b1 | -2.80519 | -52.37332 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d2660e-7fa6-314c-8f89-ca0336551474 | -3.08146 | -53.37905 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f059cd48-630c-3bb0-9cbc-20ab04cfb9fb | -2.81224 | -55.30838 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78a54d9b-b44d-3c2b-b8dc-dbca6b3bd476 | -2.4081 | -53.8611 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94d5b2d4-fb5c-39c5-b8ac-5d45576ad6b2 | -1.23551 | -51.62265 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 369719f2-dc65-3adc-9142-e98968ae8174 | -2.22647 | -53.69468 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d42ebd1-5a12-3149-bec6-a4feb5b07223 | -1.78979 | -52.75044 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8e6270f-39bd-3df9-9cc3-edc95987f230 | -3.1342 | -54.17891 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5f5b56f-c460-3907-9efb-6049b7c19571 | -2.7876 | -55.33621 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d68c7955-5186-3283-996e-10ab4f05e4ff | -3.11959 | -53.99168 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5ea0134-7393-3a9d-8a49-c5ad06d382ef | -2.45724 | -53.63118 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0c9e5fe-76c1-3c53-8312-fa06773ab7cc | -3.12807 | -54.61399 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 1f8bacbf-cd36-3fad-97d8-a24bb58a2dfa | -3.05678 | -52.76455 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32625a12-c565-394f-82aa-23559b9d3a80 | -3.54837 | -50.1811 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7509557-5beb-3713-b764-6131ee1c2e8f | -3.408 | -51.24726 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8448ea29-e5d4-3222-ab87-765b44f8416a | -2.76678 | -54.02874 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e46d7875-f9a8-3248-9390-b07aca4a6a58 | -2.79835 | -53.0546 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15ceb92a-602f-3f19-9c33-a5a25de2a00b | -1.38802 | -53.55526 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a38c93e-035e-3e98-84cc-15524c4e638c | -2.03869 | -53.94482 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 055dab30-297f-3d92-8ea1-2adf6f49d84d | -4.27374 | -50.67509 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de1f88d3-c2fa-328d-9df5-c83527c42955 | -3.94392 | -46.63718 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e05b259-d167-3b3e-9e5e-e40f72039ffa | -2.25891 | -51.25618 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1d56618-5c97-3215-a75c-011b63326b74 | -3.5254 | -51.60129 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e413e268-6cb5-3ef5-81fe-588f39cd4463 | -2.36854 | -53.96688 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d555f21a-2129-3e39-848c-b24c5ffbed1c | -1.62173 | -52.6983 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0314d54-e21e-369b-9a97-7d779286e5ed | -3.09066 | -54.04529 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a5d6aae-0c65-35f4-9945-3c67996e4fdb | -2.98841 | -53.89171 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17f6f7a7-2666-3532-94d5-61be53784a58 | -2.42025 | -54.15851 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13066ae3-46da-34ab-9fc9-f36c0e8794db | -3.1347 | -54.61502 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0775d9-ae7e-3aa9-a4a9-f3767dce6f19 | -3.22126 | -53.7253 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d65896d5-cb22-3120-9f9d-7aca903c0d22 | -2.74385 | -54.17641 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6a1957f-94f4-371b-9654-d5b7612b7ae4 | -2.78484 | -55.33227 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30b27cf-af34-3e69-a864-8b1798ee7b84 | -2.5523 | -53.41987 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9ba1af0-afc5-3646-81da-fff6054cc287 | -3.12645 | -54.62437 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 733a84c7-1193-357b-80c8-d9ab57b4381c | -3.26345 | -53.65395 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ea62d2bf-3911-363a-aba5-1098d994bee8 | -3.26475 | -53.86826 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e297d6a-3654-376b-964e-a7771d81169c | -2.90196 | -51.81653 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89f02447-eb70-3ff7-a810-f7416dd0b64c | -3.54886 | -51.34 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96207dca-3a77-3d26-8e3c-85bb308e7481 | -2.63706 | -51.76158 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00cde446-6c1c-3068-8060-8e263ddbbf67 | -3.05598 | -51.0621 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e7fc136-152f-3b9c-a7e8-8ffd4a826a7e | -3.55315 | -51.5182 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6a53770-6b5b-32c7-b2cc-ee3e3edc54c2 | -2.88059 | -54.12904 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5066fcc1-c5fc-332e-ba74-182046daa12f | -2.83697 | -53.32755 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a093b1b-3aa9-357a-8015-c80502317961 | -2.90929 | -51.81759 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 322f6347-cf6a-38d1-9285-62e03ca6c165 | -2.81962 | -53.05402 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README47.md)
