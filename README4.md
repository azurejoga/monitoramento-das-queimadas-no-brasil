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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81d68bb6-da99-3198-8f79-e9f322092412 | -11.2462 | -45.159 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a06e049-dd64-3858-a36a-95d51f0ef6d2 | -12.9502 | -45.975101 | 2026-09-01 00:15:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19067d10-a7e8-38fe-9294-ed7d250c7bb3 | -17.384899 | -42.355499 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cc940be5-1db3-31d2-a17a-f2a24d1e5eea | -11.3187 | -45.162601 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73227dd0-f223-3389-b858-9a0d61f7c08e | -11.3226 | -45.180901 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3bf743c-b456-3fec-b07f-e0f0781199fe | -10.1706 | -50.3526 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84c494bf-408b-3bf0-82b6-3a48553310a3 | -21.518801 | -48.624298 | 2026-09-01 00:15:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef4aeb8a-5d8c-36e8-9fd4-e7b40407b26c | -7.4076 | -49.740601 | 2026-09-01 00:15:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7514fc40-01ca-36ca-b15e-57226f9fef31 | -6.2021 | -42.524601 | 2026-09-01 00:15:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8933292-a45c-36f9-b370-c3546ae0292a | -8.8747 | -47.090599 | 2026-09-01 00:15:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec7508b0-509d-35e6-8231-3fa01458ee3a | -11.3524 | -45.417999 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d119967-c834-3080-8033-d5a5e357b8fa | -12.8728 | -45.846802 | 2026-09-01 00:15:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 071772ef-7712-3078-a8ca-496e59694b8f | -11.6678 | -47.6241 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84bcf9b2-8555-358f-b7e6-0f7c0c0498eb | -7.3978 | -49.742699 | 2026-09-01 00:15:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6320103-0553-374d-b1bf-d47523d22844 | -21.601999 | -41.201302 | 2026-09-01 00:15:00 | METOP-C | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35f08e97-c8bb-3640-9b4e-09b379f8c3ee | -11.9062 | -45.085098 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04eb927b-ebd1-3805-bc6d-528b8cec1521 | -16.125999 | -52.380199 | 2026-09-01 00:15:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2750489-7a39-3902-bb12-065b29abc838 | -20.474501 | -45.7006 | 2026-09-01 00:15:00 | METOP-C | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 010eb032-0290-3f91-a0d2-9f6d828b1c53 | -11.2443 | -45.149899 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cac86a61-8db2-377a-8900-f6ca3ac3084f | -5.8401 | -44.893501 | 2026-09-01 00:15:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73f2f91d-a43b-3a8d-a153-12546d6e70c9 | -6.7724 | -41.185699 | 2026-09-01 00:15:00 | METOP-C | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ead2e30-a201-353c-af19-fa9efd6a7345 | -11.2073 | -46.088001 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc99c05d-13e0-3c77-806b-a3c73371394b | -16.3029 | -42.040401 | 2026-09-01 00:15:00 | METOP-C | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73e54257-ead6-3e65-9b20-b07c1cc419f7 | -11.9042 | -45.075901 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74d8e4b4-0a00-3beb-8d06-137f0fc1fc25 | -10.1727 | -50.3125 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33d4b5e4-64ba-3666-9840-f10d12ac9fb3 | -6.425 | -41.739399 | 2026-09-01 00:15:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2ce40a4-ef67-3550-b2e6-5810c847dc7a | -10.1842 | -50.3699 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78a91580-ae81-387f-824b-413385969009 | -12.0923 | -44.9972 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0c463cb-f786-3dfc-b689-a9fa47befad3 | -11.1973 | -45.121899 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04f64cc3-c4cd-3478-81a2-b13300b93305 | -7.3605 | -45.073399 | 2026-09-01 00:15:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0a2c0f3-ae78-32d6-9d4b-426f89b1f4bb | -7.111 | -45.805302 | 2026-09-01 00:15:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e0cdb95-29e7-363a-b02f-305a4e7f66e5 | -11.9199 | -45.101501 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91cdc44b-04c9-30e6-b7d6-a2bec668364a | -6.2119 | -42.5224 | 2026-09-01 00:15:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a390e603-d9e1-3117-a4d7-44fdf357d157 | -9.5427 | -42.903301 | 2026-09-01 00:15:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7bdb56d1-fc86-35c2-9bd2-62a775fcdf06 | -8.8457 | -36.5369 | 2026-09-01 00:15:00 | METOP-C | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 135c3edb-28a7-312f-8045-0ae934c53406 | -17.3801 | -42.381901 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a2cb2d31-fd17-3016-92dc-4c83df65f88a | -10.7366 | -47.994999 | 2026-09-01 00:15:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4340b587-0ee8-3879-9ce4-1756621ee2e0 | -11.3206 | -45.171799 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2bd7b9-5583-3356-84a6-b0a2b008a755 | -11.3147 | -45.1922 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7e52770-4e73-3c2a-aff5-5921db0bc58c | -10.6746 | -46.275902 | 2026-09-01 00:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae09bb4-5819-32ae-a2b1-9167c3704c6e | -4.7696 | -41.806801 | 2026-09-01 00:15:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93e4fccb-6f2e-3dd7-8457-d8cde94f8e2c | -5.3469 | -45.171799 | 2026-09-01 00:15:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73b4ad4c-226a-3045-8a2b-f14c2d45edcf | -11.6624 | -47.5979 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ddd97df-f499-3163-bd29-73bcf7ab173f | -17.003 | -39.5051 | 2026-09-01 00:15:00 | METOP-C | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ef70d8d-b3ef-3e25-be46-5944dfa82e8c | -11.2624 | -50.614101 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d8b667b-a189-36a3-9271-5554ad095886 | -4.4335 | -42.862301 | 2026-09-01 00:15:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1734433-e18e-3fde-9da9-45ac2f4876ff | -1.9576 | -48.384998 | 2026-09-01 00:15:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1eae53-7238-3995-ba6c-c36659c753ec | -6.7594 | -44.587898 | 2026-09-01 00:15:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c648743c-dccd-3504-9439-aa84420647dc | -18.4809 | -50.895302 | 2026-09-01 00:15:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0524d7-0d74-3ceb-8bb1-2c11bba0871d | -3.143 | -44.484402 | 2026-09-01 00:15:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81d2a7b3-65a1-3dd5-b1a3-a54a89cb1d79 | -10.1493 | -50.297401 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74b04563-f2b3-386e-8f13-4aca9f6b82da | -11.258 | -45.118401 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d55e2e0-dd9c-32ea-8348-c5300204cb61 | -17.7906 | -39.708801 | 2026-09-01 00:15:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be59b46b-580b-3850-a2d7-2cca872ed678 | -11.1072 | -51.5219 | 2026-09-01 00:15:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc6688b-0be8-3733-ab2a-91f5f9ca33e3 | -4.4947 | -46.418598 | 2026-09-01 00:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c177c6e9-76d3-3fec-88c2-356d240bcd31 | -10.0126 | -44.712898 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3a2ad60-8a64-38f4-9c1e-0a2fca532fa5 | -10.1824 | -50.310501 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01528e58-72b0-3bc2-b989-3aef82489aa9 | -6.3519 | -44.100101 | 2026-09-01 00:15:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 095f8386-1c6d-3884-b963-34bb4d1a9414 | -10.1668 | -50.333401 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a41e82a8-2116-3f5b-a498-c46fdcb2a331 | -2.7098 | -48.809299 | 2026-09-01 00:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a565ab6-c44e-38b5-adb6-340c5eb08c87 | -18.495199 | -50.9216 | 2026-09-01 00:15:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb21331-a6f9-3825-983c-02a6b726c9f8 | -4.4319 | -42.8554 | 2026-09-01 00:15:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1878662b-662b-316f-9fa0-d29309252c28 | -3.0492 | -39.9394 | 2026-09-01 00:15:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 35c3526d-c956-34d0-bae2-bfaf9af595ba | -11.3049 | -45.194302 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b7589ed-2f4a-359f-be9c-a46fb467cc86 | -4.5942 | -42.933899 | 2026-09-01 00:15:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 114be84c-b66a-3648-af67-79fe7f3549a1 | -11.658 | -47.626099 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1bce66f-9c8b-3308-b37b-dea011de20e5 | -14.98 | -48.118 | 2026-09-01 00:15:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 631f4ac9-ef46-3cd0-a866-f5704c58a119 | -13.3389 | -43.678902 | 2026-09-01 00:15:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f166ab98-979d-31e0-89fd-67767401ea6d | -11.2583 | -50.593399 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebbfea47-0ebe-385f-8a04-2f53262dfb58 | -6.2005 | -42.517799 | 2026-09-01 00:15:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 808702b8-efff-3a82-b4d7-598c53d663a1 | -11.2033 | -45.1017 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59d2fbe0-c81d-3865-a745-aedd3da09011 | -4.1545 | -47.840599 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a1a270-950e-3eac-ac9b-fdf7d0f84503 | -7.2781 | -49.850101 | 2026-09-01 00:15:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d168a5-8f8d-37c3-9ec4-edf53ed7379c | -12.9644 | -45.994598 | 2026-09-01 00:15:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9b51a2d-b79a-3088-beb3-abe8a0e80370 | -7.4109 | -49.756302 | 2026-09-01 00:15:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7b7d13a-26c7-3bb0-a139-ba5450415e71 | -17.394699 | -42.353298 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f751f86f-b4fe-30db-9564-d6852644f489 | -5.0247 | -43.603802 | 2026-09-01 00:15:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 569eb9e1-60fb-3d9d-93df-64e418389b24 | -10.1997 | -50.346802 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 258c2802-7a64-364d-a187-13c22588dd0b | -17.3687 | -42.375999 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b3d5ffab-2795-3581-b6f9-a5b082f718d7 | -11.2486 | -50.595299 | 2026-09-01 00:15:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f38c515-6610-3497-a8c8-e75ceaa58561 | -4.6709 | -43.2258 | 2026-09-01 00:15:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc29a80f-6565-3482-9f9c-c2a0b3bc4b1f | -4.9424 | -47.648499 | 2026-09-01 00:15:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afaa2ee2-3b9f-39b0-a00b-a0af60b3647c | -5.8791 | -45.5755 | 2026-09-01 00:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c8653ea-194a-39da-923d-d91a04e1dcfe | -5.3451 | -45.164001 | 2026-09-01 00:15:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 774d9d6d-0d85-36e0-a457-735afaa55619 | -14.1132 | -52.799 | 2026-09-01 00:15:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4726cef1-fd4a-3664-adaa-63988f8f7178 | -11.6749 | -47.609001 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 080a2b39-f217-3231-8eab-43a0ed52971b | -10.1202 | -45.880199 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35d8df52-ce8d-39e4-9443-70bbfdcda367 | -7.16 | -45.0494 | 2026-09-01 00:15:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afa15252-399a-39b6-9c98-ddb5c884e7cc | -7.8979 | -44.250599 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 262cb6eb-6ec2-31ad-817f-4169ecc162dc | -11.2266 | -45.1632 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b52e2648-6837-397e-8bb2-0eaf7c8ce243 | -6.8716 | -45.976898 | 2026-09-01 00:15:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 408ced33-6aaa-3b0d-9441-1dbd0acaf925 | -14.6925 | -53.5384 | 2026-09-01 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 10aeec79-f5ec-3fb7-bdf0-0a0874c96a66 | -7.3302 | -60.589 | 2026-09-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8137d285-1570-3e7c-a0c2-e5c1cd3fb3d4 | -6.9552 | -55.635 | 2026-09-01 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| b80da882-2a75-37f8-9939-5aa89dd4276a | -18.5089 | -50.8974 | 2026-09-01 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 0ce423a3-78c2-3cec-ad28-171ca87fd45b | -6.9367 | -55.636 | 2026-09-01 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 2988e6d7-afa8-300a-91d5-484a03d0d459 | -10.0364 | -44.6825 | 2026-09-01 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 0ebf6511-b3db-3737-b5b0-4c1bd7ddb5a5 | -7.013 | -52.9057 | 2026-09-01 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a1c2ecab-9b62-327c-98c7-f433375380d8 | -8.8886 | -66.893 | 2026-09-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 77e9a9ea-8f9a-35f4-aec9-c6dd0438fac5 | -7.2006 | -60.6706 | 2026-09-01 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |


[Clique aqui para ver as próximas entradas](README5.md)
