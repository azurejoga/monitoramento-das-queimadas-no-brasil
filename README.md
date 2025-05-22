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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce66e7b9-e507-3654-bc0f-ae8a6f1e3b49 | -10.3668 | -47.9757 | 2025-05-22 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e4ed5d73-c882-31b3-ac84-869a73a26ccf | -20.9606 | -56.5755 | 2025-05-22 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 95fb019d-c900-37b1-9818-c656bbee7b34 | -7.0695 | -44.9335 | 2025-05-22 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 51704fed-da5a-32a1-9284-93acaa7db416 | -13.5256 | -43.7036 | 2025-05-22 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| ee076e41-6881-32b0-84d7-b7609bb2581a | -11.5532 | -47.4323 | 2025-05-22 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bf3066e9-7249-3dfd-98e5-904b41901adf | -11.5719 | -47.4521 | 2025-05-22 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0469739e-b073-3253-943a-2bf51553f928 | -12.3515 | -49.9833 | 2025-05-22 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| cb185292-9e67-3622-9d5d-57ae90d5c9ec | -20.9398 | -56.5998 | 2025-05-22 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a6a69b18-b814-3ce4-a261-a94b62683e32 | -7.0698 | -44.9107 | 2025-05-22 00:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b1c062ca-f54e-3067-84f8-3ce034b86ce8 | -11.5528 | -47.4546 | 2025-05-22 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 75cedf13-bd46-32cb-82b6-ab07ddbecb0f | -20.9402 | -56.5786 | 2025-05-22 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 46136b37-ec83-3a4b-8412-da9f4f0f941e | -20.9601 | -56.5967 | 2025-05-22 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 128.6 |
| eaa2db76-6054-36f6-93d2-a05ee819f8fb | -12.2943 | -52.4995 | 2025-05-22 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| ae57bca9-4629-364a-8dd2-c4ab0c1ddcab | -11.5723 | -47.4298 | 2025-05-22 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5eb53356-5429-320c-880e-0a1a111ccf18 | -10.8213 | -56.9604 | 2025-05-22 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e10e7810-e003-37cb-a09c-d395647c2723 | -13.5261 | -43.6797 | 2025-05-22 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 52bf3572-808b-3eca-91b5-e67e6dd6dfe1 | -12.2943 | -52.4995 | 2025-05-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 93ffcbdc-54b6-3a1e-a63d-e0c673c9608f | -12.3515 | -49.9833 | 2025-05-22 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| c63c85be-13c4-3e08-a9c6-6fe1e246a8f9 | -10.3668 | -47.9757 | 2025-05-22 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e137b177-96b3-3b59-a845-8aa7bbeda994 | -11.9737 | -44.1526 | 2025-05-22 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 6253f7c9-1e74-3755-b4e4-0711ff97e144 | -11.5723 | -47.4298 | 2025-05-22 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 21ce4691-b9ba-364e-b339-72774d0036f3 | -11.5719 | -47.4521 | 2025-05-22 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 35c62033-4a50-3973-95b1-5179ce2a8951 | -20.9398 | -56.5998 | 2025-05-22 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 909db939-3a49-3ccd-96c2-3a29917cd73b | -11.5532 | -47.4323 | 2025-05-22 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 33dad922-3595-392a-bf92-55b275734bca | -10.8213 | -56.9604 | 2025-05-22 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 622faf91-d590-3616-982e-2076fa3a1fa5 | -20.9606 | -56.5755 | 2025-05-22 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 142.9 |
| a262863c-8343-3973-805c-c379c0b755a7 | -20.9601 | -56.5967 | 2025-05-22 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 127.3 |
| c51ed7bd-b7ff-3c62-9469-86f1602d7e8c | -11.5528 | -47.4546 | 2025-05-22 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 891f2d13-8e4d-3ff6-901a-7b9ffbe8dbdf | -20.9402 | -56.5786 | 2025-05-22 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 169.8 |
| da2325e2-ad25-387b-9414-40a30089d327 | -12.2946 | -52.4785 | 2025-05-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 33c078f9-8017-3440-bf4d-d4087b2e4e10 | -11.9737 | -44.1526 | 2025-05-22 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| dddbf45f-e373-3b0c-832d-e71afd5e11e0 | -11.5719 | -47.4521 | 2025-05-22 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| eabf2bfd-1cd0-35b8-a2c9-117397803ba8 | -20.9398 | -56.5998 | 2025-05-22 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 148.5 |
| bfd8efc7-9f49-39f3-882c-5728d2158109 | -20.9606 | -56.5755 | 2025-05-22 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 7cba0c75-9573-37ba-8656-aec8aeceba8e | -11.5532 | -47.4323 | 2025-05-22 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9d5070f9-05e8-36b9-bf09-949eeef86770 | -11.5528 | -47.4546 | 2025-05-22 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| d7c71e30-cdf2-3e69-b6bd-279c51f1bf61 | -20.9601 | -56.5967 | 2025-05-22 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 8a6dfa21-88a8-3e6f-b908-28bb4b774d1d | -10.3668 | -47.9757 | 2025-05-22 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 67982091-1284-37af-8616-dd09c7312d9c | -16.3168 | -49.8879 | 2025-05-22 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cc02eefe-aa22-352e-81d4-ec038afd7574 | -12.3515 | -49.9833 | 2025-05-22 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 3588f413-9c8d-3ad4-bc54-0a1845f79980 | -16.3164 | -49.91 | 2025-05-22 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| d06191a4-7ecb-36dd-8cc7-c03f4fd3b749 | -12.2943 | -52.4995 | 2025-05-22 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 79d43f4b-8b9b-302c-b11b-0576ccbb04fc | -11.5723 | -47.4298 | 2025-05-22 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b3787ef3-d77d-3320-950a-757ab7b3ec0e | -20.9402 | -56.5786 | 2025-05-22 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 93fb31b1-5c9b-3c67-8743-6bc368497040 | -8.4727 | -49.597099 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06eda8cb-015e-3cd4-9690-c197040cdb18 | -12.0819 | -47.336399 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2055a570-6228-3f7c-b97a-a6bc768cb9eb | -12.3354 | -49.963402 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c88f504c-da64-3dbd-8819-55eb8d1cd4c8 | -10.3448 | -47.0126 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14b11261-2b7d-37ad-98ee-5f1e103c29d4 | -13.6926 | -45.266701 | 2025-05-22 00:28:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a653fa0-8d51-31c2-b29d-9c34f95fcd5a | -11.1129 | -54.6591 | 2025-05-22 00:28:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 214a142f-9c5c-334b-b59a-9248042745c7 | -7.4567 | -47.0602 | 2025-05-22 00:28:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 378dd4c0-b2e6-38f4-b19e-7dfed68da1cb | -6.1638 | -48.0662 | 2025-05-22 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d049b754-780b-3b56-893b-5d29c163abbd | -11.1206 | -54.6469 | 2025-05-22 00:28:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80439f6a-1f85-32bb-9f40-23ceb27294be | -10.3154 | -47.0196 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9718a7b0-e21f-3ccc-92c0-633d30efa346 | -12.3452 | -49.961201 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2a81495-884f-3428-a111-b5f23f1cac96 | -12.337 | -49.970402 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc7690e-44ed-3b20-a32f-a09dc46b969c | -10.3252 | -47.0173 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33b8e951-0ff5-38aa-9947-9a642de76aa8 | -9.9532 | -49.810501 | 2025-05-22 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d39bf093-9f2f-32f8-b146-4569c9cbbb27 | -12.2993 | -52.504902 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a367bc43-e26d-3af4-9c4f-162a5b760bf1 | -10.6529 | -49.438801 | 2025-05-22 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a542625a-ce69-3f9b-939e-5866e882724b | -10.3617 | -47.977001 | 2025-05-22 00:28:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c874830-c45c-38e7-aabe-b877f06c1a1b | -10.0963 | -47.097801 | 2025-05-22 00:28:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 007c7b43-1dfc-3d1f-b280-f4b2b165e4e6 | -11.5709 | -54.552502 | 2025-05-22 00:28:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed5ab217-efd0-3eb1-a8f1-e0a10374fdaf | -19.7313 | -54.495201 | 2025-05-22 00:28:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6445fb50-8552-3b65-8b69-582be8f3a3cb | -13.4485 | -47.534199 | 2025-05-22 00:28:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 423c0abd-8f89-3731-abc5-74613cc2b935 | -11.2876 | -53.975498 | 2025-05-22 00:28:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7c6415-d3f3-3622-bd2f-96b2f6e6e75e | -11.5597 | -47.444 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5b8972-c88f-3197-abdb-e833eecf9495 | -7.9679 | -49.6894 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9c4a85-41b1-37da-bc66-9b1a162d7e8a | -11.2993 | -53.9827 | 2025-05-22 00:28:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5cad18-79c6-3e0b-b84b-3f84eb772e64 | -16.318899 | -49.885799 | 2025-05-22 00:28:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0aa923-66f6-394e-a16c-b7e0f0db3a16 | -10.3429 | -47.004299 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b313e41-6951-351d-b7ac-973f355dc517 | -13.7835 | -54.294998 | 2025-05-22 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe1fb127-ebc7-3914-bae0-6a31196dfad5 | -10.3715 | -47.974701 | 2025-05-22 00:28:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cb0e3c7-03ae-3007-8560-d90129f93899 | -12.2942 | -52.480701 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29406cf6-8361-39ac-a9e6-3cf618c7d32a | -7.9429 | -49.761398 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbe0727-1e47-32a5-9fbc-cc5f45b9e756 | -11.5482 | -47.438599 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64256456-d3a0-3a8a-81ce-d7a5e65cf3de | -10.3698 | -47.967201 | 2025-05-22 00:28:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a112ef2-282a-3aa9-904d-e05c65b1ab40 | -12.0739 | -47.3465 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b408680-a0a1-3fb4-ba47-d7eefa3c5ed9 | -20.945499 | -56.57 | 2025-05-22 00:28:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 77da07cc-ba83-3187-91e4-f9f9a71abcd8 | -11.1227 | -54.657001 | 2025-05-22 00:28:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d53af1b4-95d6-3523-954d-00ce3228d210 | -9.963 | -49.8083 | 2025-05-22 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db539e5e-d7b2-368a-97b9-b4224457a699 | -11.7987 | -44.270901 | 2025-05-22 00:28:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68917d15-77fa-3da3-a773-cdaec09677ad | -12.8379 | -47.3922 | 2025-05-22 00:28:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2c78380-20e4-38b3-9247-e1f69aae5aee | -12.2976 | -52.496799 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6438e6f3-48e7-30c5-b9e0-40db61c08c82 | -14.0191 | -55.119499 | 2025-05-22 00:28:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d06dade5-fd88-3998-bb23-5931ec3b4a75 | -9.9615 | -49.801399 | 2025-05-22 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e22c2d1-8c8d-31a0-b751-de269e702081 | -7.4664 | -47.057899 | 2025-05-22 00:28:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 453397ed-2d09-3992-bb97-936d073e3c4c | -12.3597 | -49.98 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a70ff387-0350-3b81-ab9d-7def6fcaae82 | -17.341801 | -51.895199 | 2025-05-22 00:28:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4fc3f64-5f3a-3615-a30a-12b98b3418fc | -10.3527 | -47.001999 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca164535-a60e-33d2-8ae3-9c797a9ffd9a | -8.7352 | -47.992001 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 986af6ae-9393-3dda-bc4e-db86c850475c | -10.3462 | -47.819801 | 2025-05-22 00:28:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f070989-2cda-3364-ac34-dd9aaacb5ffe | -9.6717 | -50.950802 | 2025-05-22 00:28:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb47b761-e0bd-3380-ac94-150b798fea78 | -13.5067 | -43.6898 | 2025-05-22 00:28:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee707670-7a56-3316-b16f-d28a3368b886 | -14.0289 | -55.1175 | 2025-05-22 00:28:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f92c0f9b-5e11-3a66-a2d5-4b377d614a68 | -16.851101 | -51.394199 | 2025-05-22 00:28:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec8eeed6-cf8d-3846-b4f9-2b689896f929 | -19.117901 | -52.678101 | 2025-05-22 00:28:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dbd04962-1cf9-340b-91e3-44ece69d13c7 | -9.0359 | -47.02 | 2025-05-22 00:28:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d489d6b-8607-386d-915f-bf6441f3d57d | -23.601299 | -49.001202 | 2025-05-22 00:28:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6266363a-ab10-3fe3-ae1b-4fb0699c4f02 | -12.3041 | -52.4786 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
