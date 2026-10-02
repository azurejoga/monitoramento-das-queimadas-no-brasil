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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9a8a5a0-f01d-3004-84b2-f5e27d8cb323 | -7.78762 | -55.63068 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5e6566f-1e16-3194-b94b-3c2d33fc71b8 | -3.40144 | -49.70458 | 2026-10-02 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e96fe33-e1c6-36ab-b2e6-85d929263d17 | -9.07831 | -44.98765 | 2026-10-02 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c5a5000e-aabe-33a7-af2e-3f9b858399bb | -5.87185 | -43.59645 | 2026-10-02 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e8f5a9a8-e03f-3ee3-ad77-d1489a9577ba | -1.08116 | -54.11025 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5865915f-5f4c-3b82-a865-d72f4eb69c3e | -8.25598 | -54.72926 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3d191b3-9131-3897-828d-7140d408f758 | -7.71535 | -54.81317 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99802c27-1d2e-3ba9-9bff-a0dc6e813993 | -3.54219 | -55.53199 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15242c65-f21e-3675-b056-17612cc7066c | -3.16839 | -54.10093 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97aa0406-8aca-3b19-8ddb-40fe530edd07 | -5.86474 | -53.47968 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e8fc440-b767-3bf3-9b44-548c1647c313 | -1.60429 | -55.12849 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfc9edbe-c732-3593-93c0-8faa5e1bb355 | -2.85427 | -54.13277 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5e950fb-7d22-3a1b-b2fb-908e762aa0eb | -4.27823 | -50.78201 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23595477-2b0b-361a-9e0c-158b3f48bb2f | -8.20536 | -54.70717 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d97fdb1-9254-3ea0-8376-79ce65cd0592 | -7.55529 | -55.03245 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 006f868e-60b2-3778-a766-c78559ea01fe | -7.83821 | -55.13816 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adab4700-c374-33dc-ba76-e7a3cc0492a4 | -4.06443 | -51.11708 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3ca004b-10bf-314d-a736-bc1c37a60865 | -5.99357 | -53.54922 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca7d859-11a0-3b4e-aea6-502f9985018d | -3.18233 | -48.68808 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53e52fc2-db0f-32b5-96aa-e3fe6c265e70 | -5.99742 | -53.54626 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d80b7ad5-c992-35e9-98d9-be391f87478b | -5.87124 | -50.15729 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 85704f0f-1c09-33fb-8cda-1558e1b6aed0 | -3.04875 | -46.9269 | 2026-10-02 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a2a6cb-95bc-3fd4-82da-464d588508d2 | -6.70054 | -56.15018 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eac1d01-57f2-3cd5-9501-c7928e0834c3 | -4.68822 | -55.79258 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a95a3f9-5c12-3217-856a-224731569261 | -4.25975 | -50.75795 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bac1ac6-efde-3a01-a9a2-cb59e5ed7177 | -4.28245 | -50.77844 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68c4954e-d189-353f-8c83-fb7892ed5e14 | -7.39812 | -55.20966 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| fe8aae45-94fc-317f-9c0a-390ab52dbe44 | -7.46004 | -55.0097 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efadedf7-19c3-3d66-b4c5-ab9eda96c69e | -4.45442 | -54.90696 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c167ceec-c440-36ca-90ca-6e43f28aa4ba | -7.48917 | -54.99654 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cd6b074-b189-3348-9129-66c53ac57464 | -7.74007 | -54.80642 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b31cc289-9514-314e-ba43-966fe9a58443 | -3.01466 | -53.89013 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75a5dd51-85ef-391d-ab3b-6bbb28c810e1 | -7.55525 | -55.01116 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c007867e-7241-3050-a930-b3a829c8616a | -6.24543 | -43.76581 | 2026-10-02 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7dcaf68f-297e-34f5-b467-ade9e76b3b2b | -6.00127 | -53.54332 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c5ea616-feec-3248-8a79-83f645acc170 | -8.08994 | -49.92793 | 2026-10-02 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbbcf0e4-8f47-3b45-bcbd-de3cf6a0a1e6 | -7.34434 | -55.2261 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fa1b1e2-c3a9-3723-af06-89d1694f0238 | -8.63682 | -47.82162 | 2026-10-02 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cd0f9ab-dc75-3769-863f-558dea38955a | -7.33608 | -55.23545 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0578c5ca-0a74-34d5-b2b1-106d78156cd7 | -6.54535 | -56.26423 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 30fa209e-c0ea-3a5d-8cdc-1b73794d49fc | -4.04008 | -54.23131 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f19fc5-b114-371e-bda6-ecb1e668cb41 | -7.69873 | -54.76807 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d213c7db-2fab-34fa-82bf-137d3083a8df | -6.19566 | -53.18546 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac86a21a-1e35-3135-9f85-cf00f2ffafe5 | -6.7513 | -55.08172 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30c4496d-bc21-3a84-96d3-77872f7d4697 | -3.61232 | -55.51293 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ea63305-1b68-3da6-a12b-a9fb3046abca | -5.91711 | -56.52239 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f3234ef-e451-3229-b833-f67122773ca0 | -7.04516 | -55.63459 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fec63deb-fe7f-372b-9ed5-bf2390914e61 | -2.43701 | -54.70617 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4f8e4f8c-3cb8-375f-8d45-4e38055ddccf | -6.26957 | -51.84304 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9331b75-2f57-3457-8d07-925b040bd8c9 | -7.18852 | -52.60857 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c856a7f-1f1c-381e-abbb-2f1d331bf8c4 | -4.29388 | -50.77592 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95fe3339-8c6c-3755-b483-5613c0bdc189 | -7.4027 | -55.59026 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf481af-9f11-339b-a6e1-5c7c37f5fcd5 | -3.10114 | -48.6717 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fdee0bb-a3b4-3b13-877a-67b903aff862 | -4.06045 | -51.09601 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39eb3faa-492f-365c-9c5c-f05168ca0969 | -6.13484 | -53.05214 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511de554-7042-33bc-bf60-7be005b9b92b | -3.13465 | -53.75478 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 190bd8cc-54be-3a31-9545-4401fc49467f | -1.62295 | -55.14261 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c56697-016e-3fae-aef2-7d218c9299d5 | -6.23393 | -53.13697 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 281aaac2-4992-30f1-ad84-09a5f055a6ff | -6.3954 | -56.40832 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83942029-0b09-355c-b159-36122cf59997 | -2.9409 | -54.18499 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0626df88-3aae-35f4-afe9-c99bfb97f462 | -6.24175 | -53.15281 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e49ef7-5841-3662-aa74-776a95a00bbe | -6.16944 | -53.3118 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c98194-2e6b-3851-afcc-2bc4874a1927 | -6.90914 | -43.67395 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 41c7d644-0ff8-39d4-98a9-7e6e5b6d70ae | -7.0485 | -55.63511 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03f77cb4-8a11-3eb0-a7b0-ee8f49e57fb1 | -2.89063 | -54.13838 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6797100d-29f8-3451-b9c9-04042f91f694 | -8.05829 | -54.83927 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c23a763e-723e-3adf-a77d-c910a98a3455 | -7.82609 | -55.12914 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ebbb24-994c-38e3-a3ed-77daa6c03f8f | -6.40939 | -56.40992 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1baa33b-d36a-3e9c-95c6-1f2b03c66f3c | -6.90738 | -43.68727 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a3cbf0e-b105-39d0-ace0-4d759a94208b | -6.19232 | -53.18497 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5a3ca18-6a85-3fdc-aec7-73b0e2f316b2 | -5.89919 | -53.49906 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7144adbb-dde4-302d-a9da-f20862d433f0 | -6.38911 | -55.24188 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc0928a9-bd92-341c-81b7-bf9ac6e2a18c | -3.07501 | -54.37291 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e603273-2009-3cfe-ad26-1738f7c6ce94 | -7.83709 | -55.12376 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 606ace78-10f0-313a-a93c-9f679d9d945d | -5.75986 | -45.13853 | 2026-10-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 866bedf2-2999-3fd4-8b2e-daf041060d33 | -3.0196 | -54.2043 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a07d831-ac3b-3e15-9bf0-c35fd84eb00b | -3.16831 | -54.0798 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 953c5705-aaac-3a20-afde-cdc6ad7abb72 | -8.23799 | -54.77963 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6839f62-ffc2-3360-a2e4-98f2ad82e5c0 | -2.87019 | -54.11759 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c8a6fe1-5b83-3662-bac4-038f8134cbfc | -3.16233 | -54.09648 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0284fbe8-bccb-3378-b267-d006d18c3a3b | -7.27377 | -55.58792 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3497e5c0-de6e-3cc0-87de-88e84984187b | -3.00584 | -53.88174 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 27bfd75e-551f-3d50-afdd-b2862cf4f545 | -8.21236 | -55.09482 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b01e5bd1-aa10-33c5-8e25-53a04d58a499 | -4.27713 | -50.76491 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc368972-8bfa-3edc-bc01-9604087ded35 | -3.42194 | -48.33609 | 2026-10-02 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eb2b470-b04a-3894-bf27-7096723d2daa | -4.30765 | -50.78228 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd3984ac-8cf9-32e6-8f92-db0e724959d9 | -5.97016 | -55.37307 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 103a7add-7ca1-3eec-ac1e-7be3b447172e | -2.95543 | -54.09194 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f883aa85-b09a-3573-9cd6-3ff6e57657b9 | -2.90149 | -54.09067 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c968705f-1923-31a6-8bb5-63548891a14b | -7.82279 | -55.12862 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90bc43f8-2979-3f09-b216-383d1ffb7901 | -3.7794 | -52.12036 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae2061d5-9b65-3bdd-80f4-bd8910002645 | -5.84764 | -53.4804 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95fe35ad-5016-3b6c-af93-49bb51b9f753 | -3.13849 | -53.75186 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3913b084-ca02-36e6-9b5b-5324bbf0c22c | -3.17446 | -54.10539 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97489dd9-bf93-382c-951f-efa34d414505 | -5.23683 | -49.58055 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf2a5793-6a47-3a3f-94d5-87687c8c2213 | -6.75075 | -55.08521 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b47491f-c54e-3745-a2be-e2626f979801 | -7.03515 | -55.63304 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66bb832b-04f2-36cf-b274-6b0c94950a19 | -8.08486 | -54.88957 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2505bf8e-1bd9-327e-b87d-ced4fc11914f | -7.83436 | -55.14112 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d03ed90f-6d71-313d-b824-e20692c95701 | -6.19396 | -53.1743 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
