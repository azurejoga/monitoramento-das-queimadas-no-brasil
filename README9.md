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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc854e05-0a9d-37c4-9d27-c633c4d5041f | -11.66234 | -39.01759 | 2026-06-17 04:00:00 | NPP-375D | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 06f1ce4a-e4a3-3892-90d8-3d067ae901ba | -9.2594 | -48.54079 | 2026-06-17 04:00:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cad47a97-9806-376e-aacf-840b6fe16dde | -10.93373 | -44.67406 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| debb7b0e-c4fe-314b-8ab2-752eae793a4f | -12.1924 | -52.79175 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ab320b92-4d17-3c72-b3ab-e5ef073f3e77 | -9.34033 | -45.47366 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d3dbd09-7171-36cb-9858-e93e6cd288b7 | -13.28378 | -46.06072 | 2026-06-17 04:00:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fa8669a7-dd5f-3b44-bbf4-c6c6d7cd47ef | -10.55312 | -46.22268 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b397fd73-c857-3bc4-8fec-ca70393eaa8c | -15.5161 | -40.79347 | 2026-06-17 04:00:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 931915a7-1dc0-3f75-8591-65452a75ca2d | -17.59328 | -44.59857 | 2026-06-17 04:02:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86c1699a-2f88-329d-a072-310a84fe2c58 | -17.59852 | -44.60151 | 2026-06-17 04:02:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 860d6d4e-45ce-3c4d-b9da-f4b37f430021 | -16.44246 | -46.35836 | 2026-06-17 04:02:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8731be-d0eb-34ce-a984-9e90e480d8d9 | -17.59458 | -44.60054 | 2026-06-17 04:02:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c590184f-1d67-3acd-83e8-516dbff82db0 | -15.58944 | -41.7983 | 2026-06-17 04:02:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a4e98dd3-20f0-3f40-b463-ed30a7326e60 | -15.59296 | -41.79899 | 2026-06-17 04:02:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8085c5db-0d40-39b9-b5a1-4c7e5a00de70 | -19.30159 | -40.37737 | 2026-06-17 04:02:00 | NPP-375D | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b94eec85-4bf1-397f-8ddb-361a88d12adb | -16.44698 | -46.35931 | 2026-06-17 04:02:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 795bb953-bca2-3de0-844a-97040c52a54f | -20.07961 | -40.88171 | 2026-06-17 04:02:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 14f862a6-9982-31ac-b743-bc4552358d44 | -18.82953 | -40.12938 | 2026-06-17 04:02:00 | NPP-375D | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cb5e9114-e4a1-35bf-b919-1d5c86e1e9ec | -12.8354 | -44.3657 | 2026-06-17 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b0536edd-d82f-3ae0-acbe-d6c457a814b6 | -9.3234 | -45.4787 | 2026-06-17 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a49e8cee-978f-3db2-a8b7-e9a99c8623c1 | -12.8548 | -44.3625 | 2026-06-17 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| fa2baf75-51a2-30a1-8396-2823b3e8cb9f | -8.9824 | -46.9766 | 2026-06-17 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| c5ecf86f-706c-3fc7-a8a4-b143a30383a9 | -9.3423 | -45.4765 | 2026-06-17 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 39a9ecfe-e426-3cd5-9ec8-53547ba95422 | -9.3423 | -45.4765 | 2026-06-17 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 78134697-a73c-3b9f-b00a-560719afee35 | -9.3234 | -45.4787 | 2026-06-17 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 740bf8cc-56e7-318e-a71c-c42a455cbe5d | -9.0013 | -46.9746 | 2026-06-17 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| cbe5865e-4bae-3eb9-9b0e-f8899ae6be5e | -12.8354 | -44.3657 | 2026-06-17 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5439709e-0abc-3cd9-ac03-d87a6f4a5028 | -8.9824 | -46.9766 | 2026-06-17 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ea20e5cf-9662-32ac-ac79-aab8c496db71 | -12.8548 | -44.3625 | 2026-06-17 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 74c902d5-dec6-33d8-b719-46e284c77e07 | -12.8548 | -44.3625 | 2026-06-17 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 47a0c7aa-1c76-3e64-89d3-fd7260550213 | -12.8354 | -44.3657 | 2026-06-17 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 9762f75d-8161-339f-8973-f859cd665bb7 | -8.9824 | -46.9766 | 2026-06-17 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e6d97831-09dc-37f0-9eb5-b44f1fe9e300 | -9.3423 | -45.4765 | 2026-06-17 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 9ed7cf6f-210e-3f53-b205-91b25dc92195 | -9.3234 | -45.4787 | 2026-06-17 04:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 172926bc-2729-319d-8240-470be9b2b608 | -12.8548 | -44.3625 | 2026-06-17 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 144c655c-ed51-3c7f-a4a6-7eda813e04cf | -9.3234 | -45.4787 | 2026-06-17 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4b2ef8ba-a9a5-33c9-a1d7-d5d1f36f21c3 | -12.8354 | -44.3657 | 2026-06-17 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f228a83f-9613-3b2b-b9a3-baaa9c9ebfc1 | -8.9821 | -46.9988 | 2026-06-17 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 437ba412-3b11-3777-b241-ebbbb4957edc | -9.3423 | -45.4765 | 2026-06-17 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4372a8c8-6024-3410-958c-dbfdd7c56ccc | -9.3234 | -45.4787 | 2026-06-17 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9959943f-ea9b-38d7-a489-f74b4894d85e | -12.8354 | -44.3657 | 2026-06-17 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d67bee81-86d6-31ac-9f68-337e94dc3516 | -12.8548 | -44.3625 | 2026-06-17 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6189d090-5972-3ecc-b4ea-6f0be61f1e76 | -9.3423 | -45.4765 | 2026-06-17 04:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 598df409-c0b1-33ff-b4fe-f338cef026f4 | -12.8354 | -44.3657 | 2026-06-17 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6fe6e806-96f4-3776-bbd3-d0831806fce2 | -9.3234 | -45.4787 | 2026-06-17 05:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 44a438a3-d019-3172-9f58-9c85ee2617ed | -9.3423 | -45.4765 | 2026-06-17 05:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c036d881-8022-361c-ac3a-3828017dae8c | -12.8548 | -44.3625 | 2026-06-17 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 01c8c02d-61ce-3840-932e-1d2618babf93 | -0.09014 | -51.28178 | 2026-06-17 05:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5aaec47-150d-396d-a6c5-771f1166a458 | -8.28026 | -48.22007 | 2026-06-17 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79aac0ed-d21b-382c-baf0-3be29a88debe | -9.30864 | -45.47323 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f45f8877-30a7-3df8-8f84-acf1d14abde3 | -8.98977 | -46.97826 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 814bb64d-f1f1-3a8f-897d-884dabf5e2e6 | -3.50848 | -48.03923 | 2026-06-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f07c08c4-7888-3113-980d-8a6b0a588186 | -8.67916 | -47.84638 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e59935c-2b7b-3ed7-a250-d0c83aae542f | -3.51374 | -48.03534 | 2026-06-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 59f89a96-2323-3623-a284-98c6ec3c56aa | -8.98844 | -46.98829 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1e0ae2ce-c8d3-385a-9b0f-33e5ab174ac2 | -7.84006 | -55.39173 | 2026-06-17 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d641632f-c314-34c9-ac24-05cb0e49094e | -7.58719 | -46.35619 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17459afd-a07a-340e-a3d7-7e7d96283b69 | -7.58639 | -46.35432 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6be11e00-3036-35cb-abcd-e059df1d8e02 | -8.96476 | -46.96093 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1120223-96eb-3c84-8a3b-e3ee2ed4fb29 | -8.96387 | -46.96772 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b77c35fb-962b-3f4d-88bf-d8271b6cef34 | -6.30647 | -48.44167 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f88280f8-dc36-33b4-a6b8-f39ef04ae3e6 | -7.72256 | -44.1666 | 2026-06-17 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34860213-50da-3d29-81d3-04b64b8cc431 | -6.14596 | -48.51229 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e166d71e-627a-3443-8d8a-66eb41afbeb6 | -8.73256 | -47.98112 | 2026-06-17 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 618a6c2c-af3e-3547-a93c-fd7885d52f4d | -8.68402 | -47.84678 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c4dd51f-024f-3c2f-a66f-a28eedb287d9 | -8.68364 | -47.8497 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cfbaa66-2a5a-3bf2-8cf8-a9a86002aa91 | -8.45834 | -46.40261 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a19df48d-fe0f-346a-8dee-823a605a74f7 | -7.83542 | -48.39587 | 2026-06-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16becd14-779a-30ce-adb9-e9368df45000 | -8.6846 | -47.84409 | 2026-06-17 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 612d6e2a-983b-35bb-b0a8-4012d0bdf0ef | -8.96879 | -46.97184 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ea05a3a-cd1c-32db-a724-2be6fc3209c3 | -9.21292 | -47.90757 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb66d942-7e49-38be-925f-84a9f7b515a9 | -8.9871 | -46.99839 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 76c5caf8-9624-3c82-9459-bfa4bc7765b3 | -8.96926 | -47.00969 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83000544-b743-3865-bc70-a6166339eabe | -7.71626 | -44.16563 | 2026-06-17 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c923f75-657e-3ff8-9344-f84e1ca97b38 | -3.19081 | -52.00255 | 2026-06-17 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5671626-2488-36b1-bc4f-556a53ab5f37 | -8.9474 | -46.96851 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3624110e-da6e-3942-978b-9a4f99be599e | -9.29994 | -45.46657 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f36c8159-0964-3598-9b95-9918b8972840 | -6.17107 | -48.50173 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2ebe314-9be3-3382-b714-2aeec96c1b86 | -8.97237 | -46.98606 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 068383c8-0a13-39f4-bfcb-dfaa3377e3c3 | -8.98888 | -46.98495 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 85f0e82e-0984-33de-aa88-b1f63e00addd | -6.17042 | -48.50628 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca363e08-41f6-37a9-a6c2-f74c02c5fa89 | -7.58591 | -46.35778 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af5999b-2d1f-3c49-8cfb-295b2bd7a3cb | -4.356 | -47.76576 | 2026-06-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c006b68a-985d-3195-a520-c34215232f94 | -5.80088 | -45.09293 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa177b4e-1cb4-38c2-9b7d-201971fea366 | -4.35675 | -47.76065 | 2026-06-17 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 766e4f7a-9cb4-32da-a3e0-1a5e3cf4c274 | -8.97193 | -46.98941 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88e45ead-9be8-3d1e-8882-22a5451714a1 | -8.94696 | -46.97187 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0295f4d6-ca4b-36b4-8fb9-b95cb9268b9c | -5.79671 | -45.08022 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f3bc2cde-0403-3000-b00d-4ebdb809b5ec | -6.15058 | -48.51294 | 2026-06-17 05:04:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1791fee2-7b3d-36a5-bcea-99903c50bf41 | -8.88825 | -46.97866 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b266ee2-f040-321d-b4ac-1f1b779402ba | -9.34432 | -45.4779 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 37349cff-ffdf-3c02-8edf-a3d67686976a | -9.21214 | -47.91331 | 2026-06-17 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35780395-1f8d-3272-a584-0d8f07e6caf5 | -8.2416 | -47.12634 | 2026-06-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffa36a99-ca81-3544-a92b-a26e7171e2f7 | -5.9842 | -47.07132 | 2026-06-17 05:04:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c48722d-4346-3055-831a-c466c7c3cdc3 | -8.88425 | -46.96777 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9629f4c-2d30-32bd-b912-f00b9fdbf484 | -9.30589 | -45.46727 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b976b5d-eaa8-3628-98b2-64d8a23b015c | -5.7956 | -45.08825 | 2026-06-17 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 137c0b0e-b0d9-33ed-82c9-0325199cd6a7 | -8.98398 | -46.98078 | 2026-06-17 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d38a756e-553d-3501-8fd8-b63e67aeeaaf | -6.6297 | -44.58167 | 2026-06-17 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc62f2b8-9a8c-31d8-96fc-9e81107f73be | -9.30918 | -45.4688 | 2026-06-17 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README10.md)
