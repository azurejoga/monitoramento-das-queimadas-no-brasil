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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aa68f00-be9d-3b96-b89f-52ade6b77e17 | -11.9039 | -46.76093 | 2025-07-15 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa57a50b-8cd2-3b58-b688-f9dbd22a0542 | -10.89421 | -49.21322 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3c3d6481-f261-399c-a0dc-c79c8785927a | -7.30149 | -45.35761 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f37303aa-9979-36fc-9665-562210c318d7 | -7.09506 | -41.47824 | 2025-07-15 04:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a21f72f-9cfc-35aa-a605-dbaa9757fd3b | -7.08802 | -43.69167 | 2025-07-15 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4da09e1-f2ca-3c29-bb78-d75c4852c669 | -12.07482 | -43.47551 | 2025-07-15 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e096c7-9be9-38bc-84ba-d8de7defbdb1 | -7.2763 | -45.30338 | 2025-07-15 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03499eab-56cf-321c-a202-14280e07c00e | -7.15368 | -43.15306 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 188fa42d-da5a-366f-a4a2-7422723979bd | -11.45488 | -45.10323 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 72fae761-dc8a-321a-a6d7-a12d5eb4603f | -9.62151 | -49.10384 | 2025-07-15 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49cab47-4a1e-3907-ac27-8c3e6311d5c2 | -8.68732 | -51.45991 | 2025-07-15 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3acd88e3-cc56-3378-9652-ffca858479c7 | -7.19884 | -43.00111 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f44fee6-8f34-331b-809a-7c6decb5ec4e | -11.45336 | -45.09087 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4daf9b2f-d47b-3671-a7ab-f7edaced894d | -7.63841 | -44.41922 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d01672de-3277-3047-a60d-1cfabc281e14 | -7.2818 | -44.03798 | 2025-07-15 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 470c9b26-d87e-3408-a237-3a0635931691 | -10.28451 | -47.61797 | 2025-07-15 04:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afec451e-9007-3342-bf00-84261535443f | -10.87911 | -54.051 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab0c047-fb1d-37a9-ace0-f842414c0c75 | -11.4391 | -45.13294 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 386fa5d3-865f-3952-beea-a4242efa50bc | -6.54977 | -44.68863 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 975aa0e1-6588-3a74-ba9a-5c8487202735 | -10.88666 | -54.05168 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 692fc1df-c266-3a0c-b74b-0e08f362f612 | -10.56989 | -49.13486 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5180b37b-4aed-32fa-b532-ee9df0b22885 | -13.10409 | -47.27929 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952340d8-e30f-3c3f-9289-9f4adfca0ecd | -6.70596 | -47.79918 | 2025-07-15 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2d6e4f-90ba-3d13-9b4d-fe2ce073385c | -9.86273 | -47.87309 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 698d5446-4d90-3719-ab13-40838d68c69a | -7.16117 | -42.99873 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68fe70e8-0f66-353f-bf1a-c3757b0ef5cf | -8.23638 | -44.92603 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88af505a-1766-343d-99a1-c4852cec1da9 | -9.80039 | -47.73937 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3761c0b8-5a2a-3bb3-b822-fb672d4a29cc | -11.44855 | -45.0981 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 563b4bd5-a928-37fc-a07a-29a38d02d5cc | -6.70963 | -47.80408 | 2025-07-15 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3bd92e2-7103-34bc-a962-2b0471a1565b | -11.44043 | -45.12505 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a95da9b5-1988-3d16-abe0-64d50d5a6e42 | -8.28703 | -44.97696 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a2487bd-5968-3d21-a769-16014ee7de99 | -13.65493 | -45.73442 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 446123bf-7156-3580-b370-659e3acc62a1 | -7.93002 | -42.88998 | 2025-07-15 04:10:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7890cd2f-6a1c-39ea-accd-bf598ab015e0 | -7.09035 | -44.39156 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28bf9666-b373-33fe-bcd6-6deafb98671f | -7.09583 | -44.38023 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39b1b466-08d0-3318-8c15-ef35476e31a0 | -10.86554 | -54.06193 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dad6d30f-9267-302b-b038-5cc16ad928ca | -6.73117 | -44.33485 | 2025-07-15 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35771a32-3eae-30b0-b1fd-3cad7188e06b | -11.43627 | -45.1284 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1987e3c-de6d-3101-9ecb-cd206795ba6d | -12.41073 | -45.37385 | 2025-07-15 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd910dc0-6a1f-320d-b603-50c5bcc8ccaa | -9.43897 | -40.32119 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 47a78c06-0a39-3043-9319-ec383bc15000 | -8.64594 | -47.75291 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ffa7f45-4950-315e-b957-5e938bb243e3 | -10.56459 | -49.13857 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b0f86010-cccc-3c37-98a8-bcc9614184d5 | -10.64999 | -44.48196 | 2025-07-15 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0468be17-912c-3551-b87b-b0e4d2646fb3 | -10.64314 | -46.61892 | 2025-07-15 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83b84295-3f7c-325e-bd39-5a861bb7ec38 | -12.47137 | -44.49945 | 2025-07-15 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70cfd604-ac47-3817-b6d5-a4414386e58a | -8.38479 | -51.07482 | 2025-07-15 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 39dda3b6-b693-3676-a4a0-72b03369f2fb | -7.09519 | -44.3842 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0440a183-ba88-31e1-9880-18aa347f8231 | -8.65016 | -47.75363 | 2025-07-15 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0925bc44-1e6e-3e9f-a705-838952f0483e | -10.56379 | -49.14305 | 2025-07-15 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b1708578-6e92-35f5-a61e-1139f4534309 | -12.29003 | -48.79341 | 2025-07-15 04:10:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 327f2007-dee0-3913-ab60-bfae01bd6c68 | -9.80798 | -47.74467 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da974049-3a0e-3910-92fe-e54ba357d30c | -9.43954 | -40.31744 | 2025-07-15 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 64487f55-3ad4-3e73-abee-22b18867bde6 | -11.73151 | -47.0483 | 2025-07-15 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c63a87a4-1e71-3c2d-bfb3-374fda49d5ae | -9.81147 | -47.74912 | 2025-07-15 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61b3733e-74ca-3134-bca7-3367b5106fe1 | -10.87109 | -54.05912 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8451370e-074b-3fe6-b2f6-b9d029257b05 | -11.45903 | -45.09991 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e299b323-35df-37ea-9f80-15b650012a3a | -8.6888 | -51.46025 | 2025-07-15 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b7d17df-b8bb-32a9-ab3e-1b4561a9b131 | -11.44921 | -45.09418 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| aff33297-0922-376b-b57e-661308e37923 | -9.98232 | -48.08065 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a426b8b-e2cb-3d4a-9db1-a6dd4409da39 | -10.6483 | -46.63448 | 2025-07-15 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78672ca6-1dab-3557-bbb1-98ec542a386b | -10.37417 | -47.15012 | 2025-07-15 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8737936d-d45c-30b6-b6cd-ebb0f68aaeec | -11.44676 | -45.1302 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 44c8c086-d9f9-3370-af31-035d95adad36 | -6.29305 | -44.23096 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6934832d-300d-31ab-989f-62c32c9f27b1 | -11.73536 | -47.04898 | 2025-07-15 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6da562bf-e7e4-3c44-8aca-662ae7e7ae3e | -12.07425 | -43.47906 | 2025-07-15 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91aa9e0f-339e-3d4e-9077-7f78542962c5 | -10.87015 | -54.06377 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64cee1a7-88b2-3937-b47c-73ec6613ef34 | -7.27832 | -44.03743 | 2025-07-15 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cf8b876-a4ad-36e2-a2d6-a807dfa1ecda | -10.87166 | -54.06322 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 801dcc64-b8fd-33fe-b864-20422d270d0e | -11.90931 | -46.75228 | 2025-07-15 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e39f57d1-15f6-391b-a8f6-ab817858f061 | -10.49371 | -53.57409 | 2025-07-15 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f30605ec-ecd3-38e6-9214-6570bec3111d | -12.682 | -47.87308 | 2025-07-15 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc05a664-3850-3557-9b63-53330f707c07 | -11.4426 | -45.13354 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6b8d6a41-c40e-3f25-b881-c3153e896e73 | -7.09257 | -49.17358 | 2025-07-15 04:10:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14b0366a-6dd5-3db4-a413-1b522933a85e | -6.75181 | -47.3744 | 2025-07-15 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 636fea2d-24c0-390d-a630-bad57b975434 | -7.20355 | -43.10172 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5637538-0a13-3003-8495-b19eaa9d0371 | -6.1551 | -45.85624 | 2025-07-15 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6d4fbb-b967-35b9-82a1-05d8b4a84132 | -7.28117 | -44.04184 | 2025-07-15 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23f28f10-c09a-3433-a0f8-1e951c3d7131 | -7.64151 | -44.41855 | 2025-07-15 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46c7467f-1abe-3e24-8689-21f5dbf93779 | -7.10211 | -49.17525 | 2025-07-15 04:10:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40fd4e11-0d47-3d9c-9f7a-c7977e65fd2f | -12.07759 | -43.47959 | 2025-07-15 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2ad621a-69d5-3ebc-b66c-b5b74bb4278a | -6.42757 | -45.33274 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c446a703-34f1-3dcb-a5b8-52d7d2ad06a0 | -9.28779 | -44.84137 | 2025-07-15 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52847a0d-fa1c-3666-ad4a-1749947d581b | -13.65628 | -45.72639 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd2c02f2-0fee-322b-badc-e08916b30fee | -7.09807 | -44.38885 | 2025-07-15 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91ce07d4-dd4f-3959-947a-0051d7530bbb | -13.1787 | -47.27103 | 2025-07-15 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33f28c1a-c2b4-3b3e-9977-970de40fba1c | -8.38419 | -51.07812 | 2025-07-15 04:10:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 860695db-7912-35ec-a6e4-6f74baa37302 | -11.45554 | -45.0993 | 2025-07-15 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| a965f9c2-e45e-322c-8c6a-94d4943dc912 | -7.06196 | -44.03489 | 2025-07-15 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e24321c1-888a-3743-8375-ca29dabe28cc | -9.72633 | -48.33012 | 2025-07-15 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d4e71b6-2625-3d24-b7db-c52259e44b09 | -8.22339 | -44.91549 | 2025-07-15 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c99a8ad-8f8c-364f-bcc3-8836d38a04a6 | -7.20017 | -43.10117 | 2025-07-15 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 103ee8ed-513a-3b3e-86c5-5faa09b8247e | -6.36817 | -44.74821 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1e7289e-c83f-3d75-9959-403c6fd963e5 | -7.94641 | -43.87368 | 2025-07-15 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a28074c-c6b1-3b67-afba-23cf30ac609f | -6.37545 | -44.74939 | 2025-07-15 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92404171-7706-3da6-ac70-4e7af3ac5dc1 | -7.54258 | -43.92208 | 2025-07-15 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58fa8bef-82bb-343b-bc9a-e7b63410e00a | -7.5035 | -37.36917 | 2025-07-15 04:10:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| efae27c2-e13e-3e0f-ad9e-fcb39adbade4 | -10.88053 | -54.05043 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffde26dd-10ed-3c82-bd67-faecab249bbb | -10.87627 | -54.06507 | 2025-07-15 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e309360-450d-397f-af75-9ca2f6fb969c | -13.65912 | -45.73101 | 2025-07-15 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 478f07c2-84f6-32ab-b593-b0621dc12121 | -9.94951 | -48.16725 | 2025-07-15 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
