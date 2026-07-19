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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d07bec3b-9208-31c0-910f-55ed165cea5d | -10.7087 | -46.6682 | 2026-07-19 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 539c0f89-4291-3fc9-ad64-20ee649cd596 | -10.7091 | -46.6457 | 2026-07-19 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 0d206045-a09b-320b-860c-6358ecb89a19 | -10.6901 | -46.6481 | 2026-07-19 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ef39a702-63b5-3b35-892f-278e0afc8a45 | -4.9512 | -50.8875 | 2026-07-19 14:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0c4c2187-c43e-3d7e-9f89-5987e2deead5 | -10.7094 | -46.6232 | 2026-07-19 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| df3ef8ae-9ffa-3a32-97de-2dd6cdba29bc | -7.1169 | -44.0339 | 2026-07-19 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 14f029e7-e3bb-3ddb-a642-7cc5fd27eaf4 | -10.7087 | -46.6682 | 2026-07-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 34989a5b-14a3-3b99-ac05-5e75bbf188d0 | -10.7091 | -46.6457 | 2026-07-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 506470bd-bf78-30a1-a1b8-46e910ead51e | -29.1981 | -50.4424 | 2026-07-19 14:20:00 | GOES-19 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 185.1 |
| fb2ae626-055f-3a70-8e7d-613ca2b62aed | -11.8284 | -44.7579 | 2026-07-19 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| ee4a7258-ae97-32d1-926c-1b0780a2be5a | -2.7768 | -49.4553 | 2026-07-19 14:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 9a2f367d-3cd8-3ccd-a66f-e8d9e877d150 | -4.9512 | -50.8875 | 2026-07-19 14:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7a632af9-8e85-3a8c-8fd1-403101b850d3 | -7.1169 | -44.0339 | 2026-07-19 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3b24ad46-835a-3353-bbc5-b5ebe2a5e6c9 | -10.6901 | -46.6481 | 2026-07-19 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4b3284dc-4113-3353-89fb-2b3cc214c882 | -7.1169 | -44.0339 | 2026-07-19 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| da2d5f0c-6069-3d65-a713-3195e149d3f2 | -2.795 | -49.5184 | 2026-07-19 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 62de3dc5-a303-3441-844e-811ec7956b91 | -29.1981 | -50.4424 | 2026-07-19 14:30:00 | GOES-19 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 169.5 |
| 3cc5c806-1037-3d33-a46b-854e7ef2d25f | -11.8284 | -44.7579 | 2026-07-19 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 082dbe9b-7945-35b7-b473-7fc6500b3e42 | -2.7768 | -49.4553 | 2026-07-19 14:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| fd8a50a8-c645-31dc-9147-a40c59a761a2 | -12.0732 | -53.3567 | 2026-07-19 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4e6ca088-3991-3472-b9d0-c0e22efe51cf | -18.0393 | -50.5399 | 2026-07-19 14:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 80b0c0a0-5747-31e3-a000-b9d089dcccca | -4.9512 | -50.8875 | 2026-07-19 14:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9e742a5f-01b3-3995-a8c1-a21e8c05c906 | -11.8284 | -44.7579 | 2026-07-19 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| eaa8f4e8-52d6-37e6-962f-3f267da6eeef | -2.7768 | -49.4553 | 2026-07-19 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 03751011-0baf-305f-936e-957b3e273061 | -7.1169 | -44.0339 | 2026-07-19 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 66c437b9-7b4e-311e-a48d-8ed1400b450c | -11.621 | -47.9561 | 2026-07-19 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 3d23cfc7-b98a-3ea0-942d-13237997849b | -2.795 | -49.5184 | 2026-07-19 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 62973488-a799-3007-8ff9-509dd54e6a5e | -29.1981 | -50.4424 | 2026-07-19 14:40:00 | GOES-19 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 163.3 |


