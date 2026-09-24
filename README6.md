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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b284f3d-d62e-3483-b3da-b9afa5639ab2 | -12.1557 | -50.715801 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ceb43ba8-27c1-3971-93ce-fea63a2da9d7 | -9.8433 | -48.509998 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1af944-83a5-3c05-91bf-2ccb3dad8d46 | -9.234 | -47.354099 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e715feae-839a-3785-a167-5f9fb91b84af | -7.024 | -44.6567 | 2026-09-24 00:16:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b129ab8-e391-337a-b37d-b92060bf0e55 | -10.8805 | -45.076801 | 2026-09-24 00:16:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c22617bf-6ddd-339b-b5ab-e69a0f5a4a9c | -9.2262 | -47.364899 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37a4092e-996c-38a9-bb30-4912f62ddfce | -10.0816 | -46.005901 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36d3fbfc-777b-3278-a723-dc763fd8292a | -5.8459 | -49.878502 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a405fc-3853-3340-99a2-e0e29b30324c | -9.1533 | -49.9585 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c6e89d-c6d3-3960-9bd9-0f2825192a1c | -10.2752 | -49.951 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52c71e4b-ba42-3950-a308-edc82f4cbfe4 | -6.4279 | -48.462799 | 2026-09-24 00:16:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cd9d8078-b811-32fc-9216-00a59023d099 | -12.1619 | -50.743999 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5461908-c18a-38cf-afbb-ede94aa28b37 | -8.912 | -43.862 | 2026-09-24 00:16:00 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e903f46a-4b33-3cdd-8687-8a7ab192b54e | -3.0387 | -46.912201 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c984b76-2de5-3f30-b6e2-bf0456508663 | -12.6846 | -47.009201 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60281f49-6ac9-3d94-b751-b58c397d5da1 | -9.2515 | -47.341 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6db42ee0-76b2-3a93-9af0-961e07fe474f | -4.9926 | -45.547001 | 2026-09-24 00:16:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca90de49-9b31-34f9-8381-ea59e82ff44d | -2.8273 | -60.210899 | 2026-09-24 00:16:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0bccc8f-2852-3f63-a468-42248c09b315 | 1.5753 | -55.925301 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d6d699-a2a1-3c97-b8d6-c0c3079733a5 | -3.1792 | -48.0089 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edda5b20-b731-3bbc-8ac1-b3438bc59f2c | -3.9139 | -59.633999 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9e2b81-06da-3641-a886-107f5a0f8c26 | -5.8426 | -49.864101 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af039e3-8e3e-3253-abfe-db0441d267f6 | -12.4094 | -46.937099 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0e636fa-3da0-3645-961a-b3f6788ec3d4 | -9.3246 | -56.798901 | 2026-09-24 00:16:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26adadd3-de19-370f-9e9f-b38d8215ba71 | -12.4113 | -46.945301 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbaa460-896b-3bb9-995c-d51d4170dac0 | -10.0909 | -46.044998 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4006beda-433f-3347-960e-bbecb21636a5 | -4.1066 | -51.069698 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d179ae4-f5e4-312d-aad3-11eb67e14b29 | -10.4157 | -49.342602 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0567528e-ba3c-338f-9960-4ce8c5a2d921 | -5.7182 | -49.816399 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f485113b-e0e7-3a18-bc38-027996e2700d | -8.9155 | -43.875999 | 2026-09-24 00:16:00 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a369d7c-aa76-3ad9-8b3f-2a9e02905df8 | -19.186701 | -47.355999 | 2026-09-24 00:16:00 | METOP-B | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 29e267ea-c81e-3ed8-9022-9718735528cf | -2.4455 | -49.209499 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a845eb79-1216-3a58-b912-f60db34bec9c | -6.3435 | -57.753101 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260be9f9-b95c-31c8-be88-546036405197 | -6.0553 | -53.278599 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ccea23-232b-3831-a0bf-b8e6de10b10f | -9.236 | -47.362598 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44f9c43d-4377-331c-b519-7b24eac8c224 | -2.7395 | -51.5415 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc8e979-7614-3cff-9f97-7f00a5f786bd | 0.605 | -51.563499 | 2026-09-24 00:16:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a35123a6-b7ab-3c28-9ff9-4d3a9183e7fa | -10.975 | -54.093899 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba5c266d-a563-30f2-bc8f-7fbbdf4a4265 | -13.0566 | -47.408001 | 2026-09-24 00:16:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10099ba9-c540-3dc9-a8d0-e47701f2fb27 | -7.4289 | -49.856602 | 2026-09-24 00:16:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77c47c2a-adbe-3c74-a5b0-f096456a1084 | -1.6331 | -54.903099 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22760a17-3c83-3dab-8488-e04069f3bc7f | -2.707 | -57.498001 | 2026-09-24 00:16:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64f40290-53f8-3085-be2d-78516bd16a09 | -7.0208 | -44.643398 | 2026-09-24 00:16:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c34cd4b-7fae-3c68-87d4-0e79f9f8fa65 | -12.1866 | -46.999901 | 2026-09-24 00:16:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a067f6c-3824-35e7-8a3b-0151e35dc9d6 | -7.6179 | -46.801102 | 2026-09-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 828de545-3112-3e48-8d7f-af368b78ccae | -9.6768 | -46.692299 | 2026-09-24 00:16:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cee42209-3b53-3b58-bf67-e4531490454c | -12.1568 | -47.3582 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfb7bd68-17a3-3f26-956b-d864d15454da | -8.2709 | -54.7672 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0c6b98-19a0-3cab-849c-7e61eafcd017 | -9.5669 | -45.2383 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4072e2f-e4ca-35bc-b826-e5c2d49bf599 | -4.013 | -52.068298 | 2026-09-24 00:16:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07f14508-02d6-34c6-90dc-43625daffc5e | -6.6171 | -59.909698 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bebba05-0f6b-3c11-86e2-d245edeb2dd6 | -7.4191 | -49.858799 | 2026-09-24 00:16:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610def96-47cc-3b56-bf51-59fd395a2bd3 | -11.4523 | -47.392101 | 2026-09-24 00:16:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4664190-ae1c-3f83-bda3-8317e06ca04e | -6.7856 | -48.6721 | 2026-09-24 00:16:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e2d8fe77-9d45-3fba-a510-e3ce3db7f4ce | -1.6244 | -54.864799 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c811245b-2a37-3161-8a86-ef5165697a6f | -2.9684 | -52.143101 | 2026-09-24 00:16:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8296e388-146b-34fa-88ae-91a0955bbfe9 | -12.8473 | -44.3694 | 2026-09-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec00865a-d10a-3016-80b9-ced12dfc0a95 | -1.2733 | -57.0084 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a272901-a159-350d-a724-03288dbfe0f9 | -12.1373 | -47.3629 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79a3e127-8d28-3a40-81d3-2ecf88f34042 | 1.6039 | -55.890202 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31b25516-9150-303a-b09e-792246cd896c | -11.971 | -50.764999 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e75ef06-2f63-3edd-a74d-9566c7134325 | -10.096 | -46.023102 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c2b311e-6233-3dcc-a3db-c1fd56b4089f | -10.7546 | -44.813599 | 2026-09-24 00:16:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfaa7be-daf4-317f-8408-630db512538d | -17.4214 | -42.449902 | 2026-09-24 00:16:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb11a927-6e37-34f2-aef0-df586fae09e8 | -6.4181 | -43.473202 | 2026-09-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09c5d192-e08b-3deb-a3d5-d062c220a004 | -7.465 | -44.563499 | 2026-09-24 00:16:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4850d60a-06fc-389f-9d2c-d5ddd90ca8f2 | -11.256 | -51.3489 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e521c1fe-c831-327f-b5b1-bd26679c96b0 | -10.0839 | -46.015701 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 304b39f8-bc67-32d5-bf71-939a75309e16 | -5.3131 | -43.406502 | 2026-09-24 00:16:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dde6a0da-febe-38cf-8476-e97a92a2b5e5 | -8.459 | -48.681599 | 2026-09-24 00:16:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7d714ba6-566e-39e7-b4c4-24b13fbea25d | -4.0146 | -52.0751 | 2026-09-24 00:16:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea89a950-1147-31fb-8bc5-0c4915e0b860 | -7.9548 | -49.4049 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa80c94c-14f1-3601-bd95-f75ca832f347 | -5.5709 | -42.735401 | 2026-09-24 00:16:00 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e230c2d-50e9-30cb-a053-b54337869801 | -4.4455 | -55.015301 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e6f725-8148-3c6c-848c-e9c40bd81d5c | -3.7299 | -54.2024 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231d458d-ea83-3ccd-a3fa-be09f7b5a35d | -4.4431 | -55.050701 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955a4f8d-6e9a-3096-8692-6e62af988a83 | -5.5845 | -60.1623 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb71da4-0249-38eb-986e-2396358a9905 | -9.259 | -46.236198 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5273e803-641a-35b8-957b-32f2e775a012 | -3.0697 | -54.379002 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a508f113-0ea0-35ab-8457-4d3d1467e8c1 | -1.6249 | -54.912998 | 2026-09-24 00:16:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f93b2e19-2f0f-3e31-a280-a7bc413aca0b | -4.4738 | -54.957001 | 2026-09-24 00:16:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282765bf-64bf-3bc2-89ca-df9a941bd9b6 | -2.738 | -51.534599 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a323758-fe6f-330f-a058-6df1df306c66 | -6.6133 | -59.8913 | 2026-09-24 00:16:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82a67f64-a103-3815-9324-83170a6028b4 | -3.1535 | -50.821899 | 2026-09-24 00:16:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6c20ef-e775-3c0e-bda5-08a5abcbe5fc | -6.7189 | -44.161301 | 2026-09-24 00:16:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65341a99-0afb-3230-9803-4fe4d69c3e2f | -5.2237 | -49.233299 | 2026-09-24 00:16:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e63c2b-152a-37d3-95e3-039e97c792d3 | -11.2658 | -51.346699 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 910a0df7-611d-3f0d-876a-6aab3a5143d4 | -13.2022 | -51.5541 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c47cd985-3f36-3a82-89ac-8ce78876b0aa | -11.2771 | -51.351601 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1db9057-7d55-313d-92a9-7b320ef64bce | -12.1703 | -47.371799 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2df4239a-bcd7-35bd-8551-de045e1b06d4 | -6.4768 | -48.4515 | 2026-09-24 00:16:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 20658516-1b6a-36d7-a96a-1f7b01ef9406 | -3.644 | -54.739498 | 2026-09-24 00:16:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff431904-fa5f-35f2-ab15-8f76abcbb823 | -12.069 | -50.742802 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 010074bd-8076-3a80-b1b9-89e533eed952 | -1.3919 | -47.935101 | 2026-09-24 00:16:00 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baf9aea7-2c31-3d58-b42c-ead1e8367868 | -11.9483 | -50.755402 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0087c867-0dd3-395c-9fb3-954a7449bb01 | -5.3684 | -56.036201 | 2026-09-24 00:16:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf96a5e-86cb-3e13-84c8-aae2bac6d469 | -3.707 | -54.191601 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c62402-994e-33f7-ae1c-ecd77338a37f | -11.4764 | -42.313599 | 2026-09-24 00:16:00 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a34675cc-ea03-300a-9059-c875a361f29c | -5.8784 | -51.566601 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb5e22e-f42e-3bb1-b2d1-315ff61454d2 | -12.0528 | -50.297901 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
