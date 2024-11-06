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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9413ed64-3fa5-3e92-8324-3d20c1cf4af7 | -3.31725 | -40.03663 | 2024-11-06 03:46:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 591aad64-1532-3135-a464-ed3619a41832 | -2.89796 | -44.80709 | 2024-11-06 03:46:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1059d72-a2d8-3fc4-b6a0-28d900192e29 | -3.86369 | -41.03698 | 2024-11-06 03:46:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af7a3ed8-4ed0-3d11-9768-ade379af1e54 | -2.65493 | -48.57175 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ff049e2-205f-30bd-b0c4-a0d8c9a1a5f8 | -3.60007 | -42.86079 | 2024-11-06 03:46:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f2f4c389-db49-38ed-8457-a3889558465c | -3.71567 | -41.68982 | 2024-11-06 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 870b99e7-af30-3728-9390-68e8fe63f96e | -3.77004 | -40.99372 | 2024-11-06 03:46:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4bcbc5e-7ff0-3ff5-95ce-01a31e29bdf9 | -3.60457 | -42.86148 | 2024-11-06 03:46:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dabf40ab-e25c-3688-ad72-062d120a501f | -2.6625 | -48.56717 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a6b18f9-df9f-3ee8-b0a5-3508f8d108f0 | -2.66034 | -48.56545 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2fdefbae-a9be-39f1-9053-c617452fe8f1 | -3.72042 | -41.68674 | 2024-11-06 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f7e42ac-977c-3165-a94d-2a021f1bb673 | -3.53334 | -40.91296 | 2024-11-06 03:46:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2061060e-e910-34a5-9875-6f91efbdafaf | -2.89277 | -44.80624 | 2024-11-06 03:46:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd504f84-befa-36ae-876f-b7848d6c50ac | -3.87346 | -41.67351 | 2024-11-06 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 303fb246-4f9d-3db1-b829-e06c1b52f1b1 | -2.65273 | -48.57002 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 137ab208-fee4-33ea-81a7-7f0c7a5505a5 | -3.86138 | -41.02614 | 2024-11-06 03:46:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31786d44-4852-32c4-947e-68fc6ad62311 | -3.54128 | -40.71626 | 2024-11-06 03:46:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e75553c6-91de-3d78-8df2-a00d1ee2caf0 | -2.65371 | -48.56437 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb7d57d1-dfeb-35d2-a118-0bc8c8d0d72a | -3.71153 | -41.68916 | 2024-11-06 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5bcdd758-69ef-367e-9850-37192d92debc | -6.00991 | -38.664 | 2024-11-06 03:49:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1e4d16ca-66dd-3cc0-b8b0-3686ce8aaeb0 | -6.49399 | -47.48993 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 72bd18e2-0690-30fd-960a-f96440f81905 | -4.36083 | -45.76208 | 2024-11-06 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc8df211-4f68-3e32-946b-f7b1977d802a | -9.8959 | -42.08916 | 2024-11-06 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 57d88f1a-1d28-3b4b-b190-b8c6defa51ac | -6.48987 | -39.96889 | 2024-11-06 03:49:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 736c5fa6-59b5-320e-9095-cb39303d143c | -3.55101 | -47.38759 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f041ed-5875-3be4-a52f-6d6855fa3937 | -8.61402 | -36.39203 | 2024-11-06 03:49:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 61395183-90c8-3e6d-bf0d-a733a2b92e98 | -4.59335 | -44.04289 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a24814be-164e-3037-a68a-7ef58ac52832 | -6.49474 | -47.48582 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| daf7155c-6fa2-3fed-97c3-81042d836ce9 | -6.49979 | -47.49119 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5aa39014-085b-3943-9fd5-e21058248050 | -3.54237 | -47.40147 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44f19eb6-ba50-3a46-b705-773bd80288a6 | -4.62366 | -42.81096 | 2024-11-06 03:49:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f052dffd-01db-32b6-a8f2-8b22aa3b3cfd | -3.93398 | -45.00358 | 2024-11-06 03:49:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c079fca3-03c4-33ec-9cc9-ba4b436eeb15 | -6.62276 | -41.6675 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 03d14a3a-4c2f-3e7c-9f29-2d6246fe63ce | -6.49362 | -47.49743 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6a35d480-3aae-36b8-a603-9e1f78c95b35 | -8.76509 | -40.35318 | 2024-11-06 03:49:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 11910b8e-7ccc-39e2-be94-cb6a9d2c395a | -5.32553 | -43.07189 | 2024-11-06 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8602a9fa-4c1e-3307-a00d-023d77b91e69 | -4.65415 | -43.82059 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e35fc15-133a-3c5a-b50e-3eabd633c190 | -5.14451 | -47.69905 | 2024-11-06 03:49:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab28f750-6847-36e0-a191-3faf580eca15 | -3.52284 | -44.72425 | 2024-11-06 03:49:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84f9aca3-dd2d-34f8-b03f-69b8ecdc6be5 | -6.26181 | -46.90905 | 2024-11-06 03:49:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9329840a-02af-3437-9e44-201d08131cff | -6.12348 | -43.98243 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 237197a7-57a5-33ad-930e-f09bb5adb7ce | -3.243 | -50.02266 | 2024-11-06 03:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e654790-4f1b-363a-9690-9d5589d86371 | -7.26511 | -42.63051 | 2024-11-06 03:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce6cdd7b-b521-3f75-a2a1-39a3fb72b31f | -5.94086 | -43.77888 | 2024-11-06 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98b93f23-54f8-39e6-a5e8-69102a475d82 | -10.45102 | -36.8262 | 2024-11-06 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0a5248e-4007-3840-a1ad-62daeb57bfad | -6.64622 | -47.86745 | 2024-11-06 03:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dcd8096-8cb1-3847-b1b5-830250a40234 | -6.72328 | -46.35172 | 2024-11-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89ce6263-d2d7-3487-80cf-37533fd87b80 | -4.55297 | -48.01654 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c00599a0-432d-35b7-bf38-5b9991bbd9b2 | -4.56007 | -48.01257 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fd38f129-326b-3ad1-ae34-6c77d6e2fb52 | -3.75775 | -45.93866 | 2024-11-06 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a2783a1-3227-3346-87ee-80ad31f5ea4f | -3.54488 | -47.38682 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4e8ce266-a8d8-328a-a461-2ebd401c7915 | -4.02581 | -45.6662 | 2024-11-06 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1fc021-5f0a-3ad6-9013-4f226fd00fc5 | -4.63477 | -45.06683 | 2024-11-06 03:49:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce1d65fd-d4a1-3a52-982b-3a377b8f5eca | -6.50643 | -44.68745 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d454b280-dcba-3dbd-80ea-5b6543ea797b | -3.53628 | -47.40047 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c1ff9e8-e299-3b8f-9f4e-2a3efa329d6c | -8.49944 | -42.10344 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 97719c97-af25-370c-aeeb-2d560fbd86b9 | -6.49346 | -39.96948 | 2024-11-06 03:49:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 646923e1-da00-3ee5-96cf-7702a19f737d | -6.48922 | -47.4882 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c35024-cf55-36f0-92cb-8a4369781127 | -6.66372 | -47.28131 | 2024-11-06 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8f547ff-1c86-3791-98fd-8c7fa926a520 | -4.13736 | -43.58409 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b151d2d8-cc22-309f-a3f2-e3170e1b9a2d | -3.54567 | -47.38223 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 30ec6ad6-bf45-376b-a62b-1b095a4ef475 | -4.7052 | -44.55172 | 2024-11-06 03:49:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3024d473-921c-3d26-8a21-2542ff098741 | -4.12636 | -43.59257 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0fcd9796-b8e4-3454-a517-e9565c6e0696 | -8.50821 | -42.09958 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f5fbe20c-9535-35c4-aa36-3ad7bc79cb73 | -4.01774 | -43.62423 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ab14b9-793c-3201-abfe-8bbb02d88fc5 | -5.22575 | -44.91266 | 2024-11-06 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56103aba-4889-390a-8067-251500005b3d | -7.04213 | -39.25613 | 2024-11-06 03:49:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86453ccf-1253-3707-855b-a88b1c82d371 | -6.77994 | -37.53653 | 2024-11-06 03:49:00 | NOAA-21 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d165d7b-a8fc-3626-bb26-d5ea12741dc8 | -6.85007 | -38.90168 | 2024-11-06 03:49:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8e063cd-9618-3527-aa46-06e01cbfc328 | -5.13849 | -46.15786 | 2024-11-06 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad13405-0605-3c1a-a135-0169ccd6b699 | -5.55311 | -43.70097 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 865dca50-ca79-3abb-b733-b1aca04c5ef0 | -2.84967 | -49.48245 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f9a71694-6626-3a48-9b90-7ae7958304b3 | -5.15033 | -43.7727 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a0132aa-ddd5-3605-b990-b4e6473f2bf1 | -3.97377 | -48.15809 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a8f94e0-1b22-33e2-a9ae-fc1b98def313 | -6.48994 | -47.48412 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be75425e-0742-3c41-8abb-46672e209935 | -6.93813 | -47.78347 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2d9154a-5c91-3c08-9f57-57252bba698a | -6.49247 | -47.49822 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be6eb1de-6951-3989-904f-06c359b33e62 | -7.43513 | -42.88207 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a6798299-3197-3526-88c6-271809621933 | -6.72266 | -46.35517 | 2024-11-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8281fe1-dbce-3ada-9c51-6ee1eafb2347 | -4.66016 | -43.82386 | 2024-11-06 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7aa88d89-45b0-3579-970f-90219f2b7446 | -6.51825 | -41.42022 | 2024-11-06 03:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e27bc5be-6327-3a7e-8d80-9c4a4002a382 | -6.13228 | -43.9774 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f2198a38-574f-373d-9d6b-b7d04b119df1 | -5.48233 | -44.85979 | 2024-11-06 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e216ba04-f26a-3ec0-a3c8-205812fbb5ef | -6.66637 | -37.45827 | 2024-11-06 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fd3a2f3-0fa6-3eaa-93a9-ac6d9da5997e | -8.49098 | -42.17886 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b3e1c2a6-bd19-327b-8361-ae428dcf18c1 | -7.67254 | -42.64117 | 2024-11-06 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c2cddc8e-3f4d-3910-968c-bf03334cbc2b | -6.65811 | -47.86981 | 2024-11-06 03:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6377b5bc-6194-31d0-bc90-a1ab443fe7ca | -6.1035 | -43.95901 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 860b6adc-0a01-3bff-8be8-88a4009142a3 | -2.82647 | -49.78453 | 2024-11-06 03:49:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47879056-facf-3550-92f6-4854bec19847 | -6.5074 | -44.68182 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 47e078e3-3ab3-3459-bcde-f5562d5027e5 | -10.54838 | -45.13696 | 2024-11-06 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| adf7ee09-b4b0-3008-905f-e82f43a45668 | -6.61424 | -43.61198 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c038bc81-6e2f-3cda-be34-66696a393647 | -6.42704 | -43.77464 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e6aec40-ca16-33ee-8283-12b6f78a29e2 | -6.12265 | -43.98742 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 318de9b2-908b-33e9-b6fe-500eee87a292 | -6.1273 | -43.98826 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d0774ad6-81ea-39c2-bd1d-f695a86bd24a | -6.11198 | -43.9654 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8d5735d9-da7f-3542-a881-d214bb2b7c72 | -4.1029 | -44.27357 | 2024-11-06 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7fec117-329a-3fe7-abe7-c7ba96ead753 | -4.13442 | -43.58738 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 34ed3c1d-f65c-34b3-a919-4ee99e76eb43 | -4.5592 | -48.0176 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4afec732-d9b3-3287-8cab-b0be8d81b0e2 | -6.61465 | -43.69291 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README24.md)
