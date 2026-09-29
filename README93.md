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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd8be98f-7f8f-3e9b-9c56-46e316c4494f | -13.32946 | -43.94667 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 577a35a2-2eea-384e-9a0d-6cfdc668737a | -10.24537 | -38.29621 | 2026-09-29 15:46:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7dbb5d0e-5a23-3717-a95b-17921ccd36ae | -11.65118 | -43.51128 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9a90ffea-c967-3185-b329-56463999dd58 | -11.43083 | -43.47257 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| df1fb44a-f6c2-31d6-9301-9bc63986ddde | -8.84725 | -41.12489 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 09a925f8-b4a1-3276-bb72-cd3c726515b2 | -13.85614 | -43.94489 | 2026-09-29 15:46:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 571a4842-6be3-3c9d-accf-6cb63ca82818 | -11.0974 | -43.31305 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 730dc3ce-2f87-3d4c-b94f-ceba748b2eb7 | -8.05848 | -37.78894 | 2026-09-29 15:46:00 | NPP-375 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 3b9ef9af-9a5f-3389-99b6-a19316258b5e | -11.75575 | -37.55597 | 2026-09-29 15:46:00 | NPP-375 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f0ed95ed-303e-3693-9868-ed62e74766bf | -13.52018 | -40.71761 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e8f83d88-ddce-3b04-954f-b07f4bb538e6 | -11.40321 | -43.42004 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| de3fe8df-424b-3205-ac6c-2bc030787f19 | -11.68232 | -43.53894 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 75bbe8fc-b454-3203-b135-d717e9ec0225 | -13.13472 | -40.77401 | 2026-09-29 15:46:00 | NPP-375 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6cbb55b4-dc35-3761-af6f-ca9f84ea6bdc | -15.53478 | -40.85142 | 2026-09-29 15:46:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 635f4aea-7f09-385c-9acc-5a83a5c22a8b | -11.65267 | -43.52411 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 014840ef-6b5a-38be-a764-bec9ebf4b39d | -11.41568 | -43.46138 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a2b32961-9d9c-36d1-a444-fa1b610beff9 | -13.33019 | -43.9541 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 5ef7f327-05e2-3f06-9f03-0664b91fca2a | -10.90313 | -43.86225 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 794b6c13-279a-390a-9710-7e5105db164c | -13.40131 | -40.94424 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 31afae6e-75a1-3421-972a-2369406cd054 | -13.02719 | -41.04119 | 2026-09-29 15:46:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9954c402-66e5-341c-a6c4-dac6698b358e | -12.92086 | -40.04438 | 2026-09-29 15:46:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 930fd382-9978-3bd4-af70-23e5df924ea3 | -11.43287 | -43.42789 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0b5f5526-4c2f-3104-b3f7-c53201865b1a | -9.14892 | -41.04546 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2281f68e-04ad-3c40-8f50-e680c173f804 | -9.44352 | -41.81521 | 2026-09-29 15:46:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| af201780-a646-318e-9dc6-fe77a372163c | -14.64287 | -41.024 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eee8cfd2-bd70-3af6-a023-17aa6dbf15a8 | -11.42202 | -43.46238 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8c6c93f2-9bbf-3c72-abec-c0bdca012cbe | -13.33434 | -43.9469 | 2026-09-29 15:46:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 90574dee-3282-3d8e-bffe-07f635de5fe0 | -11.4503 | -43.46592 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| a91776c7-2f43-31c6-824f-ba567f8ea490 | -14.24668 | -40.43895 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 44b13e0f-0e4d-3a3a-b60f-eaf5aabfe022 | -14.37655 | -41.67144 | 2026-09-29 15:46:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 641d9fa6-abb5-303c-b45c-a80e05d38ee0 | -14.54438 | -40.73802 | 2026-09-29 15:46:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a14970cd-3bbf-3484-a347-8a5e08371ac2 | -14.2011 | -40.18277 | 2026-09-29 15:46:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2d94bb39-1639-3505-8190-1317405fd442 | -14.88193 | -40.41002 | 2026-09-29 15:46:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 99b23530-97b3-3e81-b3ef-283875f8560e | -14.916 | -41.03442 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d66338cc-f040-392b-9200-38f36cab051c | -14.81351 | -42.77282 | 2026-09-29 15:46:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3d10b230-afca-3fa2-aa3d-8918312a8a31 | -11.7817 | -39.85891 | 2026-09-29 15:46:00 | NPP-375 | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d24fa2f0-edce-391b-abba-51358846d380 | -15.51178 | -42.87434 | 2026-09-29 15:46:00 | NPP-375 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92d14542-b0aa-3bec-bc7c-ea1b8ce91df8 | -11.61487 | -44.14427 | 2026-09-29 15:46:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a1dc9b7b-370b-3dd9-97a2-30939985ebff | -15.13152 | -43.62099 | 2026-09-29 15:46:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3d2b15f0-2dc8-3936-9ecc-08ec274bf978 | -11.12746 | -43.26429 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3609fa96-6ca8-382b-a865-f50a6007a955 | -13.36025 | -40.32579 | 2026-09-29 15:46:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4de49a2b-7c98-36b5-a9a6-ebfe57b1272a | -12.34429 | -44.2807 | 2026-09-29 15:46:00 | NPP-375 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bb63f18f-0e6e-3266-b172-9f8a0f0e2946 | -15.48538 | -42.60031 | 2026-09-29 15:46:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4a7177fd-1991-3b55-abe1-68f950d92e08 | -11.31533 | -43.56176 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 98c05487-4ae7-34ba-84d4-470ec5844186 | -13.2064 | -39.03894 | 2026-09-29 15:46:00 | NPP-375 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2f793450-2aec-30b8-ac80-e7983ee85646 | -7.99671 | -36.27766 | 2026-09-29 15:46:00 | NPP-375 | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 338a4c45-d1bc-3903-b1f6-6e806f2a5b37 | -15.3002 | -42.76493 | 2026-09-29 15:46:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6925b1f1-ae2f-3a6e-9b8d-b7f26243afc9 | -11.43433 | -43.44849 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6c6b4b61-de11-32f0-b3f8-43ebca9e0a1a | -15.21197 | -39.77937 | 2026-09-29 15:46:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| da675a69-77d5-33a5-b8eb-af849df0d977 | -15.46953 | -41.00629 | 2026-09-29 15:46:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 08d806bd-48de-30d3-a1d9-2f7e85caaa97 | -15.19162 | -41.43326 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 25e8120f-982f-3b50-9bc7-eb7064f9b9eb | -13.51972 | -40.71336 | 2026-09-29 15:46:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7a172ba6-4c37-3eeb-93c0-b2e4aeab501f | -14.06182 | -40.56882 | 2026-09-29 15:46:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e563cb67-1993-3f1a-9c3c-69383400c879 | -10.24608 | -38.30151 | 2026-09-29 15:46:00 | NPP-375 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 461f1925-a21a-3ab4-b873-763de5932719 | -15.0663 | -41.94823 | 2026-09-29 15:46:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f02ba8ab-f248-3fcc-bc12-1672dc082a99 | -11.42463 | -43.47955 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7babed5d-c994-3164-9e05-95a387cdc804 | -11.39777 | -43.43315 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 18c5d8cc-6dff-3c42-8d6f-ca477417caf7 | -11.41839 | -43.43111 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 67ce1c22-c0b1-352e-b54a-e36e23c28829 | -11.65884 | -43.5169 | 2026-09-29 15:46:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 481bafb6-ab6d-3a5b-834f-d7f7ebff33c9 | -15.70521 | -40.59208 | 2026-09-29 15:46:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| bb6a25a2-68b7-37fd-b9cf-45237f7767d3 | -14.67418 | -42.84362 | 2026-09-29 15:46:00 | NPP-375 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 775698dc-96fe-36f8-aebb-11d28e8d1ce3 | -14.98723 | -41.48771 | 2026-09-29 15:46:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 74f62f27-fd1e-3f15-9532-8236f2ab6d9f | -11.68559 | -38.99199 | 2026-09-29 15:46:00 | NPP-375 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 313eaeb4-24da-39aa-9ac8-e2a58e2ca9e3 | -11.71323 | -44.51078 | 2026-09-29 15:46:00 | NPP-375 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8150666b-7d3b-3ccb-b8d5-948236b1020d | -8.9904 | -44.1568 | 2026-09-29 15:46:00 | NPP-375 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f346a7df-a064-3f8e-a6cb-ce55b47ff6fc | -14.13365 | -43.90473 | 2026-09-29 15:46:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 60de0d87-2d2d-37de-90c8-874d3925421b | -5.73899 | -35.49824 | 2026-09-29 15:48:00 | NPP-375 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c430b44d-a76e-3fd3-93be-9674681c6187 | -8.55641 | -44.0452 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| f0a87da7-93ec-310b-8397-f90398a70f10 | -7.04573 | -41.54586 | 2026-09-29 15:48:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0fc5ebfc-da78-3e8e-a1bf-8f41a08f08a0 | -8.01921 | -42.88173 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 15af85da-4d89-35ce-a408-c9c624ebde66 | -4.7197 | -44.34551 | 2026-09-29 15:48:00 | NPP-375 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9755b82a-1b67-3127-8c59-7aa26360c76a | -5.73081 | -43.73307 | 2026-09-29 15:48:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e9cb3d41-575c-39aa-bd90-f90db00998d0 | -6.89456 | -43.70841 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| a52b4c9c-d262-3d47-ab47-64e068012a1c | -4.2947 | -41.76704 | 2026-09-29 15:48:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 551e0ecc-e2d9-38ae-8b8b-319c217b8e40 | -7.01289 | -45.30535 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 56d14734-8726-3dd8-982e-2233646eec11 | -6.02875 | -42.58763 | 2026-09-29 15:48:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f7c2a9c0-12ef-31e1-aab8-c8555764d5f9 | -7.34125 | -42.07074 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| eb2f0574-9e66-349c-b27f-7e0c7f28ca64 | -4.30089 | -41.77015 | 2026-09-29 15:48:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 944897a2-28d2-351b-ac4d-c43cfbc928fb | -7.24349 | -43.35873 | 2026-09-29 15:48:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 774a6fba-678d-3816-8815-89f476d6b363 | -6.31495 | -43.6183 | 2026-09-29 15:48:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dabb0d62-fcaa-311f-aa02-edad33bb954f | -6.90625 | -43.69534 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| fcff875c-ee58-33e2-8352-388347d00a63 | -6.36405 | -35.16766 | 2026-09-29 15:48:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| bcd24bd4-8c2e-3072-b052-e0b727237739 | -7.04519 | -41.54191 | 2026-09-29 15:48:00 | NPP-375 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 9f4d32a8-10c6-38e1-ba36-c1844bfdd7ce | -6.90773 | -43.70644 | 2026-09-29 15:48:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a9aa2de8-3780-3955-a606-6b9569ffd308 | -6.96126 | -42.8623 | 2026-09-29 15:48:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ea054cc7-09d1-3238-9aae-325aad821d82 | -6.84141 | -45.18269 | 2026-09-29 15:48:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 028b31ff-694e-3b0d-8c34-310864f8ec1c | -7.42214 | -42.6238 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8559ffe0-2265-3f31-bd91-652193d78579 | -8.04345 | -42.86889 | 2026-09-29 15:48:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 94209f82-5327-334a-a924-5fdb192f96cf | -7.33677 | -42.07002 | 2026-09-29 15:48:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b96a59b8-e5db-3e5a-94b3-c33473310222 | -3.29028 | -42.66515 | 2026-09-29 15:48:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 701aed59-393b-3cce-ba23-6095c691bf05 | -6.0268 | -42.57955 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a28ea452-e29a-3819-ba57-0f9230456c1b | -7.99491 | -44.9739 | 2026-09-29 15:48:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ee2edb2f-10f5-390c-a566-46d2827aacf0 | -6.02694 | -42.57394 | 2026-09-29 15:48:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 78b9a03c-6b70-3903-a17f-ce5a8ad7baf1 | -8.36328 | -44.17649 | 2026-09-29 15:48:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c2a62d1e-dca8-395c-a342-fee79705f5fc | -8.54947 | -44.04555 | 2026-09-29 15:48:00 | NPP-375 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 228084ea-8b46-3e1b-922e-88eeeeb26718 | -7.00736 | -45.30507 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 04446923-8a4c-3a69-a707-1e38583f9c82 | -4.93424 | -45.46423 | 2026-09-29 15:48:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bc542dfd-b4d2-3c81-a597-545003ba91d7 | -7.39918 | -42.64136 | 2026-09-29 15:48:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 19ae745c-15ae-3d5b-be8b-5443324c0e43 | -7.02017 | -45.30463 | 2026-09-29 15:48:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f9370e2f-5be2-35f6-b44a-24b5f748b22e | -7.05415 | -36.66344 | 2026-09-29 15:48:00 | NPP-375 | ASSUNÇÃO | PARAÍBA | Brasil | 2501351 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README94.md)
