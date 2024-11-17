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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca226b40-c04a-3fc6-b49b-19b3da13103b | -2.88 | -46.73 | 2024-11-17 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 53891496-9491-388a-a15f-02a0986dfe3f | -1.7823 | -48.4332 | 2024-11-17 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1cc7f9f7-4a81-313d-ba9d-30e6ea5c1f90 | 0.6159 | -51.7881 | 2024-11-17 00:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 524af6d0-11b0-32cb-809c-d7acc7e8edae | -1.8008 | -48.4328 | 2024-11-17 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 9418154d-bb79-374f-b982-06748eac3596 | -3.7744 | -46.0528 | 2024-11-17 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1e7418f4-34c9-38e6-82cd-5d90f68dab27 | -4.4866 | -48.1045 | 2024-11-17 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| baeb1c36-f591-3663-969f-db85551e51b3 | -3.5308 | -50.2757 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 603bf0d8-691b-3ee8-80f0-3a8ce07a34f3 | 0.6159 | -51.7676 | 2024-11-17 00:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 25c76ff0-90d9-3a92-959a-de227809c447 | -8.4525 | -44.1999 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 523.2 |
| 4beeea48-50a5-3e61-a983-f4672184255e | -3.5309 | -50.2547 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| b9b849f7-479f-38e6-b2b7-94a83beb0358 | -3.7745 | -46.0305 | 2024-11-17 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 3d275add-8099-38d2-b9ad-3662ce911ace | -4.4681 | -48.1054 | 2024-11-17 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 72772796-c041-321f-832f-d86fe8c6e0d0 | -3.4968 | -53.995 | 2024-11-17 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a997eec5-2225-3aa2-821d-1c7fc5924f14 | -3.5124 | -50.2553 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 287e9f06-4f83-39b4-b562-208c9c6d75e7 | -3.5678 | -50.2534 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 5f535607-69eb-34f6-80d8-2cfcee3676da | -4.656 | -44.9966 | 2024-11-17 00:20:00 | GOES-16 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7f1daca2-61a3-3399-ae11-ce47b15333d8 | -3.793 | -46.052 | 2024-11-17 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 1a5ed11e-abb3-30ca-b773-1ea9b89d3b8b | -2.5987 | -47.5705 | 2024-11-17 00:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| f8f2ba16-5755-33c1-8bf5-a78db0a97c0c | -12.4004 | -57.5127 | 2024-11-17 00:20:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b187edf1-f9a3-3c26-90e6-9b744383ed80 | -1.9166 | -46.5804 | 2024-11-17 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 421e17a7-4430-328e-8a49-4679f2a39834 | -3.531 | -50.2337 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| d335f6ef-0d47-355a-81b4-9e95883a7b28 | -2.678 | -46.2059 | 2024-11-17 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 46449ed5-cb49-3c2b-8839-4ec6e5c7cf93 | -1.8007 | -48.4543 | 2024-11-17 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6407909d-c95d-36af-945d-38aaa381bbb1 | -2.5802 | -47.571 | 2024-11-17 00:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d628b35a-d221-3e6e-982f-8d1dc2b283da | -3.5851 | -50.5255 | 2024-11-17 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 510e2e5f-8cc6-3a1c-a47b-6842167b1723 | -3.7931 | -46.0297 | 2024-11-17 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.6 |
| e92235bf-8f00-39fe-9e16-826a26e6866f | -4.5616 | -47.9925 | 2024-11-17 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| afb5b5fe-147a-3c63-8c93-b76bdd51d188 | -8.4528 | -44.1767 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 7fdb83ea-5c35-356e-8820-290c84331329 | -2.8801 | -46.7079 | 2024-11-17 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0e0f5cf8-a0d0-383e-8be1-da94520452a0 | -2.5988 | -47.5488 | 2024-11-17 00:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| d635fc82-6785-30e4-ac3e-246f57b8a00e | -8.4336 | -44.2019 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 406.8 |
| 2efdaad5-207e-38de-9977-65aba33a7226 | -4.5614 | -48.0141 | 2024-11-17 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a370bee0-0b95-3529-a944-fb682705cd65 | -2.8295 | -45.4868 | 2024-11-17 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fc24a0da-4c06-31f9-b7a6-593db352e9c7 | -2.8614 | -46.7306 | 2024-11-17 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 95262fcf-8481-3c09-919d-6a278d02f756 | -8.4339 | -44.1788 | 2024-11-17 00:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| e9757f88-c61d-36d7-a6a7-f63d4a0755a9 | -2.6231 | -46.0299 | 2024-11-17 00:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a98eed9f-cce1-3354-9a57-415bb81dd8cd | -3.4821 | -53.9944 | 2024-11-17 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c23824dd-b683-3e77-9d15-4cec216e417f | -4.3872 | -45.279701 | 2024-11-17 00:28:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa3c61a2-00c0-378b-b625-0be9a8e18e16 | -3.5176 | -49.9375 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8621ac65-e8ec-36ea-9d54-d9311dada43e | -11.177 | -44.625999 | 2024-11-17 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 914280da-496e-33e5-906f-32a9e9cb658e | -4.473 | -48.1059 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c5f310-97ef-36f8-afbd-7e2fd8b0730f | -5.4957 | -46.251598 | 2024-11-17 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3cca6cd-c461-3645-9c36-92becfc4a52f | -4.0962 | -46.1269 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e138697-9177-38f8-b90d-6651effd79b0 | -2.2784 | -47.920101 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a586f949-c794-3e87-bd76-739b07249987 | -7.5214 | -35.176998 | 2024-11-17 00:28:00 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ea5a417-0906-3e9f-a0b8-58d85aa087e5 | -3.7632 | -43.247002 | 2024-11-17 00:28:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 724e9148-fdb5-33ca-b675-9be73c732ae2 | -3.2683 | -44.1842 | 2024-11-17 00:28:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 845fcae1-a78a-339d-9222-a461b27d3b26 | -4.3009 | -42.189301 | 2024-11-17 00:28:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3096283-8192-3691-8379-944425b05fa8 | -3.6963 | -44.4291 | 2024-11-17 00:28:00 | METOP-C | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03ee5879-9b28-316b-a6e0-8e8f98263e07 | -3.9672 | -45.968498 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3765bc7-27d9-3b36-ad68-89ee176eee6a | -3.3249 | -50.496399 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20c26f9a-9196-3f37-9c04-bace677443a6 | -2.6723 | -46.214298 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 460cd3d3-85eb-3c60-8318-0fcda4a81486 | -4.4025 | -45.527 | 2024-11-17 00:28:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 671bfd78-b0d7-369a-aee0-4abb6b0908e3 | -2.6253 | -46.188999 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78bfdfb1-abe1-31d7-a61b-06e9ab5997bf | -4.7236 | -46.8456 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab5db70-79b6-3621-8201-0f9385b17b3a | -3.0894 | -45.963699 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45d1258d-c0b1-3f6d-abcb-59164bfdfe30 | -3.5287 | -50.261501 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2813b9c-3dfd-3d43-9105-d9ad691aa6c8 | -2.6224 | -48.571499 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d87f4def-7d49-3db9-a44a-03096bb8c9e5 | -3.3508 | -46.430302 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e26f9b6-2456-3493-ae3b-87ab75754751 | -2.9019 | -46.8577 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0183b081-ecee-315c-a56c-24be06620d45 | -4.5552 | -48.013901 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1025c7-63d8-3713-8ad5-fb8742adefc1 | -4.6443 | -45.006699 | 2024-11-17 00:28:00 | METOP-C | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eec7a3a8-a9dd-3a11-a5e2-35def321de4c | -2.8684 | -45.404999 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0020477-2bdd-3aa7-9d95-f5fcd4b10ef5 | -8.4361 | -44.222099 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66ed46c8-b979-3a53-a545-8fa0994ef2bf | -2.6239 | -45.193901 | 2024-11-17 00:28:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 420312f8-cc8a-3a97-a4d4-791d4779539e | -2.5278 | -45.359299 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7833dfae-c3c7-3ffe-b687-409b00ee0ad2 | -3.4782 | -53.9767 | 2024-11-17 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e17c6a-27b2-3987-957d-d3c4aa86628c | -3.1802 | -46.540798 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcaf44d3-d3e4-31b3-9bca-5856b9c689f3 | -3.0121 | -45.401501 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e699c76-46e6-306c-a7bb-69d9e0af18b9 | -2.1545 | -46.115101 | 2024-11-17 00:28:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9be066c5-18fa-3baa-9246-489680c2b3c4 | -3.8398 | -49.817402 | 2024-11-17 00:28:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94a07da4-752c-3b60-a0d7-bc72f81b8f8e | -1.8041 | -48.0098 | 2024-11-17 00:28:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2156a76-f055-3863-9373-14133f6b6c46 | -3.7168 | -46.045898 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8edc9746-eef6-30f2-a09c-557970522329 | -5.8711 | -40.146999 | 2024-11-17 00:28:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8bb6434b-69d4-3ccd-8f14-1045cfe09549 | -2.1834 | -46.646801 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f269c4d3-8322-3af2-9a4d-7f5b60316a78 | -2.4767 | -45.406601 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ddd044b-c220-3f05-97d9-befd047e49b1 | -2.68 | -46.8339 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61848f27-5b73-33ed-92b1-ab9a2e452e5f | -5.424 | -45.3484 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 639d09c0-b091-32d0-a189-77ee339d0959 | -2.1596 | -46.407501 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a045f7-470d-3104-9c84-bf245f7e1bbe | -3.91 | -46.531101 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62e5bb29-0ee7-3181-a4ba-707e8565207e | -1.9634 | -48.391602 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e87e82-e86c-3b39-a6f6-c345904472e6 | -3.2973 | -45.430801 | 2024-11-17 00:28:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc667be3-2dbb-390a-8349-6991eee72caf | -1.7984 | -48.4361 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bddea21-1832-3752-b775-80924761dfff | -7.5118 | -35.179501 | 2024-11-17 00:28:00 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f78ebe46-a5b9-3eee-9849-0b462e0b70af | -6.0901 | -41.942101 | 2024-11-17 00:28:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6dadf5e4-5319-3a44-8cea-e1180dfec881 | -8.433 | -44.208401 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99c72e1b-1bb3-332f-8ff5-ea52db0b8e34 | -4.5801 | -48.033001 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73a812bb-2977-39d0-a9a7-81070e86c952 | -4.565 | -45.110802 | 2024-11-17 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 970000a8-5629-3c23-a81a-21b2413a1a08 | -2.1943 | -49.541901 | 2024-11-17 00:28:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39e11b4-9d2f-3a44-95e3-20f642d29457 | -2.3239 | -53.561199 | 2024-11-17 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d33ac6-2602-37ce-bffd-0accb5a8e71f | -2.6204 | -46.0326 | 2024-11-17 00:28:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 958df0a3-c467-3635-a26e-b9cf928c7970 | -2.924 | -46.7286 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31b2b01e-218d-39cb-9782-115a8f3a38ac | -2.9222 | -45.414501 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e72863f-db97-3dda-9c86-3c0d7b89a978 | -2.4762 | -45.628799 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c387c5e-dae9-3c6d-ba61-4d011b7ecd67 | -3.3494 | -46.063301 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac715324-1bb4-3034-b1cf-b398bde1e094 | -5.5127 | -46.417301 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af491892-5fd4-324c-9d66-084b28bfa81d | -3.5265 | -50.251598 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9921122e-6ba2-30e5-9b5a-3b94e177d97a | -0.3116 | -48.694401 | 2024-11-17 00:28:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 333ce8b9-f855-3b6b-8658-52c54c0c1bef | -4.3692 | -43.012901 | 2024-11-17 00:28:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b7304e6-9cd1-3121-b281-30aa7035ba77 | -3.7689 | -46.048698 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
