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

## Dados Diários - Página 384

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4827d882-ea19-36e7-b815-b0085a9fefaa | -11.6181 | -43.6669 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 75dbde60-c3fb-345d-b910-4c6f50d189b8 | -2.4806 | -56.0875 | 2026-10-08 17:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 843005b8-962c-3249-ae3e-0750670348ae | -12.2316 | -44.7427 | 2026-10-08 17:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 223e9a63-ee52-3c35-8bee-7b96f345abaf | -9.2745 | -67.6433 | 2026-10-08 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f4a0e9d1-4683-30de-a179-0f40c00a9691 | -11.2657 | -45.209 | 2026-10-08 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7e96e127-def1-3f32-bb9a-780fdabd0307 | -5.5148 | -42.8164 | 2026-10-08 17:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 204d1d0f-f611-3428-90a9-e054241d9063 | -11.6562 | -43.6846 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e6e451ea-066b-3c16-8539-62bbf21e0a41 | -11.7738 | -43.5482 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 936b456b-8d13-3cba-8fc3-90969d9d0834 | -5.2905 | -42.7388 | 2026-10-08 17:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 12dd9992-9a6d-3fb0-83dc-7174af2257c2 | -1.1991 | -55.6909 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 15417cf5-c4d0-3fea-9853-0b236d69e625 | -3.1874 | -58.8358 | 2026-10-08 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| c6daca1f-e603-3b12-8a5b-d31ac1a67e5d | -7.4697 | -42.8315 | 2026-10-08 17:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 1cb17b7f-a0e6-3680-b871-6913fa9963bd | -6.3134 | -54.7884 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d9beb024-a9ad-3ada-8e12-bef04f7463d4 | -3.1879 | -58.6433 | 2026-10-08 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 310.9 |
| ffc4fb8c-4f82-39f4-9080-3ee9122a9e0d | -11.2271 | -45.2374 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7ea71ac8-8504-3485-9650-27ebe3021ebc | -6.5322 | -55.2577 | 2026-10-08 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c967017d-7614-398a-b667-8d038519acb2 | -11.6387 | -43.5929 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 314.3 |
| 39a42724-c82f-3317-99a0-8dda139048cf | -5.4958 | -42.8413 | 2026-10-08 17:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 140.3 |
| 628145fb-1058-376a-b5b0-7bf2a14b350c | -3.0375 | -53.9066 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| bde25093-ad21-377e-a487-91cb67ffdb4e | -6.9331 | -43.6566 | 2026-10-08 17:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ab88ab4b-6020-3b9e-bde9-219fbc1da304 | -9.4819 | -66.7836 | 2026-10-08 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 157.2 |
| be7d2301-4d31-3a6b-a01d-7fb688c80ed3 | -3.1951 | -42.9538 | 2026-10-08 17:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a46453db-161e-3695-91ec-1363b4370320 | -3.7439 | -41.7217 | 2026-10-08 17:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 233.2 |
| 9107434c-9029-305a-89b4-8926751ca2fb | -5.9838 | -40.9123 | 2026-10-08 17:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 6d08b96b-c5a6-3a40-948e-14412f02535d | -8.9873 | -65.4379 | 2026-10-08 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 490046ff-b626-3a3f-8f9f-b40e285a80f2 | -6.8762 | -43.7083 | 2026-10-08 17:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 6c8cf697-8b5d-3d3b-a1f6-61b7b613498a | -6.4411 | -55.0424 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 248.1 |
| a726b87d-83c3-3467-abee-41e2f040af90 | -2.4623 | -56.0682 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b1b938b3-7e66-349e-acad-722569aa403c | 1.7672 | -55.5463 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 632d26f7-dc11-3865-a378-04a42daad032 | -10.4914 | -47.231 | 2026-10-08 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a1de5532-24c3-326e-8d4c-79af714fe0d1 | -4.7589 | -55.6516 | 2026-10-08 17:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8f98f2f6-49d0-3ab2-ad3a-75b143f14f9e | -2.5492 | -58.0373 | 2026-10-08 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| aa1af6e8-cfa0-38e0-a459-685f80e0a019 | -3.2451 | -57.8693 | 2026-10-08 17:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 6af357f6-4d28-3250-bc3b-3b2f72094e41 | -9.5124 | -46.8534 | 2026-10-08 17:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 02affa2c-2615-396b-93ac-863bd7041e2f | -11.1354 | -46.1623 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 293.1 |
| 3dfddc03-ae46-3ad7-a3f3-7683a4f28fd6 | -3.2268 | -57.8696 | 2026-10-08 17:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8b0a0cdc-e467-3cdc-92c5-38305af48c47 | -9.4506 | -45.8498 | 2026-10-08 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 49431591-2b79-39b5-881d-af47f274d960 | -7.0581 | -40.9551 | 2026-10-08 17:50:00 | GOES-19 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 3e0cca4b-620d-3612-b6d9-d92ae72786ca | -3.1506 | -58.9134 | 2026-10-08 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c5deb0aa-551c-3ca8-ae0d-5494dcf49515 | -9.9208 | -44.7893 | 2026-10-08 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b60c2029-036f-33d3-9663-8d71498caddc | -12.1554 | -44.708 | 2026-10-08 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 437bb5ef-e711-3fa1-98a7-0c68dcae890a | -9.5003 | -66.8017 | 2026-10-08 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| a23f2b5f-2576-3937-aa0c-e9c20887cc66 | -2.9819 | -54.0488 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 8bb77a0d-1d53-3138-85a1-de5ce5e7860a | -6.4905 | -55.9563 | 2026-10-08 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d434861a-ddc9-353e-a941-6d71edc0ba97 | -6.737 | -55.0674 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| ff3b4a6c-63f0-35c9-bdb7-60b6f4557b6d | 1.8038 | -55.5261 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 24b99301-e8c3-314a-8b8a-25e0939fb53b | -2.5903 | -56.1642 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 53456dc9-1cce-3cf1-99a4-bc167140babf | -9.9014 | -44.8147 | 2026-10-08 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 60420c38-9ac0-3649-8375-d7d3b7095c97 | -7.7025 | -45.4436 | 2026-10-08 17:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f512749e-e432-3c30-8dd7-a01cf42dd3fc | -9.9018 | -44.7917 | 2026-10-08 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f3ef9a02-4203-30e5-93ab-4f12b689a177 | -3.13 | -53.7229 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3f132a98-8392-394b-b180-c52286283498 | -11.1145 | -44.0009 | 2026-10-08 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 547.1 |
| feef6a9d-a66c-3ebe-8de2-0472a5827661 | -9.479 | -67.4897 | 2026-10-08 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 778706fc-0c9c-398b-ba7a-31eacceffb03 | -3.6105 | -58.171 | 2026-10-08 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ad4b3982-5099-337e-b168-dc9a22cf836d | -9.9589 | -43.5516 | 2026-10-08 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 547aae33-5d00-3fae-8d18-c63560fb1672 | -6.2155 | -52.8899 | 2026-10-08 17:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 7bf0110b-af00-3e5a-ada9-1a78fb236ae3 | -11.6382 | -43.6166 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 8ddea85e-86ee-3794-85bd-9edf2bc04430 | -12.4825 | -62.6124 | 2026-10-08 17:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 1cbd7bbf-8ad5-32b6-aaed-140a7e4b13ab | -3.3912 | -58.0017 | 2026-10-08 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 33a3ccbc-faef-361f-b1b8-c3f3eae723a1 | -2.9819 | -54.0287 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 2e897de4-7611-3d6b-8211-4a65e589e0aa | 1.7304 | -55.5863 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 606c9936-058f-3337-b63b-d56f94daec34 | -6.1977 | -52.7886 | 2026-10-08 17:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 162601ae-dadb-3e90-9ab0-e43916cc7af9 | 1.4637 | -50.7652 | 2026-10-08 17:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e5424933-565b-3507-946a-27da2ba23bb7 | 1.7121 | -55.6063 | 2026-10-08 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7ffd243f-82f7-3dfc-9b77-13da4fb92a47 | -6.7185 | -55.0684 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e9a968cc-cff4-30ed-96fc-a8e0698487c6 | -2.9449 | -54.1099 | 2026-10-08 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 36780d0a-7118-335f-8383-638053796615 | -3.1115 | -53.7637 | 2026-10-08 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 7a1007c4-addd-36f6-9545-9c68a8d90d8d | -2.572 | -56.1842 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 0bd0df44-2262-38db-8dfa-455f76390815 | -12.4455 | -62.5184 | 2026-10-08 17:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 4c32a5ca-8f1f-32a3-9f44-948e7df6afe6 | -2.8433 | -57.4891 | 2026-10-08 17:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| e0118c50-5430-387e-8a2f-605380055d42 | -5.2728 | -55.9692 | 2026-10-08 17:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 61c02424-b058-3502-abc8-1edf1d095c63 | -3.1697 | -58.6244 | 2026-10-08 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 142.4 |
| b62cb9cb-0efc-30c0-8c7e-eb575f87f9c0 | -9.1256 | -67.8507 | 2026-10-08 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 39abe7b1-ea7c-301b-9ca6-bc804371af89 | -11.2849 | -45.2063 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 454.5 |
| 45aed2d0-eb90-31e3-a11c-c478c24cb0bb | -6.4567 | -55.4809 | 2026-10-08 17:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| fb49dac8-1a9e-3046-baa5-f33a3ec91da0 | -12.1549 | -44.7314 | 2026-10-08 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 360.7 |
| 176560df-e7cf-3186-bad4-1107536b354d | 3.5448 | -51.2772 | 2026-10-08 17:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f096c579-20b4-350f-b7b9-16b3531be354 | -12.0448 | -43.434 | 2026-10-08 17:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 02ce134f-134b-31fd-a304-a291bfa1fcaf | -9.9205 | -44.8124 | 2026-10-08 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 283cfc12-0b25-3014-8266-e24355ac49de | -2.4806 | -56.0875 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| ba329aed-082d-35c1-9ae7-ce1160817019 | -2.853 | -54.1322 | 2026-10-08 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| e5396989-d18b-361d-b0f3-9e6102146be0 | -11.2661 | -45.1859 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 1d584295-0f27-399f-bb19-d5289cae1ce8 | -6.7554 | -55.0864 | 2026-10-08 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0111cd83-cf02-3d5f-9142-88d3b430a128 | -12.1545 | -44.7547 | 2026-10-08 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 42f071f1-9c66-33f7-9f7d-730add892e30 | -9.4819 | -66.765 | 2026-10-08 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| dd6062a9-a49c-3bbf-a352-c34accb37c33 | -11.0953 | -44.0037 | 2026-10-08 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 7e2796fb-ec3e-30e9-a107-936b9742ac32 | -8.9501 | -45.1334 | 2026-10-08 17:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 431b7243-6104-3f50-9d9b-62011dc2c368 | -10.5094 | -47.2956 | 2026-10-08 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 77221dc3-d0bb-352a-8982-4ca282da35ea | -2.4989 | -56.1069 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ef523b1c-e478-3a69-a6be-b18e9a6a0855 | -3.188 | -58.6241 | 2026-10-08 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| b7b5d04a-0f7e-3309-a494-6d40a0027c51 | -3.724 | -57.1189 | 2026-10-08 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 78dbabae-01d9-3ff9-899b-008d799eed7a | -1.856 | -57.057 | 2026-10-08 17:50:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2de392eb-b818-3d7d-9997-f76d9808279b | -2.572 | -56.1646 | 2026-10-08 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 6fe3559b-f824-3928-a10c-c2882096aa7f | -2.0447 | -54.3085 | 2026-10-08 17:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a6be0ef0-61c2-31c9-9c08-d978f7c6a2bc | -9.9801 | -45.9009 | 2026-10-08 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 617c6f86-4904-3c87-8aec-55834a664922 | -8.9875 | -65.4006 | 2026-10-08 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6b784ac6-2e92-3bfa-90a9-d6effbdba668 | -11.2657 | -45.209 | 2026-10-08 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| b330aaf1-0794-3e4f-b8d9-6c2137c31a29 | -3.0447 | -57.4851 | 2026-10-08 17:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| c64c0c9f-07fd-39f1-971b-34b69d435e0d | -11.755 | -43.5275 | 2026-10-08 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 963286c8-375c-39f1-ac1e-58721a5e940f | -5.9587 | -55.3448 | 2026-10-08 17:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |


[Clique aqui para ver as próximas entradas](README385.md)
