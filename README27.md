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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc18b45c-5610-33f6-be5c-2cfb55399d8a | -13.42286 | -46.86668 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ac55be9-4904-384f-ac50-540aa1da341a | -7.14501 | -44.14872 | 2025-08-27 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cff7068-006f-39c1-99a1-54747d0f7187 | -13.45845 | -46.98704 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a7552df-bb79-3b87-8c75-2dd30f804bac | -13.0709 | -46.3174 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91ff4b72-fec2-3d5c-8298-dc2da8a155ca | -6.8085 | -45.0018 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71437f1a-1354-34f6-93d8-3315946b680b | -7.66066 | -40.15617 | 2025-08-27 04:04:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fcb3bdc0-ca5c-3665-8427-d045b19b1942 | -11.07958 | -44.78252 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62c78b8f-b285-31b6-ba85-d8ad2c6dc4b7 | -9.09387 | -49.56313 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad73bad3-4d68-38f1-8d9e-54677ec9a4bd | -8.25395 | -45.11715 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3def8b0a-0aaf-3556-81f7-d5819d4176cf | -9.17079 | -40.5971 | 2025-08-27 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f18a9988-c7fd-3e34-b426-4164a3635413 | -6.90185 | -44.40083 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf8fe990-ff13-385c-b815-8e4dcdf33c61 | -6.81949 | -42.81568 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d57eba55-bb7d-34d7-bcf2-3ca6bacb8a61 | -12.40698 | -46.48914 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb1c63d-9e5f-3891-af7e-2ceb9f35557b | -7.17668 | -43.84746 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9d9ea84-8b8e-3471-93f4-47b5fad1c3c4 | -13.06801 | -46.33356 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f9a992e9-8282-3c32-9187-9eb00e01a333 | -13.06897 | -46.32817 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9863e5f9-1600-3596-9f52-2d6f432418db | -11.14246 | -46.34017 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 30e9fd24-240d-3346-a5a1-ecb8320e4e6c | -6.57641 | -47.38382 | 2025-08-27 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ebe9d0a1-6070-3b95-81e1-41651bec428e | -8.25303 | -45.12243 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658a1faa-2cf5-34ca-a2ab-e0db26eb7eb7 | -7.05131 | -44.29879 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 899e3af8-f7dd-3fbc-a4b1-5409635ea1c0 | -9.09077 | -49.57962 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f3ce1d7-a636-3530-af04-e0602dc80933 | -13.60295 | -48.15276 | 2025-08-27 04:04:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 11a17ef2-8200-3dc4-a936-f15788519441 | -12.78486 | -48.11922 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cff35a69-e33d-3a2d-95f5-05050ffc51cb | -9.16951 | -49.62933 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee02b5c-ab9f-3833-b2e9-068d3bb00ad1 | -7.60018 | -43.94983 | 2025-08-27 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2ad3996-ff72-3206-a43f-e9a2a41e1a80 | -7.43603 | -42.04766 | 2025-08-27 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a10838c-3f60-3603-be25-2fbb4cb2262d | -9.09379 | -49.5732 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a94865c7-0f69-30cd-ae3c-1f6c68c50034 | -12.76889 | -48.15536 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e43c8539-8b94-37dc-bc12-1e82b6f4adb6 | -7.88866 | -45.87085 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 062198d1-7916-30b3-88e8-afa4e6bd31a6 | -12.25061 | -45.06009 | 2025-08-27 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b46233b1-fbcb-3876-8843-0d0085a8dfd1 | -7.71075 | -45.77317 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84819725-36ec-3703-aa78-38608db6c823 | -6.96817 | -44.10019 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3168534-72d2-3d5a-8fd5-dfe8d460a534 | -9.64782 | -40.59838 | 2025-08-27 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2abb699-6a88-3715-b7de-f5f93a8c73ae | -11.925 | -46.71464 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0529967c-1e36-3195-be36-cfb52b6f602d | -8.13698 | -49.58638 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6ce765b-f7d5-342d-a61a-917c6a7dcdca | -10.32207 | -46.77545 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c63c6c8-91f3-3520-bffa-6d7ccac54d85 | -8.26433 | -45.12257 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 572d977a-6e5f-32d3-997f-74fb9f396161 | -7.65369 | -42.66215 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 025fbafb-e1bd-35ce-ad19-21421080f2f8 | -11.1498 | -44.77776 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b924f80-859d-33c9-976c-5bfd6ad745dd | -7.17292 | -43.84682 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 402a523f-282a-3734-8774-cfd7a05e223d | -13.66256 | -46.88039 | 2025-08-27 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc06b1f6-1714-3f23-8590-dd872078847b | -12.90504 | -44.65926 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a3fc22e4-9164-37a5-80a4-653c8f14de06 | -8.73041 | -49.74025 | 2025-08-27 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eca10af-1ac3-3ee7-9ad2-00a417915113 | -12.7032 | -48.1808 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57c352eb-c3a0-3425-a4fd-0e7ca65cfcc2 | -10.12243 | -47.43215 | 2025-08-27 04:04:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ebb5f40-1834-3d2d-a6cd-8ef61c38d789 | -9.07315 | -49.566 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74761026-65cf-3374-b1b6-13e27a0138a6 | -9.08483 | -49.58199 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60720f11-08f5-3aa0-a3d2-baca5fdf4ae6 | -12.80019 | -48.11187 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e25bbc13-1a2e-3a61-af91-27dd70346740 | -9.50473 | -46.71062 | 2025-08-27 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b85e5d0b-680b-3ddc-8074-65a7bb6f4bc1 | -8.56217 | -51.35696 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f055345-c7ac-3f4f-9899-f5f5500c8b0a | -6.38877 | -45.31343 | 2025-08-27 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 583d3481-c43f-3668-b2ea-af00e9ea3dd8 | -9.08728 | -49.57887 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 768cbc59-2bcb-3575-80d4-42551f837255 | -11.58773 | -47.1844 | 2025-08-27 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 099f1394-b21e-3921-975c-797b955297ea | -10.48903 | -51.60569 | 2025-08-27 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7190ee6c-d7b6-3f4f-a97a-2b383a1bfe79 | -8.26032 | -45.12194 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa43ef4f-0935-3081-b12a-a5a1202afc2a | -7.73754 | -47.46452 | 2025-08-27 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a42b8d39-bb6c-3629-8225-66555960186b | -6.80292 | -44.3473 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33fe7355-15a1-3920-85a1-387340bea139 | -11.92009 | -46.7421 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d14f8720-1ee5-3c4f-887d-946d6933bb7b | -6.8882 | -44.43414 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6db5b897-1761-3e50-ba23-c932f3f63246 | -13.3977 | -46.88825 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d1e4640-c076-35d4-9db3-ecc88961eb86 | -11.13834 | -46.33942 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3eeddd60-420b-33f1-8364-0dcf364c2bbc | -8.08556 | -45.00486 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 526ae355-eaa1-3cdf-ad81-091bceeb1839 | -7.17056 | -45.1521 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 907f84da-edf4-32e4-bde6-89cb62a20485 | -9.08847 | -49.57225 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35e7e95e-7bee-30ed-9b58-28579939614b | -7.95541 | -42.62912 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a0159082-341c-30b9-bb74-1e4dd2596bbb | -8.29729 | -46.32751 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3a5b893-3f13-3e77-b6a6-7ba6d47bf41b | -12.92935 | -46.31922 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71589d44-27d5-3c3e-ab77-a96c0c868f50 | -6.78309 | -44.2991 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af5a5d0e-1cf5-3276-a6ea-474ca6ae4370 | -13.40913 | -46.87213 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb5757f8-db39-31b9-94e7-e8b55112450b | -13.44394 | -46.98746 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd6aeee9-17ee-3208-a099-1237fe0c390e | -13.43971 | -46.98717 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b19ccb7-3bb0-3d43-8e29-ca31d56caf7b | -11.29193 | -44.96693 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df5fef23-59a8-3a68-9c42-7033137b0878 | -8.46493 | -43.67815 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2489e323-b019-3424-ad1d-9bbd172667bc | -6.38812 | -45.31718 | 2025-08-27 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d41f044f-141a-31c6-8d32-a6143ad38ddb | -13.67118 | -46.90334 | 2025-08-27 04:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bae4cb9d-71b7-3fc4-942b-0691b42ead07 | -7.25904 | -45.35878 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb11d76c-8962-31e0-b23b-fde629619074 | -8.29223 | -46.33094 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 745b7743-3f5a-3890-abfa-4cdf6639c2bb | -13.39894 | -46.88139 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 792a347a-ee8b-3132-9f73-0ff612d93fc8 | -9.60684 | -40.57749 | 2025-08-27 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0c674828-f79c-383f-9351-80bbb0c6b93a | -10.81691 | -46.37095 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50e9d898-2fbd-3e6f-af8d-92aa710de105 | -9.19732 | -46.74253 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 463423db-24fa-314e-bff3-f5da0ecd87cf | -9.85807 | -44.59688 | 2025-08-27 04:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ebc7ef9-115d-3347-baa1-92109964a130 | -10.86957 | -45.23449 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f549fa8a-132e-32a6-9cf9-3f3cc263d053 | -12.77938 | -48.12364 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0be23030-92e1-3dee-a485-077874e26802 | -6.78219 | -44.30082 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5156109-0dc3-3969-8c3d-0996a13fcb67 | -8.87389 | -47.18717 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9642a52-1cc3-3848-8a76-a42f437888fc | -6.80371 | -44.3426 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36df6abe-6b18-36b6-baab-fb49fca5cad7 | -6.63195 | -53.33776 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf0f43ef-3719-3ccd-a6f1-a343094a9b39 | -11.91592 | -46.7413 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e61373a7-6186-3b0c-8e39-f2739ea67217 | -7.73947 | -51.14111 | 2025-08-27 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6eae4e9f-8680-3b68-af5a-c2be06578c05 | -9.0991 | -49.57415 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d165423-8d15-33aa-a0e0-6f05b5908562 | -10.48814 | -51.61028 | 2025-08-27 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2572f9ba-889a-390d-a5bc-3fa5648d6442 | -7.73899 | -50.28115 | 2025-08-27 04:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8ec0115-d423-3442-b65d-488280d96420 | -12.93141 | -46.33076 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b99cba-d943-3232-ba65-169db25d8926 | -13.82495 | -45.8917 | 2025-08-27 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a8259e1-9a80-35a4-b251-b4c25e886790 | -13.05797 | -46.29746 | 2025-08-27 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce00c77-ddd5-3d83-a8e3-df64266a4ea7 | -10.31763 | -46.80079 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff6a889-57e1-332a-aa4e-4e744f35e688 | -11.10759 | -44.75423 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ba13812-4a72-36b5-8fc4-2ba4e775c85b | -6.84029 | -42.82322 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d0ad76f-3471-3709-8352-a305c0bcb3b7 | -8.13505 | -49.59035 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
