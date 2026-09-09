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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31131b0-e7ad-3262-b7f8-f4f6eacc44fb | -3.54483 | -48.1819 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e6d8954-1120-3445-bcae-86a282a6de7f | -3.86859 | -47.10039 | 2026-09-09 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c79889-513a-3334-8056-85e90ec5a9da | -1.66908 | -55.66519 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6dacb917-e34a-3d3f-b020-3eb6defe7a0d | -2.72932 | -51.82701 | 2026-09-09 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b31d2a9-e9ac-33b5-9617-06952ebcb3c2 | -5.67384 | -50.09843 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2464da44-483d-3ce7-8af0-febc97c3127c | -6.16212 | -44.64927 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 40863961-49cf-3a9e-9032-f60249c7b8b9 | -3.67774 | -58.52616 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15cfbe05-d18a-3e68-bde4-42a59a709041 | -3.76264 | -50.453 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8f2ff81-31d0-3192-9b67-4552f86a7aa9 | -1.61921 | -55.13757 | 2026-09-09 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 810da4d7-7ad0-37e8-8ee5-79101f5d9382 | -2.83481 | -49.51308 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76350f8-d24b-3fcd-9dca-89f819d1d90f | -5.42356 | -41.84037 | 2026-09-09 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 006457f7-cf4c-31e4-b53b-1c257927a351 | -3.5487 | -48.17894 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 556ab8c8-37e6-3b36-aaf1-aae1b4a339b5 | -3.43354 | -59.25797 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 594da22b-82a5-3f79-9494-55c0c79178fe | -2.11962 | -54.38723 | 2026-09-09 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e2357db-d31e-376e-ab0b-ed5204c2bc7f | -1.96933 | -56.7812 | 2026-09-09 04:44:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c3ae047-f37e-300e-bc97-1263e0a3b417 | -4.3782 | -55.04073 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25386ecb-9504-3f1c-b404-89e6c3792827 | -3.24605 | -47.25122 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26155f3f-998d-3a66-86a8-19daa0b3a8bf | -1.03755 | -53.7311 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6398adc0-1133-3757-99cd-33fa96cd0d23 | -2.94674 | -50.47274 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97d86259-7f88-3efd-918c-bbf5fa751407 | -2.93939 | -50.47529 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe2be203-6226-3a83-b3eb-df653a50cb09 | -5.75045 | -50.19267 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33aa0843-f528-3a78-adb9-66c9a8aa801e | -3.82569 | -59.40603 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34b899e5-10df-3ee7-bea0-e572e71f8468 | -3.95739 | -59.36781 | 2026-09-09 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d5c917-a7a4-35d0-86d7-7a57f94130e4 | -3.37513 | -59.42556 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21079a93-4aba-347d-8083-3414ccd2fd66 | -6.25689 | -47.34827 | 2026-09-09 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3691604-d5f0-3597-8640-5dffc8029d8b | -6.16107 | -44.65623 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7eb70a4-0cee-33cf-9bec-6aac075aaecc | -5.40766 | -49.18449 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dde36807-dcbf-3cc7-8c36-ba075df1ce71 | -4.43789 | -54.83721 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861d8212-1d68-3cdc-b891-6afcf598428f | -2.60682 | -51.2151 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a602b36b-c143-3da1-9336-944986a70a35 | -3.36869 | -59.4263 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b62e15ae-3f41-3cd0-bcd6-08a1634cf990 | -3.54815 | -48.18243 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed652feb-b41a-3a96-8eb4-761f89663d88 | -3.35492 | -59.43906 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d50227ad-7583-338a-8947-e16886777489 | -3.8127 | -55.89159 | 2026-09-09 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0514c367-7df5-38c2-9cf7-641cbd33f551 | -5.71506 | -46.19043 | 2026-09-09 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf45aeb-0619-36cf-8be9-e6d2625b7bc0 | -5.76673 | -45.06624 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bca8fa8-e002-3be7-8079-74017de22ab2 | -3.5415 | -48.18139 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905d623a-a16b-3174-91fe-9ff793712d9a | -3.72193 | -45.27765 | 2026-09-09 04:44:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec2cbaf1-841e-3a31-8f2a-673cd4d473e1 | -3.24719 | -47.24395 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82a30bf-c650-3604-af4e-33ed2456e14a | -2.94558 | -50.47999 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d7068417-0ccf-36ad-98f7-9943ef36b587 | -4.43912 | -54.82977 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e1a07ff-a8c9-311c-adee-77d8608d7956 | -4.37688 | -55.04868 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c2c8378-5662-3676-9eb4-9d29a997555f | -3.37445 | -59.42968 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd576cae-5d55-3132-b9c3-6ca836850806 | -3.77048 | -58.84838 | 2026-09-09 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fb2ea8b-d0aa-3c1e-abf3-13dde234e90b | -4.00387 | -51.03178 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 672f2094-1af1-3881-b44c-c8a2595f272b | -6.75856 | -44.58159 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0b7603-4b38-35b5-8c31-189c1be22ead | -6.83324 | -39.41152 | 2026-09-09 04:44:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19b960e9-1e1c-3fda-941e-1b39554350dc | -3.72368 | -45.27631 | 2026-09-09 04:44:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3243789e-e492-3acc-bbdd-49149ee1b19d | -5.60758 | -44.84672 | 2026-09-09 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d0f611ea-8aad-333c-8429-e68b60b303c4 | -3.54925 | -48.17546 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2606b3b-06a9-3756-b6d1-0d647742dbe6 | -6.1616 | -44.65274 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fce21252-8e1a-35ae-98b8-00f344cfad14 | -3.55148 | -48.18295 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69aff184-01a6-333b-adf7-ed79d84ecb83 | -3.26758 | -50.08352 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf671b56-7af7-3708-ad19-3436795f0f7f | -2.29952 | -48.58102 | 2026-09-09 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef4b16c5-0f54-3978-92c7-d794fa73c5b8 | -5.77837 | -45.06806 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca92166f-601d-3000-a0db-4d5df6adb391 | -3.85277 | -51.37814 | 2026-09-09 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cff821af-f35c-380b-874a-a256cfd3537b | -5.77062 | -45.0668 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3a8923a-f82b-3c8e-a458-cf4b1e931e80 | -3.26088 | -50.08246 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ca1adfa-b0a8-3d7b-b531-c8bcb9bbe054 | -2.95337 | -48.59251 | 2026-09-09 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8024ef98-644f-3450-8671-1ed8e08f46f3 | -3.3563 | -59.43084 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69074806-5e19-3c5a-85cf-b9106be8ea4a | -4.11261 | -49.0608 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ab041fd-09a2-3f4f-ba31-48110813bb93 | -6.31405 | -47.36878 | 2026-09-09 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70f0a3e0-f24f-3ef8-950c-c623c621b926 | -6.15706 | -44.65566 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01ed2f72-889b-394b-ab94-0b563bf105bd | -3.7189 | -45.27262 | 2026-09-09 04:44:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a9964c7-10cf-3bcd-ac93-7031ef7ce013 | -2.93774 | -50.46387 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 622a7649-8e5f-343d-96fb-7f493b9ddfd1 | -4.00778 | -51.02806 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 475c915e-4424-31ca-9c6b-77cf9a64ed22 | -3.84801 | -49.05814 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cd9db11-d6cc-3a4d-9d79-403a4a95c161 | -2.93832 | -50.46025 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b82582f0-6e16-3b02-978a-3df396ba78f4 | -5.77376 | -45.07229 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d2f4ade3-e4c0-3194-94a5-2ba6ebf19bba | -5.60366 | -44.84609 | 2026-09-09 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 45f666ec-7e98-3732-a119-110abadbc86b | -1.61731 | -55.13486 | 2026-09-09 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f52a2ae-3ade-31d9-8b6f-8a8c31e95b07 | -3.36144 | -59.43349 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2fbfa2b-911f-3e2a-b167-412e54f8a7cd | -5.49429 | -44.69335 | 2026-09-09 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebcf111b-77d5-35c2-99ba-951e3e880563 | -1.61052 | -54.91846 | 2026-09-09 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d158426b-c447-3e1e-91e5-25f0eadcdecb | -4.17526 | -48.70675 | 2026-09-09 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22b2b7f0-6a0d-363c-8735-85c265a21ee5 | -5.76453 | -45.0808 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ccbcffa7-683c-3199-925a-59012ea1e741 | -3.55932 | -58.55725 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 391a4b59-da84-3c77-9df8-3cfc0d244b24 | -2.11899 | -54.39112 | 2026-09-09 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd3ccd98-570a-32f1-921a-2cced47951e2 | -1.61662 | -55.13928 | 2026-09-09 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c272e36-616a-3c63-a3a4-c772c856203c | -5.73717 | -43.27771 | 2026-09-09 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c7b03fb-a858-33e0-9400-8c90d69816e9 | -1.56217 | -55.25026 | 2026-09-09 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e655984d-2a53-3e17-a1bc-3d6c7b307432 | -5.76066 | -45.08015 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 39d91f4d-9270-3258-a956-7d4a6670dad7 | -6.42944 | -47.25546 | 2026-09-09 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a37ed13-c20f-3b20-9c91-d84d702c65c7 | -4.3948 | -47.65628 | 2026-09-09 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1bca332-c1fd-3fb8-abce-2ef296a7e508 | -3.26423 | -50.08299 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 288b77e8-73ca-3e21-b63d-e5b95988135f | -2.80055 | -49.57888 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6150dc-307c-3b35-85db-c22499d0dce7 | -2.9389 | -50.45664 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4594c8eb-1886-362b-8020-fcdd1a1dee74 | -3.84135 | -49.03594 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c6d1f30-b042-30af-90d4-6a9be4fbc652 | -1.18803 | -55.71665 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 73ae9c03-6723-3e8c-a129-fc5ca6cbaff6 | -1.6068 | -54.91343 | 2026-09-09 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93aba4ba-0e25-3550-88f6-913a69cc112d | -3.79686 | -52.40607 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e6044e6-b8af-38b7-ba6e-68fd78818bae | -1.19434 | -55.72042 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c095c3aa-22a8-393d-9da9-6d3d1aee9bb8 | -6.16456 | -44.66029 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 290fe704-1b6d-3f54-aa3d-e21d1df44e1e | -5.64895 | -44.30165 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f741cc4e-e68a-39bc-8826-47641995b2f9 | -4.3014 | -49.09085 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbd75537-3afe-37ca-99c5-5d4bfff0354f | -3.89171 | -59.60826 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d78df8e5-69af-3de9-b7ec-0f73e04621d6 | -3.72063 | -45.27126 | 2026-09-09 04:44:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f86d712-ccc3-36b0-8c0b-76931707ae52 | -6.36129 | -43.5958 | 2026-09-09 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8664b1f6-4f57-373b-babd-d7832c46a962 | -3.54428 | -48.18539 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c072f79-b440-3b51-afaf-0f23003f0e5e | -6.16054 | -44.65973 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 14220ca3-22bd-3b90-a4a9-535da7cbcc6f | -5.7684 | -45.08146 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README19.md)
