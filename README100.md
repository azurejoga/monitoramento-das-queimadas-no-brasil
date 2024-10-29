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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c26a20-ed34-3855-a27b-889bd9726f2a | -3.23366 | -50.72636 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c87a0df4-f5e1-3bc5-bbf3-dbaafd2f2549 | -3.23302 | -50.73074 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be0e06a5-1778-3584-b49e-65747b4d7aa2 | -3.23239 | -50.7351 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5875ae52-6e66-3298-9cbd-f00e9f0b7fbe | -3.56469 | -51.50665 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cab3560-480f-3529-a261-56bcfde36e92 | -3.55903 | -51.50583 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c4ae933-82a6-3bc0-aa03-2d365ef142cc | -3.54603 | -51.51565 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffff93d8-5934-3e73-858d-87819ab23d89 | -3.54549 | -51.51941 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc6e1421-6fda-3ded-b303-e1b49e71536e | -3.27433 | -50.69728 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5663e13b-46b7-35b3-bc90-c2708c11cc43 | -3.26839 | -50.69637 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85a0cecf-f96f-38bb-89ae-cdebcfa63c79 | -3.26776 | -50.70066 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b1a3b07-d2a3-3bac-aa44-da4909577e81 | -3.26234 | -51.01884 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df6c0c44-0304-30e9-b35a-b268a4e83c66 | -3.26185 | -51.01931 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a0a4d3d-e741-3b7f-b7f7-9727aa36b00a | -3.26172 | -51.02293 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e26079-0936-3a33-9ae5-c45ca70856eb | -3.26126 | -51.02341 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72eb4f92-0593-3635-8f5d-a9ed657e8056 | -3.00709 | -51.77332 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e827afd2-1522-356f-93d6-7d0a1a7bd42c | -2.92499 | -51.75792 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47f930de-7880-3482-bee7-19cf283078aa | -2.91945 | -51.75726 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0aa1283b-5b83-3bf4-af2b-601cb0dc4ea8 | -2.91341 | -51.75992 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 612a560b-34b2-3387-bea9-0bef370c1780 | -2.91288 | -51.76344 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 123da728-73eb-3101-8803-6f7dc54ebc05 | -2.91236 | -51.76693 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9ef31a8-7e54-3c9a-8c79-706850fdad2d | -2.84477 | -51.80538 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3b89e36-5e0d-3418-88d8-d90f656fe1cb | -2.84425 | -51.80474 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b23f4146-cfc7-3590-a050-a14712a45073 | -2.8437 | -51.80828 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 701556d5-fbce-3453-a482-778f6e5d7432 | -2.83928 | -51.80453 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d88750bf-b7d2-38af-8fcc-ce5edf0af596 | -2.83876 | -51.80813 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc2dc829-fcb2-3553-affe-4aa839a5c389 | -2.83876 | -51.8039 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb81a8b0-08d9-3761-8cbc-e7b4e46a0075 | -2.83823 | -51.81171 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 348c4150-19f5-3039-888c-dbec0b036d02 | -2.83821 | -51.80749 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f883878d-a892-3728-a9cc-284cc9d5921e | -2.83766 | -51.81107 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 06bea715-3499-3327-94c0-82318a27fc75 | -2.83327 | -51.80726 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4d2d89-aa73-3b77-bc6f-02e10122085d | -2.83275 | -51.81086 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ea7ee3e-eb99-3d67-84e1-39433b393628 | -2.83217 | -51.81022 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8820468d-9f17-34dc-ad26-5e6820eee272 | -2.83162 | -51.8138 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd8a6033-a6bb-32e7-a232-3c7fbb9467bd | -2.80475 | -51.80603 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e119e3e-a9b6-3dfb-8ebb-7da4b1aa553e | -2.8042 | -51.80965 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b5c1a89-42e5-3bb4-ad15-88d4a850a627 | -2.79928 | -51.80506 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85e74224-5827-3226-aae6-5259155b60e8 | -2.79872 | -51.80878 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff5aeffa-7693-3004-bc3a-095f12fe5af8 | -2.79325 | -51.80783 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f6b375e-4487-38c7-969a-20916e7999a3 | -2.79282 | -51.95807 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad37057-e112-3abc-9ec1-9646ff2cab76 | -2.79269 | -51.81154 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 046da0d4-b507-3c3b-b767-85a6d45aca1e | -2.7923 | -51.96154 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50864d8e-2574-3c3e-a3d9-213b9bbf3a50 | -2.78739 | -51.95728 | 2024-10-29 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fdda195-62da-3f17-89d1-c009d887fcd8 | -2.73791 | -51.72678 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d49414c-c799-3d69-a414-1921690a3a79 | -2.73786 | -51.72641 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25795a4c-0587-3e0f-908b-2c05844e7881 | -2.64996 | -51.75013 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b203e547-9b05-3075-9625-d694dd1b6760 | -2.64943 | -51.75372 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d91a13f-0f66-3590-9a4f-482a89134737 | -2.6489 | -51.75729 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54793a42-0600-380c-becf-02b74a86901c | -2.64605 | -51.73853 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ef70166-919b-325d-8402-19a62a2c7135 | -2.64552 | -51.7421 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555dec68-ec86-39ec-a5c5-53064c38a733 | -2.64499 | -51.7457 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9327c37-7e38-376f-a75d-399f6e3ad02a | -2.64446 | -51.7493 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c29c6606-d8a0-3829-b1a9-e07ecd22033b | -2.64393 | -51.7529 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e9fd389-708f-3f24-8fdd-e3e9bf0ebcd7 | -2.6434 | -51.75649 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 22e70f2f-de4c-3455-b4e3-9afda516e3a5 | -2.64108 | -51.73409 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6640b4c-04d9-3f44-a8a4-c52a8707572a | -2.64101 | -51.73176 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8e66844-c0b9-3f44-b2ce-7688f3bb11ea | -2.64045 | -51.73533 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcb3cde0-d6d1-3aaa-9ccf-d6058bfa2289 | -2.6395 | -51.74488 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61642765-af82-3213-9d26-a5127277d3e1 | -2.63896 | -51.74849 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b76e2d5a-fdae-3f69-85fd-926c1a295d01 | -2.63879 | -51.74609 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcf9e30-5b67-3c55-872c-19e453cfd52d | -2.63824 | -51.74968 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e367d064-30bb-387d-8648-9f64f11cb3d4 | -2.63611 | -51.72968 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 491f4241-91ad-34d4-bc4b-0fffd4718c1b | -2.63551 | -51.73093 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edfb5f8e-45ea-3dbd-a2e0-e0acff8688e7 | -2.59983 | -51.78041 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 677cade2-c23a-371c-b93e-8272e527dc27 | -2.59929 | -51.78399 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feac273d-1db7-3f6d-a3d1-e3e1d45a7661 | -2.57815 | -51.84945 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 240386ce-7b04-362d-acc7-b5b8276cfcc4 | -2.57216 | -51.8522 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b3fbf53-f6cb-374c-ba61-06b38ca7f5fb | -3.07534 | -51.35519 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 561ba47d-7dcd-38fe-b50b-3ca1f5b93a1a | -3.07475 | -51.35917 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d4586f4-ec5b-3c01-99b9-effdc298e51a | -3.03275 | -51.44722 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86288a44-e24b-33d6-8dee-cf1392d7ce6e | -2.9563 | -51.00093 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 567e2261-375b-31ab-8bfe-5fdcca8c8b17 | -2.95595 | -51.00129 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d293ac1d-810e-37c5-91a1-8ce57e979b53 | -2.95569 | -51.00512 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f487f95-4d8b-3254-bdc2-59f590c87b5f | -2.95531 | -51.00547 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3e22bd-f1e1-3562-9938-f4f66b479510 | -2.89775 | -51.48242 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d577c651-7161-3044-ae21-74b1f5829a9e | -2.8972 | -51.48622 | 2024-10-29 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d1f1ead-5dd6-32c2-9924-e1ad749eef75 | -2.87954 | -51.31133 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 501b2071-2055-3369-a6ab-ef8d260722d4 | -2.87386 | -51.31049 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b77e2f2-5780-3ea7-9046-4866f3e12339 | -2.87328 | -51.31433 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad35b631-eb2a-3af5-915f-83c61321de4f | -2.54511 | -51.16957 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69e0befd-9997-311c-9fa9-0e3a83b2e51d | -2.54335 | -51.18134 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cabb53e-34cf-378b-88aa-77c002a766bb | -2.53883 | -51.1726 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3394d22-bb90-3593-9628-da6c45ade2b7 | -2.53824 | -51.17653 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b45262a4-ddba-3e00-a312-aef86d7f327b | -2.53765 | -51.18047 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93f251d1-a167-3446-af3c-1fca6671abdf | -2.53707 | -51.18442 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29edf90-167d-3234-a555-4808c44e3619 | -2.53648 | -51.18836 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e85bf669-ee41-33e9-a87c-df79941e8159 | -2.53254 | -51.17565 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e23c1bff-cbeb-30c4-8bb2-cfd59e8f4b99 | -2.53196 | -51.17959 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94780ada-ebba-3d07-8b00-8bd3a5040323 | -2.53137 | -51.18353 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01f88d7b-e51d-39b0-a902-99b0f0dcdd7d | -2.53079 | -51.18748 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af02c9d-0e8e-3aab-a9e0-1fc073dcb3a5 | -2.53021 | -51.19138 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ace03868-e374-3398-acdc-9cdd867d5984 | -2.52963 | -51.19527 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58a97fc1-4d1c-3698-99d8-9352e65c8e4b | -2.52685 | -51.17476 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59617473-385d-38f0-bd4e-162e359b5305 | -2.52626 | -51.17873 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4cb6c5d-0e73-34d1-b55e-426e26bb18c1 | -2.52568 | -51.18266 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9ad8b0a-bed8-37b5-9e1a-154bd66557b5 | -2.5251 | -51.18658 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09daecf6-60dd-3866-859d-ed1ef6597431 | -2.52451 | -51.19052 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34b206da-0b84-3c6c-a282-fa3159624da8 | -2.51999 | -51.18176 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71f6daf4-8d97-3cc9-add9-588e12499f82 | -2.51372 | -51.18478 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eea3f62-0cc0-39ce-b3a5-bc65f1000f11 | -3.16462 | -50.59276 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491de5fe-c113-32fa-a6e4-b50d74236097 | -3.15864 | -50.59189 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README101.md)
