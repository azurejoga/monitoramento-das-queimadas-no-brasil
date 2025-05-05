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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdea6ecb-1e38-3697-8db4-ed8275506d71 | -30.59626 | -52.81469 | 2025-05-05 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 127.1 |
| a4f20b68-c54f-3228-8867-ea33df458cdb | -30.59689 | -52.82151 | 2025-05-05 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 70.5 |
| 7b04b3b4-e8f3-3619-91c1-0fe1cb46e8b6 | -28.87985 | -56.24255 | 2025-05-05 12:23:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 18.9 |
| f731803a-be01-3f93-a207-968d563192e7 | -30.59414 | -52.82744 | 2025-05-05 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| 3b8b222c-13ea-314c-b636-5b621b76caf3 | -30.94377 | -52.2715 | 2025-05-05 12:23:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 10.8 |
| c1b3a2f3-925f-3be8-b9bb-c4e105361d8e | -30.59908 | -52.8088 | 2025-05-05 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 38.5 |
| 7494867e-1c6c-38ad-abd0-4e89ec8359c0 | -30.00547 | -52.8427 | 2025-05-05 12:23:00 | TERRA_M-T | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 7.9 |
| 15b4f443-5d5f-34f6-838b-df952bdc7fc1 | -30.94183 | -52.28341 | 2025-05-05 12:23:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 18.7 |
| 46806c40-8276-3abd-9643-3abca8050060 | -27.87446 | -49.80567 | 2025-05-05 12:23:00 | TERRA_M-T | RIO RUFINO | SANTA CATARINA | Brasil | 4215059 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| a8dffed5-c962-3af5-ba1f-a6add7b53d09 | -6.9613 | -42.8108 | 2025-05-05 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| a2107dab-ab66-37b5-bbc0-109b8a5af0a7 | -6.9615 | -42.7872 | 2025-05-05 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 06b80b7d-cf15-37eb-9361-613e51b26b45 | -6.9613 | -42.8108 | 2025-05-05 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 47cd90c5-9bad-3c20-914a-aaa84307f366 | -6.9615 | -42.7872 | 2025-05-05 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 4fb03075-721d-31c3-a94b-e9a9216277e5 | -6.9613 | -42.8108 | 2025-05-05 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 096f7963-64ff-3028-9620-a38a83e958ea | -17.9891 | -50.1279 | 2025-05-05 13:00:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 183ce929-a891-30f5-9723-70a0962e6d71 | -6.9804 | -42.7854 | 2025-05-05 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| d0b0aee6-0092-3d44-a583-f4734f880ff6 | -6.9615 | -42.7872 | 2025-05-05 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 6e47ca9c-b238-3944-bfc2-49821441b0cd | -17.9891 | -50.1279 | 2025-05-05 13:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 688.2 |
| 241b6ba4-6a1a-3569-bbc1-19e50da9a32e | -17.9885 | -50.1502 | 2025-05-05 13:10:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 658.9 |
| 21ddddcc-bcd9-36ac-b26f-e481ad6f5b0d | -6.9801 | -42.809 | 2025-05-05 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 0576f855-4b33-33f3-a6e2-c7dcbd05ea5a | -6.9615 | -42.7872 | 2025-05-05 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 0968cd96-942a-37d1-8dbd-bb9004a596c0 | -6.9615 | -42.7872 | 2025-05-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| e77c569a-d567-3eeb-a836-73d8295e55c7 | -6.9801 | -42.809 | 2025-05-05 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 5284f1fc-1379-367f-b89c-10f7751ceffb | -6.6211 | -44.7668 | 2025-05-05 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 7e7a3b8f-5e8a-342e-9411-4772c221a515 | -6.9804 | -42.7854 | 2025-05-05 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 01797ec3-f5d8-3c44-800a-4034cc4e3a8a | -6.9804 | -42.7854 | 2025-05-05 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 7c21078b-b95e-350f-be12-c20c1dcd9d2b | -10.9924 | -44.4383 | 2025-05-05 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |


