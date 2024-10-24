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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4442474-c0a8-3a28-bbdf-58d38a0564e3 | -17.00342 | -57.51376 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c837782a-05c7-335d-bac8-8b704e1a878d | -17.00298 | -57.52437 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b6f2242-4278-3dca-a64c-63b77f83244b | -17.00283 | -57.51744 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87e3580d-9f85-33e2-bd2d-947db3e325ca | -16.99672 | -57.51259 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ba39c9d3-7c82-38c7-b359-bbe6a611fc5b | -16.97148 | -57.5195 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ef70eefd-cd51-3b77-ad6e-93523a533fca | -16.96418 | -57.522 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| fbaa6f54-3b6f-3f1e-afb2-2b4849977988 | -16.96143 | -57.51773 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1631fb26-59ff-3f9d-a096-a700e39657e9 | -16.9551 | -57.53552 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1d66a08c-a23e-3100-a31b-bf55c84f32d7 | -16.9478 | -57.53802 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ccfd5fc2-2ce3-347b-b589-d8bf728a1cb0 | -16.94743 | -57.51906 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 542a79be-fbd1-3e4b-9a38-06ecac6eabac | -16.9472 | -57.54169 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 86481ea0-9c5e-3e89-95ba-1e051e7be7ea | -16.94444 | -57.53743 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 30164516-ad80-3a45-8819-446a0dd848f2 | -16.94385 | -57.54111 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bc3cd5b3-d5f0-37d3-be5b-8d28eb52bf70 | -16.94109 | -57.53684 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 0f1d0d1e-e95f-3c05-b4eb-f5e70319903a | -16.94049 | -57.54052 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71b58af7-33c8-3b6f-b371-592ad41ff91f | -16.93677 | -57.52097 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7729f0e8-e7af-3183-8c26-cb8530b1e7ac | -16.93618 | -57.52464 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dfd89ca2-a84f-3cea-b7e5-3632361b9029 | -16.93558 | -57.52831 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e632a046-ac32-3a57-9b77-4a56a7fc2a11 | -16.93462 | -57.51303 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 416ebc0a-f73f-3501-accd-51d10d234c26 | -16.93402 | -57.51671 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| bd0393d3-f7a8-35d9-9690-4786e7eadf69 | -16.93223 | -57.52773 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e848d3de-c267-3234-9b5d-0cd19f148482 | -16.93126 | -57.51245 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dddea42c-27a5-38d9-9343-5d3d695fe752 | -16.9175 | -57.49116 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d1196ce3-ca8d-3ad2-b02c-2b36525b189e | -16.91415 | -57.49057 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| eb6d8518-3491-3be8-85aa-97ba1b3b4821 | -16.91355 | -57.49425 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9ab2c980-4eee-3be8-b00c-9c599c145938 | -16.9096 | -57.49733 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bc276a8a-b1af-3ada-a0db-c676c423c63f | -16.89416 | -57.67643 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee58e5aa-6400-3599-af2c-79a460d2e9a6 | -16.8528 | -57.68865 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ab9df09d-cebb-3fd8-9266-28b51e5c234b | -16.8522 | -57.69234 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f9118e5b-1d79-302e-9db5-a725e37d47d0 | -16.7039 | -57.45109 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 20c7893f-77c0-3894-9a27-e9ca5106c9b8 | -17.24353 | -57.23908 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| dd2d929e-d2a8-3c94-8671-0bcacb615834 | -17.24337 | -57.26151 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 80589264-4dc4-31b6-9f97-133270f5d8b2 | -17.24295 | -57.24271 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 4a2969fc-c00c-39cd-b0d4-e85569118dd9 | -17.24003 | -57.26093 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 901c4936-c44c-3e61-8189-63fa663d78b9 | -17.23961 | -57.24213 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| b9088313-e7e1-3958-96a4-bf86fedd4c9e | -17.23903 | -57.24578 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 06e176ab-88be-37b2-81ce-b44a2b499b88 | -17.23845 | -57.24942 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1cd0232a-f4c4-3145-b426-1582d0e05d83 | -17.23828 | -57.27185 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5d3aba70-926a-3161-b4ac-022e0aeb7b18 | -17.23769 | -57.2755 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e8bcb461-4855-3913-8c0c-af739f166a36 | -17.23627 | -57.24155 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 11089c7a-98cb-38e5-a315-9eca481a887d | -17.23569 | -57.24519 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a58a885b-e19c-38a7-8d00-7066d3bacaad | -17.23511 | -57.24884 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4c70cb70-b235-3dd8-9e96-9c4557840621 | -17.23177 | -57.24826 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4787dcd3-684f-36ed-950d-49e2eb66954f | -17.23119 | -57.2519 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2c607b41-8db3-3a15-9c0f-f3b9b0bd8046 | -17.22885 | -57.26647 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e9ae809-3037-38c2-8f71-d9be7635a3ab | -17.22827 | -57.27011 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ecc701d8-71b5-35f9-bf6c-2768be81af4c | -17.22785 | -57.25132 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dd9b5911-cef0-31c2-872f-f4713e0f8a01 | -17.22727 | -57.25496 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 616ad197-4afe-3e14-9aa9-5ee2f6cbd3f2 | -17.22451 | -57.25074 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cf1bb84c-00f3-38fe-8167-765aa611d3ba | -17.22334 | -57.25802 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1809a4f4-b1db-367e-9ccb-0eb57862b8ae | -17.22083 | -57.29504 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a04726cb-9cca-31e5-8623-59bf777d3c3c | -17.22025 | -57.29868 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 034c592e-0628-350d-ae6d-7db335e232ae | -17.22001 | -57.25744 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e0d0cbf4-9928-3d60-ba3a-dc74967b6a7f | -17.2155 | -57.26414 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aec2ad66-ab09-33ad-be61-f061484e8cf2 | -17.21217 | -57.26356 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f54b5ee7-7fdd-3db4-a35d-20ec4dfe6195 | -17.21099 | -57.27085 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6a5bada9-839a-3091-8799-7243879d9eb2 | -17.20765 | -57.27026 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 06f22f8e-f9f4-3dee-8809-05f55849507a | -17.2018 | -57.30671 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c9eea7d7-2593-3b4b-96e6-f28980e6dd42 | -17.19512 | -57.30555 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 73c4eed0-c0ec-3702-85ec-36c3ab8fd0d3 | -17.19079 | -57.2898 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 24f02bbb-9204-3676-99ee-e11c6bdd94fc | -17.1902 | -57.29345 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c3a662d6-3419-3354-b0d7-bb954d0fe215 | -17.18686 | -57.29287 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 99a46081-d545-3f09-b3d9-2796722ac9ea | -17.18628 | -57.29651 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0e23d98a-41dd-3bfc-9461-653d305ecbe2 | -17.18569 | -57.30016 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c1711970-48ec-348f-bbee-18660671395c | -17.18235 | -57.29958 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6bd84c8c-33d5-387e-bf9e-36b125c0e62a | -17.31398 | -57.28135 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 896ff225-8544-348a-9fee-7a2e20aff548 | -17.31064 | -57.28077 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8e79714a-5d06-36a3-a346-287a91d61f77 | -17.29946 | -57.28632 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b7e7843f-30a3-3b20-ae6a-b56fdbd43af9 | -17.29671 | -57.28209 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 99fa1e76-7e1e-3c36-844d-e1e48bc7a753 | -17.29612 | -57.28574 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 52a601ee-48cf-34aa-853e-624bfd684cab | -17.29337 | -57.28151 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b0eab245-ebe7-37fa-80be-d7c70684006a | -17.29279 | -57.28515 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0744edad-7cb3-33e7-98d7-bc423eb13522 | -17.28435 | -57.29492 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7ae9eedc-117e-37d9-9b8b-0cb216376480 | -17.28376 | -57.29856 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9ed7529-8ef4-3328-9a5f-ebe86b37a319 | -17.28238 | -57.26461 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4a6a2e93-6486-32a7-8b22-3f537d749966 | -17.28179 | -57.26825 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 55e8a941-d7e4-32b1-8357-0a79c3ca82da | -17.2812 | -57.2719 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 11d22d76-c23c-3b5d-849f-bc14236af68d | -17.28101 | -57.29434 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 042d5c9b-e90e-3df3-b1e6-b9bfe7989674 | -17.28043 | -57.29799 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 236e2622-56eb-3840-99d3-e0c1b1b29441 | -17.27984 | -57.30163 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 08392dd8-e5d1-36d5-bde2-4e216f81afb3 | -17.27845 | -57.26767 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3c4f1ccb-365a-3fb7-ab0a-0e25411eaa2d | -17.27709 | -57.29741 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 72b785f2-b5a2-38c6-994a-58df08237d06 | -17.2765 | -57.30105 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6afd51c9-ac60-3dd8-8d2f-17c38392846c | -17.27511 | -57.26709 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 10dab51a-376e-30a3-90ce-78275ded25d5 | -17.271 | -57.29259 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d38c46ca-b5c9-3f64-9e7f-4dca833ff79d | -17.2706 | -57.2738 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3b825de3-c802-328f-b80b-e975849b1861 | -17.27041 | -57.29625 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e27aee5c-bbac-39c8-9908-8c1f6389ea81 | -17.27002 | -57.27744 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 35694d34-7752-3d36-8c54-6b90c659759d | -17.26983 | -57.29988 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 34394d40-bf46-3299-9aa5-77821de31bf9 | -17.26943 | -57.28109 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b7e19acd-48fa-3a49-8631-3d2985246a62 | -17.26884 | -57.28473 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66459e6d-6651-3ecf-8001-3fa553297941 | -17.26727 | -57.27322 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e732160d-bd5c-30f1-a75d-2601defa47b6 | -17.26708 | -57.29566 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a29826bb-bbc9-3d50-b7d6-cb227c6951b5 | -17.26705 | -57.23199 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 29958135-0a3d-32e0-b805-52b974a2c6a1 | -17.26668 | -57.27686 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d53888d4-e419-3fae-81b2-24021f822b51 | -17.26649 | -57.2993 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1363f4ff-b043-373d-922a-75aaf3f30713 | -17.2653 | -57.24291 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2079548a-3c7c-3107-aa41-9493d7034ac4 | -17.26529 | -57.23164 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8cc0f0d5-7514-3592-ada2-3a6459232ba0 | -17.26471 | -57.23528 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4e9b8272-b415-373e-b43c-ef5051c2ae87 | -17.26413 | -57.23892 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |


[Clique aqui para ver as próximas entradas](README89.md)
