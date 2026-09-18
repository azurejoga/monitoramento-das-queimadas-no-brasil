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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70ca977-3ec3-3646-a787-c3297668a310 | -4.48686 | -54.97862 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77eff4bb-2811-3459-8d41-825da8163202 | -3.26744 | -54.26527 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1330283a-bde6-3b69-a728-8c0091ca7e1e | -3.96792 | -52.18763 | 2026-09-18 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27759d8a-a7d4-3c8d-95e6-41b443b6a75a | -4.58615 | -42.95932 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9325301f-1cc6-396d-aa59-4a4ce9a60545 | -5.33641 | -45.14631 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46dae5f8-4bbd-3d8b-92e1-4246be8c2eb4 | -2.96586 | -50.32561 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 414e4098-0c79-320d-9e46-8a9fefd099c0 | -4.56346 | -42.94502 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d006e29f-1ce2-32c8-8524-e71d3363a3fa | -2.86698 | -49.62544 | 2026-09-18 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d240b8f9-75c3-373c-a863-66e34702b1ad | -3.3076 | -45.92773 | 2026-09-18 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96114810-7543-3493-8b9f-5b9d080d8cf6 | -1.70955 | -54.88542 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f082ff02-14ec-314a-9ba1-d24b9f7a23ae | -2.96367 | -50.33942 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b57de0dd-6e32-3d91-9029-519b383e68be | -2.81382 | -50.47094 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5f6f6e7-df04-3832-b13e-263a66cd8bbe | -2.70387 | -57.60276 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4f6c3d1-0aa7-30b7-850b-81d3fbe5ee9f | -3.3769 | -50.4649 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b73306e7-f754-30db-8057-aee65a45a1c2 | -4.61688 | -42.83253 | 2026-09-18 04:55:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 480a3c0e-6b9f-3f1f-a8b2-99364198ab01 | -3.21048 | -53.94699 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9744e8d-4f18-3b11-95df-417f3910b480 | -3.70707 | -54.17644 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53c08151-7877-332d-b91e-76678e3f52ad | -1.03647 | -53.73796 | 2026-09-18 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f74f197-d78a-34db-a531-10a82a860e55 | -3.33234 | -57.85142 | 2026-09-18 04:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79e4d875-783c-3278-80e6-4d9a613f4a3f | -2.89682 | -54.17211 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5816e97a-9bd1-3c59-b8e4-7dc9798ed4b1 | -2.79177 | -42.47783 | 2026-09-18 04:55:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ccc91fa-763f-3348-bb83-ab582c56f7a1 | -2.80408 | -52.08261 | 2026-09-18 04:55:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9d0c9f2-fb42-3eb9-b14c-62638aef4d7c | -6.40978 | -43.46519 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8c5c6cf-eb07-3a8b-9bd0-f51af4316a06 | -6.1178 | -44.02985 | 2026-09-18 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c1c1ce06-aaa7-31e9-aa4d-17116a932a34 | -3.37413 | -50.46092 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 873a0cea-ccc3-3dbe-b052-e373299ec0e7 | -4.57057 | -54.90401 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cccf2f17-04b8-3b1d-8a67-1e6b29a7620c | -5.74189 | -44.39257 | 2026-09-18 04:55:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94192006-37ba-3da4-a423-46809dbc9c3e | -6.13098 | -43.74341 | 2026-09-18 04:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cdd9ba9-fd89-3dcd-ac31-10f028e7bceb | -3.44661 | -58.19891 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a9e81c8-b492-3e95-af30-4ded2c710b72 | -2.96809 | -50.33304 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62330fa5-b8a5-3cf9-b4d6-ab875bf83c3e | -4.47991 | -54.97242 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fe6d68f-ea80-3eb5-b2c2-3a32e78aed91 | -5.63181 | -44.80366 | 2026-09-18 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f73e52a-f290-3e8f-8c26-a99929171ed5 | -4.57643 | -42.95794 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5fd28094-ef0a-303d-8bca-0de61977b0a0 | -4.43314 | -55.52822 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38a92327-9139-3fe8-957b-9dc65e6a0610 | -4.43428 | -55.52128 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b15d3445-3dcf-3491-b66b-e27978a4b50a | -5.75744 | -45.09824 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fca0fbb4-c20d-3554-b25a-907aab666505 | -5.42909 | -43.44354 | 2026-09-18 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 962599ff-f166-386c-90b6-38523bf4f90a | -6.11707 | -44.03479 | 2026-09-18 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e94fe75e-1e99-35af-92cc-e35c17c0ebfa | 1.28505 | -50.87531 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27268533-0b9b-3596-b32a-197d8f477400 | -5.7783 | -47.29526 | 2026-09-18 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a35f5bfa-88de-3187-9072-f86f562fbb28 | -5.62265 | -40.85902 | 2026-09-18 04:55:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d2bab1a-37f6-3ca0-9d56-c6a2632d8300 | -3.96778 | -48.12652 | 2026-09-18 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6da70b1d-2b34-3015-abbf-edda93cbf2fa | -2.82189 | -51.33795 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b0e4070-3442-3323-a51b-84c6354a281b | -4.43023 | -55.52081 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78d57c82-c7f4-39e1-89f2-7bfbd8a8acce | -3.92363 | -55.92591 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 014b29c7-eeeb-3ac9-825d-dc4503079c70 | -3.37523 | -50.45401 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf9c923c-ef57-333a-8711-61b33d9f4baf | -5.33332 | -45.14305 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3d3e2ff-cf1d-37b0-8451-0c6b4f962697 | -4.56752 | -42.95111 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 87d32285-51ea-31b1-9682-9b9d5c4dcec7 | -4.43833 | -55.52177 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7facfe6d-8ede-356a-825c-5fa409cb4c84 | -0.78127 | -47.55144 | 2026-09-18 04:55:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cbb5140-a4c5-3105-8a67-5d70447f8871 | -4.54207 | -54.93306 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d6561db-3dfe-3a6d-9b1d-276c3e3fca6a | -3.36803 | -50.45642 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 898cbe85-fc9a-3a3b-9509-c435a14b0ef1 | -4.427 | -49.187 | 2026-09-18 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10539f3d-66c3-3e17-9701-d631bb3ffc57 | -3.92278 | -55.75059 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4786aab-95b9-328d-908f-03a693d54c0e | 1.33283 | -50.60624 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 977cfc86-b0ab-3d72-9e10-6e6e5de6f6ef | -2.63306 | -48.43031 | 2026-09-18 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7df564-5364-351c-bc69-fffbdcd4e259 | -2.96754 | -50.33649 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b7374d6-7203-311e-bb6b-79e10327f4d4 | -3.35861 | -50.4514 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd104ce8-670d-3c4b-acc3-a6cec997941c | -2.89913 | -54.18186 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6f9908d-33bd-3ba2-beeb-caac4d9c9322 | -3.26819 | -54.26068 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 884a3cd1-f05a-3024-b2d5-9ed667bad9c7 | -3.25215 | -53.08588 | 2026-09-18 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43c57b0-f29e-3ef9-99ae-4ca63a353aed | -3.08357 | -48.67059 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 310bcadf-525f-3382-8c0e-175489fc9a90 | -3.70314 | -54.17906 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d51662f-a4e5-3b66-9ea3-44f0785bd99e | -3.33881 | -53.26428 | 2026-09-18 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d0efc6b-8c06-3b51-933d-6b78f528f7c2 | -2.61496 | -54.75204 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 321cac66-0951-3496-a762-014caf679b9a | -4.57319 | -42.94641 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a3b2fe81-84d0-3134-9f8b-8d337c1c8501 | -4.35989 | -47.78185 | 2026-09-18 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d6d5c45-fbe6-3bfe-aad0-5cde79893a66 | -4.58128 | -42.95865 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cd25e1c4-a3e8-3e6d-9bae-e7a4ce821947 | -3.37136 | -50.45694 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f70a3d4d-d87f-3c35-8a64-a34c348f3d8f | -6.37832 | -42.79765 | 2026-09-18 04:55:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a5d9b32d-7fac-3034-af6a-1438005181f7 | -5.75318 | -45.09756 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db12039c-87af-3eb7-9384-cd7d5cc0fc98 | 1.33002 | -50.61033 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79fd3017-7f1d-32c3-bb21-c7396fb4bf75 | -5.75803 | -45.09433 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c2c896e-48dd-3ca8-8322-456058b16c42 | -2.67841 | -57.60893 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4dddbc0-60b3-36b5-b1ee-380df65a1f23 | -4.43079 | -55.07841 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 680de6c3-5233-30c8-a34f-4dd8d08a7520 | -5.14403 | -47.6034 | 2026-09-18 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1aee6f8d-47d0-3ab5-bf01-430caf9262e9 | -3.46807 | -54.69668 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21b7009e-001b-31f0-90f7-df9e36a3ff02 | -2.29888 | -48.57753 | 2026-09-18 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6adb91bc-ac4d-36d9-bd1a-af78d725dac3 | -5.1282 | -37.71354 | 2026-09-18 04:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e2d0949-f324-36c6-b029-4b1b9016cfce | -3.26668 | -54.26985 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8b50d288-5a26-329e-8aa1-392b7c16cf94 | 1.33226 | -50.60267 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 164304b1-dade-388f-bc78-8b7458e0802a | -4.56266 | -42.9504 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 763d462b-e89a-38fa-b764-33cb794ee049 | -4.58209 | -42.95331 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b496c314-1a17-3532-9f57-75be58b400c0 | -4.42965 | -55.52433 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a2aeb63-4a4e-3dca-a338-836b64581817 | -3.38132 | -50.45851 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbb35872-c941-3dd5-99ce-23b4b47c6894 | -3.91924 | -55.74646 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bdae2f1-0bb4-376f-8edc-476d37e653c1 | -2.90135 | -54.16813 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c96ff39d-9a54-3766-a583-b4dbfc2f5191 | 1.33507 | -50.59858 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07276172-1149-3b56-9f6a-996439806915 | -4.5844 | -42.95452 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 82b59c8f-99eb-3488-9ce8-4c0909e090e0 | -4.42616 | -46.29574 | 2026-09-18 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fae026c7-5b68-3dd0-ad9c-ed76ffea3f1a | -3.33523 | -53.26371 | 2026-09-18 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3d205d8-ff13-39d6-b7b3-0eff87ff75a0 | -3.37855 | -50.45454 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b01e1dc9-197c-3ebf-a8b0-0af2502a583e | -4.53431 | -54.93191 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f82fb5d9-cab2-3adc-9c81-2cedbcd87c6b | -5.65654 | -43.38618 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35afc0b4-f650-380b-b071-ccb8e66bb4b9 | -5.19221 | -49.33392 | 2026-09-18 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dda746d-b6e6-327e-b54e-bac4e3c53086 | -3.3719 | -50.45349 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0994cff3-654b-3c7a-96ac-6ae84c538f83 | -4.61551 | -42.83151 | 2026-09-18 04:55:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 967f2a45-da26-3d5f-b557-8c85451abb7a | -4.30134 | -55.72695 | 2026-09-18 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87e090df-a454-3664-94e1-910f6635bb73 | -1.70497 | -54.88827 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5dfc44c-0902-3f7a-9102-ea62a8808c6e | -2.96308 | -50.32164 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README57.md)
