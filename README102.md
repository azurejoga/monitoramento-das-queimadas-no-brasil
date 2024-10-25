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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b04af6dd-6066-3462-867d-f87662dc01b3 | -17.04984 | -57.47318 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f92fe05f-cc54-32f5-a47a-94c0afec20fc | -17.04817 | -57.43932 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 34010154-64b5-3444-a7e0-b2b0b34b8695 | -17.04706 | -57.4466 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0b9f4fc5-fe9c-3464-8260-04fb3bd57832 | -17.04595 | -57.45388 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0da9903-70fd-37fd-ae4c-611e4e08ccd2 | -17.04484 | -57.43877 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6745e172-572a-3905-ba54-486494175b8f | -17.04374 | -57.44606 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a4e385a4-7635-33b9-946d-4a5a755934ab | -17.04207 | -57.52406 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 53542fe9-6f5e-3fb7-aada-72a3de76c9f4 | -17.04152 | -57.50535 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 76d7fdb7-efd4-3408-a4ff-c5c607aeb5cb | -17.04151 | -57.44196 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 12c1a5c8-936e-355e-bf3f-37dd1527f2d4 | -17.04039 | -57.44924 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f180f642-6e5b-3109-8a0c-9bd9bccf7abb | -17.03874 | -57.52351 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6eb0ee19-6968-31d9-8774-dd8dd2471715 | -17.03759 | -57.46743 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 42d029b4-7de6-383a-b916-ebdf47c61d1c | -17.03542 | -57.52296 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 1c7b1718-dc25-33c9-a4f6-54884581eb57 | -17.03538 | -57.45961 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1401294e-f8af-3741-85d2-06cfca7be930 | -17.03486 | -57.50425 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6d0110e2-8832-3986-8bfd-94469d22c2d3 | -17.03427 | -57.46688 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 891bcb23-2f0b-352c-a0ee-20b8dc3a3438 | -17.0332 | -57.51514 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e44cb755-c610-3c58-af2b-6724ab539dc7 | -17.03255 | -57.50014 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c5716704-26aa-3a2d-b310-dcc5b78d6a41 | -17.03154 | -57.52604 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 5bebb47b-3732-33a9-9c5b-a57032e461bc | -17.03031 | -57.51468 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 59ce64c7-516d-3763-b2c9-fd9e13414080 | -17.02926 | -57.47725 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c108f1e0-974b-3521-9842-bbf1f88caad9 | -17.02923 | -57.49959 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4e7d8789-bd80-3fac-bcca-39261c6d1667 | -17.02761 | -57.46578 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5f0a0302-1b87-3a5b-87e8-4c57df9aab5e | -17.02705 | -57.46942 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| dab7b7fb-6c96-3066-acdb-fe5cf7c8eed7 | -17.02596 | -57.45432 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4c06a3fa-678b-3234-9b13-1380820aa3c1 | -17.0254 | -57.45795 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ee62f1db-8c7d-33d7-bc36-b0a3517e35df | -17.02372 | -57.46887 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cf3f3763-25dc-370c-927c-eb2c9bae211e | -17.02313 | -57.49486 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e320aa98-2961-384a-bd08-3ba6b4206bc7 | -17.02258 | -57.49849 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 307af225-3e6d-357f-b5b2-d6ebadf16666 | -17.02254 | -57.52084 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| eb2bc37e-149a-35a2-9105-fad809d67672 | -17.02202 | -57.50212 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fa998bd7-c4b6-3dd8-8c1e-7857aa0ab6d1 | -17.01481 | -57.50465 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 547c7041-6a64-3cb3-b2d9-ac3c4b52a318 | -17.08872 | -56.88417 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b5136d62-b8cb-3737-bad2-5883885cf208 | -17.07981 | -57.3885 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a25261cf-1cde-394e-b2d4-7faef9592884 | -17.07245 | -56.87773 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e3464f34-723d-3b74-83d2-aac601425ab1 | -17.06964 | -56.87346 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fe5605ba-0371-3f0b-87fe-8f97c0e4b7c9 | -17.06908 | -56.87719 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 75106a19-2892-34d7-b879-b76983b49702 | -17.06572 | -56.87664 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c9edff4c-374f-3bbb-bc31-5411c1efcb49 | -17.04157 | -57.39717 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf2a0152-6747-3f90-9345-88426a2946f1 | -17.04157 | -56.85364 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5fecd932-f8e9-3f84-ab8d-4852368ac9dc | -17.04101 | -56.85737 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 34fd3d56-7c3b-39b4-bc7a-a0de69cca569 | -17.0388 | -57.39297 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ccc71f3-8ca0-3d40-911d-48d88014a55b | -17.03824 | -57.39662 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a19c0d78-c3a1-3873-a246-4ca753b7e5f6 | -17.03547 | -57.39243 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| af8d0337-0979-323f-a64b-44987e40d19f | -17.0349 | -57.39607 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 42a938c6-9373-3d7f-9308-407f2924d624 | -17.02382 | -57.37929 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b0c86954-58ad-32eb-ac2a-afd3e1f4cd34 | -17.02048 | -57.37874 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d8161caf-a3f0-3ecd-ba73-a8bc8c595749 | -17.01873 | -56.85814 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 093706f8-422b-3f45-ad49-a42867cc6da6 | -17.01537 | -56.85759 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cb4e3180-c684-3ce6-98ed-8c032ab4e3e8 | -17.0148 | -56.86131 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 61369856-ed1d-3730-b237-887c19ba570f | -17.01369 | -56.84586 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a2daeb60-96a0-31b6-b064-90ed011dc73b | -17.01272 | -57.3625 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f38816f2-676a-3024-b7d7-cb56ddb68106 | -17.0127 | -57.38493 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 357e63e8-0dba-34aa-894b-b2a4808329a6 | -17.01256 | -56.85332 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f569f42a-ccb2-34c9-9fd8-889345e70c2f | -17.01049 | -57.37709 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec9d0025-a503-3316-bbbb-b48607c4abad | -17.00939 | -57.36196 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d44cfcd8-0578-3804-9222-291079ab36d6 | -17.00883 | -57.3656 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 63ae97a9-093d-3d5b-825e-abe84d556de8 | -17.00882 | -57.38803 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 413f76a1-a405-358d-8a48-f1fa6f407687 | -17.0066 | -57.38019 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8dadf784-b82b-3fa3-b1b4-79b82e9819dd | -17.00162 | -57.34572 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dbd45d0e-97d7-3f9e-a9f1-667bc5bf14e5 | -16.99995 | -57.35666 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4c6da78a-1989-31e3-85d7-580c07ef0c4e | -16.99773 | -57.34882 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 2ed7aca4-40b1-30e7-8b49-20b8208bf336 | -16.99717 | -57.35246 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 8af90207-beb1-3631-ba31-bcad2d56a64e | -16.99716 | -57.37489 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 24d45da7-48fa-324d-b4c4-1c36eba5e6c0 | -16.99661 | -57.35611 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 85fcc6bd-5e05-31f0-a7aa-dbb5e5c90af7 | -16.99384 | -57.35192 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c50decc0-c592-31ee-b6c5-4e1f8565f4db | -16.99327 | -57.37799 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f2b532a9-b7ec-34ad-be83-72a9ff47c6ac | -16.99272 | -57.38164 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66a5a371-6d46-38bb-8c8f-afabdf619308 | -17.08592 | -57.41568 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f17314d0-fd2d-30ca-ad26-2f1e53bee514 | -17.08536 | -57.41932 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b494322b-6a7b-3c7e-91e5-0d8b5cf2a6d2 | -17.08369 | -57.43026 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| aa747c8f-032c-3e01-ad4a-29aaf8110398 | -17.08258 | -57.41513 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 7851d037-fd82-33fb-933c-f7048bb43b68 | -17.08203 | -57.41878 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 7a9c0441-8e3b-36bb-ac53-61d48599b7c4 | -17.07925 | -57.41459 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| a1541640-1454-3c2b-bbd9-e8293fdf4f2e | -17.0787 | -57.41822 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6d269187-f590-36d7-8ec1-24f98560130f | -17.07814 | -57.42187 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 78fdfa29-2038-3ff0-a0c0-69c52d1ef114 | -17.07703 | -57.42915 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b962347a-7156-3b84-8a29-a9cb3ec143f7 | -17.07534 | -57.48486 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f114d72c-7dfe-3e6e-9732-b35cddd5cf9d | -17.07425 | -57.42496 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e3ea68fd-c16d-341e-8526-f179a2756217 | -17.07369 | -57.47339 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f2aec424-610e-38f4-8813-5b1d422d293a | -17.07257 | -57.48067 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3495eaa1-b111-3f2b-8c80-5dd372af3e4d | -17.07202 | -57.48431 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8afb0434-9eb1-317b-a0b9-9c26a9f681a8 | -17.06981 | -57.4317 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0c6dd4fa-0566-366d-8b9d-ea16dd5bd33f | -17.0698 | -57.47648 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 246f8aa1-f8f1-3db5-98b0-ae6897c9c4db | -17.06925 | -57.48012 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 969c6a9b-40f5-31be-b285-52f63ad3b8d0 | -17.06592 | -57.47956 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 95147b9d-6e1a-33a2-b0a9-bb6e7cb47e99 | -17.06536 | -57.48321 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 893fbd5b-dc49-3fcc-b8ce-c4e3c797d40f | -17.06481 | -57.46447 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 922b4b90-b266-3f1c-b9c8-d7c99b0fddd0 | -17.0637 | -57.47174 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 45c0692a-b971-3df9-bebc-8ff5b1cff9a2 | -17.06259 | -57.47902 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2933fbf9-7cd8-3db1-a715-27b4d7332355 | -17.06204 | -57.48265 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6b4082ef-ead5-31f2-9c1e-e38452cfd72b | -17.06204 | -57.46028 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0f1400c5-6df0-37be-b829-fb8011f2cb6c | -17.06204 | -57.43788 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f319dade-0b36-3b5e-a375-73e0299f76b1 | -17.05982 | -57.47483 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ff14ad82-2746-33fd-8078-f3b4d50da538 | -17.05927 | -57.45609 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f34514ff-c690-3d8c-8ff2-1b52a9a92464 | -17.05872 | -57.43734 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 72c69743-3c29-3c80-afed-e5fb65e1cce2 | -17.05649 | -57.47428 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eb9b86d2-7bc4-3b87-95fe-bdd8d01fe073 | -17.05594 | -57.47792 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3e8c51e1-5db4-3ccc-909f-750044cf5629 | -17.05594 | -57.45554 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b9a858f-c9f4-3185-8c89-79bc90443bc3 | -17.05539 | -57.43678 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |


[Clique aqui para ver as próximas entradas](README103.md)
