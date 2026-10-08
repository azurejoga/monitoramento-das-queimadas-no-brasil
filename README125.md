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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7202dc-3224-3525-abab-66d72b3d1825 | -2.93325 | -54.17425 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3942d1dd-6013-3d17-a876-d0daf6e58dcc | -6.46551 | -55.47541 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d0c6628-975c-37f7-8c68-7ce96187106a | -3.19148 | -50.55229 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9444bb9b-2ecd-3270-95fe-7f92a9e8c049 | -1.36413 | -56.92485 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc7f0c68-4a17-310e-a742-6addaec3c804 | -4.44705 | -54.97929 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40b2d09-3351-3f02-9ffd-cfa55c46b5ed | -2.30593 | -58.11128 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0bf25fb-f4f1-3743-8292-761230930e0d | -2.89869 | -54.07419 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9410de47-fa33-3571-bc6d-f4c490d115c2 | -3.99596 | -56.24932 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0b3da4f-9c6e-3cfd-b3f3-9789071b0801 | -2.40198 | -51.30801 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75ad780-9c48-39b6-9724-80c507b7c9a2 | -1.46564 | -54.51913 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1fc497a-5993-3efe-afd1-dd78937e308c | -6.95328 | -45.26501 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72f0efd3-3a0c-31e7-a6e5-73735a949c51 | -3.26713 | -54.66784 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbc1434c-511b-353e-87a8-9e663ac22724 | -2.48297 | -56.10408 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae85c5a9-4bd1-301a-8e41-2620f8eb38ab | -3.09655 | -54.28469 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e47d611c-022d-372e-af35-ea3d1000af2d | -6.05527 | -59.94593 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07491854-a3d7-3e9d-a128-d8cb3b6f351c | -3.20436 | -53.87125 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99b62861-18b1-3199-99d1-e2b54400831c | -8.64892 | -67.17388 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f769ada5-987f-38e2-be5e-9c37ea66173b | -2.5802 | -56.17229 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 223b23f2-2846-314c-9080-2c9457d14fbe | -3.63162 | -55.27973 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cc18904-b050-3e5c-bb78-cd1220580a9d | -2.48688 | -56.12241 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2508db63-c930-3852-ab45-1e7b635bef7d | -11.34491 | -51.87573 | 2026-10-08 05:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c007f7c2-8e9b-33b7-9f21-0fec54cc8464 | -10.88471 | -49.14997 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12c77767-acb7-33d0-885b-04c5edaacea5 | -6.02892 | -51.73006 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72773ef7-1891-358c-a683-45c905cba6cf | -3.85211 | -55.9844 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb6fc138-6d24-3e77-a6e1-eecd93349f57 | -3.38217 | -59.43143 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8c66f1-ab62-3f92-b0ce-578dbd0de023 | -3.00738 | -51.12304 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a586bd7-4de7-394b-b4e6-084c084f0c48 | -3.89896 | -59.44751 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ccbf4fd-6b9b-382a-adc1-ec4931578a3c | -1.51933 | -54.53101 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53909c35-eaa0-32d1-965e-be010723e281 | -2.57077 | -56.16726 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87cd85e6-deee-3445-b320-219e9316653c | -3.41899 | -59.57777 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eb3307e-22f7-3135-825e-7445d46e8937 | -2.57906 | -56.15794 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c4ebc10-70ad-3d68-aaad-00bb012056e2 | -3.16553 | -58.62895 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 719b728d-8443-3207-a542-32fb872449c2 | -2.90522 | -54.19342 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16fb84dd-84b9-3fba-af06-a07d8d1861d9 | -3.29732 | -54.03813 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c8c3132-15fc-3bbc-bcbb-3356af2fc92d | -3.04487 | -53.87629 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93682507-753a-3ee2-aced-58d968fbbdd0 | -3.15784 | -58.04605 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc641483-184a-3e07-a132-39e930ea57d0 | -4.00516 | -55.30363 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2386a18f-3d66-394d-a45e-5d020ab6eec9 | -3.29807 | -54.67265 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7e37018-52be-340c-a1dc-0111f64072cc | -3.13894 | -51.0276 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cf91504-7b58-3356-a249-9a59ce3b6bb5 | -3.6007 | -61.64385 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a4c9c9c-c49d-339c-9e3e-aa38d45829a2 | -2.50684 | -56.12553 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b83899-131d-3424-ae9f-da7b24eeb61e | -9.05201 | -65.91943 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53713a1b-a404-39a8-8d20-95e22465c3cf | -5.69311 | -53.47905 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d2dfcbc-c6f7-3d41-b821-e6ff925e8afe | -11.97426 | -57.60878 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7484d889-ef45-3033-a699-aea47db2dce0 | -4.29838 | -54.80815 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1b52df1-66e2-3fb3-a8ec-58746387ce0d | -9.11593 | -65.35259 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b7fc3ad-419c-378e-836c-09ea1f7f536f | -3.18525 | -50.56387 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c073322-5a8a-39eb-a7e9-603aa25bc49f | -3.14509 | -53.72454 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6b289ff-f3e7-3693-91db-028678c58a2c | -3.27678 | -54.03097 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40951d7-0413-3fe3-a9de-caa633b39b49 | -4.06694 | -59.83567 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 022e6ff9-d0b4-3237-955f-70bc3f0f25f0 | -2.95329 | -54.13794 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f508b52f-d536-3cec-8f8c-6b76e8ab7e88 | -2.98161 | -54.12243 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cef1340a-e286-3e16-8cb6-f6da8d9ff3e8 | -3.97571 | -56.11782 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8350f4a7-ad37-3a5d-b14d-b40c3c4738ed | -6.93259 | -43.65953 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 19aedacb-7a0b-37e4-a290-7a42f07cb022 | -6.30402 | -54.7878 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d31251cd-e929-3e9b-975b-dac56bfdf259 | -2.89804 | -56.6687 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c538890-02f0-3797-a3f6-20801a8f5df4 | -3.29488 | -61.00959 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f079fa1-50fc-3da6-8c4d-101f8a061810 | -1.10895 | -54.14951 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e23ec02-ca19-3788-b7b4-9810e5ba008f | -6.10362 | -55.71751 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeef6969-2fbb-3d6a-b656-1ec51fd93c82 | -2.50853 | -56.13643 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83bfcb0c-2d55-395b-9876-75d962438569 | -7.50352 | -54.99656 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f8d6fa3-a172-3d76-b846-2d758dafd8fe | -8.62321 | -67.02763 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 09dbf40a-650f-3781-a018-62f6a6f1474a | -2.73788 | -57.61333 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d906f7-9883-3c22-ad0f-b8d7e7a01d56 | -3.72788 | -55.97586 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d662dfe-6fb8-3657-b47f-af58f0d7ca41 | -10.83285 | -57.20796 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21cafb78-52d4-3434-991c-d0ce1ed23ddc | -6.22179 | -52.87728 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d77ae4c-5e2f-3db5-841a-1f81344d4e18 | -3.27846 | -54.04326 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74125578-6148-3d03-857f-24e8e201f1ff | -3.50492 | -54.66589 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53725f0a-54e5-32e1-a0ce-1911cde9945b | -2.86691 | -54.16385 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d7df865a-faa4-3d14-b676-7744c1665f11 | -4.29098 | -50.77891 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe6e9290-5da2-3809-b53c-b5c90aff5c8f | -3.01484 | -53.90835 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4c20aca-5b1e-38a9-b0d6-3c75e93cf11a | -7.40466 | -55.15063 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8fed947-6d40-3ce2-94c7-9f371ef9e8b9 | -3.56284 | -59.47103 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85d1dc91-6e14-35b2-8b81-37425e51efee | -3.0535 | -54.21247 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f48ddd44-b4b4-32d4-859d-f33930e04c65 | -4.98453 | -56.22186 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee342328-b0aa-392e-9eb0-a6892e8d7ebe | -11.80948 | -47.34954 | 2026-10-08 05:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6d6873e-c0ee-3d2c-9842-0b79fdc0e29c | -3.27325 | -54.03043 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2932b76d-5033-34ab-bf18-f604bd138cbe | -3.01572 | -54.0644 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| febd2147-1a22-32f9-9244-1d6b5727fba6 | -3.1644 | -54.72458 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfd04414-1117-32a3-b02d-63c6e38ebce7 | -3.40108 | -59.58881 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae91ca37-06c3-30d6-9f47-f960356b1b7f | -2.78843 | -54.08977 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6183b0c1-4d2b-3195-9ff8-841e27470457 | -3.55598 | -59.49063 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fba79bd-f462-3c16-a19b-b1a03b4fcd83 | -3.862 | -58.64521 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e214f4c-d42a-31ae-9275-3eb6071a332b | -2.86483 | -59.30862 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f0ddcd0-3383-3c04-9e0c-1582ea682b83 | -12.09886 | -57.15962 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f339bc86-0655-3812-9379-63109185f653 | -4.06332 | -59.83509 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84a81cea-ca20-3cec-878f-b4408d5f690c | -3.96739 | -56.12723 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d535e8f8-d02f-37b7-849d-ccc5c28c9a1b | -3.27433 | -54.04662 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e9da238-fce5-3230-a55f-7b4e3be0a217 | -1.19391 | -54.13908 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba29686e-d4a1-3933-9479-ebf3a5a11864 | -3.2679 | -54.0416 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74226cc6-3b64-37a8-a71e-74ce32c8b22e | -3.11779 | -53.78185 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16d2b522-a1bf-37ff-94f0-634c944ae67d | -3.20562 | -50.55277 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 35821e12-e4ed-3ad9-a7b2-9520f07759a0 | -3.05342 | -54.03035 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11e108bf-1e21-33c7-a849-c09b3c418e33 | -3.47047 | -50.08091 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09583f98-4269-39b4-bd43-7456684c0d32 | -3.23429 | -54.32474 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f623633-e8df-3d95-97cc-0defa2793d80 | -3.53969 | -59.50045 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab1e2c85-7aa2-3806-9100-281d8be851a4 | -3.10215 | -54.17959 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7a07023-c746-395a-9f55-5f58d31e9fef | -2.76737 | -54.11013 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1910f001-38b1-3b08-85af-e727eae5ae79 | -3.03244 | -54.23274 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efdc84e6-79f1-3a26-9d9e-31304bcc5763 | -2.48857 | -56.1333 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README126.md)
