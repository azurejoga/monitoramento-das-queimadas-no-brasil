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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef243105-4f1c-3b63-85c7-0abd2c775ae4 | -11.08796 | -47.41388 | 2026-09-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 659864d8-2ce5-3061-b4e7-e2230ba303e5 | -12.595 | -44.15833 | 2026-09-17 04:40:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ff3c61d-94c2-3fc3-aadd-446b34c2e2fa | -8.84575 | -46.92054 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd28729b-ad7d-378b-b5ec-376b6ef5a61f | -6.83687 | -55.76331 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb6ed119-7495-322a-9cf5-ae654d6c4363 | -10.78824 | -46.18876 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a8b28ca-5625-3afd-9bcb-3f39ef2fd0f0 | -4.56906 | -54.90954 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36fc9115-5fc5-3ae8-850e-fffdb3fe0550 | -10.83494 | -46.17785 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0e41af9b-6169-3487-a6cf-7b667085ec94 | -4.4789 | -55.09009 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d89e1c2f-566f-368a-9d77-29910c0fb4b1 | -6.78857 | -48.65769 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58c4473-a509-300b-86e5-24ab8170a41b | -8.32923 | -51.31181 | 2026-09-17 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe4c4e17-e565-3fa2-bb80-6f1b8d34d560 | -6.36848 | -58.28513 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23f78e71-7076-38ee-b515-f03a8ed62500 | -11.22853 | -43.45496 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6947683-8fc8-367b-9d1c-807f2cb83170 | -10.86309 | -54.0388 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49b7c665-8d06-34ab-b43a-b2311c4afb13 | -7.09353 | -41.83876 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 216b0b69-a03d-3fa2-85a7-e065dc3e423f | -12.31686 | -47.96271 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3cfd8d-d1ee-349b-890e-348df3dcf94f | -9.10372 | -45.72256 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b585d370-2fad-37e8-af7d-ce5019fad636 | -8.49439 | -57.65342 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c4a3b7f-9669-3b11-9e9c-27e32892db74 | -10.39507 | -46.62971 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a02e4418-8aab-36fc-a094-e427447f6e4c | -7.58397 | -44.9267 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f587af4-3e89-39f2-9892-5e5f55c05caf | -8.99288 | -50.16485 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6c3b99f-d7c7-35d1-9f86-88baf69f309d | -10.81337 | -50.83547 | 2026-09-17 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2fbb22a-3a82-3101-ad5f-5598560602ba | -8.02095 | -45.47662 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76d9d718-ac2b-3008-956d-9a64cbbb5d52 | -9.75824 | -46.57456 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f087c2e-d983-3308-961f-5a9064255d11 | -5.97616 | -46.6408 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe7c8be-1c73-3997-939e-4d2a2f9cc4d6 | -9.03667 | -47.75809 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bc1a099-fd48-3bf7-a0ca-850a2a0f6577 | -10.10028 | -45.62366 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47861a2c-be34-35fd-88b9-889bc8a65f91 | -8.42987 | -47.75635 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 168c9158-6b9c-3b53-9286-af036b6ddeef | -7.1141 | -42.08514 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c24acc67-0d37-319b-8e56-f91407356725 | -7.12628 | -42.17263 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fe115eac-7367-31c3-a668-dc9bbf47a1c7 | -9.04577 | -45.09165 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86a1e10e-ea86-3108-a7c0-4fbd30b3e81a | -7.18987 | -41.80842 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8e95c281-4c11-310e-9235-42ab5526c301 | -7.3122 | -38.66188 | 2026-09-17 04:40:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c2629327-879e-3196-9ad6-a04188fc2aa9 | -8.48293 | -57.63493 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 7c98c95d-43d3-32d5-8397-b324c7b8bae6 | -11.55838 | -46.88697 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3bb61d7-f876-3aac-a1b0-208533a6f169 | -10.39636 | -46.6282 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35c244ef-2f5d-37b6-8e15-92ef44cd9aef | -4.43278 | -55.78596 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd37ce1-11ce-330a-9e0c-bc57893d978c | -7.09293 | -43.47038 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b09b0daf-95e7-3a88-9d13-de66872aba45 | -4.51578 | -54.96953 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f1f1d56-0da1-3258-9a8b-b35817362053 | -10.11261 | -45.56629 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1d51037-18d5-3d8e-9c3f-a172e855a9ef | -5.76557 | -45.10259 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 49445655-2fbf-3637-8c54-a12f8403b247 | -5.15644 | -55.94295 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac0dd9e6-a041-3e1b-9c60-48acd7409def | -7.45033 | -45.28978 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bed4e20-951a-3b69-b863-f9d15523706b | -10.01642 | -45.49768 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c63baa3-4e00-3ca8-8e5c-a01cd2090e85 | -9.85179 | -46.91563 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a6b2ff9-9379-3845-a96a-dfdf1166eef4 | -7.64804 | -44.33974 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af98b03d-960e-30c1-9c2b-3649aad8aa60 | -5.22868 | -49.3102 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f205ea8c-498b-3fba-84ea-555b21b1260b | -7.02336 | -50.7066 | 2026-09-17 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 606ee7e1-352a-3bbd-af1e-2874114135d9 | -10.63565 | -48.70535 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9fd4323-dbc6-3b45-ba8b-31e0c560e104 | -7.96779 | -44.83705 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4d734bd-a230-3cca-b7bb-421f76724c0c | -8.19684 | -43.67354 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22287b2b-0198-38bb-b112-4f4baf44c579 | -7.64494 | -44.33164 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3a30786c-cb14-3f35-b007-71f725f81256 | -7.38074 | -44.52066 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87a482ef-c967-3d42-96aa-13d7ff1dd5ae | -8.48963 | -57.65264 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ae63f29-f70a-332e-bbce-260906839288 | -8.46796 | -44.56282 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2722ce2-9659-361c-85a0-5ce9f281c2a8 | -11.5809 | -46.88999 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4575f6a-76d0-3b34-b209-f8dd8702cfc4 | -6.10165 | -57.62757 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fab40246-92e5-3c48-8df3-7121c7637f23 | -10.38883 | -58.3132 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f61ee25-ca96-331f-bf7e-8552a547521e | -8.49712 | -57.63768 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4234823-f8c0-3ea4-b591-527d18de183d | -9.96142 | -45.32082 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12a542d9-fc1d-3058-84a8-02d9c86daea1 | -7.72112 | -42.49863 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5e533258-3b9b-3b28-a97b-1bc0d9829398 | -8.56167 | -44.51234 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| def440ab-83cb-312a-b87f-5845b7c5d0b8 | -10.52082 | -57.45447 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01a7d494-3529-35f6-9190-29dfadaac242 | -10.05257 | -48.94955 | 2026-09-17 04:40:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7520f5a6-f1a0-360f-a304-36dccd79ba5a | -9.88363 | -48.3905 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bffc2829-398a-3f2e-bb1f-90ef2a1920b3 | -6.79082 | -48.66526 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25a8acff-ae02-325b-a1ec-a78b41d0df5b | -6.76321 | -42.77864 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d73d4d7d-1fcb-3ae1-8b6e-2abee055f8a5 | -9.15906 | -49.99521 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84761e97-9ab6-3709-8afc-cb465205770e | -9.49674 | -45.43687 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b5ccde1-08e0-3e06-a7d3-ff403358c86b | -6.82938 | -58.98299 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdc56576-74d5-3406-9a9d-b93164697ea1 | -11.64968 | -47.32693 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a652443b-7feb-3264-a8af-db331ab58cec | -11.18491 | -48.01575 | 2026-09-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89c105e3-3998-3c11-b6f0-0a9b18c52eed | -8.43045 | -47.75248 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04438c2b-dd1a-3cfd-a048-b0cdb5eedeb9 | -11.04877 | -48.27868 | 2026-09-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ee13b56-3971-310d-9992-09ecd4c31205 | -9.48094 | -47.22905 | 2026-09-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06441ee1-b872-3bc4-b00e-d48ba1c3d8aa | -4.53243 | -54.91967 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ab818c-a704-357c-9556-ac1fe2beb232 | -10.78056 | -46.19999 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 526771a0-ca45-36f2-81a4-e723d563811a | -6.90598 | -59.03568 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a73fbfb-568e-3b1a-a9cf-bed620655cd5 | -7.30614 | -42.35365 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 56cf9d8e-b233-300c-94fc-4aecf3a550d9 | -7.65456 | -45.84116 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 705879ee-2025-3a88-8729-6b2068e5c8ce | -11.56844 | -46.86972 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 831cddc9-55b5-3a7c-83e7-254d3b5f0e3f | -8.579 | -44.5708 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af6c971c-2cef-37af-a34e-d403804f8617 | -5.76418 | -45.11214 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2d23ccf6-fffc-32d2-a7f7-0167f4201743 | -9.12808 | -48.82336 | 2026-09-17 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baeddbd0-5e08-3e02-a51a-5499ee372cf6 | -9.49583 | -56.75321 | 2026-09-17 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa087629-1d32-39b6-88fe-916efaa036ac | -10.46208 | -44.94334 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 947d651d-e1d5-3698-9cd6-1537f0276e5f | -5.79829 | -47.24316 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ed5f63e-ce16-3aaa-8a49-276b780cc9d8 | -9.7564 | -46.57609 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebf3588d-bb53-3812-ae61-cc04f53c131c | -5.90674 | -52.09407 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7a30b2-f828-3108-b234-ce5f4c13e2de | -11.0453 | -48.27812 | 2026-09-17 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29de49c5-4fce-333d-8d25-23cc268f57dd | -9.61574 | -45.35848 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 945fa50c-590e-3b81-b009-b1d834a2f015 | -7.08715 | -47.48307 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7012f188-7498-3e8c-9658-64fabf6603d7 | -7.58575 | -46.33222 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02d88325-0da9-3f45-b3cf-04847cfd7d87 | -9.75384 | -46.11514 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dbabfbc-2317-3297-8163-b1644d5b51f9 | -7.64548 | -44.32788 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 832fb385-7093-3c6c-b308-5e9870365fb0 | -9.90181 | -46.51456 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa664756-fae4-3203-93d1-989dcbeff0c5 | -6.90538 | -59.03908 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b665ba10-877c-3893-b573-a33b71ab1a0b | -10.54794 | -44.85494 | 2026-09-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b34d68f4-a3d6-37cb-becf-6eee4c12986f | -9.12011 | -45.72652 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7308d340-20e6-3dbd-898f-07ec0430ec74 | -10.99006 | -48.3026 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa2603bf-beea-3014-9673-58fb273afd59 | -6.27404 | -50.94415 | 2026-09-17 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README46.md)
