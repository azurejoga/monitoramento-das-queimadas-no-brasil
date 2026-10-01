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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7942b632-1c4b-33cb-9735-d09894a4e6c7 | -5.7376 | -45.1533 | 2026-10-01 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 02070257-6793-3ae4-82c9-4627f081ef93 | -9.1407 | -64.4024 | 2026-10-01 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bf30d6eb-8664-3252-8359-f79d30304311 | 3.2742 | -60.6105 | 2026-10-01 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 00f7e6ea-cf39-3e37-a265-fa40df55eb1b | -12.1857 | -48.4345 | 2026-10-01 01:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 26aca4fe-4469-3dbb-9c1a-dd52d63901f9 | -13.6479 | -53.9336 | 2026-10-01 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 98ce3cd9-15ac-3cf7-85ef-15236c9f98f9 | -3.1655 | -54.0844 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 260.5 |
| 670ecf2d-e401-3b31-9158-9d98fc97f8c3 | -18.0458 | -51.1336 | 2026-10-01 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8bb8d636-a97a-392b-9325-27c10e8a7195 | -11.81 | -50.4999 | 2026-10-01 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 26d9552a-fd20-31d6-abfd-88d18092dce3 | -3.1838 | -54.104 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 318.1 |
| 2be47d7a-74e3-31ad-987f-62336d76c15c | -6.0179 | -49.5648 | 2026-10-01 01:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6cb3d5be-d373-39b1-8e7c-d723137a30cb | -11.791 | -50.5021 | 2026-10-01 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f389ef92-d2e5-3613-81bd-4c708defbbac | -13.6671 | -53.9314 | 2026-10-01 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 31ddeb6f-b3fc-311b-9b38-83c285916a3b | -3.1061 | -50.2686 | 2026-10-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5cabbb1c-6159-3576-8098-617690c321f7 | -6.2797 | -43.2711 | 2026-10-01 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 7eef596d-c966-30cf-872b-efd1b8fa581e | -3.1471 | -54.0849 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 62b6b0bb-50bf-37bb-98e4-50564e938feb | -3.1839 | -54.0839 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 7b0f4968-ff77-3c3e-93a8-561c5c69acd0 | -5.7542 | -43.2901 | 2026-10-01 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5b756dcf-dfe3-304c-aa19-0b3d0a4d6f72 | -11.8287 | -50.5192 | 2026-10-01 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 92acec2d-7fe6-30f9-a2e7-2b8dca5a288c | -12.1857 | -48.4345 | 2026-10-01 01:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b0101664-0a49-3640-8e7b-9cffb3e59b23 | -3.1655 | -54.1045 | 2026-10-01 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 299.5 |
| 82c6a25d-7210-3624-bddf-0ddd7ae563ed | -11.1896 | -45.1966 | 2026-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| ff0c4b0b-c0f3-3554-86a0-f5b5ec51e42b | -9.1408 | -64.3836 | 2026-10-01 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1313c826-46ec-318f-9303-dcba2cad4a2f | -3.295 | -53.8597 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e87060b2-e3b9-3662-9981-f74b2108fe13 | -5.7561 | -45.1747 | 2026-10-01 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 88df2228-0cbb-3834-952f-9d3c2f286ee9 | -5.3347 | -48.9857 | 2026-10-01 01:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 9fe2d586-e4fb-3ef5-a7bd-afe9a55e6fa7 | -9.1222 | -64.3843 | 2026-10-01 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 68f00d5b-f586-333a-a8ee-aa6952a5005f | -3.5623 | -51.4838 | 2026-10-01 01:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cda0403e-aa7e-3e61-856e-98198e8c47ef | -5.7563 | -45.152 | 2026-10-01 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 15f3e180-f16a-3133-91c1-80c43a628f41 | -11.8097 | -50.5214 | 2026-10-01 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| dfaa6c7f-63a9-32e3-a328-9d8fdcc73f63 | -5.7355 | -43.2916 | 2026-10-01 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 69e05230-235c-39a8-9fa3-033e5b04b24e | -3.106 | -50.2896 | 2026-10-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| a47513e3-0630-391f-a880-8f04b36aaff0 | -9.1221 | -64.4031 | 2026-10-01 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 233bec3e-f409-33da-8db7-87c43e8b86ea | -3.1245 | -50.289 | 2026-10-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8097134e-ee5b-35d9-ace6-b871d7e1c5b3 | -3.5808 | -51.4832 | 2026-10-01 01:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dd782d40-d42d-3da7-8ae7-0012b740067a | -3.1656 | -54.0643 | 2026-10-01 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 524c8ba9-3bce-32a2-869b-23197ec3626a | -18.0658 | -51.1301 | 2026-10-01 01:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| acd17e62-02fb-3000-9e0e-9e1b55e6585b | -13.6479 | -53.9336 | 2026-10-01 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6ad711bc-9908-32d4-9b21-ce48976bba93 | -3.106 | -50.2896 | 2026-10-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 17e93ca2-8af0-31ae-9208-60c4305797e4 | -6.0179 | -49.5648 | 2026-10-01 01:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5bda2ed8-173e-3088-9dbb-e177fffedc1a | -3.1838 | -54.104 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 294.6 |
| e10b7b22-ef1b-3d63-b38e-a4e872828bed | -11.791 | -50.5021 | 2026-10-01 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f4df7605-c8b2-35f3-bf23-8373f208c8a4 | -4.4507 | -47.9112 | 2026-10-01 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5b8f0a84-d334-3e45-a67d-3c9735a71dba | -3.1245 | -50.289 | 2026-10-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 22c275e0-558b-363d-8810-3063d241c59c | -12.1857 | -48.4345 | 2026-10-01 01:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 245526f1-5c45-3408-beb1-0e4b6850c5ad | -3.1655 | -54.1045 | 2026-10-01 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 216.7 |
| f1fe42c9-e7ce-3bf1-8135-d4406b9f2d2e | -18.0458 | -51.1336 | 2026-10-01 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9f6298a0-fe6e-322b-906d-faa268808805 | -3.1061 | -50.2686 | 2026-10-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 761dccab-fdc5-385c-accc-af2837d6dee6 | -9.1222 | -64.3843 | 2026-10-01 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 71224428-a01e-327a-b4a6-252cf27093c3 | -3.1839 | -54.0839 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 2899e066-e2e6-302a-b1ba-c3db6a6ca57e | -11.81 | -50.4999 | 2026-10-01 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e29c8e93-7e59-316d-832c-c8d46e0587ec | -18.0658 | -51.1301 | 2026-10-01 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0d4084b6-2837-36df-b9a0-5d163eb9bd8b | -5.7563 | -45.152 | 2026-10-01 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 597e2166-f3f9-3fe1-bf99-e4b1c1a2f2ec | 3.2742 | -60.6105 | 2026-10-01 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ee69c8cb-bf1d-3e08-a13c-3fa45524b578 | -11.8287 | -50.5192 | 2026-10-01 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| aad1e55b-ad22-3068-a1d8-313244598695 | -4.4506 | -47.9329 | 2026-10-01 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5983fff1-3b16-34f1-8973-99e29b9273a2 | -4.4693 | -47.9103 | 2026-10-01 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4337894b-c4fe-3326-a635-53223f31cd5a | -3.5808 | -51.4832 | 2026-10-01 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b75a057a-2bea-3821-885e-70435f476966 | -3.1655 | -54.0844 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 243.2 |
| b219ce53-0cf0-3b03-a419-ef812199eff0 | -9.1408 | -64.3836 | 2026-10-01 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a4b5b69b-4281-351e-bc89-2221df272f40 | -11.4034 | -51.0361 | 2026-10-01 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8333b43c-bfd3-3416-94ba-181f003b4fe6 | -3.1656 | -54.0643 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cb77b7b0-bd75-31f9-9473-bf7b4d2e0d07 | -4.8551 | -45.8407 | 2026-10-01 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ae8c3c1d-791c-374a-9f9c-72492d26a106 | -11.8291 | -50.4977 | 2026-10-01 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 655ba851-4707-3212-9d76-de4bac39fe5a | -4.4691 | -47.932 | 2026-10-01 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 980ff813-7a41-3eea-9b77-589ac712851e | -9.1221 | -64.4031 | 2026-10-01 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c1a6de02-64ff-320e-97f8-7f30cfc5749e | -11.4037 | -51.0148 | 2026-10-01 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 6aee0473-16f0-356a-beef-c8c1cf1a5fa6 | -3.5623 | -51.4838 | 2026-10-01 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c2e8c8fb-3374-38f6-bb1b-a0e1cdd2004a | -5.7355 | -43.2916 | 2026-10-01 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 681b3372-570d-308f-9aa9-a474cc8808f0 | -11.8097 | -50.5214 | 2026-10-01 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 749a395b-0edd-3652-b32d-654a696b731d | -5.7357 | -43.2682 | 2026-10-01 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| da0b3215-d0e5-34fe-9a08-c38db4db99b5 | -3.1471 | -54.0849 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d923ea00-24b5-3766-be2d-22bf50d73446 | -13.6671 | -53.9314 | 2026-10-01 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f0ac6508-f42c-35b8-b22e-7387c72218bd | -3.295 | -53.8597 | 2026-10-01 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 511fe761-609c-381b-bb17-d7a4a37c3362 | -8.5738 | -67.0125 | 2026-10-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 20d867e0-2fb0-3869-be1d-199eb364dc5a | -13.6479 | -53.9336 | 2026-10-01 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1b1cd5c2-1ca9-344f-a0fb-688d5c0ef526 | -3.1655 | -54.1045 | 2026-10-01 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 212.3 |
| f5f182b9-f60c-39ef-bb87-436a02bc3ade | -3.1061 | -50.2686 | 2026-10-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| afb8bdbc-e957-3d44-b9ce-33957a0ceeb2 | -4.4507 | -47.9112 | 2026-10-01 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 22ed3ca1-aaa0-3aaf-9aab-0c3b73cef08f | -9.1222 | -64.3843 | 2026-10-01 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 118.7 |
| adbdb459-a82c-3055-968f-60e6d0b9bf04 | 3.2924 | -60.6101 | 2026-10-01 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 84c24f93-e1b3-3d6e-abf5-e6339b26ebfe | -6.0179 | -49.5648 | 2026-10-01 01:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 0a0125e9-e1d6-3aa4-8969-c986248dadfd | -8.5554 | -66.9759 | 2026-10-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c40d17f6-737d-3aec-9565-d5533c8e0a07 | -3.1838 | -54.104 | 2026-10-01 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 192.1 |
| 8f52279a-2adf-3cfd-9fa1-683e7c63decd | -8.5553 | -67.013 | 2026-10-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6ea2e1be-5684-3adf-957e-7ffd17c89183 | -13.6671 | -53.9314 | 2026-10-01 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8a26748e-94d6-3f01-be9b-44ce385bdf74 | -14.4612 | -51.2571 | 2026-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c9ae6244-8c7d-3b81-9da6-e50311ac0b69 | -2.908 | -54.151 | 2026-10-01 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| eea86954-281f-3f51-9654-6088ef15acf4 | -14.4418 | -51.2597 | 2026-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| df818462-bf70-3abd-a1da-062fbfc6e737 | -11.4034 | -51.0361 | 2026-10-01 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5c10b5a5-391b-303a-a4a0-035f0840b200 | -11.404 | -50.9935 | 2026-10-01 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 68fd38d2-8848-373a-ba3e-d3d08d8dbb14 | -4.8551 | -45.8407 | 2026-10-01 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8deeb8c2-13a2-3a91-9b6e-bcfb7717805a | -9.1221 | -64.4031 | 2026-10-01 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e48c0b54-b0cb-30ef-8ff8-f11d16676658 | -3.1655 | -54.0844 | 2026-10-01 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 246.4 |
| 1786a77f-cda2-3c47-bc74-f1562589118e | -5.7563 | -45.152 | 2026-10-01 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 55afe116-634a-31be-a874-1ad0d5058559 | -3.106 | -50.2896 | 2026-10-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ab388ca2-b514-3f27-96de-7381a571798a | -11.8291 | -50.4977 | 2026-10-01 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 8e562224-3239-3b93-9e8e-7b850da98784 | -8.5554 | -66.9945 | 2026-10-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 172.3 |
| b6e41fc0-8c86-393c-bf5d-a9395c3bbda2 | -11.4037 | -51.0148 | 2026-10-01 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 0c176d41-ddea-3fe5-90c8-4626a34b43a6 | -5.7355 | -43.2916 | 2026-10-01 01:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 395282b8-ca77-3adf-93d8-3220e2d4b81e | -12.0925 | -50.7023 | 2026-10-01 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |


[Clique aqui para ver as próximas entradas](README15.md)
