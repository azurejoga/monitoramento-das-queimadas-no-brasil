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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cba6173-554c-3df3-a82e-6dc40adf97c9 | -4.36951 | -48.22609 | 2025-07-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b593f857-45ef-3961-83c4-b94be5f8f26f | -5.61664 | -46.24217 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f061fed-d19a-392f-a287-161bf279e18a | -6.89426 | -44.05009 | 2025-07-11 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d9fef24-7928-371a-9249-73b4d886fcb5 | -6.67685 | -46.30183 | 2025-07-11 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de04b922-4eac-3f55-94b5-25d31fb5a767 | -7.24322 | -39.17716 | 2025-07-11 04:06:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4fc53a21-85b3-367e-b94e-cfc843ba781d | -7.18955 | -43.35438 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2f6cc96-66aa-3bca-8d4c-71b0e308326b | -7.08187 | -43.41134 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c6e1369-1927-3a97-af31-25afe4b50041 | -3.58213 | -49.43309 | 2025-07-11 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d6e6cf-381c-3fa8-af8e-1d589b51529f | -6.14349 | -45.90603 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f50dc04-83ac-3e4a-b6f2-54b6ff8f69f3 | -6.61075 | -47.98953 | 2025-07-11 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 702a3227-bf3c-350a-86a6-a32b51a59ab2 | -5.55127 | -43.90054 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a049bbd1-8ec0-35db-8ebb-61726b953451 | -6.86756 | -42.77945 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ac5a68d-6f37-3f85-915e-6d1da6238eba | -2.44354 | -47.32705 | 2025-07-11 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec2109c4-90e3-3774-947f-5f16e1056de7 | -6.99171 | -44.45216 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6674769c-1224-34db-9643-f770f9d03f8a | -6.61152 | -47.98863 | 2025-07-11 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e142258f-6df5-312b-82ff-06e8d6c819ea | -6.14814 | -45.90181 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1331079e-5595-3386-ac06-074298dc3b72 | -6.99292 | -44.44778 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6440ce27-0520-3a46-bd62-44bac4d118c4 | -7.20171 | -43.11639 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 21cf26c7-bd13-306e-82a1-57e89fef9a87 | -7.19443 | -43.11888 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f426454f-01fc-30b4-a0b2-08462f3e4249 | -7.18494 | -43.11368 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2735c7b1-6936-3435-9ff6-fe2f4195beba | -7.19221 | -43.1112 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fdaf2697-7a3b-3011-813c-d19dc3aa0e34 | -6.98876 | -44.45112 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72106cbb-b674-3b75-80fe-1499aec74670 | -6.13883 | -45.91035 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 579e66f2-ddc4-382d-b988-645d7ce28e35 | -4.54752 | -48.00914 | 2025-07-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 285164b2-a3b3-30c3-99bf-d8493ffe13b7 | -6.86423 | -42.77892 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35ffcc06-b1c3-3511-84b9-38a1a077ef31 | -5.03501 | -48.51804 | 2025-07-11 04:06:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23240e1a-f9e7-3373-ac4b-a00e8ba5cda6 | -6.8709 | -42.77998 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74112cd7-8698-35b5-b667-1c37a4cbdbae | -5.20022 | -37.66504 | 2025-07-11 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dc55334-c8e9-3d34-b846-c639981627ba | -6.87034 | -42.7835 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a27df12-a639-3364-b8e2-88c5257dc974 | -6.67294 | -46.30116 | 2025-07-11 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09bcfd3d-44d6-38ca-a953-a49ec002e350 | -6.13819 | -44.10642 | 2025-07-11 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43449f82-64ca-304b-9fa1-d9223da199c5 | -3.74942 | -47.12329 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 825e22bb-5bd2-3d55-954a-dc0b6458b504 | -6.95817 | -42.72163 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ae3d51c-e953-324b-97d1-01f45eccd9d8 | -7.19778 | -43.11942 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 88b0165b-ba32-36a0-8c7c-6c3dd7ac7026 | -7.19293 | -43.35492 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c99fb32-40ff-32ad-810d-88a6efd8612c | -6.9805 | -44.45447 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11bb534c-95f3-3bd3-811b-e13b5d03fa99 | -7.19835 | -43.11586 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 87fc6c8f-1595-3603-834c-27dfbbc92145 | -7.19557 | -43.11175 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9f4bb4e3-9867-3c8a-8388-e11d106b641a | -7.18993 | -43.1255 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bedd0a5a-3df2-3e50-bce1-131afe4f2274 | -6.85417 | -42.799 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 96e60b6f-faff-391f-afb9-e0587009f96e | -6.67673 | -46.30432 | 2025-07-11 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64b6bcd1-b230-30c3-9241-e3b8f4c19e22 | -6.85756 | -42.77786 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a8f042d-cf65-3428-9e3f-2df4cf07ff92 | -6.99108 | -44.45608 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78d97945-c109-3173-a207-76c31d5645c0 | -6.13498 | -45.90971 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd463643-9678-3728-beb4-4b7d4c8df113 | -6.87419 | -45.22767 | 2025-07-11 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa72a200-e48e-30e1-be68-0a5ad78bb264 | -7.20057 | -43.12354 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0135371a-2553-3aff-9b6f-3c473107b2aa | -7.01459 | -44.33854 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17750860-db88-3389-9ee7-e3cf4462ee19 | -5.91476 | -45.57675 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4ac7732-e414-3567-9210-a404e7fc6b27 | -6.26944 | -42.37454 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 208ebd22-dcba-3897-af4b-aa4e720a61b2 | -6.99228 | -44.45165 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06989140-e6ab-3c0e-855c-52bcac8c4195 | -6.98692 | -44.45948 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 873d261f-f9ec-346b-b653-5308373fd9c0 | -5.23423 | -46.75154 | 2025-07-11 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf85f811-9b4e-32bf-8f79-c115c7ac2a89 | -6.72784 | -44.3379 | 2025-07-11 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6db88dc9-a0dc-3133-80b2-b61391fcec84 | -6.31224 | -43.31194 | 2025-07-11 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 282d7b26-50ed-3b0a-9135-d03d869237e0 | -6.26889 | -42.37801 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1c9255e6-7dcd-3375-9a56-9c651583cc3c | -6.98818 | -44.45164 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cfdee8c-743b-3b36-83b1-47a68d0604a2 | -6.14509 | -45.89641 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48b02cd5-f596-3587-915d-e7378f1afd69 | -6.69405 | -43.92141 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d69a3ec-4a3f-32e2-9100-6964c3c3a8f3 | -5.75107 | -40.44512 | 2025-07-11 04:06:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c33c72c-0a5c-39c9-9365-296b7a9af3e4 | -6.97987 | -44.45844 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a45e1d7-d780-3df8-90a7-c38438a397a9 | -7.195 | -43.11532 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5689b671-a596-3fe2-a483-6d1a9a41e09a | -6.27 | -42.37107 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87e4c0b8-eadc-3a30-8586-be25c225bcc9 | -6.99233 | -44.44829 | 2025-07-11 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f45a88f-a473-376f-ac8b-e7c83b4adcba | -6.85473 | -42.79548 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d9d8420-0089-3e15-8c8b-10e935f82382 | -6.30825 | -43.3151 | 2025-07-11 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30dca749-afc9-3d16-9a64-e9f59799bb2a | -6.85027 | -42.80198 | 2025-07-11 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d53e272-862b-3945-893f-fdcf40a960de | -7.07849 | -43.41079 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1a7e213-1edb-33f9-a04d-d4cc72956216 | -6.27387 | -42.36811 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b195a6a8-4d9f-3c42-85b1-bbf5c026c723 | -6.88545 | -44.06056 | 2025-07-11 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 517807d1-c546-3600-9977-ad0e980ce585 | -6.14972 | -45.89227 | 2025-07-11 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54b02655-b19d-39d6-bfce-07b78f45c67b | -6.9615 | -42.72218 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7215c121-0ec4-3e52-84d3-078f9063b24a | -3.21957 | -42.12999 | 2025-07-11 04:06:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6a97f9d-77c7-3daa-abf4-a01926d3635e | -4.54658 | -48.00789 | 2025-07-11 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1bddcf39-d0f7-363e-9498-9affc711c122 | -6.29188 | -44.23342 | 2025-07-11 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de0ba56-27b0-3742-ac79-f2329625c396 | -8.67334 | -49.95012 | 2025-07-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8375a5a1-adf6-3832-a87d-a32e8145e00f | -8.22402 | -44.91831 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 063d684e-e63a-3c15-90a0-8d9a78d2cc1c | -7.33114 | -44.3249 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffb83a5b-bce5-33ae-982b-c0fe3b712640 | -9.35044 | -48.17551 | 2025-07-11 04:08:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d3926c3-3cb8-3048-bc65-e1fa6b1c5aed | -13.151 | -47.27108 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6434a98b-aedd-38c0-8590-84cecdddb161 | -11.44265 | -45.12088 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17c12ae9-f86f-3b55-a7cf-bf9d5af8440f | -10.84868 | -49.12287 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dcb0fcbc-7ba0-32de-b6bc-c9463b2843cf | -7.95158 | -49.65984 | 2025-07-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a65bd10e-f045-3bc7-bbfe-ce2a329a66ab | -12.40256 | -45.35791 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92f0838-a45c-3a75-b019-1affda942e97 | -9.61832 | -49.01814 | 2025-07-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9b83de26-1605-3f98-9e90-6507cb1f2c10 | -8.21692 | -44.91719 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b22add6-f1fd-37f3-aa4f-cce9c6be5cbe | -13.01245 | -46.27755 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acc9949d-5bfa-3101-afd2-e14edba339e3 | -9.61752 | -49.02264 | 2025-07-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5b874a5-3d19-38a7-9134-262b40b9ffb2 | -7.27245 | -49.57564 | 2025-07-11 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9f680b7-e9f9-3a4d-bac8-e3befa525d61 | -12.41606 | -43.49023 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 098cad73-4fb0-3359-a0cc-200f701c28f5 | -14.13451 | -41.69137 | 2025-07-11 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 178ddd76-9a57-33fe-89d7-058de71bf074 | -7.33052 | -44.32873 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3187d2c2-2e5c-3666-a489-09087882bde4 | -9.61308 | -49.02177 | 2025-07-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2678ea95-96b9-317f-a24a-974b81aaa6d1 | -12.9902 | -44.86273 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa3dabb6-5af3-3648-9c05-88cd48750545 | -10.57555 | -49.13094 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1af611a-f986-33c5-a13e-4d7127bf5935 | -11.90751 | -44.89537 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd0970d0-1a30-32a4-9beb-da41bb2e9e1d | -14.39328 | -43.76947 | 2025-07-11 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15498187-8d6e-331f-afb0-e18e96505bd9 | -13.00286 | -47.83081 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 014a3556-468f-3dbd-b4be-99ad64a35c00 | -10.67925 | -49.49339 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 90676348-cd81-3fa8-bccf-942e3acf4a37 | -13.15928 | -47.26816 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c163946b-f8e0-36fa-8a55-bfeeaaa0f46f | -11.32528 | -45.21774 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
