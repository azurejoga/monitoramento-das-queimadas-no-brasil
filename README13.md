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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61990402-c382-3580-8116-58d596fe7ef7 | -2.1351 | -54.906 | 2024-11-29 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 44e42492-110e-30b5-b45b-95db239d63d2 | -17.6457 | -57.5668 | 2024-11-29 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 7814a1ac-301a-39f7-8cb7-7588f43c7179 | -17.6007 | -42.7434 | 2024-11-29 01:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3f6ccc6c-2d8f-318d-9b9e-55e37b06f7ab | -5.0399 | -43.6205 | 2024-11-29 01:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f85fad77-ba53-3f09-a5be-bef154ada432 | -3.0028 | -53.2815 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ac03203f-ece5-3e25-b981-c0428e331cbe | -2.8664 | -45.5528 | 2024-11-29 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b54afa14-f812-357a-b8e9-c27150cef220 | -2.9844 | -53.2819 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 469.9 |
| 9e64d390-e128-31e8-9add-c21f4834f8ca | -2.8611 | -46.8186 | 2024-11-29 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 60fb1fc5-497a-3fa0-ac72-41c59105c68f | -2.6683 | -48.7981 | 2024-11-29 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| af66d52e-f938-378e-b9b5-43010b9176ed | -17.5798 | -42.7731 | 2024-11-29 01:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 30c7e5c2-ca68-3a2b-affb-ff3d1d62b675 | -11.4014 | -45.0977 | 2024-11-29 01:40:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ced31c01-d20e-31c6-87db-50245f4ef649 | -17.5805 | -42.7483 | 2024-11-29 01:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a55cdd77-3544-3373-bf04-d674fa42e8f4 | -1.5897 | -52.271 | 2024-11-29 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 48373258-5748-3d52-a569-97e26b3f7e1c | -2.966 | -53.3027 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| d47668be-33c7-3e0d-8ae4-6e7defc47d3f | -2.8425 | -46.8193 | 2024-11-29 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| efbd8e44-176c-35c8-8b46-dd1833cf2968 | -3.0028 | -53.3017 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 581c668d-cbca-351b-bb13-18aeb43e3966 | -3.3439 | -46.6912 | 2024-11-29 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6fe61d48-ace1-31e4-9d78-b4b930413f26 | -11.4018 | -45.0746 | 2024-11-29 01:40:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b35ba95f-fdf9-399f-ab14-06637b4e979d | -2.8665 | -45.5304 | 2024-11-29 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| bdd64ad6-c12f-3fcf-b65c-48dd89e9bfb0 | -4.4219 | -46.5764 | 2024-11-29 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1743ea0f-ea81-3b48-8c73-873a4f1c6d4f | -2.9844 | -53.3022 | 2024-11-29 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 5806ad93-67e5-3ec3-a820-dc5928a4ec58 | -1.5869 | -53.8336 | 2024-11-29 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| adf940e3-aa99-31fe-8396-ae39c85e6eaa | -3.3253 | -46.692 | 2024-11-29 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f455b8c0-f448-3e5d-80c5-01d06977ae54 | -2.966 | -53.2824 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 085fbf6f-0eab-3710-9e0a-3b6d5d4d3ca4 | -1.6997 | -52.4535 | 2024-11-29 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1c4ba55e-0467-3470-9f19-b5c47cbeaf7a | -3.0028 | -53.2815 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 00fea30c-8a4a-3dd0-ac38-c4e0095a83e5 | -2.8665 | -45.5304 | 2024-11-29 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e2198b30-d58b-34a0-b8ec-9ea043803ce2 | -2.1351 | -54.8861 | 2024-11-29 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 6655b242-4321-3043-bc74-7c97124b98fd | -2.9844 | -53.3022 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 230.3 |
| e74bd5e2-9ac7-3ce2-89a6-3fbafa60f38e | -2.9844 | -53.2819 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 359.8 |
| da6c6c41-cf32-348b-b0b7-6d456671256a | -4.4404 | -46.5975 | 2024-11-29 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f47665cf-efaa-3bbd-9bb4-b13b9bb20d4f | -17.6007 | -42.7434 | 2024-11-29 01:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c16e0ccb-73d6-3d57-b295-06641a4132e9 | -1.6074 | -52.6181 | 2024-11-29 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bf37f0fa-4a82-3633-96c4-0988213cd60b | -3.0028 | -53.3017 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a16045cf-0983-396d-a406-911be96a67f2 | -1.5869 | -53.8336 | 2024-11-29 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a82f83a9-cbc0-3810-af48-e85e23956b8a | -2.6683 | -48.7981 | 2024-11-29 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 90dac1d9-31db-3b0a-98e6-f0861499fdec | -3.259 | -53.6388 | 2024-11-29 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0a5c3c4d-e7db-34a0-9089-a932c04a63e3 | -1.5897 | -52.271 | 2024-11-29 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5eb0e803-ceff-361f-b85b-8e7f24fb5637 | -3.0356 | -45.1193 | 2024-11-29 01:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 3bc532e5-a189-3a51-8fca-86287669fd00 | -2.861 | -46.8406 | 2024-11-29 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 03d68d46-a25d-3edf-bc4e-2ecc7ffd579b | -5.0399 | -43.6205 | 2024-11-29 01:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 44ac6cb4-ff5f-3751-92d8-9877aa4e564e | -1.092 | -53.3954 | 2024-11-29 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 306f72e4-ae60-37e6-9f11-54b6db4696d8 | -2.966 | -53.3027 | 2024-11-29 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 6bd61491-ff67-3b85-b8d1-919d99a88236 | -4.4405 | -46.5754 | 2024-11-29 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 7aecb3ab-4554-34a0-bc11-e21cd7b2f01a | -2.8611 | -46.8186 | 2024-11-29 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 5b1e79cd-60a6-3955-a826-98739a84d996 | -2.6684 | -48.7767 | 2024-11-29 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 45f88fe4-2f76-335b-9d4f-b633d36b772a | -2.6499 | -48.7772 | 2024-11-29 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b7227a24-25b2-3820-b461-4bca2087b1eb | -17.5805 | -42.7483 | 2024-11-29 01:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| aca422c2-6852-39a0-87dd-af061d7c0cb1 | 1.8583 | -55.8018 | 2024-11-29 01:50:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2be9b251-2395-3ec1-ad1f-0647945f98f4 | -2.1351 | -54.906 | 2024-11-29 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| c5b57d90-802b-301f-8ff0-97c36d613f7b | -1.9726 | -46.4467 | 2024-11-29 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2dfe9783-e479-328e-a731-8e941679592d | -2.6498 | -48.7986 | 2024-11-29 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 705c3275-abd5-3f1d-96a0-5792071a021b | -2.8425 | -46.8193 | 2024-11-29 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9f850492-f79f-3500-819c-b911ebda80f3 | -3.3439 | -46.6912 | 2024-11-29 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f6f6e8dc-c98d-34f4-8811-6311b778a709 | -17.6457 | -57.5668 | 2024-11-29 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 3a22f44d-b93b-3eba-be90-6cd8f0b53ba7 | -2.1534 | -54.9057 | 2024-11-29 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 85be2bd2-fd55-30ce-8cff-0f0dc9481ca2 | -1.5869 | -53.8336 | 2024-11-29 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bd8d6c7f-8d8e-3fbb-b889-6486b01078c9 | -2.8665 | -45.5304 | 2024-11-29 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| abab9395-10f9-3597-9215-fd7545d4dd96 | -2.966 | -53.2824 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 1be59ca5-83c2-35b4-ab35-58b664a12352 | -3.3252 | -46.714 | 2024-11-29 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 20d4a05e-816b-3706-8c91-45f9c5d906b8 | -17.6457 | -57.5668 | 2024-11-29 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 6b7d5fd8-daef-36cb-a16b-c1b7d658f6de | -1.9726 | -46.4467 | 2024-11-29 02:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e62e575f-e6b9-3346-9c99-9d8afaf1a612 | -3.3439 | -46.6912 | 2024-11-29 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3306f60c-08d1-39c5-814e-deca6a1b0590 | -17.5805 | -42.7483 | 2024-11-29 02:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 3037f822-59f8-3d9f-b5f9-7203f55373e1 | -1.092 | -53.3954 | 2024-11-29 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 95370145-ada0-3b4a-a904-671f4fbe7c52 | -1.6997 | -52.4535 | 2024-11-29 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| defc5d10-8d29-3644-a857-d7b03c3524b1 | -2.9845 | -53.2617 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2b1a2596-1a6f-3e52-b946-eba99ad3867d | -1.5897 | -52.271 | 2024-11-29 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f4c15d8a-f363-365b-b776-d0f19def206f | -4.4405 | -46.5754 | 2024-11-29 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 775e1b33-b25c-3601-b6d4-6457c08faefa | -1.6074 | -52.6181 | 2024-11-29 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 025445e0-0334-3643-9067-3b2ba37c9294 | -2.6684 | -48.7767 | 2024-11-29 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 6fad093d-f450-316c-9df9-8b76fe0691df | -2.9844 | -53.2819 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 419.9 |
| 644cbc39-1930-32db-b817-0fda46b4afdb | -3.0028 | -53.2815 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0027ba2b-2994-3820-a96a-aec1b6dff8e9 | -2.966 | -53.3027 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e0793e66-643f-3d38-9c06-1f3c43ad6f33 | -17.5798 | -42.7731 | 2024-11-29 02:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| fc75e83d-796a-3dd0-bd71-c1ba9a6d7eb7 | -4.4404 | -46.5975 | 2024-11-29 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 830582f2-0ed6-3eb1-92b7-c6bdb6ea232c | -3.3253 | -46.692 | 2024-11-29 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 2d66e97b-d2f3-312b-ac6f-501bd70a5115 | -2.1351 | -54.906 | 2024-11-29 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 78e855ff-bbc3-37a4-a391-291c401294a3 | -2.1351 | -54.8861 | 2024-11-29 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e0f4aa0b-556c-3983-bbb9-e54da9d4b65d | -2.1534 | -54.9057 | 2024-11-29 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b31ed6b2-9c26-324f-b2e4-df2d52799dc5 | -2.9844 | -53.3022 | 2024-11-29 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 231.5 |
| dc6166ae-25c5-37db-9339-e7226679ed47 | -2.96 | -53.25 | 2024-11-29 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 063625ad-d4be-3066-ba6a-ed3c17b3fbb9 | -2.96 | -53.31 | 2024-11-29 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17f0391-07c4-3a50-9bd3-2d2e29db30ac | -2.99 | -53.31 | 2024-11-29 02:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f635eeb2-f9e8-3023-9c50-525d4b4a219a | -4.4404 | -46.5975 | 2024-11-29 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e7f50fbe-b06e-3aaa-9356-c6bb83b70428 | -1.5897 | -52.271 | 2024-11-29 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| dc93bb65-fe58-3756-86c8-fbd82a4825f8 | -3.3253 | -46.692 | 2024-11-29 02:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3946be36-6fc7-36be-b97a-23543bd715c2 | -1.092 | -53.3954 | 2024-11-29 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 49a47d79-838c-328b-b769-d91879217b05 | -1.9726 | -46.4467 | 2024-11-29 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 11ce78be-5545-3bd2-a110-fdf7e8f90dae | -3.2739 | -49.8844 | 2024-11-29 02:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 333200f9-a931-3d6c-8b8f-58cccddbac2b | -2.8611 | -46.8186 | 2024-11-29 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d757d7af-3f5f-3ef4-b9cc-bef6524e6c2b | -2.9844 | -53.2819 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 300.6 |
| 36f1e191-675d-358e-b0d4-d10f86244d11 | -17.5805 | -42.7483 | 2024-11-29 02:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 738cfd0c-b370-3b46-81e7-3432aaf1624c | -17.6007 | -42.7434 | 2024-11-29 02:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 388ddbe6-767e-3bba-a539-52db274e54db | -3.0028 | -53.3017 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0f6d83f7-c695-3a0c-90a8-9d2dc61015ba | -3.3439 | -46.6912 | 2024-11-29 02:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 76f020f5-b3e0-3ee9-81d0-452cadfed093 | -1.6997 | -52.4535 | 2024-11-29 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1d79f74d-afa7-3f87-acb6-2c6bcf1b52d0 | -3.0028 | -53.2815 | 2024-11-29 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2f222d1a-980a-36e6-b138-d4fa9297bac4 | -1.5869 | -53.8336 | 2024-11-29 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5370c40c-da52-3780-952a-b6210cc3a522 | -1.9541 | -46.4471 | 2024-11-29 02:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |


[Clique aqui para ver as próximas entradas](README14.md)
