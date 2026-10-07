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

## Dados Diários - Página 225

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a421b0f-b568-3bfe-9cf4-f7072b4a0a34 | -2.70757 | -56.53706 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3d96d6ce-53ec-31b9-8a97-2fec8ee6c582 | -3.36222 | -53.53526 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b62bf30-a236-3ecf-aec0-ee391fd5088f | -4.78431 | -55.72728 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 9b95f5ec-d05e-3b4b-ada4-40b3589c659d | -3.5648 | -54.21968 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3a0b886f-c14c-3fdd-9d30-a88a19459e98 | -3.8429 | -55.98294 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 9ac53e38-2ad8-3701-b8e8-f5e8eedfda89 | -0.81257 | -49.17919 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 12381956-e24e-34d0-9943-78e5e2bc200a | 1.75735 | -55.5769 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dbcd5e36-0dc8-3ab3-96bb-0f4fb70e53c6 | 2.27656 | -55.94927 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e64ceaa8-8d26-3e53-b064-95dfbed071a7 | -2.49369 | -56.23787 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b5f26b1e-f076-3ba1-b08e-8a3dadc54095 | -0.80881 | -49.17976 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8e8bbdef-b461-3e23-ab44-9b3b159f882e | 2.00714 | -55.84898 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5af502a1-df2c-3d3a-af84-0ce6e76419c0 | -3.25399 | -44.6836 | 2026-10-07 16:39:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdb5fd6f-e777-3c10-b4dc-9e912c1cce61 | -2.33632 | -51.99082 | 2026-10-07 16:39:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d271d5d0-2eb4-3adf-a752-bfa0735c059b | -3.06968 | -54.24874 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cde9b95b-d9ed-3fbd-99bf-5d4e9cb0b828 | -2.7612 | -57.6675 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 6128b3fd-ebb0-389d-8e30-242045680e30 | -2.48865 | -56.11215 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f276e4b6-041d-3da3-bcf6-3c126a140294 | -0.80062 | -49.17638 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2697a836-a79e-3370-9e70-68ccf20b955c | -3.27567 | -54.0447 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 305be2a9-5f87-3b18-b21b-2fd20eccd66b | -3.08367 | -54.26816 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7181ff61-2cc2-3dfd-8921-e4fa2417ed11 | -3.44104 | -56.93436 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ef39b6d0-7735-34ef-838b-6a54b6300580 | 1.86723 | -55.73069 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b1e6a9c-cb35-3c0b-8c81-9b87334dbe9a | -0.22319 | -48.96718 | 2026-10-07 16:39:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6c8c4124-5d54-303b-8e60-d986d7c6f6c8 | -3.16639 | -50.59688 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d3c6a7d-4ef8-3477-b2ea-4143257ab0cc | -3.21778 | -53.96262 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0ad32dde-e101-3055-a7d7-38b0a8eef300 | -3.04218 | -53.94435 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b0a7365-8d24-3340-8e2e-35d76b1bf61b | -3.10514 | -54.14827 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 19f8d672-d9b0-33ae-8815-d7cff1ad34f2 | -3.53721 | -54.63448 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f8ac419-7abd-3641-a87f-7e21f83fdf5a | -2.79451 | -54.09924 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5c85dc2c-5a89-31ae-9bf7-5e9d8e71c298 | -4.1166 | -54.42283 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 23d589ff-f566-3822-8422-c19f2d5180f3 | -3.00727 | -57.90764 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2159a76f-b660-37f4-ab22-9fa365ea31b3 | -2.5671 | -50.68315 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 767978b7-90ad-3337-b214-071f0f2a7c7b | 1.35043 | -56.13113 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 793ea23d-c86a-3b38-a6f1-506ae6d2f0f4 | -2.48752 | -56.14585 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 896a4cc5-6ce9-371d-8595-5b3a5cb68046 | -3.4412 | -50.62753 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5c2f3ef2-3fe2-37d5-ad57-9c59ebff80c3 | -4.36416 | -56.23034 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 44dbe357-00d0-3eb7-a4d5-eb6889814e01 | 3.40241 | -51.30313 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd19bb93-0a90-3c8f-b473-be585c9a1a11 | -2.93431 | -54.17396 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97a7cf1f-a4cd-3084-b60d-c5a193f1324d | -2.93241 | -54.11023 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cbb806e4-2b80-3ddd-ad49-1a8875c72628 | -3.93784 | -54.57896 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d444672c-5dff-3e20-93cc-62065ddc63df | -0.59971 | -52.05866 | 2026-10-07 16:39:00 | NPP-375 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15ff37ff-58a3-343c-b994-79606ab3da79 | -1.29098 | -54.56221 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e24bd27-a07c-3c8d-b016-f6ba7b6f8ff2 | 3.21204 | -51.32431 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ae65822-5488-30da-a817-02f89409c58d | -3.2276 | -53.88233 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b97869af-72cd-3fc7-81c4-b6580b8fcdd9 | -3.21057 | -53.87806 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 2c40d41b-3d8c-3996-a908-48c9bad18dd8 | -1.2799 | -55.86673 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f7f36c8c-3c24-30c2-a482-77f60232afd9 | -2.55418 | -56.43585 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 33e968e2-b587-30e7-8f97-bc96cf177b94 | -3.57064 | -54.49155 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea7ee8fa-3bb3-31c1-b7bb-3e8c3b0cbded | -1.88697 | -54.38638 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c77b869d-07cf-37ba-ab21-5b8681a76aca | -3.46784 | -50.08127 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6b54318b-740a-3fe9-a43b-2869330555ac | -2.63597 | -44.31078 | 2026-10-07 16:39:00 | NPP-375 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4bb918e-bad4-3a89-b9c7-cdbcdb244777 | -3.47113 | -50.10334 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73ed1098-9edb-3bb2-a003-349c48a8a391 | -2.99428 | -51.05444 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f1221f1-3917-3822-9371-772e8ed9d11c | -1.41807 | -55.42429 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6a73907a-1a95-3f86-80d1-255dec8653b6 | -3.523 | -54.65545 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ed1ef2cd-41ff-345e-a2cf-558cf3be18f6 | -3.26559 | -54.66768 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 105b6f16-7844-30c9-8956-71098c32232a | -2.97161 | -56.62553 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d1ee2644-a37e-343e-a0c8-2a02fa991630 | -3.35859 | -50.47356 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d936fc61-ffd7-3c2b-848e-e56ec9ea1711 | -4.162 | -55.15237 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8f6e10b7-4b25-38d9-9828-f354a9811072 | -1.21032 | -49.03272 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9b9ef684-a79b-3ba5-a29a-76ade5a0acbc | -3.29828 | -53.86215 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 320b695d-ece9-3667-aea2-c0800755bd87 | -2.78881 | -57.62094 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 099a1161-a31f-3943-85df-1ceb975e0222 | -3.67477 | -55.94334 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 018abdca-f281-37c5-a794-99a0053d2869 | -2.56043 | -56.43487 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a859801-c392-3c7d-a084-865db15a3127 | -3.96962 | -55.8284 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f250946b-0542-3b1e-84a9-9c767333dfd9 | -3.19056 | -56.85065 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6e696d83-7063-3d81-8cf2-a4854c024e58 | -2.85127 | -54.13676 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86d435b0-e543-3a18-99dd-2fd060c4ae24 | -2.7743 | -54.07441 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 29cdfe59-993c-30d1-936d-6b7457289b70 | -3.44649 | -56.93619 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 230.2 |
| 2d380656-959c-3ca7-bf6a-ac02415df238 | -3.59352 | -55.56641 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6dc7a184-8483-3d7d-9e47-ccc5425bbb0b | -3.1002 | -54.15241 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bfd5cf0a-c6f2-3b2a-b892-74e9a9638a27 | -1.13591 | -57.06128 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63735692-4074-3687-8e1c-b3c18f27ba90 | -1.03262 | -47.91428 | 2026-10-07 16:39:00 | NPP-375 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6488431d-ae96-3d66-8b32-97d0b1893127 | -2.54581 | -56.42227 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4a70e93c-6b91-36d2-be3a-a97a9fa27cc1 | -2.1172 | -46.38904 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc86dc90-e309-3d07-b7af-09f49323a0fe | -2.94172 | -54.06017 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| fd07ab3d-5ac3-3420-9977-4565193d1127 | -2.72264 | -43.57634 | 2026-10-07 16:39:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab9381e9-f03a-3a68-8742-1e23f3c07165 | -2.93701 | -42.86182 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c74dda21-ac60-3e1a-9430-7ae9e803a991 | -2.49296 | -56.1459 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 47e9f21f-2a11-3476-9b39-2fb3e027b25c | 2.22281 | -55.89053 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a46e25e3-fb78-31d5-b695-553441995510 | -3.51679 | -54.6525 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4f3ead77-b6a8-3b2b-9594-d844bd1eb271 | -3.32218 | -50.17894 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf7705b3-eb40-34a4-9bc0-291e27fdb297 | -3.17677 | -50.5591 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 94c75802-82dc-3aec-a333-6b97fa84a8d5 | -1.29552 | -54.5657 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4bd62b42-8837-3ba7-bb14-93efdb1acb90 | -2.61236 | -57.57828 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fe381fcb-8de7-3fe0-bd60-88fc9a1565d3 | -3.28166 | -56.98129 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 46f50ee0-c9a3-35da-9aeb-1cf0854da3a8 | -2.76706 | -54.09983 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 27ddfcb5-ac23-347f-9921-b79f41b0f2ac | -3.01171 | -54.12324 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6dd4d551-d20d-3e19-8148-25dd8c2c9926 | -3.4334 | -56.9379 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 995dde3e-7087-3554-af72-faae466e85df | -3.04023 | -53.93098 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd58e7c1-c74f-386d-ad5f-0604c0668d9d | -3.84218 | -55.97805 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| bc52f2a4-a769-31a9-a41a-3a2b6fa9a076 | -2.79248 | -54.08567 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 500.7 |
| e1a540c2-42ed-37fa-9437-08c0451ef57b | -3.21322 | -53.87792 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5551c26c-4452-312f-b0e8-fe0918723806 | -3.65612 | -55.50512 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6eda98b1-c94d-3d21-a8fd-983c13bfb387 | -3.08315 | -54.26461 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8857a89-af74-3b5c-adbd-954277e9bb85 | -2.77379 | -54.07103 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 51bdfb1d-3d10-396c-8fd0-ce4aa1d52214 | -3.51349 | -58.59948 | 2026-10-07 16:39:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3951ac64-7657-3a37-8818-a5dbe7e36ec7 | -3.27225 | -54.05921 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| ca687db6-ee1c-32e9-9fde-0d4848e9a19b | -2.82371 | -54.09886 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5f74a1f3-1c18-3230-8c84-f3add4d7a68c | -3.05384 | -54.14539 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7c31d8c6-d6ed-36ca-a09d-6f99be7b21f2 | -3.0787 | -54.27254 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README226.md)
