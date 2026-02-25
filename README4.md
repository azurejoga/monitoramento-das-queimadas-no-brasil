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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 352484c3-afda-39f5-a950-322e2a5f80f9 | 4.29209 | -60.76912 | 2026-02-25 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c077bf9-08c1-32f4-a407-a867eef9acbb | 4.7814 | -60.15049 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46db99e1-ef73-39cf-a5ad-82b6a3b623dd | 4.23295 | -60.18884 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b0922eb-d9c2-3a17-8fc2-f386007f198f | 4.06585 | -60.19462 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d350944c-c11d-3bc8-84ae-db863a95bcc3 | 4.2346 | -60.18572 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba2c043-bc79-324f-8038-59fca6921f8c | 4.06519 | -60.19014 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 072354ab-0388-3803-844e-d882fd199670 | 4.77758 | -60.15579 | 2026-02-25 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abde0f87-d9e3-33d0-b8bd-ba8e9378a418 | 3.93319 | -60.05877 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a784deee-8d8d-3398-aab9-b8909ce782c8 | 4.15156 | -60.29357 | 2026-02-25 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61e31fd5-0d8e-35d4-8cc6-53be680d789d | 3.05179 | -60.88648 | 2026-02-25 05:03:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2adf5b1a-af89-32a2-8070-5773756fd4c5 | 2.87803 | -60.26331 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be0971ce-c2a7-3139-b734-8aa0d72d9f86 | 1.93288 | -60.36184 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c89f199-5869-3eab-8b65-17886c1a1597 | 1.77066 | -61.35972 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c67f854-5f03-3d1b-9cfa-572aeb48a7c2 | 1.52237 | -60.02991 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd08db75-0a3b-351e-a0f7-07329f52b8e6 | 3.49829 | -60.28899 | 2026-02-25 05:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 426db394-dd34-3f0d-9301-f84bb509cc3e | 1.63617 | -60.28201 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e52f17a-dca7-3f49-93d5-4ea3d5f61e7c | 3.44914 | -59.89216 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf1593a0-dadd-323f-aba9-63582fdd72b4 | 3.1604 | -59.95332 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8757e55d-397d-36e5-a5eb-ec671ef02b01 | 1.94608 | -60.35985 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a855d0f-b381-30df-88a2-a4e78beb6228 | 1.88537 | -60.91209 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52d1bdde-c58e-3dad-acf1-1edaccd3308c | 1.50539 | -59.94632 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c8c1cd33-8925-3786-8b44-1e46df52491b | 3.05086 | -60.88898 | 2026-02-25 05:03:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd535fb4-4bab-3d40-84cf-e351ffb3879c | 1.51632 | -59.93249 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0502d93e-9e63-3218-af3f-5dbcfe0ad7af | 1.20631 | -60.62209 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd32b3b-4511-3059-ba75-c11d40e5f060 | 1.49688 | -59.94756 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 754cb2ab-2dbf-35c6-b036-b0c04534ab27 | 3.49097 | -60.28923 | 2026-02-25 05:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7230309-008e-3c64-842c-84f9ecd81f6d | 1.48912 | -59.95189 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e85c40f6-4ea1-3e28-8dbe-fd8db5af5788 | 1.50061 | -59.94205 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4c5bdef7-8b8a-3775-b78c-589cc6afdd48 | 1.49147 | -59.93922 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 326e3548-18f0-330e-91f1-ed668de955fd | 2.71835 | -60.24924 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe9ea033-5911-3f77-8a7d-5ce48fc7a3b9 | 1.51268 | -59.93711 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9b76f5fc-e65e-39df-9370-63e1f32aa74a | 1.49762 | -59.95065 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c38725d2-3d25-3811-826b-8b5b541e66bd | 2.2286 | -60.70066 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb630660-47da-3903-a4e2-ba329eef1e4f | 1.48487 | -59.95249 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d5b0e4ed-46b3-3041-bc65-f5e4d81df654 | 1.20565 | -60.61774 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc3481b9-3517-3e09-bb12-f9dddd304f47 | 1.49933 | -59.93401 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ac7328dd-d5df-3f53-8ba6-6f7b323f73a4 | 1.51329 | -59.9411 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ef436c6b-aef9-3716-9e25-6cddb33482e7 | 3.44537 | -59.90525 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a84ba5-789d-3025-94bb-4970c6d6e48e | 1.93727 | -60.36117 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5af5b0-add1-3dc0-a18d-ad42330a5086 | 1.49382 | -59.95611 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ee0642d7-4034-3a98-b0be-69332879cb58 | 3.13424 | -59.98736 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06c8571e-53d6-324d-8f9a-dddfa9c38c78 | 1.49748 | -59.95153 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 882dd15b-e248-38e7-b35e-05a241bc6cbd | 3.51664 | -60.38318 | 2026-02-25 05:03:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c37154e-125c-3d02-a6d1-a190463bbd76 | 3.45037 | -59.90055 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6b41336-eb1e-3bf0-8cd6-8f4c4e4c596a | 1.50187 | -59.95004 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 422cd225-fca3-3300-8035-313f5361cce2 | 1.49567 | -59.93949 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 535e547e-3dc4-3aba-a547-c61d49380deb | 1.94066 | -60.8467 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1409d5ac-18bf-3f75-ba5d-91d3a24136c9 | 3.44602 | -59.90942 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21e8bbe9-16a8-384f-96ca-2da7f5b3ce8d | 2.23313 | -60.70004 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09e5a8c0-63e0-31ed-80f3-77636802e4d7 | 1.63682 | -60.2862 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a92ee66-5c34-3156-b2d2-fb0ac40a4187 | 1.66746 | -60.48226 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03b6abc9-15b8-3839-b4b3-b7f1a34ec48c | 1.93754 | -60.85662 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0212ebb-1722-3c70-9a53-933686d6c9e3 | 1.49992 | -59.93889 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2f65bec3-2695-3f95-b8cb-4c50c6e7c467 | 1.50964 | -59.9457 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8cef8e08-41fb-37fb-bf32-8bdf3078b1d6 | 1.35753 | -60.05432 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51280c22-292a-358a-a1cb-5293799142be | 1.49323 | -59.95216 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8cbe4620-72d2-3aff-8b0a-4022e6b92701 | 3.44663 | -59.9054 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a188b42-d210-3aab-a362-d1dbdd30c6a6 | 1.93683 | -60.85202 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd9000be-d80e-37ed-919c-0fb9595cd20c | 1.49507 | -59.93549 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ce053153-09d4-36c6-a2bf-e1369454b523 | 1.49932 | -59.93486 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8af31a39-bc5b-3654-b911-a027a116b480 | 1.51449 | -59.94904 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cd131f7-deb4-3c8a-a841-3ab9dabb85ea | 1.49337 | -59.95127 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3cbdc2a9-e9be-3bb7-bd84-67da843de559 | 1.4885 | -59.94794 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 009cb319-485a-3bd1-9e53-1bc047de335a | 1.93794 | -60.36552 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a5b495e-4661-3905-ba34-efef337af6a7 | 1.50843 | -59.93768 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7c9bfeeb-6217-320d-9ac6-dd71e0438c53 | 1.50903 | -59.94171 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4664345d-6211-3169-836b-21ca288eb4eb | 1.49572 | -59.93863 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 28c8f9f9-83c6-3a0b-b9b3-a1d4890fcb0c | 1.49871 | -59.93087 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9adb042a-2273-37cf-b59c-47fed3caaffb | 1.50781 | -59.93364 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ac40fced-84b0-3c9c-a4bb-5079280985e7 | 1.3119 | -60.40142 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56f8208-f615-3380-a840-a542d0aa0a15 | 1.49275 | -59.94732 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 8845cd97-b57c-336e-8702-05d03628ba63 | 1.50599 | -59.95029 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c878d436-7509-3c59-b7cf-4a6517755c00 | 1.49142 | -59.94011 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 69962c9b-82f7-3bad-bde7-818ac5981b80 | 1.3589 | -60.29258 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab64a500-42e9-3eea-b60f-a81bc5c2a1db | 1.94674 | -60.36418 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d5d46e4-e211-3534-89b5-cdbe0212f1b2 | 1.28894 | -60.42655 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62e640f1-92b9-3d89-a71c-353dd6ba0d67 | 1.48786 | -59.94392 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 6c5f7de7-da71-3d65-a47f-2c5745da1935 | 1.50417 | -59.93829 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c63a4ad4-6cc3-39b2-80e4-5ca85a18ad97 | 1.50125 | -59.94608 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bba30743-1c1a-3e3b-a7e6-3f49f4be6d33 | 3.49546 | -60.28856 | 2026-02-25 05:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21758da8-5cce-3cd5-8389-974a3becbdcd | 1.94167 | -60.3605 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82eeade2-8f53-3781-80bc-7fd8be2ae1c3 | 1.51693 | -59.93652 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9462bf6-f8e8-30ab-ab7f-59ba7c789056 | 1.49509 | -59.93464 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ff8d334d-372a-3437-8a01-37e0b85884b6 | 1.93611 | -60.8474 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2d7b1bd-1bf9-3641-b907-e1d44520af74 | 1.49699 | -59.94669 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8f4a336e-b4c5-3d96-a8ac-aa59130d7494 | 1.50053 | -59.94293 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 11b9ef44-1181-3162-a96d-c4f7464d629c | 3.25029 | -59.92 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fad235ae-5632-3686-bb43-d501e14c4a70 | 3.51452 | -60.38253 | 2026-02-25 05:03:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdb3aedf-1f1a-3963-abee-4a5ec5862776 | 1.51389 | -59.94507 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f1ff501c-306f-3bcc-9390-0627b783019b | 1.49084 | -59.93522 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cbc19cee-71d2-3f2a-8346-60cce7294bf9 | 1.48061 | -59.95309 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 83830b88-5f64-3cbf-9e61-6fde872aa142 | 1.82807 | -60.84844 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee5dd95d-ae4c-3132-a6c4-c528c972c745 | 2.11515 | -60.19636 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce82acf-dece-3f67-8f7e-07347a34ea64 | 1.49263 | -59.94819 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ebd4150d-4f36-37ab-b015-f989a56fcb30 | 2.71501 | -60.22766 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdecd2e1-709e-3efb-8074-43bef7067339 | 1.50113 | -59.94695 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cac9e502-f8a4-33f9-8e55-98cd1b26e944 | 3.14047 | -59.96918 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd55296-0ef6-3aed-8ed6-cbb3b8c07697 | 3.44725 | -59.9096 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64a0a8dd-975c-342d-adf1-82e079f26ed3 | 1.94541 | -60.35554 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01898454-889a-330f-99a1-2cd427dbfd5a | 3.26462 | -59.92648 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
