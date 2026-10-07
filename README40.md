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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 096970cf-1710-394f-8854-3d4ff1008db4 | -11.60832 | -44.14565 | 2026-10-07 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb0feeea-5772-38bb-a682-2bcabb327048 | -9.25567 | -45.64654 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f79a38e-490b-3a63-91cf-f46bf20c6aa8 | -6.73046 | -45.80091 | 2026-10-07 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c12834a7-ea2f-3330-82a2-4d5fa40fc535 | -8.59061 | -45.67262 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a489cce7-0925-3691-9bea-85435dc1a099 | -8.4496 | -46.41558 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c42255b-5c08-33c6-a93d-4f6a20671314 | -11.69705 | -40.10777 | 2026-10-07 04:02:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32aa8305-092b-3c90-b190-6ed36736f675 | -7.24915 | -45.2614 | 2026-10-07 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3433968-d769-3473-9f93-6df1526dc744 | -10.9784 | -45.41019 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74a2b383-78ce-31df-89c7-66064587f335 | -9.60447 | -40.61083 | 2026-10-07 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 62c3789a-5940-3ed5-81f0-f58a3992a6df | -11.01116 | -45.44849 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cc46f5f-85b6-3f47-82c4-d52ee778e260 | -10.99834 | -45.43147 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b699009e-a7aa-33f3-b7b0-8ca0267eecf8 | -11.23119 | -44.86892 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1a2d181-6586-36ee-8c4f-77a62a01bb49 | -11.70405 | -43.66387 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3defa57e-1c2f-3127-a8df-953a4bde8358 | -8.20939 | -46.35786 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ac86be6-3e2f-3ff9-a2fb-85800bbc39a1 | -10.99196 | -45.41747 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53ceea93-fe5c-371e-a9ba-436eaa6f8151 | -10.84884 | -50.66173 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9139e86e-9ec3-387a-ace9-bb4b37aca9db | -11.67263 | -43.62098 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc17d280-166a-3b7c-b0be-1c366d011a66 | -11.62961 | -43.67106 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40d30e44-9c0a-377d-ac33-70483c5ffffb | -10.98708 | -45.41703 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 224cec6b-bb88-3432-8bdf-91079848facb | -11.25499 | -45.19242 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 968da562-a18b-3c22-93e4-bcfd4e54fe2d | -13.97244 | -42.5038 | 2026-10-07 04:02:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e5e8d844-7807-35b3-8838-187225a74afe | -11.00355 | -45.43562 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21183363-c8d6-3b05-ac12-c2261c5e92c2 | -8.03712 | -47.81486 | 2026-10-07 04:02:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3047bd1a-3120-3113-a224-7f7977680f38 | -12.4371 | -47.99461 | 2026-10-07 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48fd3608-c729-39ca-b43c-e8d3a7cb497c | -11.78688 | -43.53851 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dcffd5e-844e-3a17-ba3f-0b364f98a880 | -9.60375 | -40.61506 | 2026-10-07 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 54e23fcd-fc55-3084-b473-114d8d078de6 | -11.7838 | -46.70974 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d61b1201-7fc7-38b2-945f-d6171881333d | -8.70193 | -45.2224 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1675f6dc-85b5-34e3-85e5-f7b9336f59a2 | -11.84082 | -43.55434 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c68fbc2-0886-3000-bc0a-4fc857ce3d8b | -11.3279 | -46.66957 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 064d65f8-023d-3dca-9d4b-7d432a7b72bf | -7.6026 | -42.37792 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 239154bf-ff6a-3e27-a86f-b1cc642cde9c | -10.46767 | -46.8269 | 2026-10-07 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ff9bf38-3b18-3e8f-9b9d-bd62c3cc809b | -7.99522 | -45.49581 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be4e4498-95f3-33f8-ba80-bc07f3de80f1 | -7.87719 | -44.19471 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8edaea18-5bfd-33c6-b887-82c641b9e999 | -13.58348 | -44.42451 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e9284a7-d237-3269-af9a-f8cfdf0babf3 | -9.2606 | -45.64794 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a20d0c91-aeac-399b-a265-b3aeb74cc90f | -8.5912 | -45.66924 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aec26aa1-68d9-31b8-aee1-44830da30259 | -7.45495 | -46.83676 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9027eeb3-12d7-3f62-8298-0ad1ddd7ca15 | -7.86914 | -44.21267 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dbd6a370-b326-3c7b-9ed2-b0d81d1c081c | -10.48619 | -50.42673 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aaa267a3-937b-3a93-8561-476d7be8fb17 | -9.79787 | -48.92587 | 2026-10-07 04:02:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6565c6e3-e879-36ac-947e-3901736b8c24 | -8.28911 | -50.26858 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 16784b1a-ec9a-34c9-acec-2e60f478b5cb | -7.4801 | -42.79634 | 2026-10-07 04:02:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe792737-0eeb-3b29-bb70-cb47144e667f | -7.46046 | -42.99678 | 2026-10-07 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a4b79fd0-a62e-3fdd-a47b-a0a96b7ef949 | -12.95721 | -42.43615 | 2026-10-07 04:02:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97b14225-e4bd-3872-a408-a15a320b0931 | -11.06071 | -45.83215 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 244d98fd-4a6b-34ad-813c-2749e9c95db3 | -11.79586 | -46.70248 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da14e210-07d0-3afe-b709-bbca1ecb7b43 | -9.2701 | -50.66547 | 2026-10-07 04:02:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a2ddc71-d3a1-376a-a5ed-5ad6cbc84c6b | -11.22465 | -45.27145 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aef1080-1d0b-3b42-a595-7102d08fac11 | -11.68105 | -43.62247 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68bdb357-ec88-35de-bab5-237c72321344 | -9.4424 | -45.8304 | 2026-10-07 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0832ce62-ebb8-3f3c-ab3a-5f7cca3754d2 | -8.70887 | -45.21223 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 46eb4e45-6993-3da2-9d51-ee17b815b8d3 | -8.29843 | -45.47245 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad42330a-1786-3da4-97c9-9a58c6dd8292 | -11.36892 | -46.70811 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8312de13-fbfd-3d3b-bb88-66ee0dc78cb8 | -13.3774 | -43.87347 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 396db8d4-4d6c-3fb0-b2ed-41b6cc37bcf2 | -11.00252 | -45.44133 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 846d95a0-9b12-3a33-bd3c-209356cd4174 | -11.70826 | -43.66465 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e27d34af-eeef-3dc2-b900-cb75b5fd454c | -11.79012 | -46.70459 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a03d6ec5-2fdd-3ac7-af5a-f6fbdf3dbfe4 | -11.00323 | -45.43185 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55dd0511-0fcc-3da2-9bbb-dacda3616be6 | -8.58867 | -45.66989 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9cb87bb4-47e8-364d-8a4b-659041efe081 | -7.47758 | -42.79837 | 2026-10-07 04:02:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ac529d9-8d25-3b4a-b228-1f7594428991 | -13.66729 | -44.28116 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47b0cbf1-066d-3a4c-9487-fef815d0c21d | -8.28793 | -50.27481 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6789ef88-e916-3a42-a9a5-309f3632cb43 | -13.00957 | -45.99964 | 2026-10-07 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6269a5c8-49f3-36ee-ae25-00c5aa08350a | -8.70702 | -45.19445 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c0902cd-611b-3a22-8d78-b0b134b00420 | -11.23122 | -45.26223 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8445c8e5-60b2-3458-a17a-0f2447895105 | -7.87235 | -44.21189 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e64544e4-fd4f-3003-ac55-631e598b9ca9 | -7.27925 | -46.15372 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c1a32d20-5f7f-371c-aff1-6fd73a027a1a | -7.60325 | -42.37412 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d640ea4f-1bcd-3a5e-a870-d7d8ab394d59 | -7.60674 | -42.37863 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9a423dd-891c-36a8-b643-598a6b4d0354 | -12.17469 | -44.72474 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7feb3df-2062-33bf-902f-4ff6e48cb115 | -10.49705 | -50.44117 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a46d8565-e533-3d96-bc53-1c74f6501128 | -8.69804 | -45.2158 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 66dae741-2181-36fd-b977-44a7a702e1d2 | -12.17636 | -44.71563 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a470f6-5c9f-3042-8c4b-04c603a9b3e3 | -10.85551 | -50.6632 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3649ef20-4969-3975-a632-351d8a61e6fb | -9.7988 | -48.92117 | 2026-10-07 04:02:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 804847b4-fa86-348f-8339-8f1638d08cec | -9.83071 | -44.79068 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8e9642f-9d79-38c8-921a-bf90247002cc | -10.48819 | -50.43281 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f61c6f7-d3c4-3394-8986-18ae3a33d1f2 | -7.6087 | -42.3672 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a274fc29-7a8c-3976-bd45-bb0a1b00a710 | -6.98966 | -43.21717 | 2026-10-07 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34c65fc4-f11a-3a4f-9260-a7f7f37b68ac | -10.85245 | -50.65745 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4940a915-3832-3586-9ff6-ef0556a6f726 | -12.19762 | -44.64966 | 2026-10-07 04:02:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9eb71960-c3ee-38ba-9357-d1fcb3f6ebcf | -12.16664 | -44.24925 | 2026-10-07 04:02:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c1fe74c-e9cc-31ed-bd85-160fe85fc7ef | -11.74536 | -44.94207 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d50f1c-0072-3151-b1b7-e0d2701809da | -8.71681 | -45.19648 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7423920f-0cbd-3cce-b4b4-27577a4cf66e | -9.44293 | -45.82751 | 2026-10-07 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 364f88de-0931-37d9-bb99-6856b3d4c3f9 | -14.25194 | -41.62446 | 2026-10-07 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 58ec670e-4959-3b58-840b-04840f9b923c | -11.22657 | -44.86818 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78d45a8a-7f9b-3898-94de-e0a8ef65589e | -8.71579 | -45.20211 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 841f8b01-5c2f-3ba5-87e3-05d0802e9a68 | -8.77884 | -47.5759 | 2026-10-07 04:02:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 718ce3f2-c6b6-3def-ae26-3a1e32f928b1 | -8.78458 | -47.577 | 2026-10-07 04:02:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 211bde23-e72d-30bf-ad38-b2873e888a43 | -13.97622 | -42.50454 | 2026-10-07 04:02:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73526198-b78d-3f9a-8a90-1def8e9b5219 | -9.82024 | -44.78677 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc410529-d7a0-3215-8207-72db40dc7f1f | -13.27156 | -44.00338 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c13ea6a7-70b6-37d5-8c50-7781cceb4bf7 | -7.99467 | -45.49882 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 810a4da7-5a17-377e-a82c-191f11433089 | -7.82149 | -46.86555 | 2026-10-07 04:02:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73c9faa3-1e03-3bb7-a71f-6e735c67e8f4 | -9.54318 | -43.03612 | 2026-10-07 04:02:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ab4ff87-db9c-36eb-869f-8faf3eadab09 | -13.68357 | -44.28823 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ae67ccb-ea28-3632-ae8e-69cdb5c20357 | -8.30138 | -45.47331 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ddb1b6c1-ef2f-3b94-9b78-a1483aa6de5c | -8.28112 | -50.27345 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README41.md)
