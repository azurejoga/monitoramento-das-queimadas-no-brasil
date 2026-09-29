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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 127d369b-ff01-3dff-aec6-8c3c773fd575 | -14.3886 | -52.1 | 2026-09-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0ec1356d-9b4a-33c7-974c-24e4398afdcb | -14.1115 | -46.2834 | 2026-09-29 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 452e7909-c611-3424-91b5-be2dfa41514c | -13.1803 | -48.5409 | 2026-09-29 14:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| b998dad5-a62d-3bc2-b1be-bdab90b607ab | -9.0463 | -45.0083 | 2026-09-29 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3a922c8f-d5d3-37de-a28e-7cbe7f2fa101 | -8.7264 | -44.9066 | 2026-09-29 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| bc126ddb-903d-3fed-b392-85a57b600777 | 1.8403 | -55.6442 | 2026-09-29 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| a1213791-13ea-3c49-80c3-157fbe73a192 | -7.3467 | -42.0839 | 2026-09-29 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 7f7c66ae-ece1-3e82-aa85-759e63d93102 | -13.3267 | -43.9523 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| d92db02e-9e0e-36ab-97de-45c3b570e30b | -10.2843 | -44.6274 | 2026-09-29 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 557.8 |
| 6666528e-5fc8-39f4-86f0-9a1fc98d574b | -10.2067 | -49.9898 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 84c47338-05cd-37f5-a990-e891875e0423 | -10.9154 | -50.7059 | 2026-09-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 127df783-37c0-3ef8-8586-6baac1531c10 | -8.0169 | -42.8444 | 2026-09-29 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 5cb9f3d3-f533-3da9-bb84-d144f026e563 | -11.6404 | -43.4981 | 2026-09-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 823f258c-1455-3876-94c5-a6a9e27f553e | -7.4871 | -44.5521 | 2026-09-29 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9633b612-e827-355e-864c-37306e7e64e4 | -11.9748 | -50.9295 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 98e7f639-e1c2-35b6-8f7a-577279f871c5 | -9.1525 | -49.9639 | 2026-09-29 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 07042d42-c221-36e5-8e81-f1c3cdbdf8ce | -13.3469 | -46.8169 | 2026-09-29 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ce4d1139-4929-3a14-9362-43f9068277cf | -15.735 | -46.0384 | 2026-09-29 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 4641ab2b-a4cb-3ed0-9dc2-daffc60b8e26 | -8.38 | -45.4448 | 2026-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 50fd77ee-49e9-3d47-8a1f-2693cf9bbd77 | -10.2656 | -44.6067 | 2026-09-29 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c61d2bef-c050-3f05-8f79-3d5135f63fe5 | -18.1158 | -44.3503 | 2026-09-29 14:40:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 185.8 |
| d04cb578-8d2e-3a01-a63e-3c07b90c5617 | -11.8614 | -50.8785 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ae149372-4fe5-3890-b43e-c85fed0a42d6 | -13.6762 | -45.7822 | 2026-09-29 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 8122f775-3240-31b7-9883-ee0a6ffd4a7d | -10.8967 | -50.6866 | 2026-09-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1c1f655b-e6bf-3c67-b9aa-552fc63802b6 | -6.7055 | -45.6892 | 2026-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d0add296-adbe-3f98-bbe2-5d72614d4e32 | -20.817 | -57.6919 | 2026-09-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| aed74267-a055-3ae8-a5f3-0982c3b7d602 | -20.9155 | -57.8456 | 2026-09-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 229.8 |
| 179b0bd6-3794-34cc-be35-d3dd9fd9f5c1 | -12.0806 | -50.232 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a4d2cc26-a74c-3f22-a5af-053e8b5c5a53 | -10.3082 | -49.4635 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| c3c42121-71e7-3c47-9ba0-a613bce77900 | -12.0181 | -50.5827 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d9e54975-9811-32cf-8a52-2da06d9da398 | -12.0997 | -50.2297 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 485d70eb-9ca2-3dfd-94ee-02dd207e4650 | -12.0559 | -50.5996 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 613996f6-810b-3809-bde6-ed124ad86f7b | -8.3617 | -45.4013 | 2026-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ad3b8c12-3a06-366f-b600-5f8cfabb5b4d | -12.2901 | -50.2496 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| fcf8506f-87c5-3c5c-852d-ba5882f1f4fe | -11.1907 | -45.1274 | 2026-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 884862c8-5477-3e11-89cc-32088cfb1672 | -11.98 | -50.5872 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 011edbf4-9c41-3fb6-978e-30ad3e1efc55 | -7.2718 | -45.3246 | 2026-09-29 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1f558f1f-ca7b-3c0c-9d29-5a296be65a45 | -11.8608 | -50.9212 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ed283355-f374-3a39-955b-2a456f8a1501 | -10.3895 | -61.231 | 2026-09-29 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| b9d7d303-87e2-384d-88c3-5f85e13b6dfa | -6.1598 | -52.9134 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 2f1f7a76-9558-38f7-a953-4829b67b0714 | -14.5362 | -48.2927 | 2026-09-29 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 46ec7fde-31ad-324f-a56a-45cf3d0f3cfa | -11.6784 | -43.5158 | 2026-09-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| f1983b3c-74bd-3b66-b756-96a8510932e3 | -12.0175 | -50.6256 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5a7fb477-177c-3658-ad37-a91be146df4a | -12.3088 | -50.2688 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| b82ec9b4-63a5-38b4-9d18-a710ad9c9e7b | -12.0369 | -50.6019 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| fbd799d9-0125-34ae-8204-1a508a46b07f | -10.7255 | -44.4291 | 2026-09-29 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0042f753-ae1c-3162-9c35-730d6e03b85d | -11.64 | -43.5218 | 2026-09-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| b5aecf3e-05c6-3aad-9288-84bd63866ffa | -11.7178 | -43.4623 | 2026-09-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| a505988b-ff02-356a-9b80-8088e672eb53 | -18.0956 | -44.355 | 2026-09-29 14:40:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 3a8ffd54-c52d-3fb5-9f72-f9ec695af09e | -10.2257 | -49.9879 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 96c1b948-d54b-3971-9028-c2b5703bef07 | -20.8373 | -57.6891 | 2026-09-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 156.9 |
| 4cf11b1c-fd72-3499-9c0f-177f41c1ef07 | -10.207 | -49.9684 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 162a665b-03a7-3af0-8c3d-f9d4a58a55bb | -10.2653 | -44.6298 | 2026-09-29 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 22d59c50-d982-3343-9573-f24727fc8145 | -12.2703 | -50.2951 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 15767f4f-8bcd-3297-bda3-ed2a22653c8f | -11.9939 | -50.9273 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2c1aacad-d91e-31dc-8611-48ac4290d2fa | -12.1734 | -50.3927 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8c59981a-0c31-374f-8723-50197a419237 | -20.9159 | -57.8246 | 2026-09-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 208.1 |
| 4cc5360e-95b7-34a5-bc2e-2dc6c8521432 | -11.9845 | -50.2864 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1aa9077f-dd2f-3512-bfc8-d1589993ef2d | -11.8805 | -50.8764 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| aaf015ed-55a8-361b-b7a6-6570ef20745f | -12.1027 | -50.0355 | 2026-09-29 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9123a96a-a8a8-3097-b255-b704e25ea62b | -10.706 | -44.455 | 2026-09-29 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 47947529-b99d-335a-b47e-c6b68acfef64 | -12.1185 | -50.2489 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| e8d8d1e1-8bae-3bd9-9ea5-f39d8ba73514 | -12.0642 | -50.0617 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 956bff9d-23b7-3733-b06f-9e667d4c7673 | -10.2254 | -50.0093 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5f6988b7-77a3-3a72-b356-34b21d86b2fc | 1.8403 | -55.6244 | 2026-09-29 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 9264cf27-7845-3172-8eea-590dd7caefd9 | -10.8109 | -48.7137 | 2026-09-29 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4f1581c6-01c2-3ed5-a0d7-1e5ba63c327c | -0.5258 | -49.1325 | 2026-09-29 14:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 67ace957-a6bd-3f0f-865d-3ae10b986267 | -12.0662 | -46.4643 | 2026-09-29 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 2589c72c-4ee0-386d-9a49-7f365db866bc | 1.822 | -55.6247 | 2026-09-29 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 4a4b32be-110a-3af7-9748-43b816a08ee2 | -10.8964 | -50.7079 | 2026-09-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 52ca23c7-a133-337f-aed7-5f6a733a6e7e | -8.2291 | -45.4602 | 2026-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0ff69b9c-adbf-3f95-8a8f-4bd7bfeb4799 | -10.7913 | -48.7596 | 2026-09-29 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a9d93191-7480-3e98-9a06-15b7981449d1 | -10.3894 | -61.2502 | 2026-09-29 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 2963a2b8-ac97-3242-9c1e-308f91dd4b60 | 1.4453 | -50.7863 | 2026-09-29 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 88f2d66c-00e0-3d70-a555-5f2a127a6b6a | -15.3807 | -47.9068 | 2026-09-29 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 8c236440-fd70-3a8c-b861-3c5c568a457b | -11.4791 | -49.743 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| adc70718-7cf5-3b60-8067-5e99e94e9e40 | -10.7916 | -48.7377 | 2026-09-29 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 10205266-b47b-3d51-9b1b-c2636d068512 | -11.8611 | -50.8999 | 2026-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| fdc846cf-a6db-35b6-94c0-c9de8b758ace | -9.0249 | -49.6334 | 2026-09-29 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 84012546-9c80-315a-a206-35278e46d61d | -15.3802 | -47.9294 | 2026-09-29 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1907f451-8463-3e70-adda-5eab4b160ad4 | -12.0365 | -50.6233 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a2f0a11b-25a4-323c-943f-6e6dc8a379f7 | -4.2981 | -48.6094 | 2026-09-29 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e6efd87b-2d79-3ae3-850a-151930d82035 | -11.9842 | -50.3079 | 2026-09-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 93bb363e-13b0-3aec-8a0d-d69a234d56e9 | -15.3998 | -47.9261 | 2026-09-29 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 54df8cf2-b85c-3c2c-8bbb-9aefc9d5d039 | -10.2065 | -50.0113 | 2026-09-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 093638df-80f7-3836-a75e-f6392d2645d9 | -6.5593 | -45.3173 | 2026-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a0799fcb-ee22-3a94-b1e6-80ccc864361b | -20.8369 | -57.7101 | 2026-09-29 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 6f770b0f-2ac9-394e-83b8-c053827b4f2b | -10.9156 | -50.6845 | 2026-09-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4953c7ef-2f1e-3989-a859-4e9e84172d0e | -6.7251 | -45.5975 | 2026-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 729eb1e1-daf9-30ec-b7fc-c6b108c55ed9 | -8.2102 | -45.4621 | 2026-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 42e116c4-6a28-3e0d-8be3-d311e4210b4e | -10.7064 | -44.4317 | 2026-09-29 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 7347bcb9-5220-36ca-b0bc-f43b19c1c825 | -12.8847 | -44.8015 | 2026-09-29 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 31483bc6-78b2-37c7-b912-9fc8768c818b | -11.9606 | -50.6108 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f94412e9-b7fc-38b9-8b57-d01eabfa7d59 | -12.0997 | -50.2297 | 2026-09-29 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 577d1bd1-79b0-39ef-a35a-c4b5b688710b | -9.1337 | -49.9656 | 2026-09-29 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 88c19ee1-7222-3955-a152-bd1f857af38e | -20.8373 | -57.6891 | 2026-09-29 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| a017437d-cb7e-3aab-94ca-f8e7c5d88939 | -12.7226 | -50.669 | 2026-09-29 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 4026329e-b930-31d7-9e64-3771b7c8bf94 | -7.506 | -44.5503 | 2026-09-29 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 3aac9f44-b1b8-320a-aee0-8db6068b6199 | -11.1707 | -50.0581 | 2026-09-29 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 73387e6a-ffa4-3187-a932-6195b86e5ee5 | -12.374 | -46.3972 | 2026-09-29 14:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |


[Clique aqui para ver as próximas entradas](README83.md)
