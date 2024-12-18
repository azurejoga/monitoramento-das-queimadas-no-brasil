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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4492a28-d83f-3c12-94e2-8d81eb4a2261 | -6.9692 | -43.577999 | 2024-12-18 00:23:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8ea8268-45c0-354b-a3c7-ea121752d82a | -9.2815 | -40.206299 | 2024-12-18 00:23:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b09c3461-5446-3eec-971e-5bf4fa624109 | -3.8761 | -47.0271 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2696bdba-761a-3eb7-8cfa-e771a4192887 | -21.358801 | -48.612801 | 2024-12-18 00:23:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f37af3fd-2cae-3fdc-b3f4-8a4f76bb1f18 | -21.0711 | -48.758301 | 2024-12-18 00:23:00 | METOP-B | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27259eee-ddd3-3bca-b99b-76b9ebf80f4e | -20.728701 | -54.3867 | 2024-12-18 00:23:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 39497c33-ebf9-3216-9583-f434640e9f53 | -6.9641 | -43.556198 | 2024-12-18 00:23:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc94c916-f079-3a8b-9e79-1ea5f52bee54 | -4.9546 | -43.7239 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8f142ee-eed8-3472-a2fa-2901c6c7fa38 | -4.9741 | -43.719398 | 2024-12-18 00:23:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9e6e192-60bf-371f-93dd-843fd9f786e2 | -4.7976 | -44.019501 | 2024-12-18 00:23:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3235a281-624d-3107-93c7-ce7df2f7f883 | -6.9764 | -43.5648 | 2024-12-18 00:23:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 104fed1d-181d-3c1e-903b-2bb5b30c75e5 | -20.7318 | -54.4053 | 2024-12-18 00:23:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6f885c6a-45b8-323f-a172-0356f56dc7f7 | -19.0723 | -52.8507 | 2024-12-18 00:23:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2a92f106-85b6-38b7-892d-abf1110736f6 | -4.04 | -47.022598 | 2024-12-18 00:23:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a28725f8-84e3-390a-996b-5ecd142807b0 | -3.7767 | -47.1829 | 2024-12-18 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| aff6c055-64d7-356b-88fa-76cdcd630959 | -3.46009 | -45.38297 | 2024-12-18 00:24:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2436a86a-ed8a-3c78-a6e1-08c23410a423 | -2.92346 | -41.46497 | 2024-12-18 00:24:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c365e075-f79c-3973-8267-5af67a611720 | -2.28835 | -45.50099 | 2024-12-18 00:24:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 966edb0a-e04d-32db-ac19-60106e00d489 | -3.24978 | -42.41366 | 2024-12-18 00:24:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8a513967-ee90-3347-a12a-c194eab359fb | -3.01943 | -45.23822 | 2024-12-18 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 94004539-6424-3b51-a5e7-3fbb60b1f82a | -2.03956 | -45.81937 | 2024-12-18 00:24:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 054fbee1-2b70-311e-88e1-872ae0b3af79 | -3.87349 | -47.03912 | 2024-12-18 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| fbadad0f-2ba7-3710-b865-2c60ad64f3c4 | -1.98028 | -46.54372 | 2024-12-18 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7d15c7c3-2196-3132-a1e9-f8b77acca32e | -1.63261 | -45.84725 | 2024-12-18 00:24:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d239affe-770b-3149-887c-ece1e51301f6 | -3.86587 | -47.03461 | 2024-12-18 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9b72192d-0547-34c9-9eab-fd4a52303dde | -2.63665 | -45.72174 | 2024-12-18 00:24:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2c149fc9-7edf-3e50-a77d-e3f9887b1675 | -1.62377 | -45.86159 | 2024-12-18 00:24:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e3b9adb1-2103-387a-bb19-4c33bb700cff | -2.14292 | -46.47338 | 2024-12-18 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93537531-1732-3717-bd2d-65c530fe504c | -2.14093 | -46.45845 | 2024-12-18 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5b5687de-7870-3010-bf11-8b930bc31408 | -2.2527 | -45.60187 | 2024-12-18 00:24:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 5151a81e-d0e1-3b86-a373-001047cc3e7b | -1.70603 | -45.79169 | 2024-12-18 00:24:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ccee60b9-1127-3afa-a84b-fa0037ebd2ba | -3.25102 | -42.42268 | 2024-12-18 00:24:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 217484bc-cc6a-3dfe-b0aa-b307d2720ae4 | -2.92844 | -45.24456 | 2024-12-18 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 753b67b2-8724-3dc8-a6a6-45693c826ee3 | -1.63438 | -45.86013 | 2024-12-18 00:24:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0ba2d81d-1499-3178-9a83-ab1f00619686 | -3.87113 | -47.02198 | 2024-12-18 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| eb9597a9-858e-38de-b26a-c5ca81e21ed7 | -3.02978 | -45.23678 | 2024-12-18 00:24:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 7fcd0e82-dd9b-34ab-97fa-4aa6be8c7c74 | -2.79606 | -46.71767 | 2024-12-18 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 18f51b13-9e6c-336c-899c-2db0c7e13d34 | -2.73875 | -45.87714 | 2024-12-18 00:24:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 995e18a9-57ad-3c93-8327-67f5b81aca10 | -1.70429 | -45.77893 | 2024-12-18 00:24:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 198.6 |
| 8e098d4b-deb6-3e36-8ca0-a3f1fec6700f | -2.20044 | -45.73215 | 2024-12-18 00:24:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1b6ee3ee-d8ac-369c-871c-203c13880c49 | -2.9301 | -45.25682 | 2024-12-18 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 117e3a3c-afcd-3a09-b232-f67f220e85aa | -1.62202 | -45.84872 | 2024-12-18 00:24:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e0cda527-f4d4-3249-bf26-df3d0c2ad744 | -1.98156 | -46.55285 | 2024-12-18 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3502415e-8002-3b0e-a614-b040c9c01048 | -3.23596 | -43.11318 | 2024-12-18 00:24:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9df47542-b87b-3ed7-b471-ee7e65b61f2c | -3.45831 | -45.37019 | 2024-12-18 00:24:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 63e257eb-be86-3828-9606-1e06e6bc2b71 | -2.73693 | -45.86373 | 2024-12-18 00:24:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be87893f-8560-31ee-8ebf-4d25b3c148d5 | -2.14131 | -46.46438 | 2024-12-18 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 43749a14-5e7c-3594-9fdb-464f3b6c6c4e | -2.78055 | -45.94049 | 2024-12-18 00:24:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d9ced0da-81cb-3897-8dcf-13cfb0f71dd0 | -1.9134 | -54.2229 | 2024-12-18 00:27:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a68b73-798e-3d38-a683-01bbcbc3ded3 | -4.1064 | -46.7285 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 852f9f21-f3fa-3d30-8435-207894733058 | -3.1539 | -53.152 | 2024-12-18 00:27:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e70d374c-c368-3dd2-8215-75fa06eb012b | -1.6198 | -45.8507 | 2024-12-18 00:27:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7674536-740c-3c1b-8caf-9d7a9a43badb | -3.0173 | -51.847401 | 2024-12-18 00:27:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485315a0-7985-3e8a-9684-ca16227279fd | -4.004 | -43.750401 | 2024-12-18 00:27:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9516581-eb93-37d2-9639-0924d4468b9a | -2.9188 | -45.2351 | 2024-12-18 00:27:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b32a51f2-e769-3c2d-84a1-ab934674bb0c | -2.7926 | -46.704201 | 2024-12-18 00:27:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4cdd907-8a56-3926-98fa-a109fc633753 | -4.1325 | -46.797199 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94079881-4203-3b2b-99b1-089423fd6f1b | -3.0156 | -51.839901 | 2024-12-18 00:27:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea2b261-f532-3edb-a47b-5391dbd8664e | -2.2514 | -45.599201 | 2024-12-18 00:27:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 793bf4f9-d7e4-353c-8cd7-23227f2869ba | -4.1046 | -46.7206 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21856e8a-42e2-3775-9d42-e9ef6a51b479 | -1.9177 | -54.241798 | 2024-12-18 00:27:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17f4f6e-8ce1-358c-be0b-0e46f989025d | -3.5024 | -53.9366 | 2024-12-18 00:27:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b070b0c4-32ef-3f62-b911-e20ec0c7f40c | -4.7135 | -44.895599 | 2024-12-18 00:27:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5c78c5-62f1-3e49-9b77-db3d23d5a943 | -1.6219 | -45.860001 | 2024-12-18 00:27:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5a79dbf-87f4-3b2e-b95b-38312e52192c | -3.0615 | -40.062599 | 2024-12-18 00:27:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 21cac345-f9b2-30c8-987e-36f4f4f1eb37 | -4.1361 | -46.812901 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89ae00e3-5919-3f6b-b1ec-ab2840a3a1d8 | -1.9841 | -46.544899 | 2024-12-18 00:27:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24321ded-b0c8-310f-80ce-bfe21b160626 | -3.4725 | -53.291401 | 2024-12-18 00:27:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f66e990c-c3a1-3bb6-b2e3-fef510a60449 | -1.7068 | -45.7817 | 2024-12-18 00:27:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6034e7ae-e8b0-38e5-a2a2-10275f759353 | -4.1143 | -43.562599 | 2024-12-18 00:27:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcff1191-d574-3983-b228-392aa3489ae0 | -4.1343 | -46.805 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4bab7b9-2e75-3702-b651-5efc19e9a13f | -2.2492 | -45.589699 | 2024-12-18 00:27:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb911c79-7f48-38b4-8af1-075f7f42da73 | -4.2937 | -43.889702 | 2024-12-18 00:27:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0dc10da-95fc-3b56-8bd1-e0ce5e3171fd | -4.1028 | -46.7127 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7a5977-76c0-3131-9ccb-ecd50800f154 | -2.6367 | -45.709 | 2024-12-18 00:27:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae9ee566-4581-3bf8-a068-e8bffaad58ff | -1.6949 | -45.774502 | 2024-12-18 00:27:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a55631ff-9f59-37fa-904f-f5a9aeb244e0 | -2.6904 | -51.9035 | 2024-12-18 00:27:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd9113a-42b6-3a5e-8d4c-9d4d6816db32 | -4.1115 | -43.550598 | 2024-12-18 00:27:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb0aa67a-bb98-36ea-a3cc-9b177fc87177 | -1.6176 | -45.841301 | 2024-12-18 00:27:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2effc24f-12c7-338d-bf1d-f77f53a99ccd | -4.1463 | -43.567799 | 2024-12-18 00:27:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f5721a1-31ab-389e-b68b-722abb89d447 | -4.0966 | -46.730701 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 260892ba-2572-3930-ba10-b9401e9c28ca | -1.6295 | -45.848499 | 2024-12-18 00:27:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0248bd67-f55c-3873-8c65-2b7b1f3181cf | -1.7047 | -45.772301 | 2024-12-18 00:27:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da3dae96-8b4c-3d77-8aff-33a8ad1356ee | -2.7028 | -51.6376 | 2024-12-18 00:27:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddc6b748-9848-3290-9408-59e7abacefa3 | -3.3 | -53.347401 | 2024-12-18 00:27:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4f651c-5fc9-3d37-9c92-c7ab3658ac95 | -4.7113 | -44.885899 | 2024-12-18 00:27:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f01a59a5-e691-3b50-9bf1-71b8dacdd3f0 | -2.7945 | -46.712399 | 2024-12-18 00:27:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1eda226-a017-3664-bf75-0af65b1b3b0c | -0.7452 | -47.753201 | 2024-12-18 00:27:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974c6343-ef38-3e5b-ab90-1ba2d2f6efe3 | -4.0948 | -46.722801 | 2024-12-18 00:27:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a71ba66-b05b-3fb2-9e53-382c9c3c78ef | -3.3019 | -53.356201 | 2024-12-18 00:27:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11d8336-c897-37a6-a5ba-b6615c78c078 | -1.697 | -45.783901 | 2024-12-18 00:27:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b36efa85-d31c-3145-be7c-4e40a02f00a1 | -4.4588 | -44.6413 | 2024-12-18 00:27:00 | METOP-B | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4767a172-c7f0-35a2-b177-4a9056bb06fe | -2.921 | -45.2449 | 2024-12-18 00:27:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95e480b0-a9bc-394d-8e76-6f581c626d6a | -4.1435 | -43.555801 | 2024-12-18 00:27:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9d19293-505b-3117-8c78-1ffee545525c | -0.755 | -47.750999 | 2024-12-18 00:27:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba7bcfbc-1313-3d69-a20b-b223f8661891 | -2.7332 | -45.860401 | 2024-12-18 00:27:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 619dd09c-cb19-30db-8f1e-6dbe2e547144 | -1.9156 | -54.232399 | 2024-12-18 00:27:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 447117a9-7160-3be5-9de2-2c89c6794bff | -1.5696 | -46.0368 | 2024-12-18 00:27:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8104f96-37cc-335d-8a1e-f27d1b1b9194 | -3.2374 | -42.407299 | 2024-12-18 00:27:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4dde271-217d-39d8-8280-0a80fc20b12e | -3.5045 | -53.946098 | 2024-12-18 00:27:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
