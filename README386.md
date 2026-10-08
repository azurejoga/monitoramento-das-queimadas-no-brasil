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

## Dados Diários - Página 386

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9622a6a7-48ed-3f80-8f15-7410f412e7ed | -11.7738 | -43.5482 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 310.0 |
| 3a59866f-3eed-39e5-9018-fed4b2ef507a | -2.7613 | -54.0941 | 2026-10-08 18:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 189.8 |
| bb67e6f7-bed6-3268-a797-79141df5a92d | -1.383 | -55.1944 | 2026-10-08 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e8b2b9c6-6d85-36dc-97db-debf076d426b | -11.4507 | -43.3854 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 295.5 |
| 8faff63e-6e35-3e73-9706-ae193063ad33 | -2.7797 | -54.0736 | 2026-10-08 18:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| e10d344e-4ac7-3a2a-8a8d-21704530c591 | -7.4886 | -42.8295 | 2026-10-08 18:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 96d6f27b-cfc1-35a2-8ffd-cd2ea7fa7181 | -2.9265 | -54.1104 | 2026-10-08 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 478c5ce2-c8d8-37d2-b501-1f9f2af957f1 | -6.9328 | -43.6799 | 2026-10-08 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 03d45b30-9d97-3117-9926-1a8e63f8628e | -15.6261 | -40.1386 | 2026-10-08 18:00:00 | GOES-19 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 151.8 |
| f5080bc9-faf0-3536-bc49-f9150932732d | -3.2634 | -57.8689 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 25e2dc00-cea7-3d15-a6d3-6da9b1e97f82 | -11.1145 | -44.0009 | 2026-10-08 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 1daba0ac-29ff-3091-aafa-1371f788fcdf | -1.2911 | -55.4133 | 2026-10-08 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bab768c9-de4d-328f-b5e8-f0f66dfb1e67 | -3.3912 | -58.0017 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2e2e90d3-8479-388f-89b1-b45e6434f862 | -15.0346 | -42.4941 | 2026-10-08 18:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 156.1 |
| 07a8aa21-7871-3442-85e6-44fc5347885a | -5.9647 | -40.9383 | 2026-10-08 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 253.0 |
| e54eb236-d95b-3b4d-8be5-1bf62dd9b4c6 | -2.8433 | -57.4891 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 1efab78b-db1c-321b-ac84-3e5a9a44ea25 | -3.1879 | -58.6433 | 2026-10-08 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 287.8 |
| 547d35cb-f65c-3b24-99e6-fd0ceb320757 | -2.4759 | -58.0771 | 2026-10-08 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fb1693c9-ae7f-352c-9c3d-7f2e06c95db3 | -5.3905 | -44.1968 | 2026-10-08 18:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 507c1753-07d0-36a1-b878-c3ef3cf3f9ae | -11.0758 | -44.0299 | 2026-10-08 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 5e031570-a127-336b-8a02-72f92f5c381b | -6.1617 | -52.6471 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 8f5e1d5a-bfe7-39f7-ac8c-5ad60bdfb217 | -2.853 | -54.1322 | 2026-10-08 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 7a55dacf-752e-3283-aeb3-afa7036d9419 | -2.572 | -56.1646 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| e9da9e35-c18b-35e2-b40b-84ff37e9a234 | -3.2451 | -57.8693 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| b599bb39-0b7d-33ce-abab-5d61347281ec | -3.3911 | -58.0405 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2ed9b3dd-c162-3049-8ae8-368aadef77ac | -11.7764 | -45.5265 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 32864fe2-ab56-3705-8696-2071187e7f12 | 1.7304 | -55.5863 | 2026-10-08 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 72ee53f1-ae1d-3948-ab95-bbbcac2ea229 | -11.755 | -43.5275 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 10fbe209-9b88-386d-9926-4f34fdf00778 | -5.4958 | -42.8413 | 2026-10-08 18:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 5bf32f47-7e98-3c94-b5da-60798fc3bb67 | -9.9787 | -43.502 | 2026-10-08 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| eee76fd3-f00f-399b-9b0c-99f89805c83d | -14.4345 | -43.9157 | 2026-10-08 18:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 3df373f1-76d7-3014-8b91-83b3ac294b0c | -2.4989 | -56.1069 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 69538e54-95c5-39a9-ba66-6aa7aff7be0c | -3.0192 | -53.887 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 069b4588-13d8-3143-bb5e-0162cbd3263d | -14.0472 | -43.8222 | 2026-10-08 18:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 521.0 |
| cb42b2a0-8c08-34fa-b830-0643ffe6fd0a | -6.6879 | -45.578 | 2026-10-08 18:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0603521e-67b8-3998-9198-9094e262b1e3 | -2.5903 | -56.1642 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 1e991053-75e5-3ec2-93d9-ada9ef8592ee | -9.0705 | -67.7225 | 2026-10-08 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| dc909042-1e44-30f3-b37e-b8925f664bbd | -5.6935 | -53.4464 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| cf126aa6-b8f4-33eb-bc41-4718b2add7cd | -9.9014 | -44.8147 | 2026-10-08 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 9af1145a-ea78-318b-adb7-2212d43ac8dc | -2.8873 | -54.9112 | 2026-10-08 18:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f2109ef3-668a-3338-9aba-84329d3683d4 | -2.8434 | -57.4696 | 2026-10-08 18:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 154.4 |
| bdcfcab9-14fa-340f-8fb5-ada8d4723e78 | -12.232 | -44.7194 | 2026-10-08 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| f1f67b71-96b9-3cbb-88b1-8b0f7dfc7ab4 | 1.7121 | -55.6063 | 2026-10-08 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| ac20403e-dc24-32d5-9abe-d106b071719a | -9.8817 | -44.8632 | 2026-10-08 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 442.9 |
| 75389d1e-3129-3e9b-a6f8-31756f68c0ef | -8.9497 | -45.1563 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 9657fd9e-c19d-3313-831c-db20db93a3ba | -3.1697 | -58.6244 | 2026-10-08 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 156ed97e-7e9f-3069-b768-c90630eb4dd8 | -12.2311 | -44.7661 | 2026-10-08 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 340.9 |
| 4303f573-889e-3bd3-962e-1f6dddffcca7 | -3.8383 | -55.9774 | 2026-10-08 18:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 462171d6-7f5f-3e0e-8388-72b86734ce9b | -9.8821 | -44.8402 | 2026-10-08 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8f536dc8-2198-37d5-a1e2-bc0ecab199db | -9.9398 | -43.5542 | 2026-10-08 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| cbc3666d-e7d5-3a70-9e8f-af0ecf8895e6 | -11.6181 | -43.6669 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 75a40888-9160-3c85-aaab-c7b20314ddcb | -9.0068 | -45.1271 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7a6cec38-6faf-3cfb-80ee-93126e81a1f3 | -3.13 | -53.7229 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7bbd73a5-8e82-347d-b54c-3a0a53f751d3 | -7.3941 | -44.469 | 2026-10-08 18:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| fb980f8a-ea1a-3741-b528-28cba9bfae5b | -8.9305 | -45.1812 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 348.9 |
| f1f9274f-7cd7-35e9-87bd-82f8f6b9e2f3 | -12.1549 | -44.7314 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 669.7 |
| e42d72bf-03c9-3eb3-8da0-73d4569ec6e7 | -8.2176 | -46.4068 | 2026-10-08 18:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c905ca2c-804b-3dfa-bd39-a5ed5b1d879a | -2.4623 | -56.0879 | 2026-10-08 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 81deb1cf-b0ba-3ab2-bfc4-76f836f239d1 | -6.1973 | -52.85 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 99b4b623-4a0e-3198-8bf2-584426193962 | -6.1496 | -51.7614 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| dc99a847-3a1a-38b9-812f-2e564af7a011 | -9.4509 | -45.8271 | 2026-10-08 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 70d55cee-3533-370b-8478-619d84d4387a | -2.9271 | -53.9295 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 77606d8c-996f-3ecb-ba63-1eaef6784193 | -9.1072 | -67.8141 | 2026-10-08 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 88659492-f89c-3fb3-96cf-4d260d9b8fcc | -9.9589 | -43.5516 | 2026-10-08 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 7c3050c2-2f59-31fc-a193-1d5d80b647da | -2.9449 | -54.1099 | 2026-10-08 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6e306d2c-b9d9-396e-8e37-562c8bc43b35 | -10.0734 | -46.0028 | 2026-10-08 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f75e4cf1-6336-384d-aad3-f9701b805fa9 | -6.6906 | -45.3066 | 2026-10-08 18:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| d93a9543-acc2-3c4b-bfb1-5e7bbbf836f1 | -8.9501 | -45.1334 | 2026-10-08 18:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 4ee02454-5798-300d-a17c-667b0fe6b7a4 | -6.3694 | -45.6033 | 2026-10-08 18:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 215.4 |
| d0201247-612d-3c61-af74-d409262bdbf8 | -6.3283 | -55.3276 | 2026-10-08 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 478c532a-7983-3896-89ab-3e6968970237 | -3.0375 | -53.9066 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 20f74a35-30d6-3870-aaf0-e8288f94fdda | -3.7057 | -57.0998 | 2026-10-08 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c4f61d2a-e6d0-3e5a-a6e9-1ffa1f1a15e7 | -6.0611 | -42.5844 | 2026-10-08 18:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 16fd346d-6331-3142-ab27-822142daa2f4 | -1.856 | -57.057 | 2026-10-08 18:00:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8ddfd331-9ba5-31f3-af52-80c47e44c7af | -6.1431 | -47.9214 | 2026-10-08 18:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4b334091-73ef-3ccc-b350-31c9abaddcab | -12.0444 | -43.4578 | 2026-10-08 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 5fb8b680-6c98-3064-9a74-c200a422aa04 | -15.3419 | -42.7704 | 2026-10-08 18:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8e1e7e2c-48e4-3ec7-8287-22e6f529f322 | -5.989 | -53.5132 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b4f1cd7a-3495-3dda-acbd-90edc9070421 | -1.5307 | -54.5159 | 2026-10-08 18:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e8ca0302-d0d1-37a9-b54d-cb0b227e5c03 | -3.1115 | -53.7637 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| db0bf70f-944f-32b0-b452-2529d464cf7e | -12.2316 | -44.7427 | 2026-10-08 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 321.6 |
| 57e45ea2-332f-36b6-8b30-7a47e4850da5 | -10.2488 | -49.6636 | 2026-10-08 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4bcfe1b0-be37-3301-83ea-06f18d51793c | -9.1257 | -67.8137 | 2026-10-08 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 108760db-2448-3c1c-8612-da050115a3ea | -6.4568 | -55.4609 | 2026-10-08 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| c7fd95bb-5e58-3985-98b7-7c7da8b8f6a3 | -12.1733 | -44.775 | 2026-10-08 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 20c26241-b5ca-3296-8d37-f3f0d004999d | -9.4317 | -45.8519 | 2026-10-08 18:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 91b12073-8e0f-3f52-889a-50dc27b0ebc7 | -6.6711 | -45.3761 | 2026-10-08 18:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| d6e1ce7e-2855-35d1-867a-debb29948f48 | -6.1001 | -53.5075 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e7e145a4-3c24-3e21-bb0c-9b126a28d333 | -11.7335 | -43.649 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| d2009023-1794-3b32-9b39-a70f695565c4 | -3.4312 | -56.9307 | 2026-10-08 18:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ff82da0a-9960-3351-b754-bd7fdc96afbc | 3.7462 | -51.6224 | 2026-10-08 18:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4e6948ac-d810-384e-b0c4-dcbb25e338c3 | -6.5129 | -55.3784 | 2026-10-08 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 5be3971f-b4df-37a7-bc94-1fa52b30b538 | -6.1484 | -51.927 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 599206eb-8121-3a13-9534-dbfac27deca0 | -6.3134 | -54.7884 | 2026-10-08 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0270a9f9-414f-3bc3-ba26-5e41d143f237 | -6.2162 | -52.7876 | 2026-10-08 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 21086cc5-bf68-3e9b-97f7-6f6e220cd771 | -11.6387 | -43.5929 | 2026-10-08 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 383.3 |
| 51fb9bbe-a2ef-37b2-970b-46adf4f7d3e8 | -2.9819 | -54.0287 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 2b8bc336-af19-32d7-80b4-707f5e26c9eb | -7.4697 | -42.8315 | 2026-10-08 18:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| b5c9e1be-a661-3c62-ac86-f6c0ffabaedf | -2.5492 | -58.0373 | 2026-10-08 18:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 41279696-3b7c-3cab-9553-421640a09fd2 | -3.0559 | -53.9062 | 2026-10-08 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |


[Clique aqui para ver as próximas entradas](README387.md)
