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

## Dados Diários - Página 262

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf5fdeb5-3031-30f1-a795-caea2c59cab9 | -15.25892 | -42.37992 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 30c52555-82ca-3c2f-ad69-6b233caf76ca | -11.99319 | -43.45622 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 119d9410-5c15-399c-808d-56254c5b0d8c | -11.14861 | -41.83901 | 2026-10-09 15:58:00 | NPP-375 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 64e5b4d7-150c-3f0b-bd77-7be100585922 | -11.72054 | -43.63597 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 34660c36-d70d-33fe-80b9-436ad83087eb | -11.20516 | -40.56137 | 2026-10-09 15:58:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4d78f92e-3f29-3413-893a-d4e86224d5e2 | -16.08234 | -45.97356 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2f9f1087-f79f-3e5c-8cd6-8d07be23962d | -11.98794 | -43.4609 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3876c018-cb7e-316d-b74f-88983f0246b3 | -11.77839 | -43.52799 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78245873-e091-3e1f-b8c4-2657ab50e91b | -14.64804 | -43.53107 | 2026-10-09 15:58:00 | NPP-375 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 14c70f1e-6cfc-39e2-a962-e8de06bba1ac | -12.90842 | -45.11528 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 412eb3f5-48e9-380f-83bd-db56fd8e76fa | -18.08558 | -42.26954 | 2026-10-09 15:58:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 404d7347-a4fb-3ba9-9923-6be5ec7041f1 | -14.74006 | -41.00051 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8e981b2c-4c89-3764-afd7-92c985d5c289 | -11.78366 | -43.53195 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17467006-1993-3706-968c-5cf770bdd752 | -12.22581 | -44.83683 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 79b5a919-a2fc-3df5-882b-974ba613df5e | -18.31896 | -42.38181 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| a7a460af-4bc3-37f7-974e-951c5e6a5b67 | -12.90261 | -45.12132 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 2112e0eb-3ae6-34be-8518-46f75bc4accb | -12.22226 | -44.64434 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81f476d1-1a36-316d-91b7-42ddbb91749e | -14.63566 | -43.83655 | 2026-10-09 15:58:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 660954f8-f94f-3bd4-973b-569fd76b9110 | -11.59169 | -43.64158 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 22728add-e452-3bad-aa04-bc7e8877cb6c | -12.76822 | -47.08543 | 2026-10-09 15:58:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f55c0372-9da6-3b4f-a821-6e508d4ca5fb | -11.46448 | -43.38712 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 7f80534a-6dd5-37fd-8807-86674cb6077a | -11.60647 | -43.62373 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ba1b7aaa-12a0-327f-9048-ff94f61de095 | -12.20307 | -44.74924 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 575d8d38-336f-31c8-8241-34c6ee28b4f0 | -14.05258 | -43.84324 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 577bd28b-b59a-3e14-8ebd-4232ca43d80b | -12.21438 | -44.73809 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0ba32453-3dba-3587-b6db-0682a551002d | -14.82981 | -40.94424 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 1ed25d1b-046c-34d5-a4b8-83c25f60afec | -14.76864 | -40.89923 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 3342eb83-6b44-36a8-9f91-4f6182f98cad | -14.05114 | -44.80442 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 56bad92a-998d-3bf4-9fe5-3b07a2faf550 | -14.44763 | -43.93118 | 2026-10-09 15:58:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3c0216cb-5fc2-387b-b1b0-b445a1a8d69d | -15.91007 | -38.95319 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 54613dfa-fc01-3f0d-a69c-71e9d60a5c64 | -12.14854 | -45.36032 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| da23137a-7d09-38f0-8b10-f7b205db9677 | -11.58547 | -43.63823 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 60fa2203-0638-37d0-933b-50420915ff2f | -11.96417 | -43.46585 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ac1d1ec2-7fde-30cf-bd73-8056296e5137 | -15.03484 | -41.27743 | 2026-10-09 15:58:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| aadd1135-83dd-3e80-b21f-711a31fe9bec | -14.66994 | -41.79288 | 2026-10-09 15:58:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9a7784cc-8c82-34bb-b616-1c8e513cf18d | -11.47061 | -43.39029 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2baa4847-9550-3fdc-b4ba-778b413a1786 | -11.58741 | -45.39437 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e952da6d-95e2-33ff-ab4b-e7e26db16540 | -15.24584 | -40.53074 | 2026-10-09 15:58:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 29dec7de-0ff0-3c3e-b30e-7fb8c4f7a1fb | -11.66252 | -46.77414 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 92d60e8e-cdff-3964-9b6e-bd2498fa1965 | -16.12332 | -42.85381 | 2026-10-09 15:58:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 77798d28-4bad-3c77-ba2e-949e565eaadb | -14.60631 | -46.57598 | 2026-10-09 15:58:00 | NPP-375 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bddadab5-137f-3545-a53e-2d89afce56bc | -12.36657 | -46.57587 | 2026-10-09 15:58:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| a087d9bb-46a5-3916-a70c-dc7b1852c737 | -16.94207 | -46.6223 | 2026-10-09 15:58:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8121ff4a-71b3-3c41-9cf8-bbc40d1e6ec4 | -18.17492 | -41.96737 | 2026-10-09 15:58:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 14dee2fe-3223-3681-be76-447ed811220c | -12.24037 | -44.75687 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 33969b48-e917-3375-9b6a-da5aef1f45df | -11.61139 | -43.6109 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 03783fe2-073e-3c82-82b4-5976f1f175b4 | -12.14112 | -44.74008 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed082344-3653-3a3f-8bae-0aea656a0b98 | -15.26217 | -42.37098 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 5a6b1aa2-a53a-368b-8243-280f61948fec | -11.9857 | -43.49977 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1b3898f5-92da-3486-87ff-f1400d868a69 | -12.19854 | -44.81983 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 874abbdb-516b-33ed-8632-109e99af5ff1 | -15.38246 | -41.90195 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 6bf95223-ad95-31d2-a282-0a863b5c3930 | -14.65117 | -41.27372 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| ce8ec9b9-6ade-3822-9db8-43d63449f8d6 | -14.49066 | -40.82321 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 713b0612-fd20-38ac-b9f3-f0365690d772 | -11.57971 | -43.64297 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 5d3a64f1-674a-3e72-85b0-ed07f80d4dd3 | -14.05859 | -43.84258 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3af53d6d-975e-30dc-9267-a39093a2d228 | -14.05643 | -44.79325 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e28bd917-6d2f-3f71-90f1-12f478a8edbe | -12.29475 | -40.28463 | 2026-10-09 15:58:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 062f7b5c-5574-366c-817b-ee55a8a212ec | -16.82261 | -42.29644 | 2026-10-09 15:58:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6fbc2282-4493-38a3-9fb4-5abb09361c81 | -11.464 | -43.38331 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| cb7f10e6-7035-3295-a265-1d599777e68b | -11.69053 | -46.77201 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f8ed5cf6-3311-34b4-9931-d8b697d4dd7c | -11.61186 | -43.61486 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 19887f03-efc1-38c8-8fb6-3978cc3b129a | -11.58691 | -43.70073 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b835bdda-05e2-3661-a40e-74ff7546368a | -13.24609 | -39.7646 | 2026-10-09 15:58:00 | NPP-375 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| bbd868ae-46a8-3474-a75e-6ec85f941d78 | -17.15843 | -46.12939 | 2026-10-09 15:58:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 65b3fbe3-3f8e-3ed2-ae3c-8aa59f7896eb | -18.32994 | -42.37485 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d0c6598b-8319-367d-835b-cde57779d396 | -10.83229 | -40.30487 | 2026-10-09 15:58:00 | NPP-375 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c428953f-f86d-3595-9467-00a277d41b56 | -15.38787 | -41.90148 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| 57448733-1e60-306d-a32f-1c36d1e7d468 | -12.23686 | -44.78223 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 30b5d436-dc3a-3419-ab14-1ad2ed1a358d | -17.84469 | -42.16835 | 2026-10-09 15:58:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| aa898ecb-bf85-376d-89d3-990bef5aca05 | -14.05756 | -43.8336 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ced2853d-d4f8-303d-8e3d-62b3f10fbe0d | -11.61233 | -43.61884 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f43dafea-6e02-3149-9419-4bae38bb560f | -12.22014 | -44.84259 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ce58f605-f8ef-39c0-b8d1-27378aec1c71 | -11.59751 | -43.69238 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 490c35b0-65e4-3bab-b055-9baf215e23e8 | -15.25295 | -42.377 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| a9606261-a28a-3fb4-8a70-fb197886832e | -13.28347 | -46.96463 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| fa539dcc-2a25-3fc2-9d8f-49d4f11971a7 | -15.00316 | -46.25438 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f48d3b2f-005b-3238-8915-ebef8fae17eb | -16.94219 | -46.62192 | 2026-10-09 15:58:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8227e87-d83f-36f5-9432-50dc2919c8a6 | -18.32246 | -42.36878 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| 2aef6f0f-c907-34b4-b764-7a47fc9f0a2f | -17.29796 | -41.21957 | 2026-10-09 15:58:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e0ca8b92-58db-3f25-a153-133870d0a151 | -16.26831 | -44.17385 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3b903b78-6b1a-3682-ae76-ca7a3172b2d9 | -11.60122 | -43.62839 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 05c62449-a7f4-3099-8e6c-43dd96e1e2e8 | -11.48353 | -39.77353 | 2026-10-09 15:58:00 | NPP-375 | GAVIÃO | BAHIA | Brasil | 2911253 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6e5ce2f3-3d16-3b59-8613-9fef39f0055d | -11.89251 | -41.62689 | 2026-10-09 15:58:00 | NPP-375 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| d26eef5f-c7a6-3b2e-b13f-2b1f84be16c1 | -11.59314 | -43.70399 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 8ab5005b-9459-3fb8-98f4-1da250088e00 | -14.01269 | -41.85068 | 2026-10-09 15:58:00 | NPP-375 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7b0fac77-a8af-33f1-aea3-735f4fedb1c2 | -11.82645 | -43.59076 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 69b3eeee-36ce-3509-8e39-0fa87b3e9ba8 | -13.77467 | -43.47171 | 2026-10-09 15:58:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3df75859-22df-397d-8bdd-84cfa8f1e088 | -12.21629 | -43.95288 | 2026-10-09 15:58:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| bb2bedfe-7d07-38dd-8e96-e8b6306e8415 | -12.15791 | -44.73955 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d981f6de-feee-3a14-9cd0-cde890270cb7 | -11.98479 | -43.4923 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9220d47e-e91a-39ea-b62d-bcbf49e58dd7 | -15.26355 | -42.37142 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| d6280678-0e1d-3186-a0aa-923c368cbbd0 | -14.0634 | -44.81087 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d8bbdda5-1d77-3087-8fcd-4ff1149cb5e9 | -11.89028 | -47.37987 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1232897c-073e-3dfa-b4dc-7a8f36ff97c1 | -12.1939 | -38.99573 | 2026-10-09 15:58:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d8e321d2-fdbd-3453-9eff-312b9082da7b | -11.98438 | -43.48895 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 648004ea-6c0d-384a-9e1f-f357e91a14fd | -11.57643 | -43.66365 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4fedf9e3-03ac-37fe-a73a-c71227ec3b06 | -13.97014 | -43.93401 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c6aecc3a-24f9-367c-8e33-fcaf58a4f0a8 | -18.32426 | -42.37635 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 7155b3b8-e615-3c00-8d3f-e70c59aef789 | -14.60289 | -41.21527 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2a049c58-4b62-37d1-9645-88d1c484713f | -14.52143 | -41.25377 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 36.8 |


[Clique aqui para ver as próximas entradas](README263.md)
