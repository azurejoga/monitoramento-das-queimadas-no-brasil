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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4900be71-5570-31a2-93df-d6b5d39656e6 | -3.3248 | -58.1569 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e859624a-6a5e-38e8-90d9-1f1d01681e57 | -2.57939 | -56.17524 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ceb8eb36-0615-3680-84b4-d9b1a6c36aa0 | -4.05757 | -55.33421 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f983aa63-7d6c-328c-8d89-1ebcac5cea61 | -3.65716 | -54.52363 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4a81b2c8-c630-3470-a74b-c81dcee30ee1 | -3.42145 | -54.07124 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9f5619fc-03aa-3e75-9a91-62e9dc58329f | -3.72847 | -57.14967 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9f85b72d-00de-3579-80ec-57237b85b1a4 | -3.63373 | -58.99557 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d0854e21-680a-3d40-9001-d121564ff6b7 | -3.53559 | -59.4096 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3b4eb7a2-8552-376e-80f6-5d17ca56ff29 | -3.72038 | -59.69104 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82951366-1180-3393-8c7c-7a70fc64493f | -2.89026 | -59.21122 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bf0cb3d7-0a95-3205-bcdc-70894cbac7ee | -2.85804 | -59.10807 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4c0dd921-29ba-3a89-bd30-593703450fa8 | -3.74928 | -59.4929 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0e4f59d-e6d1-3703-91cd-1f9e6dc23c6a | -3.4002 | -60.84988 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c644b25a-2363-33aa-abe4-2a5e45c8d5d7 | -3.47656 | -59.58485 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 207460e0-71a6-3246-9d98-865c310677ab | -3.09951 | -59.19658 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1cfe1a67-79b6-3ea7-a855-e30ce76476e4 | -2.34418 | -57.9964 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b3f5c4f7-1dbd-3971-b3e1-927befba05e7 | -3.54441 | -59.40837 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d5e9eb53-6920-3fcf-b9b1-b53b3c22ac00 | -2.99297 | -57.75605 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc1e9559-dd5e-3400-9cba-1edb1a30eb52 | -4.73631 | -55.65766 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 98d3899e-22db-3b4d-aae8-cc7a6bf22a60 | -3.39893 | -60.84056 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd53ac1b-ecfe-3572-948f-ac578beeb7f3 | -3.60863 | -61.63387 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fb57e1f3-0e21-34ec-8838-0f621c5b94d2 | -3.02378 | -57.7841 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 90714c93-549d-319c-b703-5e9f59770352 | -3.55767 | -59.50495 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 914fb423-bae6-3cd1-984e-00b149ef125d | -3.93981 | -56.02985 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b55f4b27-4a50-3da8-82d5-4e07e0b4c47f | -2.85043 | -59.11811 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 02213841-89e8-359d-9207-18c529677943 | -2.84345 | -57.47765 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 62a71c98-e320-32f1-8d1a-5eedbf4f0cde | -3.9 | -55.8937 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 490b72c8-692a-37db-90df-c3e8ba943e5b | -1.52852 | -56.12296 | 2026-10-09 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f667a573-fb30-3829-a55b-cd57978a7ac3 | -3.5788 | -52.67823 | 2026-10-09 00:37:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| eb8197d5-945f-3b89-9e36-094c77bf5bf4 | -3.57159 | -54.48726 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2447aa14-da41-334c-8009-9122fe8605fa | -3.29211 | -61.00434 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 21c2c7b0-1c5e-36f0-98b9-d1c7c27e6776 | -5.23599 | -60.19548 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b3df0f14-0a8c-3b3f-81ae-cba892112dea | -3.63929 | -59.55886 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a923998e-50b2-31b7-a030-740691ee6202 | -3.60726 | -61.62378 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2131ae38-c9c6-3b8d-9071-52e67bc13cbb | -3.00319 | -54.77259 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d415489b-61b0-3736-b649-22b490868475 | -2.95869 | -60.98848 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b5fe5da-5406-3a72-b1e9-540602ea6b22 | -2.47515 | -56.08751 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0183e856-e26c-33a3-be02-6ef67410a48c | -3.10511 | -53.77716 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| b3596063-cb39-3645-9c71-c0b07fad001b | -2.30675 | -57.98881 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6526cd28-1364-35a0-a8b9-ab0de76a9406 | -2.54493 | -57.38728 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5d581396-b49b-32c4-9bfa-ded12a7db5c1 | -3.50569 | -59.33921 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e3eeb26d-82f2-3803-b9b2-ae64e3991158 | -3.90363 | -58.94854 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6de4df20-5d71-3a62-8954-cdd59a03fe97 | -1.72224 | -57.15235 | 2026-10-09 00:37:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a40f8e91-e857-35d9-aada-8580140f84ed | -3.62582 | -54.23403 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3c2d074a-84ab-3419-9126-2ac190ce0f75 | -3.08171 | -54.28635 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| adb5e4d8-b674-3cb2-a5e5-7d95a4b18a86 | -1.15691 | -54.24208 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 32587c9d-6ff2-39a0-ab43-dc3230c45446 | -3.80076 | -59.32726 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36532915-1157-3b56-acbc-7b380e988903 | -3.24007 | -54.66065 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 554f0edd-dded-3d2c-96c3-9753f225ec91 | -3.78769 | -59.38011 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 445243b2-0f0b-3a60-9b5a-f5fdab2df436 | -3.71798 | -54.22085 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dc89c253-2af1-38ed-bb83-4222843b1e0a | -2.94294 | -54.18804 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 38431ba3-2559-3019-b5d8-4dce765cd4b6 | -3.46774 | -59.58608 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1d6f5e9-08e8-3f24-b94e-d18ec6090078 | -4.64326 | -50.96704 | 2026-10-09 00:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d74370e1-4e6b-358f-9ca1-296c7c4e977d | -3.98958 | -59.36028 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| fa4a5478-6a6a-302c-861f-b15164ec3a32 | -3.92981 | -56.03127 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d0b0e6e9-2bff-3d8d-b4be-bd8606ae5fca | -3.53439 | -59.40083 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7460b86c-b7d8-32d9-9a17-c3e52b53de7f | -2.74615 | -54.09567 | 2026-10-09 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a626056f-e878-3871-b4d5-e70eb6f6fac2 | -3.48334 | -59.50334 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2e3a2c5f-b6c2-31a8-b3b7-b5fd112acaee | -4.30699 | -60.95279 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dd390b73-fdd2-3ef5-bb60-4acaeb457fe4 | -3.40337 | -59.59241 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1e1e9600-8582-3315-9c34-a6574a4840b5 | -3.59783 | -61.62505 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 527f9e32-f576-3f21-b6dd-3dee796238fb | -2.07697 | -56.88824 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0630a061-6ea7-3b5a-805d-9b13b1649081 | -2.92194 | -54.12489 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2fe8a402-737c-3d5d-954d-21ed94166d48 | -3.97956 | -59.35273 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4c597f83-1f73-3034-9ea0-33d24bfe393c | -3.55406 | -59.4786 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ae9a535-21f8-3816-a23c-dfb5939ad436 | -4.52395 | -61.1277 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6f41003b-95f6-3ad3-aa7f-e6dfc31d1c75 | -3.00634 | -53.90301 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 23a65913-ade2-3a29-82bc-03f0851a31f4 | -3.77079 | -59.2572 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e2ab417b-e568-3208-875d-fdf2a2d3b052 | -4.74639 | -55.66188 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c37a5577-efa8-32d5-b7b4-75f4612af75a | -3.3113 | -59.39643 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3f374bb9-810f-3c13-956e-97f6655c9f48 | -3.36032 | -59.62221 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5bf1b4a9-f119-3f9c-9c3d-c7e2bc76073c | -3.35243 | -59.48317 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ae4b0b2a-eee9-391e-8b90-e11b8da1aa9d | -3.93818 | -56.01831 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 198fefeb-aa7e-32d6-8ce2-80b57eb25af2 | -3.47573 | -59.51335 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0bff3ead-ee9b-36a5-9176-8533abf4d6ae | -2.46161 | -56.06503 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6ebfa761-4688-3891-bf9e-b4bd0dea545d | -3.78649 | -59.37133 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6cbd6f6-bf9f-354f-8ac4-5923525daa1c | -3.10513 | -53.95109 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 8487ca10-f9cb-3d67-ab0e-636508c1bf72 | -2.62246 | -56.48366 | 2026-10-09 00:37:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 84672e3f-5438-3dc7-8277-26dbf55cd04d | -3.76937 | -58.83846 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5df6b3a6-2409-379b-b226-b284b1dfbfa8 | -2.51909 | -56.61721 | 2026-10-09 00:37:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3a6ebc51-e73d-3602-a82a-91e2940fde7a | -2.8867 | -54.18636 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ef8d6508-6d5d-3095-8d81-f72154c16c04 | -3.11081 | -53.94421 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a7f6293e-2d9d-332c-8369-19def1a9a0fa | -3.02965 | -54.23553 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3b25550a-ed8f-3a31-ad29-300b62fed935 | -2.99678 | -53.92159 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 844a7eb7-a7e0-368c-89cf-ab0b2f327dd0 | -3.49661 | -59.59996 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fee5d217-b5a0-35b2-be4e-39a15951a957 | -3.12595 | -54.18213 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 87f43fd2-1ae1-3d9e-81c6-1d87f33c4391 | -3.08133 | -53.95451 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9913bb9f-3545-3f9c-bb40-22997ff50ddb | -3.15757 | -57.68167 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 43beb365-14d0-3bff-a31e-c7a6649e946e | -3.18261 | -58.65892 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90e16a1b-23bf-3484-ab58-f2b7bc5c1e97 | -2.55191 | -58.03148 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4f0a6794-2300-372a-9b78-9c965bdd8a4b | -3.38166 | -59.43437 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e6c7ee1c-2600-39b3-bc5e-4c072b2e4553 | -3.73444 | -59.4502 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f68df1b6-0048-3dac-803b-d37d174f8df6 | -2.85079 | -59.2678 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ac4d69de-031e-33ab-92b4-6ce70f7d10d8 | -1.20294 | -55.69649 | 2026-10-09 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 71754372-1559-3fec-89ad-c8c93ed0da8e | -4.52215 | -54.86884 | 2026-10-09 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 58302eb6-20cd-30a3-a7c6-60027515f48c | -3.56501 | -54.68386 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 69a47959-9bae-3507-8601-74caac974cb7 | -3.46642 | -60.25175 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| db985f69-b714-317c-b22d-3fa216b0fe0e | -3.52025 | -59.23281 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1a51179-68fe-36e3-8d94-314845deb826 | -5.0984 | -56.19791 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f3f6c822-6d06-3b66-92a4-17d2a87f147d | -3.97907 | -59.62796 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README40.md)
