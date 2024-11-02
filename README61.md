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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a0ebee-a567-32f0-9668-f775f48ca6db | -4.2303 | -48.55366 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf1ba980-123b-33c1-84d1-8bc482331a13 | -4.22511 | -48.55746 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2016722-007e-3ad7-bf0b-3b7e9e734ca9 | -4.21157 | -48.55529 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 923895b4-f6ec-306c-99a4-0afa189038c8 | -4.1049 | -48.51443 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc343b26-1b73-3a04-b7b5-5da2f5bb2655 | -4.08708 | -48.31744 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40565b33-da76-3003-9201-bf89ccd7b8c1 | -4.08247 | -48.31695 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b347b9fe-1a6e-3bee-8095-7026f0ea4737 | -4.07008 | -48.30524 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c34fb66-0fc7-3620-9250-38de01c8515e | -3.94978 | -48.36043 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 65800d77-d14b-34b4-a614-f3790125f583 | -3.94927 | -48.35897 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8d099cb3-dac9-3be9-9d19-9cd4f03c2597 | -3.94859 | -48.36351 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fd50fa85-feb3-3e4c-912c-8bb81e5c9b42 | -3.94588 | -48.35507 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d709074c-99d5-3f1b-9902-fda79c72081c | -3.94541 | -48.35362 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6d67a2d5-29e8-302f-b62a-8a7ac57211df | -3.94522 | -48.35965 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a2b42809-42b4-389f-8ec1-e3e54371be1e | -3.94472 | -48.3582 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f3f3aa74-e828-37b0-9c7b-0f7a2f5c7d54 | -3.94457 | -48.36423 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4cc8f181-26c6-3971-80cc-bdac2524f639 | -3.94404 | -48.36278 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5c803314-1757-39fa-8627-65ddea6a3f4f | -3.94224 | -48.34362 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3ad84dd3-1015-36d8-9c7c-7c78ae20483d | -3.94154 | -48.3483 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1bcd3b31-5cee-313c-a658-5aef058e230e | -3.94084 | -48.35297 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 48357c0b-1949-39dd-8f17-81e069d0fa78 | -3.94016 | -48.35755 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c80f3451-c7d4-3fe5-9208-f4040aeef31e | -3.93948 | -48.36208 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 198900da-ecc4-3e10-bd58-c929f47d8adb | -3.93697 | -48.34766 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fd9424a-310d-3cff-a6f2-fb24242e3577 | -3.93559 | -48.35688 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6510a16-65d7-3638-873a-7a0057ec1871 | -3.93102 | -48.35623 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cca8a021-9876-30d8-a26f-57a9c2016c6d | -3.91872 | -48.34485 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6c52533-04fa-3f60-883e-1e272008462e | -3.9055 | -48.37112 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b2f157d-05c6-3c1f-acde-02561ea16ae0 | -3.90094 | -48.37043 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3cbaff56-8820-3456-8577-4a5d947d4e34 | -3.89183 | -48.36905 | 2024-11-02 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e953dade-f0ed-3bc2-ba50-154d771d1265 | -4.94661 | -48.56698 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3088baa9-271c-33d6-8b65-c71f8f184eb0 | -4.94204 | -48.56637 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b1f8a50-f5a0-3f98-b88b-cb3192886427 | -4.93568 | -48.51307 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 361bb35a-5270-3f40-a4e5-2392d90605ff | -4.93109 | -48.51247 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82c1e4e7-5d75-3241-bf93-b07674dfb587 | -4.93041 | -48.51722 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f48606e4-6ae5-3e0d-a342-c0a9d669aecd | -4.9229 | -48.63456 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c1f4a396-4548-3859-98a7-eaaa119b04d5 | -4.91902 | -48.62923 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6d0c7c-a161-3cce-80fc-cb53ccd85aff | -4.91465 | -48.56213 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daaa8246-0fc5-37d6-91da-569924a7cc06 | -4.90749 | -48.54683 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dcdcedb-a1c4-3b35-81b9-ed81a070e86c | -4.90124 | -48.06865 | 2024-11-02 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b488391-0988-365a-9817-3fc7d262d321 | -4.89828 | -48.57893 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 676a4311-dc2a-37f9-a6a3-faa9b5e99d50 | -4.89794 | -48.57712 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e9b1be5-8aee-3874-a319-4d03ee2a3705 | -4.88911 | -48.64374 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6a61238-de2b-3d60-8c3b-4de5ce1b4d9e | -4.88846 | -48.64837 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cbfc433-7114-3052-9c3d-21f5e0e43988 | -4.88758 | -48.64645 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 297c17ac-4556-323f-821d-f67304a9ca38 | -4.88689 | -48.65104 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35a1ec27-cddd-3116-89ed-93f113140d08 | -4.88274 | -48.42651 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3ed0f69-3bd7-36e1-812c-8d4359440c74 | -4.88217 | -48.58919 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b137ea4c-b878-349d-bc77-4f1b79a632a2 | -4.88039 | -48.56974 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bcae014-4028-3ec5-8173-bb650b8f90a3 | -4.8797 | -48.57441 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2453ce3e-6337-398f-a619-4646cb51c7a2 | -4.87581 | -48.56915 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16c0a42c-e1c9-3564-94b4-14f4e0c3c85f | -4.87055 | -48.57322 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3a18ee2-bd46-3c64-a481-3d94d08e6bab | -4.84252 | -48.57381 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 662a2592-5ab3-305f-bb9e-9a48a1daa87f | -4.84183 | -48.57855 | 2024-11-02 05:04:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cdc809d8-f4ab-37f4-8671-72dec0af32ae | -4.78221 | -48.07969 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81980155-148b-384c-ba71-c27b0ba0a6fc | -4.73403 | -48.76623 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3f96b07-ff3f-3c37-b00e-414ef56ff78d | -4.72222 | -48.69011 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c787dcb-f232-3167-a650-afe3e2d578ff | -4.71771 | -48.68943 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff101431-23d0-3aad-a116-aa4d5a0d4dd2 | -4.35938 | -48.61023 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da49e3d7-be79-3f89-9fcf-605257f7d35b | -4.35872 | -48.61482 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0f20968-a48d-3988-9cdd-3244be13ef95 | -4.35791 | -48.6072 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5cce7ce-ab71-3e9f-8aef-3c1cd9ace448 | -4.35739 | -48.62408 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b2bf9ab-206b-39a1-8cf2-0cf07b835f3e | -4.35722 | -48.61176 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6a4ff179-2317-3789-8ea6-b7311905da32 | -4.35674 | -48.62866 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 637a7278-a522-3856-af44-075e0f8feebb | -4.35653 | -48.61639 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07b78919-88d4-30cb-b68f-b7b5f35aefbf | -4.35607 | -48.63332 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 825286fb-5a3d-3cec-884c-ce55d3f15c8b | -4.35552 | -48.60494 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1a212a79-1612-3582-baac-c0dcfb5e0747 | -4.35486 | -48.60954 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d5e06666-d7ae-3354-bf31-fa0815e88a59 | -4.35455 | -48.15546 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0942c524-0f66-37de-ac94-250eadd7725d | -4.35444 | -48.63019 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f21d232f-de45-35a4-9fa8-9151928f0ba7 | -4.3542 | -48.61416 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 75a6961d-dbe0-33dd-b181-932d669ab688 | -4.3534 | -48.60651 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9e3ddbe-d1c5-3a89-b8e1-577b7d3719cc | -4.35271 | -48.61114 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| acf52ee0-df1a-3010-a953-937386d640e8 | -4.35201 | -48.61574 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3590d05f-1e29-3245-903f-b290334a1394 | -4.351 | -48.60429 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 61b2e1df-120f-375c-8894-ab39558a09a4 | -4.35034 | -48.60894 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b50afba2-38f0-3d80-91e0-993783826cfc | -4.34991 | -48.15465 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a8c41dd-82d0-3116-b43a-b90defd7250a | -4.34968 | -48.61357 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1754c93d-6caf-39b9-a7ce-9577d4d5b6a3 | -4.34888 | -48.60591 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a98c240-37f9-38a3-92bf-5e54d98faa39 | -4.34768 | -48.72381 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bf76971-1c05-3f4d-bd3f-3dc75c0439b3 | -4.34648 | -48.60367 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90181ddd-a562-35db-8a5a-dcbbbdc76098 | -4.34505 | -48.60066 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bc3ee2b1-96d0-33e4-b78a-f51f8f2b3b1f | -4.34436 | -48.60529 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 136bb1e8-7dcd-35a4-abd2-0b83b38aaac0 | -4.33737 | -48.59031 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd0cd304-44ee-3fe6-b09f-fa72256a9ca7 | -4.33667 | -48.59498 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42e3e158-ca60-30aa-bf28-e8e902fbc622 | -4.33285 | -48.58963 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5b62740-5af7-33a7-857b-e9d691d33803 | -4.32921 | -48.64492 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07fee780-4cdd-3704-a304-f608c308b867 | -4.32854 | -48.6494 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80cebc2f-29b2-3f0a-a3ce-c4b0336acae3 | -4.32542 | -48.63953 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 860a4ce7-ccde-3343-b284-7841f2c5c69f | -4.32473 | -48.64414 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d29bf1ca-fda6-3c40-a45d-f5b90e83ddf9 | -4.32406 | -48.64866 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d27d4548-c991-3741-8a35-a959d2f28a1d | -4.32024 | -48.64336 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7857f325-d70e-3cc1-8fff-b1cab1b8cdee | -4.31957 | -48.64789 | 2024-11-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62bb21ce-a4a9-3000-91e2-c2069cf94c84 | -5.30149 | -49.12883 | 2024-11-02 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e63907e-45f6-3f16-8ce6-c95e9ed12999 | -5.23171 | -48.08414 | 2024-11-02 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 916c09d8-6c52-3a12-95d8-ed87907a7181 | -5.22769 | -48.07835 | 2024-11-02 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cb1b6ac-9b5b-3107-9139-cf327c747882 | -5.22696 | -48.08345 | 2024-11-02 05:04:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bfc581e-4b6f-3fd3-bcb7-0aee017f35dc | -5.17039 | -48.24458 | 2024-11-02 05:04:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f17d571c-b776-38d8-8f49-f98419cd3a4b | -5.1697 | -48.2495 | 2024-11-02 05:04:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 307f6616-fcfa-3978-b178-b80e0192b94e | -5.16751 | -48.24806 | 2024-11-02 05:04:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d64f25ff-458c-3a6e-9f39-ec6349a5f89d | 0.08858 | -49.86733 | 2024-11-02 05:04:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c6ec489-eee0-3866-a7c9-609c2f239745 | 0.08781 | -49.86244 | 2024-11-02 05:04:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README62.md)
