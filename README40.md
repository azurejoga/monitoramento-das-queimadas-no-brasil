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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0326b0e8-541f-3544-a0ed-912e1b61a72d | -11.81301 | -46.83414 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac06ca97-f63e-35a8-8baa-b27236ab1d8f | -12.98818 | -46.91848 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57a6a01e-1f2b-376f-826d-2455eae5c907 | -16.0948 | -49.64348 | 2026-09-19 04:04:00 | NOAA-21 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02cc226a-066a-3806-8ccf-3f4fd51c1f8a | -10.83416 | -50.91104 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ee045c2-54df-32fc-af87-237376f385e3 | -11.07737 | -48.30573 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 77201fd6-976f-3f60-af65-298212c74be1 | -15.06075 | -48.58489 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99bebc12-66b1-3393-a3c8-7d6a219e4e30 | -11.05777 | -48.30928 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edf76414-6049-3733-8890-c8c6385d91b2 | -12.1326 | -46.96996 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61c57bca-1896-3af9-9d9c-1fd9d248dd7e | -11.87676 | -47.61315 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a372ba2d-a2ad-367f-8b62-6b0c9b27a3d9 | -13.60391 | -48.31485 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47b2bc72-b511-3d5e-91bf-94d9f8e84c5e | -13.62765 | -48.30873 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 646c52c3-268a-3137-8213-635887c89326 | -13.58303 | -45.47402 | 2026-09-19 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85ae4bc5-dcb1-3f62-9c1a-60ca1296aa3e | -13.61196 | -48.31973 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f56a56a2-2f33-36b3-a751-17b8b0658e41 | -14.69217 | -46.65385 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a6afde26-e0ac-3629-ad41-e77ae5b821ab | -13.59169 | -46.94148 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64d3ae36-3496-3d6a-a967-d4e4e3275102 | -14.10052 | -44.83509 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3acdf77b-9dfb-3a5e-a97a-06b3a5f5acfc | -14.17123 | -47.84447 | 2026-09-19 04:04:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 956d5ece-e811-39b1-9b0c-1b1ce9037794 | -13.68045 | -48.58476 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 479dbd3d-54f9-3c02-9128-84ffc14b7e64 | -14.73913 | -47.13834 | 2026-09-19 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74f6fbc5-3870-375e-a138-08ed34071a8b | -13.0029 | -46.97764 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 085bfc80-072e-3758-b2df-70c753a9cdc4 | -16.04774 | -49.98442 | 2026-09-19 04:04:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bda4436-f0bd-3225-829d-cfb36deda42c | -13.23799 | -46.90546 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a27471ba-5f72-33a5-953e-b3b674750b11 | -14.66615 | -46.66471 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 49fd832a-3551-3fd5-a305-cff56227a9bc | -11.12478 | -45.27985 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb7a9bfd-34d4-3ba2-8d64-d8a713ef2706 | -13.87774 | -48.60662 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e67f262-de45-3af9-b43e-8d49aa18f199 | -13.60561 | -46.93316 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb7861a2-1f7f-34cf-8596-4e44dca5a36e | -12.14367 | -46.97956 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5f9007d5-3232-353b-8822-7938a57b0442 | -13.65013 | -46.94613 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 309d4523-d8ba-3f7c-8c4d-261a1df7800e | -10.83468 | -50.17715 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8cbd972-53ff-35ff-b8ed-3b48c4ce4c52 | -12.6889 | -45.96227 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05d6c948-ab1e-3274-b1e0-3b3f56e4cd0b | -11.32507 | -45.54297 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63142b7a-3cb8-3dd0-ac43-2a955c724437 | -10.80389 | -48.11677 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77ffd3a0-9e66-394c-bb3a-fce1b53ab344 | -13.43482 | -43.81766 | 2026-09-19 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d6e8b86-2a83-3c7b-b31f-84121a91c593 | -10.45327 | -48.67701 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65610e7b-2331-3ac0-ab98-fbb30f73eb1c | -13.61281 | -48.31585 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 29c17071-eded-3db2-95a5-34efd0c776ce | -15.88838 | -44.72942 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdcfa82d-1e6c-357f-91eb-6c17b56f5517 | -10.83212 | -50.92194 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a485c24-92db-3fb3-9ab4-4bbe32941ef1 | -10.97177 | -49.73995 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86dca32b-0d58-388b-990d-1e1eea941ec0 | -11.81715 | -46.85849 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f177fb7-9b84-3ca9-9ac0-4659ef5eaf5e | -10.87785 | -54.06545 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f88cf5d1-635f-346a-af9b-74995a575041 | -14.94934 | -49.928 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a516b9ad-be06-3e8c-b9d5-8ea4ca6d395c | -12.12766 | -45.15032 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 999e6e60-be2b-305d-8099-3cac89b6fcc4 | -12.15563 | -47.00831 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e907d78-2cbd-32c6-814a-a72ebf9c08d9 | -11.49341 | -47.72344 | 2026-09-19 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4523cc3f-576d-3004-a15b-4df522593280 | -16.80259 | -46.98969 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 332ae747-1075-3731-8670-76074dc7cfe4 | -11.07824 | -48.30084 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e142e0ae-d5d7-3515-ae33-2155511cf997 | -11.00478 | -48.31647 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f94071e-0aa0-374b-ae64-6fa0d96ffb21 | -14.17247 | -48.75498 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8703de1f-03ad-3b00-84e7-6834997361ee | -16.09643 | -45.12999 | 2026-09-19 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3af8cf8e-e0c3-3133-a048-5cd479608c5e | -10.97457 | -49.75296 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a277533a-7877-30c6-9880-e3bc05071fc6 | -11.30537 | -51.72646 | 2026-09-19 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 68860486-8d6d-30c9-bd8d-573321813ba6 | -10.93474 | -53.95509 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f4cef6c-90be-3167-8173-9a401d608c79 | -13.02029 | -46.97425 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54a9a221-20c0-3459-b533-2d2e5228b339 | -11.06123 | -49.76598 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b21663a1-a042-389f-9139-b7e9331b8e67 | -14.66681 | -46.65735 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d3833547-d314-3aba-8e2c-71973c0d7502 | -11.12317 | -45.28921 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e5ce4d-9f6f-3f8e-9890-aa9eb15b85e8 | -14.22961 | -48.51564 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54e429ff-14c9-3b96-a8d3-d194ab1ba982 | -11.07006 | -48.26727 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf6b76f0-edb5-321c-97b4-c971e1319b79 | -10.93406 | -47.91609 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf2839c3-221e-3d4d-9a4b-9b8c75471e7e | -10.99838 | -48.32252 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d2bdf9f-9f48-3c27-b722-70c18af2ce22 | -10.9359 | -53.94939 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a0d52507-18d7-38d0-80d7-016a3e9567ea | -11.47438 | -47.65326 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e257dc4-ac47-30f2-a20d-4ff56e1c5d30 | -11.14208 | -54.02696 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 28b5c7d7-891d-3f7d-90ff-a2e557e523a0 | -12.58416 | -49.10025 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 845da688-80cc-3b3e-bf68-b4758713b135 | -12.15873 | -46.96661 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a67305bd-eac3-388d-a12f-e6b0deb219a1 | -10.89549 | -50.88895 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35151813-c250-34bd-8434-9fba29554f0a | -13.01871 | -46.93607 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b245a2e-4797-34fd-9fca-e6c13048dab5 | -12.35198 | -50.69708 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 210da4c5-12a5-3726-9121-edd4fd6d9cc4 | -13.00759 | -46.97485 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cee90252-308e-3bbd-8b92-85cbb5150130 | -10.86852 | -54.09229 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34ac6baa-619f-3135-af93-d37b03fb8715 | -11.55551 | -46.9014 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5be5f63d-c557-3a67-9d89-101e1313baa7 | -11.12398 | -45.28451 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f5798c0-46a6-3d7c-9cf7-61db25c979f7 | -11.32336 | -47.35556 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 622e4109-39b0-36d5-a8e2-f745ace479e2 | -12.33573 | -50.72491 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74f88132-5e29-3031-8679-79587552b804 | -11.18062 | -45.38405 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ba8314-5da5-3fc1-9d2f-4c34c67fd689 | -16.8863 | -50.58352 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 287d89b9-f673-358b-9421-2b1544640ec0 | -11.3319 | -47.35734 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85e40ef9-b827-3df4-91fd-26271083a5c7 | -12.35071 | -50.70372 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49ae991f-be93-3619-98f7-9fc038532862 | -11.00399 | -48.32092 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b1f750c-5968-3e43-be94-824935df3baa | -14.94283 | -49.93555 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3608a628-d0ef-3ef9-8e73-62ebe49a08e8 | -13.61464 | -48.32975 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d801e3b-847d-3915-b057-0e613040d289 | -13.6513 | -46.93958 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0272218-90a7-347f-8139-0d847a2f81a4 | -13.02106 | -48.64139 | 2026-09-19 04:04:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ad3e972-67ca-3f5e-afef-14eb679776c2 | -12.33046 | -50.72388 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8245ca8-8687-3b03-bf6e-ab22d33c61db | -11.30796 | -47.26893 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d8cd09-226f-3491-b04d-21656823261e | -10.46541 | -51.25901 | 2026-09-19 04:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b26a5794-be67-3728-b1dc-725d9c1d19f8 | -11.06062 | -49.76091 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35ab2d51-7407-3602-9218-2a06173834b4 | -11.1433 | -54.02099 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d47abd83-be1f-3610-82c3-77aa6388d58e | -11.32441 | -43.99054 | 2026-09-19 04:04:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93ce242f-26b2-3ad0-aff9-cb5a84af1b3d | -13.23866 | -46.90173 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67b81bff-b440-3622-8644-9399581ca233 | -13.62595 | -48.31784 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f9b95ca-0865-30f1-a4da-98fa194c648a | -16.88257 | -50.5772 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8689f6a1-b273-374f-bb5c-14a380932bd1 | -12.86257 | -46.33593 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8f5d4c78-fa27-3968-a804-cb9114aef335 | -11.18081 | -45.38643 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f80e8744-a273-3ace-9ac6-b55f74c09dd0 | -14.67989 | -46.67768 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93e7c515-094f-3b2b-961d-7821602eee45 | -14.95043 | -49.92219 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2d0f7c8-e549-356d-a52e-f28a9c57ac62 | -16.05244 | -49.98527 | 2026-09-19 04:04:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da4a776-3a76-3b29-a24d-6e7ee3d8ac78 | -12.13193 | -46.97375 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3384b8c2-f32c-3fb4-9f29-0bf6895b9ca9 | -12.57557 | -49.11251 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1053db5f-4ea3-35e1-940f-c24aaae771d5 | -11.33121 | -47.36123 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
