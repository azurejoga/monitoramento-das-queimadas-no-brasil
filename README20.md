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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ddb3c9d-8524-3313-bcd2-3066ba912e40 | -6.87613 | -43.59605 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf075d17-7077-3203-a2bd-af024815ec30 | -6.86464 | -43.61507 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01bb2c5-2651-31fc-a7c6-5f15471086ba | -6.81583 | -44.36211 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd72695c-6900-3749-999a-654cc071497f | -7.67358 | -45.00305 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09e2ecde-8588-37f4-bb46-62aa8cc49b7c | -6.07908 | -43.99366 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 672292be-3b37-3f51-95aa-60e3603e4465 | -4.79769 | -47.25787 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 121605ce-9729-3883-b9f0-5ee40c10081f | -8.09683 | -45.00779 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ae200e1-91ee-3d10-9939-c2ae797ae5b4 | -8.44297 | -43.67055 | 2025-08-28 03:45:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eb8acac-90cc-3ee9-a5b2-07ebe044920c | -6.46006 | -43.72412 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d196cbe8-0dd7-39bd-abba-39ee2464b106 | -7.3186 | -46.1144 | 2025-08-28 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d63059e-940f-3286-a24a-f147c599ad17 | -6.16838 | -44.06705 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05f67976-eb5e-39aa-9bc8-7f1d3455b961 | -7.34728 | -35.09611 | 2025-08-28 03:45:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aecf5f57-d8af-375f-84d3-cb1fa439351c | -6.4452 | -44.57497 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b7aafa9-c748-3dda-a2f0-7f7bb19b3854 | -6.8815 | -43.62477 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3f2ef0fb-6046-3ed4-b5ec-ff1829ecb505 | -6.88258 | -43.61867 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2da78faa-0fba-38f6-8793-e65d9eeb2268 | -7.64318 | -42.6691 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd68af1a-e6b1-3fb4-b208-991c5094d9bc | -7.07139 | -44.36414 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81b7ed02-6928-39b3-9027-0feb32705b7a | -6.86569 | -43.609 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed0786c3-a2c8-31af-ab33-fb1a9175f524 | -7.4269 | -40.08321 | 2025-08-28 03:45:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 44616b98-4d5d-3bbf-b7d7-27f0d67dbeb9 | -7.436 | -42.04949 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f1fc858-db4e-3533-84f6-d5e74a15e70e | -7.90092 | -44.77775 | 2025-08-28 03:45:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3fbe3f4-a39c-31e2-8408-22b4d5ae4e83 | -6.87157 | -43.59229 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f36666bf-47fb-315c-b61f-ad641f87fc10 | -5.23006 | -39.37383 | 2025-08-28 03:45:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| acfa406f-e717-3574-b4ef-1f763f25bf5a | -6.44031 | -44.57072 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca2840b6-ee4d-3f2c-8443-fdce0befba26 | -6.87402 | -43.60788 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d00708d7-897e-32db-8b6d-a38a2e4fb4f1 | -8.29053 | -47.21305 | 2025-08-28 03:45:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26adc651-b667-3406-8972-82f61caacc21 | -7.39504 | -39.6997 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 400887bd-9088-3b51-bbc7-c630293d5534 | -6.86784 | -43.61312 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| becc8bbe-41e4-3019-b8f2-3dcf1d2896bd | -5.68308 | -40.98015 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 667942ce-045e-31b6-bf86-234c6eb8034c | -7.06609 | -44.36302 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acd2e90d-f498-3ec9-bf04-db7f78173d11 | -5.54342 | -45.37327 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3c0ce27-3c39-31bf-a85d-f4830e0ff414 | -8.24356 | -45.07165 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cd62b7c-87d7-3621-ac2c-c67e060c80ca | -6.87965 | -43.60568 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8e329aef-8f95-31a8-9268-088561d4c580 | -7.39973 | -39.69547 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 71061ae6-eaf8-3b9c-b20d-7d908dec8121 | -6.13695 | -45.07553 | 2025-08-28 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06527371-541a-399d-88b9-98228971ca3e | -6.16505 | -44.40165 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aba5c9e-4f9a-3e4e-b135-d4aff8886bf9 | -5.23399 | -39.37449 | 2025-08-28 03:45:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40576ff3-fbd0-3ba4-8fac-e289b7b7d3dd | -6.43543 | -37.13291 | 2025-08-28 03:45:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2a20b252-4329-3f8c-987a-426006f47fa5 | -7.41896 | -40.08181 | 2025-08-28 03:45:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4ab52d09-7382-331e-a272-d360af16ae82 | -6.44157 | -44.56359 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdd8c675-1e61-3c26-becd-9b44721a4af7 | -6.17818 | -44.01167 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad49fbe3-f19e-3408-bb19-5e23b46a570d | -4.24427 | -41.89982 | 2025-08-28 03:45:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d0c814f-68ab-3be6-91c8-49faa9c3e117 | -6.71947 | -43.0955 | 2025-08-28 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6367d01d-b277-3a49-a092-d253dcde05f3 | -6.8842 | -43.6096 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 2b9b911f-bec8-35ee-a19e-49c11e3b32f0 | -5.41734 | -41.14679 | 2025-08-28 03:45:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf0988b0-f400-3a66-a985-ccbe525512be | -8.3858 | -44.9762 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 877b4f3b-ad3f-378c-8539-f007a7cf54c3 | -6.81031 | -45.00209 | 2025-08-28 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2d8974d-111e-3ee5-8189-4dabd2879115 | -5.75004 | -40.44409 | 2025-08-28 03:45:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4e6e2b5-462b-3775-a192-c41650a8e775 | -5.77771 | -44.92712 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c62fed6d-2be5-377d-8059-19ff58608a88 | -6.87803 | -43.61481 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b669145f-04a2-3842-b781-c18c8b972ac9 | -7.08324 | -43.64199 | 2025-08-28 03:45:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7641b09-4bce-33a1-afde-9d6a5d3b5e36 | -7.65512 | -42.65611 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e005066-ed28-3a0e-bea1-5b6e24f836bd | -6.80568 | -44.35707 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e279a302-9366-3c8a-9203-73ea28cfe4e3 | -6.36963 | -44.05241 | 2025-08-28 03:45:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ad97c5e-2b9b-3a34-8848-58368e093630 | -6.13367 | -44.42101 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84386de8-12e2-3bec-8e8e-8181a84650a9 | -6.57027 | -47.38357 | 2025-08-28 03:45:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71259eb9-c860-3716-a501-8e8521cb6d45 | -7.39278 | -39.68928 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 78.4 |
| d5879b8b-6eae-3c89-8722-f4961bbf7eb5 | -3.73213 | -40.27147 | 2025-08-28 03:45:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76e7cca5-d10f-31ce-83f0-f3fd621bee48 | -6.858 | -43.62325 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7adf541-bb2b-31a7-ba90-4b31a12b186c | -4.15476 | -43.88415 | 2025-08-28 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 887b1f34-8bd4-33a6-969a-4bbdad9b45eb | -7.71847 | -43.96682 | 2025-08-28 03:45:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 844d315e-de67-3053-8312-b7b3ade8817b | -6.87023 | -43.62908 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2802f33b-fbf1-3d48-adb3-f791e46d77cc | -4.29263 | -40.93909 | 2025-08-28 03:45:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90ce81b0-a278-387a-b605-10e2a51be20e | -6.29975 | -42.50652 | 2025-08-28 03:45:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b424ddf5-5e57-3f92-96dc-4b9748a8ee1b | -7.25952 | -45.35975 | 2025-08-28 03:45:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 750699cd-bd49-3bb0-8b71-83d4c7617131 | -6.19588 | -44.16045 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4dd9313-30f6-3729-9589-eaa871b1a2f8 | -6.87185 | -43.62002 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 75e4c8d1-db36-3add-a367-4fc6e0c10fbf | -6.43848 | -44.58113 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 13654146-b643-399a-88ae-3fdafe4e9fc3 | -6.88713 | -43.62263 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c6df17b-c935-300e-a99e-d9a3bfd2347a | -6.28288 | -44.47448 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d90acd4d-620c-315f-b212-fe5c431a9fee | -7.39115 | -39.69904 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 37.0 |
| efe5bee0-bb08-34a3-b607-f34b4d83d107 | -6.86165 | -43.61836 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88f3ed12-47d0-38d2-bd61-7d7332982f97 | -6.16363 | -47.2773 | 2025-08-28 03:45:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eeeda615-6803-3276-bb53-4e8d1cb8ce69 | -7.62769 | -42.70236 | 2025-08-28 03:45:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35290307-9382-3d6c-960d-0bcbba325610 | -6.17425 | -44.0648 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b59771e-57b2-3b68-a979-bfa0fe581540 | -9.19381 | -44.43952 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aea03c4-e843-3b2d-b07d-110c871f0a33 | -7.42293 | -40.0825 | 2025-08-28 03:45:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 43616890-6a84-3155-bc4b-10ca0558c52e | -6.57675 | -47.38491 | 2025-08-28 03:45:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f16f6485-15f1-3b3e-8462-2dfc9d42d7f6 | -5.8182 | -42.60538 | 2025-08-28 03:45:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bb351be7-3204-349a-bdca-dfa20260e306 | -6.19049 | -44.15985 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 113981ca-b1ef-3856-9ff0-7fbb1d38383d | -6.43889 | -37.13347 | 2025-08-28 03:45:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d5879c10-2101-3d8a-9367-04b4b437f10f | -6.88528 | -43.60354 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1ceb8916-ba18-3a64-8588-784fca5bab3a | -7.27072 | -36.1537 | 2025-08-28 03:45:00 | NPP-375D | BOA VISTA | PARAÍBA | Brasil | 2502151 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0f85ce09-4652-3ecf-9f5f-872dd293c1e9 | -6.8662 | -43.62222 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebb3a0ee-fff6-3c66-8b7f-fba3d014ac1b | -5.20069 | -46.0699 | 2025-08-28 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47cde1a3-3247-3103-8568-fa9e5804b5ab | -7.39197 | -39.69416 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 37.0 |
| cba440f7-3f1e-3e29-b1eb-155900e4389c | -4.79328 | -47.26279 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8b1ff2f9-b74d-3846-b936-0a26e10485db | -6.15528 | -44.04846 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e232d7c6-bdae-38fc-9a1a-369de482dd06 | -6.87666 | -43.59309 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b869746-f983-3735-8387-41c24674db4b | -7.42916 | -42.06219 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e9502b1-e613-3803-b194-f4f2670100ab | -9.195 | -44.43663 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f140f05a-0f2e-3228-9636-b75b1b48188d | -3.23484 | -43.44065 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1677192-b23d-3337-97a6-cf767da8ae6a | -6.28226 | -44.4779 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e55f2a08-ac62-3db0-bee6-79392052fdf7 | -6.86257 | -43.62719 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e9043c3-6284-31aa-81eb-004b115e6b24 | -7.4254 | -42.05687 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5cdc2b62-a87d-3282-a84b-c4e554eb44df | -7.00019 | -44.40932 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930df4b2-077a-378a-8873-fe254aa904e6 | -6.22188 | -43.35833 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93ebb2de-70dc-3e0a-9efb-e04b27fecef1 | -8.436 | -43.68093 | 2025-08-28 03:45:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7afe55ab-eca6-37ea-807e-2c0f465a785e | -7.66148 | -42.65551 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55382628-85f3-3c5a-b7f0-7ff6f929a6af | -8.457 | -43.70473 | 2025-08-28 03:45:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README21.md)
