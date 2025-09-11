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
| 27e684e4-b87c-355f-9f93-e7e3b301d76d | -19.37652 | -41.81841 | 2025-09-11 03:08:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eb8e75b7-8a6a-3b4f-ba58-d31442a97d1f | -20.35928 | -42.19745 | 2025-09-11 03:08:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 21806daa-c6f2-3d3f-a6c5-b00f88a12ef2 | -21.52167 | -43.88942 | 2025-09-11 03:08:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06d35a77-3c74-3011-9fdc-f4482d91eddb | -19.9994 | -47.6271 | 2025-09-11 03:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| bd7040b3-1577-3e96-93fa-326c8ecaac86 | -8.659 | -45.7329 | 2025-09-11 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fe3312a7-8630-3b6b-97a9-09c3263252d3 | -22.5894 | -51.8759 | 2025-09-11 03:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| c0e93049-f8d0-37e9-9dd0-99538e28659d | -8.5278 | -45.6787 | 2025-09-11 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| f282ce88-c8c0-3827-876f-e9e31134189f | -11.0393 | -45.0564 | 2025-09-11 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| aaaeadb9-46a3-314b-ae8c-5ab38af42ab4 | -11.0201 | -45.059 | 2025-09-11 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 684dbc4e-d1c6-3e4b-ad5f-afa834c05c07 | -8.7361 | -47.0904 | 2025-09-11 03:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c429da9c-a6e7-31be-855f-ddd718aa414e | -22.5888 | -51.8985 | 2025-09-11 03:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.7 |
| 0e8f60ca-27ba-3c71-ba93-7afc678cc8cc | -11.3588 | -46.4941 | 2025-09-11 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 70b46684-2f1a-3dee-a350-b633dc2242ea | -11.3584 | -46.5167 | 2025-09-11 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ee80126c-295a-3f24-a725-14cd78ac3c3e | -11.358 | -46.5393 | 2025-09-11 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 06636215-1e77-3dc8-a6cf-05b1fe3498c4 | -9.0234 | -49.762 | 2025-09-11 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 65b5b352-6048-36f4-8ac4-fca1e764ee1e | -8.5089 | -45.6807 | 2025-09-11 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f578e288-cea8-30ca-8122-961a61b66fcb | -9.0579 | -46.9688 | 2025-09-11 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 8d36b640-7e7d-3e74-ab81-930aef311b0d | -10.3885 | -50.5264 | 2025-09-11 03:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 88aa6921-8a0b-3618-b955-d4b402526761 | -15.1371 | -52.4252 | 2025-09-11 03:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 08161c79-7a32-3760-89b6-891e604e08e2 | -9.0234 | -49.762 | 2025-09-11 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 957e2839-104c-3281-8aad-c0d29639f0ff | -11.0201 | -45.059 | 2025-09-11 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 41850f7a-61af-37a4-9000-91ba374ad127 | -19.9994 | -47.6271 | 2025-09-11 03:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 209323fe-f108-36d9-9133-78aa646fd92a | -11.4652 | -43.6432 | 2025-09-11 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4493c845-b671-3bf4-b543-56a4b0336ae2 | -8.659 | -45.7329 | 2025-09-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9f939277-5ed6-32e6-8da9-89b3817e0829 | -10.8898 | -47.2494 | 2025-09-11 03:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ec88c435-ac7e-3505-9f46-619d7de2398e | -11.3584 | -46.5167 | 2025-09-11 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0ea65760-77ec-32bf-ba84-639549a04bad | -15.1367 | -52.4466 | 2025-09-11 03:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b4070023-cf54-3d02-ab00-f41462057e17 | -17.4768 | -45.0944 | 2025-09-11 03:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a82aea16-4235-358a-8e59-f23113dcab25 | -19.979 | -47.6318 | 2025-09-11 03:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 91781a6c-711f-30c6-9405-e0d810b0bb9f | -22.5888 | -51.8985 | 2025-09-11 03:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 1389fdc8-6d5e-30e7-8634-4b307293f2bd | -11.4469 | -43.5988 | 2025-09-11 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8927a23a-d5e2-3b20-8193-2882cf43ebe5 | -11.4845 | -43.6402 | 2025-09-11 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 68371635-2253-37f5-8f00-db22133dd36f | -10.3885 | -50.5264 | 2025-09-11 03:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 662dd82e-9276-3540-9e9b-ef1b1b3b0f4c | -11.484 | -43.6639 | 2025-09-11 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a24fa70b-78ef-3893-8056-e09359b47b6d | -11.4661 | -43.5959 | 2025-09-11 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ec66c518-c28a-37a8-9adb-efc6de1367cd | -8.6593 | -45.7103 | 2025-09-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 90cce95d-87b1-34ae-ba88-6b43877590b7 | -8.5278 | -45.6787 | 2025-09-11 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a673403d-0306-31b5-84d7-55d35e50eb62 | -22.5888 | -51.8985 | 2025-09-11 03:30:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| c59e5003-b6f8-3c0d-9d91-cd53a6dcc3f2 | -15.1371 | -52.4252 | 2025-09-11 03:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a6ce7489-49a7-30a8-affd-b35d8d81ed28 | -11.34 | -46.4741 | 2025-09-11 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 1f290486-f778-37fa-82e0-a0138b894143 | -15.1367 | -52.4466 | 2025-09-11 03:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f41b6302-313f-35a1-9c05-5659370beeb8 | -10.3885 | -50.5264 | 2025-09-11 03:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ab713163-77bf-3ac2-b959-35112cfcb238 | -19.9994 | -47.6271 | 2025-09-11 03:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| af2b04e2-f250-36b7-8c8c-f1d49d41de52 | -8.7361 | -47.0904 | 2025-09-11 03:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 893703d3-7475-3c4c-a333-6b8e817543b5 | -15.8703 | -54.9358 | 2025-09-11 03:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| fc985b0b-c730-3343-983e-1f1eefa3b7be | -11.4845 | -43.6402 | 2025-09-11 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 9ff12c11-8b08-3fc7-8e08-990bdd6fa0b4 | -11.484 | -43.6639 | 2025-09-11 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1b292408-1550-39d3-b25c-42a29db5ce6c | -15.8898 | -54.9333 | 2025-09-11 03:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 986b0b13-84ae-3787-83bc-7b4ac79ef5cd | -11.3588 | -46.4941 | 2025-09-11 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a17682db-070b-33dc-8dbe-5798e0c9e2c0 | -11.0201 | -45.059 | 2025-09-11 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9b65d4b4-8c11-3426-86b0-550ba9893a77 | -11.3584 | -46.5167 | 2025-09-11 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 48d08e61-6910-3adb-903b-9c54d55fddb1 | -19.9994 | -47.6271 | 2025-09-11 03:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 62.2 |
| a21df2ba-1850-32be-91b3-d7e142aaeea2 | -22.5888 | -51.8985 | 2025-09-11 03:40:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| d722eb97-be62-36b4-a8c0-94c6e611594a | -15.8703 | -54.9358 | 2025-09-11 03:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 7c8ed76d-ebad-3964-ac62-2e6e4c89aa1f | -15.8707 | -54.9149 | 2025-09-11 03:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ff52495a-39e3-3a13-9171-186bdbc1ac62 | -11.3584 | -46.5167 | 2025-09-11 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 51fbb2a7-0fd7-305d-9ba9-7af2725681c5 | -11.358 | -46.5393 | 2025-09-11 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 505b8716-8ad9-3225-b269-57dee3291733 | -15.1367 | -52.4466 | 2025-09-11 03:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e9387b18-79e4-37c0-aec2-7cf53a884144 | -15.7676 | -49.9555 | 2025-09-11 03:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0090a52a-9659-3b0d-bf44-532982c0371c | -11.7319 | -50.6373 | 2025-09-11 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 48aa0019-5eed-3708-b5c4-622c64d750b1 | -15.8898 | -54.9333 | 2025-09-11 03:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9da7da98-3d35-3b58-bff9-3ec7bc3e6545 | -15.748 | -49.9586 | 2025-09-11 03:40:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b79b3992-c05a-36f6-b163-567c868dbed3 | -19.979 | -47.6318 | 2025-09-11 03:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 66c1963a-8fd7-3222-a4af-9359870d394c | -19.2415 | -48.0033 | 2025-09-11 03:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 29fb28e4-5ce6-3cdb-b485-e3ee2e32f7b2 | -22.5888 | -51.8985 | 2025-09-11 03:50:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| 781f081e-4530-38de-9806-06f4db003927 | -19.9994 | -47.6271 | 2025-09-11 03:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 22906e18-d4cf-310b-b9f2-3f77f5f5de15 | -11.7129 | -50.6394 | 2025-09-11 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a3376ea8-ba16-3ccf-b400-0f2cb7eb6c53 | -11.7319 | -50.6373 | 2025-09-11 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 1b82c47b-3466-3006-964c-dfa7dbb33347 | -15.8898 | -54.9333 | 2025-09-11 03:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a984529d-4611-3914-9710-2c5c20acad6c | -15.8703 | -54.9358 | 2025-09-11 03:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6ce5a115-d0f9-3ac0-b94d-dbfb299665ce | -4.21928 | -46.36006 | 2025-09-11 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 86dde26e-aa8e-31be-8a93-de5c914acd4f | -5.28716 | -44.19755 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37447010-a448-3ce7-a120-2a1b08241369 | -2.07323 | -47.14675 | 2025-09-11 03:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8d75730-98da-3b21-8788-833d9169ea2e | -5.53207 | -44.34927 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f6422c84-2cab-39f1-9906-3cd04296e051 | -5.53453 | -44.34867 | 2025-09-11 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3000ae62-f833-36b9-bb9f-76c36392d249 | -5.22886 | -46.0924 | 2025-09-11 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c224526-b679-33d5-ae34-4c3de9edad2c | -5.28221 | -44.2009 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bfea213-b440-3dc5-957b-95b4716fe1d0 | -5.47278 | -43.43113 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b2f44b0-3237-3b72-85fa-8880ed86cf13 | -3.64977 | -48.32668 | 2025-09-11 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 78db246c-f771-3d6e-bc8b-b8a1ce7139b4 | -6.9899 | -35.15031 | 2025-09-11 03:53:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 89057a81-219e-38ba-8c5e-2a6367a93863 | -5.34823 | -42.62951 | 2025-09-11 03:53:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8731efba-f14f-34c6-b781-0321ca2e02f0 | -5.35951 | -43.409 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ae0d659-5d2a-3957-972f-52351107814a | -5.65345 | -43.90186 | 2025-09-11 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 894648f3-bece-34f7-96ed-37f0a5a1b2b1 | -5.42903 | -43.41642 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afb07a98-fa25-39c0-8e25-93c07465ed04 | -4.50197 | -40.85702 | 2025-09-11 03:53:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eace6158-096b-3518-a177-dbcd716e3c3b | -5.73462 | -43.09575 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 6bea3d9a-4ca8-3320-ab14-8803a5afa350 | -5.20434 | -45.72332 | 2025-09-11 03:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1f06e40-853e-3128-9b39-6510b47b9588 | -5.08784 | -44.25044 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2533e0e9-4333-328d-9523-364f2cba0094 | -4.94092 | -42.78272 | 2025-09-11 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5c220fa-9b17-34d2-a19a-e649f1601afb | -4.86303 | -42.76683 | 2025-09-11 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3c8eb235-a49d-3b04-a226-1d4e5082ff11 | -4.72916 | -44.45325 | 2025-09-11 03:53:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69859555-0684-3dc1-9af8-3b2d0d7ca33a | -3.45882 | -42.99579 | 2025-09-11 03:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41b46fa-e18f-35bd-b549-0c9c45d0f634 | -4.72887 | -43.53131 | 2025-09-11 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1dad405-7cff-38f3-9efa-9adbe669f681 | -4.99403 | -38.03811 | 2025-09-11 03:53:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a039f6f-110e-3712-9d5b-7bbcd30c04bf | -5.57469 | -43.44379 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41a532ce-55c5-3826-8f78-c53e827a7b63 | -5.47338 | -43.42755 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc002a28-c9f5-3f9f-8a9e-560ff20662ec | -5.57514 | -43.44479 | 2025-09-11 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d0c8dd5-9cf4-372b-a723-f6e9b8024974 | -5.54909 | -43.04979 | 2025-09-11 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bfea979-3cfb-3e74-b22a-94e997e764df | -5.22624 | -44.37646 | 2025-09-11 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a90dfa6-c9c0-3216-8d07-393dfe2e0b26 | -5.48272 | -44.11774 | 2025-09-11 03:53:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README12.md)
