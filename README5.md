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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc6de03f-df8e-30cd-9cad-d0d84669cc56 | -28.7491 | -55.64649 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| a6e540b2-9de1-3562-9963-9ca7d8eff414 | -28.76074 | -55.61604 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 37.4 |
| 60775ab0-1f2b-3b96-bffa-5bc388b66447 | -28.74685 | -55.63007 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| ccf7e0cc-ee4a-3921-924f-df18d0f26f85 | -28.75892 | -55.59568 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| a4d75b77-88ac-350c-a9f9-110abd665926 | -25.19645 | -49.32449 | 2025-01-13 05:08:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 51fb0fe7-f4f9-33c8-abff-c02ac08b149b | -28.75358 | -55.6431 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| 72948b2a-c57c-3f96-9904-4cade4b67ada | -28.74729 | -55.62611 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 628e2515-f5a1-3e79-ac8f-d38e09bd9045 | -28.75492 | -55.63124 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 41.1 |
| 6d69e90b-3dee-3487-8a64-6e55274ce34b | -28.76252 | -55.60026 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| c026755a-94e0-3cc1-9089-d16671ac88ad | -28.74999 | -55.63858 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| b8b9a94f-c4bb-3731-aeb3-ac5ace1344b7 | -28.7464 | -55.63405 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| f9fd5563-c7f2-3f36-8380-0e194d1c1dd5 | -28.76207 | -55.60421 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 28.9 |
| 9bb8ed0b-0c22-342c-b120-82f37d1c2db6 | -25.19038 | -49.32829 | 2025-01-13 05:08:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 41a36f20-f9b3-3858-98c6-2b3064f88b2e | -28.75043 | -55.63462 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| cc8baf3a-9335-3c51-96d7-3845fbefe5ee | -28.7567 | -55.61542 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 37.4 |
| 44652c8f-254e-3b54-a1f3-f1801d9358bc | -28.75939 | -55.62793 | 2025-01-13 05:08:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 41.1 |
| 0d11a98e-a769-3050-bdaf-e2976d150eb2 | 1.11861 | -59.4568 | 2025-01-13 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27911930-7544-3ec6-a349-3997403701bd | 0.95236 | -59.4664 | 2025-01-13 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8f6f847-c8a9-37fa-8f8f-413c39a0467c | 3.18219 | -60.21004 | 2025-01-13 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6fe04eb-9987-366c-8243-2661287ce06c | 1.17716 | -60.49765 | 2025-01-13 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 762f86b5-73ea-3197-b48f-054bc2384a58 | 3.57522 | -60.40794 | 2025-01-13 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2828bf-1d77-31e5-96b1-8a92f453a16a | 1.11942 | -59.46182 | 2025-01-13 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2958619b-9047-34f0-92a6-78aab7fc18eb | 1.17784 | -60.50191 | 2025-01-13 05:52:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecdb7727-d74d-3cca-9200-ad856ede4b04 | 0.5559 | -59.69529 | 2025-01-13 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08e662e-0801-373f-b5f1-41b141abfacb | 0.99313 | -60.56181 | 2025-01-13 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10abd96f-cc4d-3bc5-baff-f9f06fec3026 | 0.99751 | -60.56112 | 2025-01-13 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1656393-1ed3-33c8-b7e8-9f3de8af4144 | 0.7484 | -60.1777 | 2025-01-13 05:54:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46521a71-b50d-36f4-9577-ed5f09c59352 | 0.55981 | -59.68955 | 2025-01-13 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d1baff4-e907-384a-83af-55cefe146040 | 0.7645 | -60.09386 | 2025-01-13 05:54:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17942948-b0c3-3e07-817d-3bee4fba685f | 0.91211 | -60.38789 | 2025-01-13 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dbd546f-e5b8-373d-b67c-07aa55cbd249 | 0.91125 | -60.38925 | 2025-01-13 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf10e9d-ce53-380d-aa04-50a3b9018311 | -28.75317 | -55.63709 | 2025-01-13 06:03:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.2 |
| 33b2bc5e-246d-38b5-80d0-e54baf7abb15 | -28.75471 | -55.62486 | 2025-01-13 06:03:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 32.4 |
| 7bb747be-d7b9-3c56-9e78-a2bac6dd1c3d | -28.7578 | -55.6004 | 2025-01-13 06:03:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 17.1 |
| 2d3c22a6-fc2b-37bf-9177-7b5125e8fee5 | -28.74342 | -55.6356 | 2025-01-13 06:03:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 15.2 |
| 5ed8c62f-9679-365e-9ac8-7c1aab3bb905 | -28.75626 | -55.61263 | 2025-01-13 06:03:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 50.0 |
| d0a32635-e582-30eb-b14c-210fbb298872 | 2.93859 | -61.1108 | 2025-01-13 06:18:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdcff56c-792f-3dce-b415-c85acc45661e | 2.93405 | -61.1078 | 2025-01-13 06:18:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be08767-1e10-322c-80e7-92de5e672f79 | 2.93225 | -61.11188 | 2025-01-13 06:18:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706c4c5a-843c-35e4-b5a7-c864e5d5b159 | 2.93494 | -61.11291 | 2025-01-13 06:18:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39082805-3696-388b-8d38-b0b21231f9e0 | -28.7599 | -55.6114 | 2025-01-13 07:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.5 |
| ef43b1ed-aad4-3eea-8353-3b33394b854a | -28.7592 | -55.6345 | 2025-01-13 07:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 89.4 |
| 9d92d1f8-8007-3174-b58f-465bf25d2b5c | -28.7592 | -55.6345 | 2025-01-13 08:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 66.7 |
| b2394560-d233-3fa6-a107-2345f2f63f15 | -28.7592 | -55.6345 | 2025-01-13 11:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 148.2 |
| d3027129-ee62-3aa5-a95e-602984d44649 | -28.7592 | -55.6345 | 2025-01-13 11:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 150.0 |
| a5733b2c-39c1-336e-a5c3-c09a105f51d0 | -28.7592 | -55.6345 | 2025-01-13 11:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 194.2 |
| d0c32a50-5f8c-3db2-a256-376a15a62129 | -28.7599 | -55.6114 | 2025-01-13 11:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 106.7 |
| 662fe552-7f66-3a89-b1e0-88e01163c862 | -28.7592 | -55.6345 | 2025-01-13 11:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 255.6 |
| 590d98ea-e21f-3ad1-b2eb-89856145468a | -28.7599 | -55.6114 | 2025-01-13 11:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 105.7 |
| f0c8f258-4fc6-3325-8f34-f62d0ffb0c3e | -28.7592 | -55.6345 | 2025-01-13 11:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 157.3 |
| a273f341-2862-3286-b8cb-54e4c50b61eb | -28.7592 | -55.6345 | 2025-01-13 12:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 99.7 |
| 57edc507-fe25-3220-90da-de633405e7fe | -28.7592 | -55.6345 | 2025-01-13 12:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 108.6 |
| 1658d500-a89d-3d74-a075-b77fbaf8a3b2 | -28.7592 | -55.6345 | 2025-01-13 12:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 94.0 |
| 0384f614-ac53-3b63-bb21-1b9d7974ac2b | -28.7599 | -55.6114 | 2025-01-13 12:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 95.3 |
| 0c28785a-3114-3173-bb68-93048a805646 | -28.7592 | -55.6345 | 2025-01-13 12:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 129.7 |
| a432e1e5-7afd-3cba-baae-649988b1204d | -28.7592 | -55.6345 | 2025-01-13 12:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 108.7 |
| cfc1a08f-c5d8-343b-ac56-2bd0f38057da | -28.7599 | -55.6114 | 2025-01-13 12:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 97.9 |
| 1253f042-f053-305a-81ea-7c6715c46512 | -28.7592 | -55.6345 | 2025-01-13 12:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 96.3 |
| 284d96b9-a069-34af-9c4d-c7a4577a6e53 | -28.7592 | -55.6345 | 2025-01-13 13:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 101.6 |
| be7b66b6-d5de-3682-a3c6-ae5607617e49 | -28.7592 | -55.6345 | 2025-01-13 13:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 118.5 |
| 36927c7a-8e2a-33c1-84f6-46f239c4f1e8 | -28.7592 | -55.6345 | 2025-01-13 13:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 104.5 |
| a5448f7d-3e81-3126-816f-5a08bf0e82eb | -28.7599 | -55.6114 | 2025-01-13 13:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 117.7 |
| 4173f482-1dda-3cda-8b37-0fc67aec52aa | -28.7592 | -55.6345 | 2025-01-13 13:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 152.6 |
| 85f74a0d-38ba-36e5-aa49-be1650e8c587 | -28.7592 | -55.6345 | 2025-01-13 13:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 102.9 |
| ce9403a2-42f6-3320-9449-a8068c25b4a9 | -28.7592 | -55.6345 | 2025-01-13 13:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 134.3 |
| 7b4d0985-aa64-390c-b137-e6c26c8f8050 | -28.7599 | -55.6114 | 2025-01-13 13:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 125.7 |
| faf8cf90-d63f-3539-9eea-8dc1763bd9cd | -28.7599 | -55.6114 | 2025-01-13 14:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 138.5 |
| ca0722d5-0966-3fb9-be12-2fc04a82836c | -28.7599 | -55.6114 | 2025-01-13 14:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 112.3 |


