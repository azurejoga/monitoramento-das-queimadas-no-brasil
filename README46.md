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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051deaaa-cfff-35b1-b239-2f371cd9b095 | -12.89613 | -45.17233 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0cecffaa-f909-36db-95b7-039ec29d4747 | -11.36045 | -44.9454 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58ea034d-d23d-3448-ad97-696b52a726ce | -12.68446 | -46.87728 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25359521-addb-3006-9b8a-6b55cc1a521d | -10.9714 | -49.56799 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8a45e5-b576-3269-96b0-e50160366420 | -14.58559 | -48.25017 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e98a619-e2b3-3c31-b2be-cabecc7741c2 | -16.18075 | -43.64918 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e605d6b3-a426-3f72-a7c1-5067fa7ceb08 | -14.77273 | -45.66819 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7639d1fc-4ebc-3d87-8a4c-600f16e719b3 | -12.99187 | -49.43932 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b840d6c-c6ae-3073-b582-8f77ae5a0537 | -11.98818 | -47.03756 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 574e4829-af38-34f1-b68f-b82aa8796827 | -11.66022 | -44.2914 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aaba691-5a3e-37b0-964d-117d1d1735a3 | -13.33819 | -47.28713 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0490da3-62fc-38ac-840a-5ad042b21cbe | -11.3687 | -44.94222 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 344e62bb-5ecd-368c-b643-a9a141d04aea | -10.75699 | -45.38892 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1091a659-fef8-3eaf-ac7e-6609206a78e1 | -12.95463 | -46.38546 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a12ee4c0-ddf4-365f-82b3-47b057dc85c6 | -13.5127 | -47.40117 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12cd2aef-40f7-388f-b810-b58195a2046b | -13.3423 | -47.28708 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d15a5b9-2374-3c3c-a3ec-703829eb7b41 | -15.22021 | -48.06448 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 572ea77a-515a-3506-9139-f5c0c8c80318 | -10.9058 | -45.75243 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dcad417a-e908-34da-8f93-d40d28032161 | -13.58453 | -47.31343 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57901942-ddc0-3e36-a31a-ad49367dc5b9 | -12.01554 | -47.07951 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76d3d460-cc11-3b96-aa6c-5b9c546edefb | -16.40611 | -43.72267 | 2025-09-28 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4435a64-4aca-3731-a33c-0a9e6696c5a6 | -11.98024 | -47.08127 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3901b353-ff27-342a-aeed-7f85ec085a1c | -14.84073 | -45.5716 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca061408-ad76-306c-b98f-7f4a1145aa4b | -12.01911 | -47.91298 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f9546ae-d152-3963-81c3-e01587441d88 | -12.00363 | -47.04862 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 129c1a36-8e4d-3ea5-89c6-ae00f8a68ca3 | -10.90702 | -45.75518 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bec39c6-8af5-3988-a4bb-0ccf4f418411 | -15.55025 | -47.89507 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11f14b79-559e-3b55-bd29-1a1926483557 | -15.90793 | -45.17967 | 2025-09-28 04:06:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1950b34-eb0b-3334-8d14-92cedcd28b5d | -11.44691 | -44.98159 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29ad3360-518f-3559-8c30-784ed0934b77 | -14.77114 | -45.67735 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd524115-369f-3e2d-a410-bdf9b83bfdf8 | -15.89201 | -46.22203 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff19678-b5ce-33ae-bd3f-c48ef1921b5b | -12.92587 | -45.17769 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ca7ed6-9804-301f-bdae-3c27bc951db0 | -15.48703 | -41.92802 | 2025-09-28 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 00294c9d-1403-38fb-8c15-0ce475f3ba16 | -13.62539 | -47.32658 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e0b9420-32d9-37f8-80eb-6a7a6046051f | -10.91339 | -45.73252 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c1f909f-fa17-3196-8f31-979d26ab05f3 | -11.42372 | -44.9589 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9dc158a3-9946-38e2-ae20-278fce5ebbf1 | -11.67105 | -44.29329 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b774062-d111-3a86-a1c0-e059cc39cddb | -11.37942 | -44.96933 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f00dc0fb-2665-3f69-af14-230d817f9e00 | -12.89846 | -45.15882 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b989e356-d4b4-3ebc-904c-7401495aded0 | -11.70551 | -44.42036 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39f833d5-ab21-3a15-9e35-9bcd58366ee7 | -11.39405 | -46.97232 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7feda7ef-ecb5-3f55-b863-faeea5c7a464 | -13.52532 | -47.40369 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b48784d-ab94-33f7-9513-2b3b0ebb64ef | -11.35893 | -44.95441 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac01558f-3cd2-3938-aa99-e9cf96217315 | -13.76298 | -47.87004 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd14ee6e-da83-35d0-8fb0-fe2f66c2f375 | -11.66079 | -45.33462 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa206a77-ee41-38c4-9c7b-6ba41da7b684 | -9.53969 | -50.78164 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cefcf624-ee18-3eb1-9257-bab98da866f9 | -14.5378 | -48.41331 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 401daa3c-2304-3cb7-b752-f81018368a5d | -12.00089 | -47.88594 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6a8878d-61e9-3029-8d5a-ebeeb054b715 | -11.42698 | -44.91722 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 052be02c-974f-3699-863a-60e8d59016d5 | -11.69026 | -44.40015 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d79c308c-954b-30b8-b274-0b99713f3df7 | -14.58325 | -48.26262 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9db5d9b0-fc2d-3466-a1aa-983322f6989a | -14.73034 | -46.83488 | 2025-09-28 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42ea2aa5-6139-36ca-86fe-49962d005f9b | -15.87911 | -46.22885 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 753b94d9-b882-3b8d-8e40-dd5f1e0808f4 | -13.78188 | -47.88871 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a9a3185-6541-3d95-bf21-51aceb86eb6b | -11.98575 | -47.89312 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff752d8e-4019-34fa-9493-4b170789d0da | -13.77192 | -47.88838 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92be2eea-5177-366b-950a-c82aeefa98b2 | -13.61579 | -48.07491 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5563a38-2d92-37a7-86e0-e48ebbdb8684 | -11.61634 | -44.41908 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb1caaae-d248-3458-a4f9-67e7559ad46d | -11.41025 | -46.955 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 158fe904-b5ba-3555-8962-45c395237c8f | -14.53688 | -48.41138 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a23bd0a-fef4-3bf4-b6be-ff09321d352c | -11.41658 | -44.91043 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c01a80-d8ad-352b-80fa-aa02465ac660 | -15.43198 | -48.21129 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 420613b4-95bc-3075-8e42-dbdb1ce64935 | -12.89536 | -45.17683 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 669a6c80-6c82-3292-9892-f8d5ed3150d3 | -11.36996 | -45.02399 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 709d8840-1252-3406-aef8-2ae5d4682696 | -13.61277 | -47.32463 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 258f3ed0-e530-332c-9c62-46df84572d45 | -14.54144 | -48.41842 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d01cb1d5-6433-359c-9299-4c47bbd99d95 | -15.70524 | -47.80475 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5ec721e-f543-3497-810c-b274dbb416ab | -12.37741 | -44.16272 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a658079-fbe5-32c2-900c-af589ee08f62 | -13.76225 | -47.86767 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11e39297-6226-37d6-903a-de78b9b81969 | -13.63207 | -48.06619 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95cbb2ad-f12c-32a9-a9c8-4d09f2f1640a | -15.31738 | -47.88868 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35511064-51c4-350e-89f5-335ce734a42a | -12.768 | -50.49595 | 2025-09-28 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e931063-2261-30f8-be14-57c48ec43ec7 | -11.98931 | -47.95008 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a332c43e-bfef-35c0-ba5f-b64e6921820f | -13.65263 | -48.07244 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d02bd0ab-36ad-3594-9841-9730f575d64c | -15.29373 | -49.48717 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6b9f1fb-b398-3f78-8a37-b75413bd9cc9 | -15.21515 | -48.06796 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4634c525-d6b3-3738-9157-6d779b4db870 | -15.0317 | -46.9687 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8e1153b-a858-3774-9fd6-d6c83d071c73 | -11.60979 | -44.41353 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6b6767c-e60e-3b54-ab0e-2a48074b5045 | -12.9082 | -45.14667 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f6bf4705-7403-3465-ba2c-aa7a1a2afa8d | -11.36112 | -44.96444 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9403e4a5-2118-3cf5-92b5-bfa91df303de | -10.96574 | -49.57002 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 771cc40b-fa49-3105-b6b7-6f76189551af | -13.77684 | -47.86773 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51721ab8-38e8-3277-bacd-2522f0e6ce97 | -12.38658 | -42.53322 | 2025-09-28 04:06:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 218a532c-9163-3807-8dfe-58347388129a | -15.27741 | -46.45385 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61f56739-0ff8-3bb1-b033-4cd0b83583b2 | -14.78819 | -45.6899 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 630743d4-c263-35c0-a191-363be6db4a90 | -12.88387 | -47.09165 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 203bade3-264b-3483-8ecd-fc956bc22dbe | -12.08057 | -47.26963 | 2025-09-28 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80c1cbed-d590-338e-b592-b2644d33957e | -11.51727 | -54.31596 | 2025-09-28 04:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0826b67-6eaf-3e97-a9c6-cc7d6335e89f | -13.28726 | -46.44355 | 2025-09-28 04:06:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17433629-bf2b-327f-8713-8060a2fdab0f | -14.77141 | -45.65374 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 510521bb-b453-3023-ab90-875004e39122 | -11.40165 | -46.9295 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5de5601-6929-3923-b1e7-ba1d0674017a | -11.40393 | -46.96598 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8eb91be-d580-3ab6-8ea8-ef3f5295b72a | -13.38326 | -47.92014 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e86a8637-d7de-39b4-9b87-aa84773bae74 | -15.09018 | -48.32995 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e91f1e9f-48ad-309b-9fa4-c4fc724344ce | -11.51412 | -46.95332 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 022f0444-7423-3c6d-b83b-d7c1298c6026 | -10.82142 | -45.38601 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df79dcdb-dd9d-3f8a-9c8a-9e7d7a5495ad | -12.69463 | -46.86818 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84e147e8-1f9b-3819-9c8f-44cbb5f8c8d2 | -15.33568 | -47.88407 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73cb6c90-e50b-3971-b74a-d17a5dea2bb9 | -10.91066 | -45.74803 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcb8284a-f9a0-3ff0-80a7-abbe57e3ea78 | -11.95441 | -47.88768 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README47.md)
