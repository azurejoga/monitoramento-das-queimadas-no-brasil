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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844ff50d-00b7-3db0-957e-8923edc0fb3c | -6.39499 | -42.45705 | 2025-07-16 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4474e816-02ec-35e5-88f0-6d4b6a4f764f | -6.70973 | -44.33154 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 401fc3a0-9f3c-3494-a5c5-6daf271d2842 | -8.54366 | -36.50996 | 2025-07-16 03:23:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e19bdd47-ac2d-35ad-8c58-37d1254cbf7f | -9.43748 | -40.36977 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9df5488-2c13-3bd2-8fb7-05665ef08d95 | -8.51256 | -43.30654 | 2025-07-16 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c1835220-bd17-323f-931b-1fdd5c806cc5 | -7.19842 | -43.12303 | 2025-07-16 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 20a62128-69e4-3c22-ac9a-be9b8c38342a | -4.96276 | -43.22662 | 2025-07-16 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee875eb7-a766-3a8f-bc72-61b98f4f0add | -9.59046 | -40.36268 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58210bbf-4e6c-3845-89d0-47449f8f642d | -9.43162 | -40.3721 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 4d13db8b-a469-37e2-8865-765c30050312 | -6.70393 | -44.32369 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 56226abb-37bc-3c2f-88fc-126570f77122 | -6.73556 | -44.33702 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a1098970-5153-3f72-aaa3-18ca435fd887 | -9.36587 | -37.97308 | 2025-07-16 03:23:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7487f167-58c2-3dff-84da-6be55304018f | -9.43342 | -40.36227 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 4963526e-1989-3e55-9a29-76a83b167d72 | -8.24659 | -44.92569 | 2025-07-16 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da86744b-06ab-3e3d-be0e-494f656f7293 | -8.23955 | -44.92418 | 2025-07-16 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81f12107-f502-355e-ab1e-8b076a7e86df | -6.63784 | -44.58058 | 2025-07-16 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d3ebae2-d617-3c21-b392-ccea1f58dd7e | -7.19193 | -43.12187 | 2025-07-16 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89c85ca4-5ad1-3250-a0e4-b154ceeb9d68 | -7.05775 | -38.85584 | 2025-07-16 03:23:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68e452af-9fa6-37cd-b257-571257b3fc73 | -5.36165 | -36.89865 | 2025-07-16 03:23:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cca6a031-efd6-3ac2-b660-1351f6d651e1 | -9.29604 | -44.84689 | 2025-07-16 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 985b2126-8632-3bf4-9ee3-7a558d926adc | -6.72726 | -44.34256 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 779765f5-71e9-31eb-9342-9160e78f5535 | -9.31681 | -44.85093 | 2025-07-16 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f98c96a0-5f55-3c0c-8d47-d63402319c99 | -9.41704 | -40.36275 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 55d57023-267c-3250-bda1-f18937d548f2 | -9.42816 | -40.36134 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| a935dd66-b5fd-336b-955e-48bc67b4feca | -9.43688 | -40.37305 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5dc0c99-38d7-34d6-a102-8c05ad7e1d58 | -6.63594 | -44.57207 | 2025-07-16 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23160ecd-d229-3f14-ba20-44c77a79f687 | -12.99415 | -44.87346 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53630355-cfa0-3c45-a993-4f1eb0d27e3a | -13.02259 | -45.05503 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d975daa1-7e15-318e-b130-2a9c8fbddfa5 | -11.45538 | -45.10254 | 2025-07-16 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5adbbf94-2a7a-3522-ab1f-dbe5b259ca26 | -10.65057 | -44.48505 | 2025-07-16 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0c0b96f-f11c-3dc6-a223-2849eee636a4 | -13.65326 | -45.73282 | 2025-07-16 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54c92d4e-26d9-350d-b64f-59dd36a32729 | -13.12744 | -43.48623 | 2025-07-16 03:25:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ac21832-3c94-3f6f-8390-38011c6caa59 | -12.07287 | -43.47886 | 2025-07-16 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ddcd0091-eeb5-34c6-a3a0-3312d0db0557 | -12.99944 | -44.88073 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28f5444a-5832-3487-b05f-64110f289369 | -12.9979 | -44.88219 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4992e43c-e69c-363e-81b8-eb400249a0b9 | -12.99908 | -44.87668 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb613870-e7f0-38ab-863a-d2677e279a0f | -12.07193 | -43.48349 | 2025-07-16 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 97eb25fe-0f5f-3ec0-9b76-80784ab0c8bd | -12.41737 | -43.7529 | 2025-07-16 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 722dcd60-f253-3bf0-bb5a-a3ed5d988c8a | -11.46101 | -45.10275 | 2025-07-16 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52026c42-5e2f-3630-b979-e0349240748b | -12.07381 | -43.47416 | 2025-07-16 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4da15995-59f5-342a-9ac7-3e3051a55061 | -10.6463 | -44.48652 | 2025-07-16 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51916386-382a-345a-a680-98e86f3ccc29 | -11.78269 | -45.21554 | 2025-07-16 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b4e3b39-8bba-3e9d-9c82-6a2b213d5b39 | -12.58084 | -44.75432 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca22540f-e8bd-3b6a-af32-87690c269699 | -13.01356 | -45.06514 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 4a4e537e-b78e-3194-b89f-f7fb5f653af3 | -12.99298 | -44.87904 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5e381d5-13d8-3029-84e3-081fcf83982b | -13.01232 | -45.07098 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| db8fe986-674b-3d2c-92ad-386aee0dda22 | -12.42353 | -43.7542 | 2025-07-16 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad54913e-43a3-3212-90ff-603b1fca82d0 | -13.12051 | -43.48952 | 2025-07-16 03:25:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba028591-3693-3a4d-b1d6-fb7450e245c9 | -13.02014 | -45.06656 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5a40ec0c-80e3-3450-b95c-194c6f25dab1 | -12.41638 | -43.75773 | 2025-07-16 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7f2f166-ed67-3228-91b8-ad6a99e7ddf9 | -12.42254 | -43.75903 | 2025-07-16 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26a12277-eb68-3d2b-ab6f-411f13923d32 | -10.65294 | -44.4878 | 2025-07-16 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba02f095-bac8-3ca8-bbe7-689708dbfebd | -11.46214 | -45.10405 | 2025-07-16 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9eb90443-c547-3f1c-b7db-2b7ed093bd2f | -10.64392 | -44.48382 | 2025-07-16 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 630138b2-9a89-32d2-8e1d-4d56a358fb61 | -13.02138 | -45.06075 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 68bee560-de06-3f33-a8a0-d8dbeb12c22a | -11.45426 | -45.10123 | 2025-07-16 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ac851fe-c3a7-3bc8-9a8a-73469580e2fb | -13.0148 | -45.0593 | 2025-07-16 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3083afa3-3b77-311f-a111-7f8723d7fd69 | -20.0277 | -47.39211 | 2025-07-16 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c349b97-bb6c-3808-ae41-3fa638831ce4 | -20.03064 | -47.39621 | 2025-07-16 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37049400-1c18-3481-9fcb-64bd50f41726 | -20.09077 | -47.64285 | 2025-07-16 03:28:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 278cbc81-36b6-37cf-bf4d-eb8081c07829 | -20.03263 | -47.38803 | 2025-07-16 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fcba61fa-4ec8-317a-a2d8-fe6b05387b93 | -20.08393 | -47.64189 | 2025-07-16 03:28:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 62d96275-0899-3746-9b31-5fe5374179bc | -21.34356 | -48.63094 | 2025-07-16 03:28:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 34971306-d052-37f3-8d7e-5ec93a93cc70 | -21.34519 | -48.62437 | 2025-07-16 03:28:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4cd7cc6c-5616-3b6b-86c7-bf1825ab6666 | -20.07817 | -47.64753 | 2025-07-16 03:28:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 21b1e0f5-8648-3cb2-b623-77f07b71cb28 | -21.15766 | -43.76264 | 2025-07-16 03:28:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 813c91f6-daa7-391c-bd0c-2bfce0aa8a1c | -20.3597 | -46.59389 | 2025-07-16 03:28:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fccbade-0c97-3d0d-9c32-e704d2237f25 | -20.35827 | -46.5999 | 2025-07-16 03:28:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 375b9df5-45d1-30c6-b2ff-5a3d3b204079 | -20.07961 | -47.64165 | 2025-07-16 03:28:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f5f98e7b-8408-3722-bae9-71ae7beb7806 | -20.02959 | -47.38412 | 2025-07-16 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0762d09a-adf8-318c-814b-c1a4b87c3882 | -21.1637 | -43.76014 | 2025-07-16 03:28:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3d229cdd-3f7f-3cc0-a17f-13ba3298bc3a | -22.83193 | -42.06422 | 2025-07-16 03:28:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ed2ad4a7-1a5f-3bd9-a1b1-ad00d3043a0c | -20.38697 | -44.34815 | 2025-07-16 03:28:00 | NOAA-21 | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ba76de82-470d-3527-9bb2-b3b95f55bbd6 | -20.02435 | -47.39335 | 2025-07-16 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 986331c5-9c41-3e31-b30a-cb33d87377b4 | -20.08254 | -47.64773 | 2025-07-16 03:28:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 21ad6952-b28f-3bf8-b2c8-6c66c05c80a4 | -21.34298 | -48.63079 | 2025-07-16 03:28:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7a5f37f9-81e8-3b48-9a06-9be3b65b308e | -20.35587 | -46.59801 | 2025-07-16 03:28:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 912f6d44-4ab6-3bb2-b941-9eeb6c1f2e4d | -20.34761 | -46.54776 | 2025-07-16 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb1db1dd-bb35-33e7-9804-0978ec26152f | -21.34464 | -48.62426 | 2025-07-16 03:28:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 332aaf20-5bd0-3275-b66d-c8425cce7e4d | -9.4188 | -40.3944 | 2025-07-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.2 |
| a53c8fac-7878-371f-946c-a416356da591 | -13.0339 | -45.0561 | 2025-07-16 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 00eba3db-df11-3805-b988-9a0a31390e28 | -9.4196 | -40.3447 | 2025-07-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 0cfc82b7-f1c8-393f-b274-219141536b2f | -22.574 | -54.9542 | 2025-07-16 03:30:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| 148fd869-e836-3b43-91d5-f96b9b0ca6bd | -9.4387 | -40.3419 | 2025-07-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 323c67a8-9dbc-338f-a63b-172ccb817bf0 | -20.0805 | -47.6319 | 2025-07-16 03:30:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 389f86a0-4fcc-3af2-b5ce-d871107b7774 | -9.4383 | -40.3668 | 2025-07-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 261.8 |
| dc16a6dc-13f0-3a87-8e35-e0eb0de2f926 | -22.5745 | -54.9324 | 2025-07-16 03:30:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 03055f9f-05e1-3c70-806c-408e784c2f70 | -9.4192 | -40.3695 | 2025-07-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 287.0 |
| 0e8a4bca-f948-387f-8ed9-cd1c454e546b | -13.0146 | -45.0593 | 2025-07-16 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e9f94273-8632-37f1-a495-552c6298d054 | -22.5745 | -54.9324 | 2025-07-16 03:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| 1a300aa0-2e88-3025-ae51-63406f228271 | -13.0146 | -45.0593 | 2025-07-16 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ef857539-a68a-3fae-a8c3-54c659329e51 | -13.0339 | -45.0561 | 2025-07-16 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 31b2c0b1-eeef-3243-9244-b8eb7a7ea473 | -22.5533 | -54.958 | 2025-07-16 03:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| fffdf192-f379-382e-bd62-dc41f6970d9d | -20.0805 | -47.6319 | 2025-07-16 03:40:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e2d672d0-5bf5-3ba1-9db5-871a27873c71 | -22.5538 | -54.9361 | 2025-07-16 03:40:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 2c6fe5af-714d-370a-addf-62a7ecf27ad3 | -7.04801 | -43.47763 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 787e4d92-bd01-3574-a0f7-b311fa196d69 | -7.21924 | -45.33103 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1881a9a9-2eca-3b87-be2f-986ece7956f8 | -7.21419 | -45.33005 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b7d033b-1161-35fd-80a4-4ae20dc5bd5f | -4.78323 | -45.3426 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9473b69e-886e-3c74-9042-8640f985df87 | -7.36232 | -39.17482 | 2025-07-16 03:49:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README8.md)
