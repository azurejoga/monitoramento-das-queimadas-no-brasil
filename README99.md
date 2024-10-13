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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18e89af5-8e3c-3847-bf69-f6211d9141ec | -10.36753 | -61.22599 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02ef169d-5796-305b-a327-44f90a98069c | -10.36752 | -61.18032 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efac0b04-0c17-3eed-9804-5dc7c6e86981 | -10.36696 | -61.22969 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db79a6f-e584-33f9-b538-cfeb46bb8596 | -10.36695 | -61.18405 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c4051d5-8056-3611-8c55-9f7ee518ef6b | -10.3664 | -61.2334 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59eaa29c-b69e-3a9d-ab12-deae827e94cd | -10.36638 | -61.18778 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26559279-4247-3fac-b7e9-6b33c80ff985 | -10.36467 | -61.17607 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1604ce4c-e80e-3d9d-b6f3-6272f4be780f | -10.36413 | -61.22546 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4fa0e71-83cd-3131-9e56-cb430477431d | -10.36411 | -61.17979 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3021ae5-43df-382d-b68c-eda6e3d76ac0 | -10.36356 | -61.22916 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da61fd0e-0c70-300e-a006-607e1014f4a5 | -10.36354 | -61.18353 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4dca73c-9e67-3366-87c1-53725b7ecd66 | -10.363 | -61.23286 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48eb8dd-fd47-384e-868e-ca2f919e2472 | -10.36297 | -61.18725 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6d108c0-da13-3900-923f-dab7a3ce0294 | -10.36126 | -61.17555 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c92ea55-7d03-3b90-8467-93fa6bd63bbc | -10.3607 | -61.17928 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82188030-b682-3459-8e4c-407f7ed152d2 | -10.36016 | -61.22863 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdefeef8-d8a9-37d3-bbb7-562f4b28bd48 | -10.36013 | -61.183 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342b9cb6-aa47-39ca-9e1d-eb2fe835443c | -10.35959 | -61.23234 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1307183-8624-3b7a-b55a-9b6ba3fa456b | -9.387 | -61.04475 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fca731ea-4bdb-33c7-a4bb-469af744a9ce | -9.38644 | -61.04844 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed25fec8-670f-3b3c-9549-0ac5267d1e49 | -10.91394 | -60.89795 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76851c75-187a-3835-b515-2c86f7d87ad8 | -10.91049 | -60.89741 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e3cceab-ae6d-3892-b922-be9ad78c2cb3 | -10.90991 | -60.90125 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30166c4b-a876-3f0f-ae35-a6bc3fe1a8c4 | -10.90934 | -60.90509 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cbb90d1-ec2b-34b9-9c13-364e011e3cd9 | -10.90877 | -60.90894 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96015d1-8ce2-3965-a675-34c1a0fd80ce | -10.9076 | -60.89301 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e349cc78-4f53-3e32-b9a2-26e640f426da | -10.89843 | -60.93091 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ccf198e-f19f-3b28-988c-d7b69214c6e5 | -10.89723 | -60.8914 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2370929-2588-364a-95b7-bcf0d0e818fa | -10.89666 | -60.89525 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22264310-d162-3fe4-b96f-3731480e46e8 | -3.16013 | -61.11184 | 2024-10-13 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e718b33d-da07-3aea-a6aa-24001015e753 | -3.15852 | -61.12215 | 2024-10-13 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caf086e8-db0c-336c-a35d-7580b86ee613 | -3.15683 | -61.11133 | 2024-10-13 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 561885eb-5065-3f32-a4f2-ef8ae1c9fae7 | -3.11018 | -61.10456 | 2024-10-13 05:27:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8ba5c15-3f1a-3d76-abd0-acdedd6ffbe8 | -3.9961 | -60.39438 | 2024-10-13 05:27:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1090111d-c2ec-360b-a650-1c3f14bcd5cc | -3.84459 | -60.49369 | 2024-10-13 05:27:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83496d22-3ed1-3d3d-a9df-dafac3321793 | -3.84404 | -60.4972 | 2024-10-13 05:27:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad436e6-58c7-3e92-8802-da207a76311e | -9.09677 | -61.18412 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7eae0831-5c8c-33d3-9768-9c94cb0d0144 | -9.09559 | -61.16905 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4042bddb-7680-3db3-9533-b40eabdb8ce6 | -9.09475 | -61.1652 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29e5b862-f8fb-3c61-ae2a-e9bd6611ca1b | -9.09419 | -61.16885 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71914182-a089-3d09-a30a-f8bafe7afd87 | -9.09284 | -61.18723 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4220f1b6-87a1-3934-8700-c3a176a4ca16 | -9.09251 | -61.17974 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fe460d-ec53-3a57-a4eb-0470bd48688a | -9.09195 | -61.18338 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50a39bb5-b041-3a04-af5c-e4fef170c94b | -9.09081 | -61.16832 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 206e6dc8-a336-3d6c-89dd-e795495716d3 | -9.09025 | -61.17196 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dcdc15a-ef8f-3cc7-a550-01a8cc0468b7 | -9.08969 | -61.17559 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01628d9f-3f57-3b4d-8f3e-c277abda020d | -9.26877 | -62.38414 | 2024-10-13 05:27:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ec24bcf-3d5a-3a7b-8155-22b307e5c59c | -9.26546 | -62.38362 | 2024-10-13 05:27:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7a32b72-3cb6-3069-90c7-5f901ba87447 | -9.09897 | -61.16956 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07dd2338-32bc-3b97-ace7-9bf38ef9bd4e | -9.09842 | -61.1732 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5dfc70d-f893-3957-9640-431a7c44e662 | -9.09622 | -61.18775 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76443f7d-8ae2-3d67-ac2e-1afab7df3c3a | -9.09614 | -61.1654 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e776970-1eec-32b2-bf6d-b15e4152ef38 | -9.09567 | -61.19138 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73f18202-327f-38e3-af01-ce5903edcfea | -9.09511 | -61.19503 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 706c4db0-488b-3965-804a-9aa1e507260e | -9.09504 | -61.17268 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901153d6-594c-3ab1-a391-62d198f77d1b | -9.09449 | -61.17632 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 141f934c-37b7-336d-b3f5-58387bfa10d7 | -9.09394 | -61.17996 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c37b967a-43a9-33e0-8575-6c5f2509d7f7 | -9.09363 | -61.17248 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07d097de-7096-3f6d-ad13-21975923179e | -9.09339 | -61.18359 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c7444c9-844d-3bd2-ab93-05eb8d88d4b7 | -9.09307 | -61.17611 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e1a7bcd-fa53-3d2f-9d99-a21c6ac26d1f | -9.09139 | -61.18701 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31e0987a-ac3b-3f41-9407-090a0cfe13af | -9.08687 | -61.17144 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 008ffd6f-13b4-3666-9a84-7fb6ccfc8b56 | -9.0801 | -61.14801 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d2a4a52-0c43-3eba-9f03-1b51abacd75e | -9.07672 | -61.14749 | 2024-10-13 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84d4a03f-70dc-3d86-b446-fbf4cd61f610 | -9.74432 | -61.98804 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6e7e937-2461-337b-b378-95bcacad5972 | -9.69933 | -62.3232 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca635052-8faf-31d6-9107-e0aa8000d81a | -10.60756 | -61.76357 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 860b79d0-0e0d-3680-8eab-9c53e1d19ac1 | -10.60701 | -61.76716 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef21a1a0-0628-3a89-ae14-71e1bfec6fec | -10.7847 | -61.50434 | 2024-10-13 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b40d6092-06f5-3064-a5f0-c431a46e748b | -10.78415 | -61.508 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58455e52-ebfb-37ff-a787-8b8d0c0c4918 | -10.7836 | -61.51166 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ed0c7f-bd60-3780-9fb7-e446ac43708f | -10.78132 | -61.50378 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 833bd930-0a86-3c8a-bafb-5450f2df0431 | -10.78022 | -61.51112 | 2024-10-13 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04b9cebe-ae2b-375a-b59b-95d6c1462ea8 | -9.39478 | -62.38232 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6759c551-47fa-3c21-88a2-280beb7b71a7 | -9.3801 | -62.23679 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccdd22d3-ff67-3132-9e42-92817cb56bb3 | -9.37955 | -62.24029 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72f39dc4-9a5b-3aa4-a8c4-3a7eb5f0f978 | -9.37901 | -62.24378 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ebf7655-29eb-3959-8fdd-ddeb7797e610 | -9.37624 | -62.23976 | 2024-10-13 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 861410ff-beeb-351c-bc7c-0e2e16eb7660 | -9.34899 | -62.3715 | 2024-10-13 05:27:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff37257f-2f43-3f69-bb01-64710746ddbd | -3.48133 | -62.69609 | 2024-10-13 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc07eee-5c2e-382b-968b-c83d327e4cee | -3.47798 | -62.69557 | 2024-10-13 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3037f23b-e553-3ff3-b59c-b2cf2b88f9a9 | -3.31258 | -61.56877 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cecf61f-6394-3bb2-ae6c-e09603bc49a5 | -3.30927 | -61.56826 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f11cc86-7ae1-37a1-9d8e-bc976b8af9f0 | -3.30597 | -61.56775 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c151db2-7fb4-320a-980c-856f4ee42f5b | -3.30267 | -61.56723 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb7620de-c4ac-3a70-999b-8298d9bc6c50 | -3.08873 | -61.69547 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c1dd4fa-6e3b-3d6a-a481-02b349f7dd98 | -3.08651 | -61.68808 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a894a62c-3430-3a1c-8bc3-60ed378b9f2b | -3.08597 | -61.69152 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bea40d69-1e40-3272-8b6c-e9240f98fc52 | -3.08543 | -61.69496 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd1cc7b6-8864-3670-aef6-9b76f2f05b9c | -3.05345 | -61.68293 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e40c31c-3a08-3de1-8ace-3c39d760dd46 | -3.05291 | -61.68637 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3400103-2040-3057-8efe-1b1e2aa324fe | -3.05069 | -61.67897 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4897341f-6f11-3377-98f9-be969d694c1b | -3.05015 | -61.68242 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3dabfc63-5d9f-33b8-a07e-40705d6d795d | -3.04961 | -61.68586 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 431ef6c0-0669-336c-bc50-a8959f3e9bc3 | -3.04793 | -61.67502 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 93ce99b9-8c9e-3f73-bf2b-a8719b00e3d7 | -3.04739 | -61.67846 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de784157-212d-388c-a10c-36fed28bc6c6 | -3.04576 | -61.68878 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6babed0-d78d-33d0-9aee-ed37f997b22a | -3.04462 | -61.6745 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63a17fd7-b01f-3ee3-9f28-e938b81851c3 | -3.04132 | -61.67398 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe8d00f-fb3a-326a-a6cc-2dad00fbe8e6 | -3.04077 | -61.67743 | 2024-10-13 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README100.md)
