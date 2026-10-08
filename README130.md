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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b593143-694d-3f2e-9b00-7500119b76c8 | -3.57442 | -54.3596 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b8c2c8c-7ae0-3972-81e7-fbd628478453 | -8.61108 | -67.01876 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f61cce3-cbbd-348a-999e-f1a988c82d2c | -3.24305 | -46.95885 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad65cb7f-c9ec-3beb-9dc5-af8086314a8b | -2.50191 | -56.15664 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1446e5f0-1bd1-32a9-94e2-b79c67df63c1 | -3.31173 | -54.69764 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d98c01-38eb-38f4-9981-75d1cb567b67 | -1.02577 | -53.74314 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 585b3a75-2653-3556-87e3-e95bed5f895e | -3.10419 | -53.77559 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d1b5f70-9e31-390f-aadd-6bbe7abc3ee1 | -4.15337 | -54.02502 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cda9942b-ad7e-36ab-a94d-f630f02e2672 | -2.75931 | -54.10974 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc4df032-cc4e-332a-8978-0b78a9fbd4f3 | -13.17076 | -54.32271 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d5dd2b0-924b-33b6-aa2b-01d55041be01 | -3.66654 | -60.61068 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f725cd14-7d30-3b4e-a47d-a485065938be | -6.15901 | -52.65458 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c251925c-270a-34d5-9ab6-12568c574ea1 | -3.29397 | -54.01352 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf89933d-7a63-3ea5-8cf4-cd448974c1a4 | -3.02384 | -54.08155 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f268550f-2282-33fd-b2fc-a5428c190129 | -3.03766 | -54.5265 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6a9451-3c62-3f3e-b75f-f164492c45ee | -3.06793 | -54.37719 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950f1839-517d-39f8-b077-d61058d3fd87 | -1.32499 | -56.40671 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2be6b041-06d5-3faa-a8a5-b6cb6a2863c4 | -2.56908 | -56.15638 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 823adfaf-1691-3b51-a23a-4d2ef84e610c | -2.58552 | -54.74191 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf0ab9a-74c6-3473-8f54-357a806ffbeb | -2.46683 | -56.07674 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 205f26d5-062e-3846-833e-cff8a706ccec | -3.08756 | -58.02799 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94b4e3d-2015-350e-a21f-bd24c75944c6 | -1.3658 | -56.91438 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 139d7c14-4f77-379d-924c-c622575c9f33 | -1.1885 | -55.67027 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3906956b-fcd3-3eda-87f8-3feb66c19ae4 | -6.13652 | -53.06773 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e154e09-93c3-3f85-b5f3-48ad5be37202 | -2.98145 | -54.11863 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 94038121-a9ac-34c0-9974-2743cf659c41 | -3.04001 | -54.23 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b336e63d-b8fd-344b-9524-13a8acf210d9 | -1.45786 | -54.76559 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1e8ee8ee-c16b-3e3f-b958-bcb5ccfe8682 | -5.88355 | -53.62167 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a242387f-9738-3e4e-a109-a68b80e57a8d | -3.17901 | -54.60913 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e75cc3-dd59-30a5-b974-e89cfb0b3837 | -4.29273 | -49.08952 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cb1ed22-c7ed-35bf-8278-096869db41ce | -5.23462 | -56.11722 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1627650-e5be-3fbc-8428-ca97a59173f5 | -3.52104 | -54.65316 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34d3fa87-39a5-3f5f-8d48-b745dfe0857c | -3.0081 | -54.06718 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdddea77-66bc-3dd4-8235-8f85650b81c9 | -2.6533 | -54.30784 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6be33c17-ba0e-33e9-94ca-c985864eafe3 | -3.00564 | -54.24421 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8bd4dd-35e9-33bd-9c74-d901bc9779e9 | -2.97681 | -54.17675 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eeae121-8609-3088-9c30-c3ba48bf2ebe | -3.16892 | -54.74046 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57c225e7-ae15-3e6c-aa3f-1a6ed0c53542 | -8.7407 | -45.15595 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dffaf5a2-484b-3ac2-97bb-c4de98899f78 | -9.58253 | -65.2478 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f07f2419-16ca-3955-b341-29fe1101857a | -2.84167 | -54.07037 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46c971f3-13eb-3f57-ab5c-5baaadbd760e | -6.46894 | -55.47595 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 205627aa-7a27-36d6-a9e7-01d9bdd14427 | -3.19327 | -50.56924 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 879afa6d-5684-3336-a639-97f9bd891d4a | -3.33886 | -52.51149 | 2026-10-08 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db7f45e4-9d57-3aea-83ad-e3c14cf83375 | -6.11379 | -55.69681 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5f6f9ca-4cbd-3891-bdcc-f81636aa8415 | -1.46859 | -54.76357 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8908f7a1-2530-3313-97a9-7a4786c6f3fd | -3.53544 | -59.50393 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3c7752c-8dd8-3e4c-916b-aa890a5d0695 | -11.23945 | -54.96091 | 2026-10-08 05:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c3385e2-89f7-39da-8294-6af55cfaef27 | -8.61193 | -67.02894 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1cb0093-0e38-385d-8cb5-2f6012a15afe | -4.1345 | -54.92409 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a7b23ce-6e86-37dd-a534-7925763a7f5d | -4.29075 | -49.08832 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d9babe0-4647-3635-963b-57f339df3235 | -2.98007 | -58.00003 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55f2849a-9138-348d-bf5a-832f11813276 | -3.84256 | -55.91483 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a161b38b-4755-3916-8dee-f2583aa34b2f | -3.11193 | -53.77277 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6a4b6ca-eb5d-33ce-8a85-9c67ef4e2e84 | -3.30151 | -54.67318 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec25d5df-8ded-3c20-9d7d-7cdb9c6e5403 | -3.7212 | -55.97482 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ffec01-ee4c-331f-b357-be35aa88a116 | -3.05108 | -54.22781 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00fa1ebc-439b-38a1-8954-50e9daab9f85 | -3.01372 | -54.12355 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8b7e32e6-7e62-3776-ad9b-e878ab96543e | -6.1155 | -55.70824 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28eb8b35-99bb-3980-9d70-ddfde8dd15f1 | -2.85348 | -59.26547 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e32a40bd-b373-396e-a7c0-e2c52b68005b | -3.07507 | -54.28522 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6727bffa-178f-3c57-9cc1-5f5de086e7e0 | -1.82569 | -54.93568 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42a26143-dafb-3f5c-807a-92a7165a1173 | -3.65907 | -60.63303 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6192fcc-f9cc-3022-a39d-e2eb9d13f870 | -5.7348 | -45.15137 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f353cdee-59ee-3f29-b3ed-ce144f302518 | -1.32396 | -55.43535 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83d3d9db-91c8-315d-89f9-2078ccd07bff | -6.64075 | -58.50097 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22215222-a75b-3c9b-bf68-fee991d1d540 | -2.93747 | -54.14736 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c716e149-a327-33c1-8380-1414c88f5f57 | -4.12585 | -59.88606 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b5fc502-b3a3-3e09-8d2b-4a4a9d5e239b | -3.54533 | -54.49903 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f041f4fb-a932-33ba-a43d-e719bc53cb29 | -3.47427 | -50.08611 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9ed8541-794b-372e-9545-cbe672848539 | -6.23708 | -52.8547 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 506b6762-fee6-389a-945a-7abbcff6d04a | -3.16457 | -50.43813 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f2248d6-2e8a-3c27-96b6-4a70a4c9f0db | -3.0021 | -54.10589 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0ff5441-e227-3a1d-9d16-db9ff88faa8b | -3.14944 | -51.62337 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47114b97-6320-3090-a032-2b30c8428342 | -2.93509 | -54.04809 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ef58d8d4-008e-3fa6-9a4d-0b3ea6888ec7 | -3.02856 | -54.07434 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 213ecff1-c005-3e58-a2d1-b23491ba7c37 | -8.64828 | -67.17733 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70aefb28-e717-39af-8c56-c29267cc86b5 | -3.05322 | -53.96234 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d6f57b16-51c3-3a1d-8dc2-29df05529ea4 | -4.88352 | -55.84909 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a6fb4c-7267-30c3-a1c2-3cd51c79eb0f | -1.11782 | -54.09371 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ed322da-a486-3ffa-9182-d372b67602bd | -3.5856 | -54.66257 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7315455f-0f97-3d1a-9b98-45b0b90650ea | -2.7786 | -54.06058 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fbf70e9-868f-3d39-96ba-f56a8404e307 | -2.50152 | -58.06676 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aef751ad-f196-3d22-81bd-96bf470d934d | -3.7234 | -57.11134 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de834ff1-fba9-3e16-a3bc-2553643139b2 | -3.69832 | -54.19272 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a4ee3e7-8eb0-3251-93c1-bccfc9a84520 | -3.08603 | -54.30646 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb4a1798-1a69-3f15-98f6-ad1fee166920 | -4.28598 | -55.225 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c2ac29-85d3-32be-9ef4-2dd1f0b60a6e | -3.30041 | -54.0185 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b7d6fc7-f19d-33fa-b58e-0c5f4010ed21 | -6.66168 | -55.08512 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab9426e-56c7-3191-a025-3e9e66227d8b | -3.54055 | -54.6638 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a114af1-a18b-33ef-947c-c3eb1ce3d127 | -3.7768 | -58.5216 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0418b3b1-6f83-38f0-b358-73fb5210c6a2 | -3.56977 | -54.49056 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 50862cee-2e02-3ff7-9e61-b86b1b13568e | -4.064 | -59.83096 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebc58baa-bfb9-3fe6-9227-e97286a74d30 | -2.47741 | -56.09612 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94ed18bf-45eb-310b-9fae-a5eaf5303aae | -3.6443 | -54.51384 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 856932d0-91d5-30ca-827d-b441a69a3f8f | -3.28153 | -54.02367 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 250bf2fe-7d3c-3db1-9497-ee0b4a5852d7 | -3.69304 | -55.49035 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5177c9eb-65af-33c4-ac9d-e50412d63fa4 | -9.5808 | -65.24538 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a81cb97-f6f0-3bab-b3ac-6e333a45ee9d | -3.1053 | -54.27433 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a03e184f-e69c-3d10-b7b6-7440cc9c990c | -6.1654 | -52.6657 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e698c1c-3bd6-3267-bf30-02f08778b3a2 | -3.13799 | -54.36114 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README131.md)
