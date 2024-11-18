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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6208cb2-a61b-3d23-a8d0-5bbc4131003c | -2.87614 | -51.78465 | 2024-11-18 01:43:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7afbe20a-31d0-3a0c-a4ec-1cbc3e385cac | -3.315 | -53.37984 | 2024-11-18 01:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 7a4862e9-67ae-318d-ab24-ead2d2ee858f | -2.77287 | -52.62137 | 2024-11-18 01:43:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 2e42639c-3e61-3c13-b275-3437df2b1677 | -14.2837 | -57.630699 | 2024-11-18 01:44:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57143089-3f17-37eb-b2f3-aa2fa6a800cc | -12.55 | -57.820301 | 2024-11-18 01:44:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aed31728-a132-3636-963e-8289771a69e2 | -15.6688 | -59.729801 | 2024-11-18 01:44:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09a30d09-c2c8-3d1f-a143-4b675ac74697 | -14.2865 | -57.642101 | 2024-11-18 01:44:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b33cb87a-e9ea-3eda-8afe-beb3dd19fe79 | 2.94987 | -60.35923 | 2024-11-18 01:45:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 41bfd441-4f28-3d76-97e9-27f22c6e4354 | -0.18052 | -60.68795 | 2024-11-18 01:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 034abc46-2cd2-3896-9f0c-2f46fd28dc33 | -0.17923 | -60.67878 | 2024-11-18 01:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a52914d-885d-35ad-aa4a-f01cc4330ac2 | 0.95281 | -59.56221 | 2024-11-18 01:45:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0161b4ab-54d5-392a-9717-4ba30875e440 | -13.0158 | -56.469299 | 2024-11-18 01:46:00 | METOP-C | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecb2b9bd-7320-39a2-9b40-7fb6e93653d8 | -0.1781 | -60.690601 | 2024-11-18 01:46:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fc92f2f0-b53d-325c-a76f-3291eaf1a630 | -3.0568 | -54.410999 | 2024-11-18 01:46:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae81d8a-3c10-3a4c-adbb-dfe80ca1bd69 | -13.0121 | -56.455101 | 2024-11-18 01:46:00 | METOP-C | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3a9b82-d70d-36b3-ade3-eefc58a03854 | -16.0763 | -60.092499 | 2024-11-18 01:46:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 744d0265-5ce1-3d24-bae9-f03f78e1302b | -1.2964 | -51.741 | 2024-11-18 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 268.5 |
| 27898bb2-ce4a-3895-a33c-9dce3d7ea9e0 | -2.8791 | -51.7932 | 2024-11-18 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 09c5320c-12e1-346d-96fc-d821040e71db | -2.8792 | -51.7726 | 2024-11-18 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6cd46623-605a-349b-be8b-c16b009a4be2 | -2.8607 | -51.7937 | 2024-11-18 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 72bd4ce4-a72f-385d-959e-f264e06a77d7 | -2.5847 | -51.7181 | 2024-11-18 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3076761f-b84b-3627-99a3-3abfe11c35c4 | -1.7147 | -45.8307 | 2024-11-18 01:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 217.5 |
| eb33d212-e1ef-38b1-8795-67c3f6f610ad | -1.6962 | -45.8087 | 2024-11-18 01:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 77aca38e-edcc-336f-a6ad-1ec494ae784d | -1.2964 | -51.7616 | 2024-11-18 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 1e1b24a0-ea7c-34ab-9a5c-824c4b622d52 | -1.2964 | -51.7204 | 2024-11-18 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| fc3fed6e-9a1a-3b0f-afa6-1ba6e5c44536 | -2.4888 | -47.2466 | 2024-11-18 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 895e27da-d24d-3093-82fd-c10cfdde23b9 | -2.5074 | -47.2242 | 2024-11-18 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 616e78ed-b5a8-3ae7-95ad-2e3de094a446 | -2.5258 | -47.2455 | 2024-11-18 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 637f0973-9da1-3590-a4a8-e7b15c94e8a2 | -2.5072 | -47.2679 | 2024-11-18 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3f1a35d0-c6f0-3c41-a727-25f7ba33a966 | -1.7148 | -45.8084 | 2024-11-18 01:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c9c0e8c9-0b3e-331f-a29f-0acc50409729 | -3.3267 | -50.4923 | 2024-11-18 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e7e43c43-f66c-3dc1-a880-cb652c88fc2a | -1.3148 | -51.7408 | 2024-11-18 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 208.5 |
| af174a99-4468-3d9e-94cd-c7d806c29429 | -2.8608 | -51.7731 | 2024-11-18 01:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2e878307-543c-3e55-b2df-98e4a0bb956a | -3.1461 | -45.3404 | 2024-11-18 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| eba1ce1c-c58e-3cb8-bfdd-0e4665397ed0 | -3.3452 | -50.4917 | 2024-11-18 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 317d50a9-660c-37fe-9177-c72b687bab36 | -3.0542 | -54.4081 | 2024-11-18 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| deae4e56-c559-365f-942b-3e10741651d2 | -3.6593 | -50.439 | 2024-11-18 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 73b58443-5d8c-3093-83ac-b8fa4b076d30 | -1.6962 | -45.8311 | 2024-11-18 01:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 251.4 |
| 2b395af3-d648-33a5-83da-e7fa3009e672 | -1.3148 | -51.7614 | 2024-11-18 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 535a9f2a-4f2e-3245-bb61-21e35d6b4b8d | -2.5073 | -47.2461 | 2024-11-18 01:50:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 446.2 |
| 298d1fb3-aef6-30df-9978-3a3e33b21c9b | -1.7147 | -45.8307 | 2024-11-18 02:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 5e22d757-a105-307e-bab9-4d6ec5f2e950 | -1.2964 | -51.7204 | 2024-11-18 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| dd156068-ae88-32e0-b3b9-ea01c4b49ad2 | -2.5074 | -47.2242 | 2024-11-18 02:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f9f462a1-fbde-3ba6-a9d2-b05e506d371f | -2.8607 | -51.7937 | 2024-11-18 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 20d826b0-bf70-349e-9010-67159205c8a1 | -3.1461 | -45.3404 | 2024-11-18 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 407.4 |
| ea5658b9-65f6-3686-8e3d-643f8f25b744 | -1.3148 | -51.7614 | 2024-11-18 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6deb50d2-3d3f-3b12-b5d6-cc0e0beb2eb2 | -3.3267 | -50.4923 | 2024-11-18 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 327f79f7-ef89-3df0-a2f0-505c38df7753 | -3.146 | -45.3629 | 2024-11-18 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 231.8 |
| f52cef61-5f68-3382-8f57-ac41a98def91 | -1.7147 | -45.853 | 2024-11-18 02:00:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b9a3a96d-a54d-38de-a89a-5765da0e7595 | -3.1275 | -45.3412 | 2024-11-18 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 1f0c0f2d-b5bc-362a-81fe-911756bb2380 | -1.6962 | -45.8311 | 2024-11-18 02:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 63ffe058-96b0-3a45-8187-d35659412334 | -3.0542 | -54.4081 | 2024-11-18 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4a09c419-0d42-3880-8342-ac3cfe45437a | -3.3452 | -50.4917 | 2024-11-18 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 82a28c31-3a72-306c-86c1-ebcd0c557db2 | -3.1645 | -45.3622 | 2024-11-18 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3d21154f-525b-3369-9571-dac61b0c72c7 | -2.5847 | -51.7181 | 2024-11-18 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ca80b598-f35b-36b5-bc3e-a7480590961f | -3.1647 | -45.3397 | 2024-11-18 02:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 083af0ab-3cb4-3f19-9029-09bcc4d0b7b4 | -2.8608 | -51.7731 | 2024-11-18 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c8c371cb-c3b6-3aa7-9022-cfde81ab607a | -1.2964 | -51.7616 | 2024-11-18 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e9a998d0-59bb-39a3-b534-608a92de857e | -2.5073 | -47.2461 | 2024-11-18 02:00:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 9faea810-9d6a-3e93-97d4-42107a3e9fce | -1.2964 | -51.741 | 2024-11-18 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 272.6 |
| 3d0cc3c8-2fd6-34e3-8a22-96817724100f | -1.7148 | -45.8084 | 2024-11-18 02:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b6a8b751-3bcb-31e2-aa27-ea17c195e9cd | -3.1274 | -45.3637 | 2024-11-18 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6383a2a3-1ae4-3ef7-9453-345c3e5aa088 | -1.3148 | -51.7408 | 2024-11-18 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 4ca35c5f-3db0-3fc0-bd75-7087b238df20 | -4.9059 | -44.022 | 2024-11-18 02:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7bf2123b-3e8a-3ad3-80e9-3f89c56ba206 | -2.8791 | -51.7932 | 2024-11-18 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 733fc7e0-ff0c-3a47-b8e1-6e64cc41c51e | -2.8792 | -51.7726 | 2024-11-18 02:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 18a68ee6-219a-3411-aed7-d8001f39d5f8 | -1.7 | -45.83 | 2024-11-18 02:00:00 | MSG-03 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a557c50d-697e-3eb3-be9e-b6263e9098d4 | -3.13 | -45.35 | 2024-11-18 02:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5acd9bcf-6dc6-3bf9-9fb1-7c97cb453e07 | -1.28 | -51.75 | 2024-11-18 02:00:00 | MSG-03 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4663b691-c681-3191-9b0a-33400b0e431b | -3.13 | -45.3 | 2024-11-18 02:00:00 | MSG-03 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49bc20b9-4613-37d8-b54d-6e5438e8277f | -3.16 | -45.35 | 2024-11-18 02:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 130238d3-caae-31bc-ac72-683d28be33c3 | -2.8607 | -51.7937 | 2024-11-18 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b46e96c7-2003-3334-b4cd-71937e927701 | -1.3148 | -51.7408 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 1018efc9-3f3e-3ef8-a4c4-f7f771d0b85a | -3.3267 | -50.4923 | 2024-11-18 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 48cdd663-f47b-3c2e-98e1-f9e1d89eaae6 | -3.0542 | -54.4081 | 2024-11-18 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 14d6acc5-b83a-358a-88ce-614596462086 | -2.5847 | -51.7181 | 2024-11-18 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 97535617-6347-3bca-893f-4418f8eb9a44 | -1.3148 | -51.7202 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 316b9921-ed5d-36fd-88d3-1192b35ac965 | -1.3148 | -51.7614 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f010bf15-1219-3e15-a680-7dd22449a6c6 | -3.1647 | -45.3397 | 2024-11-18 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 04e61e9a-dd63-32fc-b9a3-afb943be50e7 | -3.1461 | -45.3404 | 2024-11-18 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 270.1 |
| f280819b-f2ec-308a-8bc5-9725d8a7f4c0 | -3.6593 | -50.439 | 2024-11-18 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 74576a1a-a7b2-3200-a25c-4dcad0bbd90d | -4.9059 | -44.022 | 2024-11-18 02:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| b8c214d9-8652-364a-9e73-3322db673ee0 | -1.2964 | -51.7616 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5e31305f-14d1-30aa-8e36-ad82440f6c9a | -3.1274 | -45.3637 | 2024-11-18 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0e2ec4e9-42ec-3815-9e16-b6c7f55ceccf | -2.5073 | -47.2461 | 2024-11-18 02:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e21c8d8c-04f5-3dbf-9a29-8f44455a48a7 | -1.2964 | -51.7204 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 02f577ae-f511-3b1d-8255-21316b2eb587 | -1.6962 | -45.8311 | 2024-11-18 02:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 0e3b7108-0b84-320b-a5ca-6ca0f9a88827 | -2.8608 | -51.7731 | 2024-11-18 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 85f60fe6-90e6-345a-8433-326ff7fdc1f7 | -1.6962 | -45.8087 | 2024-11-18 02:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0ddcc1fc-ffb4-35a4-8328-0a6c7e9e5572 | -3.146 | -45.3629 | 2024-11-18 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 15e0027a-9a4c-38c1-b916-fa103237b6a7 | -1.7147 | -45.8307 | 2024-11-18 02:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 21394a41-5cf6-3174-b857-75b0fa4ca536 | -3.1275 | -45.3412 | 2024-11-18 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e7c4c00d-0be7-30a1-9d64-02874d96745a | -1.2964 | -51.741 | 2024-11-18 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 189.1 |
| d809a119-67be-3205-9c1d-24a72912443e | -2.8791 | -51.7932 | 2024-11-18 02:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 4839df1b-070f-3e9d-83d4-7d691c4a4a14 | -1.6962 | -45.8087 | 2024-11-18 02:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| bb5a79a5-ced1-3bf7-81b9-1b8c4bba61b6 | -1.2964 | -51.7204 | 2024-11-18 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 34ee82ac-0d07-365c-8fb9-65af4a2a4f67 | -1.3148 | -51.7614 | 2024-11-18 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 107621e0-23e1-37bd-bae4-bf1d18f4d910 | -2.8792 | -51.7726 | 2024-11-18 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 21a9bc7b-7b29-3c68-b08e-161b7736626f | -1.7147 | -45.8307 | 2024-11-18 02:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| a61e1333-f9ec-3114-bdb8-193237cb0e31 | -2.8791 | -51.7932 | 2024-11-18 02:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README13.md)
