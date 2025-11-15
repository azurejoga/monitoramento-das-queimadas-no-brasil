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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec23c8fe-d259-306c-86f9-a61a15f5118c | -9.45924 | -44.87022 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f47bddc1-b2d0-3149-bd82-dddf75be41a0 | -4.49335 | -44.09317 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3210f4c-04a3-3048-84aa-a279078692e2 | -3.1323 | -49.11052 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d33d3b-069d-38a2-bbe7-c4d3e2680653 | -7.10441 | -42.7346 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 58bbb926-3075-3402-8fc4-02e11d006800 | -7.3846 | -48.64635 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04891848-9ed1-36a2-811d-3ae42a3d8744 | -2.88179 | -51.43079 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9ba1881-f4b5-3992-a95f-959742f76dac | -2.20711 | -46.54701 | 2025-11-15 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fd15af4-d384-3ac0-851a-d6b837cabcc3 | -8.6509 | -45.45697 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641c142a-eb30-30b6-b322-507c6894613e | -7.31894 | -42.86469 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 488471f1-b810-3f8f-a8fd-869c00f2d139 | -5.09118 | -47.7047 | 2025-11-15 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b963e91-48ff-3714-9cd8-172cd3e1b4c4 | -4.90372 | -44.04625 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dd095c2-926a-3bb3-83e4-6c0d79a6a44a | -5.58235 | -46.78128 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86f96151-9f4e-33df-a248-080cabd2a210 | -4.18241 | -50.42051 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b81921c-a944-32f7-80d7-c8125f74341f | -4.37165 | -47.25129 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07d6d4dd-7d08-3773-919d-3716305ff72d | -6.39966 | -42.22667 | 2025-11-15 04:25:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54cd2dbe-4052-3cb2-a2e5-6bd1573a9f29 | -4.21159 | -49.13173 | 2025-11-15 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a2162b-022b-3db1-9806-5b2626f2ccef | -3.46334 | -50.1225 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6faf417c-fbbc-395a-8bf7-0c4b1736b7bd | -8.54035 | -49.58895 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fce1ce92-6e04-3f81-bf7e-88d0f3e02e05 | -3.45592 | -50.11454 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68b5b846-b8ad-390c-ba43-33f6f4f3b74b | -3.52152 | -56.3202 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9456dd93-7254-35e1-8d89-9209dae2be39 | -4.73296 | -47.16143 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2eda8532-51d8-3290-b743-d4a9cb86c254 | -9.35232 | -46.59727 | 2025-11-15 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c334cb9f-0e28-3fb3-8944-e6e71b50bc2b | -4.88873 | -46.05507 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b108e24-0997-35bc-ac81-bd6389cda5ee | -4.53521 | -43.217 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f73faf9-a9bc-3af5-90fa-80396ed2f731 | -3.98877 | -44.27591 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 673ccc81-b97b-33e5-b274-08f3bddf4dfa | -4.41383 | -50.8269 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a71c9a-73c6-3159-ba6c-c08d185bf211 | -9.66495 | -43.90383 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45950330-a57e-35d3-8835-f513c42fd510 | -5.42247 | -43.25938 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d265e5e8-f004-3c94-9cbe-38ff43699550 | -4.35079 | -46.4901 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 720d3381-be66-3747-8830-8759d2899235 | -5.5169 | -40.97975 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b9258422-f26c-3722-a446-9abe9189c8b4 | -9.13741 | -47.76101 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f8475a7-bc2e-3e02-aba8-63a896707aaf | -5.22759 | -44.35017 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 447bef94-9cca-39c7-821e-4868a1b03e33 | -3.35605 | -52.14106 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b4b094b-c126-315e-b1c7-03b42badc6c7 | -3.99935 | -47.66613 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd2c53f8-1c88-362b-b17f-16d74e22cb0b | -9.01772 | -44.17907 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb1b78ae-b297-361a-a0a4-cd90f44d06d6 | -7.65208 | -41.30063 | 2025-11-15 04:25:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ba02dd68-ea19-3b75-95ff-a054618d5be8 | -6.07637 | -42.85755 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4eabf337-5230-3aaa-a6a8-231a76d501cc | -7.10167 | -39.07667 | 2025-11-15 04:25:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56f737f5-13d7-3b93-aa0d-d7496f515814 | -5.51164 | -44.39671 | 2025-11-15 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8784a58d-fc00-316c-8016-3ca7a03dd21e | -3.46293 | -50.12071 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5456784a-2280-3712-be01-f86a5c94a2dd | -4.16088 | -46.1444 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54e0370d-6fed-3daa-8416-c304c1256895 | -4.88401 | -49.37477 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4cd37a-8792-3d5f-8384-1b819bbe7a51 | -3.22267 | -45.4784 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 178eed0d-ce9d-3412-a084-8cb2dad18c38 | -4.19894 | -48.56211 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbf7fef7-31d2-3ed5-8610-81ba0f983344 | -7.29266 | -45.10861 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c34c3e4-834e-37ad-9f2f-3a856fcd259f | -6.03895 | -45.80583 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f71a7423-dace-31c4-b7e5-017c89f7e2b6 | -4.59274 | -49.62407 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc7d05c1-6d21-310b-a6b9-cc88b5efd54a | -7.39123 | -44.05748 | 2025-11-15 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc6e1176-8187-36f7-9e86-029d60614de4 | -6.16605 | -48.04372 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6379ebf0-07e7-312e-8449-ec9fbe8386d1 | -4.47321 | -45.65108 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5d279f4-98c0-3841-a712-87dda9bbfa1c | -5.74249 | -46.26426 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fb197f4-a56e-3aa7-8cdd-ecbda901f265 | -4.43804 | -43.65933 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca8c8363-0c5a-3e1a-8fe4-de777ff328b3 | -7.21607 | -47.97463 | 2025-11-15 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46349e7a-a68e-348a-bc9d-4da382574872 | -7.4222 | -45.23073 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a5b8f30-8750-3add-a855-bdbdf162c287 | -7.88305 | -48.40739 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cededc3-bfec-3717-a328-fada4f01fc6c | -5.13026 | -44.88491 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09e703dd-ee25-3666-82b5-94ba07d5203e | -9.7421 | -43.95354 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e43bb9-4587-31cc-aaa1-9d05a2d706c0 | -3.91197 | -40.91319 | 2025-11-15 04:25:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87a2ed54-f795-3945-87c6-f4f4d94ade35 | -4.67968 | -45.84955 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8bc1b4-2484-37de-8c34-1cbb1edd4a9a | -7.40205 | -48.34207 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccae1617-deee-393f-a064-30aaee20dc07 | -8.06441 | -43.104 | 2025-11-15 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ec84698-296a-3f8b-be88-a15a12638fb1 | -9.73912 | -43.94891 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88532ccd-829a-3ee2-a0e7-b8bf8b361a79 | -6.72043 | -42.94866 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ef5d749f-7d8a-3907-9a00-711ff346eb02 | -8.74601 | -48.31689 | 2025-11-15 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb1743c7-5ad4-3aac-9204-55568ed998bb | -7.39089 | -48.65121 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85f55e91-96a8-3cd5-9840-eb259826961c | -6.28468 | -44.7485 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43abb0a7-e012-37d0-91a2-bcbf9d2b7bf5 | -4.47236 | -42.87658 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 722bd322-6c06-31a1-846c-6044656e9fad | -5.23833 | -44.34809 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b418f560-5b62-3b0a-8aae-437ce8feb17c | -10.18163 | -44.39361 | 2025-11-15 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1988d643-ccc2-3ebd-af5b-3a72cf782e77 | -7.88025 | -48.40314 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 03dae57c-c150-3a66-aa73-b46599e63ee6 | -8.3263 | -45.40363 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b0a8e51-b7db-3d23-aa85-3b6bc6a3e96e | -5.65529 | -41.08713 | 2025-11-15 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aabe3ed4-9624-3282-b191-7603f892f2f8 | -4.42383 | -43.39614 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39c50055-0948-3702-9a5f-afbd141b21e9 | -3.52672 | -56.32527 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99f84e30-c320-3569-ae3e-419589d61c57 | -7.07868 | -46.55812 | 2025-11-15 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9008439e-adae-3e7b-bdc3-97a5ed3387fd | -5.8932 | -43.56158 | 2025-11-15 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e421a1b3-3fde-3c2f-828a-0a097a9008bb | -5.04001 | -43.61114 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 37121f4d-d82f-37f8-94ad-6dba638ca874 | -2.7095 | -46.97999 | 2025-11-15 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0220dd-d4c2-3853-9981-d77a66161ba6 | -4.1817 | -50.42227 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b77e6ff3-2a85-3cf6-8f86-d4693bd84f34 | -3.99774 | -44.26262 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19452b05-6dd6-3238-8afb-ae1d32fdc381 | -5.89046 | -42.27164 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 48caa357-14ce-3b2d-b9b4-3917209034c8 | -5.41884 | -43.25814 | 2025-11-15 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e87eef13-e84f-3893-aae8-2a75b6441f33 | -8.06809 | -43.10455 | 2025-11-15 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5331a0ca-1f89-35e2-83d4-236dd398bdfc | -6.39897 | -46.5596 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d655c51-2685-3adc-aec1-36aa868f2a60 | -4.32442 | -48.63794 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a01aa2-d94b-3405-9031-b6e2669d9e37 | -5.73653 | -42.73281 | 2025-11-15 04:25:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 53a335f4-4ad6-3aeb-9946-dfb45f9fffd3 | -4.38982 | -49.65436 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43212ab9-ca42-30d6-99cc-088b8af9620c | -5.51637 | -40.98331 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 714ab4c4-bf20-3974-9f45-cd51b6287ff8 | -3.6601 | -44.81515 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6a2fc0f7-d7e2-3ecc-a04e-8dee6b837812 | -4.53583 | -43.21307 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb3ce5ba-aba5-3813-813e-a43bc17ebfbd | -4.63137 | -45.66224 | 2025-11-15 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec870a06-6852-3578-b1a6-51eb458b5091 | -7.88485 | -48.39635 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 979f3c25-5af2-36c0-afce-dfd47042f0a4 | -4.05286 | -46.41805 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62aac00c-bcd7-336c-8c02-add6fdce8fab | -9.66303 | -43.9046 | 2025-11-15 04:25:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c9e3c46-0217-37ee-8351-cfdd7880b3af | -7.39149 | -48.64745 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eab58f2-3607-3847-98ef-d6b9d8cb61d4 | -7.49194 | -42.55268 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e6bdc6d9-3121-3e50-8ea0-f8e53c614a0b | -8.37343 | -45.05465 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20723bd9-41bb-35ea-bd6f-c5edfe29b493 | -7.35738 | -47.28655 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0d7aa47-93a3-388d-b407-6c910d91f512 | -4.42349 | -47.60378 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce1e4a2b-0ed6-3ff0-b165-234ac2a9baf3 | -3.37624 | -41.16485 | 2025-11-15 04:25:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README39.md)
