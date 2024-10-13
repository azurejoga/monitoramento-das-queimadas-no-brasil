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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 175f7e23-a772-38e4-a526-eed24965175f | -10.4905 | -49.9604 | 2024-10-13 13:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f0084a29-53f9-3fb7-b085-943d9844abef | -10.4716 | -49.9624 | 2024-10-13 13:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ac3fc1bb-8cb2-3d94-ad4b-2d46d3e17106 | -10.4908 | -49.9389 | 2024-10-13 13:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4b6103ff-2e54-325f-ab7b-ff8e6a6f6a62 | -10.9502 | -44.6762 | 2024-10-13 13:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 1cb3d33e-9ac6-3871-9f52-678963379ecb | -10.9311 | -44.6789 | 2024-10-13 13:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 475.9 |
| 74556ef5-cbb2-3ed8-b7ba-2dafff5dc0bd | -10.9506 | -44.653 | 2024-10-13 13:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 64cb0ea3-7f44-3a35-9a31-4b2960fb1b13 | -10.9315 | -44.6557 | 2024-10-13 13:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 80f6db61-31d3-3f2d-8646-8108a6fbc8e7 | -11.6949 | -42.6315 | 2024-10-13 13:16:12 | GOES-16 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| a604a883-77a1-3877-b76b-f81b3da6ac4d | -11.7365 | -44.5393 | 2024-10-13 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 63eece25-9262-3511-abad-5eed3d8b6687 | -11.7373 | -44.4926 | 2024-10-13 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a91de2f2-5bfe-307c-9362-584f70468779 | -11.633 | -48.3956 | 2024-10-13 13:16:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2db8bb83-ee03-3cfb-833e-9f36c9162733 | -12.0114 | -51.0318 | 2024-10-13 13:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| db7c804e-dda4-31ec-8d94-43b765e1f802 | -12.0737 | -50.6831 | 2024-10-13 13:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 405c4f76-3c32-3cb5-b58b-b8c3747313c9 | -12.1142 | -50.5285 | 2024-10-13 13:16:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| c72ade97-34aa-394a-a43c-bfd9caa188c2 | -13.2514 | -51.1168 | 2024-10-13 13:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ac02b1ee-42a5-3763-8c8e-3a09b5c9abe2 | -13.2517 | -51.0953 | 2024-10-13 13:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f89f2d17-3105-340a-8fb3-77d9fbf12d9d | -13.5107 | -43.492 | 2024-10-13 13:16:22 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 50e7f284-d776-3671-944d-9b8d9a4dac36 | -9.1046 | -47.7377 | 2024-10-13 13:25:58 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 6f749fc1-1522-37ae-aea3-af5965f9be6b | -9.1043 | -47.7597 | 2024-10-13 13:25:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 72a90027-8cd9-35bd-9fca-6dd2d452697e | -9.4368 | -45.4884 | 2024-10-13 13:26:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8d6c7ecb-0972-3bd4-aa30-7d6d009ca55b | -9.4554 | -45.509 | 2024-10-13 13:26:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 1641b173-f9e5-3b43-b674-d7b1beae91e9 | -9.4365 | -45.5112 | 2024-10-13 13:26:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 1fdb1a42-03ee-325e-8626-e91e212012ee | -10.0633 | -44.1692 | 2024-10-13 13:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 237.8 |
| a7cb2ed7-478d-32f0-9a34-182de99d5dcf | -10.1637 | -46.3079 | 2024-10-13 13:26:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| b1951514-4a03-3886-a7b0-92819dda6e62 | -10.1827 | -46.3056 | 2024-10-13 13:26:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c512c01d-befd-326c-ab72-7c3cbd5110b9 | -10.9311 | -44.6789 | 2024-10-13 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 425.7 |
| 5cf03728-4432-319f-b972-601e92c6f45e | -10.9315 | -44.6557 | 2024-10-13 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 280106cb-be1f-31ae-8e3d-2388a5aca25a | -10.9506 | -44.653 | 2024-10-13 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3322b528-2a7f-3e45-81e5-60ae94457bee | -10.9502 | -44.6762 | 2024-10-13 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| be24a0f8-cb35-3866-af94-16d755064601 | -11.245 | -44.1924 | 2024-10-13 13:26:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 6bcfdc99-ff7c-3fb1-a984-f7885c657250 | -11.4602 | -43.9263 | 2024-10-13 13:26:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6ef22f73-024e-3328-bdbc-4355910b9e57 | -11.7177 | -44.5188 | 2024-10-13 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2d7546f8-d12a-3ce1-8854-826d3054e0e8 | -11.7373 | -44.4926 | 2024-10-13 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 93ef9025-e546-3e60-8260-e5fe52ea08be | -11.7365 | -44.5393 | 2024-10-13 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5da51e59-5902-3b27-9fff-96a2e9b3821a | -12.0114 | -51.0318 | 2024-10-13 13:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 81db6463-e109-3590-bdf3-e7ca3d7695ca | -12.1138 | -50.55 | 2024-10-13 13:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7635eea7-dca6-3c35-bed6-ec6ac08c804e | -12.0737 | -50.6831 | 2024-10-13 13:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f12c387f-4af5-3fd9-8c1b-8cba50982299 | -12.1142 | -50.5285 | 2024-10-13 13:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e6dbc570-4e1c-39c4-9273-73f81c9229a6 | -13.3893 | -44.6705 | 2024-10-13 13:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cee3dd8f-f7f9-3a13-9245-b08300284433 | -13.2514 | -51.1168 | 2024-10-13 13:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1e0405d5-bd21-3e9c-b8fc-c61ca1494000 | -13.2517 | -51.0953 | 2024-10-13 13:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 39949587-70ab-38ff-aaf3-e4898ffe0703 | -9.4365 | -45.5112 | 2024-10-13 13:36:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 7c53777f-f202-3ec4-b607-9652fa68bd39 | -9.4554 | -45.509 | 2024-10-13 13:36:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b694f059-3543-3f86-b015-4fa072b6e951 | -9.8318 | -46.996 | 2024-10-13 13:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4676ffcd-f3b4-3cdc-af69-f1f9353db9db | -9.8898 | -48.2699 | 2024-10-13 13:36:02 | GOES-16 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ecf9831b-f3e6-3c5a-b619-8129cb4d76df | -9.7377 | -46.9621 | 2024-10-13 13:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3e5a5d04-d08e-3cf7-90f1-b89b5af165e7 | -10.0633 | -44.1692 | 2024-10-13 13:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 335.2 |
| eba77674-8a45-36ca-8122-46974c9d603f | -10.1637 | -46.3079 | 2024-10-13 13:36:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cc713df7-08c0-371a-87c2-309bcb03d969 | -10.9315 | -44.6557 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a3b4c8c6-c182-3ead-92d7-99e29296f1ba | -10.9502 | -44.6762 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| ff3510ad-7fd8-3b49-a1ae-39f8fa3393b0 | -10.9506 | -44.653 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| edcf42ff-c39f-3d80-a50e-339bd7333dbd | -10.9311 | -44.6789 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 543.8 |
| 3df26590-08db-3902-a4b1-b239abe9ea06 | -10.9116 | -44.7048 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 88922315-22f5-386d-b3eb-ccb5aff93f46 | -10.9319 | -44.6325 | 2024-10-13 13:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 81e22bdc-8ba1-3fa5-a6db-bf5e0714a9aa | -11.7177 | -44.5188 | 2024-10-13 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a8b2fbd9-d1ce-3afd-b8c6-a7a2e68a5291 | -11.7373 | -44.4926 | 2024-10-13 13:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e5974cbd-d3a2-329a-b255-e091c5f058c1 | -12.011 | -51.0531 | 2024-10-13 13:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 83edf952-be47-3d21-8a8b-95d3ca94e88d | -12.0737 | -50.6831 | 2024-10-13 13:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e289bda3-7115-30ad-88b0-6b3e5e9ed8f2 | -13.2514 | -51.1168 | 2024-10-13 13:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3dc19c53-7a74-3e5f-90e2-91f74ac938d6 | -13.2329 | -51.0763 | 2024-10-13 13:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1e7be136-f5f8-3a1d-a1c9-aefc4b6c2922 | -13.2517 | -51.0953 | 2024-10-13 13:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 95f16901-bb32-30df-821c-cccd39090952 | -8.7732 | -45.6529 | 2024-10-13 13:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 78800375-e7a6-3a8c-a99d-ffdd7b65d9e6 | -9.22 | -47.5497 | 2024-10-13 13:45:59 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 6331461a-4f6c-3d1d-9156-ddb5dc5bc41c | -9.2868 | -48.2234 | 2024-10-13 13:45:59 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 3c431321-bfa2-3a84-9bcc-77a1a9b0606d | -9.4365 | -45.5112 | 2024-10-13 13:46:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 299.9 |
| dae60db9-3d0a-3ff6-9c61-afa89523baa2 | -9.4368 | -45.4884 | 2024-10-13 13:46:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 9cc44125-7c5c-3e70-8589-fcb2f89fe782 | -9.4554 | -45.509 | 2024-10-13 13:46:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 26283dc4-159c-372a-945c-12db40d5ae21 | -9.7377 | -46.9621 | 2024-10-13 13:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4df55dd5-2704-3e9c-b0bb-c40a41ce07c8 | -9.8898 | -48.2699 | 2024-10-13 13:46:02 | GOES-16 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e682f05c-85a8-3bc3-8bc5-e36059e79440 | -10.0633 | -44.1692 | 2024-10-13 13:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 119b4f57-c9ec-32f1-9867-f248cab88456 | -10.1827 | -46.3056 | 2024-10-13 13:46:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8dd98c41-63f6-3281-87db-146cfb83be2b | -10.1637 | -46.3079 | 2024-10-13 13:46:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2a192714-7af2-3bb1-992d-fc7ae468a1d3 | -10.183 | -46.283 | 2024-10-13 13:46:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| cbd0a875-aa33-3dbf-a562-483a3456cf94 | -10.7645 | -46.751 | 2024-10-13 13:46:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 8b381fa3-b88e-3c91-ac29-ce260e02be77 | -10.9506 | -44.653 | 2024-10-13 13:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ff0ce936-6bb7-3965-a0d7-ade892cd33c5 | -10.9319 | -44.6325 | 2024-10-13 13:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9f8d7548-33ea-3ce9-8315-e796294a3ddd | -10.9311 | -44.6789 | 2024-10-13 13:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 438.6 |
| 47a1be2d-30a4-3a52-9c2e-26192b5507df | -10.9315 | -44.6557 | 2024-10-13 13:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 46a9a35c-6200-3723-92b4-36c0b8d2271c | -11.2454 | -44.169 | 2024-10-13 13:46:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e32fc31c-37b8-3795-8f29-7614c7ea1a4e | -11.2646 | -44.1662 | 2024-10-13 13:46:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c6135c64-d6c5-3597-88d9-42e3e9b2704c | -11.245 | -44.1924 | 2024-10-13 13:46:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 6e84a19b-1384-33e0-b0d6-f2856dc56498 | -11.7373 | -44.4926 | 2024-10-13 13:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1d304a6a-5c00-3d79-9fdf-de77a0488258 | -11.7177 | -44.5188 | 2024-10-13 13:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2773893c-d81d-3f3f-a772-adf8a938e71a | -12.0737 | -50.6831 | 2024-10-13 13:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 8c1abcd0-35e7-334a-9253-7ebbd15df508 | -13.2329 | -51.0763 | 2024-10-13 13:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c11cfb0d-d0e0-3a83-995d-275282434b4b | -13.2517 | -51.0953 | 2024-10-13 13:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6c9810e8-2168-3e22-91f9-d3ba289e5331 | -13.2514 | -51.1168 | 2024-10-13 13:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ab840ab7-5803-3f0a-85ef-5c161ed806e4 | -14.1007 | -44.9438 | 2024-10-13 13:46:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e39280ab-a5bb-3c20-8be7-c37b4f93081d | 2.477 | -50.8086 | 2024-10-13 13:54:52 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6d203bfc-5721-3916-9d5d-e32e52e6836e | 2.4769 | -50.8294 | 2024-10-13 13:54:52 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f044a189-51a4-3301-8ac0-1c685cccbd4d | -3.6142 | -41.513 | 2024-10-13 13:55:27 | GOES-16 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| aa704f60-08d9-3f1a-9d59-861358319abe | -9.4554 | -45.509 | 2024-10-13 13:56:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f7e5d4cd-8233-37a9-9875-08297a32d6d0 | -9.5652 | -44.4641 | 2024-10-13 13:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4c1529df-661f-339f-8ba9-27ced28d5624 | -9.4365 | -45.5112 | 2024-10-13 13:56:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 38261448-1a23-312a-8325-4389ddb44e92 | -9.738 | -46.9398 | 2024-10-13 13:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 09777559-b85f-3400-b300-c90b0d83d7af | -9.7377 | -46.9621 | 2024-10-13 13:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 26106877-bce3-3345-81ee-c167fd1c43c8 | -10.0633 | -44.1692 | 2024-10-13 13:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 519.9 |
| 8282bc15-1d87-3691-87f0-ac2cf80aa956 | -10.7645 | -46.751 | 2024-10-13 13:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 4156bd3d-2c48-3a8b-a25e-9d85bc5b4da0 | -10.9311 | -44.6789 | 2024-10-13 13:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 537.8 |
| 18f215b9-d3df-3c8a-b45c-3e690d92a4b2 | -10.9506 | -44.653 | 2024-10-13 13:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |


[Clique aqui para ver as próximas entradas](README119.md)
