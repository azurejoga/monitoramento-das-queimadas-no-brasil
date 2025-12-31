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
| 7d1c4a3b-2477-3062-8073-06e9dbcb8e78 | -1.0809 | -47.9916 | 2025-12-31 00:00:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e3ac83f8-5922-3e12-8e3d-e47988d0e73a | -13.4259 | -43.8401 | 2025-12-31 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 76d556f2-9b27-3b70-b7f6-e541f9d27e05 | -2.9064 | -49.3667 | 2025-12-31 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b20feccd-6fbc-3467-ae94-b1bf3a086795 | -2.9064 | -49.3879 | 2025-12-31 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9da11d63-3ad5-3c48-9e75-391e138d373e | -13.4254 | -43.8639 | 2025-12-31 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4c8690f9-005c-3ce1-b781-5c2f48460de4 | -2.699 | -45.6033 | 2025-12-31 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| ec04cf78-880d-39d8-995b-47def6155498 | -17.3844 | -42.6235 | 2025-12-31 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 84b48903-df32-393e-a283-602538b69a11 | -16.63867 | -43.10707 | 2025-12-31 00:09:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0fdd5795-3627-3f4b-b1cd-cac99076aa41 | -12.15906 | -41.84726 | 2025-12-31 00:09:00 | TERRA_M-M | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b2c42adf-c8fb-38fd-90b2-3bf93d370839 | -17.3813 | -42.62279 | 2025-12-31 00:09:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 65ede111-25b4-36e7-88f6-60324e974975 | -13.42561 | -43.85408 | 2025-12-31 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 67110fbb-a58c-32b1-a887-43521b6a3f3d | -19.2825 | -42.18819 | 2025-12-31 00:09:00 | TERRA_M-M | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| f6332642-c37d-3034-94d9-bd60e0673db5 | -17.37241 | -42.6242 | 2025-12-31 00:09:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c228f5c4-6169-300b-b84f-105b3a4fa71b | -16.4366 | -42.21313 | 2025-12-31 00:09:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 6bb355fb-4cc3-3445-b15e-7095da5462df | -13.47487 | -44.013 | 2025-12-31 00:09:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4e3c0bb-0fba-3cce-beb6-4726a0feda1e | -13.35474 | -39.89524 | 2025-12-31 00:09:00 | TERRA_M-M | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 139beb84-8b0f-3fc2-9c94-81aca5021d76 | -11.91783 | -40.73064 | 2025-12-31 00:09:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e572fe3c-10c1-3f63-bb0d-25c56ecaeb3e | -9.86092 | -37.64233 | 2025-12-31 00:09:00 | TERRA_M-M | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 1646c8dd-8ead-3124-83a6-34fdfa5a1f24 | -9.85506 | -37.65016 | 2025-12-31 00:09:00 | TERRA_M-M | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 476f0b99-8bf1-3bba-85a4-34bd97db8183 | -13.42688 | -43.86314 | 2025-12-31 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 555bb949-e1f8-371d-be45-7d8f9c3fee12 | -9.85123 | -37.62621 | 2025-12-31 00:09:00 | TERRA_M-M | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 2eb40d48-487b-3b7d-9204-65c6bb4756a1 | -16.89812 | -39.77301 | 2025-12-31 00:09:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| feba3439-aa21-34ed-a389-59306b0a2859 | -13.03267 | -44.08202 | 2025-12-31 00:09:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9ac2448c-b91e-3f7e-bd29-299f307b56ec | -17.53021 | -40.61763 | 2025-12-31 00:09:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 82e28bde-c62e-367c-9086-3775eb1c2025 | -13.03393 | -44.09104 | 2025-12-31 00:09:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 34d6478e-5acf-35dc-9014-979d9356c769 | -17.37375 | -42.63355 | 2025-12-31 00:09:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a8897f85-92ae-3202-936e-321846c4fa6d | -19.28386 | -42.19765 | 2025-12-31 00:09:00 | TERRA_M-M | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 54e66553-2795-3a10-9694-b828febfcfb3 | -12.9862 | -42.65229 | 2025-12-31 00:09:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8e6605aa-5f22-3109-a218-3ac399824bd8 | -13.35212 | -39.90186 | 2025-12-31 00:09:00 | TERRA_M-M | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 3f2c76e9-2dd6-32ad-b4c6-143b9f0c928b | -13.53405 | -44.09967 | 2025-12-31 00:09:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7aaf737d-014b-388f-8734-11e4691e57f1 | -17.38264 | -42.63212 | 2025-12-31 00:09:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 47ab0256-5957-30eb-b04a-99f7a82e5a93 | -12.98478 | -42.6425 | 2025-12-31 00:09:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 91f94e48-2b6d-33fc-a48b-8c5ad47f3153 | -11.92257 | -40.736 | 2025-12-31 00:09:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8f2141e6-be84-3604-b13f-74944b935f60 | -13.53279 | -44.09065 | 2025-12-31 00:09:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f518fbb3-5c56-37eb-a03b-c370af8c1e16 | -20.20601 | -41.68647 | 2025-12-31 00:09:00 | TERRA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e535bf26-d07e-3fbf-817e-6da8f0c88fe4 | -3.9002 | -40.724 | 2025-12-31 00:10:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 2398fdca-f3a1-39f2-953e-eaeb6e1022c5 | -3.9189 | -40.7229 | 2025-12-31 00:10:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 682ea5c6-ac54-3a83-9a78-25cef3171bcb | -4.3286 | -43.7801 | 2025-12-31 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f20897f2-47b4-33ce-9eb0-150aa1d3ca38 | -17.3844 | -42.6235 | 2025-12-31 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 0d5ddbe9-693e-3167-aef6-714bd90fa592 | -4.3099 | -43.7811 | 2025-12-31 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 680bafa7-47f6-36a2-bc4e-d362e42a3dfd | -13.4254 | -43.8639 | 2025-12-31 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 59f71da0-99fa-3003-9a6c-d5d7b8a3e778 | -1.0809 | -47.9916 | 2025-12-31 00:10:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ccbd464d-008e-384e-a745-aec37d9b508b | -4.3285 | -43.8032 | 2025-12-31 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| cb5c9603-e25f-3a97-bab1-23741ad45e3f | -2.9064 | -49.3667 | 2025-12-31 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| bac13669-f1fd-3b49-b171-af16898bd0db | -4.3098 | -43.8042 | 2025-12-31 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 4307cd72-b631-3e4a-a493-b46cf66009d7 | -2.9064 | -49.3879 | 2025-12-31 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d94d2be5-0103-3a80-9778-c83f953ed184 | -4.60639 | -46.59517 | 2025-12-31 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 017b76c2-6989-32c7-a853-449f33c275dd | -3.45094 | -43.60294 | 2025-12-31 00:11:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e93705f9-f656-3b51-b91d-8f2a2669ce97 | -3.89481 | -42.56283 | 2025-12-31 00:11:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 243d2c3a-dfff-3048-9282-b5c847acf77b | -3.41841 | -39.36324 | 2025-12-31 00:11:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 9d65ce89-1997-36df-8bc9-c364e65532e5 | -2.99425 | -40.32884 | 2025-12-31 00:11:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| bdfae05e-4019-3667-8d26-9c326da3fb27 | -2.70667 | -45.59337 | 2025-12-31 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 7e3417b4-8d45-361d-bc39-fee54db22cd9 | -2.70792 | -45.60237 | 2025-12-31 00:11:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 59c462c6-fa15-3324-82c4-6e4bc8236e31 | -3.87543 | -40.44664 | 2025-12-31 00:11:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| ef49657f-ce51-33cb-b2af-f8bf3140297a | -5.47731 | -44.70326 | 2025-12-31 00:11:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bba7e83d-790c-3a3a-a296-a98ca0e97602 | -3.99372 | -43.7376 | 2025-12-31 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ac900924-d256-3740-b3f8-e896932cb571 | -4.07439 | -42.87605 | 2025-12-31 00:11:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a8bc0d8-3f04-35b6-8fe5-9e9f61c59348 | -4.30703 | -43.79104 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 15d4a245-f46b-3260-9891-5b56e4c1e690 | -6.48607 | -39.03334 | 2025-12-31 00:11:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 3a90fd8d-5818-3d98-b64a-d57cb0bd66b8 | -3.95907 | -44.07354 | 2025-12-31 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c9a438c-21b9-3399-8470-49ae9a32fb27 | -3.44614 | -49.03109 | 2025-12-31 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 51f2ea21-d6a5-316e-9dfa-40f00695e4e2 | -3.913 | -40.71117 | 2025-12-31 00:11:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 36.0 |
| be0851a8-8a4a-36aa-a93a-7b0a01b16d98 | -5.04649 | -47.18198 | 2025-12-31 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bbcd8b9c-4c85-3d4f-ac5a-a041e5d6d764 | -4.30555 | -43.7806 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| f424b404-6c68-3479-ad82-f894cbf01b79 | -5.72801 | -45.03948 | 2025-12-31 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| a6ed0778-4221-3367-a303-60d92b4877c8 | -3.95764 | -44.06349 | 2025-12-31 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43251fa6-477b-3aa7-a071-fb059345a3ff | -7.49261 | -42.72402 | 2025-12-31 00:11:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3c31e73a-60fe-34e4-99fa-12d8aaf9bfd3 | -5.88388 | -46.50207 | 2025-12-31 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6d836155-f48c-35de-9503-9954a964eb95 | -5.4644 | -40.50695 | 2025-12-31 00:11:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 78ba4a13-8502-3a7c-9208-8158fc47b86e | -4.32602 | -43.78825 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| eee18da0-e6fd-351f-b4e4-64baba867b08 | -2.997 | -40.34789 | 2025-12-31 00:11:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 3cadaa8a-825f-393f-bf4e-bef4e50337bb | -6.48932 | -39.03867 | 2025-12-31 00:11:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 9961c1ca-8c1e-3bf2-8f5b-1fd2ad711c70 | -4.40404 | -45.73424 | 2025-12-31 00:11:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35331f85-2e54-39a3-a42f-44e7c5f86876 | -6.28578 | -39.60445 | 2025-12-31 00:11:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 4e579295-af2d-3737-841d-48557b3e7fbc | -3.90858 | -40.72273 | 2025-12-31 00:11:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 8a5e79cb-2de3-35df-a4ef-c92bc48a88f9 | -5.10847 | -43.15748 | 2025-12-31 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c083c310-07d9-31e6-a734-db297398e6b3 | -4.60727 | -45.67524 | 2025-12-31 00:11:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa2b8db5-1a2a-3096-a49f-04cfc283c7de | -7.78523 | -43.10586 | 2025-12-31 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 338474a5-eee2-3462-9ac5-62663b6187e6 | -4.79518 | -40.79293 | 2025-12-31 00:11:00 | TERRA_M-M | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| afd9d898-3a55-320b-a91d-6fd356c1f5a7 | -2.90522 | -45.09959 | 2025-12-31 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1cca00e7-452a-3984-8c61-2e8ca02f69a4 | -3.45286 | -49.00878 | 2025-12-31 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e5d02aa-a190-327d-b2b4-4d5084681560 | -7.82983 | -42.01249 | 2025-12-31 00:11:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a3244fe1-4e11-37d1-803c-af865a45d625 | -6.29293 | -46.99787 | 2025-12-31 00:11:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99fa7fca-c17b-33a2-8df1-0745cebd0618 | -5.71854 | -45.04668 | 2025-12-31 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 28b8e30a-2839-349d-9dc4-be96e49a62d3 | -4.2519 | -46.63338 | 2025-12-31 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6bd395d2-7249-3887-a103-adec52a9b952 | -3.86892 | -40.45943 | 2025-12-31 00:11:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 4acdabb4-8fd9-3019-857f-42a04051f010 | -5.05667 | -47.18984 | 2025-12-31 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1b553b1a-75cc-3387-9386-f54e60310047 | -4.07609 | -42.88785 | 2025-12-31 00:11:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d6767232-714e-398f-8f7e-3bf87c73d435 | -5.23237 | -49.0895 | 2025-12-31 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1ff1d43e-c206-3615-af37-86068e3f48f2 | -4.31506 | -43.77925 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 17214e1e-0b24-305f-981a-3f74ebc59d37 | -4.53079 | -44.33657 | 2025-12-31 00:11:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 76448c4e-f2fc-3c68-8b92-bff31612bef9 | -3.55249 | -43.67003 | 2025-12-31 00:11:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ff6045c-fa2a-3e08-8886-4d7ee4a6f72d | -3.93387 | -42.12944 | 2025-12-31 00:11:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c5aae660-129f-3ebc-bf78-876cf5fc36d3 | -6.61325 | -43.73486 | 2025-12-31 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 931d7002-e228-3bc2-8944-380c93bf823b | -5.04774 | -47.19113 | 2025-12-31 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4d45431e-3ecb-3b2a-93f1-4525e1ec4f26 | -3.91544 | -40.72834 | 2025-12-31 00:11:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 47.1 |
| 3e542226-55c6-38fc-ba17-8026b5405ca2 | -4.26071 | -46.63214 | 2025-12-31 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| db398a3e-9e2f-31fd-a3c7-6180313b493d | -4.55931 | -46.66201 | 2025-12-31 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad0cf8c9-4110-305e-b736-6e355bc7a645 | -6.20907 | -39.27177 | 2025-12-31 00:11:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 2cc6f793-c77d-33f7-8cba-d6fcaa9e571d | -4.32456 | -43.77787 | 2025-12-31 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |


[Clique aqui para ver as próximas entradas](README2.md)
