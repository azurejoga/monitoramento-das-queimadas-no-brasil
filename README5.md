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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e53d54ea-8fc7-350d-8370-7677df7c5ca4 | -5.88188 | -57.75058 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 6c29268b-c036-32c1-b867-1eef90ef7a1c | -1.51008 | -52.59624 | 2026-08-29 00:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad2d7a17-c997-398c-8e75-7e2233b08da6 | -4.93162 | -55.77309 | 2026-08-29 00:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 34295781-e528-3a71-8aeb-b0a85e76e6d6 | -2.71709 | -47.03331 | 2026-08-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0a48f3ab-5751-37ea-8ea9-2a0452238415 | -4.06085 | -56.30403 | 2026-08-29 00:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0d4c3569-b728-34af-a734-64ee6d78c5b3 | -6.25241 | -55.43183 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8f7259a0-abbd-3c74-883b-12feab59c04a | -2.72101 | -47.06094 | 2026-08-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d6a0ffcc-6708-3ba5-bb18-331b90b76c17 | -2.99717 | -48.95075 | 2026-08-29 00:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f72c743-1214-3d67-bd56-5a6d62d430e8 | -2.03251 | -48.78276 | 2026-08-29 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf504fc4-cc27-3f57-926e-5d2ac456cfaf | -6.26351 | -55.43021 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a2b02868-a15c-3292-b0ad-850f9709cbe9 | -3.43356 | -52.78125 | 2026-08-29 00:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b46b4615-2486-3116-91dc-8f5ceb91d273 | -3.16341 | -54.62036 | 2026-08-29 00:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b8f612b3-bd25-3f8e-bf11-38470a21850f | -3.96512 | -41.521 | 2026-08-29 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| f53e8494-9339-3b80-bd44-8ba1356de624 | -4.28227 | -48.18627 | 2026-08-29 00:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 60245e6b-8d6b-391c-9ed0-403564412921 | -6.72848 | -60.01514 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 8f70df8a-897a-3fc2-892d-dbb7bff8745a | -6.2742 | -53.35009 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6c121185-5405-316c-8662-5153d3fe2978 | -4.1898 | -54.57859 | 2026-08-29 00:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d26251c4-3c25-3e7b-8a1c-00a679d77758 | -2.93348 | -51.47847 | 2026-08-29 00:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a96973e5-86de-3d06-a260-fc55529aabf1 | -3.72278 | -45.25159 | 2026-08-29 00:09:00 | TERRA_M-M | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3df04eb6-1a84-3353-8585-09d441a6af71 | -6.77864 | -55.68444 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ae55d6b4-fb8e-3ff4-8875-3dbf14027654 | -2.50517 | -48.1398 | 2026-08-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 14b8f234-eb58-3e42-86b4-97232e645060 | -6.65538 | -55.44537 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7b0fb3e5-8db7-3f3f-bec5-a8a1e780e0b5 | -6.1655 | -57.7922 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9eb59b5e-447a-3e3c-bbd1-7582d9b58e3d | -4.55275 | -54.91797 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 704d3a39-2763-35c4-8737-bb6d8fce6b3c | -5.88918 | -57.77734 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 92339434-21df-3cba-ab83-f5497c43437b | -6.7746 | -55.65364 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bc5494b6-b532-353c-ba18-13b62151a634 | -5.88462 | -57.77257 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 25094440-f154-3468-946e-2d519cde2fea | -6.76521 | -55.67064 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 208.2 |
| e3b50e1f-fe03-3e1e-b26d-23c6f2ad0272 | -2.71905 | -47.04711 | 2026-08-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b0a862fb-4d1e-37be-9b92-e871db2f1ec8 | -6.76724 | -55.68622 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 102c2e45-52b4-39c0-917c-6de717d9173c | -3.16493 | -54.6319 | 2026-08-29 00:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 56c4f3ad-8fc7-3b74-9b4c-5a5edd08cc1b | -6.53725 | -55.24606 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 2bfba2fa-e515-3c3e-b477-7fac45dda3aa | -6.7538 | -55.67229 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| d755a79f-99c6-3f26-9592-e5ef26a32fef | -6.26164 | -55.41594 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 41934937-adbc-32ea-8aef-e8378eb8d350 | -2.98912 | -48.96242 | 2026-08-29 00:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b5ababc-1e84-3e8c-9b47-6b46e25034cf | -4.97162 | -49.6221 | 2026-08-29 00:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 93a3c2e9-95a1-3875-86d5-af7e44023c4c | -3.43102 | -52.76273 | 2026-08-29 00:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a2c50cb-a3a3-31e7-9539-5e415e1d1485 | -5.43544 | -49.17976 | 2026-08-29 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 36b74e2b-db57-311c-8427-d4d70a86bf71 | -6.77659 | -55.66881 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| e141b0a5-2cfb-398b-ac7f-532648ce087f | -2.02369 | -52.10969 | 2026-08-29 00:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6072bdda-6cea-3357-af2c-182a91c7cf98 | -5.43677 | -49.1893 | 2026-08-29 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70792c25-53e6-39fe-9e24-b1138e47dc7f | -6.76321 | -55.6553 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 724a4643-6ee2-3bf6-8498-3a92ecaf2ce6 | -5.87293 | -57.75737 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 85378dbb-4018-307f-90f9-b08dd52d2e1a | -6.16298 | -57.80845 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5f20bac6-9331-3b7d-9eb0-32ccd5030183 | -2.93468 | -51.48721 | 2026-08-29 00:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3d7ebc48-25e2-340d-ae06-c8d7e5bd0628 | -6.13276 | -53.52165 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 48d70c06-05b5-328f-abb7-88b8f4464caf | -6.37521 | -54.96398 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 41065e01-1f7a-3370-ab17-835508467779 | -6.1699 | -53.47787 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 322cf1a4-1d38-3b20-9fe3-d7566129123b | -6.1342 | -53.5323 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 114f9560-e430-37ad-aaff-e597befb18fb | -2.99861 | -48.96106 | 2026-08-29 00:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| fe305969-4229-3298-944a-3bab527f1fd4 | -5.34727 | -45.16268 | 2026-08-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 01517cfb-7d03-3181-9e3b-aca97fe0da4c | -4.54232 | -54.91903 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3a7cb03a-1a07-3a96-8792-40de9ef5145d | -6.73949 | -55.47372 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 287.9 |
| c3d791ce-651e-3f79-ab37-f78260ccf927 | -6.27561 | -53.36063 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eb64402c-5f3c-3feb-8afc-1d91fe0107c5 | -6.27606 | -53.14894 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fe55f894-df61-3894-b100-61bf4c103230 | -3.4323 | -52.77202 | 2026-08-29 00:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 79212556-0b7c-30f4-b4e0-f66e6b7ab9b7 | -5.99223 | -57.68605 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b6479173-4235-3a9e-872f-0fdce34df520 | -3.75009 | -53.35126 | 2026-08-29 00:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0b088ab2-7214-34c7-8b59-b0b5fd95f822 | -5.16336 | -45.41572 | 2026-08-29 00:09:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 91689ed8-50c1-3683-9593-7479a991cf1f | -3.18384 | -48.01768 | 2026-08-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f4c05394-d36b-3d42-bc2e-3f00edae896b | -3.33433 | -52.52979 | 2026-08-29 00:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e8449085-95f4-3174-ad5d-d53f83723ca2 | -6.72825 | -55.47525 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1b0ec053-4260-371c-8d0a-1e3779518289 | 0.13107 | -60.41325 | 2026-08-29 00:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 1819e9d3-205a-30b0-8e55-f45f226b54cf | 2.40928 | -60.88979 | 2026-08-29 00:09:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5955ec54-68ed-3439-a9ef-ee0b6e52baf5 | 0.14498 | -60.42061 | 2026-08-29 00:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9ebaa01f-9249-3640-9cce-0b0ea8c108b7 | 0.14606 | -60.41534 | 2026-08-29 00:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e7294402-050f-3f45-af40-38ceabf330a9 | 2.23811 | -50.76014 | 2026-08-29 00:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f5d66c8-ac0d-36de-a64c-4f9f7076868c | 0.15002 | -60.38691 | 2026-08-29 00:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 06c64370-5e28-30aa-9721-a5573f3d08f0 | 1.19402 | -51.04105 | 2026-08-29 00:09:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f2404289-6dbf-3705-bf19-b437f7e5e8e1 | 2.2368 | -50.76964 | 2026-08-29 00:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 965e7a41-a20c-34f1-ab49-8adcf0755747 | 2.51974 | -50.85256 | 2026-08-29 00:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 684d1ab6-9055-34cc-8b35-5c6645c4cc14 | 1.19528 | -51.03192 | 2026-08-29 00:09:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1c9c263a-25c3-3c85-abdc-eb71c8f03077 | 0.14915 | -60.39228 | 2026-08-29 00:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e7f7179d-6e6f-3f86-8a1a-1f13c3519dc8 | 2.40798 | -60.89616 | 2026-08-29 00:09:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 01929bce-80d7-3a18-9c45-48a24cab0a45 | 2.24593 | -50.7709 | 2026-08-29 00:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e749a405-9704-3085-b417-9a471633d23f | 2.41217 | -60.86805 | 2026-08-29 00:09:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 29eb9119-c055-3d94-93f0-2ec1487c5dee | -8.5358 | -55.3629 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3d11abe1-78e5-3196-917f-856a23f13893 | -6.6315 | -43.7533 | 2026-08-29 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 000ec03d-5ccc-35a2-8368-a7796e3df8a0 | -14.2027 | -52.8432 | 2026-08-29 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 30dd8fc7-bf17-37a6-aa61-cbb4762ab9f0 | -7.3034 | -49.5414 | 2026-08-29 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7eb37527-4940-31ec-b591-d1ae17f70ea2 | -6.6129 | -43.7317 | 2026-08-29 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a77da5f7-ea7b-3b53-a5f1-bbc9fa1403d6 | -11.0254 | -57.2237 | 2026-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 018c06d2-7c0e-3a05-90c2-f2d0609b863e | -4.282 | -48.2007 | 2026-08-29 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 78e5762a-c09d-31db-89c0-b6284f760054 | -6.1657 | -57.7793 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 583d587c-8894-3091-a41e-fcdfe1841c83 | -6.7528 | -55.4661 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 323c2e10-8a30-3366-b6d7-db7324394efb | -7.2849 | -45.8427 | 2026-08-29 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 646fa024-ffb5-3ace-9711-bfb72ddd23e2 | -6.6505 | -43.7284 | 2026-08-29 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 95b9b543-1396-325b-8f36-697d1924e62e | -5.871 | -57.7715 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 20bd2a07-aba1-30dd-a42e-7f4a66f30f8a | -11.0252 | -57.2436 | 2026-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 0cd7fbfc-c5f2-38e5-9fe3-8f979ecc9d87 | -11.0443 | -57.2222 | 2026-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 44631585-bd22-3d4b-ba15-406b928bb559 | -11.0445 | -57.2023 | 2026-08-29 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 11249338-b60e-3cf0-a8b7-b204da93c437 | -14.9386 | -56.3216 | 2026-08-29 00:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c25912fd-bc7c-3e65-8ce6-82d56869b103 | -20.9406 | -57.5905 | 2026-08-29 00:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 7c44c6a7-267d-3b59-b052-8f2b7a643607 | -5.9079 | -57.7506 | 2026-08-29 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6b74a4d0-eeff-3c2d-b644-12d8d92405c0 | -3.8749 | -48.0458 | 2026-08-29 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3fa2dffc-eede-3247-b96f-da88f79eba38 | -6.77 | -55.6445 | 2026-08-29 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2f30bc66-6bb1-3f97-8cab-b0c4404720b5 | -6.6127 | -43.7549 | 2026-08-29 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 432249ba-0365-32bf-b75d-242d2335a840 | -6.6317 | -43.73 | 2026-08-29 00:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 5267577c-c30c-3818-9fdd-fa6b498d20f2 | -10.8996 | -46.6216 | 2026-08-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a62abf48-7070-304d-8ca6-160164647ec7 | -7.2847 | -45.8652 | 2026-08-29 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |


[Clique aqui para ver as próximas entradas](README6.md)
