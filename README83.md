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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce5ca5a7-4f0e-3604-803e-e48d100c3f36 | -2.77693 | -48.56591 | 2024-10-25 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c36cadf-c953-30c1-a102-c357b5d4fce4 | -2.77651 | -48.5646 | 2024-10-25 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bd77607-00d3-3b76-8ae6-59af42096ce2 | -2.57506 | -48.14753 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05ca885d-0479-33e2-848f-ae2fbf4d1139 | -2.47616 | -48.49816 | 2024-10-25 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deb32577-7615-3ca4-9cfd-4b33bacd339c | -2.45207 | -48.50793 | 2024-10-25 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9846d86a-5ce1-3add-8cdd-9c0a051a23ae | -2.44934 | -48.61726 | 2024-10-25 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2a0601b-4dea-3564-adab-7eb6c7c9e5cc | -2.4365 | -48.46728 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c081a6d-9c96-3231-90af-8a2bf4045c60 | -2.43582 | -48.47163 | 2024-10-25 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec6b9f2f-5a30-3cf2-9fcb-291c0c39242b | -2.19069 | -48.74491 | 2024-10-25 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5478abc3-05fe-31de-a886-d9d0fdce24b3 | -3.92989 | -48.33799 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ab12405-47f6-355b-974b-995746b748ae | -3.92919 | -48.34267 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ffe9eb8-6ab4-3a4a-ab33-e1da2b785c3e | -3.92463 | -48.34191 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee8ef07a-d740-3be0-84b7-17db190bca5b | -3.91597 | -48.36885 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e1f81c3-6a54-3525-be1b-bc4f5a1ac069 | -3.91139 | -48.36822 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3081d4f-7ae5-3cdf-b65a-d801cae62a24 | -3.91072 | -48.37282 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 808c13b0-b066-3dfb-8dca-03880dd447ae | -3.90749 | -48.36299 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b290f48c-054f-3492-be9c-854c721b2124 | -3.90682 | -48.36758 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd90ae52-1d34-362e-8af3-1e49ab266069 | -3.83417 | -48.89088 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e887d37-dd8c-3445-b7b7-abc07e46bea9 | -3.82725 | -48.87683 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5e53c3a-939c-39d3-a847-7add3c7aa72d | -3.82661 | -48.88112 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f9165c0-c7c3-389f-a685-dd055baa0dd9 | -4.36248 | -48.60959 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c430b9a2-7d52-366f-9c74-87d0ce887e6d | -4.34299 | -48.61626 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58d05f46-33b3-3158-af04-8e7421b2c425 | -4.34231 | -48.6208 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8cb468e-56cc-3826-9784-930b509ead3c | -4.34161 | -48.62544 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a494d61-6230-397e-bc51-023357017819 | -4.33958 | -48.63908 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 639974e6-5538-356e-9061-61ad8c61b93c | -4.33641 | -48.62939 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35efc5e2-ccb3-36b0-a44b-0a654673e645 | -4.33574 | -48.63389 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0d26927a-5b89-3f67-b577-efc5e6e57ff6 | -4.33507 | -48.63837 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 87eea66e-5345-3bdd-8bb9-140ae00fb100 | -4.3344 | -48.64287 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e561145b-06e2-36bb-956f-1144cc468637 | -4.3319 | -48.62867 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a51531fb-8ad0-3c45-8504-c8d4cb76d372 | -4.33124 | -48.63313 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9bd1c255-e129-3c0f-bcf0-a5680d5f72d3 | -4.33057 | -48.63759 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e5a50198-a2ff-36e2-901e-1ca4bb488343 | -4.32989 | -48.64221 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| a7e382fe-f595-3ad3-9d82-c112a19a38ec | -4.32673 | -48.63242 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3570dda7-0aa5-35bd-8f5e-9a417c0a2b4e | -4.32607 | -48.63687 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 02d1b22e-d682-3c16-a491-f82198c11c07 | -4.29128 | -48.62244 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a15eb9da-efaa-3b72-a153-d12262d8647d | -4.29062 | -48.62696 | 2024-10-25 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5246d5ad-e149-3f81-a50c-ed71570882ed | -4.19366 | -47.77668 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bd1deb9-7aad-3d66-a4ec-532b627f19e4 | -4.19359 | -47.77909 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95d3def0-34b3-31b4-a2ac-07baaa287887 | -4.18892 | -47.77567 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3468a2f1-904d-3c1b-be24-736078fec3c3 | -4.18885 | -47.7781 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2418b10a-0b43-3342-8949-9ea7eef213f2 | -4.13974 | -48.74622 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f41eddf4-ad38-343b-aa21-5f4de44047b9 | -4.13823 | -48.74398 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e683ba2c-be9e-341b-b583-da92aa7d0ce1 | -4.13751 | -48.96674 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72e2337f-c3c2-3db1-b974-aa6d54c01609 | -4.13688 | -48.97101 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5207fdee-04ec-3c1a-be75-7b41d48b4446 | -4.09928 | -48.23989 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4419d758-ae4d-369e-a2a7-1f302fa5e9f5 | -4.09469 | -48.23906 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43949e24-34ff-3c91-a87c-fde792c3202d | -4.06637 | -48.96209 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6575705-6436-32c2-88a2-6d32f3fcdab1 | -4.05154 | -48.11438 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcfe10a2-14d3-3c34-9a73-882d8f6ad56c | -4.04614 | -48.11874 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e7e521a-6ee5-3374-8e35-60c064eef5b9 | -4.04295 | -48.10801 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 403c5658-b333-37a0-b32f-357a7ea10111 | -4.04101 | -47.95585 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420cf654-ecee-3b01-b724-04029d258767 | -4.03972 | -47.95382 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13f6d35d-3640-31f7-b14b-7e6196cec570 | -4.03631 | -47.95512 | 2024-10-25 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feec655d-f1bc-3f04-99f8-2cbfb68da7a0 | -6.48463 | -48.73895 | 2024-10-25 05:01:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 230ef5c0-198d-3826-a12f-393d46a20d94 | -5.72952 | -49.29737 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fcaf25f-1ae6-33a2-a637-4f307c5e1219 | -5.69366 | -49.29654 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e22e9fd-e177-3d7f-9bb4-0eb62919b2a8 | -5.38321 | -48.90377 | 2024-10-25 05:01:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 76a9b628-219e-3f84-b53c-9377d6886557 | -5.35428 | -48.16983 | 2024-10-25 05:01:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a4ecbf1-1283-39a9-8852-749b08d68814 | -3.25605 | -50.16744 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2bb4d3d-f78d-3258-8857-808041c0ddc1 | -5.20597 | -48.21939 | 2024-10-25 05:01:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d537ff63-38b7-3527-bdd8-21b320e28902 | -5.20445 | -48.21658 | 2024-10-25 05:01:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 641497a6-baae-3fa6-a25d-5045bc92dbe9 | -5.2037 | -48.22155 | 2024-10-25 05:01:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89989c28-8cd1-3b46-80ad-82f4145f7771 | -7.82231 | -49.82918 | 2024-10-25 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf5ff24-ee7b-3009-a88e-ed2097c90480 | -7.78976 | -49.52437 | 2024-10-25 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 147cfd4e-8123-3bf1-bfca-d9c1b06f5705 | -7.34016 | -49.13751 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4eb02a6f-34dd-365b-a1b2-e259c238a51b | -7.33496 | -49.14143 | 2024-10-25 05:01:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad2887dd-1d24-3a69-aec9-e2d002e2d0d0 | -7.11028 | -49.16914 | 2024-10-25 05:01:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 095bb513-f9ff-32ac-9a30-fc4af7233711 | -8.1324 | -49.79399 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a48699d2-bd39-3c89-86b7-0113c3447a1d | -8.12799 | -49.79335 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee9836f2-c9e4-301f-8fcf-4901ba9b99a5 | -8.06418 | -49.38091 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccd0c3ff-c3e7-3196-b76e-5b1eefee49b9 | -8.05962 | -49.38036 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbeb5a5c-ce5e-3559-aec0-9409281b7a6e | -8.0247 | -49.63306 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76bb2284-e989-3f1f-bad9-d9c33e3a7267 | -8.02408 | -49.63746 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 69313d39-aac2-3a3b-a5f8-e8f63f2f8009 | -8.01963 | -49.6368 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8be7e87e-9f6e-3671-9b31-49f81e66cce7 | -8.01518 | -49.63614 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90d2fe96-a16a-3486-a13e-83e46ca97eeb | -8.01174 | -49.637 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ff4f83-5923-30df-b9fc-3b6d60a775b0 | -8.01073 | -49.63551 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fe466a4-f434-3bfd-912c-2e2fbd07a72c | -8.57674 | -49.22625 | 2024-10-25 05:01:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25f255b2-307f-35a9-9e59-06671da117a4 | -8.57608 | -49.231 | 2024-10-25 05:01:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f19ee932-05b1-38cc-b335-f8be4300c9ff | -8.45769 | -49.43748 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50e43e7a-8235-3dd6-89d4-535e2585c026 | -8.41416 | -50.08985 | 2024-10-25 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f3b28d8-c571-3e37-a659-a9efff3539bb | -8.41357 | -50.09406 | 2024-10-25 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 403eaaf6-5a79-33c1-a50a-ba0bd4aff2ca | -8.35216 | -49.63174 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb16d0ef-7620-3406-9732-2af61d5ee5c7 | -8.35154 | -49.63619 | 2024-10-25 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34bf5484-9730-3184-88fb-d214cc1693a4 | -2.10834 | -49.27208 | 2024-10-25 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6301871d-7e45-3e59-b26e-7305bf9d31a1 | -2.10775 | -49.27587 | 2024-10-25 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04f9bfc9-cd30-3fbd-a648-57694355091c | -1.1771 | -49.08898 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aee5562-1795-3bb4-b950-fe956aa9f91c | -1.17653 | -49.09278 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2670782-5783-321e-b157-b9925c8a472e | -1.17549 | -49.08883 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55f33616-763c-33f9-b0a2-73d24479d5ec | -1.17489 | -49.09262 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b1a28e-463a-37f7-a288-e1909dcf1c4e | -1.17293 | -49.08834 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b2378c2-ad52-32bd-ab6f-bae1058c2a1f | -1.17132 | -49.08819 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8e3324-20d0-3805-8083-b1bfd78d8545 | -1.16715 | -49.08756 | 2024-10-25 05:01:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce14ffa-98f8-35c4-a716-c8c33d10d8cf | -3.50668 | -49.61091 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d04d7af-01a1-3c53-b002-e1d895be8558 | -3.4687 | -50.08514 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a966a516-8803-3fa9-838d-aef6979f79e1 | -3.46815 | -50.08872 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1d4ccb1-8c83-330d-a113-8e61802dcba1 | -3.46467 | -50.08447 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f60d97c1-1ec8-37df-83be-ca9c38923b7b | -3.46412 | -50.08804 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6831f2ee-e880-354e-9c6b-813e6916225d | -3.44955 | -49.82446 | 2024-10-25 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README84.md)
