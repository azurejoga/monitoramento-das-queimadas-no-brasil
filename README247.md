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

## Dados Diários - Página 247

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc238646-db4c-337d-b005-7a145874e2e6 | -6.88996 | -43.69269 | 2026-10-08 15:41:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5daa4d2e-d8b3-3c61-b01e-26db9141a387 | -5.95899 | -46.38066 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 65faa694-461e-3502-b720-a4935ad7d23d | -7.48633 | -40.65078 | 2026-10-08 15:41:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 2bc49835-0e40-3253-a0db-82f0c6e9724e | -6.37323 | -42.52607 | 2026-10-08 15:41:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 258cbdf6-c14a-3f8b-9d52-14ca073c7881 | -8.21027 | -46.42443 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a7fc9e38-1207-3f35-9247-cbc5e0f79ee2 | -5.50514 | -42.82336 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 719dc32f-5100-36eb-a60f-3b9641809910 | -5.99044 | -40.93405 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| 0682395c-ae94-352b-b13c-06afdceab8a8 | -8.57317 | -37.11948 | 2026-10-08 15:41:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f20f00fc-0369-325a-b99c-30d7ee583c63 | -6.0111 | -42.26411 | 2026-10-08 15:41:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 217ebdc0-ede3-3d85-be35-4e1a44f77f27 | -6.58777 | -44.85913 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ab906fa-4413-3e0d-b842-858b7e361503 | -8.89133 | -45.38281 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e8169046-965e-3c05-a2f9-09a91c986ec5 | -5.4684 | -41.22109 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 2dec5351-8773-3f6e-a737-62714acef489 | -8.96082 | -45.14163 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2c39c377-cb27-3cd2-893e-518991056665 | -6.53209 | -45.39523 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d77504be-c7ce-39ff-b403-b6f8a1d7afb8 | -6.9984 | -43.44293 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e456a146-bcb9-3f81-9f0c-0caa75a2d3a4 | -7.34911 | -44.36948 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4960ab1a-0a32-334e-b109-f83579f36e08 | -5.73509 | -41.76899 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8fd13932-2263-36e2-812d-bbde971374c8 | -6.68908 | -41.76609 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ea2b34f5-aecb-3cb6-806f-fd4c4fd33906 | -8.95109 | -45.17154 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4d02bfd9-fbda-3899-b6a5-595ea40ad4b1 | -7.11609 | -42.53762 | 2026-10-08 15:41:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 33b1aff7-090d-3745-bfb7-9dc264bc65ca | -11.11266 | -45.6978 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4a0c04e5-ce16-3705-8c6b-76548adc2066 | -9.82974 | -45.76845 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e725e7ea-7b94-33a0-a122-4526f690b84c | -8.94312 | -45.16071 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7ddaa935-19ea-3b61-ac4b-32e77c10db00 | -8.18864 | -46.36488 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ad86bf1b-68c1-3c5c-8af1-a73fb8352067 | -10.89801 | -45.5374 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b37195e5-1485-3b8b-b5e8-874874b53112 | -11.26862 | -45.20785 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ca342b49-0eec-302e-ab86-4989753cea49 | -7.04544 | -44.34156 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 36d3e952-2a20-35ef-bbdd-61509a19ae39 | -6.82391 | -39.55844 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| ab590a5c-8042-3166-b4b4-aae09c4a90df | -8.93859 | -45.17865 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 340.0 |
| 762bb916-f6a3-37eb-8997-d5481a686388 | -6.57226 | -41.61175 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f1ec5fa1-e5c6-3e1a-98f2-3e881d6f14b1 | -5.88074 | -45.98344 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 30acc916-4b7d-3022-b5d6-5cb687c03155 | -8.07061 | -45.61385 | 2026-10-08 15:41:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 7d5fbec6-c6c3-36c5-9e10-849eb9d7e2b5 | -6.83251 | -39.55439 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 7ee71e81-eb92-3d47-a021-0ffe7c7fe4fd | -10.16032 | -40.52522 | 2026-10-08 15:41:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 2273f351-bb21-3190-a790-1e25ea9d80e1 | -7.59725 | -42.38474 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| d522f1d2-ca1d-3fc4-83fb-1a9e2b116881 | -9.89798 | -45.19956 | 2026-10-08 15:41:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 797782c9-ca3d-31f7-85f5-201fbc0bf9ba | -9.71761 | -40.13478 | 2026-10-08 15:41:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a995957c-6e15-360e-9da7-e8515bc554a0 | -5.97466 | -41.37076 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 481068f3-d18f-36b7-b25b-5caaa3901834 | -6.05566 | -42.5937 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b9019942-41ee-3413-a70f-301441be7e95 | -8.84177 | -45.45435 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6ce830f6-fbfb-34f5-abe1-8d22720a4035 | -9.81902 | -45.67886 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 461c4ce3-5f0a-3ccb-8b78-5f47a467675e | -6.82751 | -39.55074 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2f9d117d-32ec-3f2e-a29b-d2f6898231b8 | -8.58913 | -45.69294 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 34a75de7-da3a-3538-ab73-7e590ef06e41 | -7.3449 | -45.28353 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6e45ee3f-0db7-3590-ada5-650666699d2c | -10.22813 | -40.04582 | 2026-10-08 15:41:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5d4d460f-52b8-3e5a-8331-b3d6eeb8edae | -6.82917 | -39.56271 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| ccd7b207-5c07-3469-93c3-1f224aecd722 | -7.20699 | -45.09065 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f198e90-dc64-3036-b931-d0625c8f9068 | -5.24382 | -38.54593 | 2026-10-08 15:41:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| fa2536b1-e491-3f61-9371-b601b55dfcbb | -8.61706 | -44.88245 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| caea7823-97bb-3e7e-b7ee-2d2e0e988cbb | -5.28319 | -42.73064 | 2026-10-08 15:41:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 854b446c-5ad3-3360-974a-32da62d17eff | -6.9306 | -43.07187 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7c0cfe67-ec21-3c2e-a12b-e7129f1d8e84 | -8.37027 | -44.76618 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f019af4-ec85-3829-b718-200d9e5ac656 | -8.94712 | -45.13011 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7b944f45-d4d9-3185-b332-630210626d30 | -6.83305 | -39.55832 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 2a6a4399-96c6-33c1-a36f-e694e78d6ad3 | -11.20526 | -44.85679 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8a518850-897a-3055-8606-d280328bb588 | -7.19075 | -44.30827 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f4867c4-8f7a-317d-b9fd-7e0e4ab77cb6 | -8.18952 | -46.37198 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9387f8e8-f35c-3ced-bf29-418a1978cc79 | -7.46719 | -45.77222 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7a5be82a-1bd6-32da-8f30-81d990fc9425 | -11.2289 | -45.23958 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c69f579c-4add-3fd8-985a-a98028ce549a | -6.4075 | -44.95734 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e4a54d47-ac13-37b6-8785-24839dcd7bf8 | -5.71615 | -41.74475 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2ca1ec7b-b3f2-3fd5-b00a-31ad6cc713cf | -5.87174 | -45.9664 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ba0e71be-9c0e-3559-943e-2d1e8f596a07 | -5.75262 | -41.64245 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5910d697-6c1c-30cc-add0-fc58101e79aa | -6.84716 | -41.75684 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 505a9556-2d36-3046-8eeb-fd18f209b304 | -5.72468 | -41.77383 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ad32f526-2c3a-3d49-822b-e635bd60e82a | -7.48621 | -42.81444 | 2026-10-08 15:41:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 91e1292d-e797-39e5-bfea-1b8cf1ea1801 | -10.96614 | -45.38958 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 15575540-8353-32ef-87cd-f925f7ec9e65 | -8.95209 | -45.16909 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 761e19b6-8627-3920-b492-c9c9cb15206e | -5.74759 | -41.64299 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 95c4803f-694f-3cad-a86f-facb163caadd | -7.26082 | -45.34932 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a64b0298-ca88-3154-89ac-3b3770e0ff97 | -6.42791 | -44.82446 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4c7622e9-62b2-3504-82b2-4f35a9ba4b6f | -7.04331 | -44.33274 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0f2a81cc-7e97-3764-b34e-73ffed90df48 | -5.77375 | -42.05649 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fef9d988-3181-32bb-875c-16414984167f | -10.33858 | -46.23838 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 26b29ec4-b53a-3dd4-9714-6ba08ad88b19 | -6.1562 | -42.58536 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2cc77504-f84a-3f7a-aa8a-41dc741ee160 | -6.10057 | -42.81436 | 2026-10-08 15:41:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b1842baf-ad56-3e39-82c2-b8dea2530b23 | -4.75278 | -40.50393 | 2026-10-08 15:41:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4d082d80-1d8a-3b21-bb7d-810cdf239e5d | -7.18838 | -44.33741 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1c2b4e71-a14a-3e1f-8250-46d1db7ef039 | -6.59879 | -37.88865 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |
| becd07c4-83e6-39de-94b6-90b462753f83 | -8.20262 | -46.36312 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9412f558-2eac-3cd5-9ef3-d8edcf621a6a | -8.93235 | -45.17144 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 326.3 |
| 464e6d10-f83f-3560-946e-6136ce7af346 | -6.95221 | -45.27291 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d22c932c-60cb-385c-81d1-266b66607017 | -6.67862 | -45.35412 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 29c3f10a-35db-30e0-a415-6e957ab640d2 | -5.74738 | -41.67809 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cfb7de75-8c64-36ba-b618-dfffbd23b8e1 | -8.5779 | -36.72222 | 2026-10-08 15:41:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| df1d4a77-bcf7-368e-8b75-5682ed4cf404 | -8.9683 | -45.13933 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c9226dac-bbc9-3b53-9ffa-f37ad8dfa2a6 | -5.94936 | -45.69714 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 63acb0b1-58a5-3d88-b944-8a56c53e996c | -6.16201 | -42.58788 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6c936584-8b1d-323b-9b99-453a848f953c | -11.21321 | -44.86731 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 66807019-4587-3ec7-83b0-ceb19d2a0690 | -5.71857 | -41.65538 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 5a5dfdaa-bcb9-31c6-b36e-c7b7a9de910a | -10.25311 | -37.86228 | 2026-10-08 15:41:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| beaff20b-1eb0-3ecd-a3a4-ed8e09798092 | -6.32556 | -35.13765 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| bbf7acc5-0b5e-3ec6-8ecb-ea29c9ab5f8e | -5.71907 | -41.73276 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e20d4581-8207-3df8-b18f-5c40cdd47315 | -9.93582 | -43.56833 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| b8895d34-a8da-3200-9bc1-2a40babac403 | -6.16456 | -39.43694 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 2e5651b2-bed3-3f5a-8fdf-127eca253e44 | -8.61633 | -44.87688 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 22022d75-cc67-3641-bc11-2b35a58722ba | -11.27354 | -45.20958 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4ea22897-1472-38a5-b230-c8140dceb666 | -8.2192 | -46.38202 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| a6543c77-2b9e-31f7-a38a-b4fa52ac4efb | -5.9897 | -40.92887 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 859967bd-575d-3476-a017-a92584e209bc | -7.48788 | -42.82311 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README248.md)
