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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82cbdfa8-3e6f-384a-91cf-7ac5e6526a5e | -19.82511 | -43.79582 | 2024-10-08 00:33:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b461a226-d682-3444-b284-67d812e0e77b | -19.82127 | -43.8507 | 2024-10-08 00:33:00 | TERRA_M-M | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 31729c6b-0683-34a5-80f2-a42676853a77 | -19.80621 | -41.9171 | 2024-10-08 00:33:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 57439ff3-5a75-34b7-bb4e-5b0a7bbb634b | -19.46328 | -41.67279 | 2024-10-08 00:33:00 | TERRA_M-M | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f2789287-e5cb-31b6-b4db-d50bf514bd8f | -19.43185 | -41.16052 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| a2151533-b6ca-3151-b3e3-2b3f39526fd8 | -19.43056 | -41.15088 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 4ab92aad-af6a-3507-9d7e-f4fdc0ab0f96 | -19.42412 | -41.17147 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 029f2835-611c-3d83-8ad4-97b3017f7480 | -19.42285 | -41.16192 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.5 |
| 81ddab7d-6591-32e4-a329-d7569c29d71f | -19.42157 | -41.15229 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| fa0ad12d-5fa2-37a2-86a1-0267c11b1930 | -19.41512 | -41.1729 | 2024-10-08 00:33:00 | TERRA_M-M | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 64cf188b-4f3a-3d85-85e1-88be1a2cc9bc | -19.27585 | -46.12203 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 364db398-8d69-3695-a40a-89f32862c06f | -19.26923 | -46.13538 | 2024-10-08 00:33:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 202d7234-1ba2-3451-a43b-394d40589a50 | -19.26726 | -46.11652 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| c53dcd0c-c67a-3047-b43b-ff75e3e95b6c | -19.26571 | -46.14216 | 2024-10-08 00:33:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 08ad3a72-3067-3036-89e4-9cc61f39b8a7 | -19.26366 | -46.12375 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ccfc6010-4148-3c09-ac88-bca08bb50451 | -19.14018 | -42.71839 | 2024-10-08 00:33:00 | TERRA_M-M | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| fbedc436-1fed-3a0a-a7dd-9078de6f09e1 | -19.0061 | -50.25664 | 2024-10-08 00:33:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e42dcffd-48e5-3f53-8a23-6eeda115d455 | -19.00087 | -50.26225 | 2024-10-08 00:33:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ab9456ac-8cac-32bb-ad1e-ce0e3a41d725 | -18.99742 | -50.22338 | 2024-10-08 00:33:00 | TERRA_M-M | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1927080a-7268-335b-be12-322bc7e175aa | -18.63959 | -42.77355 | 2024-10-08 00:33:00 | TERRA_M-M | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 69bdacf3-eeb5-3391-9425-b3d2b773d9c9 | -18.56536 | -42.41443 | 2024-10-08 00:33:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 9457976c-73a6-31c1-b0fc-d2d68670f108 | -18.56404 | -42.40401 | 2024-10-08 00:33:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| afb028c9-a419-3b8a-9f72-dd4d15249c91 | -18.25593 | -39.90445 | 2024-10-08 00:33:00 | TERRA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4e1737ae-53f6-38fd-b1d0-ef9bab48faa3 | -18.18968 | -42.61687 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d7974bed-8866-3862-83da-b488a4efc97d | -18.18164 | -43.01311 | 2024-10-08 00:33:00 | TERRA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3e4ba7dc-0512-3cc6-92af-b6b0d55b09b2 | -18.10454 | -45.07342 | 2024-10-08 00:33:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c6ed1968-00b6-35fd-bf92-e725d2c8325f | -18.05834 | -42.1125 | 2024-10-08 00:33:00 | TERRA_M-M | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| af94603f-c91b-3a8c-8651-d2112baff093 | -17.87143 | -42.73339 | 2024-10-08 00:33:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| ff6e3330-a6fc-3b41-b00f-c02f7cb3fc0f | -17.802 | -44.42393 | 2024-10-08 00:33:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 27100d4e-cf9b-37ad-acfe-f70c9d1f297e | -17.71406 | -40.77038 | 2024-10-08 00:33:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a41e1008-46fa-34bc-8273-ccecfb9573cc | -17.69955 | -42.03519 | 2024-10-08 00:33:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f6ccc6d4-b0ec-3394-b83c-3fad7aad1ba3 | -17.65807 | -43.89605 | 2024-10-08 00:33:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| d9e1a96e-cf3d-3ed2-bf0b-986631a17648 | -17.60968 | -43.25983 | 2024-10-08 00:33:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ab648ec-4bf0-3d96-8476-39ad67bff84a | -17.58773 | -43.73671 | 2024-10-08 00:33:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0258dc91-b605-3ff8-a811-6b71bfd38af7 | -17.58489 | -43.71383 | 2024-10-08 00:33:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48ce1833-ff0f-3a79-afdf-e76c3cf87bbf | -17.20506 | -39.51661 | 2024-10-08 00:33:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 635d80b0-b15f-3a8c-8cf0-8dd3d222d1e0 | -17.20369 | -39.50709 | 2024-10-08 00:33:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| a15ea84d-6840-3f8f-90f7-eccff412b6c1 | -16.3046 | -42.05288 | 2024-10-08 00:33:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7c65432d-3ad1-39b2-a8b4-209f04476f4d | -16.30334 | -42.04332 | 2024-10-08 00:33:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 9a677d69-fc47-36c9-b9c3-0ed243898a04 | -16.09686 | -50.22523 | 2024-10-08 00:33:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 6fdce6fa-f104-3c97-aa24-4ffe2dc167a6 | -16.09344 | -50.19034 | 2024-10-08 00:33:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 62e865c2-6d9b-3081-9d7f-860d69876227 | -16.08425 | -50.19551 | 2024-10-08 00:33:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 1e160a36-1705-39d4-859d-fb0dc7b535a2 | -15.76959 | -49.97723 | 2024-10-08 00:33:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f2489c84-bf66-3275-b3ce-b270399ef9e4 | -15.75912 | -49.98317 | 2024-10-08 00:33:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c59434da-28ac-3d4f-908a-b2e499035449 | -14.96672 | -41.88738 | 2024-10-08 00:33:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| c0e9f074-84fd-336b-acdc-42be72b52193 | -14.95772 | -42.36486 | 2024-10-08 00:33:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a6addde9-af9a-3a09-95d9-d37c3d2150fe | -14.79723 | -50.77618 | 2024-10-08 00:33:00 | TERRA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 440abf40-e08e-300c-9273-b30adc25b439 | -14.79079 | -50.78223 | 2024-10-08 00:33:00 | TERRA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| b34209b1-9b4d-31d5-b066-7949bfcff35d | -14.57426 | -42.31898 | 2024-10-08 00:33:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 66d43f53-24b6-381c-bb71-f07516043406 | -14.53741 | -43.22802 | 2024-10-08 00:33:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3202d27c-253e-3f94-9964-b891eba98d33 | -14.53609 | -43.21782 | 2024-10-08 00:33:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e96383f8-a4dc-3152-bf21-afa3b78175ec | -14.51184 | -42.46923 | 2024-10-08 00:33:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 6407c141-5c4c-3102-9ef7-eae3e4f3676a | -14.42568 | -43.79057 | 2024-10-08 00:33:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2c54a787-542e-3a97-9e03-0f79222deb1e | -14.1588 | -45.55527 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 58f12e6c-3c1a-3b65-97f0-45c679266aaa | -14.14538 | -44.40007 | 2024-10-08 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4dbe6a27-691f-3e27-b6f3-662449b876c4 | -14.11795 | -44.10309 | 2024-10-08 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5510e762-19d0-3ab7-a1d9-40f7fc474801 | -14.10946 | -44.0364 | 2024-10-08 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 603706a0-6cba-3c49-bad9-f27bff3199f2 | -14.0625 | -45.51811 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 7d5e1efc-fc04-3b5d-88d2-a0face4e96bb | -14.06077 | -45.50428 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a990060-e3f6-35d3-b7a5-150fdd4958cb | -14.05172 | -45.51943 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7081d901-208a-3891-a20d-19958f18b6e9 | -14.01557 | -42.47422 | 2024-10-08 00:33:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b94614e7-de01-3aec-b963-63299f15a9cd | -13.94939 | -44.6244 | 2024-10-08 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 078de2ce-c0f4-3a13-b5a1-959d7f1d5f02 | -13.91464 | -44.59258 | 2024-10-08 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d27eee1c-56ca-379f-a6d7-50ffe9b654a1 | -13.75815 | -44.00698 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b3e1ca46-6c3d-3c2d-a5e9-74fe185b266b | -13.58539 | -43.79223 | 2024-10-08 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cefdca9c-0b4f-3db6-9a56-f1ec2364564b | -13.52442 | -44.40929 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 71cfece7-ae50-38a8-8aa2-7905ec194a01 | -13.50037 | -44.37791 | 2024-10-08 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 13f91bf1-15a3-3688-9608-fd83fdf5d4c5 | -13.48233 | -43.66835 | 2024-10-08 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 109fab7b-5737-330a-88e8-daca6f8ca40b | -13.47516 | -42.49283 | 2024-10-08 00:33:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6b0f5aeb-1849-316c-8055-9529d00b3047 | -13.47389 | -42.48345 | 2024-10-08 00:33:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 1df4c368-732c-362c-9d42-86af3c675b24 | -13.42654 | -43.79935 | 2024-10-08 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89714816-9f6d-3689-9ba8-d41f8402101e | -13.41703 | -43.80069 | 2024-10-08 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 1c5d2a10-b67f-3baa-a50d-68c9089d6f6a | -5.47644 | -44.26149 | 2024-10-08 00:35:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1e4854b6-7357-3b3d-ba09-b51a90eabc7b | -5.45919 | -48.9105 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0337a786-5257-31e0-983b-db3f050d3bb6 | -5.43256 | -45.47859 | 2024-10-08 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c70fe67-4bb3-326f-b9ff-b4a34371723b | -5.39622 | -44.9578 | 2024-10-08 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a3ed6449-3260-3816-8e1d-8d521082a886 | -5.39491 | -44.94813 | 2024-10-08 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 83b1f189-02fb-30c9-a15f-dfbb4b585bd4 | -5.27887 | -45.38032 | 2024-10-08 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3c998ad-89f6-33d8-b6ad-56d259f103fd | -5.27297 | -45.12682 | 2024-10-08 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e12db681-057c-3996-9d2f-4a1b6753bd33 | -5.27163 | -45.11703 | 2024-10-08 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d71164f1-4186-3034-a38c-b9a9cb9f7203 | -5.17168 | -44.66022 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94380fbf-d6b2-3d7d-b79c-ef4bd10082a2 | -5.10243 | -46.19323 | 2024-10-08 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b82b2db5-5e6a-3c3e-a0a1-b63cd1a4b86f | -5.06872 | -48.44801 | 2024-10-08 00:35:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5097517a-96d9-35b5-aca8-64a124e2531c | -5.01282 | -49.60287 | 2024-10-08 00:35:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 5700015f-ce30-3c11-ae8b-7978a2f8d052 | -5.01025 | -49.58309 | 2024-10-08 00:35:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 2edf835f-0265-3901-b5ba-033bbdca23d4 | -4.97483 | -48.89588 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b5f4057e-efd4-3eba-967e-a42f331219da | -4.92817 | -45.65219 | 2024-10-08 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1012f37b-4cd5-3118-bfca-2a742e478e3e | -4.9261 | -46.78162 | 2024-10-08 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dea06674-b61c-3971-8f2d-38a30eb5f69c | -4.92446 | -46.76949 | 2024-10-08 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 44fcc975-397e-3b07-bd9a-b379b32221b5 | -4.65397 | -44.37572 | 2024-10-08 00:35:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b0e12a53-d7f9-359d-81b6-b9f483c1d6f2 | -4.46994 | -45.91175 | 2024-10-08 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c2d3a34c-7103-3d05-b102-ac797301f0db | -4.39974 | -48.69556 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 0f648921-9fd7-3764-966b-a1af6ebcb031 | -4.39339 | -48.70279 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 4d8e1270-f0b3-3440-86d6-b75af8e4c26d | -4.39116 | -48.68646 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4c265f66-06ac-32da-89ae-0751d09220b0 | -4.36287 | -48.23214 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e1e14c2d-d31a-39bd-86af-bc416e9a2086 | -4.36085 | -48.21686 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 779c6080-6532-3738-b218-31561e71b202 | -4.31546 | -47.7058 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| cc037783-8b15-3419-92f5-75966daeffa9 | -3.15237 | -45.04413 | 2024-10-08 00:35:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a94248f-6cef-314d-a339-e2b7f36b382c | -4.27671 | -46.28136 | 2024-10-08 00:35:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 36a59851-3d28-3cc4-b769-6bbeb8065a94 | -4.26687 | -46.28269 | 2024-10-08 00:35:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README10.md)
