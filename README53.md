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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5232ba18-89ae-3408-8d93-b00b489a2d9b | -6.1683 | -43.32349 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8d01cef6-e3d7-3e9c-8ae4-29bfb4ea64fb | -3.81155 | -48.95444 | 2025-08-31 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfbad4af-13b3-3989-97e6-e775fce1e9c7 | -4.0706 | -47.95657 | 2025-08-31 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d636df9f-8669-388d-b977-909b6ce4a550 | -6.18334 | -44.20454 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6449648-a954-32f3-83d5-35e9b27e6ddc | -5.55178 | -44.29662 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29e6d4db-069a-3702-89ae-811b9c540e6f | -6.16472 | -44.00337 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f0b6c32-8c60-3d8e-a55b-788a090e0ac0 | -3.62762 | -49.192 | 2025-08-31 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4c598b4-d3cc-333e-9b34-3956f7b02d71 | -4.73678 | -44.44937 | 2025-08-31 04:49:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| bedf14d5-6e48-3dd7-8905-2e389d216acc | -3.48421 | -51.18894 | 2025-08-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73dddbf0-aecf-38e3-ac53-130ab9a72375 | -6.01624 | -42.71524 | 2025-08-31 04:49:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f6fe7c9-8eb1-3461-8d18-a4aff5aff8a7 | -6.64627 | -44.25816 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f369a3a-ee8a-3a8f-9cc1-7cf2952902f2 | -6.70782 | -51.41581 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4fe8ae59-ac01-30ad-8389-3b495c65bb3e | -6.71118 | -51.41634 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0690d606-a3e6-3258-a354-649ecad7a61d | -6.4347 | -45.61003 | 2025-08-31 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6300f97c-b778-391a-8a48-4ae0d2edb535 | -7.36662 | -43.40201 | 2025-08-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbb313a3-cbaf-3262-862b-c493d96d8635 | -6.31303 | -43.52214 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed1ef68-f459-34f2-8542-2befedbfef78 | -7.09633 | -44.31251 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed4cf604-c300-3d9e-b548-329db71afe1e | -5.55136 | -44.29948 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b339ca1-68d8-3905-b034-fe7cdad210b4 | -6.97151 | -40.9455 | 2025-08-31 04:49:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 90a5be11-031d-31be-addd-c22262cba36e | -6.27797 | -43.53919 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d4ccf81-dfb6-3c2f-8b37-b1a09199cdea | -6.83535 | -43.33826 | 2025-08-31 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69dce9ec-379e-39d5-a25d-35baf09b69d6 | -4.30862 | -48.0986 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab34216f-f809-3110-9304-64dabd8c55f3 | -6.17744 | -44.1364 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fde50f6a-e766-313b-8989-1a0d3f19e2f8 | -3.73159 | -53.70396 | 2025-08-31 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d35517-7eeb-39c9-9fe5-3e33b0a74a17 | -6.15735 | -44.13111 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 807c1b2c-9c54-30b0-8c3b-1ae1be54d9f5 | -4.94397 | -47.58391 | 2025-08-31 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90fe72d6-bcda-3934-8872-c69140e5433f | -6.57649 | -43.69826 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d61b5b2-c225-3eee-bc33-ade5b8b6fcaa | -6.17191 | -44.1754 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4de664e-5245-3fa1-9472-8cd5d969feca | -6.8176 | -43.34622 | 2025-08-31 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60cd93c7-3ab7-3ed7-8d4e-4ae457dd8610 | -4.22301 | -47.20996 | 2025-08-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c5eefb7-e893-3406-9482-03ce271f6c47 | -3.51802 | -47.20263 | 2025-08-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a6fb7c8-f6da-3364-9c96-087dbb84080c | -6.57788 | -43.68842 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 885f5043-93ec-315f-807d-97c4404954c0 | -6.21651 | -42.76948 | 2025-08-31 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c636d2d8-2b09-3e71-b914-62bd901940a0 | -6.9498 | -44.31184 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7ffb6f4-6d3f-3316-828f-a2fbc2d43913 | -7.1826 | -43.84065 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a832b37-fc8a-3d34-b31c-c6579f6bda54 | -8.18897 | -42.31978 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db6583db-a37d-3408-ba26-d55e654bdf40 | -6.44263 | -43.96357 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6239439b-0817-3a45-9247-0ebd5cf6d353 | -7.41318 | -42.05467 | 2025-08-31 04:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ccdbcb1c-d6ec-36f7-bc4e-43e4d194ce6d | -4.1672 | -42.03207 | 2025-08-31 04:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 475d01a4-a8fc-3b28-a2ce-36ee98380a28 | -3.59102 | -47.51872 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9ed64899-039f-3321-8cef-210dbd1ccefb | -4.40486 | -40.6953 | 2025-08-31 04:49:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb446e5d-7627-31c6-9b36-c11a25c3de08 | -6.50622 | -43.55433 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06b8c70f-7357-3bad-82fc-de9be859090f | -4.27427 | -48.63695 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e94e2826-713d-390d-b3c4-8e307bb6d0dd | -6.63652 | -44.25361 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d63b00a-6882-3fba-ae2c-66c18b3f87fe | -6.31351 | -43.51879 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d52fccdf-0f97-3ee8-b992-c3c6231bb683 | -3.81427 | -41.55193 | 2025-08-31 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1b20adb-28d3-3f62-b69e-b36b54171b50 | -7.37703 | -43.40722 | 2025-08-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95a1b9b1-8791-3e72-9fe0-524cfc62970c | -6.17791 | -44.20622 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e655c30-728b-325d-9e33-feec85e7f305 | -6.61903 | -43.74031 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9ecf50d-4bcc-3ea7-b32f-f855671a1b2f | -4.22704 | -47.21054 | 2025-08-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a43380e7-4507-39a2-bb10-7aed3a3ffef6 | -5.70086 | -45.95525 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee1c3a03-03cb-3507-b15e-724b1fd9be3a | -6.29359 | -43.54394 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8c91a97-745e-3ec3-81a4-4f1c19be6370 | -6.95397 | -42.01163 | 2025-08-31 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63b24bfb-3e7e-3ac9-99c9-1784b1b2196b | -7.40364 | -49.51704 | 2025-08-31 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2a554fc-a95e-3474-99c0-87f987037684 | -6.17784 | -43.56577 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36b2df46-ec93-3fa9-b3eb-76763fb10faa | -6.28821 | -43.54362 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5927a23-1614-3a4b-8801-bbe525af1ae9 | -7.09458 | -49.92643 | 2025-08-31 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3bd5ac41-301e-38f6-b67f-0c0add9ca907 | -6.50849 | -45.41367 | 2025-08-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd503eca-5652-3646-9c96-d09b41ba60c3 | -7.37206 | -43.40287 | 2025-08-31 04:49:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c298f198-ed59-3fb4-95de-67eba362f3ae | -6.18256 | -43.33955 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d68383a4-6ca4-34a5-a0cc-641518ec3f0c | -6.5837 | -43.68541 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f6cf91ce-3034-3eb5-ad37-78d1a2d95880 | -6.42707 | -43.96138 | 2025-08-31 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900967ba-43b8-34c1-9e67-d7f6c95b517a | -3.59419 | -47.5242 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 361352ec-4300-3412-ac93-095c006bcdba | -7.4116 | -47.45417 | 2025-08-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8bddcf3-606f-3d4e-be0d-b85b9acc5522 | -7.40909 | -47.44227 | 2025-08-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99533508-9261-3f9a-aab5-b8cf2ef68a5a | -6.18314 | -43.56656 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 467f684d-fe6b-351e-93c0-ce8605905980 | -6.77102 | -43.76079 | 2025-08-31 04:49:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f1a73de-bc5b-3026-b33c-9ca3f59691b4 | -5.48027 | -44.40398 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9273cc5c-feff-333f-9771-363350e5cd8b | -6.85871 | -44.44398 | 2025-08-31 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd5ec5b9-6d78-3e97-b6f4-c54fc16f4760 | -6.17869 | -44.2008 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b757e6a-a884-30cf-809a-924883d7f0cc | -6.16719 | -44.13518 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7377121-7479-3e11-92d2-bfb8b49d3f01 | -7.198 | -45.43959 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff7985e0-28b2-36fa-8adb-58c81d98a21e | -7.78117 | -45.46217 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abcf80e4-5fd5-3b71-a5e9-c39cb4a979c8 | -7.58061 | -45.1213 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae1cad28-d608-3f0b-b589-c40fe0b72ec1 | -7.09593 | -44.31541 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46d3901c-d56f-3ede-8a13-d0ea2d313148 | -6.3082 | -43.51789 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ae0406c-fc93-36e3-ae58-d1dc7625a54d | -6.63935 | -44.25481 | 2025-08-31 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3647c4d-304c-39a0-8b03-eec42b693846 | -7.05752 | -44.8826 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e9217fa-e005-3947-8365-1df98c5dd542 | -7.10581 | -44.31936 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 19ae3a7b-f1d2-3ab8-b360-8edb1efaa0ba | -3.28359 | -43.41463 | 2025-08-31 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f785bba-891b-31cd-9731-18eeafd115db | -7.32987 | -44.09373 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 870c8d06-e290-3e5d-8452-55d8fdcf41d6 | -7.21361 | -45.4319 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 829adee5-92d8-347e-b04d-81b57848375e | -6.24498 | -43.38434 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7b6a5c9-e211-33db-8d1b-d488608d186c | -3.21955 | -46.83132 | 2025-08-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b23c9e17-6f59-3139-b136-498f549e820e | -5.49406 | -45.44752 | 2025-08-31 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edca0f1b-83df-38b5-8d27-d2bf651a58a6 | -6.96288 | -44.31577 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 108f9c61-43e4-37a9-a36f-faef9453ac4b | -5.99315 | -43.35979 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7f7ebfe-0268-3ffb-ab70-5913fe8c06c0 | -7.40515 | -44.08737 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff740d51-a31c-323e-bfea-5816b3b20b1d | -6.16783 | -43.32692 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f42eeaa3-d6c9-3c6a-b345-7acc332e7715 | -6.50046 | -43.55659 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 936bcfba-214c-34ef-8251-3f0f59a7a7be | -6.17372 | -43.32413 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2deb8a01-d981-39fd-af1a-6d2bc29aace6 | -6.57833 | -43.68519 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8a68ab2c-41e1-3507-8947-1407960bef96 | -6.94355 | -44.05892 | 2025-08-31 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e76abf4-5599-36a9-a7b7-27e13cb667bc | -7.78596 | -45.46272 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15ab8f1e-b414-32c9-8606-7340e5dbbf4c | -5.69574 | -45.95901 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d51d58db-791a-3f11-a640-c82fc39e8405 | -3.27922 | -52.341 | 2025-08-31 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88e7ffa6-77d0-3061-a25f-a316c20aa150 | -3.87572 | -54.22661 | 2025-08-31 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8c9a465-d34b-351f-85f2-e69410a267d3 | -7.58395 | -45.11766 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d14b4caf-acb0-3978-b7c4-1a52533c6ddc | -6.60974 | -53.12711 | 2025-08-31 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f012081-f543-38cf-af8f-3799c2253df0 | -7.08409 | -44.32577 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
