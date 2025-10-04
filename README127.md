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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ed990e4-faf5-36a1-84e9-adacc8be9045 | -9.33986 | -45.79492 | 2025-10-04 05:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fbc394ca-af33-354f-8f0f-33ff40d8e92c | -7.04439 | -42.77628 | 2025-10-04 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e948be8c-001c-3d60-8ea8-134c7d66090d | -4.44392 | -43.23148 | 2025-10-04 05:33:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2d635304-7dac-3123-858d-63cc430205ad | -6.17458 | -43.91788 | 2025-10-04 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3eb13095-a566-3a74-960f-e9354bc91b25 | -6.06837 | -42.51749 | 2025-10-04 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| a60ca015-c51c-3912-9e87-acc68fb4992d | -5.87544 | -42.52076 | 2025-10-04 05:33:00 | AQUA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 06d983a6-909c-329a-ae26-7a348ff2616c | -6.37441 | -43.88807 | 2025-10-04 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4834bbd9-9b65-34d3-ae35-661c9f7d7fbb | -7.00851 | -42.30107 | 2025-10-04 05:33:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dfc463fa-eeda-3c97-a260-b85363844588 | -5.81981 | -42.886 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3207c065-24f2-3a2f-9e05-08dd640b747b | -9.10902 | -44.39316 | 2025-10-04 05:33:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 48139c28-75a5-3001-b871-755fb688b08a | -6.88464 | -47.22851 | 2025-10-04 05:33:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1a11b466-05c0-33ef-ae77-45d0bbabde22 | -6.36527 | -42.88042 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c648ac77-574c-3721-9b11-641910be8985 | -7.74248 | -42.51776 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| fcac2a9d-385a-3461-a2e7-95d38e111afc | -6.07765 | -42.51891 | 2025-10-04 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 81cbbb7a-5ede-3e3b-b6a3-d6eadf831a07 | -6.88138 | -47.23534 | 2025-10-04 05:33:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8a36a232-f5ba-3287-a531-f286d8f7a4c3 | -6.18578 | -43.58762 | 2025-10-04 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1578e6cf-169a-353f-a7bd-fbdf4a4d757c | -6.0792 | -42.50903 | 2025-10-04 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 7644d530-965c-36a5-b62a-cc1075b3e939 | -5.88176 | -42.52752 | 2025-10-04 05:33:00 | AQUA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1343baaf-a2a3-318f-a9e0-d01d7a9bdd20 | -5.98675 | -43.4806 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1517e7f7-536c-3e2e-bf04-b06aefee5429 | -7.75162 | -42.51909 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 74e81091-9582-39aa-90bf-0d4f003d4037 | -5.83715 | -42.87312 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 79f63a10-fcd5-3a93-b825-0e206b8fb38c | -7.3741 | -39.20256 | 2025-10-04 05:33:00 | AQUA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 25370916-93d6-32ce-b987-78ee367f1abc | -7.04282 | -42.78624 | 2025-10-04 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9fe462d1-9c6b-333c-a40b-1d6bf8c6da4f | -4.8275 | -42.75856 | 2025-10-04 05:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64c56ba0-bfb1-3f78-9379-cfff1cb28f6d | -4.82333 | -42.76183 | 2025-10-04 05:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c7cf8ac0-75ea-3a49-bf56-8dabfaea18f5 | -8.85166 | -46.7927 | 2025-10-04 05:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 050b97ed-3dc6-3ae6-955f-4c8640b5ca99 | -5.67452 | -42.73088 | 2025-10-04 05:33:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 69f89f1f-3d8e-39ad-9736-12d72e706998 | -5.6869 | -42.83791 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0a1f9170-d0b9-330d-a139-ca90423d3ccc | -6.87305 | -44.49632 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3465176f-0900-34f3-9376-d546f255dc41 | -5.98501 | -43.49193 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bc8617c9-be4e-3652-bcb8-954f0777aae0 | -6.86845 | -47.23304 | 2025-10-04 05:33:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c790d49b-2a2a-3990-9c0a-754ed6abdeca | -6.46285 | -44.57172 | 2025-10-04 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 499dc755-ef28-3a68-b526-adf9cc215fc3 | -6.27323 | -42.45021 | 2025-10-04 05:33:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 5018458e-9ac0-369d-a8a3-74f1ee183f07 | -8.05801 | -44.793 | 2025-10-04 05:33:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 93349b05-006b-3fa6-9110-0c106671f39f | -6.86843 | -47.24646 | 2025-10-04 05:33:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4d389ed5-d171-366b-94ac-a87f0f0f72ac | -7.0537 | -42.7777 | 2025-10-04 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 9d595ffa-1200-386c-801e-7ec03b7230ad | -4.61206 | -43.14348 | 2025-10-04 05:33:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 6246b26a-cf5a-3af7-8b34-261fbe2d6122 | -5.87694 | -42.51095 | 2025-10-04 05:33:00 | AQUA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| bf2fa23b-39bc-3f3c-a02c-6a627b3e8916 | -7.80347 | -42.54655 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 566cc4d5-9437-31ef-a677-621983f57bc3 | -6.43902 | -44.44993 | 2025-10-04 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fa57d437-f9d4-3cf4-80c0-cbc80e1cc84a | -5.78484 | -42.9235 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 20fea973-de4b-3022-99f7-443a5efb5201 | -4.44218 | -43.24277 | 2025-10-04 05:33:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 226.6 |
| a256d1b4-d80a-3d41-ac5e-c88a0ec44df7 | -4.62188 | -43.14493 | 2025-10-04 05:33:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8eccf4ff-f988-306c-aac4-d0d4f3f24913 | -7.37272 | -39.21186 | 2025-10-04 05:33:00 | AQUA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 37b270ac-aa8b-31c3-a4dd-34b77923a98d | -6.64503 | -42.80632 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 5fee1035-0161-34f6-af13-e5d984ee5741 | -5.19697 | -45.0757 | 2025-10-04 05:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4e382d82-b34c-314d-8f74-6adb31436fb2 | -5.20004 | -45.05264 | 2025-10-04 05:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a54052a3-0ad6-38d9-b93d-67eaacd51b78 | -6.3709 | -44.30255 | 2025-10-04 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9daec2bb-b106-3f0c-bcc0-ab2fbd5ee739 | -7.54923 | -42.3918 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f7940c85-d576-3839-9219-94570ce40870 | -5.48907 | -44.10393 | 2025-10-04 05:33:00 | AQUA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d67fa692-444c-31c6-a2bf-d49e155d8e14 | -9.33997 | -45.78811 | 2025-10-04 05:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 1cbc46bf-4c1a-3fb8-a1c4-cfc8b2dab239 | -6.66808 | -42.81652 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5e07fd2f-526e-3deb-bfea-0800807453ff | -5.82602 | -42.88203 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1791bad8-3098-30ff-9952-f19bb64c0639 | -5.83552 | -42.8835 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 11ba2483-6422-3993-ae07-85b9b20c1b09 | -6.05101 | -42.51921 | 2025-10-04 05:33:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 213d4ebf-4d76-3624-ad21-04a2093fabad | -4.95558 | -45.07097 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| a12ac87e-276e-3c32-a1ee-2a9b91ca876c | -9.3509 | -45.79663 | 2025-10-04 05:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d94b122c-841d-3b77-85da-9a6957fa4178 | -6.17014 | -47.24023 | 2025-10-04 05:33:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 7ac0ace4-07e5-3b2e-b915-5e2c9117e823 | -9.11896 | -44.39496 | 2025-10-04 05:33:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b16d418-4159-3157-8de8-4c5cdaf5e7c9 | -5.54927 | -42.65765 | 2025-10-04 05:33:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 132eba2d-d1a7-3c3e-9001-1779c5856813 | -7.55833 | -42.39318 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 631e07ae-174c-3976-96c9-fe2b9b8842fe | -6.33978 | -43.45752 | 2025-10-04 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 718ce78d-1659-3f5f-b447-151178cc9122 | -5.80427 | -43.59763 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 57b49412-248e-3693-88ac-9807ad067b78 | -5.66151 | -42.71237 | 2025-10-04 05:33:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 44a8ce79-dfe3-366f-a6d7-930b0171a020 | -6.16663 | -47.26145 | 2025-10-04 05:33:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 267.9 |
| d2ef0ff1-88e9-3202-a89f-66a590bdc1c8 | -7.74098 | -42.52734 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f3cb5540-b962-338b-bd7c-abeb7e7ddee5 | -7.80639 | -42.52747 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 360ee917-eec7-391a-b3dc-af0dbaa30ff3 | -4.95792 | -45.05624 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e2261221-6ab0-3cd4-95c7-69ab676eb5e4 | -5.77694 | -42.91156 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3bf8609f-a6b6-371f-a918-f1910352225b | -6.65439 | -42.80781 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b758b9f3-4249-3717-80bf-3a83d139ac20 | -6.15844 | -44.61316 | 2025-10-04 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1b308b54-8ef6-3741-aa07-f226c112519a | -5.80352 | -43.60241 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 12445e43-0145-3f6c-aaf8-910e2cdb0ef7 | -8.84298 | -46.8451 | 2025-10-04 05:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| db0849a6-e01e-3552-bfd0-2005713b6882 | -5.47347 | -42.77193 | 2025-10-04 05:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1d28405f-a94f-37c9-b88b-4f87511f1f86 | -7.79139 | -42.56432 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5efc0601-66f9-3292-8825-9d8a45c94613 | -7.80493 | -42.53698 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| df54e476-754b-3a3b-af23-8e4191cedb25 | -6.36247 | -43.89853 | 2025-10-04 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 88aaab19-c71a-355d-88f0-9a4fa9514fba | -5.6964 | -42.83932 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3b6a589b-ceca-3347-9d72-e8d98a4b087f | -5.7372 | -42.91615 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 8b92f103-8b3d-3050-9837-1ed22b011b89 | -5.08236 | -44.08791 | 2025-10-04 05:33:00 | AQUA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b8592474-a05c-33b6-9c77-6a9dea9073bf | -4.61032 | -43.15462 | 2025-10-04 05:33:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7198d8f9-018b-3286-83d8-6c257942da5c | -6.09835 | -43.48118 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d781f295-46e3-3e27-94d6-a1157c231f44 | -6.34149 | -43.44658 | 2025-10-04 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1d9d903-e12d-33ec-8f1a-f12a23cc501e | -7.35162 | -44.34212 | 2025-10-04 05:33:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7d42ba0c-f246-3a03-9c44-ef388ca4512d | -7.78991 | -42.57393 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 430afb48-2054-3960-932c-cec39b40f109 | -5.77531 | -42.92205 | 2025-10-04 05:33:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| df83ec1d-917b-3abc-ad66-f594be07ad22 | -5.6667 | -42.71916 | 2025-10-04 05:33:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ae9300ef-41cc-3e73-a305-c8fa7d814591 | -6.06992 | -42.50759 | 2025-10-04 05:33:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 5a64f5ed-14fe-3cd6-95f1-6d8771ab8605 | -10.53639 | -44.5171 | 2025-10-04 05:33:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fd49967b-7f21-38c6-8feb-3034a88228be | -9.34229 | -45.7804 | 2025-10-04 05:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| de7582cf-c508-3263-be7b-b5317c82f721 | -6.66221 | -42.81935 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 1f70d603-1714-3e90-a658-3187ab242777 | -9.34567 | -54.51843 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dc6698f-d354-30d3-8a04-4efff62864b6 | -10.29663 | -50.2931 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e13b201-681c-3012-b664-2450cadbc4db | -8.62145 | -54.9805 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 966af949-6b83-347a-b4b1-709a8fd85b18 | -8.6222 | -54.9751 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 061381ab-534a-3885-b439-205f46e03540 | -13.33143 | -50.95498 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47444fdc-ff77-3c67-9f71-f1a0fd1ec259 | -12.36302 | -54.17323 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99e2d996-d5a8-3912-b93a-e4d6952c1317 | -9.19035 | -59.55052 | 2025-10-04 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cff3311c-0289-3397-9ab7-5a8eaacefddc | -14.58369 | -52.48935 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6553787-5fab-3110-97cf-f399460c30be | -16.07928 | -51.07127 | 2025-10-04 05:33:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README128.md)
