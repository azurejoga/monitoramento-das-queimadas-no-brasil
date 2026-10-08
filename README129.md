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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbab0106-3a2f-3579-b0f7-e80f727c7051 | -3.2275 | -56.82714 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf6084f7-b4e9-32ee-9f1e-2a81487aeb81 | -1.28491 | -56.98077 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 19ed2ab2-3154-345a-80da-700186c06eed | -3.66981 | -56.81193 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35a96832-7adc-3313-adc7-ba70746df1b2 | -4.13792 | -54.92467 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 479193ae-0ab1-3316-8264-00a379a6bbfc | -5.29926 | -60.10474 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9071dc2-4073-3f0d-90cf-cba5d6035d63 | -3.19264 | -50.5733 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1174aec4-5ae7-3614-812c-bf9a7d6b9144 | -2.50915 | -56.17549 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a27d5cb-d865-34f3-8814-d0ab4f3d2f53 | -3.29855 | -53.86865 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b94668cf-4e4f-307f-a456-8fa39685bc54 | -4.77364 | -55.71978 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39cdc9d3-0f2d-3c27-854b-4a4cd64eb534 | -3.17571 | -50.45283 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf62a8df-4b9b-39a4-a8d4-ae7c07c4d2ff | -3.73956 | -51.21146 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d001dc-3e97-3d8a-a85a-9ca766e9ce42 | -2.49674 | -56.06016 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14249f3-41e0-39da-a8f3-520712731e13 | -6.51194 | -55.37971 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1ca4dea-1517-35e9-b05c-001f524a61ac | -4.54917 | -54.97189 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52055627-fb07-3e85-9b86-43b9d04c1be2 | -3.23331 | -53.89104 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4355c95d-6cb3-3efa-a8c4-617d14394551 | -7.38126 | -55.2102 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08b0ce95-c432-3f08-91ac-81667136e73b | -3.10259 | -54.98463 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b51d449e-6b82-3d4a-9785-979861e5bd47 | -4.11284 | -55.17211 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f8ad83-28d0-3991-a0e9-e66572663149 | -2.46688 | -56.09801 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a36a3360-a294-3cdf-857c-aba130fa4cdf | -3.01422 | -54.14333 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b54320d0-7c66-3e9b-933f-e668a7be92cc | -9.13612 | -65.2935 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c01181-f06a-3282-aac6-14e0d9a1f000 | -3.11155 | -54.16519 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d70308f4-6da6-3d03-85b2-bd49f321a66e | -3.26743 | -54.0215 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca4895a0-4d6d-34c5-9b4a-dfc1e94f2850 | -3.1747 | -58.63813 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d82b39-7d39-36da-adca-3d1c53426d6a | -5.68738 | -53.49186 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51667e23-ea75-3911-971b-0c4c01044b9f | -3.55108 | -59.49813 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0daa89c5-9d6f-34c4-ae7c-dce29d532984 | -3.07257 | -54.37021 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae88be7-5b42-3f72-ae2c-afeee8a0af3a | -3.07143 | -54.14432 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fc76625-92c7-3a34-bf94-24b08191f275 | -7.2159 | -55.15884 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ac87fc-8b83-317c-a29e-ac50a8b81925 | -1.38984 | -55.46376 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d62b5ff7-1e60-35b8-87de-67efebd05b3c | -5.68434 | -53.48675 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4a4a26-265f-3342-8e70-f0d55c0ffbfa | -3.1113 | -53.77675 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 519c5448-8e0a-39dc-9ff7-884b92614196 | -4.98119 | -56.22132 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9041a1d8-b725-3ff4-9a67-b2e551b8ed8e | -3.87964 | -55.99564 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00072b44-ea62-3795-bb91-5ca1068d39ab | -3.1733 | -50.4394 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ab0b2f-07ba-3e07-b03e-5a01bab27c48 | -3.03741 | -53.94783 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af7ea433-e275-396d-8f37-6c2b569523c7 | -6.71064 | -55.0456 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 086ce25f-178b-352a-8909-a7a0c82c3375 | -3.6674 | -60.62967 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1e4ef15-3cc4-3fc7-a772-6e0c5a08a857 | -3.59158 | -54.55601 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c75611d0-15f1-353b-8c3c-b4967dd5b237 | -3.4825 | -59.45881 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fea1a03-4c0b-3e5a-bf72-3a92a785c0d9 | -2.89361 | -56.67509 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 310eb230-f3dc-3648-8b1a-e470bb84406f | -2.72621 | -57.47 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bea1fe5-6440-339e-9035-f6d433a6da67 | -3.3341 | -58.16683 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d9271c3-32ec-3c42-99c6-c5d58b8ac34f | -5.28687 | -60.08996 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdcb158e-4735-3a91-9316-4218b3ef9fec | -3.53247 | -54.67022 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa3af459-0d1d-33a4-a965-336309fb47ae | -3.5873 | -54.67431 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72c5579e-7584-3d7e-9ffd-bf2b3d0269da | -3.07685 | -53.94992 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0e020f0c-867c-30cd-966b-a45a62af6094 | -2.47686 | -56.09958 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2c08781-2a03-34d7-b171-1e274688af04 | -9.25657 | -60.87603 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c58e0b1-3106-3d94-8250-eed0e88314a8 | -2.77093 | -54.08707 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89d1a89-52d6-3500-ada2-b325d53baefe | -2.50762 | -56.24959 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cd5ab8-4b77-3d1c-9843-1274910f0bfe | -3.26973 | -54.02989 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1554a69-9572-3a3a-adf9-a7a601640c8c | -2.97923 | -54.13786 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c32d730-39fc-38e3-bb08-060b4b614ca2 | -2.94319 | -54.06523 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a02f2ed-9b31-3252-974f-e546131a8892 | -3.47465 | -59.50735 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1e80db3-182c-347f-9b40-3746ed262576 | -2.50798 | -56.13988 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d853f718-d0c3-3a4a-816f-b1d5d4bda941 | -3.90615 | -55.89227 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e4e4a06-9ec0-3585-bad0-750dab37cfd8 | -2.70431 | -56.54634 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bec2c16-3664-3644-a190-4be950ca2fd0 | -3.30771 | -54.70081 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6f07730-0a53-3dc3-a530-f09afe17bb6c | -3.56181 | -59.49986 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b375e85-d372-3c1f-8e97-dc83d7a033d2 | -3.52449 | -54.65369 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272c67ef-8907-38cb-98c4-b033c77239d3 | -2.97155 | -54.11314 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 161b1012-428e-3657-8c14-30b9a9e13683 | -2.93893 | -48.86611 | 2026-10-08 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f57f577a-9b7e-35ca-9217-f4e23930ce36 | -2.56799 | -56.16329 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18b76d72-7c47-374b-a3b3-24debd62f861 | -4.60149 | -56.0794 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d4dea67-23ad-3bb2-886f-c4b8fed4959e | -6.94926 | -45.29419 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 124b9aad-19c8-3b38-9892-40512d973896 | -4.12223 | -59.88547 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11b77e8f-0de7-3d0f-9ea3-c10e59af8b37 | -3.70896 | -57.09484 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 723e22e8-b173-3718-a0ab-6e7bb01f3199 | -3.10312 | -53.75913 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1d46bd6-7999-34c3-a229-7e70e972d734 | -2.51036 | -56.23233 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc0f8abf-1e41-3687-b81a-eb1df3c073e8 | -3.30436 | -54.03922 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9715839-4d4d-3148-81a9-348d932daea2 | -3.93175 | -50.33843 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4c718329-5448-3000-af6f-f0b3e3f8116e | -9.05593 | -65.92584 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22364649-0699-3330-9dab-8526be59c03c | -2.96013 | -54.16263 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fbf3a88-677f-31dd-ba23-74eaf19a4da0 | -9.11414 | -65.36274 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfe4220f-deec-3216-91c6-2bc5ed21ff50 | -3.02395 | -54.0577 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d6710b1-e46b-3cca-8e59-b19ad3b8f0f1 | -6.88099 | -43.69272 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| deeb0d45-f8fd-33db-bd62-72375e80005f | -3.31822 | -58.26525 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df3b37c7-ebf9-3343-80d9-2c3a5b68a282 | -6.31274 | -54.80114 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ca0f8cc-a338-37da-8d7b-179b15eb1407 | -3.69584 | -60.54759 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe1bd68-23cb-360e-a943-bb538b9c9aea | -5.11058 | -47.11553 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed258658-de2d-3cd3-ab74-296d5411b6d3 | -5.21278 | -56.08139 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41c44760-2b0c-3ba9-8663-b251a515dff8 | -4.69194 | -50.64065 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88fe7f5e-ed66-3fb9-9327-b60972aeb888 | -6.4678 | -55.48335 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da77520e-484c-3f73-8a33-f019edd45693 | -7.59927 | -46.76155 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f89659-c72b-3bd6-8093-d92d1a8b98b6 | -3.52794 | -54.65422 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 189fd86d-038c-36bc-89c9-0289843607be | -3.01167 | -54.73888 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad011823-eed7-3447-8ebb-61a77a7eb4d4 | -5.69989 | -53.48464 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e28c659-4808-379e-a082-2d339eb18290 | -4.77925 | -55.72794 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fb4626a-f09a-33b2-9972-461f1b2aa962 | -3.28596 | -54.0644 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fec1a33a-aa60-3c1a-9501-6c485ba4f706 | -3.7747 | -59.25896 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f62d7c11-e950-3015-83e4-3038611644bc | -3.05675 | -53.9629 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 59af4091-42f5-3e31-8d32-c26434eb6219 | -1.1971 | -54.20795 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30e24dd3-f360-32d2-8ca6-a6c3338ab81f | -2.51928 | -56.26204 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a30ff74-bd2a-346a-9d2e-b3d2f84fd19e | -2.91483 | -59.3166 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0046b876-edff-3329-9278-941ae7b8fc0a | -3.28489 | -54.04826 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99be3857-f502-3469-90c6-33b13c36f8a7 | -3.048 | -54.1565 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fba068e4-fc62-3aef-a8bc-4650822f4821 | -4.12178 | -59.8872 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bb5d2b4-a459-365d-a6d6-a3e37ff49040 | -3.5426 | -59.50507 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925220cb-fae4-38cc-af87-77165f74cf2f | -2.93855 | -54.16328 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README130.md)
