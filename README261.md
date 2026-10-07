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

## Dados Diários - Página 261

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ebc5454-3f13-37b8-aedb-20caa6284ea9 | -6.1482 | -51.9477 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 11418568-ae5d-3faa-9c63-65f86078e2a6 | -5.7189 | -45.1547 | 2026-10-07 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| f4c773f7-82d3-371c-be99-2ce3f4ba4d13 | -6.3541 | -43.3349 | 2026-10-07 19:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 38f10255-1810-3aaf-a679-8cf73cc6042b | -2.6859 | -49.0539 | 2026-10-07 19:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 34e34b18-5036-38e8-a389-e22e172eb3a0 | -3.6931 | -40.8572 | 2026-10-07 19:30:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 14f4a71e-0cad-3ee9-9e26-15951edadbab | -6.3353 | -43.3365 | 2026-10-07 19:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 01dd7327-0207-3a62-b931-a1c9a8396abb | -8.6511 | -44.8919 | 2026-10-07 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d415f6af-a923-35ca-95c5-83f4a85dfdbf | -11.7187 | -43.4148 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5bb18fb1-e91d-30ee-b587-4f312713359a | -6.5988 | -41.5341 | 2026-10-07 19:30:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 6e6e7a37-fddf-35ef-82fd-a76471495a08 | -3.3637 | -50.4701 | 2026-10-07 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 240.4 |
| 1cdbd384-3b17-3ffe-aca8-1a1a79a0fbe8 | -5.0325 | -49.7687 | 2026-10-07 19:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| eca3093a-b34b-3c99-ae07-e695d0414fc6 | -3.8627 | -50.4106 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 627fd0f5-9984-380a-b185-3f45d03fa25b | -7.5762 | -40.359 | 2026-10-07 19:30:00 | GOES-19 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 178.8 |
| 53b4662e-9113-3856-b0b0-dba1ed5ea7c6 | -6.5985 | -41.5582 | 2026-10-07 19:30:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 403f8e80-e9ac-3c79-a375-b4bab4fc3d53 | -11.6181 | -43.6669 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0ae64e5f-d503-3d43-ad45-17e367600d1a | -6.6599 | -52.9675 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8bb969be-f0d8-3800-8376-a0725937fceb | -5.9412 | -45.3874 | 2026-10-07 19:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9446272b-dcac-3e2d-86f9-c0d36ea483b0 | -5.977 | -43.529 | 2026-10-07 19:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bf448d1a-0a77-3e33-bb34-0ab0e17752e5 | -0.5993 | -49.4293 | 2026-10-07 19:30:00 | GOES-19 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| fd316b6c-6100-3ae6-897c-fcc1a3b5d016 | -6.5852 | -53.0331 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| fb8ee0de-320d-35a4-a2f7-413c368654f6 | -11.2333 | -44.8678 | 2026-10-07 19:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| ffdebfbb-5c13-3cb6-9796-5febb2a74f3d | -3.5127 | -54.6362 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3754f350-774f-34e2-947e-7c6b65224f6f | -3.295 | -53.8597 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 30e5458f-cbdd-3e04-972f-c70b4957e2e2 | -5.7378 | -45.1307 | 2026-10-07 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| f95c1c95-cc3e-3e9b-bb6e-49ae0b217a9a | -2.7043 | -49.0533 | 2026-10-07 19:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| deb2f5ec-16a5-3197-9ac7-b046c1677c33 | -5.7376 | -45.1533 | 2026-10-07 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 926.2 |
| 9caa5ecf-7eb4-31bd-be1e-e6e90725da79 | -3.7166 | -54.2096 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| c9511bfa-0a2d-3301-b611-ccb29e8079d1 | -2.8899 | -54.0711 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7bf4ea1c-b745-31d8-ae0f-8b19afe4c5be | -3.4947 | -50.0877 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cbb0820f-5711-392a-ac4c-f34503f834ec | -8.5365 | -67.0876 | 2026-10-07 19:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| c4526370-9155-30a3-8e4d-02e17263bbf5 | -5.372 | -44.1751 | 2026-10-07 19:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b365f121-b2c9-35f0-b529-73686368e438 | -3.195 | -42.9772 | 2026-10-07 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| a5090b9d-622c-3e1d-9774-b007bc8c11b4 | -3.1951 | -42.9538 | 2026-10-07 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 43ff0d90-6be0-3f39-9138-0884ceac620a | -5.7489 | -53.4641 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f57bc4a0-19b4-36e6-a7dd-b8e56f119a2c | -11.7143 | -43.652 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| dd46936c-e2e0-300b-aeb9-1957147f9d01 | -9.507 | -70.4439 | 2026-10-07 19:30:00 | GOES-19 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c4fe14bf-fe1b-3414-b73f-247d3506662c | -6.3163 | -43.3614 | 2026-10-07 19:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| ba412f5e-6a33-37ea-ad34-daddecc26e21 | -9.0406 | -65.9401 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 1a04fa07-478f-372e-9961-15eca99fb759 | -5.6748 | -53.4879 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| f50aa068-475e-39cd-aed4-57f40e5cf34a | -3.891 | -52.2147 | 2026-10-07 19:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ca58bfdc-0774-398e-896d-66436edf1cb3 | -5.8773 | -53.6202 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| df665a6f-ade9-381d-964d-96fdaa17ca1a | -3.203 | -53.8823 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 97065f80-f4a5-3df0-8b1c-04bb2813e1f9 | -5.7191 | -45.132 | 2026-10-07 19:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 48da3820-cf9a-3f47-b39b-65c9b3182dfa | -3.4245 | -49.2648 | 2026-10-07 19:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 44096ee8-9136-3be9-b5a5-3cb3de373781 | -9.9596 | -43.5045 | 2026-10-07 19:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 63591592-6454-3066-a9ab-2d6e2e1b3fc3 | -6.1937 | -42.4785 | 2026-10-07 19:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 9a76e5e9-d725-334f-9155-f2344ee41c47 | -3.4944 | -54.6167 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 202ec51a-5688-3103-91b0-4d69b3bd6a0d | -3.476 | -54.6372 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 70aafe57-7dc0-3829-b1e2-442245597c9a | -3.73 | -55.486 | 2026-10-07 19:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a47279be-8a34-3fd5-9088-d24621009e99 | -9.475 | -64.3525 | 2026-10-07 19:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 320.4 |
| 1937b8df-afab-3f8c-8b0b-3aec545604a7 | -3.8037 | -47.4839 | 2026-10-07 19:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 25cf154e-a8ee-353e-9fb0-d8dc0de6064e | -6.5853 | -53.0127 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 350583bb-e57e-386c-bf66-5e5741d65ee2 | -4.2558 | -46.3855 | 2026-10-07 19:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 348e5762-a4a5-312a-a4ca-07ca87708c03 | -3.2214 | -53.8818 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8f32be00-94c5-353a-86f2-e082d5fe0ec4 | -3.4762 | -50.0883 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 215.5 |
| c09d0ca4-78d2-301d-b725-e6481f7b8be7 | -9.1174 | -65.359 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| eb3cfe4e-e267-3274-821a-08bc13a14de5 | -8.5367 | -67.032 | 2026-10-07 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 9ecb70f9-910d-3f64-8796-40ce1543731a | -5.8204 | -53.8457 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| d3634d84-cadf-30fd-96bf-a7e91581a9b4 | -3.2136 | -42.9764 | 2026-10-07 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5f7aa404-2225-398b-9857-bf32469f908f | -3.6049 | -54.5736 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 66235a13-6530-3dc2-9114-e820a6f222d0 | -8.2181 | -46.362 | 2026-10-07 19:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1607929e-13df-3828-8c1c-4a03544d5895 | -3.5311 | -54.6357 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 664e13e8-2b77-3e8b-9740-282f89f2af4d | -6.8952 | -43.6833 | 2026-10-07 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 608cc80f-571a-34d3-9448-dcd0373a12af | -6.1244 | -47.9227 | 2026-10-07 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 79285147-5c3f-3fc2-a694-06c59afe212f | -7.1825 | -52.6283 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 266c32bb-056b-3ec8-95e0-003e2d2099d8 | -3.476 | -54.6172 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 18547c64-197c-3d86-ae84-2bb595405313 | -2.9271 | -53.9295 | 2026-10-07 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 7c48a254-fd39-3cc6-bda1-a925aee17624 | -5.6931 | -53.5073 | 2026-10-07 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c19ebfe8-ed30-3075-b264-de6aa31e9368 | -3.2137 | -42.953 | 2026-10-07 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7de5e3da-bd06-3fea-9a7f-9cb385fb11d3 | -6.6037 | -53.0321 | 2026-10-07 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| a961c6ec-30d1-3577-98c9-992e9ce266f0 | -3.5127 | -54.6562 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b4a24faa-52ba-3c68-9c00-df6f41db25ca | -3.5876 | -54.2937 | 2026-10-07 19:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 7dd3adbc-7a66-3613-9cca-76f07bf89125 | -3.269 | -51.0575 | 2026-10-07 19:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 339fca9d-dedb-3e67-bd62-34362e58b372 | -11.8503 | -43.5598 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 23e488ad-1f66-38e3-8899-2e6bb34b11cd | -3.6932 | -55.4871 | 2026-10-07 19:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2f31bf08-94ca-3bcb-a8f2-dccc84a9dc1a | -11.6177 | -43.6906 | 2026-10-07 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f4456f08-6ca4-3a40-bbc9-becd0d19b707 | -8.5551 | -67.0686 | 2026-10-07 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 48d215e5-62c1-34ec-882e-8835affe8de7 | -3.7818 | -41.6479 | 2026-10-07 19:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 7e685a4e-d752-3c70-b43a-6fbea51ea96e | -5.8205 | -53.8255 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 52727952-73ff-35b5-8012-e78af78c2ff5 | -5.9647 | -40.9383 | 2026-10-07 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 171.3 |
| 83bde8ba-bd3e-3dcb-bcc0-15260a7a02a3 | -11.8503 | -43.5598 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 094d204f-b6ce-3c5b-b676-b59ee90a1340 | -6.9331 | -43.6566 | 2026-10-07 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4840b51b-58d4-3d07-8d8c-ceddaaf6c498 | -6.9328 | -43.6799 | 2026-10-07 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ba5c3fd1-d981-3850-88ad-2100d8bf0eab | -6.9937 | -40.0277 | 2026-10-07 19:40:00 | GOES-19 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 89.9 |
| ae25be16-4467-38cf-a8fb-bf74b36a488e | -12.0457 | -43.3864 | 2026-10-07 19:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| f016f1ea-bc35-389d-a05b-f4e6e5b568f5 | -3.328 | -50.1775 | 2026-10-07 19:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 228.3 |
| 44534e64-27ca-37da-8a61-7e4af037dc01 | -9.0591 | -65.9396 | 2026-10-07 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 155.1 |
| ee737030-84e0-3edf-8753-abe2fd6a9dab | -5.749 | -53.4437 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 905a4faf-cd75-3726-88d2-c19a9ea51b89 | -3.3452 | -50.4707 | 2026-10-07 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 282.5 |
| aebb3e36-c864-355e-81a6-92c63a5197c3 | -3.4245 | -49.2648 | 2026-10-07 19:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| f5a672e7-a899-39a6-b144-f14e2f392928 | -5.4771 | -42.8427 | 2026-10-07 19:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 591a37d5-6066-3208-a32a-180eb89f7f62 | -3.2136 | -42.9764 | 2026-10-07 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 678a6f64-1669-35a4-ab9c-fdcf37c16c4d | 1.6937 | -55.6461 | 2026-10-07 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 153fdf8a-a3c7-3717-a49a-1f381f1560ca | -5.8204 | -53.8457 | 2026-10-07 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6cf2d667-a832-3da6-ad74-f4bd6f7ab12a | -3.5181 | -41.948 | 2026-10-07 19:40:00 | GOES-19 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 12f45192-e55d-37dd-b86c-eaa0e17bce67 | -11.6369 | -43.6876 | 2026-10-07 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f35878f2-cdfa-3f49-b104-3dc304501d3c | -9.475 | -64.3525 | 2026-10-07 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 543.5 |
| 27594fe7-9af9-33cd-b7dd-11ce5857fa5d | -5.051 | -49.7677 | 2026-10-07 19:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 7bcc532e-fd4b-3a07-b75b-bf149e3f1353 | -1.091 | -54.1603 | 2026-10-07 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 638bd6d5-fe61-3c9d-9ae4-d8f434254207 | -6.3351 | -43.3598 | 2026-10-07 19:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |


[Clique aqui para ver as próximas entradas](README262.md)
