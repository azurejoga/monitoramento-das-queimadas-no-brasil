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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2898ab6-b2bc-3fd0-8ea7-6dc08b330be5 | -6.87117 | -46.25867 | 2024-10-22 04:17:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59fd2fb1-6848-3112-b0f1-bd61eb8be219 | -6.80173 | -46.47468 | 2024-10-22 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f23b6a6-c15b-399d-8c66-c83b41ed4bd9 | -6.7778 | -46.42317 | 2024-10-22 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d61fc666-157a-3d6d-95e8-398c266eeeac | -6.77403 | -46.25142 | 2024-10-22 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66ee1ade-b6f6-3e8d-9f2c-43c17c3bcddd | -6.64179 | -47.34578 | 2024-10-22 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e759e00-e4e6-36ee-a739-37e82fa12f49 | -6.64157 | -47.34332 | 2024-10-22 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a965ae-5236-375a-898b-422873c779fe | -6.64095 | -47.34724 | 2024-10-22 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db9569e-6801-3aa5-ba62-62e6e87affb7 | -6.63807 | -47.34271 | 2024-10-22 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 939627f5-050b-3218-82fd-ae2e2d31ea9e | -6.44729 | -49.91706 | 2024-10-22 04:17:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 303d6a8f-a9a2-36ca-9c1a-2544f1f52dbb | -6.35197 | -46.34431 | 2024-10-22 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d73d174-664d-3d83-ae99-3ef5e39ae0f9 | -6.24584 | -44.13229 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6f60ad5-ca6d-3320-b26c-bcd92384d3e1 | -6.2453 | -44.13577 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f94de4e-e58b-391d-9840-36343627e6b8 | -6.24475 | -44.13924 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f71fa8da-5a18-35cf-b7fd-1931b4a4249e | -6.24421 | -44.14272 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51304d62-c1ef-36f5-ae3d-efa3763c6d5f | -6.24253 | -44.13177 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c64cd7f3-409c-356d-94b0-3c187b8aabda | -6.24144 | -44.13872 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae5117bd-cc2e-3de1-b63c-57c6cc0c6623 | -6.23982 | -44.14912 | 2024-10-22 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35b7f3e-032a-3bcb-bc19-008fcf2ceba5 | -6.00816 | -44.52299 | 2024-10-22 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a477ced-c3a0-3145-b6e7-0d2e019a4c63 | -5.92682 | -44.73686 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc94f1d0-e290-3af6-a1d1-1bd1a21c7b7b | -5.92628 | -44.74031 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2918c5ca-2792-37ca-a540-5fa483b4701b | -5.92352 | -44.73634 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f40cabff-2210-3974-9220-7adbb734f89d | -5.92297 | -44.73979 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f270d69-318b-3712-b923-73034ee497dd | -5.91117 | -45.41585 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 102e5cc8-d791-31b0-b863-7ed52a3e0d9d | -5.9095 | -45.42635 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df86bc73-734c-3f71-9480-4ef87cb5a662 | -5.90785 | -45.41533 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e97ea5-af76-3eb9-8813-d66f14277c25 | -5.90673 | -45.42233 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 849fc5ab-36a1-39cd-b07a-b9b22d0c7804 | -5.90618 | -45.42583 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 198b922b-838d-3368-93db-025c47f036da | -5.84326 | -45.30916 | 2024-10-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ffc4967-7b2e-3ac1-b345-c52d99322816 | -5.84097 | -44.46163 | 2024-10-22 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3807678b-767c-3eea-be24-42922d83fcbe | -5.83322 | -44.6617 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc0c477-7a99-39ee-993d-c2420aa17683 | -5.83046 | -44.65773 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af34aee4-d4e2-315a-ba4a-c2e4e2420c8b | -5.82992 | -44.66118 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 533e2042-45e7-320e-b579-ada5b0b6012e | -5.82662 | -44.66066 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa69d25-5a87-3645-9440-0719c7572ee8 | -5.74484 | -46.39156 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 467d604a-2ce4-32d1-8cc9-135cd8c6cefd | -5.73931 | -46.44767 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d1b7c88-2db8-328d-8ccc-df32ffc04528 | -5.7118 | -46.02832 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef9f3b89-944f-3b48-ba29-45440ccde14d | -5.70843 | -46.02778 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377c214c-a357-3eb6-9e97-c549099fca9e | -5.69742 | -46.46855 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b6b1138-04a4-370a-b0ac-1252e78b77bf | -5.694 | -46.46796 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 057d3b58-975c-32bb-926b-89d465e0f1a5 | -5.68828 | -44.48355 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d743ba8-11b8-3f2a-a406-053813d288db | -5.66206 | -45.93917 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85a7f07e-b641-3d0b-b9b5-88b8b009375a | -5.66149 | -45.94276 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7db549d9-bf21-3545-9b9b-9e9fcd197345 | -5.6587 | -45.93863 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e96907f3-9e1f-32a8-8e16-177500f1d556 | -5.65813 | -45.94223 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20644073-a120-38a9-877c-c44586397097 | -5.65525 | -44.06444 | 2024-10-22 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c02b11-747e-3313-a37b-12e14a755411 | -5.62208 | -44.83657 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39566ab0-922e-3640-8518-b2d1fc0cb6e6 | -5.61932 | -44.8326 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab60a07-d794-3b54-8ef2-ce51e798d1a4 | -5.61878 | -44.83605 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c58b8284-256b-33ed-b155-5c07fd459634 | -5.59188 | -44.87779 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9efaaee0-c9f4-34df-9813-94666c630266 | -5.59133 | -44.88124 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8b9c843-b8d0-3507-a837-d4d25cdfc615 | -5.58911 | -44.87381 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 38abe3eb-6c6c-3f01-a792-569f9d50a4a7 | -5.58857 | -44.87726 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5e03a4a5-e29e-3975-bdcb-f7fde2110ad6 | -5.58803 | -44.88072 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c88c680-0de1-320c-b852-31e1d88e4cb4 | -5.58748 | -44.88418 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff7f9967-6d46-3f80-8028-ce0c850509dc | -5.58635 | -44.86983 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a870c2c9-8d99-3d5b-90c4-fa8c4b62952d | -5.58581 | -44.87329 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9197405b-c072-3e03-85da-7ad7d1be06cd | -5.58526 | -44.87674 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96e508ff-c10f-3329-a178-678fd27f0db8 | -5.58472 | -44.8802 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f9b5d92-cced-3211-89fb-f5f4ecdf1f9d | -5.58417 | -44.88366 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c7e4963-ce2b-322e-83f5-61bbd74ea46e | -5.58305 | -44.86932 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e90bc8a6-5a92-35b2-8cbd-172bfd7c55a8 | -5.5825 | -44.87276 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0cc4eac7-eb3a-3e56-87a1-31552600bbc0 | -5.58196 | -44.87622 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 00b7aadc-12ea-303e-b529-d53b5e1112b5 | -5.58141 | -44.87968 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e623c7b4-54f5-30dc-8954-597468b35542 | -5.58087 | -44.88313 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e86bd8ea-34a7-3ec5-8ccd-d33860840b2f | -5.57974 | -44.86879 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fdd8ab8-9b7a-3349-b004-87b9ad8a91b0 | -5.5792 | -44.87225 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9023bea9-f734-3932-af2a-01698687b9c2 | -5.57865 | -44.8757 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| abddafe2-d708-3d38-bda2-97fe8952f299 | -5.57811 | -44.87915 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b336321-02c2-3740-9322-b822d01d5341 | -5.57756 | -44.88261 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67ff54dc-5742-3df3-a447-5a9b6578f71b | -5.57589 | -44.87173 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b3b136b-b0e4-3d7e-932b-476968551166 | -5.57535 | -44.87518 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3b23ad7-1858-323d-a012-67857ae3f326 | -5.5748 | -44.87864 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6da96b41-6191-3031-b9d4-8583a6c62be8 | -5.57204 | -44.87466 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bc45734-359c-3f87-9ece-3ce85f1e911d | -5.56271 | -46.36731 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d2020e3-4a9e-39c8-b02c-5bf18684368c | -5.50114 | -46.38025 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 577a6fe8-58b6-35d4-977f-be8fffcbd23e | -5.47706 | -46.37674 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f03c667-42b8-31bf-87b2-c9f9d87f7f06 | -5.43847 | -46.35536 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 845f6b5e-1aad-3fd8-9441-a1019dc95ef6 | -5.43788 | -46.35904 | 2024-10-22 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0644322f-006a-3521-8700-a8a5a5fe58c9 | -5.39517 | -45.98923 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd3869fa-cf82-36d8-bba9-e0f5026eaa58 | -5.33522 | -46.14689 | 2024-10-22 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7f28562-e831-372b-9467-4bd3060cfc1e | -5.3093 | -44.7734 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bfd84c6-1f0c-392c-b93e-4b4722eeb85f | -5.30115 | -44.82518 | 2024-10-22 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a7a6a2b-2e13-3b10-9d6b-7038523592c3 | -5.29566 | -45.44103 | 2024-10-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6db061-0ac9-3733-a187-7adc786df3ba | -5.29233 | -45.44049 | 2024-10-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b200e20-c947-364d-9a53-78ea68575aa7 | -5.29177 | -45.44402 | 2024-10-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c59385a-40c8-322f-9642-44015afcac7d | -5.26893 | -45.52347 | 2024-10-22 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df149f8a-8800-3fba-aa10-f5be8f7bcabf | -5.21433 | -46.02026 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4093bbd0-9f23-325d-9719-3ae9aebfe383 | -5.21106 | -45.05217 | 2024-10-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e099f7ed-69b9-3089-b6f8-7ee995fce33b | -5.14685 | -46.09521 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f2d1171-3a7d-3c42-b2e8-103ba88eff31 | -5.14626 | -46.09887 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eadabaf3-a029-33c1-b8a6-269301ef0d2e | -5.14346 | -46.09466 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 566df673-5252-3462-bb80-9f02b595fdbb | -5.14288 | -46.0983 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7863f856-e89b-34ec-ab47-4517c49827cd | -5.12533 | -44.34529 | 2024-10-22 04:17:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08220c69-ff55-394f-a170-841edb47865b | -5.12257 | -44.34134 | 2024-10-22 04:17:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93aab4b7-fdb8-3984-aa45-5970520af861 | -5.12203 | -44.34478 | 2024-10-22 04:17:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e16ae8d0-27c6-3aa2-83e4-a639495569af | -5.08117 | -46.17523 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab7e1fa-f9c5-36d4-827c-c7ba8ca02b7e | -5.06795 | -45.4409 | 2024-10-22 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1adebed9-e28e-30a1-b127-874340dbcf35 | -5.05967 | -45.21332 | 2024-10-22 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc7686d-1bef-3645-853e-4c5a916e640e | -5.02113 | -44.07869 | 2024-10-22 04:17:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| decefc8f-8281-3e4f-8ad9-26c6cc931060 | -4.98495 | -45.48931 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
