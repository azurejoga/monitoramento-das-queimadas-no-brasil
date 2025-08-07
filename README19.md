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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 965638af-64c7-367b-9fc5-6a39dee31eb7 | -13.00891 | -44.88646 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45fa1141-67d6-3e5d-b581-e2d54a9b6fca | -11.73982 | -45.01905 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 542fadc0-d0a4-318c-a78c-c3ba54be4b55 | -12.28121 | -45.87684 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74a93a70-3bb3-3344-9875-9b47ccb5b025 | -11.75993 | -48.18886 | 2025-08-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| faa09bec-5ed3-3fd1-a363-f558644ed136 | -9.9332 | -60.46844 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0390f38e-7bdc-3abb-951b-eacb104c98d2 | -14.82198 | -48.40784 | 2025-08-07 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee05bc71-d086-3828-b8f1-cd87c54df251 | -9.93272 | -60.49712 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3fbaf407-d69e-33a2-92c8-d9a54bb305b2 | -9.93642 | -60.50256 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 021e4192-3ea6-3e70-97a8-e1179a9a620e | -12.71251 | -46.39825 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77bf8155-6b3d-38bf-9574-0504fcfc2f36 | -11.75294 | -44.9554 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7326707-f392-3eed-9d9a-ee475b7219c5 | -9.93604 | -60.4786 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561cf64e-d78b-3be4-b59c-f4cda079d00e | -10.64211 | -55.31686 | 2025-08-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39030d85-25a5-38f1-81df-e54862d97114 | -13.71863 | -53.85989 | 2025-08-07 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 273528ba-b7e8-37a1-8587-e3778bf83a4a | -12.55805 | -44.746 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f379b68-07b8-3bfd-b279-ffafc38ff9a6 | -12.54009 | -47.15464 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8f7ead4-ec84-3236-8ed0-4c56641890d2 | -12.71038 | -46.38671 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82f64cc7-69c4-3a88-bcab-70d1f58ac9e3 | -13.7214 | -53.86399 | 2025-08-07 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79d9892f-4fe0-3da9-9311-1fd0f9a1b550 | -9.92819 | -60.49629 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 579f54aa-31a6-3cb5-a153-947e4e123959 | -12.47145 | -49.12235 | 2025-08-07 04:53:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aa4ff5f-f77e-303b-a885-32b74605a99b | -12.73047 | -46.38387 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b5a3a5c-a61f-3f93-b52e-f0273161e64d | -11.77683 | -47.51758 | 2025-08-07 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 434ebb07-3bc0-30c5-8f57-f8a3bad0bd12 | -12.27622 | -45.87619 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51d05fc9-a934-3f99-a86d-fba3680d578f | -12.34525 | -46.06154 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96de753e-814e-3d55-878a-6186d3f3a708 | -16.71743 | -50.68755 | 2025-08-07 04:53:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 062d424a-c846-3045-ae97-701ad07fb799 | -13.00391 | -44.88242 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d008f605-ac5b-3f92-9e88-b74304d5bb35 | -13.00565 | -44.88944 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae29cc91-2151-32b1-bad6-bb8496505ef4 | -9.93355 | -60.49247 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b5b2c96-31d2-3f23-a67d-36b58926fe04 | -12.33117 | -46.05378 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 738ea2c2-4437-36af-8f9c-4f2267538e17 | -16.01607 | -47.30338 | 2025-08-07 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8b4ed36-43ae-3394-a91b-c0eb2b5ca63d | -12.64044 | -48.11278 | 2025-08-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61eb82aa-359f-3bad-af42-777162568a6a | -12.54922 | -47.15634 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c614db-757c-308a-9dc1-42820e1d3d53 | -14.82069 | -48.40866 | 2025-08-07 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e48f9f-3f90-3029-a570-265e3433db2a | -14.35524 | -51.0915 | 2025-08-07 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9663d815-8213-3dca-985e-b70431ac7693 | -12.53156 | -47.14822 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5770096b-cd04-3c02-89ab-f86c23fef245 | -13.00932 | -44.88292 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 458cb6a1-ab04-36da-98a2-49d7d73fab3a | -14.52517 | -45.60735 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 127ccbf0-014b-3af6-a763-1518e6edd93e | -11.8141 | -44.26361 | 2025-08-07 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 830e1307-8160-343f-9da9-d5531320177c | -14.52557 | -45.60406 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04753f9b-2084-3b5e-8057-c8e96151426f | -17.113 | -49.14487 | 2025-08-07 04:53:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e53203d4-ba44-300f-8901-1de7e543de88 | -14.5308 | -45.60475 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 980e5078-5030-377f-8db2-bfac7f9eb9eb | -12.72964 | -46.37901 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f8403db-31df-3b8f-b7cc-ab7e37ac661f | -13.06034 | -56.8546 | 2025-08-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b9df98-ea7e-347b-81dd-383f3aa271b6 | -12.33934 | -46.05471 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 215e9e66-e289-371d-afcb-de85229d0d08 | -12.33368 | -46.05968 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96eacdd2-c823-3a62-a3ed-73a5cebf9ec2 | -14.5313 | -45.6026 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ce2efad-9dc8-37b5-91d4-e90203e60a1d | -12.37627 | -47.04904 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a601d900-7a48-3e18-a65a-e52fa9c71595 | -12.71591 | -46.38206 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79e5ba6b-6217-38c2-b501-5eec9ff824d2 | -12.70485 | -46.39136 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5ceaeee7-3377-30b7-a5e6-ca6640c7127b | -15.74672 | -43.38812 | 2025-08-07 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8b33033e-66f8-324c-898b-f70a49878675 | -9.94012 | -60.50803 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62f6f23c-6925-3597-bc8b-1bcdd626b507 | -12.41411 | -47.78393 | 2025-08-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fc2ad89-93a9-3bf6-9436-17673f1080c3 | -12.71106 | -46.3814 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6077c65-8e62-3d86-b89c-7af453e79a0f | -9.94223 | -60.47015 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bff52c5e-bf21-3c0b-aafe-c6c35ef7833e | -13.05967 | -56.85856 | 2025-08-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9842744-c24e-38b5-9b8b-96d302728acc | -12.32876 | -46.05899 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a04de05-50f8-3004-a94f-5e29f78b919a | -9.94095 | -60.5034 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 991bea0b-266a-3bb5-8ed6-3a49f209639d | -11.45446 | -47.30914 | 2025-08-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0b6dd2f-9c27-3d06-8175-de5cb8c9f8b0 | -12.72898 | -46.38445 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc2f1c86-aa03-3c76-af5e-23f9836433c2 | -14.82122 | -48.40464 | 2025-08-07 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1b57da6-f6ce-34ef-8211-9dba4a75ab80 | -10.6427 | -55.3132 | 2025-08-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8468859-335e-3952-908e-c1be0c9638ee | -14.52644 | -45.5986 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a6be1b-4323-376d-9e17-c21a3edc0958 | -15.93274 | -43.51695 | 2025-08-07 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5581c249-1619-33c0-a903-f9b9bdd05f45 | -14.52607 | -45.60188 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a0002e4-b7a5-3fe5-9cdf-65cd59ecdfd2 | -13.0035 | -44.88597 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd68c8f7-94f9-34d0-a178-89b7dc6bbf44 | -9.94343 | -60.48953 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1498069d-2c7d-3b87-bd36-1711c805b8e0 | -12.52242 | -47.14592 | 2025-08-07 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d20bf1c3-1a9c-3ab2-b9f3-977297530162 | -9.93688 | -60.47396 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d0db680-4400-3372-b0ea-a1f507f2c295 | -12.46888 | -49.12211 | 2025-08-07 04:53:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3205aed0-1d59-3b1b-8def-a8246408ced2 | -12.34102 | -46.05518 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d161357-b0eb-3100-8ba3-d70e7d275daa | -11.90821 | -54.78207 | 2025-08-07 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d2a4d93-cdf9-3fc7-8744-6ad288edcc1b | -9.93402 | -60.46386 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a786ba7b-7663-3268-9365-48db3447ab36 | -12.72347 | -46.38918 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 531c6636-b8cb-3eb7-a84c-3b097312254f | -14.52636 | -45.5975 | 2025-08-07 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b8f3db4-72f8-3002-954a-fd55c8b9be16 | -11.89993 | -44.97649 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2aa8635-0c18-36d1-9e15-13a6eac30fc2 | -9.93891 | -60.48867 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523c6fc2-aefb-3d87-9c9b-7aa1281f874a | -9.26436 | -60.77715 | 2025-08-07 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aaa138e-9a9c-3201-b5ab-42b5ab2af01b | -13.00608 | -44.88594 | 2025-08-07 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9590bba-3b5f-3cb9-951e-8783ce8bc7cf | -11.75335 | -44.95204 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5be542fb-98ba-3948-a32a-e83659dc1ad8 | -9.92583 | -60.45755 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d130cf5b-60eb-360a-b2a5-7ba508083ee4 | -12.70552 | -46.38611 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cf41305-8f5b-3971-9156-ce51735628cf | -12.34689 | -45.7592 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f4f26b4-9048-36b8-9e01-7a3d333e9e75 | -13.05684 | -56.854 | 2025-08-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ea2c8af-0385-3a78-98bf-b95bf586a46c | -9.93035 | -60.45837 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7636ff32-34bc-3787-96be-007bb785d919 | -10.05668 | -64.99788 | 2025-08-07 04:53:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54def611-0da3-3955-bf21-bd2f8aa3dded | -11.90067 | -44.97059 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c792985-e73d-3119-9b1b-dc9621bcb454 | -11.74022 | -45.01571 | 2025-08-07 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba5972bf-1fca-3380-bf13-0c149d679a45 | -9.94389 | -60.46088 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 655f61f3-7620-368b-9042-3e856e361d99 | -13.06383 | -56.8552 | 2025-08-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b55d26e0-a845-3fbc-aa81-fe2ae2351a74 | -10.09778 | -63.19228 | 2025-08-07 04:53:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae239d12-f7ff-372f-aad3-e5bd0b5dd10d | -9.93937 | -60.46006 | 2025-08-07 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba6b172c-3cca-333a-9af5-7157cb9fabcf | -10.63932 | -55.31263 | 2025-08-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 99869183-4eb7-3477-92ac-f45f26b25efe | -12.70892 | -46.38725 | 2025-08-07 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27423f9e-07ec-33cf-b43e-2f7c18a8374c | -12.27765 | -45.86461 | 2025-08-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 677b4739-bcd8-3e64-af3d-993509fbcaa3 | -19.40497 | -48.89695 | 2025-08-07 04:55:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2011d0e6-61a3-399d-896c-56467d5f238f | -22.33974 | -47.20979 | 2025-08-07 04:55:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ac0dedf-78a1-3cdd-b736-68fed7755404 | -18.84614 | -47.0503 | 2025-08-07 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e299136-94a4-3b10-9f9d-fe525ed44075 | -20.47869 | -53.67665 | 2025-08-07 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e27abd-0531-359e-b9ba-32dcfa8e3ff3 | -22.34089 | -47.20853 | 2025-08-07 04:55:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93141652-1a5c-3548-aa4b-17e202a59e22 | -18.84548 | -47.05013 | 2025-08-07 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d12de6bc-0834-36b2-b5db-f452495c92ce | -21.11327 | -47.04222 | 2025-08-07 04:55:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
