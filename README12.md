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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 568099ad-c8fc-3433-9d7d-8ce9d0b15d56 | -3.9289 | -48.3458 | 2024-10-29 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 98b70488-3687-3927-a488-1b1fce0b12c5 | -4.1024 | -50.5271 | 2024-10-29 00:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| c7f7695b-dc8b-36ae-8e76-a3dda62e7bff | -4.3473 | -43.779 | 2024-10-29 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d3d8f1b0-2592-376c-ad61-f16380d72b70 | -4.3475 | -43.7559 | 2024-10-29 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d9125838-b64d-34b0-9e39-4d51a388c47f | -6.5054 | -47.0414 | 2024-10-29 00:35:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| fa6e736a-913f-3b1f-9381-9874e0b62302 | -6.5956 | -47.3867 | 2024-10-29 00:35:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 187f408b-0910-34ea-8d4f-242aad62aaf9 | -6.6143 | -47.3853 | 2024-10-29 00:35:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 789e7eb1-67e9-3087-9b93-b8a08d2af023 | -11.1378 | -55.5515 | 2024-10-29 00:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6451c7c4-38f2-3ed0-94be-3883219a621c | -11.138 | -55.5313 | 2024-10-29 00:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 27b6ac82-3a73-325e-9f73-3cc1512e40eb | -12.1045 | -52.4782 | 2024-10-29 00:36:14 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5b7c075d-daac-356c-8b5c-da6f00f56fbb | -12.3331 | -49.9424 | 2024-10-29 00:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 9a5894f2-5e4e-3a99-805d-7fb5f7b2f8ea | -12.3334 | -49.9208 | 2024-10-29 00:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8f206e92-bc68-3b44-b57d-7698822ac4c0 | -12.3522 | -49.94 | 2024-10-29 00:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 89585c75-c36b-36e2-a238-192ff7dc2495 | -12.3526 | -49.9184 | 2024-10-29 00:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4a2eafdf-ce95-3bb8-be9e-c15718f07cbb | -12.6725 | -43.8279 | 2024-10-29 00:36:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ca55aaea-3dcc-349b-8d27-732835017ab5 | -13.6222 | -45.5838 | 2024-10-29 00:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6ec5c8b9-8f0d-3eef-baa1-4753e2f465e4 | -13.6227 | -45.5606 | 2024-10-29 00:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3e4fb054-2787-3e37-9058-0bf4e31f9347 | -13.6887 | -46.1247 | 2024-10-29 00:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9aeddb49-5288-3a1c-a27d-d97390d62fe9 | -13.6891 | -46.1017 | 2024-10-29 00:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e29cc64c-c062-3d05-beac-62662e3391df | -14.1329 | -44.351 | 2024-10-29 00:36:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| a2f773b5-71ba-3149-b759-4782aa06be89 | -1.714 | -54.5335 | 2024-10-29 00:45:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 7160cb48-4372-3cfc-869d-a8d54508b205 | -2.3353 | -48.9137 | 2024-10-29 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 4ce6c1ef-3b68-3f06-a517-fc4445a0acc1 | -2.3537 | -48.9133 | 2024-10-29 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 548a70dc-ea8c-3df0-a7a7-d438e416f0a4 | -2.3538 | -48.8919 | 2024-10-29 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 3b2a443e-1b43-32b8-9da4-ffe430840349 | -2.5066 | -47.4425 | 2024-10-29 00:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6475cc72-59bf-3c66-a78b-0655464846e6 | -2.5251 | -47.442 | 2024-10-29 00:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 98a7ce5c-680f-3fc1-abbc-1d26e73c722b | -2.8146 | -49.2206 | 2024-10-29 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 76984293-b2b8-3c67-8e1b-6a1e456b78c8 | -2.8555 | -53.3459 | 2024-10-29 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0f27b262-566f-34ff-ada4-c4a27b7c7db5 | -2.8739 | -53.3454 | 2024-10-29 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fff33ebf-d072-3dee-a274-7151857dc4b3 | -2.9619 | -54.5304 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 28f9c632-164d-3df9-a025-5b73c07fa469 | -2.962 | -54.5104 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 6ed1064a-4abc-318a-a4da-5d3d7cd862d9 | -2.9803 | -54.5299 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 5aee01e3-73e7-378f-b603-db243120fb80 | -2.9804 | -54.5099 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 515b99eb-c199-3336-94f9-ab7b10048739 | -3.0913 | -54.287 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6fccb614-fe35-333f-b5d2-e023f4a0236c | -3.1097 | -54.2865 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 1b5e7fde-4a49-3205-961f-426854b154e0 | -3.1098 | -54.2665 | 2024-10-29 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6f93a181-d572-341a-b382-708af0bae5fe | -3.1794 | -50.3922 | 2024-10-29 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 77051fb9-24a9-3389-807d-5573609fb0d5 | -3.1281 | -54.286 | 2024-10-29 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9d451496-4acd-32ab-8d19-23dcdf4abff5 | -3.1281 | -54.266 | 2024-10-29 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| cf21f76a-f455-3578-ad1b-30514d5315a5 | -3.8308 | -45.9388 | 2024-10-29 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e09b3c9e-4bc0-3162-9e3f-ce09b35699d7 | -3.9289 | -48.3458 | 2024-10-29 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 62f614e7-2282-3475-8c3f-6aca982f5627 | -4.1024 | -50.5271 | 2024-10-29 00:45:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 12d920d1-9fbf-3737-8c23-574ef268da5c | -4.3286 | -43.7801 | 2024-10-29 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 58e2257d-cf67-3faa-967d-74962d0f6e66 | -4.3473 | -43.779 | 2024-10-29 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 1a5251f0-18d3-3882-bba7-b68cf1d6548b | -4.3475 | -43.7559 | 2024-10-29 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8785e20c-2201-33e8-b286-a9a50650f211 | -4.4631 | -45.9744 | 2024-10-29 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1681e984-4659-39a9-8e63-dd11cd395c49 | -4.4632 | -45.952 | 2024-10-29 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 89c8c61c-2d97-3d92-ac58-9b3cdd6aac9f | -4.6432 | -44.1762 | 2024-10-29 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8ac92518-daf4-3977-a884-bfb21081f31b | -4.6618 | -44.1981 | 2024-10-29 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| de20e933-f2d6-34ec-a9bc-faa914354b73 | -4.6619 | -44.1751 | 2024-10-29 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| bfc2e307-0844-3e14-8b7e-0c810caf2063 | -4.6621 | -44.1521 | 2024-10-29 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| f3b77542-5e14-3cec-876a-44331a557a43 | -4.6806 | -44.174 | 2024-10-29 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 61f33821-2b49-339a-a98a-c0f9c6f95791 | -6.5054 | -47.0414 | 2024-10-29 00:45:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 546cd642-765a-388b-9777-89150e3ce269 | -6.5956 | -47.3867 | 2024-10-29 00:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9d717670-4304-3c33-969d-84cf8ced5763 | -6.6141 | -47.4073 | 2024-10-29 00:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 77f3b158-e5fc-3012-8f53-89813102c17d | -6.6143 | -47.3853 | 2024-10-29 00:45:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1e125ac0-e7aa-3d80-85ae-5167a5db2f2b | -11.138 | -55.5313 | 2024-10-29 00:46:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e1f5c1b3-16f6-3a34-acc6-69112b89d797 | -12.6725 | -43.8279 | 2024-10-29 00:46:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c9f1a8ec-5ea0-35e2-ae69-8824a2f49c96 | -12.673 | -43.8042 | 2024-10-29 00:46:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c0672894-8601-3bd7-bace-13561fc9ceef | -1.714 | -54.5335 | 2024-10-29 00:55:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 12c18da4-1360-35cc-b578-07cdc793181f | -2.3352 | -48.9351 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f82be1a9-e872-30db-aa76-a6ff8f92b441 | -2.3353 | -48.9137 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 9812e6d1-38a2-3f6d-89b3-f48a2820209f | -2.3353 | -48.8924 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c6eaa6df-998f-3390-8145-76a057594dd0 | -2.3537 | -48.9346 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e5768657-1812-347f-880b-a1a385002038 | -2.3537 | -48.9133 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 264.5 |
| 126629c8-6611-347c-ba80-0b6af400c9bc | -2.3538 | -48.8919 | 2024-10-29 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 154fd57b-5663-37e2-a432-691b75c61a8c | -2.5066 | -47.4425 | 2024-10-29 00:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 31f7093c-85cf-3c89-94ba-4d2b91212ca6 | -2.8555 | -53.3459 | 2024-10-29 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 51ce3e3e-55f0-31ac-ab3b-1da3ade18667 | -2.8739 | -53.3454 | 2024-10-29 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b2a3f70d-e891-337b-b08a-c0dd8fe3fb9a | -2.9619 | -54.5304 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b563acc6-e80d-346d-a3d9-77d166b15170 | -2.962 | -54.5104 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 39f5327a-1384-3b5d-b7df-43db87170b4a | -2.9803 | -54.5299 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| af218c08-0044-3adc-9b1f-4f9db20f81f0 | -2.9804 | -54.5099 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| cee0cb25-8446-3bcb-9bf3-cf62a01018d5 | -3.0913 | -54.287 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 624de4d4-f51a-3fac-b482-c15ea20434d8 | -3.0914 | -54.2669 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1916a49d-c3d9-36d2-bd55-929840f2a6c0 | -3.1097 | -54.2865 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 1a013812-ab54-38be-bbc0-a55bc091aa11 | -3.1098 | -54.2665 | 2024-10-29 00:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8fbf697e-551d-3d1c-a291-656e18bc9937 | -3.1281 | -54.286 | 2024-10-29 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ebc5db38-51a3-38f0-9dc1-70a3cf83b845 | -3.1281 | -54.266 | 2024-10-29 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fecec54b-aac9-3e3b-9c84-9ea4baae91e5 | -3.1794 | -50.3922 | 2024-10-29 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1b5b47ba-9e0b-35dd-81e0-0f2c552c7f48 | -3.3044 | -47.198 | 2024-10-29 00:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 32ed58bf-8de1-3dec-8077-cc1f454f5ebb | -3.3275 | -50.3035 | 2024-10-29 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ab368975-4b95-3a20-a1b2-e43b08f1b3fe | -3.9289 | -48.3458 | 2024-10-29 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6e7f8f7d-7ba0-3317-a43e-9387836f0566 | -4.3286 | -43.7801 | 2024-10-29 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1e674457-c09f-3086-8c26-bdd9514f88e2 | -4.3473 | -43.779 | 2024-10-29 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 22012fe7-650e-35c6-9cab-3fd3164c798d | -4.3475 | -43.7559 | 2024-10-29 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b86d51ff-6c35-3016-97b2-b4ef0af4a8f2 | -4.4631 | -45.9744 | 2024-10-29 00:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 931a9566-2ab0-3b86-b987-ed981f551a1f | -4.4632 | -45.952 | 2024-10-29 00:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5ff6404d-d06d-353e-90db-2e87041a259e | -4.6431 | -44.1992 | 2024-10-29 00:55:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 30791635-18fc-3fc9-b1f5-eaf5e096fe7c | -4.6432 | -44.1762 | 2024-10-29 00:55:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f545fd0f-794b-3690-b841-067799b6a6e2 | -4.6618 | -44.1981 | 2024-10-29 00:55:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 843b00b9-5d2d-321a-9b44-4099eebb1915 | -4.6619 | -44.1751 | 2024-10-29 00:55:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ee5e22b7-15f7-31fd-892f-07203e4194cd | -6.5956 | -47.3867 | 2024-10-29 00:55:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 05396932-c27c-3745-bde9-23bff9a3d952 | -6.6141 | -47.4073 | 2024-10-29 00:55:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8f138c2a-7c52-3bab-a705-ba3f133d3bf2 | -6.6143 | -47.3853 | 2024-10-29 00:55:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| e738227a-1156-324e-ac72-98e231ae8e22 | -11.1378 | -55.5515 | 2024-10-29 00:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3a7b21b1-7df1-36ef-bb44-00af8749fafd | -11.138 | -55.5313 | 2024-10-29 00:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 383b77c2-f4ab-3ae9-89c1-39c99104b73e | -12.3334 | -49.9208 | 2024-10-29 00:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e255dc8f-cc80-3bf8-9c8c-cdea052e2da2 | -12.3522 | -49.94 | 2024-10-29 00:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 95271fff-d130-38d9-8b31-c518f98a1f6c | -12.3526 | -49.9184 | 2024-10-29 00:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |


[Clique aqui para ver as próximas entradas](README13.md)
