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

## Dados Diários - Página 294

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7105ea25-0841-383c-a5c1-3ed5f02d21b7 | -5.88893 | -44.12626 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 18113f61-1dc8-32ed-90c4-c62745894198 | -3.16369 | -50.59583 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9e8b62dd-8f1e-31e9-89ac-e64983ebda5f | -3.30008 | -39.27184 | 2026-10-08 16:20:00 | NPP-375 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d4d8573a-1a47-31e5-9c38-b1319c9b723e | -7.34187 | -50.82793 | 2026-10-08 16:20:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2a2639b9-659e-3599-a044-4186405e7bbb | -5.74174 | -42.05553 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 6fdf0b8c-8595-384e-ad1f-4c0452ccb7a6 | -7.73799 | -45.44754 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8cc41327-533c-3f0e-b8ef-a3a277442870 | -6.37174 | -45.79626 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 48576656-a244-3a2e-9ece-9dca480b482c | -7.84891 | -45.50997 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 878c19d1-6114-322b-8ee7-075ea947ffd9 | -3.30872 | -54.06025 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b8fcc84c-1baa-3a5b-8962-916c4ecb9bd3 | -4.63323 | -50.95705 | 2026-10-08 16:20:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4191f4e6-faf4-3ae3-8e13-1fdd3c2e3578 | -6.27022 | -52.88977 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a4059a0-93ab-3824-a50a-870013db4be7 | -6.15937 | -52.6423 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 211b12d7-77c8-3cb7-a8d7-660a98d775d1 | -6.53826 | -45.37144 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0b5a2a6d-c558-30da-936b-5f8167865dc5 | -4.36411 | -40.41248 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 21fec037-e47c-3d3e-b0b0-76434a1894b3 | -6.05255 | -42.60017 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| d903d9d9-a964-33ad-9ceb-f907b0a98cbe | -7.59762 | -42.38427 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 1844f115-eb1e-3b74-b17e-407e38e1ad75 | -2.99476 | -49.21716 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5a75804a-0bd9-3ee2-9097-42408b6f9020 | -6.40978 | -51.94955 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec3befa9-f107-37e4-8364-ccf08dd30769 | -7.46724 | -42.82036 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 27171ad0-c6f5-3b76-900b-96bc319a23eb | -4.77802 | -43.34027 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 4ad3881c-6dd0-3585-b15e-69f24bb4aa4f | -8.10804 | -50.93251 | 2026-10-08 16:20:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a718b7b7-84cd-38fe-91b0-3ee68b964562 | -4.19206 | -38.73904 | 2026-10-08 16:20:00 | NPP-375 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d91bff0c-d1d9-3419-9250-ee16049da95a | -4.19541 | -38.73848 | 2026-10-08 16:20:00 | NPP-375 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 63.9 |
| deba3d1e-153d-35ec-88fc-cffac93e3eb7 | -7.25068 | -43.50815 | 2026-10-08 16:20:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| a3c77fba-ff4b-387a-b50b-8755528f1683 | -4.16606 | -41.99863 | 2026-10-08 16:20:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 153ea793-f8bb-3fa8-b107-b00c6e01fb44 | -6.97512 | -43.29778 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| aad14a91-8b79-303d-8c20-062737f30b11 | -2.07691 | -46.58126 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| ce70b221-a6cf-374f-a2d3-3d518732edfc | -7.5748 | -46.69923 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fc2ad97-1230-3d85-b14e-fe18f6e7af59 | -3.79485 | -41.6656 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 26cfc4b9-ff66-3907-b363-9a3b9c690923 | -7.19204 | -44.34476 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 35b89286-041c-3a58-93fd-53a16cf86ad1 | -7.87488 | -44.14855 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 751ecce0-23cb-361b-9a60-33ed338faf18 | -5.67451 | -46.35839 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4a9d8c85-3f84-3c49-9d2f-b2aa2c5fb5d6 | -3.07565 | -53.95058 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| dec0f5ed-a653-39ae-845d-f21a96b1f419 | -5.47167 | -41.22385 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 85deccad-dd04-3c93-9fc4-e2bbf630c421 | -4.92102 | -40.36733 | 2026-10-08 16:20:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cb2e69c6-51a1-3211-887f-935c8845fdb1 | -6.06064 | -43.91165 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3b1e44a4-263c-3a5d-a1cd-e66e97d35c89 | -6.52618 | -46.11974 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d1c30d8-3123-35f1-9ab1-cf9358660fdc | -6.95324 | -44.41261 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 911a2e36-267b-3600-941a-de096aef3c4e | -1.69869 | -50.38096 | 2026-10-08 16:20:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93a36866-fd90-326d-bca9-861878838559 | -6.69515 | -45.28239 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 67404aff-93bf-39eb-9ca8-adf2be00a0ef | -7.96064 | -47.26973 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e6ea62c-4386-3eb3-97ff-0b18b3fe7122 | -2.87671 | -45.76055 | 2026-10-08 16:20:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0534adf-e1f5-3877-b64b-b2769ac92e06 | -7.70839 | -45.45418 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4f6bc198-77b7-3d3a-a2c3-b369373982bf | -3.55558 | -44.56818 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 3b90aee2-796e-3196-bc04-a9b6f725b57b | -3.9771 | -39.54147 | 2026-10-08 16:20:00 | NPP-375 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 745e216e-e7db-3d9d-8489-acc0550da390 | -3.03449 | -41.09288 | 2026-10-08 16:20:00 | NPP-375 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3626874e-86af-34fa-adb6-ceba4a50c26d | -6.77018 | -44.1208 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 30b305cd-1895-3d77-842b-a41481ccc1ab | -6.95306 | -44.89799 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bdd65e7c-b998-3af4-9693-d9ce2e71a298 | -7.63958 | -44.37779 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 994e5ed1-b05d-3dae-ab94-7fe87d62bd57 | -3.46615 | -45.1111 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c5f68a33-958d-39e0-bb22-a31c242a9d14 | -6.39241 | -44.94351 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3da9d505-7f34-3e3a-b4fd-78214f97b012 | -8.35275 | -47.67219 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7dfb95db-3844-3bba-8d1b-7f245f6ded2e | -5.38614 | -44.18051 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d37b54ca-6bbb-3ac0-942d-3bf1abb08f93 | -6.84631 | -41.76221 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e580fed5-8965-3a3e-85d4-93119b26c3e1 | -6.20998 | -52.8695 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| aa587455-b143-3797-bd76-2ea25c090b2d | -5.77382 | -45.38858 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 55bd8790-33d6-34c9-9a90-e8a3dafe7960 | -7.03389 | -39.21199 | 2026-10-08 16:20:00 | NPP-375 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 262d0a04-a288-398b-87e2-4450d2e75977 | -5.49776 | -42.84843 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 1c3f9529-e6bc-3000-9d87-f569d33daa58 | -7.71941 | -44.72866 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| adf00391-b6b0-381d-8a8e-82cdf0a7173d | -6.60158 | -44.8433 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2a7b0b6-96cf-3c87-82af-35d325153061 | -2.05593 | -54.31149 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 1d2ab2ae-9428-3971-95ac-cb4221438375 | -7.30992 | -43.98146 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d5cfba24-1845-3c38-aecf-2b7a6178fd3f | -7.75319 | -43.8147 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 66181592-13e8-3ea5-9b00-84230116b68b | -7.03772 | -45.45731 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| be75b1e3-5c6c-3875-92f0-9859b061ab0c | -3.81272 | -44.60215 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| d197afa5-6997-37eb-9a29-cd11b776c26c | -5.48287 | -44.60201 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e0e0576-d2ba-3169-867e-1a9856ed020a | -3.79255 | -41.67345 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 26c5a388-3c18-3046-9115-fd4c6e23221b | -3.47337 | -44.30983 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3e1700a7-fd8a-3d1c-8605-62ceccc7a3b6 | -3.31086 | -53.7183 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c8117d23-ff3c-3fff-a477-f303b626fa4a | -7.51645 | -47.33285 | 2026-10-08 16:20:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f652b68-ed2b-3c42-a06c-9a328830e1af | -3.72907 | -39.53489 | 2026-10-08 16:20:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b470eec2-3046-30a7-8870-54638900bc8d | -5.43821 | -46.6333 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3c27841b-3f18-3fa7-bb82-37d79001abe5 | -5.74788 | -41.68992 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 10a298a7-1d4e-334e-a947-207c6c740a80 | -6.69982 | -47.38687 | 2026-10-08 16:20:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93fe8db0-9cbe-344a-9bf1-5b63cefa9410 | -6.40858 | -37.79286 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3dffcb85-f520-31e1-91ec-3aa657293477 | -3.85696 | -44.11991 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 3e9fad31-4563-30c5-9a56-0d23fd0a597a | -7.04588 | -44.33914 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0053fce5-3418-3b1a-85be-943378bf6553 | -6.19175 | -37.85736 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 369109af-f321-30e2-9162-5e2d04f6fa42 | -6.60132 | -37.88472 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 3cb07b38-b044-3cbf-bea6-1e7276ed83f2 | -4.96799 | -42.6885 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc831807-3c4a-370d-bdd6-4d1403e85ab8 | -5.51558 | -42.82126 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2556aaf4-b527-3f4c-aa58-29e92eff933a | -6.04584 | -44.03015 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2f49d044-e74c-3059-92f1-2336cec2f16d | -7.39877 | -45.63316 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d44f5e1e-6219-3c16-9210-c146a9f57b3a | -6.84513 | -41.75439 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 0be31bbc-b87e-39ce-8215-1de55215052e | -5.75192 | -41.71669 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| faa27142-e348-3973-aae5-6edb6bc7a012 | -3.17658 | -50.45003 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4b005b96-1ffa-389f-80fb-368514429f2a | -3.00781 | -54.10259 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ecb8d984-b626-3dfc-9f3c-5c4226c4d0bc | -5.09696 | -46.20277 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 38493eb6-b24a-318e-b12c-1a12535cde9a | -7.21223 | -44.28278 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 564dbcad-108d-3a9a-9a61-52076c856ef7 | -6.49668 | -41.83288 | 2026-10-08 16:20:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| fcdb3653-51e3-3959-b5a5-eef822bf468a | -5.05297 | -45.19991 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6d21d677-0ec6-333a-9985-fa50726bdb5e | -2.99809 | -49.21797 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3dbd55d9-4641-37cd-87ca-35665ed4ab8f | -7.96612 | -47.27203 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5676604-f67d-3aed-ad9d-4995d71dce66 | -5.21692 | -45.17275 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 482bb777-ef4d-3efc-97df-daffc42d0bd8 | -3.12484 | -42.92041 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01405256-ff0c-3ebc-8f46-c245e02e421d | -5.015 | -45.49356 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a23d9078-e829-38d5-be90-58c49a96708a | -5.55508 | -45.57233 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3663aa5-cc79-3cbc-890b-1982f78f0ea6 | -5.09046 | -46.22128 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4d8d95d1-a1f2-311e-9c51-d8131695630f | -5.54646 | -43.22273 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 06770f55-35ed-3526-8faa-d91981254df3 | -7.96495 | -47.27188 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |


[Clique aqui para ver as próximas entradas](README295.md)
