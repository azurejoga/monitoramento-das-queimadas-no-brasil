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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b2073fd-1009-32a0-9425-fb062f2aa6eb | -20.9618 | -49.751999 | 2025-01-08 00:51:00 | METOP-C | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f82d1ec-d84f-3637-81ea-497b0a316b50 | -20.6509 | -49.2957 | 2025-01-08 00:51:00 | METOP-C | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 60d0076c-662a-3087-9c15-98a3da55a807 | -2.02 | -52.069 | 2025-01-08 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e41de33-48a3-3680-939e-b509fd7d8310 | -20.6525 | -49.303299 | 2025-01-08 00:51:00 | METOP-C | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d9ed13d2-9517-3f23-ba9f-4dda0607e03c | -20.960199 | -49.744099 | 2025-01-08 00:51:00 | METOP-C | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c88e438d-7d71-3fb5-a0a1-c9b1d82d78bb | -23.756701 | -50.3232 | 2025-01-08 00:51:00 | METOP-C | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 517156c0-bccc-3e20-bf48-75ed46c10499 | -20.6607 | -49.2934 | 2025-01-08 00:51:00 | METOP-C | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1b693dc-66a4-3da6-9b63-879ce4136929 | -20.9585 | -49.736198 | 2025-01-08 00:51:00 | METOP-C | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47ecfe2e-f968-3205-b9be-7f9c127ef509 | -1.3569 | -53.7206 | 2025-01-08 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df67b4c6-2173-368f-aeee-72cae138e9f7 | -22.4177 | -49.6586 | 2025-01-08 00:51:00 | METOP-C | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d887b8e-8c42-3b99-991b-23f45a211857 | -23.79361 | -50.26975 | 2025-01-08 01:06:00 | TERRA_M-M | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 89fed200-3e4b-30d6-8656-520c775f56c9 | -23.79494 | -50.27943 | 2025-01-08 01:06:00 | TERRA_M-M | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| a0c73604-c6c3-3cfc-abf8-d49629baa5d6 | -23.75715 | -50.33521 | 2025-01-08 01:06:00 | TERRA_M-M | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 93eec6f6-80cc-35c4-a4cf-a48bd6e0a124 | -22.23355 | -52.01346 | 2025-01-08 01:09:00 | TERRA_M-M | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| e552845f-9133-33b4-8a39-0928a696258b | -20.65343 | -49.30386 | 2025-01-08 01:09:00 | TERRA_M-M | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0be0ab06-a0fd-350d-89f2-b07e7d9624f1 | -20.95804 | -49.74847 | 2025-01-08 01:09:00 | TERRA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 58af703e-c95e-350e-9b98-66a383ce8597 | -20.64437 | -49.30536 | 2025-01-08 01:09:00 | TERRA_M-M | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9bc59acc-2ec5-3f0a-be4b-6f498e6fdcfe | -20.95942 | -49.75809 | 2025-01-08 01:09:00 | TERRA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 7e310d9a-dd15-38bd-ad04-e3557b8aa344 | -21.55522 | -54.2007 | 2025-01-08 01:09:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 32a36eda-e6ba-32c3-a461-012da980b211 | -20.65488 | -49.31369 | 2025-01-08 01:09:00 | TERRA_M-M | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c077bb98-6bf1-3e1d-a15b-9040ffee7d20 | 1.34845 | -60.04168 | 2025-01-08 01:13:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 497d7a47-6135-33e8-a79b-58cce4e0afa2 | 1.05137 | -59.55203 | 2025-01-08 01:13:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 20e6f385-a2d3-398a-a5c5-4ca2908da30c | -2.01412 | -52.07434 | 2025-01-08 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9809f14d-20a0-307d-97d5-400f4969097a | -1.36078 | -53.72459 | 2025-01-08 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| aea59983-0a68-33dd-919e-08892d97ba76 | 1.34788 | -60.03587 | 2025-01-08 01:13:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7fb92a80-c69c-38a6-b538-251f3d0a3805 | 3.38217 | -60.2112 | 2025-01-08 01:15:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e5f59a64-5808-3233-9424-5f0a977e0891 | -9.35186 | -35.50239 | 2025-01-08 02:51:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c3cf9e90-71bc-37f7-a32e-99458cf545ae | -9.35827 | -35.50372 | 2025-01-08 02:51:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8076f386-11da-3dae-967f-7f77acf3443a | -6.64691 | -34.98866 | 2025-01-08 02:51:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cd9f233a-1fbf-3c1f-b54b-bfe95f7cab2e | -9.05122 | -35.33134 | 2025-01-08 02:51:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 9a19c4a2-ba39-38b7-9e55-764463006868 | -6.91786 | -35.00156 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| fd47c77e-677a-3339-a82d-506a2ef17eb1 | -6.91474 | -35.01802 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| da05650d-f8fd-35c5-86be-b99b2a185d68 | -9.36465 | -35.50514 | 2025-01-08 02:51:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7485aa43-a9e0-37c9-a990-337afc63020f | -6.91093 | -35.00475 | 2025-01-08 02:51:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| f9d12ca2-7c90-384e-b16c-a0c01c670d06 | -9.05225 | -35.32602 | 2025-01-08 02:51:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 8c7c1154-53c2-3bc8-9d8c-e196ec873da0 | -9.35721 | -35.50919 | 2025-01-08 02:51:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 09d06f64-1835-328d-a1a2-71d3f264b4ec | -6.92402 | -35.00651 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 46c7d9fc-212f-3a7a-99f6-316cc651a996 | -6.91546 | -35.01671 | 2025-01-08 02:51:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| fbefd3fe-5487-3ada-9074-e649c7e02f61 | -6.92233 | -35.0134 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 18abda18-0bb6-3117-93d8-9bcb0e60713e | -6.91646 | -35.01122 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| 0df1d455-be36-3500-ac0e-2c014ff0ff2a | -6.92302 | -35.01198 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 61c9e77f-1ae3-3053-b794-d746b74e6e9a | -6.92337 | -35.00787 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0b5eb3e5-606d-3c81-965f-7572b6242909 | -9.35082 | -35.50781 | 2025-01-08 02:51:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4b166744-ca2e-3eb6-a162-0ec91f3c9876 | -6.91847 | -35.00018 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| a9934680-d7a4-3940-833c-b273c320a0b3 | -6.9189 | -34.99605 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e2254cf1-64c3-3930-b4d7-10bd8af20006 | -6.92198 | -35.0177 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00d35cbe-e49e-3f15-b64e-f650b6d024a4 | -6.91747 | -35.00568 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 52.7 |
| 2dbcc8cf-bebd-31ae-89d5-5f8131758b65 | -6.91578 | -35.01255 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 2fb0efd0-04af-3370-bda3-1018e458a9c3 | -6.91681 | -35.00711 | 2025-01-08 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 02f3dda3-5a8e-335a-b3df-a0dbeae7f69e | -10.59604 | -37.02105 | 2025-01-08 02:53:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d303f863-4e4e-3898-b0d8-8ba7d1a9646c | -5.92546 | -35.62746 | 2025-01-08 03:14:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d95b4172-0a8e-3b1a-ba5c-74ecc3873a82 | -5.95072 | -39.68599 | 2025-01-08 03:14:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 23ac8112-9c87-36be-a96a-8c11dac325ed | -6.84804 | -35.25863 | 2025-01-08 03:14:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4fb70965-86f9-3f8c-9b9a-0d9919fa9e1d | -5.92546 | -35.62584 | 2025-01-08 03:14:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 53b181e5-3280-3b7f-8acb-8fd37fcdfb27 | -5.94474 | -39.68495 | 2025-01-08 03:14:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 54ea0d60-c3d0-336d-b014-18b89147e34c | -5.92089 | -35.62509 | 2025-01-08 03:14:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9d4928d-ab8c-3712-ac3a-753eddba32c7 | -7.68558 | -35.404 | 2025-01-08 03:17:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f909f4d-147d-3a2e-be43-b5f60589a821 | -7.47618 | -34.84596 | 2025-01-08 03:17:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d44a13b-d32b-3db0-8b4e-50f1ded9f0fd | -11.0635 | -38.43818 | 2025-01-08 03:17:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1978dbac-a9f0-3c9e-aca7-a1b9a8de04aa | -9.86956 | -36.27428 | 2025-01-08 03:17:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 894afe68-5683-3ae0-bde9-10850e7559cb | -9.35886 | -35.50499 | 2025-01-08 03:17:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a18ca78e-728b-3b7b-bd82-c225bf603f1d | -9.35031 | -35.50344 | 2025-01-08 03:17:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0d814316-1aee-3f33-91aa-a92d50b7a870 | -10.30553 | -36.44465 | 2025-01-08 03:17:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11619c9a-1bae-3ec0-8ec8-d1fbf5a540a8 | -9.05021 | -35.333 | 2025-01-08 03:17:00 | NOAA-20 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bbded44d-145e-3684-9185-dc9e72ffd48f | -9.35458 | -35.50423 | 2025-01-08 03:17:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9e727743-b727-3bd9-ba8b-e2c32305fa53 | -9.05517 | -35.3297 | 2025-01-08 03:17:00 | NOAA-20 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 019ca51e-5b19-3a1d-bea7-e3d2992b9331 | -8.06288 | -35.12283 | 2025-01-08 03:17:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4b770feb-7e6e-31e2-8fb6-e5aa3d553e7b | -7.68096 | -35.27339 | 2025-01-08 03:17:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f616c53e-2614-341d-81a1-3bce6d74618e | -8.0622 | -35.12685 | 2025-01-08 03:17:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0175e20f-6bf6-3bff-96d2-a83f5d10cb15 | -7.71269 | -35.13951 | 2025-01-08 03:17:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 84e7e705-dd2c-35e1-83f4-b11cca2c449c | -8.06645 | -35.12766 | 2025-01-08 03:17:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e9395b65-ac11-3d8c-b532-0312115f8379 | -9.05092 | -35.32894 | 2025-01-08 03:17:00 | NOAA-20 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 673390f9-280e-3c3a-bc6d-09163799bb6f | -10.04717 | -36.49452 | 2025-01-08 03:17:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4c87764c-9af7-3773-95a4-2e1b1f161acf | -9.39282 | -35.69323 | 2025-01-08 03:17:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1500931f-577a-3603-8876-25ddc7f9e832 | -7.68631 | -35.39972 | 2025-01-08 03:17:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20f6d2f6-778c-335f-8d09-29b363bd12aa | -7.34924 | -35.23361 | 2025-01-08 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 695b365b-d87e-387a-96e8-109ca7a46b00 | -9.86876 | -36.27875 | 2025-01-08 03:17:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8779e74f-e12c-3caa-8347-e6ef3fcfc896 | -9.39443 | -35.69253 | 2025-01-08 03:17:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5540f4e5-17e2-3f27-8fc4-05fcab31dfd5 | -2.8829 | -40.30074 | 2025-01-08 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d645c403-9aa1-35a6-9fc3-40014f8b3e70 | -7.13999 | -38.8628 | 2025-01-08 04:08:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1459f5a7-053a-3dca-8597-b16965e76863 | -4.35777 | -38.15606 | 2025-01-08 04:08:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b3e1d53-a057-39d8-a697-e65e7efbe04f | -10.05104 | -36.49866 | 2025-01-08 04:08:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61e23984-4f7d-3220-93ed-64998dc5471c | -5.69429 | -35.57364 | 2025-01-08 04:08:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe2b41a7-ad5c-34f7-9b8b-ac4ca9ac1eb7 | -9.05572 | -35.32915 | 2025-01-08 04:08:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| fa19e716-7672-3023-a74c-b2527fb30b33 | -7.48612 | -37.07673 | 2025-01-08 04:08:00 | NOAA-21 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fbb77999-70ff-3d00-bdb9-627c545dab2a | -8.6536 | -36.90755 | 2025-01-08 04:08:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b0ef24f-254d-331e-894d-026b8341cb99 | -5.95418 | -39.68175 | 2025-01-08 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b40bb610-5cb4-370e-a286-91a3f2ac7879 | -10.32733 | -36.71833 | 2025-01-08 04:08:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f5e6ffe1-697a-391c-9e23-a0a84aeb9b15 | -9.05636 | -35.32447 | 2025-01-08 04:08:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 1b157b98-ee21-3574-ae17-21fa241d5b0d | -10.04549 | -36.03751 | 2025-01-08 04:08:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f774cba8-fac6-3179-9554-c0650283d917 | -5.95022 | -39.6849 | 2025-01-08 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 70a08753-5406-3959-a30d-3ff41e3acb1b | -8.07155 | -35.12591 | 2025-01-08 04:08:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad87b500-ca89-3b06-9b90-38b6d717fe51 | -6.73351 | -38.14816 | 2025-01-08 04:08:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df2b9e33-3486-3ab7-86c6-2ed4407d8e7c | -3.55615 | -38.84856 | 2025-01-08 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee1b569c-84b7-34c7-a209-bacbeddf4005 | -6.54469 | -35.29774 | 2025-01-08 04:08:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a2f6f6e5-6366-3612-8f3b-a70e3b79cbfc | -6.54529 | -35.29349 | 2025-01-08 04:08:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c0553221-7724-39fb-96f0-b3991fea3978 | -3.94938 | -38.33926 | 2025-01-08 04:08:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ac32729-5493-302f-a4fc-44e6eb004849 | -9.35553 | -35.50047 | 2025-01-08 04:08:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5e5dbd5c-ad0f-32f4-aa37-4d411dc98c82 | -10.32292 | -36.72122 | 2025-01-08 04:08:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5884139-771f-3cfd-9679-5f08cc3f761c | -10.32679 | -36.72219 | 2025-01-08 04:08:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README2.md)
