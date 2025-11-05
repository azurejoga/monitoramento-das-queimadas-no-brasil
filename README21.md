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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c396d9b4-b203-3a1f-a5a2-23383cb142f1 | -5.77797 | -40.80376 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84df463d-bb66-384b-bc6c-b40ab511fbb5 | -1.25206 | -49.14583 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8662b7e3-77e2-3874-9090-3e6d97e9fb47 | -3.47371 | -43.64039 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8240736b-ca9e-33ef-a370-1a3b58c1ee99 | -3.49272 | -43.62883 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0aab2a7a-27d0-3006-bd39-36a1ced0d6f4 | -4.0965 | -47.28463 | 2025-11-05 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0069568-c77c-301f-842f-8cf1c3ffad42 | -2.97082 | -44.59521 | 2025-11-05 04:12:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f41042a-9799-3412-8f30-7e1246762f6a | -4.89465 | -46.85384 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 031d4983-adc3-3f0f-b83e-d3a8b56fd496 | -3.10446 | -51.0315 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65edb724-ad7c-39a9-ae44-56af1a967c1e | -5.65493 | -44.06811 | 2025-11-05 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff76a0b0-0808-3d47-8c13-c9674369c2ff | -4.86181 | -44.61459 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| efdc49b8-2e35-3955-a867-733bc0f8dc9c | -4.30327 | -41.45974 | 2025-11-05 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86628116-f59b-3e1d-8b77-c7459fc2dd7c | -4.63076 | -40.76884 | 2025-11-05 04:12:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b2fdddd-e622-3080-8be1-d1d515311cb7 | -4.40737 | -48.95453 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c71bf462-749c-3bb3-9ad5-17ca6ed9c9f9 | -5.76781 | -40.7556 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a26d91a4-ec43-3b5a-9fb3-9c9d4322b022 | -3.4418 | -50.21675 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7a9a81-97d1-39ae-ac6f-0539b462e608 | -2.37424 | -47.72657 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ac801d3-c059-3ee3-913a-c95db1f9eeb0 | -6.12728 | -41.69748 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3dc8d122-798a-3027-a6eb-d9640257b3b5 | -5.26389 | -44.13712 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad899b80-80f6-38b5-bb87-f63109c49ba1 | -2.62451 | -49.22831 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57bc55ba-9feb-344c-a7be-0cc76d48e29b | -3.70643 | -45.89118 | 2025-11-05 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86a4db8e-5eb9-3064-a4a3-8abef64ef093 | -5.03363 | -44.79029 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| facdae73-09d0-3656-bb04-65fdd4cde917 | -5.47116 | -43.58138 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6bd0ec7-411e-3a63-a394-597b9c9da1e2 | -3.40905 | -44.44222 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aab32c7f-a87f-3c00-9a0c-ba4f56fb412b | -3.41518 | -49.99634 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2d19093-069a-306d-a4c1-acd01590ae6c | -5.77678 | -40.81145 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc9de9e9-4049-3c63-8e6b-a16aaa2b358e | -5.42856 | -46.40932 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e896707-0b18-3771-a770-fd11b699c6c3 | -3.10912 | -51.03547 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2730f42-dc6a-393f-85d5-9dc9c037ec5b | -2.61529 | -49.22676 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59a93649-b730-3fd5-8b8e-84f40a971b89 | -5.08833 | -47.70519 | 2025-11-05 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a707dea5-9ce2-35b9-81f8-b19cb6fef688 | -3.12987 | -44.48013 | 2025-11-05 04:12:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed3bc519-0dad-3403-8a08-b11fce679b12 | -4.10826 | -48.02509 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 79a8b42c-a749-3fef-8c04-4add0e84bc44 | -5.92868 | -41.36557 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc020ef9-81e5-3177-93c8-73f0270b264d | -4.27865 | -46.93632 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0050e30c-32f6-3902-a0a7-9ea497ab131f | -3.05028 | -40.11684 | 2025-11-05 04:12:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 033aae88-82a2-3100-b2a7-1aa03b53f5b0 | -3.60405 | -50.62627 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce850986-5bd8-316b-9030-b656b7caafb8 | -3.277 | -50.76954 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d148372-ecd8-3e0d-a892-968c18bdaa37 | -3.47484 | -43.63329 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee0a42d4-5999-35ae-844a-c82b02a3e452 | -6.46689 | -39.16777 | 2025-11-05 04:12:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7781e23a-5f35-335a-9bde-e92a39a4e916 | -5.63295 | -41.12811 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8cabcb1e-6bd5-3ed6-8145-1d6271e2e948 | -4.23855 | -48.66983 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe506b1-1f17-3950-93b7-7cf2ce8009a8 | -3.50884 | -55.50461 | 2025-11-05 04:12:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56f08db2-3a13-329f-ba19-b5af6bd29a83 | -3.10965 | -51.03231 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21dc136c-4f6a-38ad-ac9c-ed58fd8dfc17 | -2.75194 | -47.7536 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b9929bb-75d5-32df-982e-fa71c239c9b9 | -5.72817 | -40.73801 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 873aa8b0-7571-3c05-946f-c28b173dc91f | -2.98157 | -48.71106 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c95adc2f-1247-3149-bc24-109df2f69943 | -2.84373 | -49.41186 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03e0bfe9-9a17-3130-b937-a605839885df | -2.75547 | -47.75812 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90680008-699b-382e-a928-d4a0b5dd81cd | -4.69742 | -44.76429 | 2025-11-05 04:12:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3308631-76f4-3119-9f2d-8a5b652ad750 | -5.5108 | -38.57883 | 2025-11-05 04:12:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a25dbb4-fd18-30ee-b1a2-1d131b587cf7 | -2.42039 | -49.29887 | 2025-11-05 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 583ef0cc-1bb6-3cf4-8c65-c6381de14d74 | -3.97304 | -42.1385 | 2025-11-05 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c10e2ae-d1a0-39b7-a0c5-fb0cf5a89b5d | -3.84291 | -49.90523 | 2025-11-05 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f5c657-4460-3c27-8d33-cba0c373f781 | -2.64876 | -48.512 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 0be13c07-3b49-3ada-a3ed-caf38feb18cc | -3.59388 | -49.28385 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef58cfef-8db1-30ac-9972-fedabc5bc3a7 | -3.47819 | -43.63382 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91696c61-4914-3f8c-9d04-0c1d11e013d2 | -3.55506 | -45.87872 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f8a870-8e98-3056-a1a8-7c7e69fc9f41 | -2.63629 | -48.50559 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7b51fe7-1760-3af1-95f6-52a4d7be461c | -5.44994 | -45.40322 | 2025-11-05 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90969ee4-7d85-32d2-ad57-5d261f269471 | -4.28949 | -43.78661 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 791695d2-9125-3646-a801-0dc41b957cdc | -4.36022 | -48.35913 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb06661-38e8-3f3a-9100-f0b803d11c79 | -4.4726 | -43.23414 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e51902d-72c5-3916-9b44-c4650a1baa1c | -3.41249 | -44.44276 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b3d1b50d-3ecd-3aa4-be1d-b4faef6d9536 | -4.55594 | -45.59735 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd68ad57-6aa4-30b0-baed-d4852ad52ef2 | -3.66631 | -44.80381 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf6a4e1e-9083-33b6-b9b4-f3c3397c9ac8 | -4.40956 | -48.94157 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8545e3c8-7b74-32cf-b6f4-4bdde5264f19 | -5.92811 | -41.3692 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2afec87-0765-3b1c-976b-c4218b86711f | -3.12642 | -44.47958 | 2025-11-05 04:12:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ae2735d-ae9a-35f9-b6df-2b18c8bea484 | -5.51824 | -41.14407 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| faa42ffb-54df-3a11-bdcf-87a5bfe9cc3c | -3.27751 | -50.76652 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5050bfb-a646-3ddf-98ec-3dc9c360e951 | -2.74234 | -45.55112 | 2025-11-05 04:12:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7666a850-8d86-3d2d-a454-6e5f748298d7 | -5.36052 | -44.74166 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8193049b-3f2d-3b65-bd2b-2901307c0cc3 | -1.24268 | -49.1443 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cdf01bc-c8b1-35e3-b8c2-c0ef86ad3b03 | -4.56188 | -45.56062 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0d7c70-44df-38b0-899a-cf9dd472db7d | -5.82574 | -39.2073 | 2025-11-05 04:12:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0726f7c2-ffdf-383b-83c3-11291eaab5a6 | -1.2888 | -49.15691 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fa277641-5c07-3260-801f-c47f5bef75f0 | -5.52786 | -41.14919 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1a745f8-5515-3a74-a4e9-6b0430882e49 | -5.91712 | -43.12678 | 2025-11-05 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01b498dd-2ebd-3394-b32e-a065228d5ca3 | -4.56016 | -45.59385 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b73a4f2-a48b-3742-a15b-be78c17042a1 | -4.51568 | -42.07845 | 2025-11-05 04:12:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62002c8e-6796-338c-888c-b41745060d21 | -6.34713 | -40.63479 | 2025-11-05 04:12:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90f1bd79-f16d-3075-b7d7-7052eec48f05 | -5.48987 | -42.1707 | 2025-11-05 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 18dc21cf-4b53-3885-94d2-acb7d19ba1ea | -5.91853 | -41.36406 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ba3798c-1748-32ce-b890-9c3a1565f1cc | -4.49021 | -44.5908 | 2025-11-05 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25427f0c-11fc-3d55-93ff-37e0a7cb8260 | -6.17351 | -40.66431 | 2025-11-05 04:12:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6f959b5-1280-369b-a5d9-a35dcf008242 | -6.10386 | -41.71572 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74da463f-314b-3692-a57b-07a30b77172d | -5.78364 | -40.81257 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cbdcbdca-01ca-3b9a-8bf2-96d8727f119f | -2.25372 | -47.99194 | 2025-11-05 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c37e50cf-ecb2-383e-964d-18a937a33e82 | -3.4094 | -50.84282 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55778745-a100-3bd3-b864-b4779ae292cb | -3.05314 | -40.12112 | 2025-11-05 04:12:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1e4b3bb-d7eb-3fea-a355-354771b72d0e | -2.89121 | -51.01776 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75466ab0-d32d-385c-a738-ba3dbcf15ea9 | -4.4632 | -43.2291 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3931ed12-99fb-33c4-aa3d-ef18cf0ea72a | -5.67576 | -44.74536 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da8f208a-56b6-30b0-a861-e8a89fd17814 | -3.23757 | -46.88082 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d66b9f2c-7bb9-3de4-a272-b4bfe2f3f0e4 | -6.46758 | -39.16321 | 2025-11-05 04:12:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b755739-1bf7-3cca-b8c8-79958a4a6321 | -5.92291 | -43.36839 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f96d8ce4-0902-37c4-adc2-e1bac19517f4 | -2.45264 | -49.42531 | 2025-11-05 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 220e5e2d-716e-3459-a259-fc2887c38007 | -4.11226 | -43.87934 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 735d6e6c-e6a0-3617-9e90-850dc9e0f212 | -2.73892 | -49.39256 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bc6cf94-c08a-3801-99aa-6284807f1c0b | -4.28628 | -47.17915 | 2025-11-05 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f46d3a1-09aa-39ca-8999-db7ffdad73bd | -3.23915 | -46.87114 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README22.md)
