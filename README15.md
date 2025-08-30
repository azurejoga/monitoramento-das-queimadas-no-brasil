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
| 7e911eba-e806-34f9-bbfb-ebfaada48824 | -13.35014 | -46.88346 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 043de227-1f9a-351b-8685-1c57d908521b | -14.00134 | -44.59699 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f10557da-0094-3414-bb45-5cc45aa91b94 | -13.19033 | -45.28761 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77f080d3-dbea-3d81-a21a-4e9d494ee3cf | -15.30861 | -46.09816 | 2025-08-30 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 010bb205-a8f0-3d5e-82cb-2f0157c87e5d | -13.40561 | -46.95222 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1f35e88-6848-3374-8e93-0f41bd1c42ba | -13.65765 | -46.92307 | 2025-08-30 03:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8da6de5c-703a-30f9-8244-76956d19d212 | -14.03758 | -44.50866 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08971882-ff24-3e67-8169-c12b51d99bce | -13.99645 | -44.59146 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bc404156-ca65-3500-9a0b-426a84cf22ae | -20.08607 | -48.27235 | 2025-08-30 03:32:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2099c54-f243-32b8-b099-d845b56dccd8 | -17.45074 | -44.48824 | 2025-08-30 03:32:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b5b36af-b867-308c-a557-fc576fe6b147 | -14.02289 | -44.49272 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5adb2055-2c69-35d7-a50c-7ec9bb1c298f | -13.6287 | -48.19041 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 453f17c9-6ccb-394a-a5e6-6655d9beb2cb | -14.00669 | -44.5711 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6923c76a-4789-31f0-a4d8-e46129981a28 | -13.39174 | -47.01846 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a9aef59c-9696-399f-8584-6d51451e9cd2 | -13.36506 | -47.02083 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 13510d2b-5950-374d-9740-0438ba910e88 | -14.00306 | -44.59047 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b9b64c1d-f4f3-3b4f-97c7-ffdc136778a2 | -13.19701 | -45.28334 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bbf2ab7-635b-39db-b61c-f5481e542d5a | -13.36631 | -47.00553 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81f53462-f151-3235-aae0-cb641f156def | -13.35875 | -46.87587 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77195bb2-ed58-3c65-a0fe-1d64fb0c3845 | -15.72613 | -42.59639 | 2025-08-30 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2cac097f-c4e9-396d-86f9-ad8f647adebd | -14.03509 | -44.52076 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8fea9a7-9b1d-31ea-b26a-7a0555263d3d | -15.79961 | -41.49512 | 2025-08-30 03:32:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f618a29-8ad2-3d9d-a721-55f1c77c2759 | -13.49493 | -46.84029 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7d3f983-ef42-3dae-a3ea-bb7ece9651bc | -13.46395 | -46.95322 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9d1789b-d816-34cc-ad8e-7b4161a0f6c3 | -13.46614 | -46.95409 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 583c9ff5-f56b-3f89-a9e9-2898dd66e0dc | -14.02205 | -44.4968 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa9b710d-5228-306c-a843-1393982bd53a | -17.45152 | -44.4845 | 2025-08-30 03:32:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fcdaefb-afbe-3813-9334-ad8a843846fe | -13.99822 | -44.58294 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6b06c80-7210-3b31-9768-d3e64ba62853 | -14.02221 | -44.49435 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eac3adaa-3701-391d-81dc-f5bd8f7703b1 | -15.78285 | -38.9317 | 2025-08-30 03:32:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cea26523-efdb-3ba8-9718-3145a646a585 | -14.84149 | -46.74629 | 2025-08-30 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a775e9a-c0db-3206-b8d7-75d0d90c89bc | -13.37026 | -47.02932 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5a3224b1-15ea-3a28-8ecc-4f14b610c3e1 | -13.50145 | -46.84237 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f67d46f-5bcc-3a8f-945f-82b30539c451 | -13.38972 | -46.96112 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09421e43-fb62-318f-887f-80c5ad99c040 | -14.24734 | -45.24419 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bc9c963-d0cf-3ab7-80c8-404845dba767 | -13.99646 | -44.59337 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f7ea201c-2be9-38bb-9858-74fc3426090d | -13.19228 | -45.27798 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ac90f56-8779-3606-b881-6b6ee21d2da9 | -15.42252 | -41.66811 | 2025-08-30 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9154ad55-e159-3ba4-a0c0-2af258a467d9 | -13.19545 | -45.29379 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64afa1ff-0de8-3b48-8083-ce39abf9d1fa | -17.44547 | -44.48653 | 2025-08-30 03:32:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72e84ed7-ce8f-3786-914c-914abdf74400 | -14.0031 | -44.58847 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19e8e616-790b-398e-a7d8-88f816abb8c9 | -14.00709 | -44.59831 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d009bb96-fb8c-319c-9972-1fa744ef09b8 | -14.01854 | -44.54283 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7e0278-463a-3fd0-85e6-55ec613defd3 | -13.58165 | -46.90518 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee3e6dbc-c8c0-3393-abbb-cf2b4ca90f52 | -13.99239 | -44.5836 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 799cabcb-5ba0-3144-bcaf-4f25fdf03a36 | -13.41571 | -46.94941 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f301f8e-00e8-309f-bc08-fedcb15521ff | -16.98044 | -49.32022 | 2025-08-30 03:32:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8967f94d-f02d-3b07-b1d8-80d966cb2f83 | -13.37303 | -47.0166 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 45764bc3-8e3d-3ad6-8250-bea53f98b493 | -13.37161 | -47.01376 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7e2c2df-67a9-37d5-b364-7ff492b19e51 | -13.37355 | -46.98189 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 367e76b0-38d1-3f87-9d79-de6272560e6a | -14.61652 | -48.08323 | 2025-08-30 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6958bd4e-4523-3218-bf9e-666e25b7bdd8 | -13.99814 | -44.58492 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ee8d6e4-bfd2-3b46-9623-121b1a883ded | -13.62636 | -48.19061 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2db8ca46-393b-3f59-8cf3-289d1e8c642d | -13.46515 | -46.94755 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f35a5207-ca11-3ce7-8c3d-8e59c028588c | -13.42264 | -46.94977 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b1cc3bd-4f6a-3383-bb35-022bc633319e | -18.61184 | -40.08008 | 2025-08-30 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb4bd5cd-10ae-3cfa-be24-bb6a832909a5 | -13.37028 | -47.02007 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 46529ca9-bfc1-31c4-9404-cf349f170503 | -13.36386 | -46.99405 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d54252c0-9542-3451-80ac-929a8375676d | -14.02339 | -44.54845 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce39bab9-262f-3c80-96e5-b4bd07ee0495 | -13.49117 | -46.83995 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dc8e3e5-24ec-3877-90b4-5aceecf31e2a | -15.07398 | -48.15819 | 2025-08-30 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df8f8e5f-e151-3066-822d-9da70e0258ca | -13.40681 | -46.95813 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39e6ca94-5c5f-320a-baa3-862e2da82b2b | -18.79911 | -40.15646 | 2025-08-30 03:32:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3893e42-74ad-378a-96a2-cc2e7e075a5f | -14.0214 | -44.49845 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a093c191-1539-3e8f-948c-076ce3a9300a | -13.36636 | -47.01486 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 00ee63b8-be55-3cb7-9931-fe1ca1f3aca9 | -14.004 | -44.5841 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ef1838a9-2835-3ffa-9f56-9c4f38159256 | -14.0225 | -44.55279 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03f790c5-b752-322c-b91e-ab9d1c3b10f4 | -14.02303 | -44.49025 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec3c6aa1-99d1-3601-83a1-5f2a43324733 | -13.36778 | -46.99857 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8065fe64-54eb-382d-b2a4-b373799588ef | -13.3785 | -46.98109 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46bd1a98-56bd-3f1b-917d-f4e3199dc5d5 | -13.38142 | -46.97802 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e796ff9-6e3f-3083-af5c-bdcdf68ecbf0 | -14.05659 | -43.57057 | 2025-08-30 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfcb0870-fac6-3c2a-b89a-d3ea1d53898d | -13.39484 | -46.97013 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 87b623bc-3780-32a5-a503-c29c8492c39f | -13.39156 | -46.9637 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3e27e109-9410-3f9c-a1b7-87da7d6f34c5 | -13.3812 | -46.96828 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 56fc04a3-949f-3ff8-9f19-041131465d83 | -13.62488 | -48.19733 | 2025-08-30 03:32:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef871e5c-30d0-3280-b314-4c1637ab1665 | -13.38252 | -47.00534 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3b911fb-c7b4-3d30-bd0d-16b4eb6f857a | -13.36095 | -47.03086 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9fff5abe-4dcf-343d-b96d-bedf8cdad578 | -13.42936 | -46.95114 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fbd9f16-e253-3b39-ae15-6ef91b671b15 | -13.40468 | -46.95662 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 945bfa61-840f-3cb7-82ae-b44bb70559e5 | -13.36669 | -46.98106 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a9143ee-f7e8-3329-8f09-0a696f7c1dd2 | -13.56328 | -46.92581 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f66a0e8d-a9ae-303c-8002-cc1cba529603 | -13.38636 | -47.01055 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4aa26e18-28a0-3941-ad35-7cce9172a0d6 | -14.6215 | -48.08353 | 2025-08-30 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b814331-4e6b-35d0-ab54-1dd98143d6b3 | -15.3097 | -46.09293 | 2025-08-30 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 184475b9-b0dd-33fe-a2c6-a451cb2444e2 | -13.37586 | -47.00358 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7fae005e-22db-3100-85b9-113dcb1463a0 | -19.07929 | -40.5185 | 2025-08-30 03:32:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 437deffe-fa44-3fe9-89d9-4714ba55e7fe | -16.98263 | -49.31099 | 2025-08-30 03:32:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbdbb540-5e31-3ab5-b564-ae47b034ac00 | -16.40366 | -45.65161 | 2025-08-30 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a7239cf-d890-3f11-996d-1159d88c80ee | -14.0058 | -44.57539 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85862a44-690f-3415-a48d-64624bb7f3c9 | -13.196 | -45.28815 | 2025-08-30 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b52f0f7a-67dd-3e84-a5a3-ebf96c56a2ae | -14.03924 | -44.50055 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a305e4-cca0-3bdd-b2a9-5f358b31ad3a | -14.04166 | -44.51796 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3221225-ff67-3221-a194-93dda62398ab | -13.3654 | -46.987 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bf5b10d9-3dae-3e5c-8c19-1493abbfb21d | -13.49778 | -46.84155 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74625a4c-ae14-37f8-952b-c317b7dff50f | -14.0048 | -44.58172 | 2025-08-30 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 783cd060-cd0f-3de6-abc0-a10b1a3f52c9 | -14.84081 | -46.74687 | 2025-08-30 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3b3eb52-b090-3cc3-ba84-f958076eaab6 | -13.40294 | -46.84691 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4139ca7-0d20-3cb8-8abb-b44bfe6bf428 | -13.38423 | -46.99746 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a7e49d9-3cb3-3724-ac72-0483e1e282c4 | -13.38451 | -46.96381 | 2025-08-30 03:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README16.md)
