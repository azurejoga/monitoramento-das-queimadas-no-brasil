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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28cf0351-c0b2-335c-875a-4ac27e3d6b8d | -12.52616 | -47.09624 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8a6a72f6-8d94-35cb-afdb-a84e68ed83c5 | -9.18515 | -46.76934 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e75de28f-ed67-3f66-b25b-1e73410dc6bc | -13.24887 | -46.90728 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| da42e4db-fddf-3512-8e1a-df097e143c59 | -14.80417 | -48.56258 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14b3d3ee-8268-374b-9b60-3cf9a1a7cb28 | -12.16239 | -46.98639 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85d9604a-e86c-3126-902f-94adea57ab2d | -11.31478 | -46.76368 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0954e2ac-f9f8-3e7e-a7f1-d7cb7d8e42b1 | -9.73744 | -46.12705 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1589b5b-6124-3007-8f36-4709a9354831 | -11.33646 | -44.01676 | 2026-09-18 03:38:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88148164-75ba-3b76-871e-0dff9585cd82 | -14.80274 | -48.55472 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65f0c649-ebd2-3d85-b5f7-5a9d401d6cc5 | -9.39306 | -46.8521 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd70dce9-7452-315b-baa0-6051df63b104 | -9.90591 | -46.56136 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 862038ae-00f6-397d-962d-0481be1a1c1b | -9.0898 | -45.72028 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08d3c6af-8c2c-3e39-9015-d81f62ee8637 | -9.10022 | -45.7202 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e75e9d7b-346d-36e8-98af-c919c0447df3 | -11.27819 | -43.51761 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86257636-2bfd-3003-8483-78afba716a9f | -13.40574 | -42.27997 | 2026-09-18 03:38:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ac11217-8639-3cab-9fb0-c77970280956 | -11.52109 | -46.87259 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d825d522-4968-31cb-9dbd-23bae78d4c77 | -10.54641 | -44.85167 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4731aefc-524f-36d1-8cb1-d8914deb1c12 | -12.52817 | -47.09006 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e1381a00-0ce2-3a3d-ac59-b69652e02a5b | -9.24144 | -45.91724 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f26dbbf0-9866-317e-96cc-37c550925dc2 | -13.23429 | -42.33778 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 4486c024-d1fe-3407-9da5-971fec815da5 | -10.6068 | -46.55581 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4788bed-9769-3f01-9637-21ce94ed05d8 | -12.52956 | -47.08364 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3c4c52af-3917-3fb0-ad78-1890bc94aebe | -9.24459 | -45.91388 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84ef5027-31f6-384c-b59e-66e0cdee924a | -9.59605 | -45.85331 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6babf4ce-18ca-3419-b068-268dffd42737 | -11.29861 | -43.38266 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3980bb39-bab9-3a73-812c-d0db4306dada | -11.29712 | -43.39034 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab372cad-fa60-3a66-8137-3e746d84c38b | -9.75552 | -46.09752 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 33e22601-0215-30e8-a1b3-425a2563f4e5 | -12.67827 | -43.91677 | 2026-09-18 03:38:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5426738-1f8b-3c86-afe3-1ca84cd7b67e | -14.801 | -48.56256 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feae4771-d646-3801-85f7-072042d0cfdd | -14.88995 | -39.90272 | 2026-09-18 03:38:00 | NOAA-20 | FIRMINO ALVES | BAHIA | Brasil | 2910909 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b55fc5a9-c89b-3a0a-ac70-37a938528da1 | -14.95759 | -47.53589 | 2026-09-18 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecfb8384-ac99-3197-8c43-00fa667d49dd | -14.80205 | -48.57185 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82b8c94d-9b03-3e7d-941c-ea12f39198ce | -9.95016 | -45.34146 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f988a0-fa62-3d0f-beb3-800df890032f | -12.78275 | -47.56856 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4ad4ab7-8f21-3720-96a3-688b872e369e | -11.89142 | -43.81778 | 2026-09-18 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76b7c23e-f0e5-39ec-8683-f0a9beb8e18b | -12.52677 | -47.09652 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 64411c18-0739-38f1-adf3-e10ef2de6d12 | -11.33052 | -43.39708 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c791c406-051d-3ebd-af2f-fd30d4746714 | -11.51868 | -46.88497 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 21218146-0969-3b36-a5b0-64efc13f2f02 | -10.11674 | -45.65199 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dae52105-c038-3c8b-9d6d-00229b94dfa3 | -11.27713 | -43.3742 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65058a8d-81d1-3edc-8b09-42df85354538 | -12.16508 | -46.97692 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f15fb6ae-3efa-3085-843e-eb803769858f | -10.54226 | -44.84745 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52cdcd7c-efe7-3dfa-80a8-eb5d51d5f97b | -13.64576 | -46.93689 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78630439-a6d3-38cc-b4cd-9d72460dc767 | -11.8809 | -47.57838 | 2026-09-18 03:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68bc457a-8436-38b8-8249-60ff17c29df8 | -10.11901 | -45.57254 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dfd8dd2-3da7-3608-9981-ae2a64f32e1d | -11.33578 | -44.02148 | 2026-09-18 03:38:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82693902-f8f2-36ee-aa48-22552e910099 | -9.39869 | -46.86081 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 749d9521-0490-350e-bb04-c5ff0c4f5d84 | -11.25126 | -41.90603 | 2026-09-18 03:38:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b65c3483-adc7-3b38-ae9b-7fe35e20ef12 | -14.96196 | -46.24471 | 2026-09-18 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b2e67a3-08bf-3743-8e1b-8906ba22b721 | -13.69557 | -43.62305 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 194acf51-9da3-3b31-834c-6ab427909278 | -11.2827 | -43.37531 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0838f2d8-2e78-3e61-bd1b-9fa4f4111d59 | -9.76992 | -46.60291 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7534d41-6470-3e46-b899-0b95c49c5c46 | -11.22743 | -43.43136 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be265f05-5d10-309e-a0a0-ea8f7757e94b | -13.34439 | -43.78154 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f413e671-f85c-37a7-800e-bca740a73e13 | -15.56475 | -46.4584 | 2026-09-18 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d99430fa-7d2a-3b5d-9f72-393eff820dd7 | -9.74524 | -46.58207 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24004d86-41a5-371a-8d09-606a46b51cbc | -10.1151 | -46.30272 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d75c1178-e7f8-394e-9abb-d3235b6760e7 | -9.59799 | -45.85973 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c3dfc42b-2ff8-3a93-a0e4-1068db123ace | -13.2252 | -42.3414 | 2026-09-18 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 127.4 |
| 3498377d-3ae2-36aa-91b5-d0a0b841850c | -19.2015 | -48.7675 | 2026-09-18 03:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d60cc671-d4c0-33ff-be48-b8a0d3e9ed82 | -8.8921 | -62.4297 | 2026-09-18 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6e23e193-47c9-383c-ae60-db1387f78a40 | -12.5497 | -50.7332 | 2026-09-18 03:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 123a63e9-0362-3857-9a36-f612e9f78149 | -2.6125 | -54.7577 | 2026-09-18 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 8f0dfa8a-f75e-3d25-b570-99a8aa74ba4a | -19.1812 | -48.7717 | 2026-09-18 03:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 137.7 |
| c4f287e6-12b8-31ec-a327-93a4f0f3e28d | -9.699 | -54.8176 | 2026-09-18 03:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| aff6142b-2d1c-3100-9a5b-e6505d6d455a | -8.9107 | -62.41 | 2026-09-18 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b7b9c115-f390-36e0-b03d-bbb8d341b5ce | -13.2451 | -42.3133 | 2026-09-18 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 2e08f748-c4a1-316e-bc5c-383b226666f6 | -13.2446 | -42.3377 | 2026-09-18 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 114.5 |
| ed437ac6-9b40-3c05-917c-7496e088350d | -8.8922 | -62.4107 | 2026-09-18 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3593c731-59d9-3675-8250-1842a49cadbe | -19.2009 | -48.7904 | 2026-09-18 03:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 27cb8b35-2445-3f82-ae10-03061b7b1abe | -9.7175 | -54.8365 | 2026-09-18 03:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2d90e787-d465-3535-bf7f-ad29d1cefd12 | -13.2257 | -42.317 | 2026-09-18 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 5358e6b6-0d57-3499-960e-bf2bddba994e | -19.1806 | -48.7946 | 2026-09-18 03:40:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 276d3267-f928-327e-80ef-0f5d9cbb17b7 | -12.3015 | -50.7417 | 2026-09-18 03:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 12b6654f-cf58-33fe-aac0-186adfbdb228 | -9.7177 | -54.8162 | 2026-09-18 03:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 309db6cd-9ede-3ab8-b2a9-ac9895c00e74 | -19.18786 | -48.78933 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2fc70fc5-309f-3b9c-af90-52ba41376ada | -19.17978 | -48.79391 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 9a90954e-a6b1-3fd7-9fae-792dc20353ca | -19.18402 | -48.79073 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 50ae4260-ad2a-357b-889e-f108eb664d71 | -19.54849 | -47.64018 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f0459c69-991f-3916-9c20-7dc23a1ba684 | -19.17459 | -48.78621 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d6d9b3b6-cfc1-3ad2-bf5e-72efbf3aa908 | -17.77301 | -46.47652 | 2026-09-18 03:40:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c65c038-3997-33f5-9416-25a09df9de18 | -19.54965 | -47.63512 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ab07113-7e2e-3a19-8dc7-31893b35964b | -19.17751 | -48.77375 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9edc168b-8582-3369-8a4d-f5cc86639cc9 | -19.18037 | -48.7768 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ae5dd988-9f3e-34bc-9c40-05621d637068 | -19.1812 | -48.78786 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 85f88702-de73-3fe6-959a-fc2d7ba7ed71 | -19.1841 | -48.77551 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 97ab1c76-75e8-3e61-a6ca-7b96eadf8864 | -19.17887 | -48.78305 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e2642e28-6151-3235-b83a-84dc584c503f | -19.54971 | -47.62579 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5107ce7d-1d0b-3992-8408-96e0da28c103 | -19.17738 | -48.78921 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2ebb9b05-9849-370b-9b23-37cc0f2e8e19 | -19.18929 | -48.78322 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a404917a-edae-3a77-a726-68225d175b70 | -19.18551 | -48.78457 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8896abb5-eae1-3def-8995-ef9d0901d8ba | -19.19068 | -48.79218 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 837000da-361d-3619-9527-3c9863ab03f6 | -19.55219 | -47.64297 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 54a6fd13-028c-3987-836e-89c46bf6019a | -19.55453 | -47.63302 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4cb60fe7-76ef-3779-ad0e-686ceb5a4319 | -16.99798 | -45.46972 | 2026-09-18 03:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18f20a4e-44f8-3239-b0da-65a4bb3f9369 | -19.18698 | -48.77846 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5085fc0a-7bac-3141-a895-64629a07e497 | -17.77087 | -46.47743 | 2026-09-18 03:40:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c2b6074-f0c7-3859-9503-a1aada555089 | -19.55079 | -47.63008 | 2026-09-18 03:40:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7e73693-bf8f-3294-9608-69ceb12a3bcc | -19.18182 | -48.7708 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a7043bdb-9157-3a3a-9c61-3538938afdcc | -19.17605 | -48.77997 | 2026-09-18 03:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |


[Clique aqui para ver as próximas entradas](README29.md)
