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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 787afe8f-d3c3-369d-af4b-4a0e1bb96e7d | -10.498 | -64.5193 | 2026-08-28 08:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3bbed022-ad05-3c60-8d14-8035214193f5 | -6.1656 | -57.7988 | 2026-08-28 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 79128e3d-232f-36bb-bde7-3bb9c85ecff6 | -6.1657 | -57.7793 | 2026-08-28 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| a579dbc8-a5d8-311c-b047-b0724023c019 | -16.1444 | -58.6073 | 2026-08-28 08:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 5c4b4dfb-ab19-38d3-8de4-49ee12071987 | -10.5166 | -64.5186 | 2026-08-28 08:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 51b1c449-2e7d-3822-a360-203587b95a60 | -6.1656 | -57.7988 | 2026-08-28 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 43f1dd04-609f-351f-9f38-64ac45099069 | -10.498 | -64.5193 | 2026-08-28 08:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 37617115-e886-3635-8384-c230c3ec43ab | -10.4981 | -64.5005 | 2026-08-28 08:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b1715d91-5222-3201-b4f3-914212a7ca4b | -6.1657 | -57.7793 | 2026-08-28 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 52dcc4f3-ed20-37fa-bcb1-20d6849a0138 | -10.5166 | -64.5186 | 2026-08-28 08:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3e5550fb-d4b5-34fb-9690-977f2edc706d | -10.4981 | -64.5005 | 2026-08-28 08:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e4aeb9bd-21b7-3a57-82ef-a6748468ace4 | -10.498 | -64.5193 | 2026-08-28 08:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4c539463-d4f6-3f0d-9749-69c689b2ef79 | -6.1656 | -57.7988 | 2026-08-28 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 0d76cc79-7bd4-3b10-9f41-7740e0ab459b | -6.1657 | -57.7793 | 2026-08-28 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 41c8cd9e-51f4-304b-ac95-6bfd37145e9b | -12.2468 | -50.577 | 2026-08-28 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 30521d1d-2688-3d57-81bc-71cbd24c26dd | -6.1656 | -57.7988 | 2026-08-28 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7ac4ef3d-b6cc-35ad-9b8a-6ae6376e7141 | -10.498 | -64.5193 | 2026-08-28 08:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 762e4ce2-287d-3193-9463-29f86ac25d40 | -6.1657 | -57.7793 | 2026-08-28 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 559add98-ed32-3f2a-8be8-83bc79b7d1a7 | -12.2472 | -50.5555 | 2026-08-28 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| bab2c032-3953-3abd-a026-7fafd4826735 | -10.4981 | -64.5005 | 2026-08-28 08:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b78c29d7-dbfb-3a6f-b621-43b647d1ef60 | -12.2663 | -50.5532 | 2026-08-28 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0a9d9905-ecc1-37c1-8668-f7d560eabfab | -10.5166 | -64.5186 | 2026-08-28 08:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a7e0307d-99f7-3825-8bb1-50cad9acda55 | -12.285 | -50.5724 | 2026-08-28 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 22890010-db3e-3f92-8932-dcbcf08606b7 | -12.2659 | -50.5747 | 2026-08-28 08:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 1fc234f4-7891-3df2-8b6c-9dd53cfde0ba | -6.1657 | -57.7793 | 2026-08-28 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e5a8e5ce-3abe-3598-9563-19873ad1987c | -10.498 | -64.5193 | 2026-08-28 09:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a84ab5ab-7844-38f8-a92e-ba6a8f0bccbc | -10.4981 | -64.5005 | 2026-08-28 09:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d867c001-36ad-3b1c-99f5-631a78e13dc9 | -6.1656 | -57.7988 | 2026-08-28 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 323ce237-0765-3c8e-801f-a570604d74d0 | -10.5166 | -64.5186 | 2026-08-28 09:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7f67b29e-2bf5-3ad0-aa92-d5cde543ee45 | -10.4981 | -64.5005 | 2026-08-28 09:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c5fb6b9a-89da-3ce4-af8c-993518fbe4ac | -6.1657 | -57.7793 | 2026-08-28 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| bd836294-953f-3f82-bd07-c07f8a871176 | -10.498 | -64.5193 | 2026-08-28 09:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a3771897-2c29-30b0-8757-41bf22c885be | -6.1656 | -57.7988 | 2026-08-28 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 590b1cbc-94a9-37b2-811d-a6b7dce0b2db | -10.5166 | -64.5186 | 2026-08-28 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 37fc719c-3a8e-350d-8620-2e4099980b1f | -10.498 | -64.5193 | 2026-08-28 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ddf22264-f42c-30e3-93ec-91327f2a8eee | -10.4981 | -64.5005 | 2026-08-28 09:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9db92fae-cc74-37da-9661-6cb62cade19c | -12.2659 | -50.5747 | 2026-08-28 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e42b852b-d43b-344f-82cc-2a2069f50f69 | -12.2472 | -50.5555 | 2026-08-28 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 21554d58-e470-3b2f-b1dc-9e265da8de74 | -12.2663 | -50.5532 | 2026-08-28 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| fa54ab4a-972e-333c-b616-7b0985de10af | -10.4981 | -64.5005 | 2026-08-28 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 89d8be62-ad5a-3fc1-8ee4-2fa3c9687b93 | -10.5166 | -64.5186 | 2026-08-28 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f4d49828-3874-30ec-8009-1c44ac7d8beb | -12.285 | -50.5724 | 2026-08-28 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f0a2b185-ac37-3f7c-98e9-42a47a45801d | -10.498 | -64.5193 | 2026-08-28 09:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d2a06ec5-3a86-314b-8dc3-6e6d6c43df7a | -10.498 | -64.5193 | 2026-08-28 09:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8a8a2999-2997-346a-83c5-096b7cf78c5f | -10.5166 | -64.5186 | 2026-08-28 09:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e4b96a48-7c07-3a22-a685-c03dd37a2de4 | -10.4981 | -64.5005 | 2026-08-28 09:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9785bf83-1db4-379d-939d-e4a77296e615 | -11.8239 | -47.2178 | 2026-08-28 09:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 20a05092-d84f-3835-9a1d-d2a40fd903d1 | -12.2663 | -50.5532 | 2026-08-28 09:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b3ae971a-31fc-327f-b042-1aaaaa4e0314 | -12.2663 | -50.5532 | 2026-08-28 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| f94c35fb-befb-37ac-823d-3dee6fecf5ea | -12.209 | -50.5601 | 2026-08-28 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6fb546f2-fd68-362a-a696-4a97819d433e | -12.285 | -50.5724 | 2026-08-28 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 45521304-f27d-3836-a6e3-6a42b9cc715f | -12.285 | -50.5724 | 2026-08-28 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 294f9c7c-905c-3d54-99d8-65ef6403d6bd | -12.2663 | -50.5532 | 2026-08-28 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 08cb87fe-bdaa-315e-a976-9f75b194d1af | -12.2659 | -50.5747 | 2026-08-28 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 074887da-ee32-3d59-a226-b4ccfb050f7a | -12.209 | -50.5601 | 2026-08-28 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 66106232-0380-3486-9296-d2f097a03dde | -12.2854 | -50.5509 | 2026-08-28 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 620d26f5-fe46-3fdf-894f-6a7eb196af55 | -12.2659 | -50.5747 | 2026-08-28 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 685aff07-5434-3e99-bd7a-8dd4837e310d | -12.2659 | -50.5747 | 2026-08-28 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 93281ad1-d590-30c2-9095-c00d820a9d3e | -10.899 | -50.5159 | 2026-08-28 11:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 117b6eef-8741-3fa3-a229-b90eed3dbfaa | -12.2847 | -50.5938 | 2026-08-28 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7ae31fbd-7e37-3de9-97d4-2adb4b3a59d5 | -10.8801 | -50.5179 | 2026-08-28 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 840e7520-3d94-3c95-a532-feca0c3e3406 | -10.899 | -50.5159 | 2026-08-28 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 3be115a4-b4b4-39e5-943b-0447b04bbff2 | -10.918 | -50.5138 | 2026-08-28 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| cd484774-be0e-3062-8177-6195f7765151 | -12.2659 | -50.5747 | 2026-08-28 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 80097bd3-4874-3fb1-bdbe-3f6d58d7e48e | -10.899 | -50.5159 | 2026-08-28 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 35975e0b-96fa-3dbf-9dc9-e7574e316017 | -10.8801 | -50.5179 | 2026-08-28 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 68ce434a-dab9-3fa8-8350-3db8d2bfb35d | -2.7304 | -47.0424 | 2026-08-28 11:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 86fc2cde-9aae-33aa-bb6a-e63300dbc48e | -10.918 | -50.5138 | 2026-08-28 11:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 80146675-b095-314e-a89b-36664692b030 | -10.8992 | -46.6442 | 2026-08-28 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 27456572-51a8-3ca6-98c8-9724a687f648 | -10.899 | -50.5159 | 2026-08-28 11:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| f1dd1261-3803-3d48-84ee-c03af0e29810 | -2.7303 | -47.0644 | 2026-08-28 11:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| dc88e1ba-afdd-36ff-b144-563ec373eb70 | -11.2493 | -45.0501 | 2026-08-28 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 777198cc-c3f1-3d57-8769-3ae793f6a5b0 | -10.8996 | -46.6216 | 2026-08-28 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| cdd08244-f217-365e-af31-1a981c76be3e | -12.0158 | -47.1693 | 2026-08-28 11:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8c9af795-af1f-3ce6-9a75-cf8b512c9d60 | -2.7304 | -47.0424 | 2026-08-28 11:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 402fff62-b460-37c7-a4ea-a079d6ee44a8 | -2.72773 | -47.0374 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 77d4308d-553b-3150-83ff-79d15112717e | -2.7252 | -47.05512 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 4bbb8cda-9016-3606-8073-71dead629e20 | -2.72646 | -47.04626 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 15856f49-40ea-3a20-bba3-f17de8a53a45 | -2.8142 | -48.63037 | 2026-08-28 11:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d89f0b6d-ca19-35ba-94f1-ef9da1ec1375 | 2.51338 | -50.85793 | 2026-08-28 11:49:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a6f26162-9ef9-32aa-9689-50a02a0f3197 | -1.35024 | -47.32573 | 2026-08-28 11:49:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 427bb5a5-eaaf-3a59-ae65-1afc48ab2ce6 | -2.73533 | -47.04747 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 06a4a795-18c9-3afa-b1d5-af606df98b7a | -2.73407 | -47.05634 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 760f7776-1c9f-3967-9f8c-ea00ddfa3856 | -2.7366 | -47.03859 | 2026-08-28 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 856dc02b-405c-3a29-b8e0-0c531bd1b6cf | -10.8996 | -46.6216 | 2026-08-28 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| fda0e1cc-f26a-3512-897a-a2d9acdd7aaa | -10.7839 | -50.6346 | 2026-08-28 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 73a9a79b-feac-31e6-9caf-bcdcb7858870 | -12.2086 | -50.5815 | 2026-08-28 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 91622d3d-008d-33f4-9c92-65ff0b908ef5 | -10.899 | -50.5159 | 2026-08-28 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 4be3dd9f-47a6-3f31-a297-edd23c454877 | -10.918 | -50.5138 | 2026-08-28 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 53d274ab-9250-342c-859f-a1e466ef120f | -10.8992 | -46.6442 | 2026-08-28 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d455c24f-88e9-3f56-aa27-ded5cdaec3a0 | -2.7303 | -47.0644 | 2026-08-28 11:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 5b4dd886-50ea-3b30-b2d1-0519b1ff7369 | -12.0158 | -47.1693 | 2026-08-28 11:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 71a0cddb-1879-3421-999d-cb28088508d8 | -12.2847 | -50.5938 | 2026-08-28 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8c4f6d8d-0916-353c-b204-0557616f9b56 | -2.7304 | -47.0424 | 2026-08-28 11:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| ea1b659f-1944-341f-9005-587cb2bcdf7f | -11.2503 | -45.03703 | 2026-08-28 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9730d354-58e2-3926-b14b-a0ee205ea81a | -4.64526 | -43.12632 | 2026-08-28 11:51:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4e35b080-9c2d-3019-8936-dfb3a25bb07f | -9.96603 | -53.94044 | 2026-08-28 11:51:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 8627a921-2c67-31df-b782-de26f859aab0 | -9.93306 | -47.90712 | 2026-08-28 11:51:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4bda4a4e-2e1c-3387-ba54-cdc15b07829a | -9.2177 | -51.56511 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bfa9d62a-2d7c-38d1-a11f-dcb0915845de | -9.1603 | -49.96405 | 2026-08-28 11:51:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README71.md)
