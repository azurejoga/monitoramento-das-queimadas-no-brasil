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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24fdad6d-07ca-3a4c-98dc-9024213341d3 | -6.19966 | -52.78406 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 886e7ad2-fb32-370c-ade1-7530e08612c1 | -3.30084 | -54.03867 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cff18c5d-44cc-3974-b836-53372ef4bc58 | -3.17212 | -54.60808 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6639835-9c49-39cc-84a8-99f59f0d950d | -2.77443 | -54.0876 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ce58fb5-f17c-3314-8af4-fa5e5cd7477a | -3.66813 | -60.62506 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 551fc2ed-88b5-3b8f-9338-cb8f4df1b6c8 | -3.09975 | -54.98048 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629553d6-02c4-3a5f-a372-d6e15f69a706 | -3.52911 | -54.64678 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9094518e-e209-3ea5-8957-a9e2d2712097 | -2.54962 | -57.39196 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acf4370f-6282-38fa-91cd-7a0874c7181a | -5.29048 | -60.09056 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2e64761-8e80-31fd-af3c-2bdc1ea56ce7 | -6.30924 | -54.80053 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 279a3f9b-01ab-367b-b079-b0aa1b1f5058 | -3.5488 | -54.6722 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 80759578-9098-397d-b745-0dfa2c48cae8 | -2.47631 | -56.10304 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 175614f0-1846-36c6-b5c7-739feda8ce33 | -2.88616 | -54.15507 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bfd631e-dd8c-3e06-8366-5382fcf7f8f2 | -7.16127 | -55.11863 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff000880-e24a-3fbb-ba30-f84e925787d2 | -5.83025 | -51.99738 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4aafbce9-7122-3fd8-bf01-6646a1adbf90 | -0.99787 | -53.73864 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beaf06bc-82f5-338b-8c42-d5680d8d4c3d | -12.09829 | -57.1633 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9473819-9a5d-3961-a91b-c154988313eb | -3.6508 | -54.0572 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 467a8d2e-058e-369c-b5d1-da9435c8e641 | -3.91005 | -55.8893 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 032b4faf-9c69-3325-9de8-c941e81c2775 | -2.9898 | -54.11586 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f8decd9d-8b78-3d5c-937f-e8204f10f176 | -4.77645 | -55.72386 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7969461-2c9a-3c94-abe8-766448e243e3 | -4.63662 | -48.85857 | 2026-10-08 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfbf1088-a57e-3f21-8223-cadbe3d7a144 | -1.25672 | -55.7518 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3faff06-6023-3eb2-8883-cf4460da25a9 | -8.62711 | -67.02171 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de848a31-31a6-3824-b091-2a07581a7601 | -2.76862 | -54.07882 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02e941f6-fb6f-3517-8443-4b8de377d15a | -1.52842 | -54.53986 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e17b481-5c20-365c-85de-f5c5ae4c8544 | -3.05849 | -54.15813 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0a040da-397f-3020-909d-7968e7428e43 | -3.29608 | -54.04596 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9570b5ec-c168-37fb-b283-86b0d581400b | -3.09325 | -53.72888 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c9a32eb-1f63-3d94-99ad-948499edbd9d | -2.85375 | -59.1065 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ff5940f-382e-3193-8a6c-e177462782cc | -6.95152 | -45.27017 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 628a3e7a-3625-384d-ace8-e8b3da9837d5 | -7.1411 | -46.52095 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 124312b1-7272-3286-997f-26523ae8d030 | -3.1025 | -53.76312 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dab429ca-1fed-3cef-b62e-8226395b729f | -3.05982 | -54.38363 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405531bd-daf1-3ab9-b56d-b30a58b46f69 | -3.03425 | -54.10691 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53b49024-6599-350c-8a1c-64125584ad4b | -3.47784 | -59.57886 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85d69df6-8c41-302e-9ff6-565da9b1b8f5 | -3.16789 | -50.59037 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9560db4e-be39-35f1-a5cc-ae4e95541b12 | -3.28046 | -54.00746 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85447688-48ed-37d4-8274-aa0057ca1c69 | -2.58517 | -56.16244 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6d2b6fa-a1ec-3cc2-8a2d-fe83bcf1eb02 | -2.58348 | -56.15155 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef8a4ec3-1b1c-3862-863a-9dd019e75baf | -3.11591 | -53.79377 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 91e325ec-3848-3bf8-aa04-c32619b52f1d | -3.35961 | -50.48182 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa64d9cc-35ad-3508-a0cb-a12b3cd7f539 | -7.21471 | -55.16658 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d4a2a92-6a2f-3d43-9601-22e36acda2e4 | -3.44381 | -56.93552 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3804a22c-03e8-327b-9005-54911d47966e | -3.38574 | -59.432 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3760560c-cfd9-34ae-ba70-8478456836dc | -2.79253 | -54.08646 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26e0d053-8605-39ab-b501-d26a06019bed | -3.17876 | -58.63492 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 282da998-3a91-3b8e-b062-aa4667232ad7 | -3.67952 | -57.05123 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f269fe-5361-3781-a051-0cc45c0c0b40 | -3.49642 | -59.26027 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b3ac78a-7812-3b06-ae50-7bd92f1c3286 | -3.96798 | -55.82639 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef0e4431-5428-3958-b12f-22dacadf8cd5 | -2.78672 | -54.07766 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83b15aaf-577a-382d-8f94-1090f92f08a1 | -3.02473 | -53.88941 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc7c9fa-df33-3d86-b768-1d673403681e | -2.51982 | -56.25858 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61623023-b75d-320b-bbdc-2991db58d835 | -3.01622 | -54.08434 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f35fb51d-8081-3322-b231-c2e3feca499d | -3.0422 | -54.26145 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62fb76d5-a061-344d-a6e2-ee19a313e756 | -7.21819 | -55.16718 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f33b9f-ee3c-362d-95f4-6a8543eb59b8 | -3.11497 | -57.59638 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c527ee6-0898-3dd4-9fce-13f996a4a899 | -3.83372 | -55.97079 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1992defb-5786-3e80-b6c0-c1b0882849b1 | -2.47408 | -56.0956 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcf96776-0c04-3efb-9714-0b7a032e0b81 | -1.46278 | -53.23785 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f830beb7-2fec-3eb7-9908-24de9c13456d | -4.27259 | -55.71465 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d0d7fd0-b49b-39c1-8853-ef43dce42ea0 | -2.94313 | -54.17965 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da7a2af-6e8f-3e0a-946d-38da5f3c54b1 | -5.83348 | -52.0596 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fccff1d-efc3-3fc0-a9db-54dc08e49f04 | -2.37054 | -56.12897 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4482a44b-c009-324d-a126-eb77f18a2001 | -3.69863 | -58.29075 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0ff148-8d8d-3c97-b4c4-da69bb1dbf71 | -4.06988 | -59.84042 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88220c4f-0a2d-30ca-b4c7-01f9609b8a6d | -3.53866 | -53.9878 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 813a6da2-fe0c-3d63-8216-56f971bbd6c0 | -4.95171 | -55.1191 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc872cf6-d4cc-3a6f-b943-a87cd6cdcf74 | -3.48862 | -59.58059 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce26b34-1155-3b82-b93b-361ed4683a8e | -4.92946 | -55.86367 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6221946f-1809-3735-b8a7-e33b81b867d6 | -2.9992 | -54.10148 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1e223081-bffe-323f-bfcb-4955b16e98bb | -3.83875 | -55.9823 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c71e5e7-d668-3c8d-968b-e12fcc6e6ce1 | -9.0925 | -61.13879 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 582f7140-0c57-381b-939c-34371b3ca13c | -2.49084 | -56.16199 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05913de1-0464-36c5-9ab7-f18e25e42529 | -4.45768 | -55.39937 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e427da5e-40f3-3297-aad2-da7f4c057c03 | -2.86069 | -49.54855 | 2026-10-08 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 822daf1a-8ba1-37d7-be33-dc801dea0ad8 | -3.04965 | -53.16811 | 2026-10-08 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2923238a-f121-35f2-812e-bf9df45b03e7 | -3.3624 | -58.18624 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8ea0b31-92eb-3226-b77a-1e81fe4f844b | -3.51516 | -59.32432 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c08f806-e590-3bea-9d72-57aa32cf941d | -3.8436 | -55.86478 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f76a8080-49e0-30f7-abc0-4c6f7a1038cc | -2.45246 | -56.38247 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99565851-457e-3449-8eff-716165ac63a5 | -2.98392 | -54.13072 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2bdcbf1-64c3-3fcb-8c3a-d0bba93e08ec | -4.28785 | -49.08883 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af57127a-2557-37a8-a003-c647a364df44 | -2.96531 | -54.08453 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82b39288-973a-38cf-8a75-fffe8dea976c | -3.68018 | -59.64296 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f9a729e-ca3a-320f-bfa3-91f84cfad3fe | -2.05136 | -56.20254 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bed7753e-d0c3-39ce-9ac1-7a32cab0f217 | -3.35898 | -50.48598 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2df64dc1-1be2-3cff-90bb-366ddcbbbf2f | -1.20572 | -55.69069 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cea0a75d-3703-3f14-8562-1dc69882701c | -3.28887 | -54.06882 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5611c1b6-0d17-39d2-820c-905dc3a34927 | -3.54281 | -54.67179 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e51b7fe-c8e1-33f2-a476-9ae0d4f2590e | -2.84337 | -57.47732 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91163747-51b3-35f9-a086-4f021fa55507 | -5.82216 | -53.83382 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d79b2e8-4c8b-34ba-b772-7c689397abef | -3.58327 | -54.67752 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18f8cd4d-9c4f-3082-8500-dd94d185d12f | -3.56153 | -59.47909 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00ce969-baff-3fca-b561-728fdb7a3934 | -3.74373 | -51.2121 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a61f2c7-2106-37fe-90a8-6840b6ea771e | -2.49952 | -56.06414 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 44a09ffa-0e56-3646-9733-26553e28d124 | -6.94487 | -45.27038 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95ab8bb6-de25-388c-93b5-3062b21a83a9 | -3.33187 | -58.15903 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b392500f-27c5-34a6-8eb6-7bba329cbbe1 | -5.83793 | -50.14116 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 589adbae-2c17-3aea-a255-a18d1d522b19 | -3.00879 | -54.75735 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README155.md)
