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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fdf2c4a-77a4-3a04-ba5d-78420c69948c | -15.35704 | -47.98152 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9bbd9477-4730-363d-9d94-65d5db691648 | -11.0249 | -45.58131 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c4226d8-cad1-3995-b974-76bfe77fb699 | -13.12154 | -43.84683 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8191c96f-5b4f-3e0c-90db-64ae301f9e11 | -9.30217 | -45.98488 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7bc888dc-de38-3ca7-aae2-8b5654ffa24d | -14.27476 | -45.86652 | 2025-10-05 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| da745067-f820-3a81-9666-8ebd2165c9e3 | -12.41275 | -51.10402 | 2025-10-05 00:33:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 7244fcb5-7094-3f43-9753-c9244a2e3115 | -14.87195 | -48.14531 | 2025-10-05 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 62d7fe76-6be1-3515-acce-283d3452b8ee | -11.09407 | -47.74094 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9292d9c5-51c7-3427-be38-bedc44f14ad5 | -11.91113 | -46.23326 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3acb4f07-2f29-3159-9707-24a37e9402a2 | -15.513 | -46.85138 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0f55f5e8-047c-3c26-8b9d-63ffa84bce44 | -14.88817 | -48.2646 | 2025-10-05 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a43206bc-1d4c-3b0e-84c4-4d55d0e395c3 | -13.25863 | -47.20715 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da919ed0-8924-386d-a8cc-305572e3ae8a | -11.70862 | -45.34799 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 403d58d6-04d4-3ecf-bb1f-562afaf3fb39 | -11.09534 | -47.74994 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c4a0db2b-6ad0-36ed-b6b4-bbf71fd92245 | -11.53764 | -47.68179 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f1e158ba-8ef8-3de0-932b-8a2b3a798858 | -13.86283 | -44.00226 | 2025-10-05 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| baaf50a5-9c2f-30b5-b028-60a4da7f1b17 | -11.12685 | -47.91027 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c42e628-4b65-35e2-a83b-2f8248c4c5e2 | -7.29205 | -39.25657 | 2025-10-05 00:33:00 | TERRA_M-M | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 251cad15-2955-34f6-b519-4d473d63785b | -13.23486 | -47.82552 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a3668a1-9775-3ddb-ae90-ae2d6bf163e5 | -9.06377 | -47.01857 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1541698a-5885-3c5f-b86f-c91b5e1a71b9 | -13.11951 | -43.83374 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d40745ed-6634-35c3-ae4c-1ba9a40af03a | -13.1528 | -47.96282 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1e64a69f-8025-3177-96e1-c5d5e2227fc8 | -15.44653 | -44.30029 | 2025-10-05 00:33:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8151a1ce-74fd-330f-8fa2-d00dc19e62c7 | -10.95225 | -51.001 | 2025-10-05 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2185666e-abfd-3fd4-bf5a-6e4d7350a6c0 | -15.98157 | -50.86384 | 2025-10-05 00:33:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 66c018b8-2ef3-31c1-a030-52792e4bcb9d | -8.93623 | -48.66344 | 2025-10-05 00:33:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4929fae9-d9e7-3d14-96cc-a87454504597 | -13.11268 | -47.86779 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a0cce342-164b-378a-bca9-3194505afc0f | -8.54978 | -46.31637 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| dec4491b-4a0a-3918-bdf5-ed1f3fc28903 | -14.94977 | -46.8435 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7def23bd-916e-32eb-a4e6-f1bdc85d7d47 | -12.97548 | -51.03829 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e395f753-9fcf-3e8a-ae2d-418364e378c1 | -13.14399 | -47.96412 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 49b5320d-80f1-348f-946a-a3ac66280944 | -11.10419 | -47.74865 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e57bda7a-89b0-3f9d-bce7-ca793d513f10 | -10.72971 | -47.64392 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c32fee80-5dca-3eaf-9e65-49c7d1aa61be | -8.55483 | -46.32053 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 16ab7d82-bad5-3c8c-911c-396314446cca | -14.79639 | -44.88948 | 2025-10-05 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d08ba055-6ad2-35ad-a55b-c1d2217adcda | -11.02735 | -45.57495 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dced6e2f-6968-3dd9-ac26-c25f7b389c03 | -12.59817 | -48.14531 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1f51639e-170f-39c2-8e5a-733fbae1baca | -8.53873 | -46.3073 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2d020e9d-1b77-3274-a408-4014f496ec30 | -11.69616 | -47.49837 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b3372e43-67c5-3a93-ae11-b9c4166a7421 | -14.33217 | -47.69978 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f1790503-5692-3360-ad73-1e9267863199 | -8.79062 | -40.55571 | 2025-10-05 00:33:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 33.8 |
| 80fca705-e4cc-3db4-82e1-0c3be61af541 | -13.58576 | -48.16932 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7f0eb54b-e88d-32ce-b337-6d0c0064b623 | -13.09622 | -47.83071 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d16f9c2c-d015-3348-9eb4-7e26d9765d83 | -11.00117 | -46.5131 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ca711af1-065c-3a00-aa1d-472c38612bf2 | -12.58921 | -48.16199 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38e0d16b-4260-38b8-beaf-b5047668fbfc | -10.96185 | -50.99969 | 2025-10-05 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f7521932-e1eb-3cb7-b2e5-85426f18b767 | -10.74627 | -47.89017 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51eeb913-c2cf-3493-ab41-0e9bb0959ce8 | -11.82623 | -45.10025 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 32aa97ff-10e3-3026-853b-98987b336b49 | -13.29805 | -47.61678 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| af57a03e-0c80-3250-9e10-63e962ba3184 | -13.62868 | -48.68373 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a898a2a6-d710-39ba-8b54-51c10608e503 | -13.26128 | -47.82161 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 15e3a117-7e04-39cc-9521-130d987b58bd | -13.73078 | -48.08041 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8511ec00-9684-3ee7-9075-32ac78ac855e | -12.38411 | -44.45192 | 2025-10-05 00:33:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| fa99a48e-9ae3-3746-b57c-a321cf5e0938 | -10.50891 | -51.85103 | 2025-10-05 00:33:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9f86fd10-3d84-3249-b666-da0222c5c131 | -10.06794 | -48.18434 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8033938-108f-39c7-b0c0-446331cadb8f | -8.54526 | -46.28473 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 130ef467-19be-3ac7-afbb-71b84b40b08f | -9.2941 | -45.99695 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 715cf55e-976d-367b-af58-20373e5110e7 | -13.13437 | -50.92385 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 54113104-e08b-3285-af95-6e943706daa0 | -11.80368 | -46.83073 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8cd1076d-2541-3101-8e4f-7301148f2bb9 | -15.16958 | -43.63914 | 2025-10-05 00:33:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 33.9 |
| c72c298b-9438-3ab0-8533-01aa0cb85002 | -12.39161 | -51.09536 | 2025-10-05 00:33:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 524597f1-fd26-3175-83ce-a8cf4da0f36e | -13.33067 | -47.78666 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be6e3950-bd36-38bb-a868-e2fa144c86e8 | -13.67956 | -47.30804 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 76834f0f-0f88-3056-ab45-2639eb875893 | -10.05093 | -49.19934 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9f407e58-d2a3-3210-94cf-6b1336f16d5a | -12.30857 | -55.13972 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 967634a0-df73-3b12-9c22-c60176d85aa8 | -12.88824 | -47.32389 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c0428bf4-3e14-3368-8e02-eb6ccfcbe50a | -15.38993 | -47.95789 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b8283546-653c-3129-8842-150d699238bd | -11.68602 | -47.49072 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5219578-2eb9-3bab-8d31-689f69288576 | -13.23361 | -47.81652 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c72c698a-4b89-3d12-9e4b-edeca12b0cbb | -13.68087 | -47.31724 | 2025-10-05 00:33:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f654fdd-29f4-3ab4-a5c4-0071d4f8db67 | -9.05462 | -47.01992 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 396d6db4-d2e4-3dd6-9af3-0e689cf66a96 | -13.30363 | -48.12787 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2f91973a-eb65-365a-aae4-7029e6b396ac | -5.06084 | -40.46053 | 2025-10-05 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 0ada3a6e-4fa9-3b78-828c-f08020eb215e | -5.34355 | -45.30395 | 2025-10-05 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 44f8c288-3085-3437-971f-46529cbc84e9 | -5.76991 | -45.77958 | 2025-10-05 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d79994a1-4805-3311-8984-6872f1c434c0 | -4.56846 | -48.61143 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b93c8edb-6145-377e-a74d-3d9551785117 | -2.14567 | -53.63609 | 2025-10-05 00:35:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 28273430-6460-3bb2-a01a-2d5ec00779b5 | -6.02015 | -45.40945 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| be792ca8-2815-3253-9aa2-d9fd121ffcb1 | -6.00882 | -42.51476 | 2025-10-05 00:35:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 7132cc22-39cb-30df-8487-2108930f3e9c | -6.64591 | -51.12211 | 2025-10-05 00:35:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86c5733d-6b1d-3a01-aa96-8e6788a1c6af | -8.55615 | -47.66346 | 2025-10-05 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a287a1be-62e9-33e4-af8d-22d6657d1cef | -6.40245 | -42.68637 | 2025-10-05 00:35:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 621a78d5-c64f-3bef-baf3-ab0d741b6916 | -6.99029 | -44.21405 | 2025-10-05 00:35:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dcde935e-ee9e-3148-a508-dc0e260f8b5a | -8.40899 | -47.01947 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| feac5cc2-8529-3f4c-b215-9f98926af335 | -8.5408 | -47.68449 | 2025-10-05 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 53e8493b-124c-3264-b91d-8f87b4159577 | -4.45016 | -43.22739 | 2025-10-05 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 45621f35-ecc1-3126-a1d4-52030fe2c0d2 | -6.67314 | -42.38862 | 2025-10-05 00:35:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| ab29cf30-03d7-31c4-8fa4-b4a802859010 | -2.68322 | -48.38735 | 2025-10-05 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c59ad1b2-83e6-356e-8468-dc691a9a001d | -5.18766 | -46.21398 | 2025-10-05 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 95b00ecb-8886-3386-a2f6-887f477e9399 | -7.78511 | -44.52296 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1938a689-4864-3a18-ab28-ed6308d78d37 | -6.55874 | -44.17086 | 2025-10-05 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 992f15f5-eefa-3405-8eeb-ba59fd13ba28 | -4.65675 | -43.20393 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fd2f2f99-c712-3a4e-91a8-7b174fa7f3a8 | -7.31739 | -45.99686 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e25eec66-6d8a-3b8f-9528-dcd906176628 | -3.39905 | -50.27531 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8b91a3b2-5f82-3648-aa7e-03976b877926 | -5.97587 | -44.35843 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 174a8647-0c23-3404-b6b2-7f2300cf3300 | -3.78256 | -53.93866 | 2025-10-05 00:35:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2a1aa2b1-2f47-3540-b3e4-d4b6584dc2d8 | -6.45835 | -44.5846 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 193d1d4e-3ab0-32e4-bfda-bfd23a9f0bfc | -6.69355 | -41.96072 | 2025-10-05 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 59dec7d8-0ba5-32a8-8394-9958159d0032 | -8.21988 | -49.13987 | 2025-10-05 00:35:00 | TERRA_M-M | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 85efbef1-2813-34fa-8dd1-014bbb87b351 | -8.51609 | -50.03478 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README11.md)
