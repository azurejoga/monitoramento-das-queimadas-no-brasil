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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a14fbaf8-c613-3d97-8353-0152c988938b | -4.30044 | -48.06787 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 561b9afc-8c27-327d-a7b5-4ff6230fd34f | -8.19456 | -42.35162 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59a580e6-af26-3a52-89b9-591fcb5178e8 | -5.0741 | -44.00757 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de556115-a1c0-3f0a-84fd-badb70f7fb5a | -6.21926 | -41.54582 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6edf22f4-00bf-3041-ad65-c5745468513b | -9.34897 | -46.91438 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b7cbd8-e32e-36dd-9b44-561f1953911e | -8.09363 | -45.41568 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 793c2494-f65b-374d-a778-c10b2b0fe655 | -5.88006 | -43.90398 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a527e1a7-a8ae-3ae3-82be-a9376495c304 | -10.26564 | -44.04083 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd228f54-3d00-3f14-9aea-0c43fc353fc5 | -7.57871 | -42.68058 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1fc7ac3-666a-39ae-83e7-8883e4bc61a4 | -6.34981 | -44.75203 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 253655ca-ee3f-3c4c-a759-ec79d8a976a5 | -11.47076 | -44.25462 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2772ea60-a77e-391e-9d7d-4d21353087f7 | -5.3597 | -47.30109 | 2025-10-17 04:19:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9884d49a-1cf5-34dd-8a55-791db96754e7 | -7.95244 | -44.1177 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 743846eb-824a-36d3-88c7-b84e11d633e6 | -5.69431 | -42.68297 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 782247d8-c368-3d47-852e-04ef7c0bac9f | -5.1762 | -42.93078 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86b7e805-86d0-36e2-8c17-5c2d916fc7d8 | -9.28707 | -45.38013 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c769d9d4-aa28-327f-84b4-3a256949e5e8 | -10.50731 | -43.43905 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fcb98e49-a579-3b32-ba1a-ba8891d09b12 | -7.47104 | -43.93095 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a171d701-5e4a-393d-99b6-d9e999cb094d | -11.45044 | -44.20641 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a5b672d-db84-3ae0-a3d5-03dd09f775f8 | -4.01445 | -44.19237 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b29e486-12e6-3578-bd7b-74b7f4fa3489 | -6.87673 | -44.69126 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bf207127-8351-33ba-9a23-a1d08010ab25 | -7.12062 | -44.71883 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34c8fe75-72d2-3629-8960-3b3fa215d002 | -4.68776 | -45.40585 | 2025-10-17 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf868740-e237-331a-88e0-c9b078912826 | -7.04923 | -44.26162 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf690556-271e-36b7-bb2d-d8ed785027ff | -10.50094 | -43.41135 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 988db1ee-9b62-3f4e-a876-1d9900089013 | -7.9542 | -44.15034 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8a7b5e0-30cc-39b4-9cc0-073a0bcca002 | -10.28303 | -44.03978 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 416b6ecd-8d7d-325a-a3b8-ed7624fdefab | -9.17027 | -46.73594 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97fa6e6c-5e57-33e6-a085-632265b2612c | -8.07051 | -45.41209 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2322d49f-01a1-3f8e-ac2c-9b867080470a | -5.51726 | -43.30355 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92796157-4e49-34cd-8953-96df8ab60198 | -6.80089 | -46.89064 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f15c01-ec0e-3dc0-9505-7672b8f1dca8 | -2.87383 | -50.72908 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adf4ae6f-ff5e-3d7b-bf69-a2916aed4b47 | -5.87681 | -44.83944 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad96121-00d9-32c5-a281-ac7eb325bfc6 | -10.77623 | -44.57269 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27748a34-139d-3438-8fa0-97163dc39469 | -5.39386 | -45.91153 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95962fa4-8853-32bc-b465-87da7aa22eaa | -9.28377 | -45.37961 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fceadf14-8583-3ce2-b96e-2ab398271867 | -6.09116 | -42.38373 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55765866-b0c5-336b-ad29-b8c73f7031fc | -9.38975 | -46.96225 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32b16916-c9fa-3ff4-a949-8b53306feddb | -6.5301 | -55.04902 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcf7352d-c55b-3b85-8b83-eb1ec96a2920 | -6.20482 | -41.75956 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 624bb1eb-73f6-3396-8300-e6474edcf85c | -9.2554 | -46.59101 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffe0de96-daa2-3f86-b2c5-874509ce249d | -7.79218 | -44.9322 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2285d5f2-8d6d-31fd-ae27-28835a4048a4 | -6.2432 | -41.54783 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4333cc51-92e4-39e4-bd92-d5b641a13c76 | -8.39933 | -46.21513 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5959f2-49e7-30c0-adac-b1eb2cdd8bf2 | -11.40944 | -44.22631 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea55f8a1-1036-38c3-a24c-afbf1ba5c5dc | -7.46597 | -42.6832 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8c029ac-66c2-3caa-b518-bcc6ddc49f30 | -4.92259 | -46.72664 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c37f74e4-8da0-3891-a204-13cdeaccb726 | -8.2362 | -44.78603 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9e8f1ee-ebea-3303-a31f-67263bce6731 | -11.48025 | -44.19223 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eeae5a68-1dae-33c3-bac4-38b5ead8c09b | -7.30623 | -46.23747 | 2025-10-17 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d89925f5-f3bb-37af-b9d7-31a9378603cc | -10.1272 | -44.54764 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aed909a-c6f1-3c4f-a53f-8b60ddd62607 | -7.20085 | -45.48672 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19b7d155-90db-338f-bcde-8cc28c61f025 | -6.58475 | -44.11753 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 557d6306-96f2-3b07-8ebf-10e525bb9bc8 | -2.86851 | -50.73299 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 87568a65-396a-30aa-a6af-7ea5e4c0a625 | -5.90185 | -44.74454 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cfd5adb-076c-31db-bd8c-ae7ff6c40382 | -5.39333 | -43.68586 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3456684-5382-3c7c-992b-af1a7c859bae | -5.88328 | -43.88311 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98ce9aa0-fc49-301c-a426-bd9825aedb27 | -6.28955 | -42.96716 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07be0fc4-73d4-3092-b484-77dbf703af01 | -3.59661 | -48.98423 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d295640a-f40e-368b-bcc1-b84a1b2234cd | -6.84223 | -44.38832 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90778d0f-edfe-3fa4-a287-b662f9ecbec3 | -10.10416 | -44.63069 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ec05d96-e192-3fab-b9f2-b603c0072ab3 | -5.4942 | -42.16003 | 2025-10-17 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 14f0e03f-5628-3289-ae85-072fa3603378 | -7.57593 | -43.82424 | 2025-10-17 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b252438-7f63-3b1b-b44d-40cd69632a18 | -7.28277 | -42.31835 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| df89608c-ece4-38ee-97e4-cd4885bd4a28 | -7.04482 | -46.38 | 2025-10-17 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1d32ee4-be1e-3557-b31d-cf6e60eae4a0 | -5.33411 | -42.9031 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ea96e271-6ed4-330b-b5d5-4aeab0bdc54d | -5.90682 | -44.7559 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a250efb-c283-308b-bdec-4168f7cb6e83 | -9.03764 | -47.66093 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae799477-24f6-3200-bf0f-987cdc8790f6 | -7.62761 | -40.68657 | 2025-10-17 04:19:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 894a7848-4f66-3134-b897-b827b879c1fc | -10.50693 | -45.04036 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 261607d5-776e-3464-9b25-37821404b290 | -10.59986 | -47.39307 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db25d1df-d04e-32c8-8b64-18c24b534be1 | -6.75365 | -42.36452 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef04d7f8-28a4-3dc6-9e46-5a9a138c6af0 | -8.28789 | -43.45997 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21cb27c5-cb35-3969-98d8-452b8bf5c4b3 | -5.15733 | -46.26952 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7e38f04-b2c1-32e3-a6f9-8aed52e02e7c | -7.30679 | -44.44069 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4f1a670-2421-3041-933f-d3b8d331b024 | -7.24008 | -46.45618 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8752845d-2bdf-3767-a656-babde2d1ec70 | -7.74073 | -42.50679 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a67cf102-96fb-36da-8542-2112fd34498e | -11.39986 | -44.22107 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f290a3f-06dc-30d1-b599-d12433629b61 | -7.11079 | -44.73849 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6002ba6-e07d-3c17-a08a-81b8387af342 | -5.70529 | -44.52277 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd9935b5-8455-350d-ab7d-bbb5774cad9d | -10.6473 | -45.25246 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 171252ee-0943-3507-9a18-a993f3567cce | -6.58582 | -43.93615 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f519df0c-db54-303f-bac0-af5abac560a5 | -5.72024 | -43.83656 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bea8ef22-8cfd-3663-8d70-8318657ffd0f | -7.06961 | -44.74264 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb73f2c1-929f-3523-b458-9f12e87fb847 | -11.45946 | -44.21532 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b9f61d-acc9-3e12-a1da-3763264f2f3e | -6.8943 | -44.68694 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0358f6d-a165-3a75-aac4-aa7d636d665e | -9.09052 | -47.78529 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f3d884-ca3c-3628-a97d-7c7f9902abd6 | -9.71063 | -44.55818 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 934a4b48-804a-384e-b6c9-ecb07dc6246d | -6.15322 | -41.78923 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1356f882-4325-35cc-92ee-59c9bffa849c | -5.46346 | -42.94833 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| daec5762-1be0-3c35-8330-c54d798a897a | -4.93872 | -47.07715 | 2025-10-17 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28d8e064-6d5d-3d39-b656-019e23bf4231 | -5.91395 | -44.75349 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ff6cf5b6-00df-39ed-918a-ad5485f4d1ca | -5.18011 | -42.92772 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efa13cfd-eaf7-3632-a81e-84608c3ca943 | -8.84402 | -44.40052 | 2025-10-17 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d2b2183-1e53-37e5-b0c6-7d5d0c918189 | -6.93635 | -45.13522 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adb2b659-a474-3647-b790-407c395108a6 | -10.11849 | -44.60402 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33a663c3-eab1-35fb-9e09-a7df82f6dc64 | -7.47196 | -42.75725 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa2770f4-383d-3111-8e74-825b5c6e2b16 | -5.91503 | -44.74661 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0c6949d-6f1a-3c41-8972-5cb673db8fad | -7.30576 | -41.85155 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 428e95cc-7e51-3d00-9507-e976a5fbf5e0 | -10.65122 | -45.29245 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README65.md)
