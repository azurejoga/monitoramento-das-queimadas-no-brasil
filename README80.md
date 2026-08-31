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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8853fd03-c0b2-32fa-8823-7d7cee58e38d | -6.1109 | -57.684 | 2026-08-31 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7926c60f-1d30-3923-8282-e79a88cc5adc | -7.98 | -44.2731 | 2026-08-31 07:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6779e2cf-3691-3403-89b7-6666fb0478b0 | -6.1295 | -57.6637 | 2026-08-31 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b53442d4-973a-3164-adf3-395f4c6b3b07 | -6.622 | -58.5965 | 2026-08-31 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 54d3ff45-6aed-3463-a566-0c4a601395e4 | -6.6036 | -58.5972 | 2026-08-31 07:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ae036761-2617-31c4-bf23-401e4c76dc00 | -5.2548 | -55.8907 | 2026-08-31 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0bd6b5cd-fef6-309b-b79a-8252939a80b1 | -7.9797 | -44.2962 | 2026-08-31 07:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 093bffc6-a019-3750-a1e1-d1816fdcebb4 | -5.2547 | -55.9105 | 2026-08-31 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cf041871-335d-384e-a5e1-8c662676dede | -6.1295 | -57.6637 | 2026-08-31 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 8806647b-9b2e-3e46-8cb9-4f8522187a0b | -6.6036 | -58.5972 | 2026-08-31 07:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 68bad00f-dcf0-396b-b157-dab94059e85f | -5.2547 | -55.9105 | 2026-08-31 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ab396c92-0ac2-3f9f-8d14-3252eb6c5972 | -6.1294 | -57.6833 | 2026-08-31 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 8878575f-8bfe-3f71-8b4a-c8bedcde5694 | -5.2548 | -55.8907 | 2026-08-31 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9804e9a4-62d5-3647-a5f9-c5dd1a9025d5 | -5.2362 | -55.9112 | 2026-08-31 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 413bc91f-bf3f-3970-8cd3-1008c68dbfda | -6.622 | -58.5965 | 2026-08-31 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5b6bc43d-c6bb-3dc5-ab97-d8450b57354f | -6.1295 | -57.6637 | 2026-08-31 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c83ea55f-830b-337f-a5bd-95c9e7d0cd4a | -6.6036 | -58.5972 | 2026-08-31 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 4a3d2e97-a101-387e-b9ee-44928d206539 | -6.1294 | -57.6833 | 2026-08-31 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ea1358a1-b858-32fb-8b6c-6f68dbba3516 | -5.2548 | -55.8907 | 2026-08-31 07:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5c6d942a-4f67-3e65-afbd-65fc4aa481c5 | -5.2547 | -55.9105 | 2026-08-31 07:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 416468d5-ec53-370d-b13b-1581ed3cf58e | -6.1109 | -57.684 | 2026-08-31 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 178060d6-fec4-369e-8b96-9e6abd3d7625 | -6.1111 | -57.6645 | 2026-08-31 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 8925d021-5def-3438-88e9-6fc20a1441ff | -5.2548 | -55.8907 | 2026-08-31 08:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f6ded4f9-32e3-3d77-ac76-d920043b93de | -6.6036 | -58.5972 | 2026-08-31 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 34af4bb7-498a-330f-b195-93037b085265 | -6.1109 | -57.684 | 2026-08-31 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e0ebfa0f-d6a2-368d-9d52-e6983eba05c2 | -19.154 | -57.3978 | 2026-08-31 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 8b39119d-980a-3936-9cee-a5501b86b6b1 | -6.1294 | -57.6833 | 2026-08-31 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2fdf9687-9d4e-384a-ab48-21792c1ee2f0 | -6.1295 | -57.6637 | 2026-08-31 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cce8a176-8608-3686-8a86-1d13b94a40b1 | -6.622 | -58.5965 | 2026-08-31 08:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4c2fe404-9a33-3339-a976-7fea1b96875c | -5.2547 | -55.9105 | 2026-08-31 08:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 822abacd-5f2c-3bfb-86ad-77b0acc7fb58 | -6.1111 | -57.6645 | 2026-08-31 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f3055047-ae9b-30e4-9022-84df105a4e7c | -6.1295 | -57.6637 | 2026-08-31 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8a313848-270e-3ed8-89df-067cae2562de | -5.2548 | -55.8907 | 2026-08-31 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 10f71523-c30a-3c4f-b75f-bd3a9194cee6 | -5.2362 | -55.9112 | 2026-08-31 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 89f3fe65-d3b5-34d4-8364-6e911fa0abb3 | -19.154 | -57.3978 | 2026-08-31 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 55edace1-9e68-392c-b3b6-ca31436efc85 | -6.6035 | -58.6166 | 2026-08-31 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 462a2140-797a-39a7-9a80-54f4d901f1fe | -6.6036 | -58.5972 | 2026-08-31 08:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 0d05882b-008e-32d3-891f-199d51b574f2 | -6.1294 | -57.6833 | 2026-08-31 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 522730c1-a58d-3336-9c81-f2e6f3a1ae42 | -5.2547 | -55.9105 | 2026-08-31 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 302bd976-c6ec-33a3-8b5e-24a3b7090764 | -6.6036 | -58.5972 | 2026-08-31 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 7552e15c-ffdf-3923-92f5-d74c13f74ed7 | -6.1295 | -57.6637 | 2026-08-31 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2d3af57c-2dbf-35ba-b7aa-eae470a722d1 | -5.2362 | -55.9112 | 2026-08-31 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6382ef02-bcce-3b64-919a-32d5c14b5370 | -19.154 | -57.3978 | 2026-08-31 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 19a3d00a-ab07-3f96-86c8-e5bab49d7e11 | -5.2548 | -55.8907 | 2026-08-31 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 35e1b4c9-c447-3ea0-88e5-781bc744c497 | -5.2547 | -55.9105 | 2026-08-31 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d6432f4d-1160-33d2-841f-aaf4bef8ae16 | -6.1294 | -57.6833 | 2026-08-31 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2d9d3643-49fd-373b-a48d-f3d4231b1368 | -7.3118 | -60.5897 | 2026-08-31 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8651d8a2-d400-35d7-a589-4e856e513114 | -7.3119 | -60.5706 | 2026-08-31 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 00f876d3-7684-3545-a1df-18ba173dc67e | -6.622 | -58.5965 | 2026-08-31 08:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 640dfeb2-7953-30e3-befa-c1da0051bf71 | -7.3118 | -60.5897 | 2026-08-31 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d2feeb26-29e9-3a0e-b2dd-ea6eeeae3243 | -6.622 | -58.5965 | 2026-08-31 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ad5049b9-3f68-3c3e-9540-c6f77900edc2 | -6.1109 | -57.684 | 2026-08-31 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a44021cc-b269-300c-a079-d5dc978bf9c5 | -6.1294 | -57.6833 | 2026-08-31 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 91d89262-165f-3597-8722-3b994af3595c | -7.3119 | -60.5706 | 2026-08-31 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 99347b3f-0eff-3b98-9353-f8b55826f5ec | -6.1295 | -57.6637 | 2026-08-31 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e0789aff-f3e5-3188-b401-f95846030b26 | -5.2548 | -55.8907 | 2026-08-31 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 601abe1b-e4e0-34fe-bf8e-c0c5b270c990 | -6.6035 | -58.6166 | 2026-08-31 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| be1ae6a2-f119-38a9-9657-6d1691edc1ba | -5.2362 | -55.9112 | 2026-08-31 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5f8109df-e927-3f02-817e-e17a7c44ef10 | -19.154 | -57.3978 | 2026-08-31 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 8651e70e-46c4-371c-81e1-abce6e5a96a6 | -5.2547 | -55.9105 | 2026-08-31 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 23a55e4d-c1d9-333d-9542-dde81830d471 | -6.6036 | -58.5972 | 2026-08-31 08:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 54de98c6-ef85-3994-85f7-7f20007e3440 | -5.2548 | -55.8907 | 2026-08-31 08:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cf9a12a7-95ef-3e5a-8238-492c774f784e | -7.3119 | -60.5706 | 2026-08-31 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c774d1fd-9839-36bd-a4d3-0d09fbc1e4ee | -19.1543 | -57.377 | 2026-08-31 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| ab2cf27e-c223-3041-af58-c2a463a3e7f4 | -6.1111 | -57.6645 | 2026-08-31 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 60448b71-37cb-3afe-b468-442525f0bb6d | -6.1295 | -57.6637 | 2026-08-31 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 97d1c5dd-4b20-3f1d-8a2a-4138f83ad001 | -18.2904 | -52.6818 | 2026-08-31 08:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b293dfcb-1348-3788-b4b8-8b7ace7b00cd | -19.134 | -57.4005 | 2026-08-31 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| b98c5043-4298-3448-a513-2835858d1ec5 | -18.2704 | -52.6851 | 2026-08-31 08:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 229a6458-102a-3860-a9b7-6335d4bce43b | -6.1294 | -57.6833 | 2026-08-31 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9a7e79d6-1498-3bdf-b71c-a7c670dab291 | -5.2547 | -55.9105 | 2026-08-31 08:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 80b89090-f86d-306c-937e-fc78c731b5d7 | -6.1109 | -57.684 | 2026-08-31 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5923ad66-4827-30d8-856b-a02a91482891 | -7.3118 | -60.5897 | 2026-08-31 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ac94d24b-13f9-3204-b36f-e2b2aa371714 | -19.154 | -57.3978 | 2026-08-31 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.6 |
| c10f0a38-a993-3582-8256-df1163833ef0 | -6.622 | -58.5965 | 2026-08-31 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 96b00a0f-c0b9-3d18-bc86-7dda0089754a | -5.2548 | -55.8907 | 2026-08-31 08:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2e4262a9-a198-3598-9176-4f763fe54bab | -6.6035 | -58.6166 | 2026-08-31 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ed91da42-7cd5-305f-bbcd-986c569e7b21 | -19.154 | -57.3978 | 2026-08-31 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.2 |
| 01f1470a-01dd-3f43-a9db-4bf8a81ab08e | -6.1109 | -57.684 | 2026-08-31 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6483deb4-62d5-31a4-85a0-d5da789a08dc | -6.1111 | -57.6645 | 2026-08-31 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 7f1ed0e8-cfd2-3e34-97f6-c86ed5b19913 | -19.1543 | -57.377 | 2026-08-31 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 1da65e82-09f3-3461-b9fb-367634fb3626 | -6.1294 | -57.6833 | 2026-08-31 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f042f46e-99f7-376d-9dc7-aa7fd6f9b54c | -7.3119 | -60.5706 | 2026-08-31 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4abbc4a5-b448-3869-b972-32c5d1735873 | -5.2547 | -55.9105 | 2026-08-31 08:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 15b7f4ab-811a-3a49-9ff2-ae68298b123a | -6.6036 | -58.5972 | 2026-08-31 08:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 31028dde-338d-3de5-b3ae-510b52cac527 | -7.3119 | -60.5706 | 2026-08-31 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 702305ba-62fd-34fd-884c-3c95214d936a | -5.2547 | -55.9105 | 2026-08-31 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| fe583177-7825-36d2-b2ac-4fd332d19306 | -6.1109 | -57.684 | 2026-08-31 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 6d008b32-5d55-3e58-aa54-67f3ab9d5db7 | -6.6035 | -58.6166 | 2026-08-31 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8aad302d-3609-395a-be99-942a6938b81b | -6.1294 | -57.6833 | 2026-08-31 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cbd7e247-5386-3e84-a867-fef08b4a2cc5 | -5.2362 | -55.9112 | 2026-08-31 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1f1ca3b3-1629-3967-8745-1a2d2c86ed9c | -6.6036 | -58.5972 | 2026-08-31 09:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 52db1be3-d121-3d3d-9ce6-d4abd13a7b11 | -5.2548 | -55.8907 | 2026-08-31 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7ba14818-7c05-3698-bd35-29a22eb4885c | -6.6036 | -58.5972 | 2026-08-31 09:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| eb9fa314-cdbe-312b-ae57-8669e8f55ce8 | -6.1294 | -57.6833 | 2026-08-31 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| cd70d4ca-23ba-3a89-9c10-2dae5051fa4f | -6.1109 | -57.684 | 2026-08-31 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fa7e516f-6d1a-3ce7-9c91-a78103cbd1ba | -19.154 | -57.3978 | 2026-08-31 09:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| abaa1ca9-daab-30db-9953-fffc67dce1bd | -7.3119 | -60.5706 | 2026-08-31 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f9c25af0-bec4-3f93-ab98-09e7ea1a8f30 | -7.3118 | -60.5897 | 2026-08-31 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 4d7cad49-70a8-3e64-9567-5d93efddb27e | -5.2547 | -55.9105 | 2026-08-31 09:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |


[Clique aqui para ver as próximas entradas](README81.md)
