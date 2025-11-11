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
| 90f74577-e245-3811-a938-7a74ba9a1a94 | -5.77768 | -44.02786 | 2025-11-11 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18376aa6-1971-3ad3-809e-f894bfc847cb | -7.19585 | -40.17363 | 2025-11-11 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc674248-e21e-32c1-b9ec-f5b7438f0754 | -7.15001 | -41.73915 | 2025-11-11 03:40:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d661303d-560b-37b9-9387-6466f035a0b8 | -10.22405 | -44.04245 | 2025-11-11 03:40:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 251474b9-0ed6-30f9-a867-0b68b3d3aabf | -10.28178 | -36.30021 | 2025-11-11 03:40:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4bfe529f-7ab4-30de-9180-7828c7632961 | -5.51253 | -44.39462 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 460bfbef-7918-3091-99a1-224d6d674216 | -6.44386 | -45.66253 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc18ca98-8f1a-3696-a6a2-6209302a96b2 | -9.9796 | -44.45647 | 2025-11-11 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 562a139b-1714-3610-885b-0f16c76e1a0a | -5.65478 | -41.05785 | 2025-11-11 03:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 509ec1d1-7629-346b-97d8-70795e654ef8 | -6.55301 | -44.46439 | 2025-11-11 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 873eaabf-7c9d-35ac-8009-a753b3712176 | -4.72797 | -46.45467 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328ab7da-2558-3a75-bc11-e8cd1755b815 | -6.06859 | -45.81187 | 2025-11-11 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1e49fa2-0613-31e0-ab65-65cf25444822 | -7.06615 | -39.67568 | 2025-11-11 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5dcda7d2-256c-3940-8947-345e30c06dee | -7.6915 | -35.09528 | 2025-11-11 03:40:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ab8ace71-088b-39f9-bced-242ff42bc6f3 | -5.77846 | -44.02332 | 2025-11-11 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51dcbf11-41a6-3782-b730-28e5fad31693 | -6.4365 | -45.66643 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2fa9f3b-0e0f-3240-b83c-187fee6ae865 | -9.98033 | -44.45271 | 2025-11-11 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65517893-15d6-3f2a-8499-c237d5339503 | -6.56123 | -38.69793 | 2025-11-11 03:40:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ccb7715-a087-3b07-a3cf-eb08caa4bfab | -5.64251 | -41.08182 | 2025-11-11 03:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d507212-9a48-3392-8741-c6da2b69aad4 | -4.76024 | -42.66676 | 2025-11-11 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7bb07ce7-cce9-3c6b-a5c5-2318b2ed3c21 | -4.72084 | -46.46101 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 91443d1b-30a9-34e3-af08-109943164e30 | -6.43747 | -45.66121 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a08fa3dc-79ea-300c-bf66-bd40796c57b5 | -5.12785 | -44.72227 | 2025-11-11 03:40:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17ff8f51-62ab-3a6a-aadd-9fa973e421fa | -4.72241 | -46.44608 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| be845d6e-3975-3e0a-a967-2966e00a5469 | -6.09337 | -41.56982 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e90a7ee-8493-38c7-a476-c07ff6ddacd8 | -6.5503 | -44.4666 | 2025-11-11 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07eb1427-4f66-3c40-8530-7122ef8a5b94 | -10.50247 | -44.93333 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3533c1a6-9970-39d7-b69b-c917c5f24d79 | -5.51174 | -44.3992 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eca11c35-0059-3da4-a779-8ff80aea88a5 | -4.72201 | -46.45428 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 22dda4c3-4edb-3ac1-82ca-ed3c0023e0ad | -5.39919 | -45.24307 | 2025-11-11 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2351f286-577f-3aab-a284-02403f33ff69 | -10.50012 | -44.94558 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42c72965-16b6-3a5b-81a8-e77d86be157b | -11.05223 | -45.39462 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 536ec58f-356f-3405-8188-68ef3a4870e6 | -5.4233 | -44.83545 | 2025-11-11 03:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45be7fe4-41e8-3684-b908-939bbe197330 | -6.08786 | -41.56727 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a4ab357a-a8ad-341c-975b-c6d251df95d9 | -6.09049 | -41.55735 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8bf0f15d-bdae-3fae-81f4-1878694daf69 | -4.76085 | -42.66327 | 2025-11-11 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9ea8f953-78e0-34c7-92fb-9d5df6e5a7f3 | -5.5124 | -44.40081 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57143d5e-33b0-3bc6-b4a2-8f781bfc170f | -4.59621 | -45.49134 | 2025-11-11 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c5ff943-7615-31ca-985d-68ae8d950561 | -4.57943 | -44.31057 | 2025-11-11 03:40:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cde867f-b188-3413-acef-c24acebc3e94 | -5.66343 | -35.60725 | 2025-11-11 03:40:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f6a2a415-0050-3834-a33f-cb5065f7873c | -7.8904 | -42.48006 | 2025-11-11 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f25d455-afbd-362b-8355-2af899c02bf0 | -6.37168 | -41.07797 | 2025-11-11 03:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f33c1b37-0358-3b80-98e0-eac0ac64d25c | -5.41819 | -44.64745 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdf8dd80-e82d-3208-85e2-e61b18cf7d47 | -5.12897 | -44.72507 | 2025-11-11 03:40:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a4a485-ac59-37d7-a918-0d6ce3ab430e | -4.7554 | -42.66235 | 2025-11-11 03:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0792faa0-e240-36d1-a4e5-d74d483fa0ec | -9.36048 | -40.33722 | 2025-11-11 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eaa16203-00fb-3b55-a06e-4026b3ce1484 | -9.35975 | -40.34135 | 2025-11-11 03:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e05baee-6bbc-3f55-bb2b-728e01b1e55b | -10.49438 | -44.9445 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5817d4b4-4cbe-344d-ac73-9ac68a1565df | -9.67178 | -43.90732 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e672106c-6917-3ccd-9fc9-d957c166c0ff | -5.77632 | -44.02464 | 2025-11-11 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fef18bd-7b30-3360-81f1-bcd922c46335 | -5.50806 | -44.39044 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 067259db-40c4-3f00-ae67-2520abd48d5f | -6.74758 | -34.96647 | 2025-11-11 03:40:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53b29320-11d0-39af-95e7-59812e599d68 | -9.18941 | -41.02978 | 2025-11-11 03:40:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2ca47b9-4d70-3e6a-90c2-3a5ea2b27cbf | -6.71954 | -38.55229 | 2025-11-11 03:40:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 45ac489d-00d8-32af-ae63-b47d79900d58 | -5.51405 | -44.39165 | 2025-11-11 03:40:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef365c58-3eff-339a-89ca-35c52847230a | -5.42349 | -44.65322 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fab1168d-1701-3227-9baf-ded2567e0ce0 | -5.95105 | -36.75952 | 2025-11-11 03:40:00 | NPP-375D | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 691782c4-06bb-3c81-847c-45e6210c9f87 | -6.44286 | -45.66785 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffe0a440-8c3d-3a56-95a5-98704bbc7b98 | -10.84806 | -44.94258 | 2025-11-11 03:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d29b438f-bc22-37e6-8394-38e2f2d3429f | -4.6477 | -45.75957 | 2025-11-11 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aadcabc1-a934-3ed0-9329-6af6121bbdaf | -10.49594 | -44.93636 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffc3f39d-c8c4-30cb-a76c-495dde780a97 | -10.49516 | -44.94044 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 397a39a1-cae0-3153-a842-e82d16abfa76 | -7.27133 | -42.1632 | 2025-11-11 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68b0a4c9-23ee-3240-82cb-6ad1a9e8a76f | -9.38008 | -36.043 | 2025-11-11 03:40:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5b064681-eb53-3f4a-9846-039ea2a946db | -9.6725 | -43.90139 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c91ebfe0-12f9-37f1-806e-326316490fb0 | -4.86885 | -46.68672 | 2025-11-11 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e623c379-2402-3224-9999-0be44ef40145 | -10.5074 | -44.93858 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a54f1c2d-9dcf-398f-82f3-e1562659b427 | -5.77552 | -44.02908 | 2025-11-11 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab802f1c-c386-3244-97fc-96617b51b5ac | -9.67186 | -43.90488 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c910d38e-afd6-3f93-969e-cf39b30417f8 | -5.61439 | -41.07193 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78716998-1f3b-31f5-a020-6b177ec6e5df | -6.09278 | -41.56831 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d8136cd9-4e56-3258-b916-3df22dbbf5d1 | -11.05142 | -45.39878 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d829d23-74d0-34e9-8b96-08348f221200 | -5.65 | -41.05683 | 2025-11-11 03:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 055c6aa9-0755-3573-a3e9-5ea0ad0f51e5 | -7.13363 | -41.26137 | 2025-11-11 03:40:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0695fd2f-1bf6-33dc-a7d2-c68ba87e2eec | -5.43023 | -44.64581 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b6f320c-9d55-3d6d-8b4a-c1dbdddd1a34 | -4.74258 | -44.59496 | 2025-11-11 03:40:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3df65c48-d5bc-3785-8fc2-048d8fa06aeb | -4.71516 | -46.45279 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2410dbce-be48-34d2-8b40-f41c70c2cb7e | -4.88826 | -40.44889 | 2025-11-11 03:40:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d619863-8454-3b0c-be3d-5fc3c2a28ca4 | -5.63665 | -41.0763 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f75a6ea1-8502-30cf-8285-7e4b451d264d | -7.13455 | -41.25616 | 2025-11-11 03:40:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f22e5757-3e76-34f7-bddf-82fa24d1e50c | -7.06764 | -39.67716 | 2025-11-11 03:40:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ce4c0d92-d79b-38b3-bd50-0db00822831f | -6.90051 | -39.61193 | 2025-11-11 03:40:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1b80e339-8ffe-3633-b820-d77e7129e6f9 | -6.44316 | -45.66089 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82fedc23-53d9-30db-a83a-2bb831bf0c41 | -7.1352 | -41.25489 | 2025-11-11 03:40:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1449c943-b573-3ca6-b95b-1e523c5f43a7 | -8.61016 | -37.72173 | 2025-11-11 03:40:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10be36c8-39d7-3d37-9cae-18c612ee7dfe | -11.04396 | -45.40589 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a954790-d918-3646-9c75-f390f96590f8 | -5.63859 | -41.07559 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22e16dfa-ff43-3ddc-925b-a55b7c436b97 | -9.67124 | -43.90825 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 623b7446-0bd8-38f5-adb6-8b7edb68896d | -7.69486 | -35.09582 | 2025-11-11 03:40:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bb3deac3-297d-3947-949f-9f37929ff076 | -4.72317 | -46.44769 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b1ec6385-827f-3f28-987c-7a830e7e207a | -5.1222 | -45.59983 | 2025-11-11 03:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92d37ee6-6b3c-328b-9ebd-b7fc1e81d4a0 | -6.71885 | -38.54997 | 2025-11-11 03:40:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7c703a4e-b397-3c65-a289-907594b28a28 | -6.43584 | -45.66473 | 2025-11-11 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ebab17-d351-381d-9088-34944cadd44a | -5.78218 | -44.0257 | 2025-11-11 03:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab483338-e7f0-3c89-8f61-d39256f5d999 | -10.50169 | -44.93739 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78d5a67b-3750-3ef3-89f2-1adaaa0f4774 | -7.27636 | -42.16427 | 2025-11-11 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4877c971-b9f3-32cd-965e-c38bc47f4862 | -9.89173 | -47.8649 | 2025-11-11 03:40:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a4769de-257c-3afd-a154-bd076c11e2c1 | -6.59356 | -35.25367 | 2025-11-11 03:40:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69218de4-14e5-34b8-b4f7-5e85d8b294d3 | -9.67115 | -43.91067 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68102375-1040-357f-a98c-48950b9ebc9d | -4.86766 | -46.69317 | 2025-11-11 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
