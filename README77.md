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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1cab933-8529-3534-bb54-603824ca1e6e | -12.82325 | -51.20104 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d2bd9d0f-a305-33bd-b973-7ee0db921bd7 | -12.82265 | -51.17683 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7d0b51f9-61bb-3176-b43f-aca0de7934fe | -12.82156 | -51.18262 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 82534550-91bf-3fea-9b58-cb412cc2b1d1 | -12.82047 | -51.18843 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b4d8709-9941-3658-b044-911c56e61c29 | -12.81988 | -51.16425 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 039130fb-e297-3f1a-8711-147a8f48d8be | -12.81938 | -51.19423 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69c5a090-6034-349b-b54b-2c1e4857fcc0 | -12.81879 | -51.17004 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ca7b7f79-f92f-3961-b761-c1a7fc21bddb | -12.81769 | -51.17583 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 86b0bf52-374e-3738-945f-10b1ff114159 | -12.8166 | -51.18162 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b1597775-453a-3a11-9bcc-0ccb85baf001 | -12.81551 | -51.18742 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2ffe80d-b2ec-34ce-88f7-8f74f8ab3967 | -12.81492 | -51.16327 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| efc67370-ddba-3067-bfa9-e85c1530db66 | -12.81383 | -51.16904 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| da3feb18-f8a2-37e8-8642-32314da85ee4 | -12.81274 | -51.17483 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 657c5fa8-8e9c-312b-9be6-96ac39cb9165 | -12.81164 | -51.18063 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 71a85694-830b-3120-a321-a7a278138817 | -12.80887 | -51.16803 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 6d858766-8509-38b5-9757-7456e5adc4be | -12.80778 | -51.17383 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b7d6ae17-03d7-3da5-8684-a4325424333a | -12.80668 | -51.17962 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8f2d9652-1f88-315b-be30-e2b72438b1ad | -12.80392 | -51.16704 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d99abc10-5ac2-3d9b-95b9-4243eaa85796 | -12.80282 | -51.17282 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b89b8cf1-988d-3979-9acb-978f986ece52 | -12.80172 | -51.17862 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 47e64cb5-df13-308b-bd5f-3f650b4ad6c4 | -12.80062 | -51.18441 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ccf022fc-fed9-3326-b59c-25279349e2dc | -12.79952 | -51.19022 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 892993f0-a453-379f-8eb4-222bf4fcb23e | -12.79896 | -51.16603 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| cdf76d19-c86b-3b1d-9471-9f86a8f9aa64 | -12.79786 | -51.17183 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 8ec2fc6f-61c4-30f6-8591-25848e6b3067 | -12.79676 | -51.17761 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 115605fb-b9b0-36fc-a24b-e0c334f7191c | -12.79566 | -51.18341 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8ae2bc95-d49e-30a9-8358-361e13c59b78 | -12.7929 | -51.17083 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 417a1cc6-2fe8-3e74-911c-157f8898b109 | -12.7918 | -51.17661 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 11f11c75-a7c1-3273-9718-a8e08e6555cd | -12.7907 | -51.1824 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b271729b-9ae4-3652-b881-e7e4f131efcf | -12.7896 | -51.18818 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1a585a3f-a672-359f-8d33-b0e9e324fbfa | -12.78684 | -51.17561 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| beb28206-659c-3997-ba55-09ee4d49389c | -12.78574 | -51.1814 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64c4af53-d584-3b9c-9d63-9815ddb09cf6 | -12.78463 | -51.18719 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1b65cb33-7155-3abf-bed1-d082489971a8 | -12.78352 | -51.19301 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ae132171-67ab-397d-9b54-6ff5b7225121 | -13.29592 | -51.35111 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eaa66c4-3b2d-3bfd-9e3a-fe32d779998c | -13.29431 | -51.33261 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fe04ae1-5401-3dc0-8ec3-e1ed0e260ff0 | -13.29319 | -51.33843 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7db51e41-1a8e-3aff-bf6d-09835dcc3837 | -13.28935 | -51.3316 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01a305e2-6108-32f8-b33b-ad0051f1d785 | -13.2855 | -51.32481 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8e36d33-f620-3487-936c-01963d5eb61a | -12.84873 | -51.31134 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcb1e975-d09b-343f-8e62-2bc510164603 | -12.84373 | -51.31034 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc084aeb-b7c6-322e-a28f-a705d39ad914 | -12.84316 | -51.31329 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7787b060-ebff-35f5-861a-4471edc86b74 | -12.83813 | -51.31512 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e145624-a012-3156-b905-8ae2ec40d0f9 | -12.83759 | -51.31523 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e6b6a6-0c7e-33b8-932d-849959075b96 | -12.83258 | -51.31705 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 445b35b2-fbec-3251-980b-d8ca9f66589e | -12.83203 | -51.32001 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a88a2ff6-654e-3811-b274-a212bba58bf5 | -12.83201 | -51.31717 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f44db897-d64c-38b1-9df8-eadb460937a4 | -12.83144 | -51.32012 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73760f7f-5e86-326b-b431-7c1d02e4b8a9 | -12.83086 | -51.32308 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b24d8a9-be55-301a-b5e5-d90c3a330746 | -12.77134 | -51.33849 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96430819-c076-3b32-a761-90f910b91803 | -12.76858 | -51.3256 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85923520-cc85-3649-b98c-56fbba76a560 | -12.76802 | -51.32857 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54e90c9d-f0e3-31e0-a754-0be291836c77 | -12.7664 | -51.30978 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0cef26d-92a5-33cc-b53b-e27ba0ade2cf | -12.76584 | -51.31273 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 464bda07-dbcb-35ea-868e-d9e4dc306cb7 | -12.76527 | -51.31569 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 733a9532-c58a-3fb7-a953-791d4ad4e22e | -12.76471 | -51.31866 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b1aae41-7b28-3a0d-ac83-a5d96ef483c1 | -12.76301 | -51.32756 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5089d896-27e8-362c-af96-5a9d25eeb4d5 | -12.76244 | -51.33053 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25873fbc-c787-32f1-91c3-aa1a09431782 | -12.75856 | -51.32358 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6b1c08a-277a-3ad6-9393-3677a783974a | -12.75799 | -51.32656 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0e450f-dd1c-33ed-be05-3db7e917052f | -13.30201 | -51.34629 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40901951-4889-37e3-a119-3d69f81b684d | -13.29816 | -51.33944 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1611f977-027f-37de-84a1-27f5eeac79ae | -13.29704 | -51.34527 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8839b47e-d16b-3e73-8409-d091de3b2125 | -13.29207 | -51.34426 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91404891-5165-3864-b062-c4faf2835510 | -13.28326 | -51.33641 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35d3cb52-c605-3dc6-80b1-a4c034db5f42 | -13.28053 | -51.32381 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4683bb7b-34fc-370b-99ab-c2c14070dab0 | -13.27951 | -51.32782 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d3cc21b-a900-3f82-a069-8a5dea7d15bf | -13.20508 | -51.25846 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e15a3c24-d9d4-3d2d-b9b1-1b30c29b8575 | -13.20123 | -51.2517 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e965b227-c0d8-392b-acdf-a4124c71a3fe | -12.83996 | -51.22289 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 271ec772-379d-3f03-bde8-3d286876734a | -12.83985 | -51.22254 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d18c9be7-597c-3c34-82b3-12741bb89d8f | -12.83883 | -51.2287 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ae3942cd-8cbb-3147-8ab2-0fc6a42c3e1d | -12.83876 | -51.22837 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8c05f06-f3a2-34b9-9f7e-43aecaffb6a2 | -12.8377 | -51.23453 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8708a29-8355-3f44-85d5-99909bcdc8fa | -12.83767 | -51.23421 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaf5477f-6565-3d9b-8a0f-ef3e30885492 | -12.83685 | -51.23859 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03085d9f-aa2d-3792-9868-355c2ee2a383 | -12.83657 | -51.24037 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e5183af-dbee-340a-afc0-3a7132c9bd19 | -12.83631 | -51.24151 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102499c1-1c72-3c5d-8b15-2788daf82388 | -12.83499 | -51.22189 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 845df397-f709-3e23-b9b3-634481d68aa5 | -12.83488 | -51.22153 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 06a25a38-b020-3cb2-9f31-5118f277c74a | -12.83386 | -51.22771 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0c54cc5e-b1f3-36cd-a266-644050c54ed3 | -12.83379 | -51.22736 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7bd15e98-accd-356d-b659-e4ed1e20063f | -12.83209 | -51.20887 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| fc7bdff0-c839-32f0-b5b8-b407b42e3dad | -12.83188 | -51.23758 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eacf46f-b20f-3c26-8ba8-d55a5e4fe100 | -12.83159 | -51.23936 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0ff3124-b57d-3185-9e58-9f24c1487e1c | -12.83133 | -51.2405 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2281d1a0-fd09-33d1-9d67-b3ce062130a4 | -12.831 | -51.21469 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 0ba1d99e-1995-38bb-a2ea-d0bbc63b0453 | -12.83078 | -51.24342 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed9bc122-c3e8-3edf-b990-f06231c7f6fa | -12.83024 | -51.24634 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed5f928e-b0f5-3536-8662-e1e762f0a4eb | -12.82991 | -51.22052 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 498ace87-fd50-38a7-a933-de69508e709b | -12.82969 | -51.24927 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f417ae6-122b-3e50-b358-0dce9c8df6f2 | -12.82914 | -51.2522 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba5a29d-4247-3998-88f5-3c6c2c3c455f | -12.82882 | -51.22635 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1a223968-b5b6-380c-89b4-6584e79e5b87 | -12.82859 | -51.25514 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7a134d9-12d5-30f1-96b0-3a5f4d9ee015 | -12.82804 | -51.25806 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44ac4c52-45c4-3365-91bd-3d32dde8745a | -12.82772 | -51.23218 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a934cdec-9cc8-389e-a7bb-7283454f44cf | -12.8275 | -51.26099 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10bad92f-e77e-3dd7-95f7-2329d9a26422 | -12.82712 | -51.20786 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3f0d6f21-400f-3feb-a294-8cee72121060 | -12.82695 | -51.26393 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e24d5c-b7ba-34e3-a816-bf6100cc67a3 | -12.8269 | -51.23657 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README78.md)
