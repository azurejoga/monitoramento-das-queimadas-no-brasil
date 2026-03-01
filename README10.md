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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61d44df7-bd36-3b04-9d71-16fb461041d0 | 3.32089 | -59.88995 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3002a68d-2a90-37f4-a828-9d5ab8d01085 | 3.16276 | -59.91842 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7937899-eb5a-32f5-a98a-109c2b7d8a00 | 4.09164 | -59.87923 | 2026-03-01 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 300c86ab-cf75-3177-ae4b-30496c4dd177 | 1.49762 | -59.9123 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 10714a5b-bfce-3de0-b246-3240a8b34708 | 1.50133 | -59.93541 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fc81d63-5f0a-317f-9f31-56d0ff6985fe | 1.20728 | -60.62203 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a23bb477-4b0e-3361-b748-30e8892f69b7 | 3.44934 | -60.80349 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c72743f0-56af-380f-98db-6c2f8b991fea | 3.15978 | -59.92787 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f71b64a-f5cc-32d3-842a-b46e6dae67bc | 3.16056 | -59.90535 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81e301c9-bb18-3d96-8b12-8ac27d0c43f0 | 1.2782 | -60.41463 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e3230c4-8562-399e-b4d0-7351f6049fd8 | 0.57834 | -59.90666 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09c67e6d-4116-3aa4-a0af-2802abfd5e04 | 4.436 | -60.73951 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6f0a11-2f8a-326b-877e-d3c2424617c9 | 2.18659 | -61.91911 | 2026-03-01 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a213d72b-345a-3683-ab54-de75c7cc8dfe | 3.05351 | -60.68013 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29cc3a5b-cfb5-3fce-a968-ed32642eb4d6 | 1.06022 | -59.25608 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ed1d92b-0324-3575-b5aa-e4988b77cddd | 3.39318 | -60.2216 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb886f5-3343-3300-b40e-2e7cc95132bc | 1.50661 | -59.93913 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40aa1fb3-b36d-3e99-b776-877928ce9ab8 | 4.41824 | -60.7598 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e3f4158c-1efe-382e-8f2f-efd0d2f057f9 | 3.4458 | -60.80796 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39d30d1e-0027-32e7-8907-d1e97f52c2e4 | 1.50366 | -59.92076 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6dabd6e6-f0af-33ce-bd5a-2088f0d98879 | 1.49452 | -59.92215 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79b5cb1c-3467-36b0-a4db-adbff2f96c20 | 3.45058 | -60.81099 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b12b831b-4fe5-39d9-9217-6bb403d804b2 | 2.82268 | -60.77522 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d40b92fc-dba7-3615-91d6-6906f9055221 | 0.5756 | -59.90523 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f884be56-dc11-38fa-b971-9093c76ec996 | 1.17374 | -60.36007 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 387fbcb0-1e92-3137-bc03-31f1c1e64505 | 3.4512 | -60.81474 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bc5d349-dccf-38f5-8fad-3caf55ad1a79 | 1.48693 | -59.93311 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df1de08b-01b3-36ad-82b1-36ba50eb0b39 | 4.29392 | -60.06713 | 2026-03-01 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a9b5baf-9d12-358e-824a-3cfb97986263 | 4.1516 | -60.71158 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f2756ec-1549-3a45-b072-1d2ea589ce42 | 1.47778 | -59.93446 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bf0e03f-6887-3573-b221-704e3d1b5e9c | 1.48846 | -59.91361 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 6aa3c769-25fa-3e85-b0a7-98d0936152ca | 3.44642 | -60.81171 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d464be11-2bfd-3d5a-9a66-1528b12dd72c | 1.86427 | -60.40644 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9412f004-30ed-312c-9021-a3e05ad54e14 | 3.44164 | -60.80865 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21cad683-52e0-32ff-a52e-1d0c58013738 | 0.94954 | -59.45189 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdf37b1-8dcf-37ba-aca7-29e4295ed175 | 3.99667 | -60.11844 | 2026-03-01 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d5fcc61-b322-3dea-b67e-76a456ad57b3 | 0.94479 | -60.02518 | 2026-03-01 05:59:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 273d2128-4f06-3a47-ad96-6ebb1ca405aa | 3.05414 | -60.68402 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 396f0ed8-b0ca-3a6e-96e5-639bcd2ed2dc | 2.82689 | -60.77452 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 18a05a53-afdc-3d2d-a0f6-a327f690bd65 | 3.46429 | -60.81639 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8381e47c-7686-3eaf-96d1-7117286a2ec4 | 0.89264 | -59.79151 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2d837512-c03d-3a5a-add8-23b2826bdaef | 2.90267 | -60.44222 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b14d17-ec77-393e-8ea0-45db6d4fa607 | 1.4831 | -59.93839 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24f02059-3dfc-38e8-8605-93d75b7eca72 | 1.49677 | -59.93615 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc413909-143f-3fac-b3db-ec31bbcb5ada | 1.5157 | -59.93752 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35da6f66-09e5-395c-b3e5-246749d4505c | 0.85522 | -60.40932 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e63671a7-d315-3b3d-9a07-2885411c5445 | 3.31344 | -59.9001 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d25e06e-075f-320a-9ee9-0887d148e992 | 3.31788 | -59.89937 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f5a033-cdc1-3ff2-8ca7-8f50bc3ee950 | 3.45181 | -60.81846 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 564114c8-055c-3646-b882-0c369d4a5806 | 1.49223 | -59.93696 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46d18a5b-49d5-3354-b6c2-2be64d4e5cca | 3.16647 | -59.91334 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73aac002-76a3-33fa-b59c-8be33f2d66e3 | 1.49073 | -59.92767 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46df07da-a707-33bd-9540-81e254625811 | 1.48997 | -59.92294 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce0abd10-2222-332e-ba95-a1d8199d8682 | 1.47169 | -59.92578 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 09623ca0-70db-3bdf-89b3-382991443298 | 1.47853 | -59.93905 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84702680-5a83-3baf-abde-5d604f57a238 | 3.15614 | -59.92186 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 499d3c29-559d-3b14-a2dc-9837e9d07233 | 1.87791 | -60.91174 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a541b93c-48b2-3b9b-999d-6bf212e893ed | 2.74811 | -60.74346 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0e7e861-cdb3-3025-81de-e4978c5e7a4d | 3.16292 | -59.90728 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ebcb74-4c39-3c97-97b3-21d4b7e3b2d8 | 1.49909 | -59.92144 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c0e6674-8644-329b-b1b2-78ff38e7bbc1 | 1.07949 | -59.25303 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c513a272-8f8a-3ba7-8529-4eeed00051fa | 2.30314 | -60.58736 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c325cce-423c-3e5a-8730-8256916af47b | 1.06504 | -59.25532 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 971fc621-c6c8-30a5-812d-1010f8647f98 | 0.5737 | -59.90742 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 092a42b8-9168-3765-9959-3ab81f0a3cf9 | 1.49378 | -59.91753 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 89ef793d-9eb5-3fc8-99ce-0e924db81f05 | 3.3925 | -60.21747 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90880f65-741b-3fa6-97bf-22faaec77e5f | 4.42349 | -60.74055 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fe5bf15-1703-3c78-8dbb-741cd0eadc50 | 0.65026 | -60.37631 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59dfcbf6-5f7a-3780-acb8-a6ad76ac9897 | 1.48541 | -59.92374 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d70ac7e-684a-36f2-8875-ed2a0ddeb58f | 2.61809 | -60.61392 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab3d3f9e-2c67-3dfa-9dd8-325946460aae | 1.47704 | -59.92989 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 11faa151-91e2-3654-8c49-2fbb7d2ecc56 | 1.06902 | -59.24933 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9df5ed6d-fdc2-3fee-8631-0137ee2426ff | 1.49985 | -59.92622 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5e252134-8d49-32f7-99db-db0a00c974ba | 1.8743 | -60.91633 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9cd7b66-7efe-33e2-aae2-8fd02797d3ed | 4.29326 | -60.06316 | 2026-03-01 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36008fb3-5cad-33da-a4a5-b7b4b09facee | 3.44518 | -60.8042 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3b8244-e394-343d-af71-3d8919e39b48 | 3.16202 | -59.91407 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e65e7017-edce-3dad-8e41-50c52d36649a | 1.48086 | -59.92456 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f8c65008-96f8-317b-bba9-fb2d996cd5fe | 3.48912 | -60.78521 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bde4f7b-c57b-3f7a-9cd6-76ad311e5815 | 1.48465 | -59.91904 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de668e2f-1faf-3d7f-96c2-fcecea862c96 | 4.09736 | -59.88662 | 2026-03-01 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b80c46-b8e5-39e9-8f2c-19580e3dc4e1 | 3.15684 | -59.92622 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 822c20f3-bf2c-3470-9d3d-78a96a2cd720 | 1.50443 | -59.92553 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb5dd7b2-8dcf-3720-a15f-0f65ad2a7b60 | 3.16432 | -59.916 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0ae6076-c43e-396b-b7d6-671124f39101 | 0.85639 | -60.40229 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9db86b34-4ae5-3072-900f-4e24f5c726e0 | 1.50733 | -59.94366 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca86d75a-469b-3c5d-a4c9-bccdca9b8e3b | 3.05836 | -60.68333 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d0d1756-5f48-3948-9ca4-d185b46afb8e | 1.03078 | -59.46651 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7628d98-0698-37fd-bddc-378cd6cb4c7d | 3.45225 | -60.79523 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d1e067-8393-3840-8ad0-e2cbe5ab8845 | 3.16574 | -59.90898 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c482af69-af7a-3a4a-aaaa-4fd502edbde5 | 1.36437 | -60.30962 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1158b506-e90b-3cc1-b020-1801e77272a1 | 1.0642 | -59.25009 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428495d4-783a-387f-bb9d-5838d277195d | 3.05774 | -60.67944 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c27e2328-e31c-3ae3-9d78-9ace9da76fc8 | 4.09804 | -59.89072 | 2026-03-01 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64936add-d9d1-386e-b9bc-75f42cbf34a7 | 2.90933 | -60.42864 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31c8de05-e5ce-31cf-8038-553e64736e63 | 4.09673 | -59.88279 | 2026-03-01 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e5223d-ec6e-31e2-8b86-321cf8b27e49 | 1.51188 | -59.94289 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4baf53bb-d8c2-3f90-bdce-b23078b7c398 | 2.74814 | -60.74216 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dc95649-cec1-3e28-840c-ceaf6d5cff5f | 1.49148 | -59.93233 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb0575d8-53cb-3079-be03-39e3be57d60b | 2.82331 | -60.77908 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |


[Clique aqui para ver as próximas entradas](README11.md)
