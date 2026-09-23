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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa225cd6-b72d-33c7-8027-df4937fb785d | -11.74829 | -47.61872 | 2026-09-23 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e3bd0dd-188d-30d0-9adc-23edc3494486 | -12.42248 | -46.97163 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 20570f7d-fa61-3210-89c8-95ed665dfdee | -11.68634 | -43.44837 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c1a0603-7ca0-3e8f-9381-f06219891888 | -11.45679 | -47.33385 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2320e236-8023-3dd4-a01c-4cf7e0d98243 | -11.15273 | -42.84779 | 2026-09-23 03:45:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b21c4267-0700-3c57-834e-1dfa0e596307 | -12.126 | -47.38109 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5437f625-a868-3cbf-b1f2-394619e714d5 | -13.29852 | -47.89843 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 820fcf16-47c9-3550-93d8-831877e2f8b3 | -12.4193 | -46.96422 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a47c4dd6-2eaf-38f4-9edc-33eaffa63b12 | -9.9977 | -39.17589 | 2026-09-23 03:45:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 61a9eeeb-38b9-3a0b-9365-6f19097c4fd0 | -9.86188 | -48.39398 | 2026-09-23 03:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09ad446d-82c7-3032-87d4-1ed5525e2096 | -11.47834 | -47.35953 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 93169286-9c29-3a6d-b6ea-11fa851206b3 | -12.42351 | -46.96672 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e465bad1-1b6d-3d7e-a279-e2e55927d916 | -11.86918 | -45.78237 | 2026-09-23 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7379a5b6-5634-3c11-ae70-854df7a5f4d0 | -13.45293 | -46.27052 | 2026-09-23 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 113c60db-f6f9-37f2-936f-37119fc8c428 | -11.26343 | -43.42076 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e721a4b3-56cb-3959-a99a-62a7b041713e | -10.45903 | -44.94839 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49ec9caa-05c1-321f-af23-4f02356877c0 | -9.54454 | -45.77176 | 2026-09-23 03:45:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a625286-1cc4-3b9a-97a6-64398f301d4d | -11.532 | -45.3603 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2df1e8d-f1c6-376e-b634-2e81d44c14fb | -10.44379 | -45.09892 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fdc4da7-9ea2-3369-86af-be998feb4764 | -10.71111 | -48.73556 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 804f0b83-97c8-3b17-a56f-6d1b0dc0f481 | -9.55872 | -46.54173 | 2026-09-23 03:45:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad1ea582-cc5d-3805-9e9f-92901930128f | -13.45699 | -46.28057 | 2026-09-23 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4052febe-c07e-38db-b685-677567be5e13 | -10.50203 | -44.86016 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de9e6684-a735-31f5-9e93-70ced9bee21f | -10.44867 | -45.09733 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 932ed634-0253-399f-9304-fdaae81dfafe | -12.41532 | -46.98388 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aecc282b-66f7-3792-b82b-cb21a0a5268e | -11.73782 | -40.41122 | 2026-09-23 03:45:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bdc2d94-2d83-3ef4-b773-d2f49d808d7b | -12.40815 | -46.98747 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f5bb53d-6df0-3471-a5c3-74c4d9f574f6 | -11.87665 | -45.7751 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c525eaa1-2df7-3d79-be66-8d2357697c71 | -10.51027 | -44.87775 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63627f18-1b69-375c-9ace-3adee4150a35 | -9.83571 | -46.39039 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e77bdb92-29d3-399d-9dd6-4b4d8075d6b0 | -12.38378 | -47.0757 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c1d1304-38e1-3b47-973a-bd49379c9e96 | -10.11502 | -46.09188 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7128201-cd5d-3b21-97ea-1166837f3468 | -8.7993 | -44.28425 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa8b2f06-cd81-3453-ab7e-3323eadef6fb | -10.70951 | -48.70807 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82e23828-6b39-308a-97f4-449ddf154584 | -12.12271 | -47.39732 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 036cff81-1393-3aa0-bb0b-9a7489c26122 | -13.86223 | -48.56799 | 2026-09-23 03:45:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 678d5f5e-50d1-338c-bfe3-d9dc565ad483 | -12.4163 | -46.97035 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 67e0c20c-a2ad-318e-bff7-f9a9db146e08 | -10.50763 | -44.86131 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eaad5a2-45f8-3567-b798-05c9c7ef4a84 | -9.93678 | -36.35941 | 2026-09-23 03:45:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 805636f7-c55a-30db-be77-b7b376719ffa | -11.87167 | -45.76981 | 2026-09-23 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8a45f837-d51b-31a7-8597-b00809bd8702 | -14.6128 | -45.64877 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f278a713-da63-38a4-b214-762e94ef0e70 | -11.35311 | -43.38173 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 015cf624-abd9-35f2-8dbd-dfd2a856592a | -10.51663 | -44.87498 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 738acbc1-302d-3fd0-83f9-3b9e37d2d053 | -11.47145 | -47.36045 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 665d2628-4360-39e1-82f1-d1a2d7085d40 | -11.53283 | -45.35601 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 05d90d67-070b-32a2-8ec1-e986848cc1cc | -11.35812 | -43.38269 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5031c5ba-0d47-37f7-8119-7b653fc98cdd | -11.35868 | -43.37975 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24d38729-3bc6-3825-a4b4-be74a22f0f3e | -11.47204 | -47.35948 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f60bd951-e136-3cb8-b25d-aa44dfc9cf27 | -10.44713 | -45.10549 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8626a49e-7fde-3f83-b002-28bc037262d1 | -11.88329 | -45.77203 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75a68c1f-5e73-3340-b9ed-0034561aaa1c | -10.45519 | -44.95056 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db4d1e8a-c9db-3454-b2b9-6b3a6f2ffd37 | -9.57226 | -46.5396 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64736379-63ea-3c2e-9da4-921c3fecb7dd | -12.12607 | -47.38782 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70480854-66fa-3708-801c-69b20f8f1370 | -11.93389 | -38.29307 | 2026-09-23 03:45:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e93cdab7-bdd6-380a-ad92-05d9b0b99b5f | -11.9375 | -38.29371 | 2026-09-23 03:45:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| fb084544-0315-3265-a810-2cbc324f5919 | -10.21169 | -44.15046 | 2026-09-23 03:45:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26d48a47-200a-3b3e-ba36-5c049e78cd99 | -8.80763 | -44.27047 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1dbcad68-6c66-3039-82de-b6e8833d0b5f | -11.42294 | -47.36845 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adb858be-2f52-3030-9c8a-3b9a9aeb0059 | -10.49833 | -44.87922 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59206b06-b1a7-3d7c-80c0-329d27829e87 | -15.1683 | -43.55669 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3095a4d7-06bc-39ec-9411-e9af0e35ac87 | -11.66464 | -43.48084 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa53ce33-856b-30a0-a801-235343f3b3a5 | -8.79588 | -44.27169 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 195c16e9-34a8-30ff-8c48-b96610cf44e7 | -8.90718 | -45.95596 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddb4566-1e2f-31f9-933b-b720aed84ad6 | -11.29352 | -44.03849 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 874323d3-00f4-3ae9-a8f1-89fc888a0543 | -11.65572 | -43.47292 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18b01600-2cdf-3e23-b202-3ffb5bd26d32 | -10.82848 | -48.4777 | 2026-09-23 03:45:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87263163-0bae-39f9-9ee6-a6e01d82543c | -9.86488 | -48.40413 | 2026-09-23 03:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 359f51f1-9720-3e2e-aac6-aed0d1d4f1ab | -14.29566 | -43.18891 | 2026-09-23 03:45:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2a7f3a77-f989-30b8-ad7f-bb88038afb70 | -13.87006 | -48.56378 | 2026-09-23 03:45:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d38ee0e-25d5-3ed5-8e9f-fa25d09e0f33 | -10.12116 | -46.09283 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0df4dd4a-1dd5-3de5-b9bd-fa448175f363 | -14.64537 | -45.60006 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03c49eaf-842a-34cc-a3a3-86b72aa2c1e4 | -12.40914 | -46.98259 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9eb36c7a-68ab-3fa7-9aae-b7b2a3ab8d88 | -11.12686 | -42.7975 | 2026-09-23 03:45:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 38b094fa-0a8f-308b-8783-0e0ae09a5523 | -15.6344 | -43.52826 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1668f205-36f8-33e0-ad3d-d2e31ddb4006 | -15.16628 | -43.56964 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 15dd2873-5f68-3ac1-b87c-0f6c0589b26a | -11.47897 | -47.35838 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bf2cfd80-4c1c-3616-b02c-e9a51e72b6a0 | -8.80826 | -44.26708 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86b95a88-5b85-3440-9930-0b1da76e83da | -8.37293 | -45.60757 | 2026-09-23 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6adc4bc6-9302-3b7b-8160-daf9dc4dafef | -13.6185 | -42.44922 | 2026-09-23 03:45:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b36edf56-5a8b-3b0c-a753-a84eaf3e5e45 | -11.74718 | -47.62119 | 2026-09-23 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1561f5d8-079a-3af4-ae3c-24419905f463 | -11.87001 | -45.77819 | 2026-09-23 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4312eaa9-16b1-3a2c-af27-7a6c6b5c0520 | -9.84299 | -46.38622 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 243393a9-a885-3160-ba3e-dd4ce731ec14 | -10.11506 | -46.09091 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3e7edc6-de35-3227-bc0a-689b21fea785 | -14.61206 | -45.65242 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0404d905-8985-3038-ab55-c9700ba94cc5 | -10.12121 | -46.09181 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d57f24c-ffb0-31a6-90f2-33d88c270d78 | -10.51516 | -44.88263 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf70a375-a07d-31db-bf58-8f8841b5bcca | -12.12493 | -47.38637 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef087465-f52a-3caf-89b4-0d10417942db | -10.7079 | -48.71575 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8505b617-7b22-3e2e-9950-2dcb9c1d5acf | -10.45234 | -46.27572 | 2026-09-23 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 501799cd-d549-3e44-8c90-35df435286a1 | -8.36672 | -45.60701 | 2026-09-23 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5427082-90ed-3ee1-83dd-29d85c499928 | -11.52308 | -45.34547 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a44869-94d9-3bb3-ae53-84d1f2f0f013 | -10.45829 | -44.95233 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6e7028a-6c75-3499-9149-2452b2bc23a4 | -12.4183 | -46.96915 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0f7256b7-617f-3dff-a3da-10499f9f3ec2 | -11.46919 | -47.37309 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4724d3df-5e3c-3ed6-aeca-ef82c51e99e3 | -11.47116 | -47.3637 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 671471e8-65eb-39ce-857d-7fb43dcea806 | -9.40142 | -40.31034 | 2026-09-23 03:45:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 713f27ec-4cd0-3d55-a401-0b79e8d6368f | -6.61 | -43.79 | 2026-09-23 03:45:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d468a709-f5ea-38e2-85da-e066db0b9145 | -6.61 | -43.74 | 2026-09-23 03:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 313073d8-6946-33fc-a346-8a58061b53c7 | -6.58 | -43.74 | 2026-09-23 03:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66ca0bae-52af-3d7e-b5dc-54e301991d20 | -6.61 | -43.7 | 2026-09-23 03:45:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README47.md)
