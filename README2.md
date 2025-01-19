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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdd9aa68-2d38-393a-a1bd-4e51fbd65421 | 4.5177 | -60.6982 | 2025-01-19 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 47b8a8be-bd27-3a16-bd30-78084825b942 | 4.4993 | -60.6987 | 2025-01-19 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| aaf5ede1-5f62-3910-a1f6-57d41c9dc37e | 4.5176 | -60.7172 | 2025-01-19 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5030b312-5e2c-3493-956f-d636a0c33473 | 3.27069 | -59.95315 | 2025-01-19 02:00:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8c868766-7586-3177-8a1b-99f17574e697 | 4.49944 | -60.71409 | 2025-01-19 02:00:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 131.6 |
| fe2127a2-7953-3f57-a34a-3e86aa6f61cd | 4.51494 | -60.69818 | 2025-01-19 02:00:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 22.1 |
| eb161bcf-d452-38b8-9241-39695f9a8000 | 3.28023 | -59.93644 | 2025-01-19 02:00:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7d16e213-71a2-3a8d-8b52-dbd7b90248a8 | 3.27722 | -59.95966 | 2025-01-19 02:00:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 76a35ca0-8d35-331d-956d-9018aedb4605 | 3.12076 | -60.75899 | 2025-01-19 02:00:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 30.5 |
| ab3bf6ea-df6a-3fc0-b9e6-1300c813e63e | 3.11811 | -60.77868 | 2025-01-19 02:00:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 82a822b1-35f7-32cc-a0cb-cf28bb2bfe63 | 4.5125 | -60.71664 | 2025-01-19 02:00:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 9c77f9a4-e3dd-3748-98fa-7bd6d7046c37 | 4.5176 | -60.7172 | 2025-01-19 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3f4461fb-6e6c-38a3-9279-d60beef55075 | 4.4993 | -60.6987 | 2025-01-19 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 05bc0fe8-20cc-3cc8-a2a1-2fc5f1a1c1e9 | 4.5177 | -60.6982 | 2025-01-19 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6a7a1106-8011-3566-907b-8c80155e5dbb | 4.4993 | -60.7177 | 2025-01-19 02:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a75bc2b2-711d-3e6a-b2c9-f0c74522fa38 | 3.2759 | -59.9447 | 2025-01-19 02:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7c8b7d26-523d-37a9-b8e6-fa37e3d1a45d | 4.4993 | -60.7177 | 2025-01-19 02:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 55ff5641-51b0-3be3-afe8-a6cebed242b4 | -17.797 | -40.1431 | 2025-01-19 02:20:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 50c837bb-90a8-3b0a-98e6-7a67d38404aa | -19.13437 | -40.40936 | 2025-01-19 03:12:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 87225d06-d498-325b-aea3-13d2f23fd5d6 | -22.90331 | -43.75463 | 2025-01-19 03:14:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d37aa2dc-10b8-3079-baef-a5eddf208822 | -22.89722 | -43.75288 | 2025-01-19 03:14:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 02224b35-1f34-3233-922e-7243b5baed29 | -6.446 | -35.1484 | 2025-01-19 03:30:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| aa741321-aa02-30c6-9669-ccc21c01d5f9 | -6.446 | -35.1484 | 2025-01-19 03:40:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 5f7461c4-ce1c-3beb-8132-c2d3b0f982c5 | 4.5177 | -60.6982 | 2025-01-19 03:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ab9bdba5-6cbf-3f26-bddd-d34e368f35f7 | -4.65224 | -37.91281 | 2025-01-19 03:59:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd4557a5-50c4-3f13-af9e-c546e12ed888 | -5.65142 | -35.83265 | 2025-01-19 03:59:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52588690-da92-32e4-a7fd-5fca3cdb2ae9 | 4.5177 | -60.6982 | 2025-01-19 04:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7762ea98-9fc8-3571-826e-1f65335371ae | -6.45273 | -35.15248 | 2025-01-19 04:01:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7d7fabe6-c07e-3b49-b329-9ad0e939bd9c | -10.69677 | -37.04815 | 2025-01-19 04:01:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 700b91a5-6165-3505-afe6-7274731c35cb | -6.45348 | -35.14739 | 2025-01-19 04:01:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f9326f48-f232-34f2-94ca-2a769ed17600 | -11.03354 | -45.04846 | 2025-01-19 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b43bfb6-3763-350e-8135-4951399938a6 | -9.59324 | -35.80904 | 2025-01-19 04:01:00 | NOAA-21 | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4d4179e2-e5ba-3e6c-a32e-428912815801 | -8.22628 | -35.24386 | 2025-01-19 04:01:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87e21d77-b9c2-3164-9c42-14a766fc3638 | -9.36626 | -43.28717 | 2025-01-19 04:01:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b17c966-ebdd-3bbb-a2f5-3424cc60ab6e | -11.03352 | -45.05099 | 2025-01-19 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 01fdd942-143c-3868-a5a3-1bf4851c989b | -11.02978 | -45.04774 | 2025-01-19 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d8f8230-7ba5-32ed-8426-4a8b1db9f0af | -8.2268 | -35.24014 | 2025-01-19 04:01:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad19da7a-147e-31f4-bc1e-163ce275a001 | -11.03276 | -45.05312 | 2025-01-19 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db3893b6-705b-3ef5-9d8c-a1a139351f21 | -19.13556 | -40.40486 | 2025-01-19 04:04:00 | NOAA-21 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 20da4f46-5d63-3c40-b29b-133556b7fba7 | -20.41795 | -43.55334 | 2025-01-19 04:04:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 333005ad-6362-32d2-bb08-e73e0682b31f | -16.83033 | -42.86993 | 2025-01-19 04:04:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52a019dc-9e28-31f1-a057-f360e606e022 | -16.3504 | -43.69525 | 2025-01-19 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d776ab03-89a7-3016-91ea-aebb673af1e6 | -18.04023 | -39.92461 | 2025-01-19 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 779cd994-8016-3674-8883-e6247660bfdc | -20.34826 | -40.36276 | 2025-01-19 04:04:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 830cb91a-2cf4-36ff-b676-79f87ada171b | -19.13498 | -40.4089 | 2025-01-19 04:04:00 | NOAA-21 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e963211a-9bee-330e-8903-36a82765255a | -17.17492 | -45.46592 | 2025-01-19 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86a15c45-5054-3814-8ca4-cf3ec5eded85 | -17.17137 | -45.46528 | 2025-01-19 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6b3cc61-0ea5-3afe-b239-45f7aca762fc | -19.71737 | -40.35254 | 2025-01-19 04:04:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1fa7f8d4-2429-3f2c-97dd-1ad2ec127ea7 | -17.75574 | -42.89449 | 2025-01-19 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8923e329-eec6-368a-855e-635d478a8024 | -15.08115 | -48.94674 | 2025-01-19 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28f5bca-73b9-3c93-a395-3a3c55a95869 | -15.56827 | -47.85485 | 2025-01-19 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f97e0cbe-36c2-3c43-973a-90e3e1f963a1 | -17.09539 | -43.8052 | 2025-01-19 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfa7a0d2-11ea-3922-b6ed-b8e82f4d1a74 | -17.16781 | -45.46463 | 2025-01-19 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83488b7f-ddf4-39ff-b1ba-edbdd3037b61 | -17.00735 | -49.78267 | 2025-01-19 04:04:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bcf266a-561e-39ca-9dbb-4241c93d6faf | -16.45542 | -50.05127 | 2025-01-19 04:04:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3c521fb-a031-3939-9593-aeffff012144 | -19.92647 | -44.09166 | 2025-01-19 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6dc68e7-cc5d-3c26-9a81-a30d03a1752d | -19.92708 | -44.08795 | 2025-01-19 04:04:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8356f75f-eeb4-3f7e-8b48-5218275cf3f2 | -23.98539 | -48.91745 | 2025-01-19 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ee398c8-56f0-312f-a1dd-00068e74b9c2 | -21.62572 | -43.46761 | 2025-01-19 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 789eeaee-b435-3270-a77a-6a37c5917634 | -21.18063 | -43.98042 | 2025-01-19 04:06:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3de1903a-d5db-3f52-bd50-75c44d49e69f | -20.32453 | -47.73611 | 2025-01-19 04:06:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0622f823-5dce-358a-94fa-5ee47c4b6e87 | -20.76564 | -46.77106 | 2025-01-19 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff7119a7-3fbf-3310-b701-3343ea28d02c | -21.18117 | -44.27464 | 2025-01-19 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05fd13c3-c7fc-3e3a-9b2f-134659a2ae8d | -21.54832 | -47.96461 | 2025-01-19 04:06:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85ba36fc-eb3e-3957-b3a8-d251c790e0eb | -20.89985 | -43.82015 | 2025-01-19 04:06:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5240c98b-a7db-31c3-b221-1496e527ebcd | -20.32548 | -47.73093 | 2025-01-19 04:06:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fad5426d-e021-338c-b90b-0dd5dd339880 | -23.70492 | -46.36784 | 2025-01-19 04:06:00 | NOAA-21 | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| edee3d27-40ee-3621-ab10-c47c23325422 | -21.19606 | -44.93825 | 2025-01-19 04:06:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6225beed-eeb1-32fa-8b10-1f2e4185601c | -20.65684 | -49.99186 | 2025-01-19 04:06:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad5fee5-f3ac-3e93-8cb6-e463331d410b | -26.32059 | -52.26286 | 2025-01-19 04:08:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b81c96bf-bde7-320a-9ad3-40c31fa916b1 | -27.26546 | -49.8713 | 2025-01-19 04:08:00 | NOAA-21 | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66652193-5b09-36f8-b3e7-d638d17e1545 | -26.32163 | -52.25798 | 2025-01-19 04:08:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2423e188-4946-309b-abf4-8a286ef0b6e4 | -27.38381 | -51.50956 | 2025-01-19 04:08:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6bf10e5-377a-37dd-aaac-43f534501323 | -11.03326 | -45.04816 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1f610d2-fd7e-32d5-bebb-d11e614946e0 | -11.03301 | -45.04937 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9056d036-6e14-39fd-a9f0-57ae418d11d1 | -11.02916 | -45.0516 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 624ec5e5-a194-395b-8dd4-15bc6f346143 | -11.0336 | -45.04543 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f0cb933-2517-35f7-b3da-0b8148bc9681 | -11.03268 | -45.0521 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 319795e9-0232-3d35-aa16-8e801a9059a3 | -11.02949 | -45.04887 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fa9df9-417f-34e2-beaf-c23dda6cc75a | -11.02974 | -45.04766 | 2025-01-19 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d93c1ef-be35-30a1-9b3b-677a3d02c302 | -20.30972 | -45.58284 | 2025-01-19 04:29:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0337aa75-455d-3de8-86f1-e2acb628bbfb | -16.45491 | -50.05367 | 2025-01-19 04:29:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2e04c2c-f680-38e0-85fd-830c404c5fa7 | -19.13565 | -40.40504 | 2025-01-19 04:29:00 | NPP-375D | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f60b6c8e-6284-3539-836a-0f978f9ae1d5 | -18.9976 | -52.3924 | 2025-01-19 04:29:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b75d67b-5e63-3aa9-af2e-51ca67ce8ab9 | -20.32504 | -47.73354 | 2025-01-19 04:29:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a999edb-a76a-37b4-8e94-e8126772482b | -18.99686 | -52.39668 | 2025-01-19 04:29:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aa80e04-1003-368f-b668-13420a96ec0c | -17.09389 | -43.8049 | 2025-01-19 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 035a6496-2847-3eb4-a429-29ea7af45854 | -21.19349 | -44.93636 | 2025-01-19 04:29:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24a4ea55-309e-3242-9d91-c74ebc89bb06 | -15.26573 | -51.4778 | 2025-01-19 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83520fff-5d69-3103-8376-7815ac15a0fa | -17.87968 | -40.11468 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a60b92a4-9e82-3cee-b55f-36490367b526 | -17.88527 | -40.112 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08729e3e-71ee-3ae2-a8d5-c7e6ee926526 | -16.83065 | -42.86796 | 2025-01-19 04:29:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d096f804-5612-3795-a2da-c89b58e0f7e6 | -19.97002 | -44.21644 | 2025-01-19 04:29:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc296d37-f5fb-329f-a06f-dcc7e63782cc | -20.6576 | -49.99021 | 2025-01-19 04:29:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 378fa359-8d60-3074-bf78-09f340578b7e | -20.65701 | -49.99391 | 2025-01-19 04:29:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 955c4799-04c8-3955-a648-eb4a7da2fd34 | -19.13531 | -40.40828 | 2025-01-19 04:29:00 | NPP-375D | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| afbc2998-47a4-3aa3-9ba2-34f828973714 | -17.88006 | -40.11139 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cfb93878-e927-3fda-b381-81c909be27ad | -20.41475 | -43.5524 | 2025-01-19 04:29:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1af99aa5-defa-3c3c-975c-6c94abd90c8e | -17.88535 | -40.11163 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5127629c-7f1c-3789-b9bc-d7a1fe46d1ae | -17.885 | -40.11489 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
