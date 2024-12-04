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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f466fa49-14f3-3701-acb2-36ab8528a857 | -13.8015 | -41.568001 | 2024-12-04 00:17:00 | METOP-B | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 458a3abe-22af-33a4-988e-2cde2081bd86 | -4.578 | -50.448101 | 2024-12-04 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f64aede0-2461-3057-917f-f167eb9bebeb | -3.04 | -49.491199 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c22b6e64-ada6-33dc-9cd6-275e28054612 | -4.2904 | -45.112999 | 2024-12-04 00:17:00 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a696ab2a-fb1c-3f04-a146-fabdaf2e6ca4 | -2.5463 | -45.375198 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7afa53-08f2-3b8f-a093-223db83bee2f | -3.8451 | -46.514 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36ca26d8-6d73-36b3-a5e4-149adda4ed6a | -4.4338 | -47.4828 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2e38ded-38c1-3475-a619-dd384f700abd | -2.4444 | -45.698502 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 691758f4-c70d-3af0-8060-bfcbb332253a | -4.3783 | -43.334702 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 065da727-82a2-3a2b-89b2-6a9e4519ae75 | -4.2936 | -48.191299 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b6328ce-3b08-3a40-9962-8f152716c4dc | -4.2968 | -48.205601 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be6efb48-57ed-3b0e-8c6f-85a83f020e97 | -2.9474 | -51.384602 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2adb21-33ba-3be9-80c9-61a88aee76f6 | -3.1268 | -45.980801 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91a153d7-1ef6-3a0c-a02c-aba7b91614c7 | -3.1283 | -45.987801 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1cbd83-503a-37a3-beeb-7e5c4eca2e44 | -3.3354 | -51.190102 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3958613-91b3-3a02-a0fb-bd06e8f08884 | -4.1091 | -43.9123 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eddb7480-6266-3557-b1ff-d7dbd94d504a | -2.7145 | -45.526199 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 314e493b-9305-3900-aaaa-1b660205f3af | -4.7142 | -45.662601 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52048ebd-9ee4-3438-8f5e-c07f5596b1b2 | -3.0628 | -53.250198 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06896873-a078-3335-bed3-34b71dbd1f8a | -2.8221 | -53.040798 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdbc885-0bab-3aa2-a6dc-ae9c20a47838 | -4.5006 | -48.011398 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdbe2fbd-ba09-36f6-9236-59dfa0ab3e09 | -4.1011 | -43.922501 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 386fa82a-cbde-38a0-8ad1-a4530d1dab8a | -8.436 | -40.4566 | 2024-12-04 00:17:00 | METOP-B | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| baefe516-0e0b-33b0-a15a-e1dbc254c4a1 | -3.0785 | -49.2029 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b495e002-75a5-3c20-8944-38b8e32d5994 | -2.7205 | -51.795898 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0365b22b-cdb9-3a82-9f4c-3c04e1abd0b1 | -4.2484 | -47.5746 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734cabfa-fe95-3b62-a17f-8919c20c6b7b | -3.7041 | -50.4436 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e889ea0-5ef9-3b2d-a542-e6b2318cead6 | -3.06 | -53.237499 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7de3f8-6174-3601-b859-ab47dddacee9 | -3.3355 | -49.755798 | 2024-12-04 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ad1421-4acc-3b63-9d1b-767f425d4b4e | -3.5301 | -49.890701 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f091298-604a-34ab-b53b-65864750ebb8 | -1.5065 | -46.7463 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fff76a19-06a0-3d32-82f5-0eee3c4162cd | -2.6256 | -45.724899 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a98c6ed-3dd8-3083-aa4a-8a9e4ba90a8d | -5.5777 | -45.152302 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93c1c850-5585-36c5-8931-0a38e121f604 | -5.6087 | -43.933601 | 2024-12-04 00:17:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04598fb9-9661-38e2-8e60-cdbc7784cf66 | -3.3454 | -49.753601 | 2024-12-04 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b26e497a-c563-3408-9a07-12aa7744da0f | -1.6131 | -53.4986 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 886425db-5292-3560-a9d6-8f0158c44820 | -3.5777 | -50.290501 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8fb2c7-880b-3ff0-96ee-5006c4514b20 | -9.8566 | -36.592201 | 2024-12-04 00:17:00 | METOP-B | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4da02d53-e787-3356-ade9-84e2282d383a | -3.3191 | -50.328899 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 873b8678-ae20-3bd9-b8b3-350fb8466bab | -3.7289 | -50.0457 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 081cdafe-77bf-3c46-9709-605030daacb2 | -3.1641 | -44.422298 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6461fed2-db11-34e4-8b83-cdb9e457ae03 | -3.4836 | -51.5355 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3b762e3-2d2a-338e-aaf0-694a6ec246b1 | -2.6752 | -45.216801 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 615b1b6f-4e8f-38a5-8a87-9ea7f56c6aad | -3.4477 | -45.8508 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa6fbb04-01bb-3ceb-b133-a874b2363b4e | -3.5478 | -51.315102 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b92072-c5bc-3784-8776-c29e9f17acf9 | -2.8718 | -51.784302 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca11082-e62e-3ff8-9089-26b3d0e3ce9e | -6.0915 | -48.0383 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43f0a327-7787-3188-99d9-be264dad5767 | -3.0383 | -49.483501 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3add7ef-8cf4-384b-9951-fc5f8706dd1c | -3.5679 | -50.292599 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 537a54d0-71d2-37e2-b077-2641be63b5bb | -2.5365 | -45.377399 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6898ba50-fb17-33c0-9caf-dc36ffbbf6b9 | -2.7311 | -46.236198 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 795879f0-d270-365c-9eca-7a5feed0f8a8 | -4.6848 | -45.669201 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8163634-f621-3c14-a0f6-e820a5e0d683 | -2.1635 | -46.6437 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5864fdbc-7f7f-3622-8e7c-0697e8f312e8 | -2.0248 | -45.529499 | 2024-12-04 00:17:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7e8c1c-2e00-37a2-967b-ffcb59d42277 | -1.6542 | -52.719398 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7425d68-6c7b-317f-a18b-864dd4577297 | -6.0893 | -43.960999 | 2024-12-04 00:17:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b405d1b-1ba0-32e8-aa0f-5e5b0ec574ee | -2.6051 | -45.407501 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1f20a3-d709-35d7-ab4c-8572b8c30ff1 | -3.5319 | -49.8988 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a397ca5d-1513-3308-acc8-8d4b28f0331f | -4.3181 | -48.208401 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e848ea-0bde-3c2b-9d45-5e6b6e8ea9cc | -6.0817 | -48.040401 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3b0abac-fc31-3adc-bd2a-7f71e26749a9 | -3.8445 | -46.557098 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cceb6f56-d4f4-300d-9878-0700c3ea8093 | -11.0738 | -44.292702 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2f047fe-a202-3077-a886-284c1661cbcf | -3.1047 | -54.554901 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf7680cb-7a11-3a8d-8976-08322afbc8d8 | -9.8663 | -36.589699 | 2024-12-04 00:17:00 | METOP-B | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a64bac3-8e71-3030-aa73-a086551cfa84 | -4.0455 | -46.992199 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cfec718-ac3e-3563-bc0a-2e944dc2c89e | -2.201 | -45.6707 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d296fab-a62c-3818-a629-bcfaa6abad2a | -4.7401 | -45.686001 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 136c34bb-2f98-3483-a20f-97d828712b0d | -3.7298 | -47.558701 | 2024-12-04 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd28768-5da1-311e-9404-5c0c7d53cd57 | -3.5478 | -52.896999 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4017c77f-d866-3b26-9e9c-0b34aee21c0e | -4.623 | -48.006699 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75b1031b-19da-3853-a9a9-a50d71b8d126 | -6.0833 | -48.0476 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 250e7bb1-1f46-38a4-af22-ae5d4856fe87 | -2.5249 | -45.553501 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4465d5-8238-35b4-b4a4-d92935902a4b | -2.5201 | -45.396301 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8651377-6934-37f6-8d75-e98a3d9f2180 | -9.1926 | -43.148102 | 2024-12-04 00:17:00 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ac4a97b-9cb5-37af-adc9-bc7d256f7cd7 | -4.0478 | -46.590801 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 945a6eb4-3e86-3780-b9ce-bccd286fcaa5 | -6.9501 | -47.781101 | 2024-12-04 00:17:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0c692e9-75c8-3b23-87af-ffdc2c077c2d | -2.9581 | -45.191799 | 2024-12-04 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1268ff16-95e2-3b6f-91a8-51ceb2a86d7e | -3.8549 | -46.511799 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c571abd1-964c-3bc4-830b-4d30a18fe566 | -3.2503 | -53.6371 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d66a37b-7456-32df-b408-0aaa33aea68d | -2.9718 | -46.937 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c5d6f1-c5c4-3424-a215-845173cae824 | -3.9801 | -46.655899 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45276c65-a874-3c1a-b0ca-4c62eaf96f58 | -3.3727 | -51.034302 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a29c0d6-6136-3ed1-aa8c-4264b5b66dfd | -3.254 | -53.607899 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4e4d5d9-9609-39e3-bc58-15637eab54b9 | -3.5452 | -52.8848 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad724d18-a2a5-398c-89e7-e4b5effe224e | -2.2819 | -47.9002 | 2024-12-04 00:17:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1d7914-f9f6-3404-9cb2-1c190d7a119d | -4.9149 | -47.838501 | 2024-12-04 00:17:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28d2f6ca-4f76-3a78-86b5-6f20f10c2053 | -4.6262 | -48.667702 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 999f872c-800f-373d-b86e-ee19051dd7a5 | -3.1757 | -44.427799 | 2024-12-04 00:17:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94a86afe-be0a-3528-a60c-d36cd2425960 | -3.1904 | -50.6287 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 647449ad-1595-3f93-b1f2-a587f0a15f65 | -3.4146 | -50.157902 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e107f907-4e45-3ced-a68d-6c03f553e897 | -3.9672 | -46.644501 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50db4aa8-ca81-3b13-b651-8fc884af6a51 | -4.2921 | -45.120201 | 2024-12-04 00:17:00 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8566187b-aed1-3389-844f-557574274e2e | -4.018 | -48.800999 | 2024-12-04 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a24436-48b2-3960-921c-de44f22b8d3f | -3.251 | -53.594299 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd231ce8-142a-31b4-bd1a-d0a6d67789d3 | -2.6911 | -46.1507 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3140cfdf-cc97-39c5-b7ac-f25cda038ea3 | -5.6122 | -43.949001 | 2024-12-04 00:17:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b56b5a89-7e70-3565-b132-810cf5a2069b | -2.8026 | -53.045101 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e987aea8-cc8b-3449-826d-d82021580b66 | -2.8938 | -51.559502 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43182077-9321-35b2-941b-e1db317af36e | -3.5575 | -51.498501 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcfd3171-9008-3298-85f4-43d1352e80c0 | -3.4364 | -45.846001 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
