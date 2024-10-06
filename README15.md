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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fee85281-a7ca-3167-b963-964bc93a099b | -21.73854 | -45.62305 | 2024-10-06 00:50:00 | TERRA_M-M | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| bfe186f8-e91d-331a-9a81-15070393f22d | -21.73725 | -45.61298 | 2024-10-06 00:50:00 | TERRA_M-M | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 27fb6fb0-c1d7-31e5-b904-570fda0c9a90 | -21.59378 | -47.9424 | 2024-10-06 00:50:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2b7e5475-940a-31a5-a519-9b331567c219 | -21.58341 | -47.9438 | 2024-10-06 00:50:00 | TERRA_M-M | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 70d04bac-effc-3193-955e-bfa1d8e63c32 | -21.39994 | -44.2606 | 2024-10-06 00:50:00 | TERRA_M-M | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 828ea271-58ad-3f8f-bde1-349a270ad729 | -21.37706 | -48.63489 | 2024-10-06 00:50:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0c2338ab-c9a2-39bc-9b30-03a2d5fae804 | -21.36621 | -48.6363 | 2024-10-06 00:50:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 45644fa0-9d7d-39b9-bb86-21c63e8c6ad8 | -21.31067 | -47.60847 | 2024-10-06 00:50:00 | TERRA_M-M | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 91be0b38-189f-3fc6-be60-0f71c4fd6076 | -21.29473 | -48.81546 | 2024-10-06 00:50:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 70b6e105-97a5-3f37-bd6f-2e08a882c074 | -21.18199 | -45.58032 | 2024-10-06 00:50:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 93d0dd1f-540c-3b26-9b82-0e82dc849e7b | -21.08288 | -45.73008 | 2024-10-06 00:50:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85cee0e8-cd8d-3b27-875c-c0e50327a757 | -21.08156 | -45.72004 | 2024-10-06 00:50:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 31524a74-c5db-395a-9567-c54556f6c3a7 | -20.02629 | -45.66376 | 2024-10-06 00:50:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f407a3ce-cfa9-365a-a38f-1aa34dec27ef | -20.02499 | -45.65398 | 2024-10-06 00:50:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 79db36e0-53e5-3107-9d91-fcb3601ae918 | -19.91703 | -44.52457 | 2024-10-06 00:50:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 35bcf2ba-4073-3f4b-9ec5-a0c1a7390ccd | -19.91573 | -44.51521 | 2024-10-06 00:50:00 | TERRA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 58cec403-3caa-34e8-9651-85e4cd9f0b23 | -19.86493 | -47.85383 | 2024-10-06 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6b1474b-fe5f-3281-9591-4d35936fb34b | -19.85636 | -47.86743 | 2024-10-06 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b10dded5-748e-3085-9952-190ffab1419b | -19.85486 | -47.85512 | 2024-10-06 00:50:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0c8cf5ac-a3ad-3299-b7b3-3fcecb005afc | -19.83579 | -44.46095 | 2024-10-06 00:50:00 | TERRA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8c80243-b5b9-3d80-891e-4fda203b9fa8 | -19.81314 | -43.85032 | 2024-10-06 00:50:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f9770ff-5154-3dfb-8cfa-c1f086a9efae | -19.6169 | -46.26049 | 2024-10-06 00:50:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 85b6e602-2816-3967-b19f-b0a31193d361 | -19.09309 | -48.19978 | 2024-10-06 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| af42c1b6-06cd-38bb-a68e-7de9546537f2 | -19.06923 | -47.00761 | 2024-10-06 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ba5f6b76-b995-3a75-b42f-08f67f7ea449 | -18.75598 | -44.19065 | 2024-10-06 00:50:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 66683bc3-3b0c-38fa-b728-9012b6aa12d9 | -18.75465 | -44.18129 | 2024-10-06 00:50:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f06572c5-f61e-36c7-b038-9b6e0f60a97c | -18.56716 | -43.83365 | 2024-10-06 00:50:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ae79e633-cc24-3e01-8e10-3cb1703d0e8c | -18.55961 | -43.84462 | 2024-10-06 00:50:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 783a8be7-6d56-37c5-bf8c-179639609e75 | -18.55824 | -43.83514 | 2024-10-06 00:50:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2a3ac1ca-a59e-3bd7-9997-19fc73304b0f | -18.53711 | -44.07515 | 2024-10-06 00:50:00 | TERRA_M-M | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f763e103-ad36-33b1-a343-4cb559afe32e | -18.47595 | -47.40017 | 2024-10-06 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fc6bec7e-ddbf-3b2e-bea2-db041fa0f484 | -18.47458 | -47.38911 | 2024-10-06 00:50:00 | TERRA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 07dfef00-b5d1-34b4-b883-9ec96980cb77 | -17.74713 | -43.83704 | 2024-10-06 00:50:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd3c9814-e1d2-39c7-a171-8bd106f67a77 | -17.73953 | -43.84786 | 2024-10-06 00:50:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60b80c14-c750-3120-b38c-66e17bd0b8d9 | -17.73817 | -43.83849 | 2024-10-06 00:50:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 56818e88-bb6a-39c1-945a-9f69f78bcc86 | -17.65108 | -46.40098 | 2024-10-06 00:50:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 40bb44ba-6a81-3819-992d-62dbde935cb0 | -17.64678 | -44.42199 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a3eb2ae4-bd51-3929-9280-9dc4ed1a4315 | -17.64546 | -44.41269 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9b77678-0465-3b3a-a0ba-ce53a6a61127 | -17.63792 | -44.4234 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 072aa208-b3a2-3039-87e6-49f899b0f7ec | -17.63659 | -44.41408 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9151264b-b604-39bd-b01e-0d843ce868c2 | -17.63527 | -44.40477 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e79367a0-f89c-3c7c-9dcb-dee69721d632 | -17.63373 | -46.96945 | 2024-10-06 00:50:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08bb4b5c-98ca-3838-a58e-cc061f18a631 | -17.62905 | -44.42479 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d37f3688-fe14-3206-818d-c0536752bbd6 | -17.62772 | -44.41548 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6bac08e1-9044-39e6-899a-0170534d3088 | -17.62308 | -46.96042 | 2024-10-06 00:50:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8b1c102e-fa76-3d53-b557-62830aa59e2c | -17.61885 | -44.41686 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 3d99c797-d351-3054-8548-cf4fe5ea6227 | -17.61752 | -44.40756 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3938622-defd-30d4-bc1d-8586876906c8 | -17.60998 | -44.41825 | 2024-10-06 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ea4c38b9-e2c0-32b2-a8bb-b771faa24555 | -17.58572 | -44.51363 | 2024-10-06 00:50:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7c552e61-c998-3582-8dca-8380b2f5d91c | -17.58066 | -46.92488 | 2024-10-06 00:50:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8cdf4d3d-684d-3cd7-9821-0d2a1d6d2ff4 | -17.38738 | -42.65666 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 85eab52d-d65e-3b0f-bc25-fc09b971a5ce | -17.38579 | -42.64614 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 05d28ff0-ee9c-3a89-9b3c-8272e87d8af2 | -17.37958 | -42.66872 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 80311924-acc1-3a55-a352-e8176133ff4c | -17.37798 | -42.6582 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| a9d6d4aa-5d1f-3ff4-88d8-0b6d53e5929e | -17.37018 | -42.67029 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5aeb6528-436e-3aba-b29f-d7eb6d1af8c7 | -17.36857 | -42.65976 | 2024-10-06 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 01172c86-2510-3a43-9aa9-632e06eeb0c5 | -16.99579 | -47.08185 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44d7e979-1050-3c63-a919-a123913b4112 | -16.96386 | -47.1281 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5e26eff8-3156-3790-954d-0e388b6fff55 | -16.95691 | -47.1246 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7263fadb-0883-37a2-a37f-e29f7b866de7 | -16.94761 | -47.12597 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97358870-17e0-3ff0-8e4f-1f3d7f11a6a7 | -16.9157 | -47.17229 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 51e165cd-b1eb-3d41-8df9-da2315239d67 | -16.91437 | -47.16199 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a16a124e-ce86-3a9f-b868-dc5cb849d0ff | -16.90637 | -47.17355 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd7ecfd3-14f8-3f1a-922f-073d65877d95 | -16.90505 | -47.16331 | 2024-10-06 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f4cd55ac-c075-3ebb-a098-6274fecb12e9 | -16.32702 | -51.29475 | 2024-10-06 00:50:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1a4d200d-1a20-3ce0-8d3c-3c8bb2e862c4 | -16.32478 | -51.275 | 2024-10-06 00:50:00 | TERRA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3668c6f1-0fe8-3ed9-8139-7af0321ba2e8 | -16.11747 | -50.4702 | 2024-10-06 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d9bb12ef-94b9-3bdd-b3f2-33c6557c63b1 | -16.07861 | -50.23348 | 2024-10-06 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 801ac9df-a123-32d3-ac3d-9cfd66469d1e | -15.95417 | -43.36616 | 2024-10-06 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b42fc51-d88b-3ead-899e-1ff5da175e38 | -15.95268 | -43.35609 | 2024-10-06 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf176917-dbbb-30ea-899f-c7523afa4e13 | -15.43298 | -47.70573 | 2024-10-06 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| addfcbaa-0264-3c50-b8bc-446d98f7dca7 | -15.40202 | -47.68861 | 2024-10-06 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4afb246f-4d11-3b95-a7d9-83da5151675b | -15.26329 | -41.77805 | 2024-10-06 00:50:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 170f61e0-3de9-3d5a-bf86-144012389afe | -15.13059 | -47.0858 | 2024-10-06 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a714c9b9-fbc6-3470-a3aa-02f170a182e8 | -15.12145 | -47.0871 | 2024-10-06 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b21d3fd5-d71a-3223-af53-6a8094ed44ad | -14.84534 | -44.23291 | 2024-10-06 00:50:00 | TERRA_M-M | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b2280cd-624f-3fcd-9c9a-3c8248374401 | -14.7733 | -48.06053 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6d8ce942-dacc-33e8-b433-018003743e08 | -14.76242 | -48.05144 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c2c96067-0888-37bb-b752-96102fa26292 | -14.69881 | -45.13843 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a05602c3-4e7c-381c-a74e-a7b946221574 | -14.69752 | -45.12932 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aeafc8f1-6cfc-3e25-a37a-8ff10b7dde37 | -14.65552 | -41.96708 | 2024-10-06 00:50:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d92ba2c2-cad6-3961-9ba3-15e2124bbe08 | -14.56627 | -48.8209 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 34752796-d3c3-3543-b8c4-d4ec85c5175e | -14.5578 | -48.83406 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b2cc555a-b097-38dd-a53e-11fa70ac8cb0 | -14.55632 | -48.82235 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 17a882bb-82c7-346e-9879-1da694ac8a8a | -14.55483 | -48.81051 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5dfe1792-e045-370f-b10b-f0d37f6fd20b | -14.55335 | -48.79881 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5fb5091f-36d7-3c2f-bb39-29b6ad417cc3 | -14.55194 | -48.7876 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 15970c1a-c1d5-3de6-aaf7-a04b5cb983e6 | -14.5464 | -48.82398 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a182680a-768f-3035-904a-cfbfd23ff146 | -14.54342 | -48.80022 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bd500a81-009c-3c53-ae57-fee687993ddc | -14.54198 | -48.78879 | 2024-10-06 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f2e7fdc-859a-358b-8929-73a09afca847 | -14.49021 | -44.96741 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a137092-2eee-39d6-9a71-5d77e430effa | -14.4889 | -44.95821 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f952ebae-c77e-3ebe-b02c-fb063bd8a692 | -14.42979 | -43.78694 | 2024-10-06 00:50:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ea69809f-a33d-3ad7-bc3c-ea929462d788 | -14.29698 | -44.65028 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 481cdd9d-3457-38ee-b615-2e47660bf7b9 | -14.19895 | -46.45285 | 2024-10-06 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8382cd7f-1074-34ed-ac56-83460f1d832c | -14.089 | -45.5801 | 2024-10-06 00:50:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 961d841d-b3b0-3df7-ba8d-e981a2fd9e25 | -14.08773 | -45.57103 | 2024-10-06 00:50:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35c39e95-efe5-3fac-b5e3-1fe118308189 | -14.0864 | -45.49718 | 2024-10-06 00:50:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cea110b7-183b-34ad-80d0-b8829483c288 | -14.0798 | -44.48553 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a4f181f-85d3-33d3-ad4a-f68695f442b6 | -14.07844 | -44.47611 | 2024-10-06 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README16.md)
