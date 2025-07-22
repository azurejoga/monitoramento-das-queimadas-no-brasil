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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fa60fde-256e-3838-ac54-a172b0391f59 | -4.4067 | -43.2885 | 2025-07-22 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5414eb1a-bf07-3d96-9792-f200db04e096 | -11.7317 | -48.1849 | 2025-07-22 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 464f4f13-a97f-35a2-9efb-087841862908 | -12.4921 | -57.7841 | 2025-07-22 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 11b16a61-e73a-3e00-b6f7-b921be49aec1 | -3.1833 | -49.4429 | 2025-07-22 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 99314523-d0eb-35e9-aecb-5d6072c7e791 | -3.1649 | -49.4435 | 2025-07-22 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 1bf2ce7e-0e38-3c29-9f76-35a5390b7c91 | -5.6946 | -43.6669 | 2025-07-22 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 917104a1-91e2-3ad3-b812-0cbd48dfa130 | -4.388 | -43.2896 | 2025-07-22 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| f93a1937-95d5-3316-95be-a5911c797e64 | -12.4921 | -57.7841 | 2025-07-22 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2ddf8edf-3c0c-3032-a561-329705a0cfd2 | -12.4923 | -57.7642 | 2025-07-22 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 877f185e-947a-3dee-a376-f7e3dbaf3d7c | -3.1648 | -49.4648 | 2025-07-22 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c51a8f0f-ef8f-33bf-afea-0bbcbf8de8dd | -8.5211 | -43.3063 | 2025-07-22 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| bfff801a-49c8-3861-bc07-9cc16afb42b3 | -3.1833 | -49.4429 | 2025-07-22 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 914701cd-0e93-3f87-b5be-a22cff697bd5 | -12.5113 | -57.7626 | 2025-07-22 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 9a416a64-8a1d-3553-9722-4a26ea1bb6a8 | -11.7317 | -48.1849 | 2025-07-22 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c543bbe0-0b0d-3e50-bfec-9cdb6e71d708 | -13.6975 | -45.6865 | 2025-07-22 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 54bd2b95-ce95-34f9-9479-79cbf59bbff0 | -8.5022 | -43.3085 | 2025-07-22 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| f66e521e-81ef-3471-a77f-1d99cf62292c | -3.1832 | -49.4642 | 2025-07-22 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 618f04df-4ba5-398c-81f1-9a22ceb042a9 | -4.3693 | -43.2907 | 2025-07-22 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 1f251390-e895-3bc6-a795-78b68ced2446 | -4.4067 | -43.2885 | 2025-07-22 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5fa29268-fca3-3b79-b56a-d9c7b5c48468 | -5.6758 | -43.6683 | 2025-07-22 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ae89d585-5084-3ae8-b7b5-484622bc303e | -12.511 | -57.7825 | 2025-07-22 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f48098b7-aca9-33c0-b183-db2c8e1d0523 | -15.9333 | -43.5166 | 2025-07-22 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bdd9374f-a8a2-3690-8211-1a8282e9d94c | -7.2587 | -60.1897 | 2025-07-22 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 85646c61-5fbd-33e0-9bfb-badf66e87ce1 | -3.1648 | -49.4648 | 2025-07-22 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cf6ad307-52bf-307a-81fd-d38675323774 | -8.5211 | -43.3063 | 2025-07-22 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a30b758f-ae53-327c-a842-4b64a106f694 | -23.1095 | -50.3955 | 2025-07-22 00:50:00 | GOES-19 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| 7f5ed0ad-097c-3af3-b9c6-235cd2216868 | -7.2587 | -60.1897 | 2025-07-22 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 41444df8-1a1b-3170-a0f7-9b837e059881 | -15.9333 | -43.5166 | 2025-07-22 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| aa1deedd-a9c9-3e30-9e6d-9b6151bc698f | -4.388 | -43.2896 | 2025-07-22 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| d077a2f7-696d-375f-a402-d2252b3badb4 | -3.1649 | -49.4435 | 2025-07-22 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e52f7c0c-5f7d-34bc-9d81-e0f57085d128 | -3.1833 | -49.4429 | 2025-07-22 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| e7025bc3-60e9-3ac0-8023-273d21626bd1 | -12.5113 | -57.7626 | 2025-07-22 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| f9a1f72f-6b01-3817-8f0e-38cc2754c90e | -3.1832 | -49.4642 | 2025-07-22 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 15d2679c-dc31-3a15-b1ae-f8bb9682359a | -5.6946 | -43.6669 | 2025-07-22 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 92d3af7a-5108-3e95-8d43-feb14668d6ec | -12.4921 | -57.7841 | 2025-07-22 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| acf572ce-2229-3902-81e0-7064a1a54550 | -12.511 | -57.7825 | 2025-07-22 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3f391d37-c977-3912-a825-60baedd47a82 | -5.6758 | -43.6683 | 2025-07-22 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a95ef036-baa6-3328-90a1-d981e42aef73 | -11.7317 | -48.1849 | 2025-07-22 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 19332e80-71a9-3767-a3e9-2ed55f6ace14 | -4.3693 | -43.2907 | 2025-07-22 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0157232c-1f3d-3d04-b32f-fc3456ea0845 | -12.4923 | -57.7642 | 2025-07-22 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 23dc2be0-6691-3066-b907-564c3f1ca87f | -15.4915 | -50.1087 | 2025-07-22 01:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fa2093d4-196e-3063-a5d9-b67a19acd79f | -12.5113 | -57.7626 | 2025-07-22 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4688bda0-8765-3bec-a3b6-a7cc0742d9b3 | -12.4923 | -57.7642 | 2025-07-22 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9c046291-a5bb-3121-852b-68223fd18add | -5.6758 | -43.6683 | 2025-07-22 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| f6172f29-da48-3595-97f3-9165a64b879d | -9.0646 | -45.052 | 2025-07-22 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a6689a3e-1002-362d-b409-5ba76d39429e | -11.7317 | -48.1849 | 2025-07-22 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 1048a7f9-63da-3851-b41a-d8a2dc1e6656 | -12.4921 | -57.7841 | 2025-07-22 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c6ab29e3-e596-3401-a80a-c39130839baf | -4.388 | -43.2896 | 2025-07-22 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 58d9ff63-1256-3c4e-bebb-dc9d30b98e11 | -5.6946 | -43.6669 | 2025-07-22 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| df3464c4-6615-317c-afaf-05cefba91653 | -8.5211 | -43.3063 | 2025-07-22 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7d9f0485-70c2-3429-800b-4b6abf1f6a97 | -3.1832 | -49.4642 | 2025-07-22 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9b049424-355c-3c67-b759-3beb9ce47feb | -4.3693 | -43.2907 | 2025-07-22 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| bf533bef-9bb9-3242-8bf5-ee3f14125a97 | -3.1833 | -49.4429 | 2025-07-22 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3452b3b1-ca90-3a19-826c-9e883af8b7c5 | -15.491 | -50.1307 | 2025-07-22 01:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| aa21e70f-a98e-38a4-842b-324f3cca9470 | -15.9333 | -43.5166 | 2025-07-22 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5d148387-0550-3d89-8319-9b90d351b6aa | -3.1832 | -49.4642 | 2025-07-22 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 15a46000-7d87-3238-a5ac-921607c88ec2 | -11.7317 | -48.1849 | 2025-07-22 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 49b2ef57-cbf2-3fda-8dc5-4b4d64bdad2e | -4.388 | -43.2896 | 2025-07-22 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 9b8e58f2-fde2-36f2-9119-0bbe344732a2 | -13.6975 | -45.6865 | 2025-07-22 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 55e8797d-9c75-316c-a9fc-5cd72f738d63 | -15.511 | -50.1057 | 2025-07-22 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 30c4f624-dc8e-3e4f-82f6-6872ad11e692 | -12.4923 | -57.7642 | 2025-07-22 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d659fbb7-e21c-3242-b0bd-1067f2729dfd | -5.6758 | -43.6683 | 2025-07-22 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 70bd1005-1228-3387-a9b4-e16d192e94cb | -5.6946 | -43.6669 | 2025-07-22 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bd5ce791-1e52-33b4-b20d-51262f3c5367 | -12.4921 | -57.7841 | 2025-07-22 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8d1e455a-3733-38a1-a9cf-7aeca2afc41b | -12.5113 | -57.7626 | 2025-07-22 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d0edf8c4-20b1-3b77-b4ec-3af37c1a8957 | -3.1833 | -49.4429 | 2025-07-22 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 04ec930e-2fc5-3e01-a429-6f7d92cff4c6 | -8.5211 | -43.3063 | 2025-07-22 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a269d4c1-2e4b-3eed-9b11-a66d7bef6cd4 | -15.491 | -50.1307 | 2025-07-22 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 904fa4f8-1f1d-336f-be13-a19a6f2903a0 | -15.4915 | -50.1087 | 2025-07-22 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 015c8535-69c8-366b-88fe-e0e5efc88b92 | -15.5106 | -50.1276 | 2025-07-22 01:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| de9bc1f6-84a7-3c07-9643-8b2938d73a0b | -4.3693 | -43.2907 | 2025-07-22 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 2678c807-8ab2-3471-9632-197ff2f72e57 | -8.5211 | -43.3063 | 2025-07-22 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ad2d1648-92a5-3cb6-a8fd-fa6ee6e46fd2 | -3.1833 | -49.4429 | 2025-07-22 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 749dcd74-c9e6-3636-8737-ad911ab64840 | -15.9333 | -43.5166 | 2025-07-22 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0af8bb42-24a8-3f1f-aca9-bf259e5d5724 | -12.4923 | -57.7642 | 2025-07-22 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9dadecf0-c419-36d2-a1f6-c46a4749328c | -13.6975 | -45.6865 | 2025-07-22 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 179509df-0dad-3a69-a678-ca4b39b3bc5d | -13.698 | -45.6634 | 2025-07-22 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| b461e8e9-a7a0-32d2-96f6-c0b8af109b07 | -11.7317 | -48.1849 | 2025-07-22 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 91fd5929-90fd-39d5-9ba6-245cd24dbc9b | -5.6946 | -43.6669 | 2025-07-22 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5cc485f3-bbab-36ce-ab5e-25f677ee1150 | -4.388 | -43.2896 | 2025-07-22 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| bd2f724c-31b6-3ff3-9232-29fd38d70c53 | -5.6758 | -43.6683 | 2025-07-22 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 9db7b6b0-9730-3218-806d-5f9e88edfc99 | -3.1832 | -49.4642 | 2025-07-22 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 0492e85d-1b1c-36a2-a811-5b0b8ae8ec66 | -5.6758 | -43.6683 | 2025-07-22 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 81cb0914-b82a-363f-a15d-784b707c2e2c | -8.5211 | -43.3063 | 2025-07-22 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2704cae8-2a95-3f93-9d1e-c51335a4c7c9 | -5.6946 | -43.6669 | 2025-07-22 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 85debd6b-9f48-392c-a087-fcd5d4a2291f | -15.9333 | -43.5166 | 2025-07-22 01:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e60e47c6-906d-30dc-959c-a7e1527e46a2 | -13.6975 | -45.6865 | 2025-07-22 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ba1bcec1-7d5c-316d-ad27-835e09c95385 | -3.1832 | -49.4642 | 2025-07-22 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| b0bda4e2-c4e9-3cb7-a333-8d191b08784d | -3.1833 | -49.4429 | 2025-07-22 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 9991d285-76d0-341b-8487-b31e7c06a4ae | -11.7317 | -48.1849 | 2025-07-22 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 49f01ae5-bb65-3739-b931-99ee3daf9d40 | -12.4923 | -57.7642 | 2025-07-22 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 68c7b6ad-bdf0-318e-8d03-38cd11a5490e | -3.1833 | -49.4429 | 2025-07-22 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| ad2bd8e1-ff34-34bb-bcc6-27000a2fce29 | -12.5113 | -57.7626 | 2025-07-22 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 835a441f-dceb-314d-8995-1b2b1b20e060 | -11.7317 | -48.1849 | 2025-07-22 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| debaf06a-132c-37a0-b67c-df6c4c59c6fe | -15.9333 | -43.5166 | 2025-07-22 01:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4b4ef4a3-3bed-3aed-93bc-3654a791ab66 | -5.6758 | -43.6683 | 2025-07-22 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 85d550c5-20cb-3d7c-b8d4-b9f963d1efff | -8.5211 | -43.3063 | 2025-07-22 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 09866da7-8759-3254-b224-951e7164e7dc | -3.1832 | -49.4642 | 2025-07-22 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 72727020-2d18-3fce-954c-183c73db8df0 | -5.6946 | -43.6669 | 2025-07-22 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6707787d-fd88-315b-b75b-36cba73b9863 | -4.388 | -43.2896 | 2025-07-22 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |


[Clique aqui para ver as próximas entradas](README4.md)
