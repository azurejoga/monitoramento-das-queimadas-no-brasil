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

## Dados Diários - Página 361

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d28487df-0db7-3466-b919-78315cc49d5e | -1.18996 | -46.78288 | 2026-10-08 16:39:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e6f4dbb7-074f-3a9d-a4c4-78c808d4800a | -3.00839 | -54.07417 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7472b094-2e5b-37a6-a9da-68c92123b922 | -2.70062 | -49.03495 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 46ede8ad-cfb0-3c85-9984-8827847b19a0 | -3.01911 | -54.73048 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 98edec08-9f59-39ba-9271-2a062502b41a | -5.26073 | -47.9005 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81f4a9ed-a344-3423-b0b9-37429b503770 | -2.61416 | -57.5857 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b7fcc9cc-7e86-3288-9bc8-3ae941532f13 | -2.9014 | -54.02383 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8bc4c79d-4fea-3ba8-8248-ed605112227d | -0.28474 | -49.87745 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 199fee5c-c97c-3242-83da-491ef1afba46 | -3.29771 | -43.25514 | 2026-10-08 16:39:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a421913-78e4-3adb-9ebd-61d0dbaf21f6 | -3.78732 | -59.37259 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 54df02c3-02fb-3363-a884-a759eb8327f2 | -5.85821 | -53.46116 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0820c328-c720-3f87-8ac9-610a88a2819b | -3.59611 | -39.14018 | 2026-10-08 16:39:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5124332f-0262-3395-aeee-198c3a698fb9 | -5.66337 | -43.62498 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e0856f92-9666-32e5-bafb-bcb8a80844ae | -3.77057 | -59.25243 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 86bf35d3-8253-30d9-be54-e059bef67029 | -3.43097 | -54.05887 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| ef749d43-4545-3c7b-85ec-5cc5497fa8aa | -6.9944 | -59.10231 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f9103279-17aa-3ace-b7de-b3309def2345 | -1.43817 | -52.85326 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c2c2b01-31f3-3095-af72-66d33ced3bb5 | -1.50419 | -54.8121 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 538d4aad-3c64-3f19-bd44-2d650ed49c6b | -2.89759 | -43.98784 | 2026-10-08 16:39:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d610326-d012-3f73-9d77-4bdbd85db80a | -3.00295 | -54.0775 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| ca9732c3-e54b-37d2-89bb-ccf7ea908d6a | -2.92703 | -58.31016 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 252088e1-c879-36d7-9195-48177b4f508f | -5.32743 | -42.81139 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 27a913cc-cd8a-3198-980c-6ad191fb156f | -3.65829 | -59.15618 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f1e09531-2ded-3d4a-9a72-61b1d735684d | -2.78594 | -57.63678 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2586572a-38f5-3f98-b96e-ee465a9ac76d | -2.48578 | -57.78576 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 27535c2a-05c9-3af2-80bc-d0a77b423468 | -3.00088 | -43.31958 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ec0764e-6f40-37cb-a759-03099f8d453a | -3.79677 | -41.64937 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 590233f4-c1c5-3dfa-b2d9-75adfbc8cae6 | -2.09234 | -46.5807 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17e88b2e-1a23-3505-be9a-c54cb3f93c71 | -1.32458 | -56.40994 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e57637ae-26f7-3b58-a38c-86ccd6e0a64d | -3.3869 | -42.89984 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4bea9463-9b8b-3cb8-878f-7649da7f73c8 | -5.16105 | -42.72993 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 16a18f18-6e48-3d23-8aaf-57d2edfc2f25 | -1.88805 | -56.29899 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 74ab176a-aae0-3522-9bc2-6e885b07770c | -5.4179 | -45.71077 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51243ec3-c569-3bea-8293-6dd8efbdf929 | -3.00845 | -54.08183 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 5e4daa1f-87c9-35e9-9428-4b3a02ca9b17 | -6.19392 | -53.14841 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aef0560c-b517-3906-a1c4-d9e9cfe48955 | -6.74864 | -55.14639 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1df628cd-8013-364a-887c-9e75a0178458 | -6.04693 | -53.48265 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f4249074-45cb-32ed-9eb2-56c39020e7ab | -3.88714 | -55.82556 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| db10b9c9-42c4-3aac-aaa5-da91f1cadf8c | -3.89453 | -59.44477 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 09abd003-3166-3edd-91b8-f94349ced547 | -2.56841 | -56.17719 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 0a8838be-4581-305a-baf8-e51b3beeda8b | -4.29792 | -48.59954 | 2026-10-08 16:39:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63ddec54-2c9d-3f18-b3d9-fd20cff8851d | -1.3295 | -56.4058 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2956bb7e-5b71-37a3-a350-01fa13e03e2a | -3.90133 | -59.44381 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 50f718ab-0053-309b-899f-e65131fe3d24 | -5.95957 | -51.79567 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4899ddfd-a6d0-39cd-9687-a2a780a6646d | -5.77567 | -52.36366 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe53ac9e-b194-38b8-9004-afb72f7bef5a | -1.82947 | -56.16446 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcaef5ac-8319-3f99-877d-035c34ab81b1 | -3.66356 | -45.40862 | 2026-10-08 16:39:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17cdf392-0b87-3d1e-9983-0464cbb0ae1d | -5.09012 | -46.20745 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b1acc0dc-39c0-359a-ac5d-b4b7e4520a8f | -5.38951 | -42.9662 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 823639c3-0fb5-3177-97d1-19ac2124b49f | -2.37402 | -55.27594 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94eeb9af-7657-39cd-93a6-76b78bc0311b | -4.1926 | -38.73632 | 2026-10-08 16:39:00 | NOAA-20 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e1891e75-bb03-374e-aff9-337c3449b276 | -4.4372 | -43.90258 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf020ec7-470f-3eaf-9023-42a27145e6d3 | -3.38313 | -58.30092 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 22742c18-e644-3433-9b35-d6da180fa1d8 | -2.94438 | -54.10675 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a946ea55-6591-334d-a896-a9fbadaf5562 | -7.2075 | -55.1344 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aded4538-e21c-37bb-a81b-513ced6d7708 | -4.32893 | -55.03719 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83b2c407-efed-39e0-b1ba-3103200b0253 | -2.07369 | -46.56942 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 519be0a6-6fc1-3b36-a021-883754aec99e | -5.37401 | -45.66783 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4456173-265b-3060-bb86-3cf627a5c895 | -3.33057 | -42.91692 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 997ae13e-27cd-3200-a16e-4d542cdd1193 | -1.32407 | -56.40648 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ba30e09-619a-3c90-a66e-bbf57857ae66 | -2.93552 | -54.04632 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2c866981-affd-33be-97fc-5b08efa66388 | -4.2612 | -58.91069 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 09c1cfa8-5512-32e3-a229-a65d85c1b4f3 | -2.50847 | -56.14715 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4d81ba38-0460-3ac5-a266-7b93944c1891 | -3.3857 | -42.90378 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0bd7f782-629c-3a58-9b9f-3f25004c061a | -3.74337 | -59.61316 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3d768fb8-7f53-3861-9b76-b6529ee35f5e | -3.01983 | -54.76133 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d9541be0-8da3-3f0c-8032-8fc7f79e68d0 | -3.77725 | -51.91286 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 147b8b25-6324-37eb-a909-85602746d4de | -5.09674 | -46.20645 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| da2c79cc-0f62-378c-aa92-66bbe6cbae71 | -2.46157 | -56.09092 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3372e879-de56-3883-ae1a-b4d011eee3f8 | -3.30864 | -44.70578 | 2026-10-08 16:39:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 32a73fa7-7255-3588-94d6-161f38050201 | -2.76313 | -54.1082 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ce9d92e5-4b36-3306-ac06-fb4db5e5c178 | -2.45155 | -46.02081 | 2026-10-08 16:39:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 151c3675-79fc-372b-8296-97e0051726ae | -5.51202 | -42.84367 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| abc7ce62-fb20-3beb-bb11-de68f931fe42 | -5.36649 | -45.72925 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6352da99-16f1-38ab-bf85-d27fe1f882af | -6.14356 | -47.95621 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17ca864b-88dd-3ac6-9af3-1a2dfa2306f9 | -3.26029 | -41.62992 | 2026-10-08 16:39:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b7046584-07dd-391e-bfbe-956241e5e26a | -3.00817 | -53.90633 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6b7bfccd-a485-3004-894b-0fb28e5fb099 | -7.23358 | -55.12323 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5f1aa005-d451-36f7-a0a1-1e8a8dcb45e3 | -5.40942 | -45.92082 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a4c53479-49d2-3c24-b490-c7c4888a222f | -3.10672 | -50.26401 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| fc54ffaf-a5aa-3c50-aa73-b0a240d80fd4 | -3.36192 | -59.42153 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 52711581-409f-34fc-a038-e83545602d6a | -1.32238 | -56.40993 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 67a6949a-e07c-3e8a-a16f-7688e138a3fb | -5.35165 | -45.72092 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 257cec6b-6bda-39ef-8ce2-5222c29f60b6 | -6.2159 | -53.54127 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d97a02a7-4d99-35b9-b2c3-a2e90506f91f | -6.20332 | -52.85291 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b5c0ad4b-a389-397a-b257-8609d8b1d168 | -6.32168 | -54.80121 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8710d5f2-6661-34e7-8266-06a7dc60c4d2 | -5.36962 | -44.19397 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 804b5eaa-1a2e-395e-be33-67f169bb0ff2 | -2.41379 | -56.53285 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c155137e-73f8-3078-9321-1c70a97b31c8 | -3.26907 | -54.02116 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8e0c738b-4736-37ab-8fa8-fa9e60168bff | -3.66142 | -45.40961 | 2026-10-08 16:39:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5e9f532e-cd56-3a58-b5a8-20d891ee882a | -3.49622 | -39.50267 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 193cde29-16cb-37f1-bc66-79b986f92c89 | -6.4882 | -52.81785 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 05f332a2-e1be-3efe-82ec-57f6ca6ce4a4 | -4.47213 | -55.89849 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d360331-c5db-340b-8b1a-9ae4bcb4d059 | -3.55287 | -44.56515 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 68e4695e-5e47-34b9-bf24-fda15518a26d | -6.17062 | -52.65201 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e4b32466-5e4d-37fa-9aaf-43f749cc0985 | -6.87107 | -59.34562 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 755a03fd-9dfb-3ebf-bda4-0b15446edcde | -6.83162 | -56.12047 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c5a81b96-43a5-398d-acfc-0754508c7ce9 | -2.04292 | -46.32341 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96d4a787-9730-36d8-91a9-f13df2f471e0 | -4.58633 | -40.65119 | 2026-10-08 16:39:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5640d1df-4093-390a-818a-a91149fb9dce | -4.99317 | -45.59668 | 2026-10-08 16:39:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README362.md)
