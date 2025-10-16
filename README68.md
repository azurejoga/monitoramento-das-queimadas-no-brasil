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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3030414-6932-35e3-84ca-8922c35c84eb | -9.14885 | -41.06147 | 2025-10-16 05:06:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 49.1 |
| 5eacbc7e-4311-3741-b478-15c42c00245d | -7.01397 | -43.7352 | 2025-10-16 05:06:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6fe91698-3c44-39d5-9d71-4710bfc33b81 | -6.99877 | -43.73737 | 2025-10-16 05:06:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ec55a2b8-ff41-33de-bb88-1033d0da72e3 | -9.15282 | -41.0382 | 2025-10-16 05:06:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 24.7 |
| ed998a8c-f35b-3b99-bb1c-bc1674fbdf6d | -8.4623 | -44.14647 | 2025-10-16 05:06:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| cccf529e-4638-3dc2-8e39-4c1c81a8fc30 | -10.70148 | -44.41927 | 2025-10-16 05:06:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 851d2383-7be9-3bed-81b2-5c9573e8fa0e | -8.1924 | -43.30165 | 2025-10-16 05:06:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 0c772577-8048-30b0-88c6-437f7d3822b7 | -13.65763 | -43.92899 | 2025-10-16 05:06:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 45364f6a-8c98-3b4b-b821-ddf1c654f568 | -12.67508 | -43.41292 | 2025-10-16 05:06:00 | AQUA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c2781d81-2662-36c8-9595-1842fd82a485 | -11.43527 | -44.13966 | 2025-10-16 05:06:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 7ba69c78-63d0-368d-969d-192a48bbaeb2 | 1.83207 | -55.72853 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3340f93f-0344-3cfc-9d49-863430bc217d | -4.3859 | -43.38138 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 161bc6aa-468f-32f3-a22b-b290fbede158 | 1.19856 | -51.28694 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf457667-f30e-397c-bb0d-08d5b42267fd | -3.34121 | -51.64314 | 2025-10-16 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9aff468-81e5-3753-a5b1-6bbeb718bf46 | -4.37943 | -43.38052 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8689d18d-ac6a-39cf-90ff-1cc703475222 | -4.40304 | -43.39978 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d03dc9e4-4c4e-3112-9425-295bd6837df9 | -4.27942 | -48.589 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a94a22e2-2c51-393c-abb7-caebb6c9de55 | 1.05966 | -51.0267 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59062648-79f5-3d1e-9ab2-fc5245e1e835 | -2.87928 | -50.73701 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa3d36fd-112b-3073-ba8d-25fb520df383 | -4.37721 | -43.39603 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 85b917fb-0e53-3025-b019-4eda0d20b8ff | -1.65722 | -55.14399 | 2025-10-16 05:06:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae7a7f1e-f3ff-31f3-8965-11f0696316c0 | -2.88003 | -50.7322 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1d45b42-8c01-3995-a320-df5a81c5c7cc | -2.25688 | -56.05759 | 2025-10-16 05:06:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0065926-b243-33db-8f73-462df06d7cf8 | -3.32945 | -50.10358 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a76dd056-1fbb-3d04-a309-bd983a562074 | -3.16757 | -49.53753 | 2025-10-16 05:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a52c5c81-ed5c-3817-b43b-2343deb9a6c4 | 1.76375 | -55.76168 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7331c5ba-b6e3-3c23-9359-a2185530e060 | -4.35616 | -43.39958 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3095db38-5de0-3554-b443-ff826f7da585 | -4.72301 | -46.16204 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddfef0e0-ba23-3039-ac59-1ad4e25b72db | -4.25224 | -48.55192 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dabd4156-7fff-34f5-9a41-0c6360c33a95 | 1.83101 | -55.76628 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3f6a44-bcb3-3493-a2eb-64534d5435b3 | -3.05582 | -52.65667 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c48e44c2-f8a7-3055-8b4b-a115d6c868fd | -4.28468 | -48.58502 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aa22758-032d-3acf-a2c4-c7d0e524633e | -4.10521 | -48.02867 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9ae048ea-3141-324b-9cd3-b0b1f77e7e0c | 1.04716 | -51.04136 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0db69e3-a1ba-32c9-87a4-a91fb9e35ae8 | -3.51376 | -52.48959 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6877771-3075-3d79-9be1-f1c824b7c8b0 | -4.15729 | -46.78929 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72acbeae-a9e2-3535-a57a-697eae3f9974 | -1.43033 | -55.25338 | 2025-10-16 05:06:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3f53601-79f5-3f4e-8b85-dac081f9284a | -3.81815 | -48.88869 | 2025-10-16 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bc84693-5f01-3378-98f7-1ba3dbdb4895 | -4.87396 | -44.58369 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51aa5132-05aa-30ae-bf7e-e6fd6b5f8313 | -4.72354 | -46.15842 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bd22d7d-a934-3c75-9636-f45a878a99d3 | -4.56479 | -44.00891 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65736231-a842-38b8-8a93-d3dc98ce0d29 | -4.21582 | -48.35793 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45893220-62aa-3e0d-b69c-7f92c05b609d | -4.72249 | -46.16568 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 536c7253-bb94-3036-8e84-ea45809fb861 | -3.42219 | -50.25514 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1256ea79-e8f4-3f6f-879a-9939c9b9a09e | -3.09744 | -50.37982 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b187f670-0d73-3056-9b83-2f6638d2a66d | -3.13069 | -50.21362 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3699c99e-b523-3470-b03f-966101fb916d | -3.38734 | -50.26757 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 890cbab7-dbb0-3e40-91be-0a5b223d0d8f | -3.21725 | -50.2157 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 283afc8f-65e1-33f3-9f8d-ebac71c805d0 | 1.83391 | -55.78469 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6afc585-8c64-3856-b494-b49f71123cd9 | -4.38515 | -43.3866 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 555c9311-e3d6-3bc8-b23c-374bbbe0af20 | -3.47376 | -50.02315 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 266ee579-9702-32ea-b408-cb5aa73327a8 | -4.502 | -45.40157 | 2025-10-16 05:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72ab8db0-0325-35f2-8b5e-742e995362d3 | -3.55785 | -50.12721 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cfdfcb4-2e58-3e44-825a-a9b16eb61c85 | -3.51316 | -52.49356 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| eb247ded-18a5-3d46-8879-15c124b37b56 | 1.74953 | -55.779 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25b5d748-b903-3980-ad48-4a8f93c201f0 | -4.28754 | -48.62791 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91878bd9-847c-36de-8841-d1ee482881b8 | -2.87764 | -50.72199 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f84a46f1-af6a-33a1-93ea-664d4a20a527 | -3.68571 | -47.63845 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 389434be-2102-3b78-9bb3-a66eed4f2be5 | -4.67512 | -44.09694 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee216f6e-5675-30e4-a693-19d9146184e6 | -3.44902 | -52.81639 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a40e3293-2b9c-3c10-82c3-719a07011566 | -2.44375 | -49.37305 | 2025-10-16 05:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 780c4873-17ba-364d-b4f3-c336e8108d81 | -3.48111 | -53.454 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51575d74-2c50-3172-b2db-e465621befa7 | -4.1066 | -48.01921 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3f5df934-0dbc-3d46-97ac-30142fc6fb88 | -3.48903 | -50.0881 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc875288-3086-3345-af2b-bcc0f8b45a2f | -3.1587 | -51.8163 | 2025-10-16 05:06:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2453e1cd-3abb-3588-b5b9-d1dda8ef2d73 | -3.01447 | -45.3805 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c5981d92-f59b-33d3-998d-99ff4656aed8 | -4.1059 | -48.024 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 6cbc96f9-fdea-36e8-bbfe-a4520f73404c | 1.78369 | -55.75486 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af33a7f4-6117-3b3b-848b-475f5c1c405b | -3.60164 | -48.98705 | 2025-10-16 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b62b4a5-5fef-329d-a25a-256a6f83a849 | -4.66494 | -44.08898 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 036ce756-3a5b-3ea0-9b53-fe417e9635de | -3.35414 | -54.72701 | 2025-10-16 05:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9399d7a0-7774-3da2-b14c-84a74e1f8389 | -3.68289 | -52.06092 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d7346c4-63a7-3155-9d52-5097bb93e1f2 | -4.1562 | -46.78923 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58eda023-cdd0-3ed1-ad5c-cbe740997ac1 | 1.82129 | -55.74899 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b618fc-ed98-312f-8e95-dc4793351dac | -4.67188 | -44.08493 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79c4fd63-3a24-30f6-8386-a0426a4b4dfa | -3.40582 | -51.56834 | 2025-10-16 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb55940-dfa8-3358-b399-00e6af8402c3 | -4.15598 | -46.79844 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c9828d31-ca5a-39c0-a42c-36e2ab92a575 | -3.83766 | -44.55034 | 2025-10-16 05:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a77f3948-d886-350b-92f6-192db9f6bb17 | -4.87461 | -44.57918 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30c60115-d3b4-3e4d-b8db-59203f856baf | -3.13924 | -50.21146 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9263422-940e-3de9-ac06-6b3edd6b8641 | -3.51119 | -50.21459 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23938d86-f400-34c4-9cd4-3a04f6d907c5 | -4.3981 | -43.38829 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3925c778-4056-3dae-b9cf-dd6c7eb7d255 | -3.83558 | -44.54856 | 2025-10-16 05:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 078e4627-9cf4-3756-a90b-2976b5757a52 | 0.87327 | -51.12155 | 2025-10-16 05:06:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16e3d24e-0c70-3c6c-b424-136635714d32 | 1.81388 | -55.7464 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0078b2cf-0640-3563-9e65-fd1ce2d120b8 | -3.56376 | -51.11851 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 862866f1-c406-3470-a5c8-8869b8ef1779 | -4.21118 | -48.35729 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6dfd926-3a92-37d6-8038-523c7ae38171 | -4.1609 | -46.79299 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65cad719-47e8-35da-9732-4fc7cf5ec263 | -4.38365 | -43.3971 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 9a606c96-edfc-3a49-9591-01a597362357 | -4.72847 | -46.16269 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497b66c2-143e-32fd-a683-6f7c9553ed6c | -4.40228 | -43.40503 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c19fc61-2f94-3ed8-b939-885973d9c4ff | 1.77343 | -55.75644 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a13fb2-b0ac-3183-9a76-2db3f83988d8 | -2.88315 | -50.73761 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ebd664f-f1fe-3b39-8c62-a7bf7cf5f172 | 1.78938 | -55.74646 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c9754b-7c51-37f4-b4a1-a3799e546d36 | -4.63952 | -43.13044 | 2025-10-16 05:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 791fc78d-1c4d-3abd-b048-91a96250efc5 | -2.16175 | -52.2895 | 2025-10-16 05:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828e02ab-36e4-3028-95bc-f0bab0d3bd47 | 1.82244 | -55.75633 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7112f839-b8d7-35c6-b826-b0cf04a9aac2 | -4.10733 | -48.01418 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1da27e6e-0332-32a6-85c0-dd60d08b7935 | -4.55856 | -44.00803 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e3fb112-9906-3b21-98f0-10c879cf274a | 1.20148 | -51.28235 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README69.md)
