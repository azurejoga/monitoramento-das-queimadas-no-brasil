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
| 9376c349-ebe5-3ee1-82d1-48426f808f28 | -4.19264 | -48.5764 | 2024-10-08 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8d85753c-9173-34eb-95ac-cc9eeb03e44d | -4.10219 | -48.25455 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5ec1ff43-1f5d-329f-a228-f684faf67ecb | -4.09283 | -48.27129 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fdadd772-2221-3d05-99e3-12228befbd13 | -4.09081 | -48.25607 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 48c9c311-69e7-3e54-a45d-bd9bc6581f82 | -3.94051 | -46.44236 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4845922-6162-3e93-a3c5-e51c7771f4ef | -3.93213 | -46.45502 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 66db2286-c44b-3dc0-8702-1e523dae9005 | -3.93062 | -46.44374 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 37c6932a-0eac-31b2-bfbe-0886830d6e17 | -3.90893 | -48.35559 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 70e20f4c-8770-36db-b17e-5b48e676ee9f | -3.90886 | -48.34569 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 19f9d854-165a-3896-befa-262f9f3e1d20 | -3.9069 | -48.34012 | 2024-10-08 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 46e13b3c-8062-37e6-b400-ae5b78e05dde | -3.8945 | -49.54657 | 2024-10-08 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 57627a81-db94-3636-ab2c-5522e9dcb686 | -3.89201 | -49.5276 | 2024-10-08 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 3494e21c-ffe1-3366-b5a9-c6e0db1903f5 | -3.8909 | -49.53329 | 2024-10-08 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9a8d047b-b6d3-3d0f-9838-a26a5eadd539 | -3.70332 | -47.61063 | 2024-10-08 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f5e0b2ba-e5f9-3bc4-ab03-3bfc05c5ccb9 | -3.70147 | -47.59732 | 2024-10-08 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c53700c4-6cde-3fe5-826d-f3bda17685dd | -3.70146 | -45.08456 | 2024-10-08 00:35:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 3e542bd4-9d46-39cb-8f4f-812c3236cd09 | -3.70015 | -45.07508 | 2024-10-08 00:35:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f987869b-8c77-3c43-9f71-40b010470e26 | -3.61474 | -44.79115 | 2024-10-08 00:35:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1825bee7-555e-34e0-88cb-dafdc932add3 | -3.60569 | -44.79241 | 2024-10-08 00:35:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4a1711ea-384d-3951-943c-11fc5d002b78 | -3.46199 | -47.6696 | 2024-10-08 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d0ce978a-4597-3644-965b-7ac92d7c95ec | -3.31325 | -47.01452 | 2024-10-08 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 73ff49aa-2458-35bb-ace2-4f29d13e6a61 | -3.28697 | -47.12861 | 2024-10-08 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| e684725f-cc19-3511-9a1f-c31207684f56 | -3.28531 | -47.11619 | 2024-10-08 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 10e2039f-e52e-3c93-b817-58a386cde0a1 | -12.53468 | -49.49084 | 2024-10-08 00:35:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d147f108-16f7-3b97-848c-1fef38e9e6b0 | -12.47258 | -47.3181 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c5f8c133-3930-3a3e-b5d0-23aea4187e06 | -12.46802 | -47.32494 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f2f19f2b-2247-3556-9a82-9f8923c10ac5 | -12.46585 | -47.3074 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 18abf3f1-7c0c-386b-95ba-d94845d44cec | -12.4605 | -47.31976 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| be29447d-df50-35d4-a345-35df1c0c39ca | -12.28579 | -47.63476 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f65fa9e7-65a6-3439-8413-c03fa7e1e66d | -12.17051 | -47.7741 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| cb8fbd9b-c7fd-3241-9029-0406ec444056 | -12.16825 | -47.75586 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c8aee808-8d6f-3588-93db-09b4bd130854 | -12.15979 | -47.76896 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6a0a0527-90f5-3ae0-a5d7-bc070e06a0b5 | -12.15796 | -47.77521 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| fe031d0a-40b1-3b41-898d-bfe990b6921d | -12.15769 | -47.75076 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4eebe82b-d24f-338a-9c15-2998799042ca | -12.15576 | -47.75726 | 2024-10-08 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| eafc854b-b7eb-31a8-b9be-bc99d9068805 | -12.0437 | -46.85663 | 2024-10-08 00:35:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 91c24f7c-87a7-3da5-b055-eafb46f5f2ec | -12.04231 | -46.86667 | 2024-10-08 00:35:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| dc837292-a0d8-3086-9724-a7b2d104b2b9 | -12.04043 | -46.85074 | 2024-10-08 00:35:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 2ce0525f-0ebd-30d1-965c-a84c694fd4f3 | -12.03212 | -46.85806 | 2024-10-08 00:35:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 791160ae-c79d-3ee3-ac79-00be142f308c | -11.35682 | -51.02916 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 45b2c05d-7c71-3146-bc5a-d70833664c65 | -11.36042 | -51.06244 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2a5441fb-6dc2-3f0d-824c-32848d5ad883 | -11.35182 | -51.06839 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| c1a126db-ac5e-3baa-b98c-67a4d5ee91e2 | -11.348 | -51.03513 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 358.1 |
| 3a18e011-4d66-3ef7-9be7-afe41c76ae26 | -11.34442 | -51.06431 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b2e8c597-e64c-3ca7-b5d1-f754e8d69585 | -11.34421 | -51.00206 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 54987177-624b-3019-9200-661c81f3b2d7 | -11.34086 | -51.03101 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 680.4 |
| 99193a80-4607-3067-8337-25ad039d07cd | -11.33731 | -50.99789 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 34d44fc2-87ff-3649-96f9-e2fe5998979f | -11.33581 | -51.07022 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 18deaea0-428f-3ea5-9be0-392099d7cf21 | -11.33204 | -51.03695 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 374.4 |
| 30be0737-24c5-383a-b797-1b8b2be1617f | -11.32841 | -51.06617 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a8f1fe0c-85c0-3703-ab28-44cdf4e59cfb | -11.32828 | -51.00386 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 200e4cfd-b44c-3690-a6a7-76e2a6cd9f72 | -7.60148 | -41.71714 | 2024-10-08 00:35:00 | TERRA_M-M | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4085da42-5fad-33a4-abf0-879daf1b028c | -7.64925 | -42.51746 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| e8999949-af45-321a-8570-a2de4243ef8d | -7.65049 | -42.52631 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1aed4419-926e-3afc-95ce-f924ab54e877 | -7.65561 | -42.49847 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 568cc115-6306-34e5-a4ff-b203d463f8bd | -7.65685 | -42.50733 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| acb264f6-e24a-3e6e-a0f7-bc550055c44f | -9.53818 | -44.07214 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| efdb4f59-b5a3-34c4-b482-9342e40dceaa | -9.5395 | -44.08196 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bfcc0839-1a1f-3ec1-8107-9c01a81ce10d | -9.54875 | -44.08068 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7e001cb0-5f90-394c-8d56-04774be16d4d | -7.34731 | -43.66596 | 2024-10-08 00:35:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 49d19fb1-0bae-3a84-80fb-f069c236e853 | -8.00576 | -44.37883 | 2024-10-08 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 06b2bbda-c421-3dba-9a1c-3433f76e39f9 | -9.9565 | -44.11529 | 2024-10-08 00:35:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c94e4a0a-5330-3dc7-992c-a10350d9b8e9 | -9.9494 | -44.11198 | 2024-10-08 00:35:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a759ebee-976b-3281-a826-b2d3b92b5e4c | -9.53122 | -43.00023 | 2024-10-08 00:35:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| fc80f63e-077f-3a1f-8a24-bda46b93ef35 | -9.52998 | -42.99115 | 2024-10-08 00:35:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 1c60b23e-422a-31c9-95a3-63a313e32096 | -9.43116 | -35.78232 | 2024-10-08 00:35:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 3daf6d99-85c9-317d-85fc-874b5ee69b00 | -9.42801 | -35.7626 | 2024-10-08 00:35:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 775c00fd-1ef2-37c8-ae50-9ec65dce6d5f | -9.42484 | -44.12444 | 2024-10-08 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e272e50-62b8-3ff1-b720-fad97f841a47 | -9.12912 | -45.52868 | 2024-10-08 00:35:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7f8e1b63-6edc-3155-8d32-c033c9e1b765 | -9.11912 | -45.53008 | 2024-10-08 00:35:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e0cd59f4-420a-3a45-afcd-0825f346f528 | -8.80499 | -41.04322 | 2024-10-08 00:35:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 69049c17-0fc9-3c48-841a-cf34b099f11b | -8.80365 | -41.03393 | 2024-10-08 00:35:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 10182b04-fae1-3a1f-b8a9-95443b7342f0 | -8.75894 | -44.15698 | 2024-10-08 00:35:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0d5de93-17b4-3a67-a054-0faa28bc84de | -8.41759 | -41.95277 | 2024-10-08 00:35:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5cd812f1-46ac-3551-921c-87f4e29873c9 | -8.37664 | -40.43801 | 2024-10-08 00:35:00 | TERRA_M-M | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 32.6 |
| d61559fe-8b9d-35cd-8f7c-970640947d21 | -8.37521 | -40.42815 | 2024-10-08 00:35:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 57af9a08-5c8b-352c-9592-d477a621843c | -8.32862 | -44.11292 | 2024-10-08 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4714b6e2-b9a7-36be-9862-bf1013f0a056 | -8.2948 | -44.06928 | 2024-10-08 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 280dc7df-986e-3636-8e2c-cc6c53245b41 | -8.14162 | -44.42355 | 2024-10-08 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 99dceb24-85c6-3e59-9ddf-71e0d3b8e6e8 | -8.14028 | -44.41373 | 2024-10-08 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 879a2a2e-9929-3a84-81be-3d12d3753cc4 | -8.00445 | -44.36908 | 2024-10-08 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 83b0bac2-8ebd-3e8c-8608-8d89efe26d9f | -7.97699 | -40.02534 | 2024-10-08 00:35:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| dfd52d77-57ca-358f-ba16-9e3b284399c7 | -7.9746 | -41.61963 | 2024-10-08 00:35:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 21d81987-d14e-3738-814c-dfb2b28e322d | -7.86244 | -45.36815 | 2024-10-08 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0633b6d8-3b25-3940-b05d-015449d3f078 | -7.86099 | -45.35722 | 2024-10-08 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| e96d74ef-754e-3efa-91a5-1c0090f4d07d | -7.85126 | -45.35855 | 2024-10-08 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| d4d33ac5-df69-340e-a6e1-d9bc2f538ac5 | -7.82888 | -42.22599 | 2024-10-08 00:35:00 | TERRA_M-M | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ec742efd-f12c-3d08-9825-aaa8db0f0c02 | -7.78373 | -43.09574 | 2024-10-08 00:35:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 1f1433db-c02e-390e-ac44-f5336455f86e | -7.78249 | -43.08679 | 2024-10-08 00:35:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 9e4493b3-866e-3553-bcd6-0bd965179d35 | -7.77487 | -43.09698 | 2024-10-08 00:35:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ec7da3a4-3612-334e-ae3a-08f007e4c43e | -7.75401 | -45.1713 | 2024-10-08 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 272ff498-d8ee-3bea-902d-ab20c6cb68c1 | -7.73201 | -43.04849 | 2024-10-08 00:35:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fc297544-e454-30eb-aa15-b66e6c36b5f5 | -7.66444 | -42.4972 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b807e662-9e6d-3e6c-8d04-405b291bec26 | -7.65808 | -42.51619 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 87c6891e-4919-34b5-bd8b-d79320935eea | -6.83315 | -42.80679 | 2024-10-08 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 6ce419f7-83c2-3e9d-baaf-282ad80170ff | -6.83192 | -42.79795 | 2024-10-08 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d76a7d10-e9ff-3d0b-a631-0682c2ff725a | -6.69726 | -43.96459 | 2024-10-08 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aea0c08e-35f3-3e73-a9c7-1227eba82e46 | -6.69598 | -43.95539 | 2024-10-08 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3c4a9901-9069-39c4-9a5c-743c1eee14c9 | -6.54367 | -42.71307 | 2024-10-08 00:35:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6f9dcc51-c085-3148-ae90-577284267a0a | -6.54244 | -42.70423 | 2024-10-08 00:35:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |


[Clique aqui para ver as próximas entradas](README11.md)
