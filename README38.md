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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0d99da0-ea0e-363b-8ca3-addb623eeedb | -7.53458 | -44.3016 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9145238-93c9-3361-a183-3f6c12189c52 | -11.78178 | -45.03833 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d8e7988-3b12-3189-9a7e-74163054ecc4 | -11.96858 | -45.21395 | 2025-10-10 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d40fcd8-0ead-3a52-82f9-df7759b92594 | -8.49019 | -46.13126 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7838218-8c95-32df-9f9e-c367d8bf9375 | -8.49541 | -46.12723 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 48626887-9346-36b2-8074-5fb98a469b14 | -8.19613 | -43.3358 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c6c2645a-25bf-34c6-8cba-e3f3e195123a | -7.28409 | -41.96896 | 2025-10-10 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 822d0fae-9a9f-3c61-b00a-02c5835f2273 | -9.6599 | -43.84846 | 2025-10-10 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cbcc95e4-0129-3521-b578-2bee2a316259 | -5.79641 | -45.10981 | 2025-10-10 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e22fa3c8-cc64-343f-89db-f5ea05ad0ac0 | -6.98793 | -41.92976 | 2025-10-10 04:51:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b9875871-14d4-3e24-9971-b682b229128f | -6.45821 | -44.58548 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d1342fd6-6bb9-357f-b3da-c825a2c5c0e3 | -7.90099 | -45.49433 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df43104-facf-35dd-8b69-19be336ea6a7 | -8.18588 | -43.32885 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dcb74784-d450-320f-9cdf-2449038d4af0 | -11.78135 | -45.04172 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b45250f-5957-33f5-bd1a-68a3c964c38a | -8.21109 | -43.35135 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3db86a30-732a-3800-9092-e8cae5283021 | -11.78618 | -45.04518 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 544d44f4-3a20-30d9-88b8-0be69a0c36d7 | -9.09808 | -45.03181 | 2025-10-10 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bde76300-3fac-314c-b94e-7947181fc6c1 | -7.26584 | -44.10358 | 2025-10-10 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79b059c9-e2f3-39cc-b965-c2e083a3e70e | -6.45898 | -44.57991 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6885f5b-bfcd-31fe-b7f6-5369838a9b3e | -8.50194 | -46.11371 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5591f426-3658-3f3c-a9c3-b484f870e8dd | -7.26105 | -44.09998 | 2025-10-10 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a674d982-aa52-3c5c-b368-386f068a289a | -6.59011 | -44.62793 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d370147-8ebf-3768-9def-84850e1398df | -7.67768 | -42.39091 | 2025-10-10 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f54d1345-101d-31ec-982e-6df5b8ee9a4b | -11.82462 | -47.09396 | 2025-10-10 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12e05f56-0374-359e-a474-ae3d16be2812 | -6.81658 | -42.79833 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 291de46f-4166-3d09-8f0a-24585b8f6bff | -11.46549 | -41.89666 | 2025-10-10 04:51:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c3d1a4b-12d7-3a65-a49c-2544fdcf838f | -12.63437 | -45.06421 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 12e816b0-339a-36b5-85e4-c25e9aaf3b3a | -8.49806 | -46.14196 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 414c06be-a7d2-3a7f-8165-e3a555ba68b4 | -12.85645 | -43.81678 | 2025-10-10 04:51:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afa735b9-671b-3b5d-a6ce-09750d838d5a | -8.1705 | -43.31721 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f338d08-1dfc-30f1-8776-08ba104fe9b0 | -8.4993 | -46.09878 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37ab078d-673d-3dc6-bd98-35c3d070a348 | -7.5 | -43.1116 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea19173f-4071-3aa7-8492-54859012ad79 | -8.50457 | -46.12859 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4e733a1a-c90b-3724-b341-bf84b4454d5b | -12.64886 | -48.31812 | 2025-10-10 04:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf3047bd-62fd-3a71-8418-0513a01989a8 | -6.58584 | -44.21667 | 2025-10-10 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68d8fdfb-8c18-3b44-9858-85d6a4c1c285 | -13.06084 | -43.83996 | 2025-10-10 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66faa1c9-f951-3dd8-a233-bb87a713ccb4 | -12.77474 | -45.7803 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c386619b-2669-3c9b-9059-054c09a13c4f | -15.07958 | -46.58645 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 679c3676-bea8-35c5-aded-f91c66567dd3 | -14.9418 | -46.76217 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22a78f94-918e-30ad-96d1-755ab3b3a158 | -14.68133 | -48.05852 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8b4124a-35c6-350d-9f25-5c20f1004103 | -17.94239 | -45.03448 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 762c6619-89e9-3104-8797-6576c633aea1 | -19.58132 | -44.04272 | 2025-10-10 04:53:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25bafd79-f983-3012-bbd8-e0ab2c7e8760 | -13.24739 | -46.47488 | 2025-10-10 04:53:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 839b1be5-bf07-33e5-9b3a-a77839851929 | -15.46607 | -48.53619 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5262adba-06ff-3aa4-9849-2916d452e2e6 | -15.40752 | -48.05058 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23fed293-bd13-34d7-96c7-a0fa5ed2a411 | -15.75239 | -48.98516 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5789a497-89d6-336c-b136-6e9ebe2e3ce0 | -14.2382 | -49.08962 | 2025-10-10 04:53:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c009095-8cb7-385f-a171-e6ac592cfaf3 | -16.27974 | -47.17835 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28dde74c-c64f-3e8c-8fe3-2dd721633a53 | -17.7181 | -56.78428 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fc092b17-56be-3141-b682-2f42d3ff0824 | -15.23989 | -47.16103 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b310be8a-5ee1-33f5-a295-4468179d70a8 | -13.32695 | -48.47789 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 083d2882-7b68-34c5-b80c-759ce56d0618 | -14.26264 | -45.87087 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc76207a-9d62-345a-addc-3a7f202340a9 | -15.2363 | -46.37619 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 517b757b-e0d2-3ad5-9ed5-37d7f6ce82c4 | -13.28437 | -48.00823 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 187e63dd-54a9-3a6f-bedf-d3bf17d0e944 | -14.27128 | -45.88437 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41971dce-c81a-3673-8c0f-31c7a80bcdc7 | -18.01604 | -45.01944 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3e28b8a-fe1f-3c3a-a456-377481fd2265 | -15.46468 | -48.5335 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37338379-fc42-3705-9a9d-56efee7dee51 | -14.98908 | -47.2015 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e8b4aa42-be40-30b1-a1ef-889e1136dd97 | -17.90187 | -57.50336 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 60e47de7-1924-3a8b-b4ed-6b2e59232491 | -17.85529 | -57.65363 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7071a7ef-3354-37ea-ac76-70e89f0519d7 | -18.02201 | -45.01659 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7e37934-b6ec-3b1a-a8c9-42d944f7a245 | -16.00515 | -59.54752 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 415ce55f-56ea-301a-91f4-6ef85ea5cdbc | -13.40982 | -47.62778 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1922d700-5c44-3e15-bb50-a42183ba0f99 | -13.26592 | -48.03186 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8906db25-a495-325b-9992-55277ade2115 | -11.72249 | -62.97646 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34dd8af4-d101-3af3-9190-aa18528c25c1 | -13.80469 | -45.82046 | 2025-10-10 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ad4dfa0-eaa3-3084-9023-511c97d66148 | -17.89027 | -57.50921 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9be02f2c-0aca-3106-b356-e3261288707c | -13.31328 | -48.47585 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea887ffa-1084-351b-be82-9a70bdb10c18 | -13.83638 | -45.81318 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de752773-60e3-3c6c-95db-6bb0dc7ac029 | -13.37527 | -47.75331 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ee47a46-a632-3f6a-a28d-3b3633530552 | -14.92922 | -46.78585 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| afa7ecfc-40eb-3a97-981e-3809a9cfdc92 | -16.01193 | -59.55452 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c24d5f1-a4bc-3cb4-99b3-5f91574e1d5f | -16.68944 | -47.59091 | 2025-10-10 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a86c057d-087d-38fd-8823-8c5c82ef5552 | -14.37352 | -46.00459 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 978a49d5-db83-34b6-b27f-bd3ad19644be | -15.74773 | -48.98825 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ec19c5b-4076-3ca8-a04a-fc6500dba44c | -15.4062 | -47.9982 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f4a7151-45fb-370b-8207-7885bdb6bc16 | -14.40381 | -56.45327 | 2025-10-10 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d6127e1-4174-3682-bf54-90d97544e597 | -15.33334 | -43.19129 | 2025-10-10 04:53:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| dcb93a85-833e-30d3-bf18-e5d61f7647ba | -14.93701 | -46.76606 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1ec6f6e-5d9e-347c-bcc5-17395b83009e | -13.37583 | -47.74905 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38612011-3541-3783-928a-12e41e93c96f | -15.74823 | -48.98436 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdbd830c-5cd4-32bc-8d6c-c86de98f15f1 | -18.04868 | -44.97826 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dcc38087-149d-38ac-98b0-5815bfdd6eec | -13.8464 | -45.85679 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bc09bdb-7913-3efb-984b-505ba52e4121 | -13.26701 | -48.02381 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9056a82c-150e-34a0-9312-cb1e229f2c72 | -16.13041 | -48.43815 | 2025-10-10 04:53:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab060e79-9de8-312b-b0c8-103e4eeb5d5e | -18.02163 | -45.02041 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73d0cc0-67e9-32b7-bdad-85c27f8e6522 | -13.3228 | -48.47692 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e4cef39-1241-3cdb-aab1-bb14d052ebf0 | -13.32329 | -47.73943 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1aac5c7-320d-336f-b1e0-9ec1d21d3b1c | -17.895 | -57.50213 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a83bdfe8-39fb-3b01-b4d2-e127775cbb7c | -16.05549 | -48.07295 | 2025-10-10 04:53:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87741eeb-e1d3-3265-b5e8-bdd6420fda2a | -13.41267 | -47.25322 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f2b4e76-51c8-335e-bb6a-2ed500c96e4a | -17.81885 | -57.65853 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 293e79e7-2b28-3930-83fd-9e394fcbd701 | -15.09356 | -46.59404 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25808619-b6a1-3b06-8ae1-a83f9f4cb193 | -13.84247 | -45.84713 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d691db0c-84e0-3721-85ee-1692cd599705 | -13.30745 | -48.0 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ec53480-7323-3c64-9f1c-165d28c87680 | -14.9371 | -46.76049 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8607c769-ffec-344e-b468-68c25df582ff | -14.98973 | -47.19642 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 01ff7f23-dcfb-33a3-815d-eea5d2391931 | -14.89542 | -47.22943 | 2025-10-10 04:53:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87dc9848-937a-396f-9185-603157db5746 | -13.82923 | -45.78759 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ce1af4-26d0-3ff5-b624-7c290461b731 | -14.68077 | -48.06293 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README39.md)
