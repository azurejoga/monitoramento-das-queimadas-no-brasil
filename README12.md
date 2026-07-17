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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5fee7e5-5efc-32f2-a59b-8d22e4d04a47 | -28.84319 | -50.69668 | 2026-07-17 04:44:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f52bcdd3-b8bf-3913-a217-9bfd93686553 | -28.26502 | -55.08772 | 2026-07-17 04:44:00 | NPP-375D | DEZESSEIS DE NOVEMBRO | RIO GRANDE DO SUL | Brasil | 4306353 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 4611c480-dcc3-38ae-84fa-d24782c3d22a | -31.70734 | -52.21308 | 2026-07-17 04:44:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 1b127995-1ed0-3e43-8462-40ba808a2a58 | -28.89402 | -50.73008 | 2026-07-17 04:44:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3337f271-d356-3f06-b8be-63c23dd9fa8f | -29.8967 | -53.95837 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 9e4436b3-bc83-3518-ad20-0887e2cd2608 | -28.68527 | -55.39416 | 2026-07-17 04:44:00 | NPP-375D | ITACURUBI | RIO GRANDE DO SUL | Brasil | 4310553 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 63265408-328e-3e43-8b31-c94723c762e3 | -32.34907 | -52.39584 | 2026-07-17 04:44:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 2ff9a502-f3ec-31d2-b775-5c61008e1173 | -28.94487 | -55.2913 | 2026-07-17 04:44:00 | NPP-375D | ITACURUBI | RIO GRANDE DO SUL | Brasil | 4310553 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| de056209-4a59-38ce-bfc2-8e2a6acf924b | -29.89331 | -53.95759 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 5f860723-7e4b-333e-829d-b67956cf6068 | -31.71671 | -52.21928 | 2026-07-17 04:44:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 5bdb310e-0008-392f-9009-82f6fee9f024 | -29.49035 | -56.09901 | 2026-07-17 04:44:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 84de0406-5f28-3193-9b90-ddca17156ce7 | -32.3524 | -52.39655 | 2026-07-17 04:44:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| eb4c5442-6b37-3664-9164-67e4b944feb7 | -29.22725 | -55.77139 | 2026-07-17 04:44:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 7a8cc76c-c086-3937-a7f7-5c594d6eb71b | -29.89598 | -53.96252 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| afa5dc12-bbec-3b20-892c-4b3c80745a4c | -27.34591 | -50.72902 | 2026-07-17 04:44:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe007aa8-e1fa-326a-9769-238ac489eb60 | -29.89403 | -53.95343 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 5615040b-9596-3280-a3f5-662ea0180906 | -29.90009 | -53.95914 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| b57f89ba-e9a5-3103-a47f-0243ac242c2e | -29.22834 | -55.76933 | 2026-07-17 04:44:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 15393f63-c355-346f-8a30-20d48d481f29 | -29.49248 | -56.09606 | 2026-07-17 04:44:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 512505ea-48fc-3053-9446-b13588d55c2e | -29.09851 | -50.61847 | 2026-07-17 04:44:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 886644fb-12f0-3d7d-b374-7b7354a48c41 | -28.26711 | -55.08971 | 2026-07-17 04:44:00 | NPP-375D | DEZESSEIS DE NOVEMBRO | RIO GRANDE DO SUL | Brasil | 4306353 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3f4bdcc1-7ca9-3277-9de6-71a5dba8abdd | -29.32799 | -50.62144 | 2026-07-17 04:44:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7578bda-fa82-34ae-8925-c862fa28ad57 | -29.72413 | -51.89901 | 2026-07-17 04:44:00 | NPP-375D | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 741df300-dd96-301c-ae8a-201ec3d3ade6 | -31.72005 | -52.21998 | 2026-07-17 04:44:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 04ec31c0-c55f-31ed-af72-cfa8ef93d8c8 | -31.71004 | -52.21787 | 2026-07-17 04:44:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 67de4b21-61c5-3d4e-acef-3c8c951d8f04 | -29.69332 | -55.50702 | 2026-07-17 04:44:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 5e0d80d5-0bf5-3ae0-84dc-53d38f0d4435 | -30.98838 | -53.26318 | 2026-07-17 04:44:00 | NPP-375D | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f9428465-5da6-371f-ba89-e083da35d1a2 | -28.84259 | -50.70073 | 2026-07-17 04:44:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a23035a8-a687-3b3c-9c7c-d8ffb9f80c4a | -31.79964 | -52.45047 | 2026-07-17 04:44:00 | NPP-375D | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| f1555606-c2d5-33c4-ba14-32067e270071 | -30.74199 | -54.36634 | 2026-07-17 04:44:00 | NPP-375D | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 99e86615-7c9c-3c83-9418-e7ea8fa1d65f | -32.3497 | -52.39172 | 2026-07-17 04:44:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| afb39755-4a3f-3d0b-b29b-9e2a9853d9bd | -29.89065 | -53.95266 | 2026-07-17 04:44:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6ac110d9-a29c-385a-9d0a-5cb8dfcea532 | -31.79631 | -52.44976 | 2026-07-17 04:44:00 | NPP-375D | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| cc302129-f334-3624-bf57-35bdd86b6fe8 | -27.34926 | -50.72965 | 2026-07-17 04:44:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 788f25e2-3ec1-3130-88eb-f72e2be5f596 | -28.98529 | -52.39182 | 2026-07-17 04:44:00 | NPP-375D | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 24ab62be-faa0-383b-944e-099107adce72 | -13.2649 | -45.0877 | 2026-07-17 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| d8544ef0-7548-3534-a9eb-072f9e449cfd | -13.2456 | -45.0909 | 2026-07-17 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a865aa13-80d2-3ae0-a208-06c295ceb29c | -13.2451 | -45.1142 | 2026-07-17 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| d2dd8611-a98e-3180-9aaa-5312a5509f5b | -13.2645 | -45.111 | 2026-07-17 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 91db19d5-4c74-327c-b567-146ac2070275 | -0.85617 | -52.71389 | 2026-07-17 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b1c4b72-9c0f-3839-9a48-e0512d2df345 | -0.85561 | -52.71741 | 2026-07-17 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1db814b3-c866-3e46-bcf9-d4c522a6ad3a | -5.89705 | -46.20721 | 2026-07-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48208639-aac4-32fc-bd8b-5f38e5b20a10 | -7.69651 | -55.36547 | 2026-07-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64ca61a-6e7d-30ed-8b8a-9051aa6278e3 | -7.73138 | -44.55881 | 2026-07-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dda7b26d-9515-3b6f-bff4-1b7900a85089 | -3.73542 | -53.73499 | 2026-07-17 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0586a987-824d-3c5f-9a6f-2760f827ec62 | -7.2899 | -46.25102 | 2026-07-17 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1220ad0-a404-305d-88bb-98ffbd3b371c | -5.89595 | -46.21039 | 2026-07-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 650750b9-bace-33d8-ac03-8747c80268c8 | -3.07478 | -52.90746 | 2026-07-17 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 549e69a6-8070-3643-9ce3-89e2f9c03407 | -9.56967 | -48.6731 | 2026-07-17 04:55:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86c7f210-56d3-3276-8e08-0cf01127937f | -8.50868 | -48.07801 | 2026-07-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b196d71-7e95-39c4-8c52-1d3881985c8a | -7.89515 | -47.69879 | 2026-07-17 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd5e0522-93fe-3d56-a3fc-9c95775e152d | -7.72849 | -47.24121 | 2026-07-17 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45473d09-27d4-3f43-934b-844825ce32bd | -5.89636 | -46.21172 | 2026-07-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28112d44-28a7-3fde-9c95-2ea8188923e1 | -9.51211 | -47.13962 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dbd1ec03-1e78-3b9c-a83a-1bc3daf2a686 | -8.5092 | -48.07444 | 2026-07-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3892194-0c2a-3412-af1a-10baebd349a0 | -7.29442 | -46.25165 | 2026-07-17 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f1af38e-f268-3e3f-98f8-10de48bf0735 | -7.68918 | -50.59952 | 2026-07-17 04:55:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6f1789c-a1ea-3795-96f2-f12134d13c6b | -9.69586 | -47.69186 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acbd9f66-87fb-3f34-a1ca-1f40ba87f5c3 | -7.73098 | -44.56181 | 2026-07-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29ba176c-c55c-3524-9d0d-d5db052cf3be | -8.04922 | -46.72662 | 2026-07-17 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 165b722a-0865-37de-ac07-9667c608e68a | -8.65695 | -46.96603 | 2026-07-17 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6092f6b6-3438-3e04-8475-f19368e693e1 | -7.96152 | -49.64457 | 2026-07-17 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa816962-f635-35e6-98d5-48251d30bb40 | -7.69242 | -55.36876 | 2026-07-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2b93348-0306-399d-ba75-edad3a3db56d | -9.00144 | -47.99918 | 2026-07-17 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc6d07f-1478-3bae-925a-cbc67ba2f9ed | -8.51272 | -48.07871 | 2026-07-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 117bb618-eb66-3a72-ae1c-9ca9f5902693 | -7.2931 | -46.24911 | 2026-07-17 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7871f5d-5a7a-305f-bb6e-fb1d15afd76a | -9.56571 | -48.67251 | 2026-07-17 04:55:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c25670fb-50dc-3e1d-8cba-ebb0fbc74a9c | -7.90909 | -48.25745 | 2026-07-17 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ada3fb1-4c04-3287-a8f9-a49f80b3881d | -8.71471 | -49.60568 | 2026-07-17 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bad3802-26b3-350d-b879-a315aac4b187 | -7.69997 | -55.36606 | 2026-07-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9917775-5484-3493-bc66-62c5d52262af | -5.79681 | -43.63648 | 2026-07-17 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cad324f4-faf9-383a-a923-319fbe22df51 | -9.69531 | -47.69582 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cad1921-0200-34ff-a2ea-102844f1c2da | -5.63278 | -47.09706 | 2026-07-17 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf3b5a6f-25a1-3999-896b-32b39f7d2caa | -8.4726 | -50.22449 | 2026-07-17 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b22e90f6-ffc6-3317-b8c6-366cfd490b7e | -8.76175 | -43.93946 | 2026-07-17 04:55:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10f9fb3-ebaf-3115-bdb2-ebac6c378139 | -9.67585 | -47.89622 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 766af041-a0c6-3bca-98ba-20c0fd2329d9 | -7.72792 | -47.24517 | 2026-07-17 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ff1f4e8-79d7-3e8e-9340-27ffe40e6f2c | -8.04983 | -46.72235 | 2026-07-17 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3789f96-f811-34e8-9981-95438ca37e9d | -5.80257 | -43.63394 | 2026-07-17 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc8691f0-c563-3099-9d48-3d18aa13ca84 | -8.73477 | -48.06653 | 2026-07-17 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1014e218-4a5c-362a-9f5e-d9ece6c02553 | -5.8966 | -46.20587 | 2026-07-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84e78a89-d15c-32f0-a4e2-0b35c03b3ded | -7.96518 | -49.64511 | 2026-07-17 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e216ad1c-dd87-314f-bb97-eedc2f057302 | -5.80209 | -43.63725 | 2026-07-17 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6cd60ca-9e42-39c0-a18e-37fd75c3fff1 | -9.51271 | -47.13538 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ffb8b83-e91e-3d37-acc0-e096f890cfbf | -9.51649 | -47.14026 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 10d75595-95b3-3477-bbb7-553d22d138e7 | -6.0145 | -46.32262 | 2026-07-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3830958-7e1b-378a-b33f-339a117e5614 | -7.73329 | -44.56131 | 2026-07-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2808ce4-8ab3-338c-9d08-1bd9fa7217a1 | -9.69954 | -47.69648 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb18757-611f-3d03-8847-bd0997d671f1 | -7.6301 | -50.03572 | 2026-07-17 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ba95f94-0150-37c1-9c45-8e7d2538cbdc | -7.96454 | -49.64936 | 2026-07-17 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a56b63-b4b9-37d4-b661-2cd04fdc96a4 | -7.29505 | -46.24711 | 2026-07-17 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87e93887-5217-3cbf-a100-57b94c0d1865 | -6.2556 | -49.8757 | 2026-07-17 04:55:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24a192b3-2ca8-3463-b534-cdee7d5645a4 | -9.56645 | -48.6673 | 2026-07-17 04:55:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f83d86c-dae8-3cf1-9e69-5edc48d908cc | -7.91306 | -48.25807 | 2026-07-17 04:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fc2f368f-24f4-399b-bda4-49cd6ad3bd9b | -5.9129 | -46.67206 | 2026-07-17 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6be2e19a-0a9d-389b-b72e-203d2727d54f | -9.5171 | -47.13602 | 2026-07-17 04:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3273460f-edae-33f4-a4c2-c10e6637d2a5 | -7.72818 | -44.56065 | 2026-07-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f6717a3-3552-33ff-a80a-8ac47791c878 | -8.50569 | -48.07017 | 2026-07-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d41e711-4c17-3a9a-9291-aa51cbca6df9 | -3.85602 | -54.0797 | 2026-07-17 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c8d559-a6b3-3a11-a2ac-150788551c40 | -11.0603 | -54.59658 | 2026-07-17 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README13.md)
