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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc9340a9-4c5f-3332-adb5-85edf051b017 | -2.5428 | -53.3935 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9eddc385-09fa-3d83-8785-939051cb5f77 | -2.5428 | -53.4137 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| abaa4ebb-f1d0-385d-9585-6a853e4173f5 | -3.259 | -53.6388 | 2024-12-02 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 30798783-d515-3b27-8e54-ff31230ecee8 | -2.5612 | -53.3931 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| b2da6a18-c746-34dd-a6f7-cf8784d95043 | -2.0263 | -54.3088 | 2024-12-02 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 63755f02-19ab-3981-a4e9-d106d65db421 | -3.2591 | -53.6186 | 2024-12-02 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 832bdb1e-e400-31ed-ade8-fab21a3bdf9a | -3.4201 | -50.2375 | 2024-12-02 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b6dee433-361e-3a08-959b-aebcbe2114f2 | -2.2666 | -53.6212 | 2024-12-02 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1fc19767-76a4-3b04-b276-66fa423031bc | 3.3842 | -60.4756 | 2024-12-02 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7fafb856-e7fd-397e-93cb-8f8794ae179c | -2.60932 | -45.23533 | 2024-12-02 01:11:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 4d368cad-6292-3531-8783-1a18ae3f3c88 | -3.40156 | -50.22239 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2459f3d1-e3be-3ff6-a1fb-9cda6557379c | -3.266 | -50.21132 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 043ec24f-8329-3b3b-9665-88c7dfc8ffd9 | -4.19342 | -50.67922 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 68129db4-40a5-32ab-b65d-ae2a8e929672 | -3.54685 | -51.03197 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5bd53cbf-a0ac-345b-9817-0a7f2cddf979 | -3.72182 | -52.28094 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 96e0b940-0fac-305c-af32-d365a1b51839 | -3.6118 | -51.42604 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd1cf86c-2a79-3d45-bac7-678f175b7197 | -3.70712 | -51.0723 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f0f97c35-95a0-33a7-a670-4d3d24b8b730 | -3.75557 | -52.32711 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fbba5086-5a47-3f0f-ae06-3f10c97855d0 | -2.93017 | -45.83995 | 2024-12-02 01:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4aeabb15-fbe2-31e4-a78b-7e52f01c6785 | -4.20481 | -50.6888 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 420a5d5a-32c0-35a3-a5e8-79ad811ef62e | -2.61793 | -45.27131 | 2024-12-02 01:11:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6b020c76-5e2f-3753-9b81-18075ab4ae06 | -3.405 | -50.24641 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cce3003e-399a-3ad9-962a-63b20c932778 | -4.76052 | -46.43861 | 2024-12-02 01:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1fce331a-9737-33a1-8d32-c1bfbd7f113b | -3.49779 | -50.32409 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e6f48989-bfc8-3497-8989-173b8af41f29 | -3.72791 | -51.08014 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cde25d1c-ec00-38f9-bcfb-c6cbc3a32726 | -3.76359 | -52.44851 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| faf22d1b-dcb4-3d6f-9aa1-3ce3a9c6ebda | -3.70519 | -51.8414 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 19d0a65b-3815-36a3-b0eb-e313d65fb2c2 | -3.3259 | -50.19024 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f022669-5f2e-3313-9688-26fdbadefa06 | -3.71821 | -51.7999 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5fc2428-79eb-34a6-8e2c-86b41bdf3bc6 | -3.96242 | -46.01056 | 2024-12-02 01:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 867f3871-3559-3daf-9c08-c89b258f3cac | -3.61788 | -51.53827 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9dd01cf8-58a0-332b-9e8b-2e857059f2d8 | -4.0579 | -48.95662 | 2024-12-02 01:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 37cc4f10-eed6-3d9c-85b4-e05ababb91a1 | -3.53542 | -51.49895 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 94ec3530-ae50-36d0-a66c-6dfdb137a321 | -3.75782 | -52.66983 | 2024-12-02 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2dc2e28-08aa-38da-9841-ede1039d1c9a | -3.53743 | -50.17798 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 69328b7e-88c9-3aba-a603-a94886a668ad | -3.47731 | -50.2543 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ead8c352-e1cb-399d-8afc-8912c5bf7a4b | -3.72051 | -52.27158 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 0af6fb11-cb5d-3c31-8874-0647f0ac46a3 | -6.37009 | -47.35935 | 2024-12-02 01:11:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3e73ef7a-93ae-3734-8ea7-b62d879b0d49 | -4.00305 | -50.35078 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b67660d3-1580-3e0c-95df-7a367ff4182c | -3.96541 | -52.18034 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e2b9c389-9261-382a-a795-bdd629c93867 | -3.85544 | -52.31599 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a1b10f9-1925-373b-bec8-c2013de2872d | -6.07654 | -48.06441 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2103216a-7107-3e80-bff4-5c09a102cd9a | -6.08226 | -48.04176 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2b1efad9-364d-3ae6-b812-87439e71ed1b | -4.81364 | -48.62416 | 2024-12-02 01:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 5f50f3ea-fc69-3c4f-87f1-ad3284dea026 | -3.89097 | -50.07718 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 82fe5b4d-e0c6-3bbf-829a-71d462a5784f | -4.26841 | -50.85654 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 94ecfb7a-6045-3002-8573-646be51eb130 | -4.02615 | -49.9391 | 2024-12-02 01:11:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| abbecd16-a814-356c-9845-d0a68f2431d3 | -4.2923 | -49.94382 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b848489d-de93-3981-9db5-107eb4bb874d | -6.08706 | -48.07315 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 37b1aee0-a73a-3ce1-89d2-e4ebd66574be | -3.75674 | -52.27006 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 551d7c0a-66b3-3212-8d27-ddf349d693a2 | -2.91716 | -45.35255 | 2024-12-02 01:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 80367a1d-ba34-3b15-bdaa-0853f290be3c | -4.11962 | -53.81243 | 2024-12-02 01:11:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1f2a4ce2-7f6e-3f74-8e29-b9232ce115e7 | -3.25396 | -49.90977 | 2024-12-02 01:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e5e08c84-1db4-3713-acae-c048468a61ea | -3.45864 | -50.26913 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 166a5288-e1a0-34fd-a1bb-484a376543d7 | -3.34468 | -50.2491 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e5f96cce-8561-3382-8668-84b1e7234261 | -4.19501 | -50.69027 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a5102e3c-a982-39eb-905a-b4d98a555510 | -4.25721 | -50.84729 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 868cdbfc-fe1a-366d-98b0-5e7296a5b139 | -6.0731 | -48.05921 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 687eae0d-ad74-3ea2-ae47-69c530c2161d | -3.48399 | -46.0942 | 2024-12-02 01:11:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6ad08627-1a1a-3a1a-824a-ae07043649af | -3.42799 | -49.98764 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ff09318-8c17-39b1-9dcb-01b50307d979 | -2.91993 | -45.35746 | 2024-12-02 01:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 31687289-7282-3f65-b5ba-5b69b1ec2ca0 | -6.07425 | -48.04865 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| dea9d37f-2859-36ba-bd7b-02856552f0b1 | -3.33445 | -50.25063 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5f9eff0e-8def-34a6-9f83-8766e6cfd5ed | -4.05999 | -48.97112 | 2024-12-02 01:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a934b12c-47bc-346d-9818-0b403e406566 | -3.46884 | -50.26768 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 33b6cd15-e1d7-33e1-80a1-83f80c916752 | -4.24079 | -48.63805 | 2024-12-02 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 866b9ee7-c95e-3b65-8cc3-63a5cbc05ae5 | -5.58211 | -45.13449 | 2024-12-02 01:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f3656fb2-bafe-386f-bdf1-d787e539cf7c | -3.85326 | -51.24774 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5aac4676-c49d-3fcc-9d56-b8af17d4ad93 | -4.11501 | -50.49218 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8e509a4-5e44-3fd3-99e6-0f2cba151d98 | -3.70873 | -52.18732 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 95ce4b06-f925-3f3e-b274-74c766e3e313 | -4.1166 | -50.50344 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dff05add-77e1-3987-b19c-bcf9af451f3c | -4.2669 | -50.84582 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1ea0ce9a-2a98-3f3c-9d20-6c7ab6022a3c | -3.65259 | -51.12959 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 29e77e4c-d035-3d91-b0ff-dddbb0956aab | -3.30521 | -50.11876 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cded446e-43ce-3225-a0fa-98cc09a7a1b7 | -2.61394 | -45.26534 | 2024-12-02 01:11:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 32afcef1-fec1-3815-b854-217d5017583b | -3.62729 | -51.53693 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 712bed7f-e76c-35fe-828b-958394734510 | -3.48731 | -46.08714 | 2024-12-02 01:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2c931d5e-8623-33aa-9aa3-b2c61ec7e9b4 | -6.81991 | -46.7836 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 35893535-0f39-33f1-87a6-ece702be60cf | -3.86594 | -52.39009 | 2024-12-02 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c32c5434-91b9-31ae-8bd9-24f2a060c16f | -3.37287 | -49.873 | 2024-12-02 01:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 433b116f-e948-3528-8b26-7a551fdcb359 | -4.25872 | -50.85803 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| d02e2578-1ed6-3b8f-aed3-5270b9bbc470 | -3.74633 | -52.26207 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 20ef4861-ad5e-3afb-ae82-e2b4b212bd4d | -5.58636 | -45.16185 | 2024-12-02 01:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1cf0a933-4352-35e2-900b-1d8fa4e13412 | -3.68436 | -51.69506 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ed95e3af-7ab6-3f2f-a936-0b178074cfc7 | -4.27046 | -50.85029 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 8cef40c9-cf0a-307b-b08a-fde7fe3a39ae | -3.70381 | -51.83171 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 02279259-d6d8-3770-aeb6-de2bc69ba612 | -3.64782 | -52.67325 | 2024-12-02 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16175d8a-ed1a-34d8-8ded-f7d21bb5b079 | -4.27607 | -50.68345 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0cca7c0b-5bed-3bba-849a-356e376bb6f1 | -3.54536 | -51.02134 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cfc0e0f7-9def-39e3-b846-d8b38a93875c | -3.40328 | -50.23441 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 84cbd1d5-3d0c-3f33-84e7-1bbfa806540a | -4.27765 | -50.69439 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b6ea729-bd28-3dea-8b79-804b43b77023 | -3.99598 | -47.27638 | 2024-12-02 01:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 774da9df-092c-35da-b3ea-331395a8068f | -2.61355 | -45.24129 | 2024-12-02 01:11:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 6d3d9c7c-897c-3b07-b384-1bb67965f594 | -3.8604 | -46.54734 | 2024-12-02 01:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 79415914-2bd4-393b-abbf-821df61d3168 | -3.42982 | -50.00017 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bf258792-56e0-3a7a-a983-965404173cce | -3.65802 | -50.44329 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8158c782-2dc8-3edc-a5ba-1b5676e2425c | -3.85691 | -46.52423 | 2024-12-02 01:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 92643781-bd21-39e0-bea5-f10051d796b6 | -4.56729 | -45.47942 | 2024-12-02 01:11:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d28c7074-082e-36e9-842a-b1733f64e20e | -4.59148 | -50.60764 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 902f9a32-e12e-30ef-a8e5-d5a4c8e9d679 | -3.74766 | -52.27146 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |


[Clique aqui para ver as próximas entradas](README12.md)
