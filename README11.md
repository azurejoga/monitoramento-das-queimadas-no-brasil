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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5945be68-c505-30eb-a396-1b1ba71c3cdd | 0.0638 | -60.9799 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b047671e-9d46-337c-b6c5-c66e554bf929 | 1.5047 | -59.9116 | 2026-03-04 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e646dfd0-7127-320e-a8f7-c0a76b789861 | 0.0455 | -60.9799 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 252.6 |
| 39529e5a-93ab-36d8-a7dc-2712c8f1514d | 0.0273 | -60.9799 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 98.0 |
| de786b21-45fb-364b-aaff-aaf09f04c981 | 0.0273 | -60.9988 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b137c373-76fd-3c84-87be-f35834626b59 | 1.5047 | -59.9116 | 2026-03-04 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 80a332ee-b9f5-31e3-a3a7-f04dc0d97ecb | 0.0273 | -60.9988 | 2026-03-04 05:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 15345430-aefb-3f57-8048-c9a0114cc639 | 0.0455 | -60.9799 | 2026-03-04 05:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 235.0 |
| 3e3c1e6e-8f4c-31f1-8f94-d557d95b3d17 | 0.0273 | -60.9799 | 2026-03-04 05:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d7d2175c-94c9-3e42-947e-9c3fcc980bac | 0.0638 | -60.9799 | 2026-03-04 05:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 5ed9d8af-7b63-360d-8540-b7d4a5012f0b | 0.0455 | -60.9988 | 2026-03-04 05:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 138.6 |
| c097e47e-7206-391e-bedd-af489dd08297 | 0.0638 | -60.9799 | 2026-03-04 06:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| feae3113-9f0e-3e3f-ae4b-422b6cbbf6d8 | 1.5047 | -59.9116 | 2026-03-04 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e96fdbce-a1d1-3e60-b1f2-0f742bb02d8d | 0.0455 | -60.9799 | 2026-03-04 06:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 121de86a-6a5b-3a13-9866-e217d8aeb334 | 0.0273 | -60.9988 | 2026-03-04 06:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3931632f-88c5-3dec-9025-f0fdd5588654 | 0.0273 | -60.9799 | 2026-03-04 06:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d0d0f6b9-34a1-3971-8d8f-02c50f04b669 | 0.0455 | -60.9988 | 2026-03-04 06:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 18c26ff7-edd6-338f-a91c-1bc79f440dae | 1.5047 | -59.9116 | 2026-03-04 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e15fd7a3-a752-320f-8a8f-368686bd86ed | 1.02134 | -60.54309 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2516803-81d9-301d-ba38-fec56aaa2e49 | 4.05021 | -59.8595 | 2026-03-04 06:12:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4173b05f-18e0-3246-b10c-82b118ef3393 | 3.8732 | -61.68869 | 2026-03-04 06:12:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba432e87-5baf-3d69-9143-ab2d8f01ed65 | 2.65259 | -60.10329 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18b03093-3e49-32d6-b260-e68d155a75aa | 1.11067 | -59.202 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74c57eff-8ec2-3bff-b0b8-7a90e6cadddb | 4.64281 | -60.69998 | 2026-03-04 06:12:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94a89892-5326-3a22-b2bd-a6a97b2338eb | 1.05795 | -59.49541 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fc1faa8-113d-35d5-935c-7bf87ee3ace3 | 2.92278 | -60.46387 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8d57d96-723d-395a-a075-1fb06fbcf859 | 1.50486 | -59.90677 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 749f86f7-4521-3c57-a7ac-ca046766f74f | 1.50015 | -59.91723 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1af8c2eb-c808-303f-a1fc-64034544ebde | 0.72985 | -59.90268 | 2026-03-04 06:12:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e36778c-56d4-34d9-b27b-478ada48d557 | 2.91881 | -60.46383 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcb2238d-a558-31b0-a14e-d6d8079fcb9c | 3.01579 | -60.65707 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 856d8e11-264e-30d6-bb81-d191deeda5e1 | 1.07855 | -59.25359 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20a56622-3f8d-3c7c-b224-23f5fc5c0ca9 | 4.04344 | -59.85626 | 2026-03-04 06:12:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2862796-100e-3c75-ad73-54a099f79da9 | 2.67197 | -60.41535 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99395843-eb7b-3b2a-8f43-d25144eb83f6 | 2.65865 | -60.10777 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c1a5e80-6289-39e5-90c2-d26543ba8684 | 2.92471 | -60.46276 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73ab872a-d6c3-3276-a16a-9ba9dad2fde9 | 1.512 | -59.91117 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 859d76a7-3684-3bf7-ae72-93ef36e58c39 | 1.07764 | -59.24794 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f59518d6-dc32-39a4-a8a0-a26d312a3684 | 3.87856 | -61.68767 | 2026-03-04 06:12:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45a5fa25-c52a-3e15-ad9a-40cd0e062b9e | 1.10931 | -59.20065 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa4bd99c-2310-3977-a18d-231305816a51 | 3.06097 | -60.71218 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0393392a-9658-3bd0-a6f9-9ba8de7758d1 | 2.22642 | -60.75113 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8febacd7-217f-3bff-a9bf-8fd353da87f1 | 3.03187 | -60.64565 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40582bec-b9ca-3fbf-8e5d-c24085f7c7aa | 0.96064 | -60.23616 | 2026-03-04 06:12:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 845717ca-a1c2-3902-b646-aea577b99d71 | 1.02205 | -60.54768 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68332c1f-420c-3f29-b689-ab1f50ec0b39 | 2.66603 | -60.41639 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47bba3cb-3681-32fb-877f-0a828f8771b9 | 1.51121 | -59.9063 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f3da7b3-9e04-3250-aac9-3a3e51d28122 | 3.87582 | -61.68642 | 2026-03-04 06:12:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24aad0d9-aaf3-3137-9ad3-f033d011e87e | 1.51276 | -59.91587 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aeb22935-506b-3b7f-a083-58db236b2723 | 2.91541 | -60.45634 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ecf02970-7a7f-3b51-9da4-4e586e45d4c0 | 0.73068 | -59.90781 | 2026-03-04 06:12:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c476c21c-22ce-3e17-8e62-53b3bd2dd89d | 4.04412 | -59.86018 | 2026-03-04 06:12:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b85f217-85da-37a2-aa3a-204ca5611efc | 1.10978 | -59.19638 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7cc3ff87-9b26-38f3-b51f-72b04c29ce76 | 1.10838 | -59.19505 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 678c5191-1def-3ce7-a234-393eb1788d6a | 4.04479 | -59.86404 | 2026-03-04 06:12:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 785b545e-4533-3be9-8d57-d049b0317637 | 0.91713 | -60.43719 | 2026-03-04 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44e61f40-9587-38bd-98b4-469adcfaa6a2 | 3.03769 | -60.64462 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73bb5b87-7bb3-3906-bc8a-3cba1a59a8f8 | 4.64226 | -60.69679 | 2026-03-04 06:12:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de074e3f-0d84-3893-8c4e-3c441cccea35 | 2.9174 | -60.45523 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40feac30-32dc-3356-9776-4981c2e5cee7 | 1.50644 | -59.91647 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6eaaa15-3547-375d-80f9-086df2550cd8 | 2.65944 | -60.10683 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47093e46-ee75-3165-80d4-dd8e6a95f31e | 3.02092 | -60.65187 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00940c48-3a6e-3342-8cbc-469e85416a9d | 3.06677 | -60.71115 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ec679e-9b88-3d98-9c4f-efd9c091b287 | 2.22527 | -60.75016 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1333bf1c-0a49-39c1-854a-4c242a694576 | 2.65184 | -60.10424 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e27dd9d-298e-3f7c-a3d8-12a46e361033 | 2.22455 | -60.74586 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c280eafd-c70c-38ec-82f8-dc5e84772861 | 2.92205 | -60.45958 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5b0d91e-3024-30ab-95ac-116c3b0fe5df | 3.87265 | -61.68532 | 2026-03-04 06:12:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6921d7a3-eb41-3232-bea2-806e38b0986d | 2.92401 | -60.45845 | 2026-03-04 06:12:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bee44361-17e4-323c-bc3f-e76d868c89ee | 1.50566 | -59.91164 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32dbd19f-f195-335e-b41a-7577c4816a8e | 3.04885 | -60.64175 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6fc9e92-2662-3155-b433-6564326a3532 | 1.06351 | -59.48892 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dbbce50-c4ea-37d5-8d07-e395cf828f77 | 1.49936 | -59.9124 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e135a576-f7a6-3f4a-90e6-0984658d7af4 | 3.05468 | -60.64074 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e12b88c5-f783-33f3-868f-f23347b3e5db | 1.50722 | -59.92129 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5149b953-8a18-31be-9356-86f5cb6463cb | 2.67864 | -60.4187 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1f6cea0-aacf-31fc-bf6c-f754f1a449f5 | 1.34817 | -60.02354 | 2026-03-04 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc84a72a-b075-30a9-831d-cf314a2d738b | 3.06094 | -60.71309 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23926f2f-510e-3634-aa4e-d297f4b1e321 | 3.06674 | -60.71205 | 2026-03-04 06:12:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0295d54b-675b-3e26-b2a5-a1365327abbf | 1.06299 | -59.48923 | 2026-03-04 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e6ef95a-b30b-3b1b-8380-c16e81cb5025 | 2.22573 | -60.74681 | 2026-03-04 06:12:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ca89277-5ec7-3414-9105-a3d25aed9a6b | 0.30332 | -60.45692 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 078038d8-f7a9-3f53-a255-78ea6a643112 | 0.04158 | -60.98886 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| ad7ab367-53c9-3c07-8c82-8b53d8f08b56 | 0.04089 | -60.98452 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 80b38eb6-e0d2-3a0c-a6d7-274fd7c87cdc | 0.31338 | -60.44067 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74864cf8-fc82-30b1-9382-06b814def7d2 | 0.48867 | -60.51432 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f8a4e34-bb10-38d3-abf1-6fa8cf360676 | 0.4948 | -60.51344 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c15213b6-1866-3aea-b038-c681f0975f8c | 0.46272 | -60.39283 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f350acfa-36b0-30e8-b010-cd4c4f90cb7c | 0.05814 | -60.97741 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9f6b329c-daac-3d50-9ba6-4bbafe017b76 | -0.50335 | -64.60608 | 2026-03-04 06:14:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75ae74b-fa99-3ed1-a8d4-f2ff8d960da2 | 0.45657 | -60.3939 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97aff214-082d-3264-abe8-f4cb6a3134da | -0.50455 | -64.60765 | 2026-03-04 06:14:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8ed342-2018-3010-a23e-0acf6188a818 | 0.45735 | -60.39865 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46a406d1-3606-3e6b-8e91-5a73c7d50392 | -0.15183 | -60.7583 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ea3dbe1-1e43-3a86-95e4-9fa7032834fe | 0.04757 | -60.98802 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8dc46680-e38d-3164-96ad-8dd4dc479627 | 0.46349 | -60.39758 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 355d3db7-899a-384e-b9d1-c25d1b8f65c7 | 0.03561 | -60.98985 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10778d37-05f5-378a-afc8-f6c4144c23bc | 0.05144 | -60.97379 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 32b76f70-a13e-3cb6-b221-fab2acca0cec | 0.27916 | -60.62003 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b675953-47d9-3bd3-9cad-f8d575e46766 | 0.04545 | -60.97465 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README12.md)
