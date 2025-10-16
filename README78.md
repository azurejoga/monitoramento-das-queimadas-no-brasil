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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fe6c3f1-3b8d-3bfd-b477-3171de03e8ec | -11.50677 | -44.07361 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a8fb8a-37e0-3e59-a9de-a2ab9505d6b6 | -10.64444 | -45.24658 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 170a9f10-fa78-354d-a244-41d1b95f7c25 | -6.33675 | -44.01315 | 2025-10-16 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4a0bb02-6ced-368a-8c46-5538e58c3fcc | -8.20641 | -43.98246 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fec1862-af2a-3559-b4aa-db412d68f2d6 | -7.07823 | -44.95461 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2540a3cd-b493-34c5-9060-493ee832e270 | -9.69277 | -44.51025 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fc55385-e9a3-31eb-a5c8-f5560a554e75 | -6.06493 | -44.3103 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba644c0f-0529-39b8-bad7-967fbda5807f | -7.9483 | -44.14855 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0fd12c5c-96b7-3288-87b1-b442ee5896db | -8.45963 | -46.18745 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57892b3f-c278-32c2-842c-9073a39a1b89 | -7.05354 | -46.6866 | 2025-10-16 05:08:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 979b8a8f-1f82-3990-a7a2-bc76ec2f779f | -8.07552 | -45.42912 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 164ef7bd-d064-3e99-8bc3-865f0b944ae4 | -8.39466 | -46.26601 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c7692efb-d09d-3a80-8c58-c7e1ca8c38e3 | -5.12418 | -50.42118 | 2025-10-16 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155d8d89-47cb-302c-8cba-41d9000336e4 | -6.79985 | -45.47239 | 2025-10-16 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c22b7eb4-6922-3788-bf17-22a64791c20d | -10.03971 | -43.83394 | 2025-10-16 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cd75b5c-317a-3a26-9795-8e0d18a08117 | -10.1702 | -47.1134 | 2025-10-16 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d76076cd-e5c8-3d5b-bdd8-7bb8079dc108 | -6.33602 | -44.01836 | 2025-10-16 05:08:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b0384fa-177c-39ea-8282-e4bcc5743a10 | -5.73301 | -48.98135 | 2025-10-16 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6576ac7-199f-3a80-a099-58d412c925c0 | -11.57717 | -44.06959 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e852685a-4b93-3d3b-99ee-48bcfe882c21 | -11.60053 | -48.55604 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ac37752-57a6-391f-866d-64809b7439ba | -7.93754 | -44.1307 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aad9f5cb-7379-3d50-99b6-22e2ffc5dd42 | -6.51631 | -42.19889 | 2025-10-16 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0d359c8-1cb3-3579-a189-bab7cb85738f | -7.96962 | -44.13464 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5742120d-9d81-3e2c-b3fb-83e344e8bcba | -6.548 | -43.91816 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3b785a2-a34c-3174-848b-2b809b356428 | -11.57697 | -48.55895 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a78728a6-3c53-3496-befd-d15222ec3fbe | -10.88814 | -47.92107 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3204ed11-7015-3869-9aa5-110cfc7b5465 | -9.16231 | -46.8714 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b711a08-15c7-381c-b279-fef5decc748a | -11.47702 | -49.8231 | 2025-10-16 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90bbe95f-e547-3ff8-8620-1ae01f703d0d | -5.69084 | -45.10244 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 466757f7-71f7-38c7-97f1-0b688cdbb909 | -9.68872 | -44.54167 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c185ab5e-f691-3e73-8afd-b0b3cf914022 | -7.00515 | -43.75171 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2a08a9a5-6c76-345b-9622-e05dc69478de | -7.96388 | -44.12809 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 983b8b8e-4c84-3e77-84d6-7d374860dd30 | -8.11888 | -55.28703 | 2025-10-16 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f168c1-9d4a-3a25-bb18-d413544b6c8d | -5.33414 | -45.03011 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93ecd4aa-67fb-31f2-b3e3-fe3a00b7f808 | -8.29431 | -43.40228 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9db53bd2-362f-302c-a7e6-20c86f254a04 | -9.68633 | -44.50925 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5278c8dd-869c-30de-8398-971cea5e41cf | -6.75493 | -44.37162 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4e5eee8-facb-3bc5-9ee5-a39005ca6a54 | -7.3538 | -43.866 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c370036a-1e79-39ab-9455-6ff6325b8551 | -6.05142 | -41.94367 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 93a8d78c-c383-353a-b9a2-79277a3edae7 | -7.40615 | -44.74613 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c802165-5577-304b-98cf-3fd0437fabe8 | -9.71074 | -44.53014 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 483ed65d-052d-3a40-84ac-0954c9c4a4d0 | -7.20418 | -45.48919 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 247884b8-406e-3c14-ad35-24341e368c87 | -11.50071 | -44.0667 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cc9f13b-d900-3c73-a8d6-7d3e25c8202f | -6.03812 | -44.32025 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ac0d9a2-02ac-3a8d-86aa-c3472bdc592c | -5.87207 | -43.88713 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d69e6379-4851-3d5a-b2bd-1536b0e729d5 | -7.35395 | -43.8552 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb7e2a21-8d31-344c-aa88-9635848126cc | -9.714 | -44.50362 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8582aef4-7220-3b59-80aa-a8263b464e5b | -8.24646 | -44.03269 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42b2883c-5756-31e1-9b06-b628f0f8934d | -6.75298 | -44.36767 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef3fb2f8-c021-3026-a8bc-e72fa876252b | -10.88013 | -48.79945 | 2025-10-16 05:08:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fcaf2855-53e7-3282-b93e-d8e73f153350 | -7.48383 | -42.75161 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b5668a0b-0389-3504-ae70-13cc6950c7d5 | -8.39655 | -46.25222 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baa73d86-f0ba-3b60-85c9-2ac2e1d4855d | -5.87095 | -43.84927 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99ec3d55-e858-3347-8715-82158d57f1a3 | -8.39043 | -46.25461 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eab79def-06a2-36f2-a72d-a78dd94e3613 | -7.16377 | -42.51891 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5457c181-fc7b-37e5-8d3a-0f9c0d5f24f5 | -10.70101 | -44.43661 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| da82b281-6089-3d12-84e8-653df55f7396 | -7.00656 | -43.7407 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 097ac83c-9a1d-3fe0-a9db-0776e16f0f1e | -10.12606 | -44.57423 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7067c221-b9ea-329f-a928-293aab21c3fd | -4.64742 | -50.92628 | 2025-10-16 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f960e6fd-f679-3fa6-9962-cbd9a41c4335 | -10.64753 | -45.23863 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 515c0e08-3aa7-34b6-a935-6d41b842b71d | -11.43607 | -44.15088 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 229eeb72-35ce-3c5a-ada7-9db01d716a96 | -7.48931 | -47.02868 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 291a97af-d088-3c83-a96d-53abaa3c9592 | -6.19253 | -44.10832 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8697d3-ca63-303a-93fd-143b143b4f9a | -5.4711 | -51.18206 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a55905-09d8-3c69-b98a-f53a26f3ae0e | -10.55397 | -58.95272 | 2025-10-16 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9dff17da-fa9b-3b84-94f5-25f9c77b877c | -7.35452 | -43.86077 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ee670f0-94cc-34ea-99dc-2fd6a4070963 | -4.64668 | -50.93122 | 2025-10-16 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a15c642-db9c-373e-a8f2-0d6923153b0c | -6.22411 | -47.04121 | 2025-10-16 05:08:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97a12cbb-93ea-366e-97c9-7d0dd22b6bc6 | -11.58392 | -44.08901 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5424e4c-9d6e-3ff6-bba2-f3715da4854e | -7.61073 | -46.47293 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c50e3cdf-eb75-3e66-90b1-8895ced02aa7 | -7.92497 | -44.12344 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f30fcc0-ff58-3b04-a17d-b8ea2c681057 | -11.58932 | -44.08342 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d37c78b2-2533-3e2f-88fe-430228a7b97c | -6.12304 | -44.28905 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b4e824-e177-39c7-8f82-c5dc15fcd385 | -8.40659 | -46.23723 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a25d7666-af59-3ee3-bd7e-a5262c657f43 | -6.32612 | -44.31989 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 457a7328-4791-3f42-872d-92faa4190da1 | -9.23056 | -48.60057 | 2025-10-16 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8b832a9-0e36-3e5f-933b-b9f79c4fbf6f | -7.94809 | -44.14856 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3f09cc20-9349-320e-b65a-1fffdc410d7c | -11.50792 | -44.07368 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1af50ae2-d0c6-3526-af4d-bfe2c42eca6d | -8.24573 | -44.03823 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa058862-aba6-39e0-873a-26989e843e08 | -5.83609 | -42.33707 | 2025-10-16 05:08:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 389be37a-06ff-3209-aaf2-7d9c320d22e3 | -5.50899 | -47.30459 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8b7f356-6158-3552-b954-ef2e68145855 | -10.61324 | -45.24213 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa1b791e-75d1-39b4-b7af-5a36404cbc05 | -11.56678 | -48.55754 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf94468-cb9d-3e4e-a9ad-096653706266 | -7.93107 | -44.12983 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4108e7f4-8a08-3e00-9a39-60253c2a2040 | -7.08008 | -44.94127 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c83f63d9-528c-3117-88e3-165c2633c4aa | -7.48431 | -42.13727 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ef1fc0ee-d094-3c84-a055-e59d0d67d2f8 | -6.33575 | -45.49775 | 2025-10-16 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9924c6c3-21f3-33ec-85a3-4a260614376b | -10.65253 | -45.24926 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc0b5369-a0da-3070-93b2-79fa293de784 | -5.50857 | -47.30754 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abaf145a-a117-30e9-a951-f378211ea3e4 | -11.59854 | -48.55273 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef4d37be-af07-3c33-bec2-d1985c1b6ea7 | -10.65696 | -45.24805 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f49e831-dc6c-3a44-ac0b-52e7f1a35b48 | -5.87643 | -42.81943 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b505cf04-5395-3258-b44e-f859e73e75a9 | -7.08029 | -44.94739 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 933ea4a7-f57e-34d0-9c18-ed0f438f17d2 | -5.8825 | -42.82572 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a96f8f37-c35d-3ef0-9e90-6eca76428123 | -4.61841 | -49.55711 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce86eb1a-6c8f-3088-9772-3a24e2b9b16f | -8.46491 | -46.19147 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7002606b-801d-3238-be67-55611ad99c43 | -8.39197 | -46.26058 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e8d3554-eb58-30b6-9fbd-b7e5794d60b4 | -5.32523 | -44.83576 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1703ee1-6fba-3d73-9527-70764a068053 | -8.18577 | -43.32578 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| af96c08f-8a8d-30fa-9c22-47389329f6a4 | -12.02968 | -47.65966 | 2025-10-16 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README79.md)
