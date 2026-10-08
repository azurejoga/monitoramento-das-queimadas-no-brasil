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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a33673-9c58-364c-89c5-2ffb73252434 | -3.1298 | -53.7834 | 2026-10-08 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9c46d766-92c3-3564-84b1-31af15555901 | -3.2499 | -46.9589 | 2026-10-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 66b81ce7-07fb-3556-ae81-fe409a531dc1 | -6.2342 | -52.8685 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 01f779fe-573e-3b43-89ff-028935106fc7 | -6.1689 | -39.4391 | 2026-10-08 00:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 4f475c9b-f417-387a-a214-d6f4ed3828f6 | -6.6505 | -43.7284 | 2026-10-08 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 22420e87-2922-3e8c-a86c-eb32458042e0 | -3.1879 | -58.6433 | 2026-10-08 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d716c8af-1333-3dbc-a4ec-59a48b629ded | -10.025 | -36.378 | 2026-10-08 00:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 76.0 |
| f1d9b0da-d5df-32e0-af07-023ec787ba74 | -6.15 | -39.4409 | 2026-10-08 00:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 5eaf40e4-e742-30ae-a594-2d264b6d07c1 | -3.1973 | -50.5382 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 45520645-68a0-3b8e-ba2d-0f64e68055ef | -5.9586 | -55.3648 | 2026-10-08 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b5ec6c83-d7e6-37c0-9805-dcd0b2e16af1 | -2.798 | -54.0933 | 2026-10-08 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 53038403-94d7-3ff0-b9de-c01e939fbe64 | -8.742 | -45.1563 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 9c4e7d45-4e7b-3343-829e-04a6bd1f15d4 | -6.8952 | -43.6833 | 2026-10-08 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4c8a4b0d-aa0e-30cb-80ff-ff805c66e83e | -8.7231 | -45.1583 | 2026-10-08 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f33306fa-61af-3695-9238-aeaa7ed27af7 | -7.2364 | -55.1807 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| afba02c4-e047-3e53-9167-3062e85a7797 | -2.5537 | -56.1649 | 2026-10-08 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a38908f1-f1eb-3789-be28-8ab536c7739a | -3.478 | -59.5779 | 2026-10-08 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fca1c7d3-f665-3ca0-a397-7b01e62f0404 | -3.1972 | -50.5592 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 654b6b4a-1432-3a6d-b450-3a1f3e7c3ba8 | -2.8712 | -54.192 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 19a08303-1dec-3a1d-b3b5-27dd87610ac4 | -3.1792 | -50.4551 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| eb3c69b9-fb39-355e-b623-ddeda0d5f323 | -3.7818 | -41.6479 | 2026-10-08 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 2eb1c315-03fc-3f61-b34c-ef31593f7b1f | -2.5903 | -56.1642 | 2026-10-08 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5ac6aece-388f-3fc7-9a47-ae3d96719755 | -4.3471 | -43.8021 | 2026-10-08 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 59008901-1791-383a-bc36-8ace4d93e639 | -1.4756 | -54.5565 | 2026-10-08 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 85465cbb-47cc-3d50-b202-cf3dd1f78e4d | -6.8764 | -43.685 | 2026-10-08 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a8e747df-ddcd-3716-b2e8-f53d4d26d5c8 | -6.2158 | -52.849 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d2eccd3c-4318-3d1c-8421-ac7ed18b75aa | -2.8895 | -54.1915 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 06f4c14d-2870-3018-b928-407af9422c3e | -7.2366 | -55.1606 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| b143724f-7607-3e6a-a137-19110b5a0771 | -3.2157 | -50.5586 | 2026-10-08 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 17ae3553-6ce3-3315-9f05-8ae2adfb5ec2 | -3.0914 | -54.2669 | 2026-10-08 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9d063b03-6aee-3e9c-8daa-6d1c0f11def0 | -2.7796 | -54.0937 | 2026-10-08 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2110621f-eaf4-349d-a4ca-b9f4e16dcffd | -4.2768 | -49.0816 | 2026-10-08 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 307add53-6ead-3d51-b7e0-6493804f0e9b | -8.5369 | -66.9949 | 2026-10-08 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0c15be3b-0a6c-30c9-a921-2977dcc756fd | -6.1502 | -39.4158 | 2026-10-08 00:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 473094cd-a0bc-3c2b-89b1-76185b07a6ac | -4.2954 | -49.0807 | 2026-10-08 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 148a6aee-917a-3163-af8c-509bbfac4205 | -3.1101 | -54.1661 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 182.8 |
| 571cd034-0427-3925-8397-aaf83e232ff2 | -2.9447 | -54.1702 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0573d870-6e72-376a-a2b9-f1ef937a53d7 | -8.3882 | -46.3006 | 2026-10-08 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 95c2a46b-1a5c-399a-bfc7-9f6ea7259576 | -6.6319 | -43.7068 | 2026-10-08 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| daa94cbe-971a-3f5c-98b4-48d36e7f75b6 | -7.0065 | -59.1223 | 2026-10-08 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 2cd76618-5fc0-3aad-928d-f6f61e124d3d | -10.4337 | -47.2824 | 2026-10-08 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| bce85467-ed15-32a6-9b54-a6609a5156a4 | -7.1964 | -45.354 | 2026-10-08 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d61bb8d1-ee55-34d1-b30f-78653eead489 | -2.7797 | -54.0736 | 2026-10-08 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 4d5d4b83-05fd-3f83-a1f3-91a26dc578ba | -2.1629 | -59.217 | 2026-10-08 00:20:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| a89f4bf6-8f71-3aa0-96d1-75ed5ed91816 | -7.2152 | -45.3523 | 2026-10-08 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a0030cce-91ec-3f9d-86f5-22b2d21182c2 | -3.6049 | -54.5736 | 2026-10-08 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 291fe319-5c7c-3de4-9b73-37197527ae0d | -3.8566 | -55.9967 | 2026-10-08 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 286710bb-cea4-344b-ab9b-7c307707739f | -9.8261 | -44.7781 | 2026-10-08 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 85eb30c9-44f0-38c5-b888-a4f9b739d608 | -2.9448 | -54.1501 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 52a8396c-5efe-3123-8492-f676473bf9b8 | -6.2527 | -52.8675 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 3db210c9-47d2-3d15-9c79-86dfa7a018f9 | -5.7116 | -53.5065 | 2026-10-08 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| de0e86b7-9fc1-3ec8-9cf7-d29f362f9b72 | -3.8749 | -55.9961 | 2026-10-08 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 93fb53cc-cc4a-3834-ae19-3b270eadc9b2 | -2.5903 | -56.1839 | 2026-10-08 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 54880855-a46b-336e-91a2-6a9b1c25600a | -9.0407 | -65.9215 | 2026-10-08 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8acc5e28-2363-31f5-af93-fce407068258 | -8.537 | -66.9764 | 2026-10-08 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a642300e-8b6b-311b-9115-2e239a092144 | -3.1697 | -58.6437 | 2026-10-08 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e657e930-02db-3eaf-b608-367731383253 | -6.895 | -43.7066 | 2026-10-08 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f273d4e6-3a25-3204-8327-687fe066d349 | -6.2529 | -52.847 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 89c0af8f-26ca-3af9-b0b7-34a2bcf5879d | -3.2554 | -54.6631 | 2026-10-08 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 070339e0-604e-3a69-96d2-12cdadf4900a | -3.11 | -54.1862 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 06f07fab-2883-30c3-b16c-b4215daeccd4 | -9.0592 | -65.9209 | 2026-10-08 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| da5ca86b-106c-3fbc-ad91-3a64473fb95d | -2.8711 | -54.212 | 2026-10-08 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f3582abf-9980-323e-a130-e253cd0de180 | -1.4756 | -54.5365 | 2026-10-08 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| bfbe4875-53b1-39b5-a21c-292f92c24a84 | -6.988 | -59.123 | 2026-10-08 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cba733ed-36de-3e20-b6bc-0549895df24e | -2.572 | -56.1842 | 2026-10-08 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| c5da8cb6-ad20-3bff-ae01-ec80d3b0f7ff | -1.5301 | -54.835 | 2026-10-08 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2e82e756-c20e-35e3-bfa9-9e95eeb2f4d4 | -3.1114 | -53.8041 | 2026-10-08 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ac1c7b2b-e887-3aea-be4e-9bc5882ff544 | -9.4936 | -64.3518 | 2026-10-08 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| a4d43bd9-6ae6-377f-8237-84523fbff9c4 | -3.1115 | -53.7637 | 2026-10-08 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 609f8982-58dc-30b0-9505-8d88efc867eb | -6.2157 | -52.8695 | 2026-10-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c7d196c2-fa5b-35c3-aacd-6124e9a6e0c7 | -9.0591 | -65.9396 | 2026-10-08 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e0c7f316-18ac-32f3-91a4-35bec501a327 | -11.8062 | -47.339699 | 2026-10-08 00:26:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d946de37-25ce-352b-8472-23d167bba04e | -3.6533 | -54.277599 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d83f01-1e5d-3786-973d-b94fd94c2abf | -13.7082 | -49.097198 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7a040b-1ca8-35b2-b86e-e6326052b585 | -9.5173 | -54.746399 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447834b0-6269-3e82-8fdc-ce81d022d442 | -3.2054 | -50.562599 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d2557bd-cbe5-3efc-aaa7-2b943cd52003 | -3.3115 | -54.043499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80deac1d-23c4-3ee9-bd27-b3c9f223e8dd | -2.3705 | -56.128899 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1625ab88-93f8-316e-8e70-f42e11c961b6 | -2.7211 | -57.4604 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3385893d-cfec-3789-ae17-df41e17b4f08 | -3.092 | -53.712502 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc475c94-0d3b-39d6-bc78-a9409105c585 | -3.2231 | -53.881199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57702084-aed3-3e13-bb29-951016264cfc | -3.0968 | -53.733501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2368bc57-33c6-31f6-a16a-acbfe9f09768 | -3.0449 | -53.913799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 024cd25e-dc71-3dea-b1a4-616bccc1676b | -3.0417 | -53.899899 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f5389d6-ae55-3928-a97a-6dc26fc8c355 | -1.364 | -56.921398 | 2026-10-08 00:26:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54fa5aa1-8bc5-3fc4-9a00-eaa4a237bcf6 | -6.2218 | -52.829498 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a08a0cd-33ed-3b6b-b351-4771a133a4a1 | -2.6484 | -56.540199 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9c3f5d-1fde-3850-9904-eab11a30c883 | -3.1814 | -50.547901 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1888df6-a5e8-3d0e-9f92-f65deb6ab35f | -1.7772 | -55.053398 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d482a7ff-28c6-3730-9831-b551ed7adf31 | -6.2087 | -52.8624 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 852847ad-9ab9-3e4f-827c-7d3712e85a6e | -16.892799 | -40.883099 | 2026-10-08 00:26:00 | METOP-B | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14700621-79f4-3c40-8205-a4d1ba1c2a73 | -3.0305 | -54.077202 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 258b021f-dcbd-3620-b61a-b4dbcbb2e168 | -3.5947 | -54.656502 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c675782-7887-3c0c-8a37-5d465bcf3165 | -6.1498 | -52.875702 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ff3298-499d-3fe6-8f6f-98cd49b023c2 | -14.9227 | -48.075699 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03876381-3837-31db-81e8-a7a27fc176b2 | -3.4821 | -59.445702 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8db7cbe1-549b-39de-87e6-391639209524 | -3.156 | -54.0854 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 210ae2ff-10c3-3a01-94a4-a929f34970fc | -7.2182 | -55.100601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e270abc-61e0-3747-aa0d-c34d9532f32e | -6.1395 | -47.927601 | 2026-10-08 00:26:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e73d827d-5bc0-3415-b629-5170664d62e9 | -2.3939 | -57.8839 | 2026-10-08 00:26:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
