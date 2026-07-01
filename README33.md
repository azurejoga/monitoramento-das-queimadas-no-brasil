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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3425165e-c47b-3c9f-8894-1b8e51c6886c | -8.9985 | -45.7418 | 2026-07-01 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 2eb593ce-fc3d-31d4-a57d-9737c4003314 | -8.9989 | -45.7191 | 2026-07-01 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9af18296-4433-3de5-a561-0ce4edad16a5 | -9.0175 | -45.7397 | 2026-07-01 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 19a271b4-30ee-3d2f-af8d-5209cc7120fa | -12.8359 | -44.3422 | 2026-07-01 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 0080a358-d295-3560-ab81-17b875e6ded1 | -8.9985 | -45.7418 | 2026-07-01 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 7e24eb8a-3034-352f-a4d5-cb8925c236e0 | -12.8359 | -44.3422 | 2026-07-01 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 43f8c8a3-7ef8-3166-9287-874789057ae0 | -8.9985 | -45.7418 | 2026-07-01 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| b0880e63-a726-3ecf-a50c-211ee61400bf | -8.9989 | -45.7191 | 2026-07-01 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9724cb31-c0c7-3705-8d5e-e2c808e8f7d4 | -9.0175 | -45.7397 | 2026-07-01 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 09d04539-4416-32f5-a486-2b56d421f016 | -12.8359 | -44.3422 | 2026-07-01 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 61f11b43-39c3-3a0c-adff-059e292c8287 | -8.9989 | -45.7191 | 2026-07-01 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5df4a225-787a-3745-b835-4372f3cb35fa | -8.9985 | -45.7418 | 2026-07-01 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 80dcd1cc-d2ef-3dae-8286-2136e03eef30 | -9.0175 | -45.7397 | 2026-07-01 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 1da150a8-68be-3961-8d89-18ed36187654 | -12.7751 | -44.4927 | 2026-07-01 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6b375a4c-052c-3972-a245-bf711336aa44 | -8.9985 | -45.7418 | 2026-07-01 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 40e1ef6e-67e1-353e-9c7a-32e7d2a727c1 | -12.5135 | -48.2802 | 2026-07-01 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dffe87e8-76c9-3f74-a9f2-d83b84866915 | -12.8359 | -44.3422 | 2026-07-01 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ee55685c-0a98-303d-a13d-06b915d1dd5c | -9.0175 | -45.7397 | 2026-07-01 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 13996bd0-abe5-357d-8bf6-d0379384aa6c | -8.9989 | -45.7191 | 2026-07-01 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 1003f0cd-9e90-3199-a8aa-90f3c1a63d52 | -12.8359 | -44.3422 | 2026-07-01 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 423af875-6056-3af7-9cb4-21b82d1aa6cc | -15.2897 | -57.4025 | 2026-07-01 12:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f70b7b89-266f-3e04-9022-78f7e2af3621 | -12.5135 | -48.2802 | 2026-07-01 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ee083954-9758-3aaf-91a8-f98b9fc029b9 | -17.7114 | -46.8031 | 2026-07-01 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 29e83a45-ffc3-31d2-ba47-d2eb90337e7e | -17.712 | -46.7798 | 2026-07-01 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 5b9fecef-05b3-33cf-88d8-d5c7182b2065 | -10.6598 | -54.5169 | 2026-07-01 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6a4b9de6-9fb8-3213-ab79-b0da7d21bec8 | -8.9985 | -45.7418 | 2026-07-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f1f2882d-085d-36e2-913c-368a3be5a541 | -8.9989 | -45.7191 | 2026-07-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 662a6ec9-aa8b-3e67-9424-9c936687eeb5 | -9.0175 | -45.7397 | 2026-07-01 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 4f63d769-a264-33b7-bd7b-2f523a05d2db | -8.9985 | -45.7418 | 2026-07-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2803db44-b642-3984-bad1-a53223012322 | -9.0178 | -45.7171 | 2026-07-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b724ecc7-c596-3aaa-964b-0936e6c123a7 | -10.6784 | -54.5356 | 2026-07-01 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d5debe56-0cbf-316c-8abe-4f45c1961d5a | -10.6598 | -54.5169 | 2026-07-01 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| aca16eff-b291-3d5b-b429-34990bf9dbbc | -17.712 | -46.7798 | 2026-07-01 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 118.8 |
| f5567952-b751-3cfd-8cfb-174f58ad82ed | -12.8359 | -44.3422 | 2026-07-01 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 2842ee38-8209-34d2-be16-4c29165df97c | -10.6787 | -54.5153 | 2026-07-01 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| eefb4192-0044-3855-8d6c-5ed71394df2a | -9.0175 | -45.7397 | 2026-07-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 652b0c62-575f-3d73-8bfa-1afae84e8355 | -8.9989 | -45.7191 | 2026-07-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d2963d33-d79d-3b1a-9c9a-c12b355810c6 | -12.5135 | -48.2802 | 2026-07-01 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6fb77cb9-c2d6-3214-afbf-8a078c1dda83 | -15.29 | -57.3823 | 2026-07-01 12:50:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1b5becf8-c908-326b-a57d-49e7568ef969 | -9.0178 | -45.7171 | 2026-07-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| f1d90c10-dca9-3fcb-b0c0-d00ea7bcdd81 | -12.8359 | -44.3422 | 2026-07-01 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 17589ee8-ad73-3135-abc4-4f22d7c523c4 | -15.29 | -57.3823 | 2026-07-01 13:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0c3ed3c1-d91f-367f-a67c-998d7ca64883 | -8.9985 | -45.7418 | 2026-07-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 3fcb911a-4384-3885-9187-9f71d2728c16 | -10.6787 | -54.5153 | 2026-07-01 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| d6b5c4b5-b359-3d66-85eb-1775932688cb | -9.0175 | -45.7397 | 2026-07-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5e37e53a-9741-34cf-95cb-57c45b12cd01 | -10.6598 | -54.5169 | 2026-07-01 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8b5f7ab7-a38f-38f0-9be7-de243776d256 | -15.2897 | -57.4025 | 2026-07-01 13:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 2e4a97a1-7a06-328c-83da-b42f4f39638a | -8.9989 | -45.7191 | 2026-07-01 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 7e51b4ed-449a-3ee4-8df7-80792bc6612a | -10.6784 | -54.5356 | 2026-07-01 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ed45e7e6-1900-3d1f-8608-bdccd998935d | -12.5135 | -48.2802 | 2026-07-01 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| cc07168f-2ca2-3344-918f-0b8328b07cb2 | -10.6596 | -54.5372 | 2026-07-01 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| cc38946b-9c78-3e48-94b2-587242fceec8 | -10.6598 | -54.5169 | 2026-07-01 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 52dc4815-7a2e-38ef-ba49-874b62bcef9d | -8.9985 | -45.7418 | 2026-07-01 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 9b9a448a-b51a-3fbc-8c30-7c544132f97f | -15.29 | -57.3823 | 2026-07-01 13:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 89448cd3-e769-3f88-924d-f329fc456360 | -12.5138 | -48.2581 | 2026-07-01 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 46bbcb4d-5ef9-3fc4-8cc7-687464a59631 | -12.5135 | -48.2802 | 2026-07-01 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8b002107-324d-3241-892f-68db94267a57 | -9.0178 | -45.7171 | 2026-07-01 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 4793f930-8b34-3a22-9e78-1f4b51316e65 | -9.0175 | -45.7397 | 2026-07-01 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 01ad95b8-1ab8-3299-b9b6-7cebea04ef82 | -8.7841 | -44.8315 | 2026-07-01 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| a77e4d1c-c051-37d3-bf5c-e2490664e9d1 | -10.6784 | -54.5356 | 2026-07-01 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 9c475c35-b985-3d14-bc98-f0075e47e860 | -15.2897 | -57.4025 | 2026-07-01 13:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| a7fc89a3-8b15-3248-a2f1-3a15d48bd67b | -8.9989 | -45.7191 | 2026-07-01 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| bfabc78c-5cc7-35b2-b266-fde53f2a182b | -10.6787 | -54.5153 | 2026-07-01 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| e3dfb38e-1604-377e-a3df-3fb14e4e0283 | -12.8359 | -44.3422 | 2026-07-01 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6714be8a-f1e7-38e1-9be7-93d95c6e66aa | -8.9985 | -45.7418 | 2026-07-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6e66bb48-57da-3a06-adb0-c113f061e5cd | -12.5135 | -48.2802 | 2026-07-01 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 2c858e42-0b74-3283-bf05-8c489ba01d0e | -15.2897 | -57.4025 | 2026-07-01 13:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f78a3483-1d32-30aa-aa58-b474342348ba | -9.0178 | -45.7171 | 2026-07-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 6e98ee7e-70df-3d00-b208-5c79d76c8b37 | -10.6598 | -54.5169 | 2026-07-01 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.3 |
| 383087c3-ced4-32ac-8eb9-24cf41b60b44 | -12.5138 | -48.2581 | 2026-07-01 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 35622307-cab3-33c7-906a-4c0f7aadee1d | -10.6596 | -54.5372 | 2026-07-01 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 3ff232a8-d8c0-3043-ab17-61a57cca463b | -15.29 | -57.3823 | 2026-07-01 13:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 5ac4f428-b521-39c6-b10f-ebed86a6d9a8 | -9.0175 | -45.7397 | 2026-07-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 44840921-eebc-345c-9a95-4a54e0aaa13b | -8.9989 | -45.7191 | 2026-07-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 42317c0c-892d-3149-be7e-33231d9183e5 | -10.6784 | -54.5356 | 2026-07-01 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| a4374e8d-7601-3475-9228-e6aa013764d7 | -10.6787 | -54.5153 | 2026-07-01 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 70a6b44f-f984-3707-95ac-6f5ed2d7d5f5 | -17.712 | -46.7798 | 2026-07-01 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 71c5cb55-99d4-3767-8f01-07ff5b54b43e | -12.8359 | -44.3422 | 2026-07-01 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d8fd56bd-6164-3070-a746-3475b91e3456 | -8.9989 | -45.7191 | 2026-07-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| a1dd76ec-6c2b-36d8-aa33-672aba025e8f | -12.5138 | -48.2581 | 2026-07-01 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6da1adab-30b1-3e48-9766-dfa3bb16fe2e | -10.6596 | -54.5372 | 2026-07-01 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.2 |
| b3b101d6-c403-3689-9028-5975eb6a7565 | -9.0178 | -45.7171 | 2026-07-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 7615d19c-e76f-302e-a7af-1cd1e4998207 | -15.29 | -57.3823 | 2026-07-01 13:30:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| f64d2aab-c370-3dd8-81a3-02748d0efd40 | -12.5135 | -48.2802 | 2026-07-01 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 4b14dcdf-699a-393d-aadd-320e2d73627b | -10.6784 | -54.5356 | 2026-07-01 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 3be29d24-ae0d-3ecf-a983-c3900d95f1f8 | -9.0175 | -45.7397 | 2026-07-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9769431f-dd9a-33f8-95b3-1f033319e941 | -15.2897 | -57.4025 | 2026-07-01 13:30:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| e90405ad-5aa3-3ce2-932f-a10b35186fc0 | -10.6787 | -54.5153 | 2026-07-01 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 228.8 |
| d7c6bdb4-ae4e-3017-80b1-3c85283d3aa8 | -8.9985 | -45.7418 | 2026-07-01 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3e1ec87b-8d0b-3bd9-9ff7-375611bfdfa0 | -11.4338 | -56.0509 | 2026-07-01 13:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b45e3fc1-436d-3697-8481-f851da75bc37 | -12.8359 | -44.3422 | 2026-07-01 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 631ff4f7-a155-366f-b8ea-239ca6a91ac2 | -10.6598 | -54.5169 | 2026-07-01 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 298.5 |
| 55682ac6-5b1d-3370-8b53-33583b1682e1 | -12.5138 | -48.2581 | 2026-07-01 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f8ab7dfc-d352-3dbe-b997-bf6a9bc1fef2 | -10.6787 | -54.5153 | 2026-07-01 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 229.5 |
| 3eb7b742-681f-309c-8ea7-2f01b0c0bd4b | -12.8359 | -44.3422 | 2026-07-01 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a0c2c4fc-c670-3e67-b48f-672aff26caf3 | -17.7114 | -46.8031 | 2026-07-01 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2d4a21fa-da88-3165-ae8e-6383aeef2b8c | -12.5135 | -48.2802 | 2026-07-01 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 4b78f13b-02bf-305b-a52f-45d9f5f328f6 | -15.29 | -57.3823 | 2026-07-01 13:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 26741221-9a73-35fd-b0cf-aabf2b9219eb | -8.7841 | -44.8315 | 2026-07-01 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 08c1e0bd-8402-3619-8bcd-36ce764f7359 | -10.6596 | -54.5372 | 2026-07-01 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 254.0 |


[Clique aqui para ver as próximas entradas](README34.md)
