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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f49cc90-1aff-3e66-936f-5d7295114a70 | -18.1977 | -53.3208 | 2025-09-28 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 161.8 |
| ec22b9cf-7126-393f-a3a5-9f7217721fe4 | -11.4083 | -46.9597 | 2025-09-28 13:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6b7800df-a94c-3af4-bbf8-18d51af9c4c2 | -12.9547 | -45.1618 | 2025-09-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 08ce089d-c23b-3463-8b96-07288094d8d7 | -11.9464 | -47.8916 | 2025-09-28 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 734323f5-b88e-391d-a994-9e819b9fc483 | -8.2859 | -45.4317 | 2025-09-28 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c76833ad-eb78-3eb9-a7ca-2538a6a1a16b | -11.3842 | -44.9849 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d68c85ef-053e-374d-bb4a-d024372d12af | -11.9982 | -47.0821 | 2025-09-28 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 407946b6-870a-3829-8c43-9e1ceb8e0f26 | -6.6192 | -44.9493 | 2025-09-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 208.6 |
| ea1e6604-3751-3b5f-9ae8-119226fd3d5f | -9.0913 | -45.8673 | 2025-09-28 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 65626f58-cd66-3c04-9882-6eed50d7fb19 | -6.0591 | -44.7661 | 2025-09-28 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3e6270a8-1659-379c-99c9-4497737cf8c3 | -11.365 | -44.9876 | 2025-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 08e2a980-52fd-3599-a11b-7dfd520618c0 | -13.6267 | -47.3152 | 2025-09-28 13:30:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3fa568db-5297-3c4b-9344-2646de39103e | -5.9004 | -43.6976 | 2025-09-28 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f8607d1e-9e1f-3179-aa2f-8c92b3b0be76 | -7.3661 | -47.0173 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0e21f88c-519d-307d-b4b7-f33d02053474 | -5.1885 | -43.7495 | 2025-09-28 13:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 1e1eb95e-7192-39c9-bebe-ed220f18edc0 | -14.7851 | -45.6818 | 2025-09-28 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 4fbab05a-1d37-3b14-8905-75b93e804b1c | -4.676 | -37.6366 | 2025-09-28 13:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 161.8 |
| 991ca8e7-77e2-3744-8033-23c937d0ec75 | -6.6005 | -44.9509 | 2025-09-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 9b55ee7b-89ed-34f4-8c90-ac04a4ee7fc1 | -5.7583 | -42.8447 | 2025-09-28 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 1e291f4e-ae10-328a-a4f1-971a09d81d20 | -10.0187 | -48.5183 | 2025-09-28 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1b4a1d89-67cf-3a2e-bc77-9a905d5f2f30 | -8.9185 | -46.0889 | 2025-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fa8506c2-9550-3f86-a2bb-77a6be077400 | -12.2825 | -44.0804 | 2025-09-28 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| c3a83eaa-15b1-3d81-9f1d-21a37eb1efa8 | -5.7396 | -42.8461 | 2025-09-28 13:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| b65c4610-a707-3525-9848-0640e66b4fa3 | -14.5535 | -48.4014 | 2025-09-28 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 98745b50-72a4-33f3-b18c-9d574e502b32 | -5.6461 | -44.933 | 2025-09-28 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 22142e5c-56d5-3157-bdc2-6209c6b38be0 | -5.6462 | -44.9102 | 2025-09-28 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| dc5865df-12e3-392b-94bc-b9dabb93f70a | -11.4604 | -44.997 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c16f131b-548a-36a1-b253-fb9335e91c1c | -11.904 | -44.8161 | 2025-09-28 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d3f005c2-b212-3f23-bc48-a38e795e8405 | -14.576 | -48.2417 | 2025-09-28 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e42c0bdf-1403-38a1-89bd-8700f58ad8b7 | -11.3642 | -45.0339 | 2025-09-28 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e8e29780-c870-3d78-854f-367522b32e2a | -9.2824 | -45.7104 | 2025-09-28 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 02dd9bae-df90-3cfc-84ee-d4c31451ef7f | -8.2668 | -45.4564 | 2025-09-28 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| eb31f8d0-25e1-3e98-bf44-1ee61754cd14 | -8.8226 | -46.2115 | 2025-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 6369c8ef-e851-301b-b434-167937a3f918 | -12.9363 | -45.1184 | 2025-09-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 40aa70ad-6f7f-343b-8d35-040ad6eb08fc | -7.1571 | -45.5158 | 2025-09-28 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6d267a99-8d9d-3250-9ce9-21eecc759553 | -7.8823 | -44.5594 | 2025-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 9ea36876-6b47-3dab-905b-15cd87190b56 | -13.7893 | -47.8957 | 2025-09-28 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9222b8f5-b610-36a0-b5bf-f9fa1d9af7ed | -7.3659 | -47.0394 | 2025-09-28 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 463817a0-0bc4-3931-b108-cd7eaa55ebff | -12.8972 | -45.1479 | 2025-09-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 80564d47-790a-3f9d-afb9-bfcf3493ab40 | -11.4409 | -45.0229 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c4569c5b-2a7a-3795-b46b-62a77c32adfc | -9.9581 | -43.5987 | 2025-09-28 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| c041141b-a78e-3c67-91aa-68819489f565 | -6.2762 | -43.621 | 2025-09-28 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a3ebdc82-7400-37a5-a985-7f4203e21703 | -8.2856 | -45.4545 | 2025-09-28 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| cae48b44-efb6-356a-b5d8-f4670eb2f667 | -12.0218 | -47.9481 | 2025-09-28 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| f7d38a6a-c913-36c9-a006-0d50782ffa3e | -9.3013 | -45.7082 | 2025-09-28 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| fdcde8ac-4345-378c-9ce0-d1ccfc5f51ee | -7.882 | -44.5824 | 2025-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 29af5c85-70ba-3f7b-892e-ba9381564eb7 | -5.3057 | -43.1599 | 2025-09-28 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| aa753fad-b9d9-39c2-9f09-df5640a28977 | -11.4217 | -45.0257 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 7e948a08-921b-38e5-9b73-d40e8043ff85 | -7.5089 | -44.297 | 2025-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 32c8f78a-a96b-33a4-8f7c-f90b0dae782a | -13.011 | -49.4423 | 2025-09-28 13:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| dba51beb-fadf-313e-8380-853f122e331a | -13.6122 | -48.0787 | 2025-09-28 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1e925b4e-3f2b-3b1f-bae5-54510d33c863 | -7.3849 | -47.0157 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| aed08bb4-f6db-3d47-9648-067e142e81b6 | -11.979 | -47.0847 | 2025-09-28 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 7b64994d-d572-34a3-8aff-c955a65b4e2e | -5.6273 | -44.9343 | 2025-09-28 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a0b78b2c-9e70-3a5f-b818-d36994852c6c | -7.8634 | -44.5612 | 2025-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b6cefa45-2321-3edc-9dcd-02f02768105a | -6.6002 | -44.9736 | 2025-09-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 343.6 |
| 2480119a-6455-3228-af7a-1810b0112799 | -6.2759 | -43.6442 | 2025-09-28 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c836e968-9f72-307e-878b-febe7f881bfa | -7.3847 | -47.0378 | 2025-09-28 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 271.7 |
| c8f1501d-e85f-306d-86c2-78f39c440b6d | -6.619 | -44.9721 | 2025-09-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| a2f04b1d-aad5-3412-b61a-e73ccce13259 | -6.3154 | -43.4548 | 2025-09-28 13:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a4d5738e-cc21-3de4-80fb-86738b667bd2 | -11.9824 | -48.0197 | 2025-09-28 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 0afd787c-d379-37d8-9829-545c1624d649 | -8.8759 | -45.0274 | 2025-09-28 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 617e2472-1219-382f-8618-96dfff459d52 | -4.6944 | -37.6868 | 2025-09-28 13:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 884f0ec4-8f07-3721-887c-e019b8072647 | -7.3659 | -47.0394 | 2025-09-28 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 9569ce54-58ab-3336-b276-0288b014f128 | -7.8823 | -44.5594 | 2025-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d663d686-c219-30b4-849b-9a53cbad1b59 | -5.6461 | -44.933 | 2025-09-28 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e16b746e-82a7-3f1e-aeae-ada18684cf6f | -9.0874 | -47.6074 | 2025-09-28 13:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a56b27ca-b476-3a21-a4fd-4ba624aa2e59 | -4.7619 | -43.29 | 2025-09-28 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1ff0ebfd-4b04-3367-8968-51880b08a949 | -8.8226 | -46.2115 | 2025-09-28 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 822694f7-7980-32b3-945b-a5a2deca058a | -11.4083 | -46.9597 | 2025-09-28 13:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d115f46f-c5ca-3ad8-b6b7-10782ea47d72 | -10.9137 | -45.7375 | 2025-09-28 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 87727535-56d8-372a-872e-ea299277c064 | -9.106 | -47.6275 | 2025-09-28 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 33676f8b-5c30-39be-9ae2-c02c5aaafebf | -11.9982 | -47.0821 | 2025-09-28 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 97030fb8-0219-339c-bdb1-cf572f179b8e | -8.2665 | -45.4791 | 2025-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c237d33c-836f-3d61-bdf0-5a69f8c7556f | -11.3842 | -44.9849 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 93a6de12-7880-37f0-a544-04c5fca39976 | -13.6267 | -47.3152 | 2025-09-28 13:40:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4085a8d2-8d9b-3aa7-a729-93f059144275 | -7.8634 | -44.5612 | 2025-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e5d248db-f7ac-3497-b57d-c6c6f7a20f90 | -5.3057 | -43.1599 | 2025-09-28 13:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 684f073c-d0b9-3568-9c2f-189a4ef3fa50 | -8.1614 | -46.3899 | 2025-09-28 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f66dfca3-0498-3535-87f7-e1010eee4f2e | -11.3654 | -44.9645 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| a9ebaed6-f603-3144-910d-bf0c57247364 | -8.2854 | -45.4772 | 2025-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 1c779d95-803e-3954-bb9f-0407724db858 | -6.3154 | -43.4548 | 2025-09-28 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b0792ebf-1895-3f0e-818e-70bf6f894c68 | -11.9986 | -47.0596 | 2025-09-28 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e8395c82-2e17-3768-84fa-630ed22f39ce | -18.1977 | -53.3208 | 2025-09-28 13:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 6844b3c3-652c-3fee-b174-544bc5c82375 | -11.4413 | -44.9998 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 04f890e6-f790-36cc-8fa5-99e0a598c801 | -14.3813 | -54.9472 | 2025-09-28 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4459f678-6d7e-348c-b64e-7af1248b2517 | -9.9581 | -43.5987 | 2025-09-28 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| feacc2af-51a0-3c0f-9a13-f4d1b1812dd1 | -9.4455 | -47.6144 | 2025-09-28 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 33646f66-b81e-3dc2-a5c6-df094e6253de | -4.6946 | -37.661 | 2025-09-28 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 561.0 |
| b98c092a-3a96-3527-a2f6-c1f9e8eeb002 | -11.3658 | -44.9413 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ef507164-7656-3d66-b3c9-473a3f2d760c | -7.3847 | -47.0378 | 2025-09-28 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 2891add9-aa98-347e-a360-48ecf409c0e1 | -5.6273 | -44.9343 | 2025-09-28 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cd9eb1a0-0e2f-3c17-b48f-9a2a39d0c40f | -11.9794 | -47.0622 | 2025-09-28 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bffd54a2-84f9-3512-942a-179a172da358 | -4.6944 | -37.6868 | 2025-09-28 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 336.7 |
| c2480be3-ad03-3026-951d-fe9eb6ea6173 | -5.1712 | -48.4792 | 2025-09-28 13:40:00 | GOES-19 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 356243d8-c949-3b34-9397-a30f331f1a75 | -7.882 | -44.5824 | 2025-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| bc6716f2-5212-343c-9b6c-89cc26b09fda | -11.4604 | -44.997 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 68bff9c8-a72a-3c17-89da-b3533912801c | -14.765 | -45.7086 | 2025-09-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6eb803c2-257e-3dd0-a030-cfe817a73391 | -5.9004 | -43.6976 | 2025-09-28 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 4918fc53-c76b-30bb-b9cb-99171273c205 | -12.0214 | -47.9703 | 2025-09-28 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 238.2 |


[Clique aqui para ver as próximas entradas](README101.md)
