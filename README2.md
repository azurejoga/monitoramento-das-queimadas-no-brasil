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
| a64e43da-da57-304b-b080-f05ab4e11b85 | -6.2527 | -52.8675 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 961d771d-e08d-349e-9617-cbb48499ec06 | -4.0628 | -59.8519 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 14b0604b-9045-3550-ac5f-9f952b37abeb | -6.1689 | -39.4391 | 2026-10-08 00:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 5398779e-e104-36f1-8b43-b6fd41ecb562 | -3.478 | -59.597 | 2026-10-08 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 70a24c57-118c-38e0-bd6f-4e6683f69098 | -8.7228 | -45.1812 | 2026-10-08 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| e100d64d-8790-3056-b49b-c3aad267b265 | -2.572 | -56.1842 | 2026-10-08 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 245ee86f-146d-3fc3-a1a5-cb7b07e9fed0 | -3.5865 | -54.5742 | 2026-10-08 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 1b940b04-ec0a-301e-9400-2963ca78c5cc | -2.7613 | -54.0941 | 2026-10-08 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 72fdf386-2d95-3279-a28d-6e0f1a6603de | -3.2499 | -46.9589 | 2026-10-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b2e36207-113c-3949-bcc7-f2bf639780cf | -6.895 | -43.7066 | 2026-10-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b9647e96-685d-31b9-90a6-2babd2924c35 | -5.7656 | -42.0628 | 2026-10-08 00:00:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 0b2c6422-830e-3dbd-b4ba-198220727cd1 | -8.537 | -66.9764 | 2026-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e421f01d-82af-3c10-b310-9972c73a7885 | -2.5903 | -56.1642 | 2026-10-08 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 28a6bb71-d3b8-3c1b-b83b-c786410100d8 | -5.7117 | -53.4862 | 2026-10-08 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e378574e-2140-37c6-ba49-f5812f7700f7 | -3.478 | -59.5779 | 2026-10-08 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ce3d923c-f1d3-3a60-bd68-0bb6a9b5849d | -2.1629 | -59.217 | 2026-10-08 00:00:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 78bc6d13-1e52-3d9c-a911-dba358cd4900 | -3.1284 | -54.1857 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 96537bc3-6aa3-3eb6-bb1d-93c57a8e798d | -3.328 | -50.1775 | 2026-10-08 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 688462b5-ce0c-33b7-ab75-2d77cb1ccd97 | -8.7417 | -45.1791 | 2026-10-08 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e4d4fada-3e50-31bd-a235-8253b1a63a06 | -6.2342 | -52.8685 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 5dd053ca-247b-3dc1-94ab-de636acf1286 | -1.4756 | -54.5365 | 2026-10-08 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| cd8909ad-e7c7-3ee3-b037-50139a1a2030 | -4.1176 | -59.8697 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 529b4a16-6f00-3798-b3d4-cacbe4e2f122 | -5.7376 | -45.1533 | 2026-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ba81bff6-d3d9-3f1b-982b-9b856e140896 | -6.6315 | -43.7533 | 2026-10-08 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 1683fdf8-4507-382e-8431-df5d0daf357c | -1.4569 | -54.7761 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6d5e7728-45b0-3c8b-97d4-d036a7dc2f1d | -2.7797 | -54.0736 | 2026-10-08 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c5ed2c1b-04c3-3faf-b835-ae1252251141 | -3.073 | -54.2874 | 2026-10-08 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 34449457-7ec1-3aa0-82fb-308330676d45 | -7.8478 | -49.285 | 2026-10-08 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8c590cf1-9dcb-3628-a802-1b2134f5a79b | -1.5485 | -54.8348 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| af50f617-a011-36d0-99af-10a037a4390f | -3.2499 | -46.9589 | 2026-10-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| df7cafa7-c03f-3fd1-a667-b82886b09546 | -2.1629 | -59.217 | 2026-10-08 00:10:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| fe885110-c7bd-33fb-82dd-fb1cc43438c0 | -4.2954 | -49.0807 | 2026-10-08 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cea6dff5-d1a2-34a2-925d-e3cc298a0154 | -3.6049 | -54.5736 | 2026-10-08 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| cc368208-4331-37ba-943b-079b03cd2478 | -3.1298 | -53.7834 | 2026-10-08 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 77c1160f-458b-329a-ba5a-966d0dc525f6 | -2.8895 | -54.1915 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 713185ef-7c1d-31af-a417-c7593a2af7b4 | -7.7579 | -54.9499 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2c96d255-d202-31d1-b4b7-567f7543266d | -2.7613 | -54.0941 | 2026-10-08 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5e8a67c1-aa08-3df9-aba5-f1c6b499151c | -9.0592 | -65.9209 | 2026-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d426234b-11d5-32a6-ac97-2907fc45e118 | -4.0628 | -59.8328 | 2026-10-08 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d264fffd-db4d-339f-9e12-076dd20de4a5 | -3.1297 | -53.8036 | 2026-10-08 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cd68d44f-59bc-313f-8c75-9801a6ba1187 | -5.6931 | -53.5073 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 338070df-2ed0-3a72-96f9-3c54a2665d10 | -1.5306 | -54.5558 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ee7e26da-63d8-33bb-a708-c37b2ec678a0 | -7.1964 | -45.354 | 2026-10-08 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| ad05c1e3-a704-3653-9ada-345c3f2043da | -1.4756 | -54.5565 | 2026-10-08 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 88bfe0d3-5b74-375d-bb65-064f183ecf64 | -1.4756 | -54.5365 | 2026-10-08 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ad17d74f-0d94-3407-87fc-51d9376212fc | -2.5903 | -56.1642 | 2026-10-08 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 404b1819-85ea-32de-9009-774f015161ae | -3.478 | -59.5779 | 2026-10-08 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1fafa8c1-36b3-35be-8c53-fff2bf807e24 | -1.5118 | -54.8352 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 72c59d68-97e0-3728-a28e-16ca8b883c59 | -2.572 | -56.1842 | 2026-10-08 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| c8c5f66f-8a37-356f-96bb-2ede01976ef0 | -1.5302 | -54.8151 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| f1871cdc-a586-3059-b120-6d2c699e5e49 | -5.7117 | -53.4862 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 005b0eb8-e91d-37b7-ada1-13ad005853fa | -3.2313 | -46.9596 | 2026-10-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e50b6e51-c16c-331e-9ced-918a75613b33 | -4.3473 | -43.779 | 2026-10-08 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 420c55ed-1f9d-3258-a195-2ab87274b2a6 | -3.1114 | -53.8041 | 2026-10-08 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 5ff4bd87-e778-304f-ac5e-0ccc967dc49a | -6.0935 | -49.411 | 2026-10-08 00:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 802c9126-9d27-3704-b37e-f277de43d4bd | -7.218 | -55.1617 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 808017c8-8ac4-3af5-ac91-5123567feffc | -3.1973 | -50.5382 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c60a9cb5-25cd-3c72-b612-43b3034ab156 | -6.2157 | -52.8695 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a473e4e6-b45b-34b5-aae2-b593a60485f8 | -3.1972 | -50.5592 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 97c887ef-9b91-3441-8440-430a4c369910 | -3.1285 | -54.1657 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| ff5abac4-8cd5-39c7-8620-462d7bf8d89a | -5.7116 | -53.5065 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 553befe7-9592-36cb-a6cf-516124095339 | -10.434 | -47.2601 | 2026-10-08 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| bbceefcb-27dc-3f2f-be8e-3379aed53c55 | -7.4443 | -63.5401 | 2026-10-08 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 761dc9ef-5a0d-3097-aefc-b164f5e529ee | -2.7796 | -54.0937 | 2026-10-08 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d2aaa047-d351-3692-b8ae-0ed6281bc3a3 | -2.8575 | -59.1107 | 2026-10-08 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5c2966c4-cb2c-3fcc-9826-02f8b8478d00 | -5.9586 | -55.3648 | 2026-10-08 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 99585409-20be-31ca-9ebd-4a4aab7080b5 | -4.3471 | -43.8021 | 2026-10-08 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| db28e1a5-e6e1-31ca-9ff2-ab1ae8912d18 | -9.0591 | -65.9396 | 2026-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1b83bdea-b030-3ca3-bf7f-334606e1b14a | -4.3658 | -43.8011 | 2026-10-08 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 498e5a17-3c53-3883-8f6c-fa214a39474c | -3.2157 | -50.5586 | 2026-10-08 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0104ad1c-a0dc-3194-a0d2-d4977b30256f | -3.5698 | -59.4803 | 2026-10-08 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b1d7ac81-5704-3f2f-88da-a23d7ae7c428 | -3.8383 | -55.9774 | 2026-10-08 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d1d79bb4-d21a-3d50-ba92-d72e1945ff29 | -2.5903 | -56.1839 | 2026-10-08 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b0d3e82c-abed-3554-b88c-80b6495bfe13 | -2.7612 | -54.1142 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0a3ce87f-c8df-38c1-847f-4301fb2f249b | -2.1629 | -59.2361 | 2026-10-08 00:10:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 40d256a3-36ff-347e-bbfe-a626cccacdf7 | -9.4749 | -64.3713 | 2026-10-08 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1e76b264-0a40-39fb-ba51-b072756e5a76 | -6.8764 | -43.685 | 2026-10-08 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ebf340be-6c47-3cef-92d3-a00ad57778cf | -3.11 | -54.1862 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| a2c502e1-46d1-376f-97eb-05da2790cef1 | -2.572 | -56.1646 | 2026-10-08 00:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 50336672-82da-3557-906e-eb5d9455df06 | -16.8634 | -40.5966 | 2026-10-08 00:10:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 145.8 |
| 78d83f26-922a-366a-a9a2-a66cc48d7636 | -1.5301 | -54.835 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| cc7b9d29-b339-3f21-8598-8e5d809272b1 | -6.9797 | -71.6457 | 2026-10-08 00:10:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 57b7f3b4-fb55-30f2-9f81-9a5612de065d | -5.6932 | -53.487 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 217.3 |
| 989d7a01-724d-3d9e-b104-58cbc9e7652c | -9.475 | -64.3525 | 2026-10-08 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 49cc5828-f55c-3d85-a75f-0e9905402171 | -3.5865 | -54.5742 | 2026-10-08 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 843542c3-313d-3047-b269-b8d089fcc44e | -3.1115 | -53.7637 | 2026-10-08 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 981a344f-4e24-3ad9-a928-93581282f360 | -2.8896 | -54.1715 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5867b111-a4b4-3f86-a55b-5f4444ffd8a7 | -6.2529 | -52.847 | 2026-10-08 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8f745ad2-d82f-3fcc-bb81-a1181c7973f5 | -6.8952 | -43.6833 | 2026-10-08 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ad6bfee7-56ad-3f56-aa97-62ff43dc7a57 | -3.328 | -50.1775 | 2026-10-08 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bf4f15c1-a336-3fd4-b6c6-65b1b150aae8 | -7.2366 | -55.1606 | 2026-10-08 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 90cc7eb5-49a3-38f4-a7e8-174b90ff5090 | -10.4337 | -47.2824 | 2026-10-08 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9f249477-cff4-31ff-bf60-01846f861bb5 | -3.0913 | -54.287 | 2026-10-08 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| c79546b9-dda5-3b5d-81f2-4ed6254839a1 | -9.0407 | -65.9215 | 2026-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b76b7c5d-9e50-329c-bef9-2626ad50b70f | -6.8762 | -43.7083 | 2026-10-08 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 13894697-71b4-3f23-9950-aace9e4f8571 | -8.537 | -66.9764 | 2026-10-08 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e43bc73e-61a0-36a9-b479-654f4ea6db4b | -3.2554 | -54.6631 | 2026-10-08 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ff2dd725-39b3-3770-964a-51674b3fcb59 | -1.4569 | -54.7562 | 2026-10-08 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e4244e72-e742-3fc1-80e6-8875f91eb896 | -6.6319 | -43.7068 | 2026-10-08 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 46c93775-5f1a-3d95-817e-05920378cb09 | -2.8711 | -54.212 | 2026-10-08 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README3.md)
