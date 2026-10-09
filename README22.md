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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5518c6-4770-3725-9ac8-0d21bfa86d84 | -5.3538 | -43.4147 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d748069d-ecce-3529-934f-b1e18c905941 | -11.199 | -45.321499 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a16285fa-c08c-3e2b-a7d6-6f8d82c9c55f | -5.3718 | -48.981602 | 2026-10-09 00:28:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5efee1ab-ee26-395a-a290-0f8653b49d37 | -6.8304 | -39.3176 | 2026-10-09 00:28:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 61000415-476f-3f71-92a4-01244fef030c | -5.0973 | -46.227901 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8198df-74b7-30b1-86d0-ae11bd36e9bc | -3.3372 | -50.4016 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746e182f-ef57-3df2-b9ac-380ee7616636 | -9.9017 | -44.872799 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79d7442c-332d-3141-b88c-23f46a21c039 | -8.6135 | -48.9161 | 2026-10-09 00:28:00 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 776f19ab-a303-3219-a420-c3c17fa8c6e0 | -6.4835 | -55.328899 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f629278-d75e-339b-8e70-9656bcd932e6 | -2.913 | -54.118 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dabc2578-ab3c-349b-abd7-167502516842 | -2.9922 | -53.9249 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74bd661b-461b-3af2-bcbe-8ec15ad0b2ab | -9.8989 | -44.815201 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d441862-8704-3d93-abeb-3c8f8a9ccdf4 | -4.1565 | -43.192001 | 2026-10-09 00:28:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47f6723f-599a-36e7-ad11-90f4619753eb | -8.0318 | -49.3978 | 2026-10-09 00:28:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e923c0-ae5e-35af-b7b7-1ac502503783 | -11.5901 | -43.644001 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2b3f48e-68cc-3809-8409-a410648d1faf | -8.9112 | -45.186001 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6548de-844d-3d9f-92ce-343fc4fb2616 | 3.53 | -51.257198 | 2026-10-09 00:28:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1053e7dc-8796-3ed5-84e3-9721340a5b7a | -4.9321 | -45.733101 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c63f4266-f5ce-39f9-8736-9796646f7739 | -6.1412 | -47.919399 | 2026-10-09 00:28:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e37f669-dc17-35f0-81c5-ad1250ad8abe | -3.0097 | -54.0485 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31f4fa50-7fd7-38e4-b45f-9821edf98bca | -7.8924 | -54.712502 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e48b1a-a18b-3abb-b769-874605b4db7d | -14.0487 | -43.839699 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea76cc2-3365-345c-a22b-496cb7dcf3c3 | -14.8702 | -50.321201 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0f56b79-5581-31c9-a1ce-a3b036bd6145 | 2.4221 | -50.833199 | 2026-10-09 00:28:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 73e10471-48c2-3c40-805b-474baf6dc0a6 | -11.3064 | -46.6814 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b600d45-1857-32c6-9437-86d461782861 | -9.3022 | -47.4268 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbfeb0ad-baf1-3202-b94a-f71189aed8bc | -11.7595 | -46.779202 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac3f1544-f1ef-39c2-b18e-010f37b54f88 | -3.8494 | -44.130699 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 853a1aca-20cb-367b-8cd4-5b2a3d94c559 | -11.7712 | -43.534199 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdab78fc-0ae8-3a18-9398-98271c987cfc | -7.5338 | -45.8815 | 2026-10-09 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb0b933-fbe9-38c9-8fdd-f0059968617f | -11.6244 | -43.613602 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 654103c1-0117-3ac4-92a2-4878371ca914 | -4.532 | -47.0471 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8404208b-3496-3f25-94d1-d414d3a9a3e6 | -5.0843 | -46.2164 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8de60c9-6330-3889-a085-8582f735570d | -14.9797 | -47.547901 | 2026-10-09 00:28:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1826c5-63fa-31e1-8258-cab4cc615e85 | -16.898399 | -40.8913 | 2026-10-09 00:28:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 113acef4-a64a-38e9-bc35-189b073af0f5 | -6.0139 | -40.972801 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab2782e5-99dc-36a4-9a0f-a7bf8b39296b | -15.5711 | -44.519901 | 2026-10-09 00:28:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 584cd151-f697-33a9-b421-f1c51f352191 | -4.087 | -44.132099 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b471c60d-e94e-3e37-a88c-03b9e770fda7 | -11.8365 | -43.5937 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeea7f4a-fdb1-383d-85b1-4230ccb33f6c | -3.2538 | -54.0439 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1804a5b6-2832-3a0d-8296-d4919783d9ef | -11.8578 | -43.596199 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc6fa3d5-6911-37d8-8c6d-4ad0159addf4 | -1.533 | -54.567902 | 2026-10-09 00:28:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2608c14b-c40b-309b-8951-5b96c99c73cf | -6.4528 | -46.023899 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffb4e50a-b125-30b2-9e96-568a38cd9e30 | -11.9996 | -43.495602 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87473d50-c79f-334d-9344-000d5bb2a414 | -7.3986 | -44.752701 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6feb69e6-7a19-35d4-9af4-8653a78916c5 | -9.1168 | -48.825401 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db5c5cae-bf61-38f8-9917-1f288172c26c | -9.1291 | -45.827 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dfb06ef9-45ca-3b1b-9a91-a42048447259 | -7.0964 | -41.7463 | 2026-10-09 00:28:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ea1c01d-81b6-3a6f-b916-eebae7306ae3 | -6.9519 | -45.276402 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3078b84-2661-348b-bff3-5bfd2d1702c7 | -4.9021 | -48.768501 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97b4562-ca3a-3e18-87b3-d14e918e5758 | -14.0077 | -48.7733 | 2026-10-09 00:28:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d35c3ee-de1c-3db1-bbbe-4239e29412c6 | -5.342 | -45.183899 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 737c70d8-4c7a-333c-af6a-b433022f4950 | -2.9986 | -53.907799 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031dec17-abe0-3b51-94ee-64c0d99559ad | -8.1932 | -46.426399 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4e83260-9249-3f49-b804-95563f095bcb | -3.0837 | -53.968399 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a451c42-6f56-3cde-bbbb-1b2446367917 | -11.2417 | -44.8722 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4105d52a-079b-3532-8b5d-bcda491786a7 | -4.7858 | -56.146301 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78947f27-0aa7-370c-8b8b-0b921ec9c7a2 | -2.9855 | -53.894901 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5675c4d-b44c-3279-8f53-c84c3df59ce0 | -6.1137 | -44.817902 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76ec9a7e-8b5c-3efa-b1b1-06f879181856 | -11.8463 | -43.5914 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24543e47-fdfe-3d50-9feb-00ca74cc6e4d | -4.6569 | -49.2323 | 2026-10-09 00:28:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e59443-641f-312d-8b7e-842d429be55b | -14.0767 | -43.7813 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76f42cf8-f016-3ce1-beb3-5e874b2ff299 | -5.9919 | -40.967098 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43f04854-0ff6-379d-b8ae-2b201450d3f9 | -9.225 | -45.659401 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7124c7d4-7bf9-3f27-88db-424a4dd7c39d | -7.3757 | -46.228901 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf27226b-c816-3bf7-ac40-5ccf3e7d4db3 | -13.4796 | -42.486599 | 2026-10-09 00:28:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| def4dc14-f0a3-3b94-a4ed-a3093debb300 | -13.3472 | -43.974201 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef3d746d-5f55-3cf0-af6c-e9a4b6bbd6f4 | -6.9553 | -45.2467 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 094c56ae-01fc-30af-98ad-d35a47f50345 | -3.2504 | -54.0285 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e623f239-e543-35bc-ba25-b4a34640fe4f | -9.8458 | -47.4683 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d07dbf1a-3865-3f21-a38c-a5c11bfe2895 | -9.8941 | -44.794498 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39c33adf-a895-37af-a540-8edfda3ab4ac | -13.3843 | -46.6954 | 2026-10-09 00:28:00 | METOP-C | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d9d6aab0-246c-3004-9670-c2c259418edb | -3.5886 | -54.584499 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6920fd43-f3af-3e22-967c-721555579786 | -9.9021 | -44.829102 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec703aa1-1bb8-30f6-b3ea-07965964c534 | -11.4671 | -43.379799 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc617c5-979c-3e72-af76-4404215afc97 | -9.8957 | -44.801399 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 634a2252-858b-3199-8e32-68a365020973 | -9.289 | -47.4137 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bbf2a7e-537a-3d5a-9849-3e6e1bb86cdb | -5.7409 | -45.348099 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9a5a7c5-bffc-3d94-96c8-700dcfe80d6c | -11.6635 | -43.693901 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24851816-eb79-3c38-9bf6-4e627de82637 | -6.9632 | -45.281101 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59a74dba-f532-3c1f-9a66-8f4460270d19 | -11.6032 | -43.7006 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 705b1f94-0b04-3316-af17-0a2f7a45dd61 | -2.7433 | -54.090401 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 702fa6ac-dc10-338f-82cc-30195dd4e70d | -13.1769 | -54.372002 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 430d735f-aea3-3ba5-aa31-246d58c6457f | -17.0042 | -41.164501 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98ff0e20-faa9-3c91-b756-15917bf3f2ef | -11.781 | -43.531898 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fdb85e2-27bb-3775-ba1d-a16d3d7dda29 | -6.009 | -40.952099 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0cd1d45c-0b15-3d2b-8764-2fad6cd1822f | -3.4813 | -50.493999 | 2026-10-09 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e92dce0a-3795-303f-8c54-e429332b7aa1 | -12.3741 | -39.473499 | 2026-10-09 00:28:00 | METOP-C | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fbb3911e-9e07-36c3-95fc-cd31efb3b207 | -17.7115 | -39.746399 | 2026-10-09 00:28:00 | METOP-C | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b31a809-a32f-38ca-b64a-6f17d0868666 | -5.7235 | -41.787899 | 2026-10-09 00:28:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c5f6ea6-5147-301a-a174-265b43727f56 | -16.756901 | -45.243698 | 2026-10-09 00:28:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19c1d4e6-47ab-38fb-8ca5-087897d31e0d | -16.9963 | -41.174702 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 332edc9d-b144-3690-81a9-cfdea4f40de6 | -16.926001 | -42.116001 | 2026-10-09 00:28:00 | METOP-C | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a0c9461-d99c-3dab-a6b8-a089951d6ab9 | -11.0527 | -44.0439 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff081ca6-78ce-3560-b393-4d0b580b453f | -11.7545 | -44.9524 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4162154f-9073-383d-bdd8-1e5ba274c895 | -15.3935 | -44.275799 | 2026-10-09 00:28:00 | METOP-C | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1c6cf51d-0d4c-3f4f-a90a-45c03e941fcc | -6.0457 | -44.035801 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f592569b-993f-3965-81c8-e2c8eedc30aa | -5.091 | -46.2006 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e73de91-6637-3c4b-90f6-3bf370e486b7 | -4.6352 | -50.9687 | 2026-10-09 00:28:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69770e9-38c0-3b6f-954b-993d4ed86f49 | -2.5925 | -47.356701 | 2026-10-09 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
