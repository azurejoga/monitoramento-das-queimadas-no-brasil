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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d6aa6b3-3e73-3629-ad76-91b88a7c43ed | -6.9723 | -47.0937 | 2025-06-05 13:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d5b31365-039f-3909-a074-e186a2a40c3e | -13.5344 | -56.5672 | 2025-06-05 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 51e03b4f-4fb1-32f4-8b46-0d5f48270d3b | -11.3904 | -56.5565 | 2025-06-05 13:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d6b1f600-736d-3d91-9e40-d50637680383 | -6.991 | -47.0922 | 2025-06-05 13:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a974b02d-5fb3-3878-912a-b70a35ea6add | -13.5155 | -56.5488 | 2025-06-05 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 262.1 |
| 2c7d6d6b-6015-3c1e-a98e-fb4d88f667eb | -13.5152 | -56.569 | 2025-06-05 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 364.2 |
| 8ff89e1b-be76-3766-a200-81aea283051a | -13.5346 | -56.5469 | 2025-06-05 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e17effd1-c88d-3fdd-bdc7-7b89940cedcd | -8.7993 | -45.1044 | 2025-06-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 06d68be9-bdcc-3c2e-9117-19ed49b20728 | -13.5346 | -56.5469 | 2025-06-05 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0cce7f8e-b5bd-30ed-8786-eadb1e715c4d | -13.5344 | -56.5672 | 2025-06-05 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 09c2ad0a-c134-3f30-9a2d-624416a124fc | -6.991 | -47.0922 | 2025-06-05 13:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 293d0e5a-3826-3cd9-9cea-788c1193fe93 | -6.9723 | -47.0937 | 2025-06-05 13:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ce665032-dfe9-3c21-85b7-98cde2720cce | -13.5152 | -56.569 | 2025-06-05 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 9e046618-f115-3276-a58b-57324e75046c | -13.5155 | -56.5488 | 2025-06-05 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 9a897d68-05fe-3054-96ba-c1089a53dc3e | -11.3904 | -56.5565 | 2025-06-05 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5a4610a4-f4cb-37ce-83f9-a06710dc1fb9 | -13.5346 | -56.5469 | 2025-06-05 14:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7b2dbaea-9ed0-3e3f-b6ef-3e77a52d0b64 | -8.1171 | -45.3807 | 2025-06-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e2390962-47ce-3dd5-a590-d93a4d352826 | -6.991 | -47.0922 | 2025-06-05 14:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 76bc9f2c-4886-38c2-9efe-b046eac39ee7 | -6.9723 | -47.0937 | 2025-06-05 14:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f17a7d88-4ea9-359d-a767-dbe8f85bfaf1 | -12.5175 | -57.2231 | 2025-06-05 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3a159a64-8513-3424-9c6d-91d7151dcf19 | -8.1173 | -45.3579 | 2025-06-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b1745576-3a36-3081-83c9-e96d3e898af5 | -13.5155 | -56.5488 | 2025-06-05 14:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 179.0 |
| d30f6b3d-1f36-31ca-ba5b-1a4d93ed4fa0 | -8.7993 | -45.1044 | 2025-06-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 685274e3-eee3-3113-8f98-bed8ddc5f4c3 | -13.5152 | -56.569 | 2025-06-05 14:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 257.9 |
| e95db0f0-4e36-33c0-8f9c-17f963d9c528 | -12.5175 | -57.2231 | 2025-06-05 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 87955569-80e9-3911-bbad-c83a565182d5 | -6.991 | -47.0922 | 2025-06-05 14:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5bb35a11-63ab-37fd-bcff-af8c4a92ada8 | -6.9723 | -47.0937 | 2025-06-05 14:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 41e5aecc-6c99-3c56-8210-5c6c58108c82 | -8.1171 | -45.3807 | 2025-06-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 58f78cba-793e-3dc8-99ca-7acfb301be22 | -13.5152 | -56.569 | 2025-06-05 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 304.0 |
| d820819e-99ec-3819-b8d3-855db3924afb | -13.5346 | -56.5469 | 2025-06-05 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 81dc9202-0925-39ef-b14e-46f18748968a | -13.5155 | -56.5488 | 2025-06-05 14:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 7262ae49-8716-39a4-b419-0b30aeed8565 | -10.2941 | -57.138 | 2025-06-05 14:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cf306d46-c426-3731-afea-ab720bba7c43 | -8.1173 | -45.3579 | 2025-06-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 5b1542d9-51ee-3f2d-835f-606acca8b3d4 | -6.2411 | -43.3677 | 2025-06-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 254cef3e-0ad7-3efd-839a-25bc92fda5d0 | -8.7993 | -45.1044 | 2025-06-05 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5af359c1-4ad3-3f25-b022-78e00bb2ff4c | -11.3904 | -56.5565 | 2025-06-05 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bdb1f7a2-a708-34f3-934d-f3c3888e4d92 | -13.5155 | -56.5488 | 2025-06-05 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| b8fe0bba-ab80-3ccf-9e86-55401f153154 | -6.2411 | -43.3677 | 2025-06-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c0e09696-2f9f-3ef5-9cf9-29b5657d9139 | -13.5152 | -56.569 | 2025-06-05 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 325.7 |
| 668726bb-1241-39e6-a918-3b51daed13e8 | -10.2941 | -57.138 | 2025-06-05 14:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c75898d2-cd3c-3be4-a053-716a89630b98 | -8.7993 | -45.1044 | 2025-06-05 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 22a735ac-2369-3881-8328-00b1517f04be | -6.9723 | -47.0937 | 2025-06-05 14:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| f7d61bc7-4de9-3e41-8e09-cc356c61a48e | -13.5346 | -56.5469 | 2025-06-05 14:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9b2f6358-31d1-3729-bde2-34f6d856ed38 | -11.3904 | -56.5565 | 2025-06-05 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 120f4d3c-5949-3242-9deb-da59169ac5cd | -6.9791 | -42.9034 | 2025-06-05 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 3b394876-6439-327d-829c-7465c6447900 | -11.3904 | -56.5565 | 2025-06-05 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ad6f676c-0733-328b-a6ab-23c992cd11e1 | -8.7993 | -45.1044 | 2025-06-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 789a3f70-7f48-3a49-a293-047e7839515f | -13.5346 | -56.5469 | 2025-06-05 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 58dfc4f0-5478-38ac-b23b-426088a85182 | -13.5155 | -56.5488 | 2025-06-05 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 81d8007a-6b77-3213-a196-07f0f9569e6c | -6.9791 | -42.9034 | 2025-06-05 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 3948217b-3e40-3d78-8417-02b769270d01 | -13.5152 | -56.569 | 2025-06-05 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 7f8ead38-c0eb-3d6e-b312-511e6fc69d1d | -12.5175 | -57.2231 | 2025-06-05 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1f911c5a-3379-3c6e-934e-5664732d5d7b | -6.9723 | -47.0937 | 2025-06-05 14:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| e3383c6a-ee4b-3060-80f1-dd58748d4018 | -6.2411 | -43.3677 | 2025-06-05 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| f6e54bfd-3bfb-3e05-951a-0884c18b7314 | -8.1171 | -45.3807 | 2025-06-05 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cb024c44-bfa0-38fc-9b76-9484e732e1e7 | -6.9791 | -42.9034 | 2025-06-05 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| f95b9360-3f45-3815-96ac-335732e5314b | -11.3904 | -56.5565 | 2025-06-05 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| afdf4ce4-9748-3f61-83c3-99c29ad7fe12 | -13.5155 | -56.5488 | 2025-06-05 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 969b3fce-945e-3be4-b0c7-b5bdbad31d61 | -13.5346 | -56.5469 | 2025-06-05 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 34844d05-e883-376b-b10e-f31def0e5c91 | -13.5152 | -56.569 | 2025-06-05 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 59e17e09-6065-3f6b-94b0-7a57310c3372 | -12.6767 | -58.2262 | 2025-06-05 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |


