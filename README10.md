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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08be146c-a229-3020-a5a0-4d9e517ceb22 | -6.76371 | -41.18675 | 2026-08-16 03:53:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 086b3e78-b936-3b4f-909d-e46d811bc213 | -3.34681 | -43.51412 | 2026-08-16 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a729d6f3-dc78-3ff2-9c6b-24f90c95a983 | -7.81239 | -44.10147 | 2026-08-16 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef966a4-11c6-3c22-8248-86e07df8146b | -7.00581 | -41.43093 | 2026-08-16 03:53:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe04f77a-e48a-33c7-98d2-93608c6b5722 | -7.2068 | -43.15732 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f53ebc7-04f7-37fc-92cb-0841a643ffa9 | -6.28106 | -47.73126 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8769ed4-5e3f-3ffb-8563-154e293440cf | -7.22115 | -41.53712 | 2026-08-16 03:53:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b5dc6de-bfd2-3a3b-b076-406e18ddbdb8 | -6.28397 | -47.73575 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b8fa15f-c3bb-3772-81ec-6a1af960d75f | -6.92922 | -43.63206 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cae5409d-a047-3e80-8fae-b2f1e5cdeaf9 | -4.10949 | -42.50191 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 271534fe-9083-3c4c-b2db-7a5c07dc9657 | -6.88831 | -41.95866 | 2026-08-16 03:53:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6bad68c6-5290-33f3-a7e0-16c550fbf5dc | -7.25462 | -44.69404 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3cad4a8-81b8-392e-a2b6-3a7877b170b2 | -7.57903 | -45.02938 | 2026-08-16 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f542d0d1-15a3-342a-9c00-98a4f97e2439 | -5.62971 | -44.11164 | 2026-08-16 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff2a44cd-5eea-3dea-a2a1-e73123fd9335 | -5.63521 | -39.50955 | 2026-08-16 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5014cd65-ea86-3e98-addd-c80d8aa2c29f | -6.30757 | -43.62617 | 2026-08-16 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 992db3ac-4ce9-3e5a-87c2-1fafbfd08ba3 | -6.95931 | -45.90235 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a7ba37-a05f-30b4-9efb-d02cac44f114 | -7.25354 | -44.69808 | 2026-08-16 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07d72452-1b77-3e37-9040-495ffebf70b3 | -7.22195 | -41.53231 | 2026-08-16 03:53:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9cb7994c-342f-3845-912e-5cce7734d397 | -7.01354 | -41.43209 | 2026-08-16 03:53:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| caeda8d4-4711-3f3f-a3f5-64bf7eb61e0a | -7.20501 | -43.15417 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c0750492-13a8-3aad-955a-c94a76c4451b | -7.27348 | -44.67095 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4526bae3-c44c-30cd-88e2-c7cd833a1e4b | -5.62884 | -44.11657 | 2026-08-16 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69ecd63f-8246-3144-8d36-531b509a9697 | -4.09152 | -42.50317 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ccfabb61-0bf1-32fe-b6e8-dfa3980d3475 | -2.8283 | -46.73401 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1561a4-729e-3983-abbd-bf1c63fce176 | -6.9748 | -41.29548 | 2026-08-16 03:53:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59d998ec-90e5-3464-b88b-646f8bed34db | -6.20378 | -47.73476 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f5e37c9-4035-3900-9734-026f4c56b995 | -2.76498 | -48.57529 | 2026-08-16 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81049dbf-7d31-3d6f-afea-8fc58cc9ee32 | -7.36724 | -46.84607 | 2026-08-16 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5feec36b-97fd-3b0c-89d6-3865f291094e | -6.9329 | -43.63732 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b0c2999-1e0a-3c5c-a213-141b22908a51 | -8.93843 | -45.46729 | 2026-08-16 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30b81f9a-32e8-32da-8abe-593259806e9a | -6.95989 | -45.89913 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 037cf1e3-83fb-33ac-8a39-ecd4e4a882fb | -6.88239 | -44.9707 | 2026-08-16 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8095c34-9b7c-3f7b-be3b-4e0c4dcd961a | -8.4067 | -48.48591 | 2026-08-16 03:53:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21205782-0834-3af9-8582-a0067d844afc | -6.98074 | -45.90232 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a6f22c1-fe36-3477-ad7b-2f1b709b0553 | -8.79762 | -45.79351 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4231cfd-79df-3c5a-8060-fb8cd8913ccf | -7.27469 | -44.71797 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d9c8e24-81e0-3f38-a82c-7946d7f60796 | -6.21371 | -47.73204 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ae0b409a-f862-34e0-9317-47fca22b4f9a | -7.01155 | -45.90973 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e935215-a51b-321a-9b4f-2ed5e637bbc8 | -7.2731 | -44.66978 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4a017f3-827c-33ca-acc2-6f4d51211a09 | -7.00107 | -45.90844 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c221822-caa8-3274-9ae1-f668ec8ff3d1 | -8.40071 | -48.48478 | 2026-08-16 03:53:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ed330f8-cca8-376f-b015-79f83550f47c | -6.30911 | -43.61718 | 2026-08-16 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a29d8c67-e545-35f4-a601-74f4d31ff4af | -6.99415 | -45.91721 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbb07d84-20c7-3cdb-a226-988f89efd86d | -7.81381 | -44.0998 | 2026-08-16 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62dfaddb-73aa-3f35-995f-e3e5206c0274 | -2.82756 | -46.73829 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ccdc0fd-9f6e-31cc-a89d-a314668070c5 | -7.01106 | -45.9125 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c9099fc-c909-3d26-b010-706d48f572e3 | -5.25819 | -47.70486 | 2026-08-16 03:53:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87316503-1ece-35c0-9ebc-090993a2702b | -7.20752 | -43.15321 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85c184c1-cce0-3460-9249-e1bc7d7df003 | -5.34132 | -43.17968 | 2026-08-16 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74345b49-d6cb-3637-8626-2b2efa22a12d | -8.35113 | -45.97948 | 2026-08-16 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a22ba974-4bc6-3aa7-a40a-41293f6b13b9 | -3.34978 | -43.51188 | 2026-08-16 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2312e394-9044-3dac-90a2-04cab5abbdf6 | -8.79817 | -45.79037 | 2026-08-16 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c27725b6-2a94-3694-87a3-7029a18998aa | -7.82206 | -44.10594 | 2026-08-16 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e18ecf5-aecd-365b-80c2-51afe53ddd45 | -4.10154 | -42.49636 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b70f978c-d2c7-393f-a618-b1e2c5275de7 | -5.21601 | -39.52233 | 2026-08-16 03:53:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a5a45e9-2316-36d7-a2ad-813c6f9f45de | -6.87961 | -44.97146 | 2026-08-16 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e345aaa-96c7-33f0-a963-43e1c1fc9d28 | -8.34133 | -36.57249 | 2026-08-16 03:53:00 | NOAA-20 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51548eae-54ed-34a2-a758-afc276fb7fd5 | -6.86318 | -43.87624 | 2026-08-16 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e34d091-8cd8-30f1-88f9-deae24e98ee2 | -7.00001 | -45.91439 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0ee9159-d6d4-35b2-bbe7-2091d3df1b5b | -7.0063 | -45.90911 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf19764b-a8d2-326b-b593-42a1ae696a06 | -6.21882 | -47.73756 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 970b006b-f123-3349-98c5-c34e5909a15e | -4.09221 | -42.49904 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4a3db002-ab7f-3fcd-aef6-9bed05cbe1ac | -4.10585 | -42.49708 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e1246d38-959f-3bb3-9273-2f4ddefd444d | -7.25919 | -44.69375 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc2e9947-2169-3aa8-ac27-c39007b92e04 | -6.2934 | -47.75091 | 2026-08-16 03:53:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4f517b7-5ec6-3b17-99b6-2e44943ece30 | -7.22327 | -43.16428 | 2026-08-16 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd995fc7-b31b-3298-aa59-61efc565839c | -2.8217 | -46.73727 | 2026-08-16 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a3715fb-2ae1-3dae-a04b-cfe55b01e44a | -6.30834 | -43.62168 | 2026-08-16 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a5ecaecc-011c-3b43-ae0b-6ff113154436 | -6.99358 | -45.92046 | 2026-08-16 03:53:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3912b325-e2df-30cd-8307-d47ae8815b4b | -8.35568 | -45.98339 | 2026-08-16 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| baa02d2e-a5fc-3bf5-8b34-c249c19e96ba | -8.53771 | -39.55571 | 2026-08-16 03:53:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5e29255-db18-36da-a997-944af43a2061 | -6.20698 | -47.73536 | 2026-08-16 03:53:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2f2aa6e2-1c0a-35dc-a0db-a558c67e5c6f | -8.81015 | -37.73611 | 2026-08-16 03:53:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e132c244-0aea-32cb-a165-46a769af306e | -4.09083 | -42.50729 | 2026-08-16 03:53:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 16ca1005-330b-3640-916c-5f5d971ec52a | -7.0012 | -41.4348 | 2026-08-16 03:53:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 13ab69b5-fed9-3ff2-82b7-dead84cf20bb | -6.67762 | -43.99324 | 2026-08-16 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 181839c8-7bf9-3f62-8301-0a8ca610588e | -6.91061 | -43.63357 | 2026-08-16 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 891a4e49-9b86-3f9f-9bc9-e6be32125a6a | -8.35168 | -45.97647 | 2026-08-16 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93f6d69e-0e2f-318b-95a4-e9cd53daaeb0 | -7.27381 | -44.72313 | 2026-08-16 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be058272-bc15-3b53-b671-978a05b35ddb | -7.27488 | -39.31889 | 2026-08-16 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18888465-532b-341b-9cb2-9a76901c1495 | -10.53932 | -44.86745 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9900881d-7bcc-357e-b75d-21f7b083aec8 | -12.23503 | -43.14534 | 2026-08-16 03:55:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 777868f2-38d8-335f-be72-9e77782cb80d | -11.45229 | -46.61142 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3d2c78c-b7f9-3caa-bbc3-1d9cd782fd42 | -12.68207 | -48.47103 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6ece6df-5b60-3542-a896-808865fd81a5 | -11.90003 | -45.97416 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b0ed65f-66c2-3c31-9a20-494d1704d910 | -14.48583 | -45.6789 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab4582b6-28ca-3063-8b93-3bc029eb4136 | -10.35678 | -46.68325 | 2026-08-16 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4af5a06f-c347-3b81-92a5-fa28cf561885 | -14.3793 | -51.90133 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4677c95f-f788-38c2-a9a3-f0b5bb984564 | -11.07308 | -47.27938 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f172288d-5c20-3ca3-9431-9fba3a21881d | -14.38706 | -51.91188 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f58aabb-0514-341f-8042-3a327a719509 | -11.48564 | -46.59554 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50f2814c-2738-396f-8394-06118a0e8f35 | -15.0675 | -47.02235 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa956b8d-10cd-3706-9c9b-728605dae5ad | -13.43688 | -43.84324 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03a4a1d1-d0c6-3b8b-888c-392269919e49 | -11.90481 | -45.97508 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2909dc7b-91ac-3c81-8140-d44ebe29cf44 | -10.53733 | -44.85244 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27dd6bde-53f9-3663-8867-6716ac2a735c | -13.69932 | -46.27022 | 2026-08-16 03:55:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf5b388e-e63e-3f4f-9114-37dd35344345 | -12.56372 | -47.85742 | 2026-08-16 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0ad6096-6d24-3712-b0e5-2eb547285022 | -11.0697 | -47.26829 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29e288e9-e30e-3a5c-998b-5cdb5e0c18ce | -13.37969 | -41.34592 | 2026-08-16 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |


[Clique aqui para ver as próximas entradas](README11.md)
