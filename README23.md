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
| 3d7fc79d-5df1-31f8-b33d-dc656464e156 | -12.36929 | -50.16133 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5634471a-e583-3ced-91e8-3fc30ed1114f | -9.23868 | -45.57148 | 2025-10-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 91a528df-845c-3c7a-bfd5-54605c6f271a | -12.06842 | -45.71745 | 2025-10-29 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce059e8f-17da-34be-a591-92c00b8930db | -9.49433 | -46.99536 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e72025c9-fca3-33bf-a163-f3ba1da6e596 | -16.1528 | -45.10055 | 2025-10-29 03:55:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66ca62e0-78aa-3acf-a150-7654150dfc58 | -9.90132 | -44.90247 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35d54c24-33f5-373f-bd4a-6165ba9c876e | -12.09458 | -47.25283 | 2025-10-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3445e29-1d1c-30ab-a027-042a6b5455e1 | -9.49926 | -46.98328 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50854bcd-2f30-3ca7-bd79-bb1f571e5ae8 | -14.66952 | -42.82504 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3bb08e44-1e7e-37af-8142-adb24cf176b6 | -9.8999 | -44.91051 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 30cbdc9c-9aa5-3f8c-8022-32c54aa64dc9 | -13.6378 | -46.49282 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e37bd48-a0a9-3ab9-b258-db3177e1c118 | -16.59271 | -43.51136 | 2025-10-29 03:55:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43948483-ccb4-311d-8499-a73bd8d08e5f | -13.65944 | -48.44512 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aeb20ce7-b31f-30b1-a2e3-e762c9daf2c2 | -13.23141 | -47.72787 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 405ba48c-a02f-3c85-bcb4-16f8b8192e8a | -12.32347 | -46.91765 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 701c0b8e-96ee-3d50-9858-b18311515d0e | -14.49282 | -47.88292 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41bb6b3a-10e6-3588-8220-91d8adbd47bd | -10.21426 | -45.95191 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b2799f5-a4a6-315c-abfa-a2d0883fa93b | -13.67308 | -47.18978 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ccdd84b-8f35-3fe6-8347-eb0beac92903 | -10.99203 | -47.72576 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab54085-8383-341d-9edb-f204f9992f79 | -15.33888 | -42.01085 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 791ca8f4-fa13-3b73-9565-08090f055b9b | -9.9242 | -47.66663 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6bd86ae-ecad-31e0-976a-5e26e5e3d452 | -9.11633 | -47.64856 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 950f4c68-2254-3390-83e1-b7faa80f2fcb | -12.41234 | -44.70665 | 2025-10-29 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d24dad2-e1d5-3c8e-b252-a4766e7e717c | -11.25885 | -47.81834 | 2025-10-29 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ae2034b-e2c9-347e-8b4e-ed000601018a | -11.3758 | -51.37333 | 2025-10-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e81aea-6750-341f-a8b2-6d80eb5328b5 | -9.48704 | -47.34147 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 52b44087-3013-3ffd-8544-3f1b9015e81d | -20.92267 | -45.58669 | 2025-10-29 03:57:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd0e6fd7-02f1-3b64-9b6f-98fc96fa5bb5 | -19.56566 | -43.76318 | 2025-10-29 03:57:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20aeaabc-6c04-3469-813c-ee867052ff9c | -20.92636 | -45.58749 | 2025-10-29 03:57:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dc06fb2-878e-3b34-b0c3-06abfca32170 | -19.39716 | -45.86895 | 2025-10-29 03:57:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ca0e57-4de3-3706-a856-8346fea41e09 | -18.83191 | -41.95509 | 2025-10-29 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 9402d592-b734-32a7-a13e-be23ff3d5d9e | -18.92669 | -45.03592 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 17569c13-a97b-30d8-bda7-66faae0d5544 | -19.28415 | -43.72529 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f79dd6-7e80-36f7-95e1-d1f0cfa2d902 | -18.92216 | -45.03982 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cb03a643-387b-37bc-9ca8-c796e4be9b17 | -20.30973 | -45.2861 | 2025-10-29 03:57:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c3f3107b-c586-353a-b686-3bc5147b2a07 | -18.50912 | -45.07858 | 2025-10-29 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ef67e4a-78b4-371f-b62f-19d8157aff7e | -20.34007 | -42.90283 | 2025-10-29 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 164d7427-2882-3f03-a51c-7ab0e2df7ee2 | -19.05901 | -44.69452 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13836a55-49f4-3d8b-a9dd-e8d7d4913bee | -18.76476 | -45.28519 | 2025-10-29 03:57:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 486d8676-37fd-33d3-8267-fd34b2464cc9 | -19.67985 | -44.19514 | 2025-10-29 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 605160c0-a41a-3eed-bed0-047e88d9c9c3 | -17.04074 | -47.05307 | 2025-10-29 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7d872e2-c571-3e07-9fb5-8588ddfa9aa1 | -18.93155 | -45.05151 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45259e05-32e5-3d66-b425-18f7ea92556a | -19.45161 | -49.33094 | 2025-10-29 03:57:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e21f634-75b0-392a-bcb7-258ddf06c817 | -19.43032 | -48.06675 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a5426f86-8aa4-3548-8ebc-480366330e60 | -19.79807 | -44.51907 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9f81365-b4d9-3cfe-89e8-f36a82fdee05 | -19.42026 | -48.06882 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f142293d-bae0-397a-a05f-9589b4dd698e | -18.58422 | -44.02987 | 2025-10-29 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ded73dbc-432f-3376-b51b-552798a5fb6a | -17.25768 | -45.29392 | 2025-10-29 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41c87687-b2e2-3876-a920-0e2d022db757 | -19.06491 | -41.13089 | 2025-10-29 03:57:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9ad457b5-3857-38f7-b790-bea895d75fa2 | -18.92132 | -45.04452 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7571f324-a681-3e42-aed0-004fdbab89b4 | -19.24191 | -43.99237 | 2025-10-29 03:57:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7af79f4-db98-30d9-836f-1843fa214b20 | -17.69045 | -43.9579 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d43cc5-e81a-3ab7-9cd1-bc8bdfd1cf41 | -19.90024 | -44.62209 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 45df301b-d6c2-3bd5-8abe-95fbdf9cdcc8 | -18.77808 | -44.34124 | 2025-10-29 03:57:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8e29dc9-00cb-3625-85f7-c12fedfa796c | -19.42283 | -48.07889 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13710790-52f9-3178-b30e-c4759645ff9a | -19.42415 | -48.07509 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 27646c0c-0666-3723-9d45-d3fb2c244361 | -19.33086 | -43.05126 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5cdb29b-bbc9-3e3f-aa36-391bfd27a1c4 | -18.54543 | -43.93843 | 2025-10-29 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 413bf834-0fd3-32e7-bfc1-d92ec5a48c33 | -20.10096 | -44.30609 | 2025-10-29 03:57:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 13b3e94f-952b-3b7c-b6e0-bdd5c15bd0a1 | -19.45974 | -43.58529 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3f8f075-e650-36a4-bc17-f29a1d8f6f01 | -19.34512 | -43.04953 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 82dd3cc6-8e9a-3f49-8838-347117211df0 | -18.50134 | -43.98311 | 2025-10-29 03:57:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbda6dba-90a0-3266-a70e-cecea93c5cbc | -18.20666 | -44.3392 | 2025-10-29 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09b6e756-9a06-3a28-a68b-49769264f85f | -19.75756 | -43.84457 | 2025-10-29 03:57:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 928132d4-4b7f-36fd-8020-78eb35bce11d | -19.42373 | -48.07436 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2772f300-3501-3f29-8b0a-c7154f1ac9bd | -19.37825 | -43.64589 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a021bfe-0944-38e3-9371-82997b9bed86 | -21.26601 | -43.02828 | 2025-10-29 03:57:00 | NOAA-21 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c104d94-f44e-3dc7-8969-8325b19fb4a5 | -20.85634 | -42.8674 | 2025-10-29 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c48446c0-970f-3144-9bb5-f2ee05ffd0e6 | -17.4826 | -44.06768 | 2025-10-29 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8712b2ac-d253-36c9-9a48-00e6e9d8fa32 | -20.96472 | -43.94306 | 2025-10-29 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71505ed4-ae08-3457-a01d-1c0d2abf695c | -19.42465 | -48.06976 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 77d0f49b-db47-31e7-9ca9-00448ed7e90b | -19.33623 | -43.03995 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 931c7cbb-f3f9-35e7-a1b2-e6799bc51846 | -20.58567 | -43.5649 | 2025-10-29 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19ddf764-da48-38a0-8859-6229cabf1322 | -18.92753 | -45.03127 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a7dabbd4-2dc2-3ddb-a4f7-f26c14310de7 | -18.923 | -45.03517 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f0f59efa-d40c-33a9-bb6a-cb2e2b7c0404 | -21.00099 | -42.79698 | 2025-10-29 03:57:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68a81696-e1b7-348f-ac21-c98380218163 | -18.56892 | -42.93817 | 2025-10-29 03:57:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46f89c93-8d6b-3eeb-a604-78ec01da89c4 | -19.45492 | -43.59283 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 300dcf76-1969-334a-9053-c99d19470604 | -17.63455 | -43.75615 | 2025-10-29 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7ed22fd-bfcc-32d6-957a-d843e68ac2dc | -17.47901 | -44.06704 | 2025-10-29 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1adeff1-de29-34c4-91b0-60edcf1751d4 | -19.45905 | -43.58937 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5a1d573-d961-3785-8d13-a48246eb0570 | -18.92586 | -45.04059 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 6f32ef00-a375-323f-93d8-30fef12a0066 | -19.33491 | -43.04789 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e934132-95e4-3fb2-80a7-9fa2e51b0ae9 | -19.37895 | -43.64182 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d4b93f2-828d-3d61-bd99-9d8cf94f194e | -20.34691 | -42.18816 | 2025-10-29 03:57:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b348bf3f-c544-3512-be02-6000ef89b5ba | -21.13133 | -42.34774 | 2025-10-29 03:57:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9f8fe7bf-019b-3061-9acf-2c0d0ce2e86e | -17.54157 | -44.61476 | 2025-10-29 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c24b6404-b3d1-33e7-8f26-76a3457325ec | -19.3315 | -43.04736 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea02defb-28c0-35e9-a03b-02e7666e2766 | -19.72081 | -43.9344 | 2025-10-29 03:57:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36bc43be-5120-395a-bf9f-fd25edfdf59f | -17.25859 | -45.28888 | 2025-10-29 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21736c3a-aab3-3a0d-adf0-a715799acf64 | -19.34043 | -43.05679 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0eb220b2-aa16-3618-a7df-53c1953c738f | -19.67914 | -44.19932 | 2025-10-29 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9469ef98-f226-36c8-8a81-e1079c3a2940 | -17.10557 | -47.16853 | 2025-10-29 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb6c3c63-d12b-3f6a-9ff5-1a5f1906d71b | -18.9287 | -45.04607 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 92329d6e-b494-3e4b-8e87-94699f68afe4 | -17.26243 | -45.28962 | 2025-10-29 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f033e25-f640-34e2-9041-422ec73b65a0 | -17.69534 | -43.97205 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea84d330-6ec3-3315-90f8-566a8bb8c44a | -19.37133 | -43.64462 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc2a712b-81aa-3332-9498-1c28d050fad1 | -19.42904 | -48.07069 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 968cb19f-1f07-30f7-8b3e-a53f7188f927 | -19.41935 | -48.07337 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9fadd9c9-3e68-3d74-a930-38d08644a68f | -19.42997 | -48.06601 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |


[Clique aqui para ver as próximas entradas](README24.md)
