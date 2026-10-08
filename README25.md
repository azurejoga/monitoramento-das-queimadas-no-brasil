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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db7cf87-86e5-35ba-8823-a8efd95947e1 | -3.8383 | -55.9774 | 2026-10-08 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 085d00d6-09d5-3436-a535-50fb74a21cbd | -4.3658 | -43.8011 | 2026-10-08 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d27abf92-2ee1-3a7e-97e4-e8bf3db5ce89 | -5.7116 | -53.5065 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| b9e4a9d1-b7be-321a-9d1a-069377e9758e | -16.8634 | -40.5966 | 2026-10-08 00:30:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 61ad8994-fd57-3b52-b330-dba07e5c4ddc | -2.7613 | -54.0941 | 2026-10-08 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 851d1a85-093d-3df3-8d71-3169ed1f627d | -7.0065 | -59.1223 | 2026-10-08 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 365c57e1-b811-3d25-94a5-fb270078463d | -4.3471 | -43.8021 | 2026-10-08 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 94a6aca3-8c16-3ca3-a13d-c22e0cd5c833 | -5.6932 | -53.487 | 2026-10-08 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 321.2 |
| 1814690a-4f93-32d1-a7ee-2aa24bcf2cd7 | -3.1298 | -53.7834 | 2026-10-08 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 97e81f7d-bedc-30b7-9e17-95ae3d7cbf08 | -5.9587 | -55.3448 | 2026-10-08 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0c718415-7fd9-3b88-9365-cde0043b9dba | -6.8764 | -43.685 | 2026-10-08 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d04dfcbd-9102-3e41-988f-bbb7934d3a01 | -5.6931 | -53.5073 | 2026-10-08 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| a9c1268a-8091-3ad5-9021-d2c1632c4059 | -3.11 | -54.1862 | 2026-10-08 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 3f65b1d1-6e3c-3b94-9da6-6dcfbf3a1176 | -6.1502 | -39.4158 | 2026-10-08 00:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 4f8d25c5-d130-33a2-b58c-dc61bf998b7a | -8.5369 | -66.9949 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9b1f7d8c-4412-3a90-a0c9-95484cbad4bc | -8.7228 | -45.1812 | 2026-10-08 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 210b9dfd-1f72-3d83-a954-077e7e41809a | -3.1792 | -50.4551 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b3e71c52-2159-3f76-adb8-f92e9bfa8f19 | -3.8566 | -55.9967 | 2026-10-08 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d927ad9b-47de-3439-83d0-8b77c71c5f19 | -2.5903 | -56.1642 | 2026-10-08 00:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 46a37b29-6133-37e1-80a0-d71900d6932d | 1.7488 | -55.5663 | 2026-10-08 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4f04c4de-51c9-39f0-bfaf-67d5a20d22ca | -3.2157 | -50.5377 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4b5b399f-e136-3909-84c9-10ebea0801e7 | -5.9586 | -55.3648 | 2026-10-08 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 08891872-1fb5-3abb-8638-c37d9421fcbe | -6.2343 | -52.848 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 77efb22f-8c4f-304b-96bf-752334a4557d | -2.572 | -56.1646 | 2026-10-08 00:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| ab899745-806c-3877-983e-fdc9c67d40f5 | -3.1879 | -58.6433 | 2026-10-08 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1ecce6f6-c499-3f02-a2a4-71b81f9527be | -9.475 | -64.3525 | 2026-10-08 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 4db05b9a-9aa3-3102-9216-22415d52b0de | -9.4936 | -64.3518 | 2026-10-08 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f4551907-a8ba-3ca4-880d-c34ac0b541f2 | -4.3473 | -43.779 | 2026-10-08 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 6ae28836-b258-3495-8154-d56687c33dc3 | -9.0407 | -65.9215 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 858dbf88-f3d5-366a-a47b-26dae7edf1c8 | -16.8948 | -40.8938 | 2026-10-08 00:40:00 | GOES-19 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 452b263b-f8cc-3afd-b174-919b1887cddc | -2.7796 | -54.0937 | 2026-10-08 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b2e781f7-f69d-35b8-9aed-520e3c28544e | -6.2529 | -52.847 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4277eae7-8da2-34ae-b6f5-142fa9c289b6 | -3.0914 | -54.2669 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a3b99830-3cc9-356f-b022-b173ea3be15e | -3.1101 | -54.1661 | 2026-10-08 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| f0897b7a-294a-3daf-bae2-16f1e8fa148f | -6.6315 | -43.7533 | 2026-10-08 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 24a87be9-2114-3eba-a4cf-3553864aa9a8 | -3.1973 | -50.5382 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c2a6842a-1e75-35fc-a62b-8eb9acaa7957 | -3.6049 | -54.5736 | 2026-10-08 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e3add024-e4d3-3f8b-b4de-7c590409d699 | -3.8383 | -55.9774 | 2026-10-08 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| aa02b185-77dc-39a1-a970-a6d9ad86b565 | -3.1297 | -53.8036 | 2026-10-08 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| dbdbc205-ce14-36d7-8afe-7e1e68c0b354 | -3.1633 | -54.7452 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 64e48b3e-0051-3d05-8237-c1736d136398 | -4.4507 | -47.9112 | 2026-10-08 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 271c2c40-15ea-3692-bb7d-42e3715d8b49 | -3.1285 | -54.1657 | 2026-10-08 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| decdbc7c-4136-35b3-b301-9e5ca36d01e8 | -5.7116 | -53.5065 | 2026-10-08 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 237.7 |
| 7553b364-4a76-303f-8779-af5cb6dbeba1 | -4.0628 | -59.8519 | 2026-10-08 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 44e58be2-23a8-3841-9b04-8bcfe778445d | -3.1697 | -58.6437 | 2026-10-08 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a7d98a70-d5e8-392a-ab90-ba6ba6262b81 | 1.7488 | -55.5861 | 2026-10-08 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5a256138-a13c-36d7-8c1f-52b97cbbffa3 | -3.1601 | -50.6021 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6ae67309-5847-3fc2-8931-7bc49d2c3ddc | -2.572 | -56.1842 | 2026-10-08 00:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 5df31933-5d6f-31fd-bd32-e0bf399b0f7f | -6.6317 | -43.73 | 2026-10-08 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 232.1 |
| fa79b3e8-97dd-33ee-b9fc-9137bcf5d870 | -3.1114 | -53.7839 | 2026-10-08 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| b819a7ff-7cfb-3209-a674-7fb834cecabe | -3.1115 | -53.7637 | 2026-10-08 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| fb425d8e-6987-38fe-b30c-a729f309e356 | -3.1607 | -50.4556 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| acf9d507-7d78-3151-b4c5-47d095bd2b64 | -3.1633 | -54.7253 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 0ebd9a2b-aab6-36c7-a593-6aba61356568 | -4.1176 | -59.8888 | 2026-10-08 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9af6bdb8-bfb0-33da-af6b-d32ca58c211c | -6.8762 | -43.7083 | 2026-10-08 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e48eac71-5143-3b1a-8a38-56b171e26e6c | -3.2499 | -46.9589 | 2026-10-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| ad424907-097c-3a34-aae6-44ac266f2a83 | -2.1629 | -59.2361 | 2026-10-08 00:40:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0c767038-d9a5-3f27-a57b-43d96a290409 | -9.0592 | -65.9209 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a268e1fc-80ed-3937-bef6-efa7d525ee40 | -6.988 | -59.123 | 2026-10-08 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ed32b970-202e-3c77-824f-c71a00a5d82c | -4.0628 | -59.8328 | 2026-10-08 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4df7abde-957c-3b8a-b765-8a6bbdf41cb0 | -6.2158 | -52.849 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| df4579c0-3eb6-3e28-806b-39d546aff84f | -2.8575 | -59.1107 | 2026-10-08 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3f2f7f86-e0fa-3d32-9ede-49eb6a7639e0 | -6.2527 | -52.8675 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 00b51e89-0e94-36be-a940-e9da2bedc77b | -2.7797 | -54.0736 | 2026-10-08 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 84a528e7-2c74-384c-a7be-d5712e6c12fc | -9.0591 | -65.9396 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e4cf33aa-b8d4-37a9-8bb8-f57b66268326 | -6.6319 | -43.7068 | 2026-10-08 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e9dfde56-a552-306d-bbe4-028d6aaa782c | -3.5515 | -59.4807 | 2026-10-08 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 794c9d2d-5e58-31cd-b774-53edebafd446 | -3.2554 | -54.6631 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a786cc3a-75ec-3473-a74c-5761c0fba325 | -10.4337 | -47.2824 | 2026-10-08 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a03304f0-0748-31a2-9405-322dbc6f472a | -7.1964 | -45.354 | 2026-10-08 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7dc6ea48-39e0-3c0c-ae5f-19c6f1079fa4 | -8.3882 | -46.3006 | 2026-10-08 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| da572b31-ecf1-3b3c-82fe-605906ef26d5 | -3.073 | -54.2874 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8d3e12a5-f371-338e-8a2c-7bac48bb2b21 | -8.537 | -66.9764 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 8cfae0c6-4a92-3880-a389-83f236cefb7b | -2.7981 | -54.0732 | 2026-10-08 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 026f3504-752f-3b3f-9839-52d642ac833e | -6.1689 | -39.4391 | 2026-10-08 00:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 46b0b9c6-57a2-3464-94fb-408a58d5f246 | -6.2157 | -52.8695 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f5fe4441-f718-3d68-9579-b6aa3c038f6f | -7.4443 | -63.5401 | 2026-10-08 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 256b9f90-6a86-3a60-bb64-42aa14fc9d71 | -9.4749 | -64.3713 | 2026-10-08 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 51adcd24-be5e-3d0b-88df-96338d266bc7 | -3.1114 | -53.8041 | 2026-10-08 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 84adbeff-815b-3f02-9eb0-2046dac197d1 | -2.798 | -54.0933 | 2026-10-08 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 37759928-9860-38ce-9ec8-215a91c823d3 | -3.478 | -59.597 | 2026-10-08 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| aafd854c-c010-3fd7-b06a-8e0cebf5a07d | -5.7376 | -45.1533 | 2026-10-08 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| cc4132da-b368-3fc2-87d4-c6a5a34100a8 | -5.7117 | -53.4862 | 2026-10-08 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 323.9 |
| 76c4ba84-d022-35eb-84bd-3b1e9f1f6aa4 | -3.2157 | -50.5586 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 1a82616a-a49f-395f-9453-787b7bca6210 | -9.0406 | -65.9401 | 2026-10-08 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 204f51c9-00ed-3beb-a507-0e9aca6cf7fe | -2.7612 | -54.1142 | 2026-10-08 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ad6dc314-bbf3-354c-8405-89f7413e5040 | -3.2313 | -46.9596 | 2026-10-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e3801521-1a3a-3143-adaa-8d1f1de0585a | -3.478 | -59.5779 | 2026-10-08 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| a76fb5cf-8a76-34df-b059-27321eb87b41 | -6.2342 | -52.8685 | 2026-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| f7ef9f4c-4871-388e-816d-cfbb9028f500 | -5.6934 | -53.4667 | 2026-10-08 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 216dd9cc-282d-319a-9ab7-020e37d97f72 | -12.232 | -44.7194 | 2026-10-08 00:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 32c9c0fc-9e7a-3590-b480-064dc85658fe | -3.328 | -50.1775 | 2026-10-08 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 38e1a42a-8961-37a4-82e1-dbbfd4b740e2 | -6.6129 | -43.7317 | 2026-10-08 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e95c40d4-f2b9-32c1-b726-8b933eb98976 | -9.4935 | -64.3706 | 2026-10-08 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| be32b2c0-5ead-39dd-90bc-a5dc239bd4fc | -3.0913 | -54.287 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9f558b03-cc71-33be-8f87-d1617154b63e | -6.15 | -39.4409 | 2026-10-08 00:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 7c57e88f-5dc1-3124-82ee-d5616c2da82c | -3.073 | -54.2674 | 2026-10-08 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 781a9453-84fa-39df-a128-5f15ad04a0ea | -3.5698 | -59.4803 | 2026-10-08 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1816865c-98a8-3962-8331-24b591af860e | -3.1972 | -50.5592 | 2026-10-08 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 2a6083ff-aa2b-3a18-8700-0d1e01176c3d | -3.5865 | -54.5742 | 2026-10-08 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README26.md)
