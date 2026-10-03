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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17618e08-8818-30f2-be84-72e75fda2429 | -2.9192 | -54.0954 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb7fb737-d590-3c35-92b8-88818a54fe91 | -2.15068 | -59.2313 | 2026-10-03 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b9fccd1-b1ad-3ea2-ad65-08fac9a99ed4 | -2.22708 | -51.92768 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9610fb04-6d65-3d89-8126-4ee0681e87b2 | -2.97401 | -53.2757 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4277460d-2f6b-3d01-9493-ff8e4c72ce98 | -0.35145 | -52.01476 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea2ca1e8-8102-3677-b4c2-69313c088b1b | 4.8065 | -60.28666 | 2026-10-03 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b926a5b5-01b2-37d6-9351-23a48461b846 | -3.27788 | -53.83308 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8d7d9daa-f0d8-3a81-be31-b71870c43985 | 1.93937 | -55.73098 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34270840-1dbd-3922-a100-59b5120cf4dd | -2.88997 | -54.12737 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0047dd9-0f10-3888-979e-852c5fb64e4a | -1.26965 | -54.56723 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0499d62b-c917-3d9a-aa7b-999b264c71f2 | 3.79297 | -60.96933 | 2026-10-03 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b862fa6-9fad-3f39-bff1-e28fe7160418 | 2.35421 | -50.75356 | 2026-10-03 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e425c0d9-6c08-302d-b08e-a74294871de1 | -3.12594 | -53.73141 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c06a6904-f7fa-33fa-a5f7-6882ef4e64c6 | -2.92712 | -54.107 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1635f3ea-6ff2-3922-a1e9-011f930dd1e3 | -3.22362 | -54.31028 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd557736-de2c-38a1-9979-5e2a534a6c26 | -3.29444 | -53.84351 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e36c83d-0a22-3df9-a603-b6aeea6c3454 | -2.96801 | -54.09809 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a19b1726-8792-350c-bfa0-e658fbfe2f5d | -3.12024 | -53.73611 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3aa239f4-6eb7-39c1-98af-b734668df4b1 | -2.4081 | -56.82557 | 2026-10-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d60e4e4-b422-3b3c-a4a0-a06c93306e57 | -3.17614 | -54.08099 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0323155c-516d-3c0a-a446-d0b1a3f09d75 | -2.17472 | -49.77954 | 2026-10-03 05:33:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86bb411f-82ef-3c91-b0e2-27f625236238 | -2.32393 | -60.0651 | 2026-10-03 05:33:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6897abc2-165a-38d1-b796-623ea8e4d6ca | -3.02722 | -51.2767 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e130d2df-f6d9-38b1-ac0b-21a1ed703711 | -3.00085 | -53.88014 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a59906c2-b908-345a-9796-ac328b4b1165 | 0.65839 | -59.56668 | 2026-10-03 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 466042b8-e095-3559-81ed-9ef83a32547e | 0.89736 | -59.70163 | 2026-10-03 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1df9d89f-0585-3d6a-805a-b4b71046ccfe | -3.09426 | -51.10316 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04c2eaae-10d7-3771-8dfd-552d20a4b987 | -2.86058 | -49.62961 | 2026-10-03 05:33:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6a76f13-4e9a-3cd5-b246-83d44c646659 | -2.92966 | -54.15969 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 418f893e-e298-3681-a523-d4c61f0031cf | -2.92316 | -54.1012 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08af47bd-5d40-306d-90c1-1a82dd18fcaa | -2.97613 | -53.26149 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae0cf04e-3168-35ce-87c5-54d9ba60bc56 | -3.11943 | -53.74153 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e1317776-9dcb-3169-a5e9-a765bcf02114 | -1.14505 | -54.15945 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85388a7c-0b5e-318e-a2bf-021cbe313b2b | -2.88766 | -54.14241 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a27dfce-3d10-3371-aaf3-2718db558130 | -2.91524 | -54.08956 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7854467-91f3-320f-90b8-1bf11f12640a | 3.79965 | -60.97205 | 2026-10-03 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b14052-1b88-35fd-ab44-4965f7129fb4 | -3.2844 | -53.82311 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3cdfd532-bf0e-395b-97cd-dbe50811b611 | -3.29036 | -53.8374 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3fa6137-e28e-3746-83c8-89d006c1e9a0 | 1.80435 | -55.58969 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2413502-137d-3530-85e8-a63537942537 | -3.01051 | -53.88159 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f351c7b-b477-3d56-9469-7ba76f772b87 | 1.92392 | -55.8104 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 580b9776-017e-342e-ab83-7ceec01545ba | -3.10053 | -50.29724 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 200089eb-1c00-32a6-96a0-abc862e69e76 | -3.70084 | -50.97743 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81b89ab8-96af-308f-b95f-22552293adf3 | -2.98034 | -53.26781 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c680f540-5c63-3d99-930c-f01d0143ed57 | -2.40886 | -56.8206 | 2026-10-03 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bfb39bf-bf1d-38f8-b8e7-cccf2c007c8c | 3.79632 | -60.97251 | 2026-10-03 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c45265-bafe-3d63-89b5-2cfebad5251e | -2.32729 | -60.06562 | 2026-10-03 05:33:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39c7c532-105a-3918-9bae-59fb8bc8cd59 | -3.17134 | -54.08043 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0856c2ef-ebe9-3a91-bef2-c9c742ff03e3 | -2.22762 | -51.92414 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1c1e245-63f9-32fa-9fea-8a85e532523f | -3.28708 | -53.82584 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd1a76f8-6566-39b3-b178-f897ec8b6c02 | -3.28879 | -53.84812 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13619d1-ffa4-3d86-8700-a3b2e197a3d1 | -1.26517 | -54.56659 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbbccaa5-8a84-3aee-af96-c7499a31c95f | 1.93543 | -55.73163 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21397dd5-1382-3dc7-84bc-80ac7c96345c | -3.16902 | -54.09601 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d9151cc-f71d-3609-8d82-f6c7ea2a8bff | -3.1874 | -54.10358 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d8dc89a-c76f-354c-b0e5-c8f9be0d088e | -2.89162 | -54.14814 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e3c3878-c337-3e61-bcb8-5d3ef8b85211 | 0.37765 | -60.00097 | 2026-10-03 05:33:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf2639e-5f0d-32f8-a6c9-11abbac4b34a | -3.02627 | -51.27682 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3d1f2ac-bb52-32fc-96cb-3f24365095fe | -2.92844 | -54.10253 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af5df490-fde7-3ff8-a073-0711282855c5 | 1.7781 | -55.60441 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bbf6adb-f2d5-37af-a082-a5469223a237 | -3.13246 | -53.75455 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e673b4f-d742-3ea6-bb13-8b56ccf9678b | -2.91048 | -54.08884 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e830fb0-03c8-353b-907f-9c71c18fbc45 | 1.91433 | -55.77611 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f1c88ff-153a-36de-bd41-1d41e61b64fc | -3.12269 | -53.75311 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8274e4d9-4716-34a7-a7a4-76588a4857e2 | 1.22567 | -59.97092 | 2026-10-03 05:33:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d80dd9-c97d-364a-b093-cd688db19670 | -2.89074 | -54.12234 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b5c4db0-352d-3ded-ad3f-c542be98ffba | 1.79238 | -55.59159 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f31fa74-f31a-3aa2-9d30-ef187ac2ee4a | -3.28357 | -53.8285 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac610506-aeac-3273-b075-e1bb663307f7 | -1.26136 | -54.56149 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a252c4b5-f715-36d1-b503-015e0e2bb011 | -2.97571 | -53.26433 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e11a7190-e785-3a6a-bf8f-4f34fda56528 | -3.1778 | -54.10255 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c2eab3-060a-3432-858d-ff7c40649d35 | -3.22985 | -54.31393 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b48657-d2c7-3835-9f2a-2efbbd602d27 | -3.71165 | -50.65718 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ceb10ff-150f-3dcb-a5fb-eec8e55e10bb | -3.12676 | -53.75927 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fc6b690-963a-3c6a-9c38-2d6005661970 | -2.17545 | -49.77456 | 2026-10-03 05:33:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 182bf637-9d4f-336b-95eb-2f5aae1febc9 | -3.00971 | -53.88691 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10217a77-59d2-3784-86b1-21854089929c | 1.2229 | -59.97491 | 2026-10-03 05:33:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2793198-9efb-3d90-8d3d-a702d68257aa | -2.89542 | -54.09185 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11d5b792-83f8-3208-83bf-f562e4154e27 | -2.97486 | -53.27001 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7c45a69-409a-3345-9815-42e414b58446 | -2.97528 | -53.26717 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1058947-184f-36cc-a373-280bb3e1d5a0 | -2.15126 | -59.22755 | 2026-10-03 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e71461-2709-3e53-b5ac-12d9fd2a5eff | -3.2908 | -53.84619 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e26f8c9-041e-3c92-9579-cf3ad6562441 | -3.28145 | -53.83031 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 762dcae2-1ca2-3416-8817-36635096aa17 | 1.78496 | -55.59626 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 094e934c-87f7-3f51-9090-90a32c9a1f5b | 1.80379 | -55.58623 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0cda760-498e-3312-928f-e623a83ba5c5 | 0.62368 | -54.41202 | 2026-10-03 05:33:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ca49955-d012-3596-a19d-51cb12b8ce3b | -2.14781 | -59.22703 | 2026-10-03 05:33:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4c0ad40-760f-314a-99db-2a9d5b104bc4 | -3.28759 | -53.83475 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4848c0f-5784-3157-8503-97733a35e220 | -3.12513 | -53.73684 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66c54abd-baf0-3a52-a788-374179b027a4 | -3.17535 | -54.08628 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0e34b0a-23f4-3323-bf02-75396905ddee | -3.12758 | -53.75383 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f044275-c563-3cca-96c6-39805ca4808f | -3.14062 | -53.73357 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 298425a3-6882-3a0d-b717-f13e39828b06 | -0.362 | -52.01631 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a28447f2-168e-338e-ad8f-1a4157d8d241 | -3.22589 | -54.30816 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4225d6cf-c9bb-36e3-af3f-3c21ca671a14 | 1.78552 | -55.59971 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 796dbf33-a60e-3573-925e-2849dab660ee | -1.37119 | -54.63774 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db5c7f2a-c617-332f-9b1c-fc72104b66b7 | -2.56988 | -54.74464 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19dd8e20-dcdd-3b07-8586-36ba1d18b479 | -3.17302 | -54.1019 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bf76fcd-6067-3470-aa1c-0dd37d571f4a | -2.04824 | -56.86762 | 2026-10-03 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 185f67ed-5f6d-3652-b670-987b6c563b17 | -0.3615 | -52.01954 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README42.md)
