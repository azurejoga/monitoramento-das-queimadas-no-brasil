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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b52b59da-97b8-3b4a-bb12-a50a330e2e86 | -10.26635 | -49.96704 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34d81d66-42dd-33f9-b696-b81dbb22b74c | -10.44946 | -46.29021 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3460149-54f2-3e96-96f3-483685721b70 | -12.91727 | -50.90972 | 2026-09-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f78b6685-bd69-3006-b7f0-ebc7e3ca1cc1 | -11.96333 | -50.75946 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80ec84fa-91e4-3fad-8095-e55b50f3ff20 | -11.42811 | -44.18771 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 406d76bd-facb-310b-8274-065326e8dd22 | -11.12845 | -48.30065 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10b27022-e9d7-3a8e-bf9c-eafaf5f4cef2 | -12.13199 | -50.74648 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea259f11-e888-3423-9295-db1dafad8f85 | -12.15178 | -47.36134 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd545381-ad96-37a9-999e-f10b408e4fb2 | -10.2794 | -49.95754 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92ad33d2-08b6-322e-b4fc-35dde824856b | -10.90939 | -53.94682 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5406293-1fcf-3e92-9f79-99b0daf3910d | -13.78938 | -54.06079 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 706a271a-d306-3d14-8c6f-a766d6c3cb9c | -7.64922 | -62.53883 | 2026-09-24 05:06:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c6d016-65d6-3330-91a4-ab44972b2997 | -12.416 | -46.9538 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f4c36a2-5935-3575-92c8-5f5c7439f67b | -12.11907 | -47.37903 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f21bbf7c-024e-38a0-b1fe-1f42c9a8ae1c | -12.92428 | -50.91794 | 2026-09-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86a402e8-19f6-34bf-9002-851b1b794a47 | -10.41006 | -54.41451 | 2026-09-24 05:06:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd06d43-fbbd-3515-b387-67bee0747260 | -11.48722 | -47.33818 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10690288-f6ba-33dd-8364-215a33e27602 | -9.49776 | -64.03828 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46404e0e-9e3b-377e-a9e5-832e6e048856 | -10.283 | -49.96185 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44c00e3f-5c29-393f-a3bb-35152bc9e2a8 | -11.64388 | -43.48834 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87b9ca4e-738e-3d1a-9f94-97402f6df763 | -11.92151 | -50.73822 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aeed6d17-98e9-3a2f-aa85-34194fd67e80 | -10.24678 | -49.98678 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53303692-00b6-3dad-b542-ec80e6cd1808 | -11.63099 | -50.61667 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe97fc99-12db-35a2-9e1e-21d12edf83f0 | -8.63068 | -66.99284 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c1d5402-c22a-36ef-8d9e-6d83739ebabf | -11.12773 | -48.30589 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a921c78-e6de-30af-b8f0-f9b094190d2d | -11.40361 | -47.39685 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dce9ec63-e938-33fe-bb92-41451048490f | -12.16154 | -50.76871 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e44146c8-db12-3236-add0-3e4450159fa5 | -11.488 | -47.33237 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7900042e-845c-3b87-b444-9bcaf33800ca | -12.12094 | -50.73769 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fff529dc-7659-3eb0-9d55-f352178cbfb4 | -14.56367 | -54.11688 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02a2d1fb-0a7f-3d62-9ed9-e9bff3579ea8 | -9.99479 | -50.23753 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a970edb3-2450-30fc-93cc-bd9e74ca2de4 | -10.14356 | -50.21876 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a05052-7864-35c3-ace7-7b64d91a1a08 | -13.7871 | -54.05262 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dd505c3-78a9-37a8-b33d-d0cfc85c55c4 | -10.72225 | -48.7455 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e45348fe-6e0e-3677-a062-7b31e7a383f0 | -11.79709 | -50.04325 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d795522-7844-3148-b0d3-3fa7d67790b0 | -13.46055 | -46.28357 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2546146-f94f-3b30-9f92-b420711dcdaa | -10.89251 | -51.52195 | 2026-09-24 05:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97433b43-68aa-3337-acfc-a55c2ee373be | -12.41484 | -46.96325 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0d2a7259-9c49-3a15-980e-094733d7dc03 | -10.65136 | -51.32181 | 2026-09-24 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72f0d4f9-7a4a-3c05-8389-378cd507b613 | -10.75447 | -44.82392 | 2026-09-24 05:06:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71611a99-60c4-3fc8-a7aa-92db54effcd6 | -10.27561 | -49.96083 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae969479-dda6-3b5c-9f0a-6bb02cc0f24a | -12.68926 | -47.02409 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfe81c9b-3adc-3837-8689-6b4e25d14785 | -10.28197 | -49.96926 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc6b5935-c79a-337e-901b-4d5feca67ed1 | -12.14389 | -50.7194 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c4ad2e4-8d7a-3e7b-a250-f3d3177a9e01 | -10.41434 | -49.35267 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 01a0f2d8-426d-355f-8662-503a2580e0bd | -12.4083 | -46.96109 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 774be208-ced8-3349-8d59-b94b98e424fb | -9.55714 | -65.98909 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00dea7ef-d2c3-30d1-a5dd-4c086a311cf4 | -10.10577 | -50.18903 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5a0aba61-3290-3354-9d33-ee24a84bc5d5 | -10.61961 | -54.00634 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36e28ba-1169-348f-8f77-658be3a79ce1 | -11.63148 | -50.61314 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a3da19d-7456-3a42-aeab-6a9f8fdd8ecb | -7.58056 | -63.46646 | 2026-09-24 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67bc9917-ca58-3fa9-a241-6171b1eb7021 | -10.71569 | -48.72658 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 738d17ed-14ed-34e2-94bd-24dc29c076b2 | -11.93512 | -48.22235 | 2026-09-24 05:06:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28f8cdff-217e-30db-8860-c94d90b96b0b | -15.24761 | -43.27095 | 2026-09-24 05:06:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c1da6a4-a778-3ac2-8b14-59ec7bfd6e20 | -10.4158 | -49.37354 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0dd12a77-332d-3439-9a34-e81664cb7a77 | -10.12648 | -46.06874 | 2026-09-24 05:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3fb2b63-2f62-349c-acf2-172fb3790248 | -12.77346 | -52.83986 | 2026-09-24 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18209adf-8009-3c94-9d71-575a0b7a70ea | -13.458 | -46.25804 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc29859f-1f7d-3498-9ca4-a288cca5f8ff | -8.92253 | -61.49549 | 2026-09-24 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86d9cfbe-67e5-364c-974a-b6784b27cc39 | -11.10988 | -48.29793 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43f1e8a5-ae68-3db8-80d9-1aeca05d0df9 | -7.89981 | -61.16794 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d632129-860f-384d-b007-c160a4157d05 | -9.55569 | -65.98576 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9779d30f-5c25-32bd-8a16-b1216dbaa551 | -10.1269 | -46.06552 | 2026-09-24 05:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6389862-1bb8-399f-8cdc-320f77a5809b | -7.89463 | -61.17158 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da1d118e-1d07-3d4c-9493-83b0d90be939 | -8.4934 | -57.60532 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1430506b-da5e-32e3-a285-14a81e81a668 | -8.62433 | -66.99158 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 863774a4-f0ea-30fe-be34-abcadcacd2b1 | -11.1316 | -48.31222 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 198d76e7-2680-3ddb-9de3-536727643b71 | -10.70621 | -48.72912 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f66a292b-9b96-37f8-ac63-53c7243d7edd | -10.24997 | -57.72394 | 2026-09-24 05:06:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6643a8f7-a285-35dd-93a9-ce0add6b59f5 | -10.71514 | -48.73063 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4df4c5-fd50-31f8-a66b-9f70a0b9de18 | -9.18772 | -65.79214 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc285f2a-c4e2-3bf9-a6ee-920d0ea6abce | -12.10308 | -50.7357 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35668cc7-62f3-38fc-9d47-9c0efa238808 | -11.43252 | -44.20267 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc731d92-eaac-3772-8e3d-6b581655af10 | -13.9306 | -47.82991 | 2026-09-24 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d8edcec-a26d-310b-9236-b91156faa074 | -10.61399 | -53.99804 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d17cc95-db4b-3890-89c6-0ed04706596e | -10.74343 | -46.29189 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00753f53-e423-350f-90b2-ed447ee67cd7 | -10.6168 | -54.00219 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb55c102-25dd-330a-8a5d-5f4ade440c91 | -11.9975 | -52.46166 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c43d8b51-bf03-310d-bc30-2a24593587ea | -9.76362 | -64.29624 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193211fc-2bd3-3c11-a52e-85033c9902f1 | -10.91166 | -53.95465 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47f14d9c-5d7d-39b0-9345-372076222871 | -8.49981 | -57.61048 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6444062f-a3cc-3fba-ae46-2ec8a4061230 | -12.16575 | -47.3722 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d57ef0c-3554-3e64-afd7-6b903e0455a9 | -12.12798 | -50.7459 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc3f475e-4912-3a23-b427-d6f658bc094c | -10.27259 | -49.95281 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e6a427-ee04-333d-945e-231b1f8ee8a6 | -12.1434 | -50.72294 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e02e5c02-4e6d-32bd-aac9-900a89cfc97c | -11.40433 | -47.39129 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fd778e8b-2071-3e71-b418-3b003142cc3d | -12.1435 | -50.75174 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0700d21b-d734-3994-86d7-b3ba056790d0 | -11.40856 | -47.39765 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d9f88a5-03c4-398f-86e4-2b2c43408d42 | -11.9255 | -50.7388 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f9bac5f-d28c-3a14-bdd4-17c23a40a5a1 | -9.19235 | -65.79231 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0be4b172-4301-3953-914f-21e110144fd8 | -10.90435 | -53.95724 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7bcbf92-9f2a-3a84-b609-fb7bea7b2f2b | -7.89388 | -61.1759 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd569928-1b66-3852-b9ea-5dd7f761bffb | -10.97469 | -54.09498 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02232b6c-d466-38e3-a169-0a1216da642d | -11.92949 | -50.73938 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0e3cf2-c52d-3275-b7b9-b5e3bc156460 | -7.88504 | -61.17447 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 414a6bd9-de3d-30df-b8f4-219f413ffb46 | -13.07178 | -43.28686 | 2026-09-24 05:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5ff409e-c903-3919-ba37-6533e4533bee | -11.98725 | -52.45581 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abe4b205-f18d-3790-93a6-5ed730207fb6 | -11.59419 | -58.51299 | 2026-09-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 605b3452-7901-3333-bfbf-8606877803d4 | -7.90056 | -61.16365 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a5d032a-d7e9-3a80-bf96-f368ed108b28 | -12.00788 | -50.32352 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README77.md)
