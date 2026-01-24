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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440acfee-bda7-39dc-a05d-812e1777e74d | -19.67128 | -57.20106 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 32f6f015-79e3-3024-bc5e-f860c401bc8e | -18.81539 | -51.60583 | 2026-01-24 05:37:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2bc51e-bf5f-32e9-8e26-963378df0f80 | -19.68447 | -56.86474 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 743a85be-be53-30b7-ad3d-b68cb784db0c | -16.16639 | -57.95802 | 2026-01-24 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2e0b1ea5-4d59-3ef6-92c5-e8aa90e63277 | -17.71251 | -53.27902 | 2026-01-24 05:37:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecc7dd88-553d-3d1c-b805-f6ad68a0bab5 | -18.81597 | -51.59911 | 2026-01-24 05:37:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20f11c99-7853-321f-a309-3d3f44b877c4 | -16.44695 | -58.16636 | 2026-01-24 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 04e5b83e-4cc4-39d3-b716-dcb98264d7d9 | -19.67357 | -57.19793 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 04723c61-a97f-3a7c-9ee8-662cf8082049 | -17.70731 | -53.26867 | 2026-01-24 05:37:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| baf2dfec-0864-3541-9540-d19e93a99d95 | -19.67295 | -57.20362 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6d47ccc5-9f52-324f-8a4d-d61b32cd9f88 | -19.66637 | -57.20044 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 29a85d94-7ae8-320c-9848-f63efb05face | -19.67062 | -57.20676 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 0c020a5e-c3ad-3c6a-881f-4af350dde672 | -17.7037 | -53.269 | 2026-01-24 05:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 059caa70-39f2-3cfb-bde2-13af7b6ad723 | -20.36835 | -57.8618 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| adbff922-0e0e-3e3b-9296-7f224b32c1b9 | -20.35437 | -57.85413 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b3ba860-1309-3853-8e6d-96faac64e4d5 | -20.34551 | -57.84761 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f0838390-91b0-304d-a6f4-fdfc509fc8c2 | -20.33603 | -57.84639 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a7654b6f-9d0e-3fe8-b5b7-fb6a0049b968 | -23.5375 | -55.50821 | 2026-01-24 05:40:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b11e7bfc-23e0-3659-8dc6-00a329b15d53 | -20.38611 | -57.87486 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a23bf977-4417-3cb1-9c70-27f3e25dab63 | -20.35946 | -57.85527 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7381f87f-434c-3a09-b084-bf979fa27c66 | -20.38197 | -57.86895 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 67a7543e-2169-3265-9432-26b37f9e5b02 | -20.36894 | -57.8565 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 29d788bb-bfbc-38b7-8a34-46d83397a3e0 | -20.34077 | -57.847 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 02421ca5-f04c-3d6c-b022-55aea218d319 | -22.02808 | -56.3359 | 2026-01-24 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb8c8dc-17b0-39d8-8e8b-e38c6bee7943 | -20.35026 | -57.84822 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b93d18bd-387f-33e0-b8e7-6f5523de3b4e | -20.34015 | -57.85229 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 58770104-dfb9-3912-ad64-f15fc3fae108 | -20.34108 | -57.84749 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| abfb3ab4-1f7d-328e-b5c2-922a3d162281 | -20.34489 | -57.85291 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fb920918-7824-3f40-80ff-9091b43c9d63 | -20.32119 | -57.84985 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6247de50-71e7-3e3c-a69f-a6dadeea7193 | -22.02773 | -56.33942 | 2026-01-24 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f46aae-8915-33ec-8cf9-199ed70280a9 | -20.33541 | -57.85168 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 11fb82b4-37c6-3e80-86c9-d069c6e7d3b7 | -20.3642 | -57.8559 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8d84019e-23a1-3f4d-a764-7685827190b2 | -20.35056 | -57.84872 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cb0f7544-34e4-3e08-9e98-9f81c5e397cc | -20.37723 | -57.86833 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 48553011-ccff-3eb6-a200-371b01ba0d95 | -20.34582 | -57.8481 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 39181ad0-fdb1-3260-b661-08f3dd212f4b | -20.35472 | -57.85464 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b38e4c93-643f-3def-9f91-030f831f9469 | -20.37783 | -57.86304 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2d39dd07-1ab5-3d37-8fd2-837773aaa4ea | -23.53687 | -55.50689 | 2026-01-24 05:40:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0032d7c1-08ec-3d34-bfc1-e070685cdd01 | -22.02241 | -56.33859 | 2026-01-24 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24bff95d-76d7-3c6d-b0c2-5ec81f7752ab | -22.02275 | -56.33507 | 2026-01-24 05:40:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91dfb7d9-5eec-3623-ad7b-f77688e3b963 | -20.31645 | -57.84924 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6b755991-78dd-3223-91f1-1dbacd793a6c | -20.33633 | -57.84687 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c6a2df67-7deb-36b1-a5b6-c884c5fb03df | -20.32593 | -57.85046 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9d2ff7d2-7639-3186-8eff-4f44e75228d2 | -20.34963 | -57.85352 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62efbd8d-5ee1-36da-bab7-331c97b6cc56 | -20.38671 | -57.86956 | 2026-01-24 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 014f8593-447c-3223-a32a-d5498fdc5994 | 3.22188 | -61.19703 | 2026-01-24 05:54:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7336f604-817d-39ef-93b7-354483635f91 | 2.51539 | -60.98647 | 2026-01-24 05:54:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c1adb70-ce80-33ac-a045-d4462674434d | 3.23588 | -60.23803 | 2026-01-24 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 350215d4-3320-325d-8516-5f55533e443b | 0.77847 | -60.18464 | 2026-01-24 05:54:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64b697b5-f3a4-31fc-93a6-125e7730a419 | 1.35448 | -60.05759 | 2026-01-24 05:54:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e453ebbc-116f-3ada-b4f6-f4450172e8ed | 3.24023 | -60.23732 | 2026-01-24 05:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c7fb7a-a1f1-3998-8ac2-148f8a3c5337 | -20.34649 | -57.85355 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f8d3817f-2fad-33f2-9115-39b1d4731f54 | -20.32746 | -57.84556 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 56292fd3-6424-3b6f-8b6e-055904b3ee18 | -20.3822 | -57.86424 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8958b3cf-d241-33fb-9b92-ba2cefd82ba2 | -20.36692 | -57.86238 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 48b77f08-b5b1-3ca2-b81d-ba94216befd4 | -20.38088 | -57.86365 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0918dd84-b437-36cc-8edb-febbd8a1fff0 | -20.36182 | -57.85555 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1e69af3a-58e9-3e09-a15b-bd453cda5591 | -20.35484 | -57.85492 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9bd1447a-b611-35f7-963b-07f67f478118 | -20.35347 | -57.85419 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 91a6bd7f-e5ba-3b20-a5bc-849a62b118b9 | -20.3739 | -57.86301 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 149b19b6-6e58-3850-a277-09b9a17ca763 | -20.38036 | -57.87053 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 15232b0d-a7e2-3946-9615-04ff43b8a964 | -20.34088 | -57.85369 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 58053eb6-f2d3-3207-aaa0-15e710becc25 | -16.44765 | -58.16709 | 2026-01-24 05:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9d16d7a0-13be-36ce-ba5d-55e55d936fa6 | -20.32692 | -57.85246 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8b0cf677-dfb5-3686-931c-ce3b1a3a8a8f | -20.36825 | -57.86303 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 514cf8ec-c555-3149-9447-5741b70e72e8 | -20.34786 | -57.85431 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cfd3484b-fb65-3a3e-9c26-58a2050a0e5c | -20.38164 | -57.87112 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7be12402-76d6-3599-980f-22e24698d663 | -20.33444 | -57.84618 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 285e4868-23a6-3a11-9be4-2da59db5502f | -20.31994 | -57.85183 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1f7e1343-1a32-3c30-81a7-8e0258ef7b65 | -20.34143 | -57.8468 | 2026-01-24 05:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 21a77f04-5381-3cea-9338-40aa8e81dfc1 | -19.67289 | -57.20653 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 68a0477e-f8a9-3672-a874-649547ba4ac5 | -19.67817 | -57.1951 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 536d3215-2bb6-369a-a44a-d8500e123681 | -19.6657 | -57.20588 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a3c78c80-3cd3-3253-a77c-de78a5529f25 | -19.67344 | -57.19908 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2780abc-0a7b-3f9c-b2e3-6edc4d48d592 | -19.67038 | -57.20193 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d2194d12-c820-36cc-962b-767777027a61 | -19.66979 | -57.20936 | 2026-01-24 06:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f22831d1-69b8-3f7e-9812-091c750a92cb | 0.5588 | -59.84465 | 2026-01-24 06:54:00 | AQUA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 06132257-b774-3e44-a578-993a09061cfd | 0.55554 | -59.83944 | 2026-01-24 06:54:00 | AQUA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 40613d85-4220-3531-a558-f2713a7c6e4e | -16.4425 | -58.16538 | 2026-01-24 06:56:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8965e948-b406-3d42-8d73-5f95615de794 | -17.69571 | -53.26453 | 2026-01-24 06:56:00 | AQUA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f6c44da6-179f-349f-9109-ffc3d0a40c62 | -17.6951 | -53.26978 | 2026-01-24 06:56:00 | AQUA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 9605c4cd-673e-3539-9881-1a0e0851b60d | -19.6718 | -57.20152 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| f1467659-a3fe-3381-9e8f-ea0a2e307dd4 | -19.6734 | -57.18958 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 78b75d85-585a-3c04-947b-05255e41c874 | -19.66029 | -57.212 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 88a5899c-dd1e-324c-8a53-a4d6a446e037 | -19.66188 | -57.2001 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 11fa8313-7541-307f-a0e7-f765d3ad8067 | -20.34397 | -57.83912 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a6842035-a25c-33cf-bc8f-5bce2c054dd6 | -20.32103 | -57.84063 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 3661975d-8cf1-37df-9780-cf9f917caa51 | -19.6702 | -57.21342 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 04a92394-ca11-3bf8-a4dd-d6a63bb4d679 | -20.3195 | -57.85185 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| dab9b2aa-a5c8-3dc1-8d63-8d01aa196ad2 | -20.34248 | -57.85037 | 2026-01-24 06:58:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5d52cdf6-72b9-3136-b83d-29900b920030 | -19.6774 | -57.2026 | 2026-01-24 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| c0525019-2a08-3a3f-b41e-9dffe0f93c5b | -19.6774 | -57.2026 | 2026-01-24 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 14de5e39-1808-33c1-95f6-7a48430751f4 | -19.677 | -57.2235 | 2026-01-24 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 518cc633-223e-37cd-8d98-aeb6fa4abf92 | -5.96727 | -38.20672 | 2026-01-24 11:53:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0c4043a5-1b9a-3866-a19f-bfa1fae51154 | -9.04979 | -45.06661 | 2026-01-24 11:55:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0273b64d-f869-3af8-9b38-1b224673543b | -13.1813 | -39.88541 | 2026-01-24 11:55:00 | TERRA_M-M | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| e0ad5e57-203b-38bf-af81-ab807a8b1610 | -8.96168 | -45.91655 | 2026-01-24 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 062acf3d-e5a3-3d2d-8770-ed8da1af42a9 | -8.96027 | -45.92614 | 2026-01-24 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d8d9dad-105b-339e-a6ce-1e37c5b9bb4f | -23.60679 | -48.2661 | 2026-01-24 11:59:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a035460-dbae-36fc-b3f7-eff0a373193c | -17.7037 | -53.269 | 2026-01-24 12:30:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |


[Clique aqui para ver as próximas entradas](README8.md)
