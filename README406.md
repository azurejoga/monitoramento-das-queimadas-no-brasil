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

## Dados Diários - Página 406

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 353fc896-9105-3c44-a4ce-378d05cd827e | -1.5301 | -54.835 | 2026-10-08 19:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 2d123db6-1130-3a50-9b7c-392d8c58425a | -1.1094 | -54.1601 | 2026-10-08 19:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 932d342e-fc78-3538-9f15-b6be4c703bf4 | -10.4914 | -47.231 | 2026-10-08 19:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5996e26e-d17a-3d77-9cfd-19af3f375d2a | -2.77 | -57.5293 | 2026-10-08 19:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| ede844e6-7aa8-33b5-b1c4-e904e10ba800 | -3.3636 | -50.4911 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 60a80385-2105-3e6c-8932-23d69bd757aa | -5.712 | -53.4455 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 4e850ad8-358b-31ca-a112-ad60ec173110 | -1.5302 | -54.8151 | 2026-10-08 19:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 615a9e78-5ab1-3245-b581-a7061b5e84ec | -6.3316 | -35.1619 | 2026-10-08 19:20:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| dcc85bd8-50a6-37a0-b483-34dd40bf9199 | -6.8907 | -45.8988 | 2026-10-08 19:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 3cd00bed-d6a3-34cd-aab5-9064a3f5bd5b | -1.3111 | -54.1982 | 2026-10-08 19:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d5b5303c-8bc4-3878-b6f5-2d983b962ce1 | -5.6934 | -53.4667 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 404.2 |
| 5a4c88a4-5b68-3a48-95b4-936f636368d3 | -3.2532 | -50.4108 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b0d707c9-552b-3970-ac1b-9e9f9e7e1958 | -3.1697 | -58.6437 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 184cab3f-d2f1-32ee-a52d-c32cadbc3a3b | -6.0421 | -42.6096 | 2026-10-08 19:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| fbd7b7dc-f160-3d65-bfc0-7b6d314a657a | -12.2316 | -44.7427 | 2026-10-08 19:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9de03fa0-fc7c-32e6-8346-27ddf140d832 | -6.4413 | -55.0224 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| f08d452f-f8e6-31aa-b065-6a729c4aba43 | -6.0024 | -40.935 | 2026-10-08 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 219.2 |
| 9688b65d-f8d7-32c6-87a1-ff8f5142038f | -3.8911 | -42.1187 | 2026-10-08 19:20:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 44f17c57-a366-38f7-85e4-8df58f6818f4 | -6.2162 | -52.7876 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 203.8 |
| bb55572f-a23d-35f9-a5de-77d7d58f616e | -5.4956 | -42.8648 | 2026-10-08 19:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 26cea12f-3ad2-3386-93bf-3819a617ef53 | -8.2176 | -46.4068 | 2026-10-08 19:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| abf62ef4-732e-3b19-8c70-b01c9e44401c | -4.2152 | -46.9396 | 2026-10-08 19:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 386f983e-e7c4-3246-8800-0cf88643721a | -2.8712 | -54.192 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fba08976-f762-3877-901c-e0bd06f07dd3 | -6.6814 | -55.0903 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 4f5c5089-5afd-39cc-ad0f-ed5c6441be9d | -3.2085 | -57.87 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c63ad1a5-118d-350d-8173-c1a39b6b5577 | -5.3718 | -44.1981 | 2026-10-08 19:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 35083b72-e058-3638-88bc-4cf6b1ef83cb | -3.8005 | -41.6468 | 2026-10-08 19:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| b12f488d-59e7-39b5-bd9a-e481b8e344eb | 1.6938 | -55.6066 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| bf21d2aa-e031-38b5-938f-0df9ca5d85ca | -4.0838 | -44.1159 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 70c65b6a-e885-30ee-8fad-19676259da1e | -6.4949 | -55.2995 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 292.4 |
| a033ce87-e453-3c5b-a1d7-b7d58c5081c1 | -14.4585 | -41.2104 | 2026-10-08 19:20:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 673ed7ca-67a7-3623-8ec1-d22f5f9798d1 | -5.8842 | -43.4199 | 2026-10-08 19:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 3f40439a-901c-38f1-91dd-486c27c88bf7 | -6.895 | -43.7066 | 2026-10-08 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ced4934e-45ee-3946-a23c-59c26b50975b | -2.7613 | -54.0941 | 2026-10-08 19:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 5dc2e139-f56c-3227-9880-080da81f98a7 | 1.7488 | -55.5663 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 52b4e105-ef8f-3e0a-b505-98f8b1af67a3 | -2.0834 | -46.5765 | 2026-10-08 19:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 72d61b72-1a51-354e-a3ca-9f89dcac4c36 | -2.9271 | -53.9295 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 48a2ecb8-23c6-37e7-95ad-91b469ca73d6 | -6.6027 | -37.8944 | 2026-10-08 19:20:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 1692e9d1-c53e-37f6-953f-cbfffddf6df0 | -6.8904 | -45.9212 | 2026-10-08 19:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a3fae881-5e88-3d38-bc3a-883e5a2dc2af | -2.9267 | -54.0501 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c54ee312-3199-3286-ae28-22603c14019f | -5.3905 | -44.1968 | 2026-10-08 19:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2005e6de-6f63-3c5c-952a-8abb4a183c16 | -15.1051 | -43.6409 | 2026-10-08 19:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 157.9 |
| 5e51ab54-6c22-3897-b77b-fb4136f393b3 | -6.5127 | -55.3984 | 2026-10-08 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 422282f1-a22b-3958-895f-5c381f4e00e4 | -2.0649 | -46.577 | 2026-10-08 19:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 24cb2d70-75f7-36c3-8d42-44784fe3d423 | -2.8346 | -54.1326 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 243.2 |
| e1e31133-5f03-3c0a-a55e-38ccb76ac36d | -7.4694 | -42.8551 | 2026-10-08 19:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 81fceb4c-d605-33f3-9d13-1db32b7efa14 | -9.9208 | -44.7893 | 2026-10-08 19:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c31301bc-e1a1-3fcb-935d-269e4c50ec10 | -12.2311 | -44.7661 | 2026-10-08 19:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| b5d8ba84-ffab-3836-8e7c-e7e25c657c4d | -3.0256 | -57.7768 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 8794a146-bcab-3877-965a-518707b89478 | -5.6136 | -44.3647 | 2026-10-08 19:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9dbe03d4-0337-36a5-84c8-cb866b58ea05 | -7.5882 | -42.3925 | 2026-10-08 19:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| a060d236-2780-3581-8e4a-13d183ba2dbc | -2.1361 | -54.4671 | 2026-10-08 19:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 570dca5f-ae60-35ce-bd2c-9c08da2aca09 | -1.7681 | -55.0309 | 2026-10-08 19:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ff2f781a-707e-340c-93b4-986110cfe4a9 | -6.8319 | -39.3213 | 2026-10-08 19:20:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 95.3 |
| cdd44acd-ab7c-3faf-bd1a-0801d4861e5a | -2.7429 | -54.0945 | 2026-10-08 19:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 9bf86ea4-abec-307d-b141-11cd1efd090a | -8.3011 | -45.7245 | 2026-10-08 19:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2c8d6d62-2bf5-3a1c-bfaf-329fb2bf8548 | -7.4097 | -44.7427 | 2026-10-08 19:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| a1bbed4f-bf52-390a-a452-efa7e405e310 | -5.9587 | -55.3448 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 22a84149-3856-307e-b558-d76910fc6de7 | -2.7612 | -54.1142 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| ecf2960a-ced6-3fae-8695-20a99970f1e6 | -3.9299 | -56.034 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| cfedd5e0-11e0-3d64-b805-d4ea5dac23c9 | -2.9005 | -56.6685 | 2026-10-08 19:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9ceceddb-3935-3452-8320-645440686acb | -5.1133 | -46.2048 | 2026-10-08 19:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 5b3401ec-5135-347a-9254-bae6c1f6ef5f | -4.6362 | -50.9646 | 2026-10-08 19:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 791.4 |
| 6cbac704-a5d7-33cf-9997-e85026af91c2 | -3.3139 | -59.3898 | 2026-10-08 19:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 1802ee33-1b3f-3e74-8a48-06d4b30eaf9d | -6.3283 | -55.3276 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 40929da3-547e-326e-9c09-dc9c483fa242 | -5.5144 | -42.8634 | 2026-10-08 19:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| e37d6fb7-f511-3725-96b0-c3f1de300cf1 | -3.1114 | -53.8041 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9ac88233-9f58-3a28-ae7e-bbde4d31f754 | -6.0076 | -53.4919 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 82c52b9a-d1a0-3b30-95e5-2baeebbd9022 | -3.1874 | -58.8358 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 318aefe4-92cf-31d2-b503-e6279fc8e1ec | -6.1615 | -47.9419 | 2026-10-08 19:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 16184035-baf1-3487-8a6d-431361fb11fe | -7.8533 | -45.4066 | 2026-10-08 19:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 1485d475-c1d2-3b28-b6b4-15837dc30d01 | -3.2634 | -57.8689 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 974b5bd6-e494-387f-b997-4a2b2ad2d3b0 | -12.62 | -44.5414 | 2026-10-08 19:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| d9fe1ff4-fded-3242-a3c1-401444ee8c8f | -6.4411 | -55.0424 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 250.2 |
| 9872ac40-9f03-3022-a473-69a6d6efbc9e | -3.86 | -44.1274 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| db2f9a30-7f36-3bba-be6b-b2f1eee84a3f | -5.6932 | -53.487 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 258.3 |
| e02656ab-e02d-3e80-96de-6be517de13ce | -3.2633 | -57.8883 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 94d102ac-745f-36ed-8fbe-e5076fbf7eb0 | -2.4942 | -58.0768 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 26dbb1c3-4f18-3927-b10f-ad257a489ef3 | -2.8434 | -57.4696 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| f2ebcc83-2f3b-3fa9-8431-e7269a51e5b6 | 1.6937 | -55.6461 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| a400fa2a-b7c3-31a4-9490-ab62676bb762 | -2.5491 | -58.0566 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 8bff8db1-df91-3f15-a7c0-7421459f9a03 | -5.6935 | -53.4464 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 1735f1ba-27fa-3089-be80-b23bf372e6b2 | -6.4032 | -55.1842 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| a9e33c85-1a84-317d-ba92-d7a17a22f591 | -3.2957 | -59.3902 | 2026-10-08 19:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 92079a99-e5b2-3b31-9163-b60023364547 | -2.0759 | -56.8784 | 2026-10-08 19:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 251f2a80-604c-337f-8ad7-f6fea1ef7ab8 | -2.3115 | -57.9829 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 91b48e78-30fd-30a4-baa7-a87743ecbeca | -9.8817 | -44.8632 | 2026-10-08 19:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 294385d9-586f-3b34-97ff-ec90c5798b09 | -4.6642 | -56.2083 | 2026-10-08 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 728ba692-e92e-395f-80ae-6143a244c6b5 | -3.1115 | -53.7637 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 85f0fa73-72be-3e3a-8c13-30f129e28eec | -3.2717 | -50.3893 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 90d8ab43-d5ed-3e3e-a51d-5c47dc553822 | -5.9586 | -55.3648 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 34de9ebd-4dcd-33e4-8869-f76fae729255 | -6.0021 | -40.9594 | 2026-10-08 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 433.0 |
| 964c09dd-b87f-3f3b-b93f-7c0a7ce3c840 | -3.9483 | -56.0138 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 11190953-a39d-37a1-9d6a-94e94e2e3104 | -11.6387 | -43.5929 | 2026-10-08 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 0238f332-f16d-3012-9324-e04c8eb2b0af | -1.3264 | -56.398 | 2026-10-08 19:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ea30b221-db14-355d-aeac-b4dc70de0714 | -3.354 | -58.1961 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9933a758-fc1f-369b-ad65-06a33130c834 | -8.0766 | -45.6112 | 2026-10-08 19:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 62f87016-ef54-3037-997e-bbf5c6149079 | -3.1601 | -50.6021 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 65d743d3-4b52-3f57-b35d-58680e60eebd | -9.9011 | -44.8378 | 2026-10-08 19:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e642a95f-0d09-3ab1-93f0-d40797811e58 | -6.509 | -55.9554 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |


[Clique aqui para ver as próximas entradas](README407.md)
