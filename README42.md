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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8343c37-08c4-3b29-ba0f-b203760491af | -6.15 | -39.4409 | 2026-10-08 00:50:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 124.1 |
| b190acb5-461c-308d-ba0b-4ff5d594a8fd | -3.8566 | -55.9967 | 2026-10-08 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| d8d16ede-3e97-3e49-82fc-78efb62cc4bc | -4.0628 | -59.8328 | 2026-10-08 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a9bcd8e8-d94e-3c66-9d71-39714d85c83a | -4.3471 | -43.8021 | 2026-10-08 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4730546f-d668-3e64-b98b-2f433e32de84 | -3.1114 | -53.8041 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| efaa6031-de81-3315-b618-b02895749e6d | -5.7376 | -45.1533 | 2026-10-08 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5d0064e5-3cdf-37c9-936d-1eb8d6947cab | -3.1601 | -50.6021 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 452a2492-4356-3c3e-be18-75d531fa77f4 | -8.7231 | -45.1583 | 2026-10-08 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 28ccb9b1-a8e5-3db5-a7ca-ecd4558d279a | -9.6456 | -63.7615 | 2026-10-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9fcaa9c3-51bf-3e8f-af23-b009d2aec863 | -2.572 | -56.1646 | 2026-10-08 00:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 56a587e4-bc00-3839-85e6-ebcc21bd0270 | -8.537 | -66.9764 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 420af9cb-e91e-3451-ae67-b8fceeadf3ec | -3.0191 | -53.9071 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 44f9235d-6c68-3fa0-8682-8fde2f91e91c | -3.478 | -59.597 | 2026-10-08 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| adaf0253-d741-3943-a26e-926daecd5fe8 | -3.8567 | -55.9769 | 2026-10-08 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| cee8a002-d5d1-3227-b5a0-927b8f4f570f | -3.478 | -59.5779 | 2026-10-08 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 9109ae4d-30a5-306f-9fea-a291ed089059 | -4.1176 | -59.8888 | 2026-10-08 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0bdef23d-9608-3278-8770-d319a1a2329c | -3.073 | -54.2674 | 2026-10-08 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f74fd1dc-1ad3-3dfa-9f1d-4a06d069dc15 | -5.7189 | -45.1547 | 2026-10-08 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7eab1c41-bc1c-338a-af72-e7f7759d0f85 | -3.2554 | -54.6631 | 2026-10-08 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9650a1e7-9361-387b-8390-969b4bd63cb5 | -3.1792 | -50.4551 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8d865d6c-7ca0-31b1-be44-98728e41551f | -8.3882 | -46.3006 | 2026-10-08 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9e416d4b-fc60-371f-8df7-390cc91d817c | -6.2158 | -52.849 | 2026-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1c561534-5b4c-3382-ab9c-8e94ce2edf7c | -5.6934 | -53.4667 | 2026-10-08 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 67a1b31c-5069-3740-90d8-95a2be2d0a4d | -6.1689 | -39.4391 | 2026-10-08 00:50:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 148.1 |
| c413ba55-2812-36ff-b167-d53fb6e354bf | -3.1973 | -50.5382 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3f6fc241-5f11-386e-b106-5e8fb6f63a98 | -10.4337 | -47.2824 | 2026-10-08 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6d12bc98-293c-377c-916a-496bb94cc411 | -6.6129 | -43.7317 | 2026-10-08 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 944e8769-9794-30ce-884c-7a476dd1c3d2 | -3.1114 | -53.7839 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 90444372-e8dd-30bf-a93b-fab8ae1dbf2c | -2.7613 | -54.0941 | 2026-10-08 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6911fac3-0882-33a0-9cb4-b23ae6e604a8 | -3.328 | -50.1775 | 2026-10-08 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 559c0227-e24f-32d7-b0d7-0d4dfe2d05be | -4.4507 | -47.9112 | 2026-10-08 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4743b44d-663e-30d3-9520-3f282575bcb1 | -3.8383 | -55.9774 | 2026-10-08 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 51d894b7-ba88-3f3f-a62b-ff45b9796b3d | -3.1115 | -53.7637 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 656da0f3-77b8-325e-879c-4d4ea28650d0 | -8.5369 | -66.9949 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 367482f7-23e6-36dc-b93b-cbc4e6ff9c77 | -2.5903 | -56.1642 | 2026-10-08 00:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 10a5a94e-6adb-341d-adc6-f43b3461720c | -3.1972 | -50.5592 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| e45def4c-d631-3bdd-beba-f13cc6c750b6 | -5.6932 | -53.487 | 2026-10-08 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 407.3 |
| 002727da-9776-3f7d-83fa-63794117feb6 | -6.2342 | -52.8685 | 2026-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 0855a7d4-5684-3ef2-995c-00947339f012 | -9.4936 | -64.3518 | 2026-10-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d58ff370-9ad2-3009-b26b-f88aef0cce1d | -6.9881 | -59.1037 | 2026-10-08 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 36ef79a6-c6e1-33ce-a1c5-5a98159132d7 | 1.7488 | -55.5861 | 2026-10-08 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7ccf248b-1a26-33c9-8d84-8088e5565fc8 | -6.988 | -59.123 | 2026-10-08 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| cd1de205-0491-3b69-8afe-a4f0c4e41c7c | -7.0065 | -59.1223 | 2026-10-08 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 265e68bd-704d-3910-8eef-02ec23cc00bb | -3.3104 | -54.7016 | 2026-10-08 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 0f68fd66-53be-34b9-a208-e4e6075e72d4 | -3.11 | -54.1862 | 2026-10-08 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| fe79ece1-12f2-344d-a99c-748e2b78a45e | -6.2527 | -52.8675 | 2026-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 15048946-813d-34cf-b2d3-7eda67fcf8f9 | -7.1964 | -45.354 | 2026-10-08 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 30ee751d-bffd-34c7-a2cd-b4d69e3e6659 | -3.1697 | -58.6244 | 2026-10-08 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| aaa3f7d3-47e8-32dc-bcb1-49311adad3b4 | -3.019 | -53.9473 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3d4e700f-50f3-3641-9514-481bc0373ec7 | -3.5865 | -54.5742 | 2026-10-08 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5d645d85-7ac4-3ce9-8065-3a76e4a04f4e | -2.7797 | -54.0736 | 2026-10-08 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f719081c-680d-3a85-b0d1-5ed0485758d6 | -3.0373 | -53.9469 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 8a1945de-579e-3bbf-8ed7-d5004ca428e6 | -6.2157 | -52.8695 | 2026-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 481e5f8f-9712-384b-8932-965403c93f4c | -6.6319 | -43.7068 | 2026-10-08 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4ddb84bd-7376-30d0-826a-ab62765cc67e | -6.0935 | -49.411 | 2026-10-08 00:50:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5f103131-2b62-3de5-b69c-b3119cedc1ba | -3.2157 | -50.5586 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3b40b90c-bb80-37a4-9e0c-da128d418149 | -6.1691 | -39.414 | 2026-10-08 00:50:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 7cf9b114-99c4-337b-a20c-287675d62a2b | -3.0374 | -53.9268 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e47081e2-e1f6-3c18-b1be-59182901daf4 | -6.8762 | -43.7083 | 2026-10-08 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 28d4405b-9f88-3a40-9165-b82ac8639c26 | -9.4935 | -64.3706 | 2026-10-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7d80e655-f011-35e1-9421-276c7fd64ceb | -3.1607 | -50.4556 | 2026-10-08 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6cddbbc8-fdfb-3716-99c9-3c931301e53d | -3.2499 | -46.9589 | 2026-10-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e87cf422-d063-3387-8af3-04989f1d4488 | -3.073 | -54.2874 | 2026-10-08 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 517caeea-aa23-3909-885a-7771ae158f97 | -2.7981 | -54.0732 | 2026-10-08 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ab5b2ea5-7709-3f15-b0f0-ad113a41ba08 | -2.572 | -56.1842 | 2026-10-08 00:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ce953f14-da54-301c-9537-bdb98312f86f | -2.7796 | -54.0937 | 2026-10-08 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7f70f8ca-85d2-3de8-9bf0-dc7131cafbb4 | -3.019 | -53.9272 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| bae9c07f-62bd-32e4-bfff-722ca3c7ffbc | -3.0913 | -54.287 | 2026-10-08 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| cdd4bccd-69c8-3549-9a92-8665966b757f | -4.0628 | -59.8519 | 2026-10-08 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 20cc3184-8686-30a1-ba0a-c93dd13bc704 | -9.0407 | -65.9215 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bb0befb9-814f-302b-8d00-1ec6a517208e | -6.6315 | -43.7533 | 2026-10-08 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3fc83fc8-2f5e-3311-baa6-0c1c0403f1e4 | -2.8575 | -59.1107 | 2026-10-08 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 7c721566-4eae-32ca-9b12-a366680650ce | -6.6317 | -43.73 | 2026-10-08 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 1247b24b-fb61-3203-a0ac-f4195384db61 | -5.6931 | -53.5073 | 2026-10-08 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| b3307f00-9441-36b6-ae7e-55d68690952d | -17.6355 | -46.6565 | 2026-10-08 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 79aa4985-20d0-306f-8ae6-b353413a1ab4 | -17.6155 | -46.6607 | 2026-10-08 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| bd524dc0-f81f-3469-b705-0169e5fb915e | -3.1101 | -54.1661 | 2026-10-08 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 3c732946-6ba7-3ad1-b6b9-af0c49584eea | -9.0592 | -65.9209 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 8362deb0-e001-3754-9506-39f68165e5ab | -3.5515 | -59.4807 | 2026-10-08 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| de1f6c01-f5cc-3080-9167-3e73791d45f5 | -4.3658 | -43.8011 | 2026-10-08 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 25994c81-b26c-3c63-907c-7424cb7f65c9 | -9.0591 | -65.9396 | 2026-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1ba64288-26d4-3e38-96b4-5d4136bddaf6 | -3.0375 | -53.9066 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5a643b85-bdf5-3015-90f2-e5a6d9936708 | -6.8764 | -43.685 | 2026-10-08 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 62980853-27bd-36ed-9322-10f85287e4d3 | -5.7117 | -53.4862 | 2026-10-08 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 301.3 |
| 7d79fb47-2913-3237-8ce2-634a79289fed | -9.475 | -64.3525 | 2026-10-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| db5c20d9-bc4f-30e9-a0f3-315847187059 | -9.4749 | -64.3713 | 2026-10-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 60190193-ede1-3757-9faf-fec35c61518f | -3.1298 | -53.7834 | 2026-10-08 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7ebd104e-69f9-3017-ab27-3a8cbbea3e3a | -3.1285 | -54.1657 | 2026-10-08 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 486abeac-a07e-3328-8151-1173a194dff3 | -5.7116 | -53.5065 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 567c96d6-c153-358d-9ac7-45ec98bba8b2 | -3.1298 | -53.7834 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7f61b7f8-0b8f-38e2-8abc-74b85be7d056 | -2.4805 | -56.1072 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 28e4d33f-5005-3375-ac56-e823ae57c19d | -6.2529 | -52.847 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f4532b48-7969-3cdc-8fcd-f76086f2c377 | 1.7488 | -55.5861 | 2026-10-08 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9965e172-3201-387f-8c8f-3d00d0cb8d00 | -2.5903 | -56.1642 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 05bcad10-6055-35eb-a221-1ed29ef91fea | -2.4805 | -56.1269 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 089ce1f0-3112-3672-baae-8c8822a9dea4 | -2.7981 | -54.0732 | 2026-10-08 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 835e65be-4540-3ca8-8765-bbc7601d4608 | -11.014 | -45.4272 | 2026-10-08 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6849ca26-86d0-32ab-9677-4edbeb7ea62e | -3.2499 | -46.9589 | 2026-10-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 85dc05ad-cd69-3502-8481-165141207f20 | -4.3473 | -43.779 | 2026-10-08 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8da8c95e-9002-35e1-8e73-7a1cfcbef910 | -6.1502 | -39.4158 | 2026-10-08 01:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 74.9 |


[Clique aqui para ver as próximas entradas](README43.md)
