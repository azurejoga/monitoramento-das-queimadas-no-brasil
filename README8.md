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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54de3030-3636-33c8-9a8c-9f2e6c82fcf8 | -4.7115 | -42.939899 | 2025-11-14 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4a6cd70-6a42-3d28-8777-704d321c7f29 | -2.8792 | -45.2775 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e575160a-0735-3732-8266-f5bfca43c3fe | -10.2878 | -44.346199 | 2025-11-14 00:38:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5202c04-ddcb-3a6a-be67-cdde37e5d0d7 | -10.0564 | -44.769299 | 2025-11-14 00:38:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 658d5b4f-6d5c-3b62-bcbb-390f21341490 | -4.0997 | -48.016399 | 2025-11-14 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d05142fd-ed8f-347a-9a76-194ac15f6a84 | -9.6317 | -40.349998 | 2025-11-14 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 49a4f564-f46c-3364-93fd-3697252736ca | -4.9605 | -47.7229 | 2025-11-14 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c13a89b-5074-3526-b669-7d2877a82769 | -3.4063 | -52.723701 | 2025-11-14 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0accef35-15f1-3d77-a8f5-910ff9e2d361 | -7.0251 | -46.428299 | 2025-11-14 00:38:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d93f8866-bd26-3942-8c3c-d295907c1364 | -6.482 | -43.752102 | 2025-11-14 00:38:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2549f98-2241-379d-b9e5-1378a260cca1 | -7.9229 | -44.345798 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8dc8d6b-ea9f-3eb2-9536-1615ca6b4833 | -3.4085 | -52.733398 | 2025-11-14 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 388bbe1e-2815-3ef9-8f1a-1870a93ae152 | -4.4563 | -43.472301 | 2025-11-14 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b607467-115d-3c08-89d7-c71e48915dc5 | -5.3618 | -46.285 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90492045-262d-33b6-8e63-5589f0b2bc23 | -13.4741 | -46.4972 | 2025-11-14 00:38:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73c34c1a-ecff-3a6e-9d7c-e0b7aca8248f | -4.5299 | -46.390598 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a09e40e3-c6f1-30bd-bda1-a3bd8d71311f | -12.6752 | -46.7467 | 2025-11-14 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4bc1e5a-2b37-3d41-ba19-fe403aee1c5d | -4.7002 | -46.457802 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 698f4f51-584a-3725-a8f5-5357a8281522 | -3.4688 | -45.640202 | 2025-11-14 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8ddedf2-e05f-32f1-9161-7601a9620a41 | -3.0096 | -49.427299 | 2025-11-14 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8b80a0-e712-3122-9de5-26882e6d409e | -9.5789 | -46.634899 | 2025-11-14 00:38:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9d4931a-0e21-3aa1-bc29-9fa08ae47ea1 | -7.4504 | -42.577 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 819ae725-e6f5-38f0-aa03-687df8d87683 | -6.1495 | -48.053101 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae931f73-7382-33f1-9f55-4d576fa3a2fe | -3.9135 | -44.319801 | 2025-11-14 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 575afb9e-0744-3af7-99c1-a14b62f87ce5 | -5.98 | -42.597 | 2025-11-14 00:38:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4309015-0a5f-38e6-82c7-10677131efd4 | -15.473 | -43.548801 | 2025-11-14 00:38:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 29bfa5b0-2fbd-3e87-b255-ded3b99fdb88 | -16.585699 | -42.2183 | 2025-11-14 00:38:00 | METOP-C | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d24bc009-49fd-3765-bef6-977905739150 | -13.7703 | -43.165401 | 2025-11-14 00:38:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b3b85653-809c-37cf-9d92-52a8549fc5da | -10.6268 | -45.001598 | 2025-11-14 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 770f6aec-db0b-37c8-a04c-afa684a0ee4f | -3.7704 | -46.006302 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a812c2e3-cb47-374a-877d-a8e7b7de1ff5 | -3.5112 | -45.5564 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be0570e4-5bb1-3a10-9bef-0622c9edaa2b | -7.1522 | -41.259499 | 2025-11-14 00:38:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4bc61ec-f670-3d5c-af17-c15c2c023017 | -5.3602 | -46.277802 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac5ed7d-737d-3194-8183-d51d91d32fd2 | -10.7485 | -44.9034 | 2025-11-14 00:38:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34fe2b20-e01e-38ef-aa33-0bb8f53a6c62 | -4.7165 | -46.439098 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 832b5fa3-2a26-3800-9999-36e23cdb492c | -10.2896 | -44.353901 | 2025-11-14 00:38:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd418e54-252d-3d57-9dbe-72abc55af196 | -14.6746 | -46.571899 | 2025-11-14 00:38:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68c9f5f1-bf98-32da-b703-abd0127504eb | -5.3716 | -46.2827 | 2025-11-14 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c27c8ec7-fe51-3c8d-ab09-7be704600600 | -15.7825 | -41.463799 | 2025-11-14 00:38:00 | METOP-C | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77240c81-9477-3aad-9558-f614f07865d5 | -5.7537 | -42.7286 | 2025-11-14 00:38:00 | METOP-C | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b728ac4e-ea7a-3e2d-802e-cfc05b08cd28 | -5.7527 | -49.255798 | 2025-11-14 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b56e2ceb-d5a5-3873-8b44-9ce01bd59fa6 | -4.3804 | -45.258301 | 2025-11-14 00:38:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca0084e0-f05e-3b5f-992d-54abd7f64b62 | -11.8268 | -47.790901 | 2025-11-14 00:38:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 889b4966-985b-39c3-8c5b-ecb4b13dc03c | -13.029 | -46.5327 | 2025-11-14 00:38:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1c89b246-2342-3e4b-80d1-9be851b64cc8 | -0.8648 | -47.313801 | 2025-11-14 00:38:00 | METOP-C | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9ff015-0a30-3ef7-a559-82e0b23209c8 | -3.6704 | -45.708801 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c2d12ef-f44a-36f8-92fd-ccd95d500a99 | -7.8742 | -44.314499 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3b45096-6b30-33c8-9b7c-ebdbf5c48f7e | -11.2461 | -47.493198 | 2025-11-14 00:38:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85abff70-c880-31f6-a4e1-a2e35c39deca | -20.7568 | -43.2141 | 2025-11-14 00:38:00 | METOP-C | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98c3fca1-b549-3e88-a75d-928f5b2599dc | -2.1159 | -45.3638 | 2025-11-14 00:38:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74934786-4d10-314a-be70-723adb37e1c9 | -5.3489 | -46.764801 | 2025-11-14 00:38:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d84fa368-520c-3dbb-aa18-9b22d3ab20db | -17.791201 | -44.979099 | 2025-11-14 00:38:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4578aaf7-c953-3e8e-875c-d6cc9027cb13 | -5.7863 | -43.733299 | 2025-11-14 00:38:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8336dde2-713d-360d-bb72-0cea271c258e | -4.3051 | -46.266201 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56ca9546-0689-356a-b0a0-e70a1085cedb | -3.722 | -45.8423 | 2025-11-14 00:38:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3255fc5d-69a7-3595-a940-86e1225b8a5b | -5.8557 | -47.5793 | 2025-11-14 00:38:00 | METOP-C | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42b9b8e6-7a80-324b-9ad3-27b088f6e287 | -10.6284 | -45.0089 | 2025-11-14 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afcc18c8-cfae-342c-8c17-56e9792d65d8 | -5.8573 | -47.586102 | 2025-11-14 00:38:00 | METOP-C | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73216bd9-3f49-34e6-8f78-72ffbfe18cef | -11.9905 | -44.207699 | 2025-11-14 00:38:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12e392ce-71b8-3094-8718-24a0e949bdcc | -7.8489 | -44.2948 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 289c59a0-66d4-32f6-be18-88a5d40f39be | -9.6251 | -40.3237 | 2025-11-14 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 680b934f-dde9-372f-bdbb-dbd09f20ef17 | -7.8568 | -44.284302 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6bccd7e3-186d-3fa2-b638-ece13a131062 | -4.732 | -44.731998 | 2025-11-14 00:38:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b168b59-1b95-3073-b8a7-2b8e181bed2d | -6.8887 | -42.859699 | 2025-11-14 00:38:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d384bc1-92c0-334a-86bc-ea30a4ccedcb | -13.2726 | -44.2575 | 2025-11-14 00:38:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 539af79f-7278-3bea-8708-5013ef416ca3 | -11.939 | -43.944401 | 2025-11-14 00:38:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 918e473c-4427-3d85-8c12-e38d737bfe5b | -9.0929 | -44.315399 | 2025-11-14 00:38:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70fb470f-be77-3fa6-b698-0a5bddb66a89 | -6.4102 | -39.745602 | 2025-11-14 00:38:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 23e01053-d52b-3c9f-bf2e-70f85a92a97a | -4.5316 | -46.3978 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 430f6d52-7d32-355c-b73d-27791fba236b | -2.8812 | -45.285702 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 653d962e-5e17-3281-86f4-484d4f240e16 | -7.8752 | -43.7948 | 2025-11-14 00:38:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bad119eb-05ef-3ec0-aa9d-38b7e623de35 | -12.1445 | -48.019001 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e946e06-8a21-3531-bcbd-e2166fa342e4 | -3.4786 | -45.638 | 2025-11-14 00:38:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 154e8be3-befd-37f2-9ae1-edf0de213574 | -9.9175 | -47.8587 | 2025-11-14 00:38:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90cf9f83-fe65-3da0-a480-2ef3019e74d6 | -12.6951 | -45.4226 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08599e66-a372-3c8a-88aa-24e7947ceb8f | -10.1042 | -40.881599 | 2025-11-14 00:38:00 | METOP-C | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e8bfbe0b-f7c0-3623-83d7-cf677fdcf88a | -10.0546 | -44.761799 | 2025-11-14 00:38:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33a136fa-5195-38a5-8998-613c61661bc0 | -2.6578 | -46.993999 | 2025-11-14 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adfce175-3104-3292-aff3-5c315dd3c9a6 | -12.0611 | -48.201 | 2025-11-14 00:38:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3a39aac-0acd-3089-93cd-15abdd5ce875 | -12.5939 | -48.335701 | 2025-11-14 00:38:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e79c8bb8-5425-358a-b848-aeefed5330b0 | -17.634199 | -46.709801 | 2025-11-14 00:38:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 401becb4-af11-3af3-ae0b-d8e097e04204 | -2.3735 | -48.674099 | 2025-11-14 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6226a91d-9a98-3f6b-b36f-55dd47d19d4b | -9.9092 | -47.868 | 2025-11-14 00:38:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f130b4fa-35a6-34b5-8456-579044355e9f | -2.6393 | -45.7542 | 2025-11-14 00:38:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 106e3608-b910-33bc-b8d5-49c17c7acea5 | -7.3881 | -48.653599 | 2025-11-14 00:38:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 92fdeed4-4ecb-31f4-88d0-bac67df42bd0 | -5.571 | -47.101898 | 2025-11-14 00:38:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18ea34dd-314b-3f33-9919-7c1ed399f099 | -4.5333 | -46.404999 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce42367-e046-3735-bb49-cfd8950296d0 | -6.5988 | -44.2467 | 2025-11-14 00:38:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e054ba99-fe6b-33c4-86ec-30ec21e0873d | -9.3125 | -47.824501 | 2025-11-14 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5b8c0bd-482c-31ae-b05e-859141def427 | -12.0002 | -46.7682 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dc3fcb1-2a05-313f-b238-e1694e4a3f80 | -13.6809 | -43.006802 | 2025-11-14 00:38:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c3ffea47-c1bc-3c45-a927-5f170d4083da | -6.2044 | -47.255699 | 2025-11-14 00:38:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2001008c-7c3c-3acb-b788-2453da9e4a62 | -11.8408 | -49.2169 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fdfb925-7e02-3a6c-b172-a23909d855c2 | -13.9192 | -42.8783 | 2025-11-14 00:38:00 | METOP-C | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f6c0542-d5c2-3ece-b462-d2420e5346e8 | -2.4663 | -48.224098 | 2025-11-14 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507afb86-2c38-353d-9531-9848d2f6c4f8 | -6.9939 | -42.781898 | 2025-11-14 00:38:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9d0e4ed-91ca-3ffb-8149-2c796115cd17 | -6.4695 | -48.3727 | 2025-11-14 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 51836064-be93-341f-9eb5-1b6e317150ea | -6.6119 | -47.6395 | 2025-11-14 00:38:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6afcd6-0f35-37f8-b409-eec9c9d7202d | -3.7694 | -47.7458 | 2025-11-14 00:38:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bd5ec4-cf94-3528-a2e6-8fc8a1e9b74a | -6.4679 | -48.365799 | 2025-11-14 00:38:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
