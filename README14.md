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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23ee4df0-beff-32ff-9369-708db596acb9 | -7.48193 | -46.67674 | 2026-09-09 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1e6093-69a3-34cd-aca8-409c9006d58f | -9.77635 | -43.46321 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eedc68ab-6130-31f5-9456-c2ede4cf1a8e | -3.54964 | -48.18325 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37691d4d-1f14-36c3-9d46-122f5fc0eeff | -5.82049 | -53.81011 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9581cee-fb79-35a6-9936-98358d5c9eb0 | -6.17227 | -43.02562 | 2026-09-09 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 864a2898-2101-364c-9adf-2be1b93bc4e3 | -9.76465 | -43.4073 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d7a6ea-7cfb-3380-82f7-d6914e90f0fd | -6.91986 | -41.34489 | 2026-09-09 04:25:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86b9bc7f-5449-3ffb-a6fb-ab87892ab5c2 | -5.80035 | -53.81959 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69f3fbd8-cf1e-3cc1-bfe3-aedd23d0480c | -5.21264 | -55.99658 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ccf6a68-91a5-3742-860f-73dd19e6e790 | -6.16451 | -44.66469 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a76a3d92-71ba-3c5f-a9ec-e2f89abe5310 | -9.70039 | -43.43332 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 71a40b4a-4bdf-3bc6-be49-96bfe2738f13 | -3.96884 | -47.58668 | 2026-09-09 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf3d385c-d7df-37ec-895a-5a20e4dca388 | -9.70096 | -43.47301 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 367eec04-f3ae-3519-be05-9064f19c4508 | -3.55313 | -48.18346 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ba51b77-fca8-3999-9461-975e3c72cca5 | -8.73126 | -36.89608 | 2026-09-09 04:25:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4113b70-d640-3b42-bc84-1930643fd177 | -11.00385 | -45.08011 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cedc9e52-71ad-37ee-b1a3-ceb1397407b5 | -7.1986 | -43.61326 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc11c488-7b94-3599-a9f0-bc4c4e756937 | -9.78192 | -43.49292 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5559959-81c0-385b-90cf-d65fd7f25877 | -10.22989 | -44.6334 | 2026-09-09 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2796b017-93e8-3aeb-9429-011c5a0005b2 | -3.5489 | -48.18279 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d0f9782-1be1-31a9-adf7-2e627a8f7f02 | -9.78337 | -41.99947 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8786c653-655a-3e6d-9fac-7ee204f638ae | -9.69983 | -43.43684 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c98e45cb-751a-3f1e-8bfd-a28fc4bdea26 | -9.26286 | -45.6594 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d656378b-b501-3fbd-ab53-787d8f0e2fd5 | -5.60495 | -44.84299 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f36d4f2a-4a37-34ba-a565-d06321ad655f | -9.7725 | -43.5094 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fbe37dc-dd76-30ed-91b8-fac1ec6152e9 | -6.03357 | -42.64112 | 2026-09-09 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bdc1bea9-3e79-32db-bd5a-8f76f95b608b | -7.68411 | -44.32299 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f6bdb3e-a0ef-3356-90d8-3768b0b7277e | -5.75031 | -50.1881 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eadf6e42-9f21-3971-9ea8-0fe58b8d0c2c | -3.76261 | -50.45449 | 2026-09-09 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af3813ae-bb48-3be0-b2db-1cf28f2be7a9 | -7.19417 | -43.61969 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 30f90f7e-57b6-35f3-9012-34a07cc58356 | -8.42011 | -46.89468 | 2026-09-09 04:25:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76da94e4-99ad-39ed-abd9-f892480a804b | -9.69376 | -43.49704 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 491f4ce8-f0e9-37cc-a378-2747ea83986e | -11.43534 | -45.1547 | 2026-09-09 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5ced78b-380d-3b65-a3ab-1b886af6396d | -7.73743 | -45.05333 | 2026-09-09 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6cb00f-d118-303a-9800-34e9fb9f7704 | -9.71706 | -43.47917 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 290c52a5-841b-3dd9-a3ed-7656ee345862 | -5.79776 | -50.2026 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c56e899-d5a7-3c2d-9a95-332a2bc3cb84 | -5.60838 | -44.84354 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f1961f37-f710-3c83-a746-b070a10f2df1 | -3.79715 | -52.40975 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2faf3c1-785d-3e4b-89de-9cce84b69376 | -11.17795 | -45.03559 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f1b39d7f-b362-3d24-b24e-40a44aaecca8 | -9.7641 | -43.41082 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da00145-d6f2-35b7-ae80-0fc9d2e651bb | -5.42703 | -43.43068 | 2026-09-09 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d8d2d04-4ffa-3307-852d-c42bdf6f5d2c | -5.83288 | -42.28035 | 2026-09-09 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf79798b-df4d-3249-ad0d-e259d5b75549 | -4.02184 | -50.44016 | 2026-09-09 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb6a9592-ccf0-31ca-a6e6-c5f244589230 | -10.3673 | -45.16713 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3040eb1-b32a-3e21-bc87-7aa97f65e538 | -3.96988 | -47.58333 | 2026-09-09 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 669b2d11-32db-3918-b1c1-dc2e24b09aa9 | -5.80404 | -53.81896 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b40cf42-606d-3570-be08-f6cddb25bc03 | -5.75979 | -45.07865 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 775d887b-30bc-3700-b1c9-51a55193560b | -10.71701 | -46.04554 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc5287db-3f65-35cb-963d-aa5eecd33a35 | -5.77483 | -45.07328 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 389aca0d-0560-3194-b7e6-5597a2108b4a | -10.71793 | -46.05668 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6594e359-b34a-3f33-bde0-dd575b5b00c7 | -5.40786 | -49.18483 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b971dd83-c805-3bea-9ef7-c50c26d544db | -9.70262 | -43.46249 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5e45116-d358-3868-becd-2d9226d819e5 | -6.83277 | -39.4052 | 2026-09-09 04:25:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4882262c-1411-3f88-9785-7dc7abd8aa8a | -5.81456 | -53.809 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35735bfa-a3c6-3630-8a82-2f1ee2ca349d | -10.58735 | -45.74786 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b836eedf-ff17-3262-add7-b99cabf0355b | -9.25721 | -45.65443 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e08666-55f5-3d1f-91da-acb50445eaad | -6.27622 | -41.6982 | 2026-09-09 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fa401cd5-1155-3faf-9d6f-4686deccf18a | -3.55089 | -48.17546 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1aeedc0b-fb8e-38aa-ae6a-e47656acc76f | -8.84264 | -36.527 | 2026-09-09 04:25:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1ab76ef-5716-3b2d-9451-f4550da690c5 | -11.32005 | -45.75504 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9fb0aad5-7c3c-3982-baf6-5e8bebcc7a2a | -10.7323 | -46.01269 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfb02660-1cf9-3d20-af42-dd54dd721a7b | -5.79889 | -53.81336 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5bae19d-2bf6-3201-a6e8-b104023279d7 | -10.24089 | -45.2161 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2773821f-cd0c-3e9e-8ec7-82faf7eaae74 | -6.86659 | -46.01642 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c43cf59-1e4f-3fc1-98bc-2e23df7c7224 | -10.36672 | -45.17072 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c58c224e-03c4-3b2e-83c4-5a2b71485b04 | -11.2665 | -45.69785 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e221a8c3-efb7-3f42-8979-f7b6563de7bd | -8.21469 | -46.00824 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ced1245e-8c78-3ae3-88b6-705ec2ee81ec | -9.69542 | -43.48652 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb0e7934-f112-3e6b-b2f3-85b1550d2486 | -5.77949 | -45.06628 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b490418a-1d2b-3383-83b7-d474d96af369 | -6.16743 | -44.64648 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06d9ea84-01c4-3c6e-b1a1-76305bccaa4d | -5.64762 | -44.30049 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da3dbb01-df0a-3e35-8193-fa4ef50dbe60 | -3.95497 | -49.01068 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40921d96-78d1-3988-89c0-d75d199e8c8e | -6.27847 | -41.70597 | 2026-09-09 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1465e4b0-434b-3b1c-9bcb-89ebcd6c3cb1 | -5.79955 | -53.82395 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c86d584d-be3b-3621-98fa-72ccbcf5a16e | -9.70039 | -43.45496 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3c6591e0-d287-373f-899b-a53eabf66d78 | -6.86789 | -46.00853 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d048681-4fcc-3b45-8003-17ddd8afef8b | -4.30018 | -49.08781 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aadd9a5e-7b74-33b4-82b8-2e635036ef64 | -9.69706 | -43.45443 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| adc71927-d9d1-3af0-a344-311f61a2a6ba | -9.72812 | -43.38731 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 827751a7-2c78-3dad-848f-ea9e05413043 | -4.29647 | -49.08269 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5349ab36-b36b-3c9a-8e0f-131d606e02d2 | -9.77861 | -43.51398 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0764faa7-0df5-3fa7-8d0b-7c4a7e3876f0 | -9.69597 | -43.483 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05eab50b-5313-3d4a-af65-6f38de66b924 | -5.82369 | -53.79251 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07837cc5-619b-3923-9710-99cdd9f671ca | -11.17852 | -45.03202 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 55fa998f-5b5a-3c04-892b-d1a8f6d1fcd5 | -9.78136 | -43.47482 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 684db93f-1381-364e-8861-a84f0822edc5 | -9.71373 | -43.47864 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2214a3e0-783c-3c6c-b427-cf20c1b821a3 | -5.77137 | -45.07274 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8737f3b5-19a7-3317-a155-5fc14fc1839a | -10.71639 | -46.04477 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7626a0ee-f62e-3a77-9168-276321d762a5 | -9.77413 | -43.45564 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 253a24ff-c1d4-318a-864c-25b8d06db81b | -5.79861 | -50.19776 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 949aa6fe-68a3-370a-84f2-b6a005f7fb09 | -5.21266 | -55.99712 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fcb548a-2f00-3968-a52b-4d4ed0e9d4e0 | -7.1314 | -42.12391 | 2026-09-09 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 580d0038-6eb8-372d-8db0-2fe6208bdf0d | -10.52569 | -47.95658 | 2026-09-09 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f07dc99-efac-3384-91e7-8e9eaba641da | -9.05231 | -41.12257 | 2026-09-09 04:25:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2a34bcd-5fdb-37a9-909d-2a4b66d3ef2c | -7.68859 | -44.31646 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93963c6f-2a84-3230-b4b6-87db76ef3be4 | -6.86435 | -46.00793 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eea1ddf7-1dca-30d4-b1cb-d5d461928314 | -6.75991 | -44.57283 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae18d12a-b8bf-38c7-af18-330f9e3aa779 | -3.87124 | -47.09716 | 2026-09-09 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75fdf22a-aa67-3135-8080-b28b4463ef0c | -11.32404 | -45.75195 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6792adb0-d12c-3187-b91d-ae34afb61f3a | -6.03025 | -42.6406 | 2026-09-09 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
