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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a63aa5af-2b11-347f-a7fe-54a754096801 | -11.1047 | -45.7119 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2134e9e9-00f6-3be0-9c4d-3edab03c4f92 | -2.9448 | -54.1501 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3069ec46-7947-31b3-81e1-90a73ccdc1f5 | -8.7039 | -45.1832 | 2026-10-07 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 9f20943a-ac0f-3220-a60a-d85727e272df | -8.7036 | -45.2061 | 2026-10-07 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 375.7 |
| 13ad8ca0-a2c1-37a2-866a-16f9438f02b9 | -8.7033 | -45.2289 | 2026-10-07 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c72a8055-fb6f-390e-9ca4-1d0c733683ae | -10.9949 | -45.4298 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 341f39d0-d8d6-32f4-968f-6a900f454c9c | -3.6205 | -55.2907 | 2026-10-07 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| d19d4c70-91d5-3016-b472-4cdc8f31967e | -3.1787 | -50.5597 | 2026-10-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 97bae907-4440-3b9f-b5a4-5fc332431e59 | -3.1787 | -50.5807 | 2026-10-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6b1b2f92-eda9-3337-b74c-69445640a42b | -3.6579 | -60.6412 | 2026-10-07 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7354606e-414a-3a35-af96-58fd311e6aa5 | -3.1972 | -50.5592 | 2026-10-07 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5de5cec5-a512-30f5-aa3e-b49b8b665ed6 | -11.1238 | -45.7093 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 069e87d6-7261-3848-9c9d-3daa1341c972 | -3.4762 | -50.0883 | 2026-10-07 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0c208c58-081f-3e35-99a2-ba011ebd0a69 | -3.0375 | -53.9066 | 2026-10-07 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c88f3e42-25b3-34dd-b427-c85ca5b56941 | -11.014 | -45.4272 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 4fa1d42d-a69e-3ca2-b506-7644714200bd | -3.1114 | -53.7839 | 2026-10-07 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ae52ae30-eb09-3876-b94d-96e6b41695a2 | -2.7613 | -54.074 | 2026-10-07 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| dba2c918-e26e-3fd6-93ec-a6e192966bbb | -3.1101 | -54.1661 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c9a75168-1f65-30ae-8d97-832a66c72179 | -3.0001 | -54.1086 | 2026-10-07 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8ee941ce-7bf4-353f-a7c1-04fb4bc585b5 | -5.7376 | -45.1533 | 2026-10-07 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e7491ccd-4fac-32ce-89e3-48295261ae97 | -1.801 | -57.1161 | 2026-10-07 02:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 463cd93b-4112-34a1-b028-1e421f51c10a | -8.2865 | -50.2731 | 2026-10-07 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 591a1e3f-0f39-352a-a971-cfcf13aa2385 | -8.7228 | -45.1812 | 2026-10-07 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| cde4649d-dfeb-3cbc-9769-b79c5c9d3d92 | -11.1242 | -45.6865 | 2026-10-07 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a67b9263-14de-328a-9a27-d00397f675e2 | -2.9264 | -54.1505 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 504525f9-d97b-3243-8474-e61234a0fd1b | -1.801 | -57.1161 | 2026-10-07 02:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5c8a9e4a-1319-3e6c-82d1-2631cff9c515 | -14.2531 | -41.6256 | 2026-10-07 02:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 4c73092c-17ac-327c-aaa1-14a71cfbb54a | -3.658 | -60.6222 | 2026-10-07 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 14484587-7b6e-3d87-beee-5db52d09591a | -3.6206 | -55.2708 | 2026-10-07 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 45e2cc9b-5f10-39ee-aec9-d502d6a88861 | -8.7036 | -45.2061 | 2026-10-07 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 300.8 |
| befa6455-c14e-3ba3-8f3e-0d02732a1449 | -5.7376 | -45.1533 | 2026-10-07 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8a09d48f-8746-36dd-845c-ea0ed5e3c710 | -2.7613 | -54.074 | 2026-10-07 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| de7a51fe-cd13-3ea5-bc9c-7693922522f2 | -10.9949 | -45.4298 | 2026-10-07 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bc3d9c41-4796-3dde-aab5-999820e06dfd | -8.2865 | -50.2731 | 2026-10-07 02:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 8a4aa207-1a42-376d-942b-ec245c1fedc6 | -3.0374 | -53.9268 | 2026-10-07 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fe46939f-b941-3f8d-a05a-4f2086622315 | -3.8567 | -55.9769 | 2026-10-07 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5c68be36-94a3-33ae-b6e2-03593279633e | -3.6205 | -55.2907 | 2026-10-07 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1b4e8403-9f99-3a35-b1a1-8c2d57ce287e | -2.7612 | -54.1142 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 2e828eb6-1d5d-37aa-a602-15d06ddb26c9 | -3.0731 | -54.2473 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f97c670b-493e-3501-bb09-2038f3569cea | -2.7797 | -54.0736 | 2026-10-07 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f4d81d92-6f19-36b1-a064-a98f7b4dd69f | -11.014 | -45.4272 | 2026-10-07 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f35b2eaa-2cf1-3f2c-8449-889c435bd003 | -2.7613 | -54.0941 | 2026-10-07 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 267.3 |
| dc47947c-6cfc-379f-909b-aca3027d0470 | -8.7033 | -45.2289 | 2026-10-07 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 15edfce3-1e8a-3bdd-9cc4-45fbc82377db | -3.4762 | -50.0883 | 2026-10-07 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 719406de-152d-336c-abcd-8c350078e1f6 | -8.7039 | -45.1832 | 2026-10-07 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 0e54ab3d-a0f6-3981-832e-6aa5a3fa7001 | -2.9448 | -54.1501 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0346180f-1abf-35ae-b95a-f1f09ba8dffb | -5.7187 | -45.1773 | 2026-10-07 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4273beb1-cee2-3d49-8b95-97e49b4b0b56 | -11.2333 | -44.8678 | 2026-10-07 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 567c264f-c412-3f3c-a885-9c1d78607f30 | -11.1047 | -45.7119 | 2026-10-07 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| eeaad8b5-2e0b-3211-8d58-860684b39e62 | -3.5515 | -59.4807 | 2026-10-07 02:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ef29b6b2-2c9b-3e48-b03c-d68eda46bfe8 | -15.2511 | -43.2743 | 2026-10-07 02:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 72.6 |
| cb205c14-eef2-320a-ba95-12e15d6a2c8f | -5.7374 | -45.176 | 2026-10-07 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 873b1a76-da47-3f9c-9aaa-1af03b44262d | -3.6579 | -60.6412 | 2026-10-07 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 47869686-1335-3f58-8ee9-3a184c807c1a | -3.0913 | -54.287 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 99c291a4-e71f-3d29-bc55-65734019360a | -2.7796 | -54.0937 | 2026-10-07 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 210.8 |
| 47dc919b-1489-3913-ace2-78ca7df5a660 | -3.1115 | -53.7637 | 2026-10-07 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f787ad90-567a-337d-bbec-5d78860d9a6d | -3.073 | -54.2674 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ef9d98cb-8af6-3255-9bdb-e122fa388cb8 | -11.0137 | -45.4501 | 2026-10-07 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 1df70a3e-9131-3192-a2bb-151ae8af7b6a | -3.0184 | -54.1282 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f36f45d5-7152-3bb4-821f-d36910a91082 | -8.7228 | -45.1812 | 2026-10-07 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 69db5fec-ccb0-3514-a70c-ace0004bb540 | -11.7335 | -43.649 | 2026-10-07 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a28f8b23-2d63-315c-9ac8-08d8ca57af2a | -3.2728 | -50.1372 | 2026-10-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7f017ad2-676e-3e88-96fe-c3d5910cfa7c | -3.0914 | -54.2669 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| dafcee95-fc0f-37e9-b6d7-42ad9d8452c0 | -3.0 | -54.1287 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8d19419d-761e-3e4e-8867-76b425432441 | -3.0913 | -54.307 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e1cdf5dc-dd62-3327-b764-8a7d0c14bd91 | -8.7225 | -45.204 | 2026-10-07 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 269.0 |
| d1d643de-a891-3b06-a2c9-ef026ada4ba7 | -3.1097 | -54.2865 | 2026-10-07 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3932ed17-22df-396b-9779-1276a99e24a4 | -3.0375 | -53.9066 | 2026-10-07 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e1ecc39c-4a6c-3a1c-8c50-32cf292bb7bc | -3.1787 | -50.5597 | 2026-10-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 036e1537-9382-3c6c-85a8-5889ecfb0385 | -2.7796 | -54.1138 | 2026-10-07 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 3fba1bbc-e93a-370e-a919-251eadaf0421 | -5.7189 | -45.1547 | 2026-10-07 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 97a9f18e-82cb-3332-afd0-1e0b0aff2eff | -3.1787 | -50.5807 | 2026-10-07 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 49474451-0f2a-3189-a18e-19eb0c8e8ae2 | -3.1114 | -53.7839 | 2026-10-07 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b2dbb94a-3c9e-3814-9291-9ed1acd4569d | -3.8566 | -55.9967 | 2026-10-07 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 4cc5d639-60cb-30d0-86d5-2abd013ab1b5 | -3.0731 | -54.2473 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 69766922-c9b9-3f46-aaee-4a86233174e5 | -3.0184 | -54.1282 | 2026-10-07 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5699c871-6a0e-3ded-8b8f-ad4b7fbef6e7 | -3.658 | -60.6222 | 2026-10-07 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ae89574f-39c5-32ec-b3b5-3c2e06f0387d | -11.7966 | -46.57 | 2026-10-07 02:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c7a8f2b3-1f4a-353e-8bff-1d5b1a31dcfa | -8.7033 | -45.2289 | 2026-10-07 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7a9d89dc-d12b-3704-a864-574b74e4d3b7 | -3.1787 | -50.5597 | 2026-10-07 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| deb86d21-89f0-3c60-827e-2e9a3dd9fe09 | -2.7796 | -54.1138 | 2026-10-07 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 274.3 |
| 8e63c0ff-8492-3c0b-99a1-94509d1f5f1c | -5.7189 | -45.1547 | 2026-10-07 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 30debfdf-f3ba-3022-a9bd-4c458c91c9a5 | -3.8567 | -55.9769 | 2026-10-07 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 76a2496a-0fb5-3470-8c34-83025ca996b0 | -2.7613 | -54.074 | 2026-10-07 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5261eedb-2737-3d61-b40c-8f84c570860b | -10.9949 | -45.4298 | 2026-10-07 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 6e778f8c-7d4e-3b85-93e1-a97442f73ac4 | -3.4762 | -50.0883 | 2026-10-07 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 90ae7a43-3d09-3da0-8099-b6ff0443a460 | -8.7039 | -45.1832 | 2026-10-07 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a3a01497-5330-3570-8c42-84e78b0bffe8 | -3.1097 | -54.2865 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cbcfece6-6505-333f-9a26-23ef8b51e064 | -8.2865 | -50.2731 | 2026-10-07 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| ce8bb8b3-a032-3ba0-8987-4df71662cd4d | -3.8566 | -55.9967 | 2026-10-07 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c1c0f4d2-955d-3a40-8691-1b3e750d6360 | -3.073 | -54.2674 | 2026-10-07 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8f0c0a96-8619-3949-82b0-5982df7d5c73 | -11.7335 | -43.649 | 2026-10-07 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 90fac4d8-b248-3568-882f-c994862ae391 | -3.1115 | -53.7637 | 2026-10-07 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| dc139576-b6a1-3ec3-b97b-fd1e2b7d9d49 | -2.7796 | -54.0937 | 2026-10-07 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 232.6 |
| 84dc4fbc-ddf9-3c57-af49-80dacc2d6dfa | -10.9953 | -45.4068 | 2026-10-07 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9d089ee6-da2c-32c5-bef4-fe3dd270ea2e | -2.7613 | -54.0941 | 2026-10-07 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 319.8 |
| 2c773da1-a317-3a13-97a7-3e3226760d0d | -2.7797 | -54.0736 | 2026-10-07 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c8b9eb19-0b83-35d0-8b74-578745f7c394 | -8.7036 | -45.2061 | 2026-10-07 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 286.4 |
| 0b921ff4-94b9-3227-98f7-1eaa6239a161 | -1.801 | -57.1161 | 2026-10-07 02:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f61eda5b-0fb5-3866-8bc0-332e28d534a8 | -3.6579 | -60.6412 | 2026-10-07 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |


[Clique aqui para ver as próximas entradas](README29.md)
