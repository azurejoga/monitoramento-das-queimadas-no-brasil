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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e17673-51be-35e0-8ba4-94686830263b | -21.00602 | -50.03495 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48825a0f-4110-3aad-8a75-a5bc309c0278 | -20.99627 | -50.00394 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0f310644-abf7-32a4-8904-d47a676de699 | -20.98559 | -50.4752 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d33be5ca-e0d6-3383-a980-add220cd917d | -21.00257 | -50.03056 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 33cfc545-9962-3bfd-a58b-638c79d5a17d | -20.98622 | -50.02122 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 1259c310-469f-3f83-a21c-94275bce34d6 | -21.00707 | -50.03042 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4fd310c4-7fac-3827-ac74-fd9c752e5886 | -20.66116 | -48.8255 | 2025-09-25 03:47:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 743d2e7a-0f53-3e19-82d0-d6323e871f6a | -20.991 | -50.02728 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e2b9ac21-33fd-39da-8323-463c0489891c | -21.97868 | -49.51155 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e57a054f-c3c3-39b8-b435-8c24028827db | -20.66197 | -48.82179 | 2025-09-25 03:47:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4b36f251-e350-3a4c-a5dc-eb3a119d1711 | -20.99992 | -50.01498 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 53b121dd-2d5b-359f-9a4d-fa6508f7423d | -21.96578 | -49.5169 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c56def71-f890-34a8-bb6f-3b61adb7b488 | -20.98415 | -50.0304 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 71bfde5e-cd6a-30b1-82bd-44ffc966e3bb | -21.96757 | -49.50889 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 077c4978-7e13-32b2-8d08-6c409f42e0e9 | -20.9898 | -50.46306 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbcdb32e-ab04-31ad-9d92-11b94131877b | -20.98277 | -50.02896 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 0ab65f3e-50f4-30b6-be20-9b1ec45a2b36 | -20.98862 | -50.0303 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 79882cd7-75e4-3221-bf02-d6f78fb3ddfc | -20.9976 | -50.01818 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 82f859a9-aba9-3279-ad63-e61d2a24adc7 | -20.99291 | -50.01187 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9a76d572-5179-3e38-bf5c-8a30a067373a | -20.98169 | -50.0336 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ca0878d5-44cf-36c4-887b-4a5f4afa6fcc | -20.9887 | -50.46772 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b3302e3-7ac5-3e40-93a2-eef2bd955ee9 | -22.04867 | -48.62394 | 2025-09-25 03:47:00 | NOAA-20 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5b350b4e-8ae2-3022-9473-74c948bd4e04 | -20.99871 | -50.01342 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| cd8b9218-96c7-311a-beb1-a8b699abac23 | -21.9796 | -49.50743 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 24aff580-cd48-3065-96a6-ed98cba73ea7 | -21.00099 | -50.01026 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| de6efded-0784-3949-80d2-6ebe069881ec | -20.98519 | -50.02579 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 6c64f70b-c917-369a-8d75-f53c102e9242 | -20.66658 | -48.82699 | 2025-09-25 03:47:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 11bc341b-9863-38dc-9d11-80000d1a53fe | -20.99039 | -50.48183 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 56b9b1b1-c3ae-35f4-a564-6c5f0dd5f7c8 | -20.99182 | -50.01658 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2f2357f2-ad37-39e9-a873-d9632a2268d9 | -20.99979 | -50.00875 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d45fc129-206e-356b-b763-1827a6bea46f | -20.98968 | -50.02575 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| fe7cb010-b64b-3529-8751-8026842c8e1d | -20.99415 | -50.01331 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| bc3d3f83-2219-3fea-9128-47e4ae5b3935 | -20.98727 | -50.01659 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 62d295b0-5841-3e5e-8135-a9cf3539c2ce | -22.04941 | -48.62052 | 2025-09-25 03:47:00 | NOAA-20 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 43e530ee-093e-3fae-8f58-0eff1a6505a1 | -20.9915 | -50.47694 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccfe21d6-29f8-3720-8b57-bd154bd9e818 | -20.98641 | -50.4774 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4a004475-cdd2-3d9d-a0e1-0d54cf407d2b | -20.99522 | -50.00857 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 9a0179e8-b0e1-3415-91ed-308f36812e2e | -20.98996 | -50.03188 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 584e9a90-9086-32cb-a697-94ff050f8a9c | -20.9849 | -50.01982 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 07e14683-2de2-390a-a6f4-a4b45bdc3d2a | -20.99073 | -50.02123 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 8e36fa8c-f689-3649-a268-7f10a7dd13c4 | -21.97221 | -49.51432 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 23cf9f2f-e048-39ad-a14b-949339074d1b | -21.97132 | -49.5183 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1df5d350-edbe-35cb-b5da-e9ffa3267501 | -21.97544 | -49.51721 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| b132fcad-3f56-36e8-98c2-e40658ca79de | -21.98051 | -49.50332 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 325963a9-f23f-3b8f-955a-258fa9c4e656 | -20.99042 | -50.00265 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c8c98572-d634-33c2-bd88-9f1b9b9a8c44 | -20.98446 | -50.48011 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2ed5aba0-fcd7-384f-b062-09c4691485b9 | -20.97149 | -50.03194 | 2025-09-25 03:47:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 95e6bbd2-54fd-334a-9781-0d4fa17f0f03 | -21.83155 | -50.58607 | 2025-09-25 03:47:00 | NOAA-20 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 79cef06e-8fe0-3999-ad76-b0bcfc021327 | -18.87554 | -51.52262 | 2025-09-25 03:47:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 07875c5f-8a1e-3181-bcdb-d23a8fe4d7e5 | -21.00154 | -50.03511 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8ee44b9-363c-3561-abea-1c14f221061f | -20.97726 | -50.03361 | 2025-09-25 03:47:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 06ae70ee-7081-3b49-9624-6b8f5c909219 | -21.97776 | -49.51569 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 5fef353b-ce58-3016-b147-dad9375f8451 | -21.98287 | -49.51041 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 02056c7b-3e23-357d-b48d-26b9998f4218 | -21.9929 | -49.5054 | 2025-09-25 03:50:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| ef43f69b-1bac-3639-823f-f7fdf5e00cbb | -17.9312 | -55.8548 | 2025-09-25 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.8 |
| f440fcea-f611-307d-8ba3-4cb75f979d94 | -20.9931 | -50.0032 | 2025-09-25 03:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.6 |
| bbcd9a9e-ad07-398a-b573-562c69f2ec9b | -16.8538 | -50.5026 | 2025-09-25 03:50:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b435265d-7f32-30f9-8d62-2ab800c7cb08 | -17.9308 | -55.8758 | 2025-09-25 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.9 |
| bbd3a59c-485b-317f-8a74-37366547f4d0 | -20.9925 | -50.0261 | 2025-09-25 03:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| f5635b58-3f33-3d39-bfab-003b4087d22d | -21.9721 | -49.5102 | 2025-09-25 03:50:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| d86f5d19-9910-3fd7-8304-8d5af77bf203 | -17.9308 | -55.8758 | 2025-09-25 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 96b306f5-9b27-3fa6-b2e1-1622c7fd6091 | -21.9929 | -49.5054 | 2025-09-25 04:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| d9dadf82-0a60-3a3f-aff4-8b174ed09105 | -16.8538 | -50.5026 | 2025-09-25 04:00:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 76ac84cc-ccce-3c3b-a32a-756c2e4b5061 | -17.9312 | -55.8548 | 2025-09-25 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.8 |
| ad34440b-23e2-34ee-9a7a-a0c08a5a323b | -21.9721 | -49.5102 | 2025-09-25 04:00:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| c19d44ab-b694-3bdc-85bc-4480d17b9432 | -20.9925 | -50.0261 | 2025-09-25 04:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 0fa9f9fb-f9f0-3967-a03c-d6d9a2a587a4 | -20.9931 | -50.0032 | 2025-09-25 04:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| d9e9028f-bc0f-3c3c-819c-5e6fe2538933 | -17.9312 | -55.8548 | 2025-09-25 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.3 |
| 76e7156d-5aa6-3c0e-b3e8-5ac7a79e7702 | -20.9726 | -50.0077 | 2025-09-25 04:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 2e4639bb-9d0f-32a4-ad5a-4d6f44ae920e | -20.9931 | -50.0032 | 2025-09-25 04:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.9 |
| bb9f5ae0-6749-3494-939e-57a6e4b40823 | -21.9929 | -49.5054 | 2025-09-25 04:10:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| c1a9798f-8cba-39d4-882e-3df0ac5f4485 | -20.972 | -50.0305 | 2025-09-25 04:10:00 | GOES-19 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| 9bb65f5e-2ecc-323e-b4a5-49b09d83f2ed | -20.9925 | -50.0261 | 2025-09-25 04:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.1 |
| f8dadec5-e157-39e0-85cd-beb0275f4c56 | -17.9308 | -55.8758 | 2025-09-25 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| feb49ff7-0c54-3d03-99eb-4ba54901e544 | -21.9721 | -49.5102 | 2025-09-25 04:10:00 | GOES-19 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| d9bd7bac-c1aa-3fd2-88e3-17d000d9ddde | -17.9312 | -55.8548 | 2025-09-25 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.8 |
| 0de4eaf6-1023-369e-aeab-53b6899403b1 | -15.7642 | -59.4872 | 2025-09-25 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 680c9dad-0279-378f-a339-90538f36c556 | -17.9308 | -55.8758 | 2025-09-25 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.1 |
| 0c4009e5-0497-3dbd-9de8-72acf4007030 | -15.7644 | -59.4672 | 2025-09-25 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1578f9ce-4ecf-3631-8605-215123e21b7e | -15.7642 | -59.4872 | 2025-09-25 04:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3b1ea6ad-10b8-38fe-96a8-d270c9c0f166 | -15.7644 | -59.4672 | 2025-09-25 04:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 00611b4d-9039-3975-a8b1-f92225668fc5 | -4.02958 | -47.77092 | 2025-09-25 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54c9b5ee-a176-3b25-84d5-3e63de748c0e | -3.78932 | -41.72839 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9bc4f46d-9d9d-31d5-83c2-dcd9431dcfc9 | -3.82246 | -50.97608 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f67d97e-b3da-3c9f-bd70-f67737ab430b | -5.93575 | -42.92862 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10826d96-0b4b-36d3-a9c6-75500cb149a3 | -6.97148 | -42.30449 | 2025-09-25 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a21680dc-1416-385b-8eb2-020c8f95cb26 | -5.24821 | -43.07972 | 2025-09-25 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da4a246-2e56-3f59-9386-2598b893e45b | -2.92125 | -48.30413 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 33b8508b-8db7-38d6-ab3f-cc2154e7a570 | -4.18267 | -42.95814 | 2025-09-25 04:32:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 523c1e07-4a6a-337a-b158-0f4b0cc25f89 | -4.29265 | -48.26196 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ef09067-6b35-37fe-ac1a-c6dfee4f200f | -3.79178 | -41.7405 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62d849ea-624e-390e-89ef-1690ab023280 | -6.28147 | -39.69021 | 2025-09-25 04:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a1a17e3-58dd-3ad4-a45f-ff75232e67cf | -5.59075 | -48.66409 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1313f641-89a8-365f-966d-db533e0c4bbf | -3.81082 | -41.55647 | 2025-09-25 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c4f28a0-cd3d-3d5e-a32d-21da841221a5 | -3.82615 | -50.97665 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5216ce86-43c1-301b-803b-2b3669dcf1ce | -0.9102 | -47.5422 | 2025-09-25 04:32:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79d2a7c3-239a-3385-8f9f-d045ffc170e3 | -5.83168 | -46.35849 | 2025-09-25 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8503f203-dbee-3a8f-868d-124e5f23d7a0 | -3.83565 | -50.96471 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32986ab5-b354-3295-aabc-bbcf77f4c71c | -6.72442 | -42.73753 | 2025-09-25 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1d3a248e-3b65-3f3f-a6c2-a6419d8a055e | -5.09392 | -47.47088 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
