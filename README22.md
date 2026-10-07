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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c1969b6-9c9a-372d-acf5-0c18227c425c | -3.5223 | -58.752102 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acc2034b-21f6-36ca-aabd-367fcde61f80 | -11.011 | -45.472599 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 190f81f2-16e3-3c06-9bc9-2d737b4b70ba | -4.0036 | -56.261101 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce642cf7-d185-3e60-bec3-0e964b72bb71 | -3.2883 | -54.021301 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef37dbc-2357-3152-9d70-ff6b57b8b560 | -3.0802 | -54.278999 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df59ccda-c29b-3f70-a961-97e8745f5a11 | -3.5192 | -54.658798 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2fcaea-2cd2-3d3c-9329-ea819f9acaf3 | -2.878 | -54.207802 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61bb7bec-5d12-322e-a4f5-8e56de1bccb2 | -7.8696 | -44.2034 | 2026-10-07 01:09:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 50da5990-eec9-3659-814e-c253eafb6cd1 | -11.1111 | -45.695499 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd588209-ce61-3a5c-9eb9-780a2709e88d | -7.7575 | -49.210899 | 2026-10-07 01:09:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bd83f163-b965-3894-8532-ff6278c08f3f | -1.2814 | -54.569401 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 329394cb-b2b1-3395-9245-2fc388264589 | -7.7444 | -49.199699 | 2026-10-07 01:09:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5fac45d8-3d11-3e4b-819a-e41bf75278fd | 0.7866 | -59.2015 | 2026-10-07 01:09:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14fd9192-a3af-3471-8a0b-542623f0cb1e | -2.7753 | -54.121101 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d94e05-2373-3c4a-966f-626dae5c7ef0 | 1.7257 | -55.606098 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0837c708-1b48-3ebb-b9a6-be254f5aa444 | -3.0991 | -54.1828 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a29e62a-42cc-3586-8ac1-d6b53243eae9 | -3.1351 | -53.762402 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23913c36-b458-3f99-91b9-8e803c8594b5 | -3.585 | -54.3209 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78573489-335d-3343-b8e8-b84612aefc32 | 3.1443 | -60.605801 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0c6c61-d1ec-3c56-8236-6946ac2f752c | -4.0266 | -54.888599 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3302769b-6632-37f6-a3a3-8f32f859345b | -4.9972 | -56.051498 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd9882cf-b6ff-3e24-9569-b67e31c18dbf | -2.7904 | -51.6791 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a5d422a-b2f3-3a30-9f4c-bef27ded95ce | -2.5511 | -57.390499 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec2c1908-a3c0-3653-9178-b67837cf7ea3 | -2.9199 | -54.1222 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37277e73-6164-3f50-82b5-94cb20caa800 | -1.2894 | -54.5592 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81278b5f-5fb7-3784-9fae-8a086e9b0301 | -3.975 | -55.8242 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f880b55-3d64-3fe6-a692-1072353b2973 | -4.9956 | -56.044701 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd23dd3a-0508-3f91-b1e0-605d3ac668be | -2.9591 | -54.1133 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a76bbb-5627-3d9f-ae74-a3c40a1448f8 | -3.8922 | -59.337399 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d21d4bba-9452-362f-8d7b-03e93fb560af | -2.0999 | -52.0686 | 2026-10-07 01:09:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05bd77d-d185-34b7-b9e8-1e7afc398ee0 | -0.0502 | -53.253899 | 2026-10-07 01:09:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98bc869-d326-37d1-b1a8-5ea4aab53fcb | -6.2088 | -52.839199 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51efd48e-6f4d-3abc-a4ae-390302175cc6 | -2.9941 | -54.130699 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea9ac4d2-3ff7-3860-a921-e722665d6db9 | -3.0863 | -54.261002 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f538cb-5a98-3444-99f4-92ceb97e1392 | -3.2792 | -50.141201 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 418ff3f7-ae9e-3ec1-8838-02324465fdb8 | -3.1037 | -53.7607 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c13f46f-7db7-3716-9a75-b32c8caf7014 | -3.2762 | -54.057999 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78c82899-ab39-375b-9426-095e5cfa5d9a | -3.0058 | -54.136501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f22729c-9077-3d3d-8034-ea1982a0b2e3 | -2.7715 | -54.1049 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf494ba3-62e4-303d-9e6d-4448d22f6cb6 | -3.9788 | -56.063999 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57c9f780-b94c-3155-ac58-f6a43f24c5c4 | -2.8985 | -54.118599 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f8be8d-ec9d-37cf-b9d9-3a8ed0ffeeba | -3.555 | -59.484901 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee08e314-56a7-3aac-be14-b8da88a1595c | -3.1771 | -58.638901 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a00adbf6-dc76-36b2-9f5d-fbddcb819cfb | 3.1495 | -60.5835 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecb9b71-00e8-33f2-90c2-c5402ddecca4 | -3.5814 | -54.305302 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 137f207d-5d40-3f6e-9110-b5895ff58fd5 | -11.2288 | -44.856499 | 2026-10-07 01:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13808dcc-5c44-37c8-900f-bde154dca599 | -3.6954 | -58.291302 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6f0723d-af9a-3ffd-80ef-61aaaedeccf4 | -8.2856 | -50.268902 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad38b402-de07-33f5-8d84-8998edc6ab51 | -3.7292 | -51.209801 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e381ac69-e3c5-3537-b4d0-7593f2ef7c8f | -3.0953 | -54.166801 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0146f2d-d444-31c0-b7f5-b814b7e4890e | -2.8789 | -54.1231 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a02d390-6c9c-3b23-93f7-68200028ac45 | -3.2897 | -54.071899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353bdf82-ae24-32bc-a3fc-4cccbd13b666 | -2.1568 | -59.224499 | 2026-10-07 01:09:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b89697f-1cfd-3ad3-b35e-a0466da4b95c | -3.1149 | -54.1623 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d55c4c0b-3572-3389-aee7-1df577b68745 | -3.0998 | -54.274502 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a81f5047-97b4-3e97-9a69-b441a8323fd5 | -3.2706 | -54.033798 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e18a612-a127-372e-bf6e-1b7a70426f23 | -3.0575 | -54.2257 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de7a4685-a3d7-38e6-ac4e-777f78438af6 | -3.7413 | -59.443802 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbe3f4a5-4cad-3f4c-b2d4-5e3831b21adf | -11.0762 | -45.8372 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b863b2f-57f0-37f6-9990-8dddc00a58cc | -14.2658 | -41.634399 | 2026-10-07 01:09:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 924cc82e-4273-3103-83cc-dc6becb8a0ec | -3.2364 | -53.887402 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 710fde56-022e-37a9-b792-e0f9dcebf8c7 | -2.5969 | -57.5452 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68af491e-d898-3bd0-909c-a99374fe8c46 | -3.6615 | -60.6371 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc1ec84c-8c63-3fc4-abd4-f8dd95b9b5b1 | -2.9218 | -54.130199 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49f8a95d-3d84-3830-997f-f6ede50717fa | -3.6532 | -55.324902 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 935b254d-d140-3596-8b1e-bfffcb9f9ea0 | -3.4811 | -59.476898 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba4be117-1850-35fd-812e-4b810c912029 | -3.2825 | -50.155102 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75de53e3-acb7-3ae4-bd56-469f6783c283 | -11.0708 | -45.8167 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0ca5c7d-209b-3f7f-9363-194b4c433166 | -3.1051 | -54.164501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1c972ed-2867-3c79-8efb-c5f3b2f13d18 | -3.4996 | -54.6633 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eedf796-36d2-3a77-b62a-08bef89cc38c | -3.8501 | -55.998402 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12bf32bb-bb66-3525-994e-41a8ce788dbd | -2.9162 | -54.105999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 651fb251-d33b-3c06-a108-708b71b4c3aa | -2.7637 | -57.687698 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48188d86-6b34-3aab-a088-8a2aff20e649 | -3.1316 | -54.366699 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc5b149-90e7-3c22-93f4-2233b30d0522 | -2.9526 | -54.174 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c419c0f-b3bf-3f70-81ee-cbd65d09e5dc | -9.1444 | -65.933296 | 2026-10-07 01:09:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8effceb1-bf11-35fe-8b34-8bacaeb85f63 | 1.7071 | -55.642399 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ffa5388-a946-347d-bce4-e541a0d0f454 | -3.9922 | -56.2565 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64cc06e1-5136-3fbd-805e-1073c6f8de1d | -4.7609 | -55.653801 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8191d5a0-b4bc-3a1a-97b2-2c3f846dbf52 | -3.0471 | -54.269901 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ceecc8-452e-3e7e-ba2e-87425f24a3e4 | 1.5227 | -55.9977 | 2026-10-07 01:09:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8730524e-1621-3835-b2d4-5cd821953a29 | -3.0062 | -57.756302 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed8aa627-5cbe-39c7-a030-bd27756adc0e | -1.1026 | -54.153198 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0057ef51-be7a-3831-8c73-1cc0097c615b | -6.5837 | -53.028099 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54dbfafe-0ed1-34cf-9005-06bbf96b3f89 | -2.799 | -54.090099 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7b3054-63c3-3e21-87a2-d782f128b009 | -3.6575 | -60.6194 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76c611c3-3df7-34b9-8cf1-5eab862c1c83 | -3.0757 | -54.1712 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de950933-1dcb-3d03-910d-78d6776a381c | -4.3809 | -59.906399 | 2026-10-07 01:09:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93f16f09-9b17-3a85-ad06-db50fc950156 | 0.9389 | -60.419899 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 40e342a4-4333-34e2-a5f6-fd2516e2c713 | -3.7417 | -51.219101 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e10f77-67d9-339d-832e-411649ec59d1 | -3.6804 | -59.629299 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8d7e36-4593-30d9-9f63-95c058bdd66d | -3.2939 | -54.045502 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 508405a1-0897-3916-938e-0c871cbeafa8 | -3.8705 | -55.818401 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 254bc8a4-fe0b-3b93-95ff-90f0e62bb379 | -2.793 | -51.690201 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b604e129-cba8-31f4-a62e-b4b15538117f | -3.1351 | -53.718399 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 702b55b5-729c-3328-8caf-3b76b05f79be | -1.8036 | -57.0998 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8acfea23-44fa-3aec-94f3-3371d3da6142 | -6.2166 | -52.8283 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a374b7fe-18ff-396c-a3a2-cd9ac8d5aae9 | -2.9974 | -54.189098 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4c1b9e-535e-3408-bec7-993676fb6ffc | -3.213 | -53.875401 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d79c93a8-b2c8-34ac-93e9-dbf907cb291d | -3.2804 | -54.031601 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
