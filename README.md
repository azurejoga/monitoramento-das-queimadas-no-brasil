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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c38354d3-8ba5-3be7-8b69-0d475b7ffdc0 | -4.4978 | -46.3509 | 2025-10-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 4c341497-f08e-3f28-9136-f8a533385cb5 | -3.4422 | -45.598 | 2025-10-08 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 7a1c5cd0-f8ec-3029-b7b5-326598fa28fa | -5.2601 | -44.1368 | 2025-10-08 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 5874ebd7-be0a-3a38-9bcb-dd62feb066cc | -17.3048 | -42.6182 | 2025-10-08 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cf5f3f95-c7e7-3ece-8eea-c78d39932a94 | -14.6988 | -46.0671 | 2025-10-08 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c63606b5-57a8-3a02-b670-eccecbadb2cf | -4.8371 | -45.7522 | 2025-10-08 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e18fcfeb-a674-376b-9e6c-7a7ec9831dc0 | -5.8469 | -43.3995 | 2025-10-08 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 06099386-7ce6-3a12-b16a-216de7d2c921 | -11.4534 | -50.198 | 2025-10-08 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f847b37a-385d-3a85-a088-13d6285a5866 | -17.284 | -42.6479 | 2025-10-08 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1a7e4c38-f8fd-3fbc-b265-beb4594c4cc4 | -11.3378 | -56.1997 | 2025-10-08 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0efd635d-7da3-336c-b6db-977d437790e3 | -4.4977 | -46.3731 | 2025-10-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 69ca12c8-8877-308b-84b8-76e7654f83e4 | -7.017 | -42.8762 | 2025-10-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 201.8 |
| 84671da1-cbfe-34b7-9ed2-ba2dd2d88fc1 | -5.8655 | -43.4214 | 2025-10-08 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8cee2e97-f74e-3670-b594-316df6240a02 | -5.8657 | -43.3981 | 2025-10-08 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 85dff2bd-85c9-320e-afdc-7de9d3d37679 | -4.6504 | -43.2038 | 2025-10-08 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 194e8b10-6509-398c-95aa-51cc6eb59649 | -4.8557 | -45.7511 | 2025-10-08 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 157.8 |
| d99d1648-5978-30e7-8f62-6e81196a8679 | -5.1227 | -44.9682 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 37781d5f-fdd2-3342-bb45-d16228e3ce8a | -4.6875 | -45.828 | 2025-10-08 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4d698c00-1342-332b-8251-e0bc3b86d0a5 | -6.949 | -63.1048 | 2025-10-08 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7e095309-fc1a-3d8a-9629-ab0da74a3a1f | -17.9817 | -57.5056 | 2025-10-08 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 1bf357ae-d171-3794-b7a0-2643f9afd673 | -7.0167 | -42.8998 | 2025-10-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 3b0c3f5e-a569-33c3-90b5-a6946f39ea6d | -4.6505 | -43.1805 | 2025-10-08 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 3a68df30-83f7-3a1d-9fa3-58fa39393463 | -12.3971 | -63.8811 | 2025-10-08 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1a491255-f028-34ee-8a27-9bc00b98f443 | -17.3041 | -42.643 | 2025-10-08 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 96be1813-fa05-31ee-8d51-611be608cb47 | -3.4608 | -45.5972 | 2025-10-08 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 95084941-12c5-3a27-b911-72b84efc2359 | -3.7937 | -49.4211 | 2025-10-08 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| abd53e23-c81a-3695-a0ab-aef4ca1b94f6 | -4.6692 | -43.1793 | 2025-10-08 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c1b7f986-38e3-3597-b3ab-b6a2cdbcc3a8 | -7.3444 | -43.8735 | 2025-10-08 00:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e185484b-c6b4-3bf7-aee6-2507dc47274e | -12.0314 | -45.1901 | 2025-10-08 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 41591715-fc1e-32c1-bc8a-d61d902aeee7 | -5.8467 | -43.4229 | 2025-10-08 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f33ae404-8194-3663-b229-addc6c15f629 | -14.7184 | -46.0636 | 2025-10-08 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 546e6897-df19-358c-a800-5a03f2e6a89e | -5.1414 | -44.967 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 339.4 |
| fc75407b-ea50-31a8-8a39-85c500825d50 | -5.614 | -44.3188 | 2025-10-08 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 41fbbd8e-a38f-3f11-bd94-41878de29f12 | -4.8556 | -45.7735 | 2025-10-08 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| c35b418d-9c9c-36fe-90b3-e351e74ea1e0 | -5.1416 | -44.9443 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 7585efe9-3dcc-3117-a281-6f71d400ad5c | -6.9982 | -42.878 | 2025-10-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 07486fca-9506-3888-9bd3-970f474fdbe1 | -5.1229 | -44.9455 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1242d984-9c65-3a98-8c7f-9f07e3f9da72 | -4.6691 | -43.2026 | 2025-10-08 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b57d7a6f-8062-37ea-953d-f8418db569e8 | -11.4531 | -50.2195 | 2025-10-08 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 9fdb55a5-846e-34cf-8581-f691e2f5cf5a | -3.2321 | -46.7836 | 2025-10-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a4cacb27-7843-3315-9bdc-7ece3026af17 | -12.0122 | -45.1929 | 2025-10-08 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 03812ad3-0e20-3d64-a22f-7564688581bd | -3.7936 | -49.4424 | 2025-10-08 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d41f0b76-f330-3d2c-8030-86caf8ce7661 | -12.0118 | -45.2161 | 2025-10-08 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| eed35dfc-5c4a-3c0f-950b-0dce0de6dd14 | -7.5874 | -64.5097 | 2025-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5b145b60-7a01-3bfd-a89e-c459ce52abf0 | -12.031 | -45.2132 | 2025-10-08 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 4954c007-bbb8-33d1-821a-3fd2f353bf56 | -19.8584 | -46.1569 | 2025-10-08 00:00:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| d10555d4-6c86-33f4-8776-6775365689f4 | -5.1412 | -44.9897 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3ab6cb05-b2a6-3f08-a9a6-039d23ca969a | -3.4423 | -45.5756 | 2025-10-08 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b0275646-b037-3689-88f7-97918a6c5c77 | -5.1601 | -44.9658 | 2025-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5a21db9a-da2d-30be-9278-f3e811dd8612 | -7.0167 | -42.8998 | 2025-10-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 0eb9ee0b-a9e5-3d57-a549-cb59d3bd209d | -6.9982 | -42.878 | 2025-10-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 1c9f88b6-9451-3334-852f-98e1b27ab023 | -7.7922 | -44.2229 | 2025-10-08 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 98fc544b-399b-3984-957d-01301c1f5c98 | -5.8655 | -43.4214 | 2025-10-08 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3bd6c529-2150-340d-af1d-127d62c7c956 | -13.8911 | -51.9094 | 2025-10-08 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 04fb5404-03dd-399f-9daf-f1304a2a3e23 | -10.3919 | -50.2702 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 107f7844-8459-3d4e-8210-33120d62e267 | -3.7937 | -49.4211 | 2025-10-08 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 07f5e7f2-cd3f-3323-b820-2e7914c6920a | -10.3727 | -50.2936 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b5ad460d-4e68-3e0b-aa03-bd753f3c9728 | -17.3048 | -42.6182 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e7011f48-a03c-3354-b506-862cd5fed796 | -10.4859 | -50.3032 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 013978fd-0f4a-3f51-a11e-7c4846806c64 | -17.3041 | -42.643 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 320.8 |
| bad95840-750e-38dc-953f-38feeb0bef48 | -4.4977 | -46.3731 | 2025-10-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c359fb5c-b992-3d51-8298-3dba310e072c | -17.2847 | -42.623 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 146acc3c-917d-3d5c-8509-9b1421bcecb2 | -7.017 | -42.8762 | 2025-10-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.3 |
| 047a1e0d-b526-34d4-be5f-986d0d60fb5e | -5.8467 | -43.4229 | 2025-10-08 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 2893e3c3-89f4-3efc-a2d8-5ef9ba7a17fe | -5.2601 | -44.1368 | 2025-10-08 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| dae6a049-e0fd-3ff7-8551-423bd2dbb889 | -6.4288 | -47.2452 | 2025-10-08 00:10:00 | GOES-19 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| efb70da7-0d35-3e77-8475-9e8584835e9e | -7.7924 | -44.1998 | 2025-10-08 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b20b1e98-47a0-3b78-a24b-c4557d9c2ec0 | -4.522 | -42.8608 | 2025-10-08 00:10:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| d0265f19-6412-314b-b12a-29dbb9b5a35e | -4.6691 | -43.2026 | 2025-10-08 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8b6335a6-84b9-36a3-97da-b21276e8939f | -10.3732 | -50.2508 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 29a18c8e-8d85-3b69-b797-95c358ab1c7a | -6.949 | -63.1048 | 2025-10-08 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 13da8983-3978-3720-8d25-86eae51f3c35 | -3.7936 | -49.4424 | 2025-10-08 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 4cc3c231-f9a9-3f1a-9bd8-ac91af286c80 | -3.8926 | -44.9014 | 2025-10-08 00:10:00 | GOES-19 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2d4681ec-0bb6-32cd-8899-207cf20ea7c3 | -5.8657 | -43.3981 | 2025-10-08 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 22020682-4b46-3b79-b06e-44eeca408dbe | -11.4531 | -50.2195 | 2025-10-08 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 58e67f59-46b7-378d-92ab-ae7f39ff9288 | -14.7184 | -46.0636 | 2025-10-08 00:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 77459cbf-cdda-3534-901e-a803b51592a8 | -3.4423 | -45.5756 | 2025-10-08 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1ba5461f-70ef-3687-ad8f-6ab1df21d6ba | -17.2853 | -57.9976 | 2025-10-08 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 44dd0d56-b506-3f6c-a5e7-55006284eb2a | -5.1229 | -44.9455 | 2025-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 2949ac03-bfc7-3ad3-8bbc-e838d97068a3 | -5.1601 | -44.9658 | 2025-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 08e7bcc2-4589-3f10-b1dd-777e0460be25 | -19.8584 | -46.1569 | 2025-10-08 00:10:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4f3b2634-91b8-35f7-97c3-881e61a0778d | -7.5874 | -64.5097 | 2025-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| eadb24ed-c350-3c68-b90a-8aa91281e14b | -10.354 | -50.2741 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cf1a4487-6aeb-32be-8161-40c54380396a | -4.6505 | -43.1805 | 2025-10-08 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 361d2d88-92dd-3b3f-a6c1-1c21c54eecea | -10.3729 | -50.2722 | 2025-10-08 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| bd0d3f9c-1651-3441-b18b-56ea54ad9f3f | -5.8469 | -43.3995 | 2025-10-08 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| dcefbec6-8ec9-31a3-83fe-8395bc67b222 | -4.8556 | -45.7735 | 2025-10-08 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6f72cc3e-8dc3-3658-825b-0b2371eb7634 | -12.2969 | -55.1026 | 2025-10-08 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ac73afb3-5c9b-36fd-8104-2bf7673730bd | -5.1227 | -44.9682 | 2025-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 28057573-6b6d-3328-b10d-3e2ef5b283ba | -12.031 | -45.2132 | 2025-10-08 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 94e182f9-dd8a-3622-8942-400f959d2c4e | -12.0314 | -45.1901 | 2025-10-08 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c8a7b98b-564d-3ae5-bfac-665003f3e209 | -12.0036 | -46.7667 | 2025-10-08 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e1c48496-de6b-3eaf-a729-51d8fafd4401 | -13.8117 | -45.7826 | 2025-10-08 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d8f4390e-5c18-3d98-bcba-be762b8e88a0 | -5.614 | -44.3188 | 2025-10-08 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a6ac4273-04a9-3f54-bc51-b5d98f2816c3 | -13.8112 | -45.8057 | 2025-10-08 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4e178a52-bdc2-3592-8a6a-e08bf7cb865a | -4.6504 | -43.2038 | 2025-10-08 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 0e96e5e0-b40f-34de-b29e-71411bd232ce | -3.2321 | -46.7836 | 2025-10-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 83192e27-bf10-3326-b938-f07a757742d5 | -12.0118 | -45.2161 | 2025-10-08 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9743d9aa-dd0f-3dfa-a26a-9d641c6fa843 | -12.3159 | -55.1008 | 2025-10-08 00:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 793a85d4-0f11-362c-81ba-b2d23020594b | -17.2833 | -42.6727 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README2.md)
