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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eef7951-29b1-35bb-a1b0-f499cb18ad79 | -11.14035 | -46.35398 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 862b7f45-358e-3096-acc0-ebff584f3b7f | -11.1598 | -45.28017 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eb85438-5bd1-32f3-b9e9-5c6831ab488e | -9.05806 | -49.81175 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708ea967-2df0-3e26-bc75-5124094706d2 | -9.74441 | -51.08274 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aebd0ad3-7828-3073-935f-3ba65f63bd93 | -11.81304 | -46.75867 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05084012-9e94-3d15-8f28-cad51d50a658 | -11.456 | -49.27504 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e79b4388-bd3e-3d6d-8800-6598db4c89af | -9.01549 | -49.53944 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b600248-92aa-3cff-8908-5a77208b4dd1 | -11.99265 | -47.19339 | 2025-09-10 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 765d7943-6b20-3376-9988-6b229eb4664c | -8.34178 | -44.83697 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5704bbdb-06db-3443-90ef-9635fd187d1f | -9.08101 | -45.70594 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19c2a674-d019-3816-baa7-8badec75c72d | -8.4117 | -49.10241 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4485ade8-f615-3c69-80d2-426c77d70e75 | -6.4423 | -44.05283 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a61791fe-019a-33a8-8422-799d73164287 | -9.67561 | -46.59327 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98879ea9-c593-3629-9cd0-5f35a309aec7 | -9.80813 | -47.76829 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d12276f-4bf8-37bd-b841-8910b100cad2 | -5.86658 | -48.15631 | 2025-09-10 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce0d0d77-37c6-380c-a17a-4214f32fb181 | -11.11579 | -48.42161 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d1a2e05-ff7a-36a0-8449-53ca6ef8c007 | -7.48467 | -48.22825 | 2025-09-10 04:42:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97fdb9ea-a1fe-3b5b-95d6-31c2f6730def | -9.66438 | -46.6186 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f4053d8-7f1f-3692-97ec-db11e726448a | -9.99175 | -48.56773 | 2025-09-10 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4517ec04-68e2-3362-813a-600feb2f6e04 | -7.79104 | -46.09927 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ad089c3-7aa5-3f85-95de-c4500f14bd31 | -10.01152 | -51.67667 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60f3b8fe-945b-338f-ab1c-0f3eacb55ab0 | -9.08047 | -47.00019 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0d71617-e4c6-3f61-80e9-274167ba145a | -11.13906 | -48.35059 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee57b493-52e5-35cf-8cb4-70d49b09fdf0 | -9.211 | -50.55045 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9da720-5321-3061-8377-a3ad81c2b3ae | -10.65512 | -48.60713 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97cfa1f6-16db-3dab-8d58-a5aebfe91c8f | -10.19416 | -46.67815 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feccbafc-fb48-3c0c-ae50-ef75be126ca6 | -10.38695 | -48.83113 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9201a15-5c99-379e-8c2b-85d673a9c490 | -8.21175 | -47.15956 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b511b48-af45-32dc-aa0c-eab123790a35 | -11.45966 | -50.32177 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7009606-c4ab-3698-9b69-3301dab57ba9 | -6.5365 | -44.78502 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b37a6fc3-276c-38ad-a0ec-4021ba163ee1 | -7.77894 | -50.76931 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cea7a2a0-62d9-37b5-92ce-d3b4c85e1e77 | -9.71238 | -48.0927 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a90cb66e-d3ec-33ad-9c62-7419db0b3959 | -7.78059 | -46.09301 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae245ca7-6a22-3b87-8bfb-d839301aedf2 | -11.44531 | -49.27706 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b06b067-6be8-345d-97dd-104e45b73637 | -11.3934 | -43.54086 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b08036d-d10b-39e6-9755-7009610e561d | -11.19742 | -48.38688 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 932815bc-162e-33f4-98a8-2fd206f69bef | -9.06296 | -49.81646 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb09c21-8003-3cd2-aa6f-3605d0ab12f2 | -9.00605 | -49.53434 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba15ff5a-e08a-3e1f-ac98-96e6f551de2c | -9.21435 | -50.52937 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f0c3036-f009-35aa-9df1-a44b0c65b109 | -6.84438 | -44.9133 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3a9a997-721a-3fd6-903f-6e365114219e | -11.03563 | -46.05288 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3ed246b-e87d-3b27-9501-12de270620c2 | -7.66319 | -50.26632 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2d97a0e-466c-321f-a132-d656a57a0a85 | -6.64884 | -44.08202 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8090f81f-f904-3a77-ba76-2cf84e4b6835 | -11.31967 | -46.52343 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6135fd0c-aae7-395d-821d-edfd3185dc00 | -9.67114 | -46.6241 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 691d65fa-603d-3f66-b74d-e29bfa059651 | -11.26379 | -51.12585 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ed5b2a5-4092-367c-899c-5241c2edd6f7 | -11.11549 | -48.41369 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3e1d28c-49a4-3051-9954-e0f17a9de75e | -8.18988 | -47.16043 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9feef38a-9162-3080-a785-b79ed83d20c7 | -6.93073 | -43.91854 | 2025-09-10 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 346d382a-d9bd-31c2-be3b-53866322c885 | -8.30308 | -44.81984 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86d40be8-2ef3-3f8a-b43c-04dafc7a743c | -9.31704 | -46.73084 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3f39f489-8ebf-37de-9133-d31b4b306d9c | -8.06706 | -52.33109 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb04a5f-0cac-3838-8089-5899eb1c731e | -11.43628 | -49.2682 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18ec6065-fb71-387a-a541-ace56355a2ba | -10.01744 | -48.09922 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e6fdcde-70ef-3cd7-bc60-e8c7ce64bcc1 | -8.4817 | -47.30366 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e979fc84-e8c5-3321-9ae8-38ffccf65184 | -10.27407 | -48.81813 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f33c7768-e0e6-3f65-8a81-50e7315a1fcb | -7.875 | -46.03242 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d7a3a0f-1f4c-3e9d-90c6-0883eb6c0420 | -9.14119 | -45.56579 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1e69658-9df2-324e-b9fc-4032a0c799ec | -7.76337 | -46.08108 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 914ba016-8359-3244-91d4-d7bfa3aabddd | -10.57276 | -52.04813 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fa26f2a-cfaa-3185-9c4f-a76284607ff6 | -10.56083 | -51.99285 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4753bd8a-7371-3cb3-ba37-8fa2bbe247bc | -10.17957 | -44.76137 | 2025-09-10 04:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d5de60e-5cd8-3f2f-88a8-3c3df4a2fc32 | -6.88524 | -47.8844 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d3ea575-55ac-3dd5-a6db-304e01468fba | -9.20448 | -50.19039 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de1479df-ae7b-3eb4-af8e-0cc4f4ce5b96 | -7.54478 | -44.65547 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab76f9d4-1d3c-38a3-86de-27e3adefa1f5 | -10.00819 | -48.08997 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9e1959f-faab-32b7-a834-a55079d52098 | -9.43844 | -46.71639 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1aa7b342-9df4-3a20-907b-f7b93ce0a6fa | -8.42841 | -49.11937 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f66b7397-d04f-3358-8a08-9c3457b41ce6 | -14.33022 | -47.30207 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 677b8434-b3a4-390e-a9ad-bf462cf3899e | -18.69491 | -52.59457 | 2025-09-10 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eaa4db1-f458-3cbc-a19f-45f3673131e4 | -19.59805 | -46.08257 | 2025-09-10 04:44:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ebfa65a-21fb-3718-8dc7-c0039c5f4cf2 | -15.52445 | -48.38427 | 2025-09-10 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1756fd-2df5-3d0f-83a7-f5d10a968366 | -12.94474 | -54.75425 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c42ffcff-1ca8-3aa5-9a0b-1dd657776918 | -19.64336 | -45.04499 | 2025-09-10 04:44:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e370be7-242f-37a4-a67e-908846b5a6e6 | -15.65673 | -49.93203 | 2025-09-10 04:44:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8b9058-aeba-362c-9b1f-9b13312653ba | -15.08417 | -50.07874 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18e67cdd-8350-33a0-8f86-0ebd711ef0dd | -15.93934 | -50.2281 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f490f824-133a-3d67-a33c-f46b0df81f39 | -13.97468 | -48.23632 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d0270d1-432b-3d7e-addb-5d9985e3b303 | -12.02111 | -51.00197 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8088ddc-fd3c-3555-8ced-2be86ae56287 | -12.06318 | -51.0597 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36e2da35-6d1c-3510-86e1-d8e11e8e0d2d | -13.33814 | -51.69337 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ed2ae5-1a09-3f50-ad9e-429190cd1494 | -15.8025 | -52.26132 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cfaf268-535a-3847-a03d-3b825186da0a | -12.03992 | -51.03409 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e98c8b-ead1-3948-ad32-beeb56ad04f4 | -12.93381 | -54.79487 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cdc39a6-567e-3740-9304-74045b99925a | -14.42908 | -52.95132 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97c4713f-8b60-31aa-99e3-4ca5ec5e7577 | -13.17612 | -47.25256 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19d326ab-9e05-32eb-95bd-2fa4ce864d14 | -13.97527 | -48.23223 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be4ff2e4-7d70-3fb3-bae7-3d60d15a9a73 | -16.14562 | -47.89339 | 2025-09-10 04:44:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f97eeda5-3e3b-3826-9c7d-3c6d9bd53c1b | -17.30756 | -46.75076 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13613014-b439-315e-af31-5003fdf6ee4f | -19.17585 | -43.0668 | 2025-09-10 04:44:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4046ff36-8779-3b5f-a1da-82a97d09bfff | -14.78527 | -48.22707 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc1a9094-959c-3e28-a80a-575bf2300dda | -20.15482 | -43.66086 | 2025-09-10 04:44:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebe56206-8e19-3e54-96ce-0f79ed5ed584 | -18.45302 | -49.56751 | 2025-09-10 04:44:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3b43a1f7-24cd-3e04-9292-798503ae1ffc | -15.84752 | -52.2692 | 2025-09-10 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82adeb6f-97a5-38b8-a076-0e09bfdd5563 | -13.12703 | -47.19205 | 2025-09-10 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 696bbfd8-d577-3234-89db-ff5b1f3052d3 | -13.98499 | -46.6619 | 2025-09-10 04:44:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15bcb5c7-47b7-39cc-90c9-645b8e6ece02 | -17.57845 | -49.81787 | 2025-09-10 04:44:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc8b5442-427e-3035-8789-3a2088dc5832 | -13.00568 | -45.20634 | 2025-09-10 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3853b5b5-7d22-359f-bbc5-3d861ecdbd64 | -15.83091 | -48.96608 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e3ba0f0-7c27-36b8-b33d-b15983fde13f | -17.32649 | -46.70074 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README72.md)
