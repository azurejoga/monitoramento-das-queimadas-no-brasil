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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e357d80e-a574-3f41-a81b-581f02f4d57a | -5.1255 | -55.955 | 2026-09-15 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| d91095df-edc8-3bd0-959c-f339ab7fda91 | -13.2678 | -51.2856 | 2026-09-15 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3dfaa874-a832-355a-b245-6ddf128e9b58 | -10.4769 | -50.9846 | 2026-09-15 13:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| fa9a89ee-28c4-36b2-abcc-3979e3e337c8 | -7.0164 | -44.6413 | 2026-09-15 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3227f15c-843c-32ed-90f1-89a7acf5dd1c | -5.1256 | -55.9352 | 2026-09-15 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2960599f-63ed-3885-8040-50f6c4b541c1 | -13.287 | -51.2832 | 2026-09-15 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 213.9 |
| b1a1cca1-c997-38b7-ba66-e256ba9fea80 | -2.9025 | -50.4004 | 2026-09-15 13:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f498f24f-93a0-306a-a49e-87da9b302219 | -8.5468 | -50.4423 | 2026-09-15 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 563.2 |
| 7b3a686e-e215-3b82-bea3-dafc1906f1e1 | -6.8217 | -43.5271 | 2026-09-15 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| df2d881a-5504-34bb-af20-6949c51a871a | -11.2113 | -54.1208 | 2026-09-15 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 304bcf37-c76b-3d3a-924f-bef03bc6ca38 | -18.1709 | -51.7685 | 2026-09-15 13:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 51f19593-d103-3804-8b33-af683f383821 | -9.3575 | -50.1156 | 2026-09-15 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| dbc31f26-e13e-3869-8d2a-474956c4ad03 | -15.5763 | -48.8144 | 2026-09-15 13:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3161bef3-b3ea-3b50-94c5-abc3b55905e7 | -8.638 | -44.4567 | 2026-09-15 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 7720b85f-05c2-3f0c-bf9f-f6c17e462e59 | -7.0166 | -44.6184 | 2026-09-15 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 65e80b31-43ac-322b-9ad9-2794bfc469d8 | -9.475 | -45.4612 | 2026-09-15 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7e330d33-9e52-32cd-8ef7-0e7d64d9c8bd | -8.5656 | -50.4407 | 2026-09-15 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| aad636d8-df75-36ef-b45d-0dc79fca7f90 | -10.8665 | -46.3105 | 2026-09-15 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 1778c8b0-2e4e-33b2-909f-b5d750c88127 | -9.4234 | -47.8588 | 2026-09-15 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9f3925c4-6517-33a2-ae6a-d061d1010820 | -9.4234 | -47.8588 | 2026-09-15 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 43aa6def-cbe9-35a5-9095-bc29199d363a | -6.8405 | -43.5254 | 2026-09-15 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 48b049a7-ea1c-34f8-84d5-d414841fca53 | -5.1256 | -55.9352 | 2026-09-15 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| c24e41d6-2aba-32fa-90c0-799b2dd0ee10 | -15.5763 | -48.8144 | 2026-09-15 13:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 04e01739-9ecc-3a60-8f31-b349039fb3cb | -10.0988 | -45.5685 | 2026-09-15 13:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7af99dec-06a3-3951-993b-f95eac4312e3 | -7.0164 | -44.6413 | 2026-09-15 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f706328b-118d-3755-b087-552a72b46ae4 | -5.1255 | -55.955 | 2026-09-15 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| dafda1ad-287f-3fd4-a996-583d261e1bab | -11.9033 | -43.8112 | 2026-09-15 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 01852f09-6c94-318e-8c57-dc83ac7c9178 | -2.7768 | -49.4553 | 2026-09-15 13:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6e2a983a-72df-34ac-a9aa-637f7ae599f5 | -15.539 | -53.8502 | 2026-09-15 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b70a5e4c-762c-3d7b-a920-5ba1c8a24706 | -8.5468 | -50.4423 | 2026-09-15 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 323.1 |
| 070c8e1b-2b35-33cd-b4b4-be6593eb71d9 | -7.0166 | -44.6184 | 2026-09-15 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| cdd49bbc-85cd-3cbe-99ca-38c3e72bfb17 | -18.1714 | -51.7466 | 2026-09-15 13:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 61da016f-d5d9-365e-b00d-da614b789e65 | -7.082 | -42.1346 | 2026-09-15 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| ad2cacba-4a6f-3042-a214-ca07ae64f45b | -10.8661 | -46.3331 | 2026-09-15 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 22a9bd11-cc39-383e-a25c-c0fbf3cc3f9d | -2.9025 | -50.4004 | 2026-09-15 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 66cabb57-7604-375c-aef9-417b31c30a74 | -4.5229 | -54.9639 | 2026-09-15 13:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8c0062ca-bb47-3f1d-8e31-9daee5a7d232 | -10.8665 | -46.3105 | 2026-09-15 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 233.7 |
| d2cc7542-4cf1-3c50-95a4-a0d30af8d9f2 | -9.7687 | -46.1067 | 2026-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 54dd3006-1c96-3e5f-aa76-5b10ba15ec6d | -9.3572 | -50.137 | 2026-09-15 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 58533a7e-5b9b-362c-893a-d2d4fdf49516 | -9.3575 | -50.1156 | 2026-09-15 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| ca6b65ea-6c1d-38ec-aba2-39beae93e2ea | -7.0823 | -42.1107 | 2026-09-15 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 308e976d-1ff3-30e3-be5f-8db236ef4fa4 | -2.9025 | -50.4214 | 2026-09-15 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| aadd8867-e03d-3916-b0d6-0946480e261b | -10.3109 | -45.3595 | 2026-09-15 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ad5088dc-53c6-3a2a-82c6-166e02509fc1 | -10.6962 | -47.4953 | 2026-09-15 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| a5ca0720-fac6-3033-a448-8c245cf005bc | -8.5656 | -50.4407 | 2026-09-15 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 437.0 |
| 6f1e7fd0-2677-3b4f-be2f-737501f723af | -10.312 | -45.2907 | 2026-09-15 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1df02701-d445-3a8a-98b2-0b9eff787993 | -9.7358 | -47.0958 | 2026-09-15 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6b161a12-d62e-3c70-b774-a8d090781a7d | -18.1709 | -51.7685 | 2026-09-15 13:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| a29112a2-25b6-303d-9428-f78642f069a0 | -11.8154 | -46.5899 | 2026-09-15 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a0b3a957-3ab5-38ab-8485-815ebe40c827 | -2.9209 | -50.4208 | 2026-09-15 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6198767a-fb91-3627-a44e-cf2e19fbbcb8 | -5.1439 | -55.9543 | 2026-09-15 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 805e839a-59b6-36d2-bd70-e81f53c0053b | -2.921 | -50.3999 | 2026-09-15 13:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e6333ef4-5154-3c0c-9400-d9cfe624e34b | -8.6191 | -44.4588 | 2026-09-15 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f7ef69a6-239c-3224-9674-9ddea12f888b | -13.287 | -51.2832 | 2026-09-15 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4096cedc-f01f-38c1-90e1-161ebcf9ca10 | -10.3116 | -45.3136 | 2026-09-15 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 66bbe260-188b-3efe-9e7f-7b0270fa0363 | -8.8137 | -46.905 | 2026-09-15 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8df0ea17-870d-3f5f-88ee-a4f0df630888 | -10.3113 | -45.3366 | 2026-09-15 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 3ef50bd0-1ad4-397b-8800-8c88f58d49fc | -10.792 | -46.2071 | 2026-09-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 793c948a-5ada-3ade-9ab8-1d58e8b0749b | -2.6602 | -57.5313 | 2026-09-15 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 46cff4fd-f62c-3c36-ae70-d65a89ec57f8 | -2.6601 | -57.5507 | 2026-09-15 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 69b35b52-5d7f-3867-93f8-db88d5d191c1 | -8.638 | -44.4567 | 2026-09-15 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 264816cb-39f6-3666-98f9-22e2f24ab224 | -13.7002 | -51.8274 | 2026-09-15 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a515e811-d8bb-3889-b2f7-8b4b59a6970f | -10.5788 | -47.7306 | 2026-09-15 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 5cb1f672-a936-38d6-bc14-4dc3d4e03589 | -11.5041 | -45.7939 | 2026-09-15 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d4bd4e43-66f0-30c1-be74-e1adb2a96565 | -8.6383 | -44.4336 | 2026-09-15 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d1d73585-3359-374f-9677-1bdf4fa66c8a | -11.5045 | -45.771 | 2026-09-15 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 40e97aa1-dc4e-37ca-92f3-bca31ce5883a | -5.144 | -55.9345 | 2026-09-15 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 05a5dd75-20cd-339c-b0ed-57f21bb624aa | -13.287 | -51.2832 | 2026-09-15 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d815393f-8d22-3a20-b699-f0b28e3a5914 | -9.4234 | -47.8588 | 2026-09-15 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| ce9b9af7-ab77-3a41-a816-4ce11e5c7749 | -9.7687 | -46.1067 | 2026-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 56645ac8-ffd4-3b4a-b433-74d5391dd334 | -13.7006 | -51.8061 | 2026-09-15 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c9bd1472-1aa3-356e-b70a-d44e823b4c16 | -2.7768 | -49.4553 | 2026-09-15 13:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 95ac4fcd-6ed4-3ae8-a19f-73112658a464 | -2.9025 | -50.4004 | 2026-09-15 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1216ab3c-afed-3ddd-9781-52c998bfde47 | -10.8665 | -46.3105 | 2026-09-15 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 69838354-2c0b-30f8-8f61-5e1b3125cf7d | -11.5041 | -45.7939 | 2026-09-15 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 742c336f-3439-344b-8fed-067f66357a79 | -11.2302 | -54.119 | 2026-09-15 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 65683480-00b8-3399-90c3-067b6da17b35 | -5.1255 | -55.955 | 2026-09-15 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| aacc6048-e8c0-302d-93b7-83d6ede6ad9d | -11.9033 | -43.8112 | 2026-09-15 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 555b6ba9-d865-39fb-a8db-d139790fb153 | -8.6191 | -44.4588 | 2026-09-15 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a2682b68-ae16-33c0-993e-2ec69dbc3646 | -2.9025 | -50.4214 | 2026-09-15 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 21ff3a9d-6b86-3aa4-b992-fe3439a9a1a1 | -7.0166 | -44.6184 | 2026-09-15 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7e331486-85fb-3461-8761-f8842471190a | -10.5788 | -47.7306 | 2026-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 417bf8ad-c6c6-393d-b6ba-59464ca95b29 | -10.0988 | -45.5685 | 2026-09-15 13:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| cdaec3ac-7bdc-3a97-aa11-9f40c023931d | -4.5229 | -54.9639 | 2026-09-15 13:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c13d791e-992b-3e28-8bc9-463ae98f7152 | -10.3109 | -45.3595 | 2026-09-15 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b463e5a7-7572-31a0-9eb7-3fbd6e73fb32 | -18.1714 | -51.7466 | 2026-09-15 13:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 5f2a66b0-f82b-3f82-ba49-c172f26ff404 | -5.1256 | -55.9352 | 2026-09-15 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| f819e831-61f5-3b94-9c1b-7beae9274b1a | -2.921 | -50.3999 | 2026-09-15 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 429f31b9-677d-3275-8662-89bba67b042d | -11.8154 | -46.5899 | 2026-09-15 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 33046cc9-8e5f-3ba6-b0de-faec940af8a3 | -9.3577 | -50.0943 | 2026-09-15 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 83d25c73-b2e3-35c2-b330-bb6847417009 | -9.5918 | -46.5765 | 2026-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c4dada35-d0f1-3815-814e-312bd439baf5 | -10.5785 | -47.7528 | 2026-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 1a87b832-0f07-3f0d-844f-4cc3037d1559 | -14.1666 | -47.3876 | 2026-09-15 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b4ec26c6-52c4-3281-a09a-01e89fe98c47 | -2.6784 | -57.5698 | 2026-09-15 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f521f6f2-bfce-32d1-8ac8-95047431d229 | -9.3575 | -50.1156 | 2026-09-15 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 6020f2de-b06b-3b62-bdc9-0152dd2216a0 | -10.3113 | -45.3366 | 2026-09-15 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 5dfbdeda-f8ec-3818-bad3-18d8784e30f6 | -2.6784 | -57.5504 | 2026-09-15 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 406417a9-6d88-3edb-9593-7c1c358978b1 | -10.312 | -45.2907 | 2026-09-15 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 58fe70b9-1ba8-35de-af06-4500dea1e8fb | -11.0434 | -49.6851 | 2026-09-15 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 5e79c5d4-dd17-3786-a03d-519a9ebc33fd | -8.5656 | -50.4407 | 2026-09-15 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |


[Clique aqui para ver as próximas entradas](README76.md)
