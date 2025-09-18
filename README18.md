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
| 2de9d1e6-e5c9-38b7-9d1c-460acaacb552 | -14.42181 | -42.20668 | 2025-09-18 04:14:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ca57711-cab8-33a4-ac8f-7ba2abd81dcc | -7.09651 | -48.29648 | 2025-09-18 04:14:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da9690c6-95f0-3676-bfa3-f66d98867ca4 | -7.24589 | -46.61193 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82572dc0-7c30-32e9-ad18-63f6757d333f | -9.14522 | -44.87125 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a48d4fcd-cd8c-3b4d-b4a6-2fdaa8102f48 | -11.37598 | -50.84468 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fc8f10db-d1de-3704-8e00-84ac1b0eb953 | -11.17487 | -45.33044 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7fb8692-5604-3293-ac21-5768134ef66f | -7.79925 | -48.39015 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 446d07b5-5cd1-3e04-afad-c1e0440ae3f9 | -11.7093 | -50.77169 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1eec0c7-57b7-3957-a380-3cac51d50795 | -8.59472 | -45.73039 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5745d85b-88d3-3afb-88e6-4df5b819f6dc | -7.55 | -44.75486 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805bba78-8c84-3d83-ae5f-b093d69035db | -11.99378 | -46.71043 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51b4838c-2c6e-3795-a27d-96e032ef8f26 | -8.95051 | -45.52768 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fda8978f-186b-3867-a50f-9291f4583c24 | -11.23044 | -47.4281 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4f5a04c-8d92-3113-97fe-66ce8633027d | -9.74915 | -48.11954 | 2025-09-18 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64993841-92e4-382b-8769-af812d665310 | -8.95112 | -45.52396 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d452727-3e3f-3a01-a21e-f36604e29167 | -8.02715 | -45.6587 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbd5eade-0de2-37ea-9516-89b8c9e812f4 | -7.34995 | -44.58266 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82b25543-955f-3687-b8ff-d1b913ea1259 | -10.21746 | -44.98678 | 2025-09-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 629b77fe-3ac7-31e0-a68a-231fd6967b13 | -8.70236 | -46.37568 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdbcd3e4-81cb-3899-af3c-14f7ed9042bf | -10.64278 | -42.3108 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb202af6-4986-3a5c-9a71-ca18df9044d2 | -8.0078 | -45.79749 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85e0ef4f-d75e-3538-8bba-5e8bb7bf703e | -12.02242 | -46.73149 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42d0bfb6-7f19-3f70-8993-29c892acc7f8 | -12.40173 | -51.41801 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64c4bf4c-ef8c-31b7-9b26-47a4ee8995c7 | -7.85125 | -45.59973 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 113074f4-6100-3a44-be93-a9b6ed8b47ae | -7.69386 | -44.47337 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af624ca1-1b41-3e1c-8ab7-c749b494ea0c | -7.85719 | -45.58507 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88a6a3df-9a87-378f-a90d-7829caa3539c | -9.37206 | -45.37563 | 2025-09-18 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76efb354-565f-3669-9900-06e79083a265 | -11.18157 | -45.33153 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7827d81a-4154-39e4-bf69-ec0a726b240c | -7.52142 | -45.30009 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb05e1b1-d2bf-3d90-a577-9f9c45157a71 | -8.9426 | -44.50661 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2541cbee-dd42-337b-a167-a9adfbf3ac93 | -10.66805 | -46.4577 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb184974-6399-3410-833e-07fdd6da8813 | -12.49241 | -46.69323 | 2025-09-18 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62ba8851-d5dc-305a-a84f-cf16322ea708 | -7.27384 | -47.91054 | 2025-09-18 04:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 126171a4-476f-33cc-8c19-a52972ee45b3 | -11.12328 | -45.35153 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05f92d73-de85-30a8-87bb-b08647472686 | -7.93411 | -43.88441 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b6fd8e5-2fa8-364f-ae54-d4f98fab484e | -8.69949 | -46.37109 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ffade6d-55ab-3aec-912f-6f949fc27a09 | -9.72791 | -46.57461 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed936cd6-9ce2-3842-a252-ab48a4860639 | -12.00223 | -46.72397 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be62f26f-9006-3f8e-936c-07f241a2fce3 | -7.26907 | -47.91491 | 2025-09-18 04:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4509e111-177b-3c10-8969-5e51c3ce9d91 | -12.90532 | -44.66441 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 19afe434-9cb1-3d3e-b818-3118e23b8665 | -11.49821 | -43.61347 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 372a01f2-6df4-3ea2-b5e6-26b9e083bbef | -9.15018 | -44.88312 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f23cf82-c878-317b-acbd-bc95045e7d61 | -7.55058 | -44.75125 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c808d8c8-a123-3494-b9b4-a6e1b1781c66 | -7.54722 | -44.75069 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 595225ed-694f-3ebb-bca7-4e7a54a3b952 | -13.94734 | -43.9888 | 2025-09-18 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce773195-529e-352e-a3e7-104567de41b0 | -8.94203 | -44.51017 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1698e0d-f5d3-34c5-8c5f-a3881be7592a | -10.91424 | -47.84813 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5b49240-4041-385d-a5aa-d40536455545 | -13.62488 | -42.47741 | 2025-09-18 04:14:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bb561be-8b58-3972-a87b-287709ddaaab | -7.54152 | -44.76454 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 850a6dbd-af72-329e-84e5-2439eab09d6d | -7.99929 | -43.81675 | 2025-09-18 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57e43f80-c973-3293-ba96-721fec6689a2 | -14.59107 | -45.17118 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63e8adf2-eff5-38c0-bff8-da0a628348d1 | -7.61735 | -44.46458 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18c495cd-4553-3f7f-a075-8420a4a656b9 | -8.0026 | -43.81729 | 2025-09-18 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84cd2e39-25aa-37c8-ac8d-3339ea069ea5 | -14.46699 | -45.98893 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29788aad-3306-3802-84b2-8876b0ff6a18 | -9.06328 | -47.02231 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09e15f57-a7ef-3970-8b8f-fe42a8d71649 | -7.5344 | -45.24118 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c757bf9-ee2c-3d22-8dce-120356224fbb | -13.30064 | -42.51987 | 2025-09-18 04:14:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bb7f2a9a-3233-324b-a6b6-44e2edcb48eb | -10.68802 | -42.10382 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 79a28e9e-3af2-3229-a20f-dcb2b6fcf556 | -8.89411 | -46.13399 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f42a9db8-999e-3478-a7ad-0cce866e970e | -10.62939 | -46.22546 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51593b21-033f-3c23-914e-dba8a1354646 | -7.50727 | -44.34513 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1003ef91-1234-3dd2-bb9d-61904c21850a | -14.3152 | -45.15437 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 876e3851-a906-3b6c-883f-75cac6c58ddf | -7.63799 | -44.46424 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e81296-5c6e-33af-8e61-8a4841897708 | -11.36947 | -50.84658 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b838a9d2-c999-3d26-b24d-6e38cbfbec23 | -13.22335 | -43.51657 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3bdba95-2b24-32cb-b728-20da6b5372e3 | -11.59876 | -49.82511 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e7ce4b8-28b1-3548-9db9-00db17de2216 | -11.99791 | -46.7071 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5049006b-f50f-33b1-bfc3-e5a926204901 | -8.75384 | -46.15141 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbbab44b-3dc0-3522-a451-21bbbce649a8 | -8.59661 | -45.71886 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d941ca-2e22-39e4-b041-d056ca345b4d | -12.90752 | -44.672 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db16cffe-82be-330f-93ac-0840636ffee8 | -10.62268 | -46.45076 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebe5371a-a40a-3db0-a15d-4b0f0b5c5d79 | -12.093 | -44.8384 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec57a4a-fa98-3bfc-af18-57073826dce6 | -11.1107 | -45.35344 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49b13a9-aa53-3dd0-adac-2b562ce19f88 | -9.15201 | -46.96267 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 0e61fd49-06a2-345a-8751-05f5a55f03f6 | -9.03801 | -44.96772 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f02f02ab-6ef8-33d3-8868-a0c5ea52c08f | -12.17185 | -43.57891 | 2025-09-18 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d3f86fa-83c1-312d-afd3-c9bf28b4b3e4 | -7.51499 | -45.31825 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffbcef6a-8db0-3c46-8e98-14b85bd61950 | -11.24922 | -47.40511 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec5c5a87-2c49-3165-a4b1-5e5ad568a362 | -8.02964 | -49.84772 | 2025-09-18 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b0b2a0-3a16-3341-8615-b34e6ca3bd19 | -8.63253 | -45.30605 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b6aec21-23ae-32dc-9cf6-73dfe3165bca | -10.92401 | -47.83588 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 437be9ff-3c92-3f57-903b-3304efcf5e0b | -11.3739 | -50.83044 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 57730ea4-0a9c-3278-b658-638aed666ebf | -10.64205 | -46.44191 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd7ba9d3-a7b3-3a96-ac74-f09a189916d9 | -7.85854 | -46.10803 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01d093a7-dbbf-3420-8af8-03219b0aa99e | -14.27302 | -44.79759 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12073fc5-eaba-3d19-801f-7ccc01f3bb91 | -11.22755 | -47.42319 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21393e59-3b77-3d74-8f6d-598cedb775ee | -9.15563 | -46.96328 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 26d1cbd4-2b10-3e99-819e-da4658e417df | -12.07498 | -46.5647 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c617279-da96-3f25-9661-5ec143625466 | -10.63882 | -42.31398 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c46a692e-c269-3c25-b8d5-2320d8abbeaa | -9.18888 | -46.94231 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5ae9102a-ae22-3b5c-80be-2f0f8651ef5d | -9.16794 | -46.95641 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3d6fa325-59a7-331c-a417-5c3211d6317d | -8.88998 | -46.13729 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5882e663-8a35-31a3-aaef-59b38dd1ca56 | -11.03168 | -45.06075 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dd46721-bbde-3702-aace-3aba35a29280 | -7.32099 | -44.00118 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78a660ef-b323-3dcd-94e5-abdee12412c6 | -7.26485 | -44.91049 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec0ae6ab-4eeb-3b4d-af06-aa6c4a0821c8 | -7.59334 | -44.61429 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d475494-f62b-3c40-b6e8-7b8592311afd | -8.65664 | -46.43537 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d71c012b-080b-3186-bb10-f350c91f2146 | -12.40543 | -51.42345 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf1652c-e891-37dd-a18d-98fe632aad29 | -11.24049 | -47.39088 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36689434-2530-385d-9e01-3dbd4e0f17f8 | -12.90807 | -44.66847 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README19.md)
