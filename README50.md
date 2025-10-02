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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dde53943-b2ce-3de0-a8d9-cfc9ceba60a9 | -13.36109 | -48.12144 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eb1a4bb-d00a-3f99-aa49-394ddd4b2be6 | -13.07649 | -47.09142 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4bc9312-6333-33e7-b65c-e5c096fb242e | -14.71578 | -48.20721 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c736ee-4ca1-3987-bedb-2e837105eff7 | -12.68541 | -48.57201 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3076b5b1-a057-3c90-83c9-dd332bba7c4c | -13.18259 | -47.8348 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9639fcb3-b3b4-321e-8e90-90cdbb36f771 | -15.43068 | -44.99566 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66d77354-caab-3fdb-9c63-4154cf1d800f | -14.34303 | -47.1322 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed05abe9-092f-3866-a298-f49d2770f797 | -13.78136 | -48.00389 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cab2691a-fd82-34b8-95f8-42ecce7a636a | -13.79058 | -48.0597 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6da125b-b982-31ff-905f-3bd94d417268 | -12.67532 | -48.57549 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 31891624-38aa-3428-9a38-e5ddbf33dd53 | -13.46168 | -47.23292 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77b09404-34bc-3581-a625-713c7808f5cc | -14.10727 | -45.63929 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3abdfa23-2c82-3984-84b4-eec32ba85628 | -15.29478 | -45.0878 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b0122046-02f0-3fab-b6b6-1a82cc979a5e | -14.21363 | -46.12184 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 33e58024-ece1-36b6-a5ed-b8df8f6e5903 | -14.90302 | -48.32652 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44fd3cd8-1e4f-3f29-a5a4-ebc0b3c563af | -14.30846 | -45.89032 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dbeca28-bb08-38be-8462-f35072c7d87c | -19.62924 | -44.89747 | 2025-10-02 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3d6a91dd-7059-3957-9efc-2666532fcb27 | -12.76452 | -48.252 | 2025-10-02 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb3c267-e299-3ee8-a24e-57b97053f021 | -14.98228 | -46.91879 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f88c71b-4953-36b9-8a8f-b24f79f08b53 | -19.46046 | -43.65806 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d248377-4d25-30f2-bef5-72400ed21c78 | -14.44188 | -46.34844 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39976286-d2b6-375f-aa00-26bc2cf44ff8 | -13.42105 | -47.79602 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b08a593a-6b5a-3708-9969-c26b6429d1c6 | -14.67937 | -49.60864 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42e6410b-02d3-3e41-bd73-2215f7d156cf | -14.86406 | -48.39188 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 893c3f35-fc53-35c8-aa38-6e5bb06731b0 | -15.11784 | -48.49068 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028c0e87-2139-3662-bd65-2ebb287a26a4 | -13.5193 | -47.25718 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7141511-52d2-349b-a968-734b8367cd36 | -20.19233 | -46.01755 | 2025-10-02 04:04:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5ca22c5-3078-37ad-9be9-1cc6ddd3445b | -20.22211 | -43.89776 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f147b37f-f640-3061-a270-096293b09ba5 | -15.01856 | -42.22171 | 2025-10-02 04:04:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e7e2dc5-d92c-3204-8397-5d063d865707 | -13.75835 | -48.00766 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68712546-fc82-3d7e-a0a7-15ed0d7d0841 | -13.17025 | -47.82915 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e442b0fa-234b-3fad-b406-b86c9adc804f | -14.3764 | -45.96931 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc42966-ee60-33c8-b889-ab6e26f02b81 | -12.49472 | -50.25975 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a04c4ca7-82ba-3018-9b5b-85bb2621f40d | -19.96185 | -43.6518 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b17eee41-5917-314a-8eb5-9112296c0eaa | -13.08398 | -47.07288 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c8443dc-1374-336e-bd99-2d459fe4c2d3 | -14.59354 | -48.33488 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5438b73d-4170-3221-9f21-9234a56fcaef | -19.01009 | -45.00183 | 2025-10-02 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3b82323-f7ff-30a6-96ce-22436029a626 | -14.40376 | -46.10199 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9905eda7-7677-3bbc-926c-4dc25c569ef8 | -20.2172 | -44.1825 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ffb97468-664f-32dd-84bd-e9d7813490f4 | -14.21744 | -46.12255 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5c2158d8-fc4f-3078-91bb-24aa3369f43e | -14.70361 | -49.61609 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 034a83b7-7364-39e6-b08d-83942ec71706 | -15.42952 | -42.7625 | 2025-10-02 04:04:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36380585-b5c5-31a4-9213-57e7dee05026 | -14.67908 | -49.61617 | 2025-10-02 04:04:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 31101a48-0619-39f8-8390-c11f55d7be06 | -13.68078 | -48.08817 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 260e68f7-1ff1-38b3-9d93-583edbb817c3 | -14.00821 | -44.97585 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8902a813-c2f5-3c42-b514-8f4f6e47b17f | -19.45861 | -44.27662 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe09749b-07a5-33a8-aa9e-70893175059a | -13.14721 | -47.8475 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3a795f6d-9c71-30cf-9483-a5e96bd0b205 | -14.47591 | -48.42773 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0a2e6278-ea2d-316e-a966-3198f9041059 | -14.48421 | -48.40697 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c99794c-d7af-3ae6-b706-4e28f71268ad | -20.23145 | -43.90318 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 46ad9bfb-3379-3552-99cf-c0c33cdfee18 | -14.92183 | -47.22789 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c07976ff-7bf9-322f-9460-e9f4f7d633ae | -14.36885 | -45.96799 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26e20271-b1cd-3990-a922-76edc4085383 | -13.6724 | -48.03673 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7250ff6b-6a47-3e85-a35d-d0c87af0bcd9 | -15.63274 | -46.2492 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cb320b4-df13-3cca-8d76-8a88e121889d | -20.70767 | -43.28212 | 2025-10-02 04:04:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 82193e16-29ed-3739-a0fd-7cb60531b0f3 | -14.68563 | -49.6077 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec0c3106-0f86-3ba9-9424-76755a0f2619 | -13.64519 | -47.18774 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07bc8e5e-e60b-3ee4-a619-a357466e777d | -13.82629 | -42.44155 | 2025-10-02 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7399fed5-3e63-37d5-88c2-168eacbdd8de | -16.36845 | -47.05515 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89623cc1-4bfb-33a5-abef-33b04e5d95b9 | -20.1881 | -46.02105 | 2025-10-02 04:04:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d3132b4-930c-3236-a161-adcfd790cfcd | -13.16284 | -47.80996 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34ab5314-53b5-3e00-bc9a-0211bc0d394b | -13.91048 | -48.07397 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d93e041-7daf-3bdf-a825-a0188a42fff5 | -13.7774 | -48.05082 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 81f732d6-456a-31a1-aed9-c865b45f54b0 | -20.21289 | -40.28265 | 2025-10-02 04:04:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51093c77-1f68-3e0c-80d1-febafb365a88 | -13.86516 | -51.24817 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf0106de-1e01-3d86-9584-ba3e2e9091d1 | -14.04231 | -47.99831 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21fdf09e-d767-3a32-a9f9-0d12873788fb | -14.35618 | -43.83558 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 841381b7-fcb4-3450-a1d6-7b052fb4a3b7 | -14.64323 | -48.14233 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef6c2a9e-a166-31b3-a673-bf0f53978829 | -18.84386 | -43.14623 | 2025-10-02 04:04:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d8bbf938-2132-38b3-91de-2638a91b103f | -15.75932 | -43.66906 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7788424-feb1-3582-8021-08e9fda71bdb | -14.21039 | -46.09518 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd375838-891d-3849-85d8-30cc5e1a62f9 | -15.93654 | -43.33577 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91aec237-984b-3b57-b81a-7b0ebf91cf75 | -17.17087 | -47.0242 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f13a2bee-ee4a-3060-8d18-31bb2362b2dd | -15.93477 | -46.21327 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 869e60c1-fb4b-3e03-9a8e-7501b0fcd095 | -16.03671 | -50.8561 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8ef45c9-f69b-3d58-9a4c-c9446f42fd3f | -14.70713 | -48.2058 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f905199-4478-3b85-925a-1981d6e167b6 | -13.42457 | -47.80096 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 417cbea9-3524-3603-b7b0-ab3edcd6a4a1 | -13.53814 | -47.24729 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9386b4ba-7cd8-3ad8-89f7-a9d5ef08eee5 | -13.31589 | -47.19986 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f40abacc-2288-30da-846d-39e2ec1b1f4c | -19.26134 | -47.353 | 2025-10-02 04:04:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a15bf76a-1361-32a8-b511-b9420a1a4d1d | -13.31185 | -47.1986 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8743af45-e6db-3efd-831e-0fdf0e0349d6 | -19.57643 | -41.90086 | 2025-10-02 04:04:00 | NOAA-21 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 23f324df-6331-3ff2-88c6-4507274004fd | -13.7565 | -47.99321 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1b803c81-b871-3a13-9bcd-90a0c0436a8b | -14.70484 | -48.21836 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e0b62d-9993-3362-ae70-35d1f538adca | -13.17743 | -47.80296 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| efdebf17-4206-3c06-b529-8d84370eba9c | -19.86283 | -42.58802 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d61a5459-fd1c-367c-81d5-e72ba25cc977 | -14.2179 | -46.09715 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b589758-4378-38f2-bd90-e089482e7694 | -17.11425 | -47.11654 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6f49500-5a56-3141-bba8-37388286f467 | -13.16749 | -47.83387 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33b0f277-a72f-348c-822b-2ba78ef33e12 | -18.90668 | -48.06855 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13a2bfd9-d7de-34c5-b906-131ed270a18c | -20.23086 | -43.90688 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 12e553c5-cb3e-3ed4-a49b-25c3c4f46d36 | -13.14642 | -47.85189 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7a4ce9c7-b623-3777-bdab-782ca90576f2 | -13.53694 | -47.25399 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 977259f2-2989-3a07-8b13-c60363ec05dc | -16.33895 | -43.52134 | 2025-10-02 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41a5378e-6b12-322a-975e-024097621c75 | -15.99531 | -50.90707 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 51284fbc-a686-376e-85c5-d29f3184ff94 | -14.80051 | -46.96617 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ece824cc-8dc7-3f4a-ace0-9361fe486362 | -13.68221 | -48.05637 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ddfcd9b4-53d3-35ab-a8f6-9d7a8aa39d1f | -15.40783 | -47.04723 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fe9e223-9390-37f6-ae74-0185b999067a | -19.02139 | -49.75153 | 2025-10-02 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd57f675-8477-35e2-b6da-8ff90de6d523 | -15.94321 | -43.33693 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README51.md)
