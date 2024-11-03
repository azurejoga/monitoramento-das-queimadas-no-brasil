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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a941dfcd-07d9-351c-a5c1-d86d465748fc | -4.76589 | -45.68716 | 2024-11-03 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d6a358-ec85-3a33-8297-0f12a12a5353 | -4.76572 | -45.6818 | 2024-11-03 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e68a6b-2e41-3cf4-85b5-9f7678464721 | -4.76479 | -45.68715 | 2024-11-03 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a460f6b-9ca0-37c7-80b4-a9e9f499614e | -4.76104 | -45.68647 | 2024-11-03 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3872fc9c-b62a-3cd0-a9fb-6f5f77d99824 | -3.92896 | -45.87177 | 2024-11-03 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d04b303-6ef7-376d-ab7f-2b258d8c745c | -5.17431 | -46.11141 | 2024-11-03 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68fd340c-ab99-3101-bee3-54a38457fda7 | -2.07547 | -47.13266 | 2024-11-03 03:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ec0ccc9-92f7-375d-bb60-4c2c8b88ee58 | -2.17326 | -46.47926 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8384f044-793f-340c-9411-728140fd2302 | -2.17271 | -46.48255 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 900afd85-aaa1-3f34-9f2b-34f6319e8a57 | -2.08167 | -46.38205 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a8425a7-c422-3676-8315-836843c7822c | -2.07709 | -46.34453 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 156ba370-ac70-37ec-bba3-4c3d71218412 | -2.07655 | -46.34776 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71201cd7-8110-398b-baf6-3401be69c82d | -2.06018 | -46.35309 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 101649f5-9797-3282-b5fc-b5ee80f0cb9d | -2.05966 | -46.35633 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e09be79-9ac6-3fe6-8aa5-c2770447052d | -2.05543 | -46.34898 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6053d23-b500-3b26-9e81-ce1b00bb5cb5 | -2.00459 | -46.59636 | 2024-11-03 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 554150fe-5048-3212-803e-ffcd310fcf2f | -1.74307 | -46.08389 | 2024-11-03 03:53:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7eb9c077-5038-375d-94f0-ded725bbc19b | -1.74255 | -46.08709 | 2024-11-03 03:53:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4755233-f097-3672-aa98-067662b60e77 | -1.7389 | -46.07669 | 2024-11-03 03:53:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e02a2dc-32f0-3946-a85d-05a0a081c694 | -1.73839 | -46.0798 | 2024-11-03 03:53:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85786131-8337-397a-a9cf-9e6a0ee2f329 | -3.36128 | -46.29474 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10299804-73a6-3ebc-8fcf-3dd7027573f7 | -3.35665 | -46.29077 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e5a7100-a1b3-3724-a93e-2bcacfbe2c5b | -3.35614 | -46.29388 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca13ac4f-0374-32d2-9950-8238ba352753 | -3.26775 | -46.23964 | 2024-11-03 03:53:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77f1df66-5091-3d65-9dcb-76e32bb9ba14 | -3.18236 | -46.59703 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c855c47c-165e-39b7-ab3f-eeb4fde8fd9a | -3.17765 | -46.59285 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 058b6048-0d61-3d12-ad17-8bc8f8037f07 | -3.1771 | -46.59612 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7aaec5-a6a4-3a39-99ec-5317b6ea838c | -3.17656 | -46.59938 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d9358d1-0a8c-3c8b-b456-534f8b28d5fa | -3.05719 | -47.38751 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2607e6-ae95-302f-bf4f-0186fe2d8adc | -2.50203 | -46.18313 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3009478-ff51-3cc7-8c01-614bc1fc27c8 | -2.49685 | -46.18228 | 2024-11-03 03:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adbec38d-e389-32bf-9a3c-d78191d598e9 | -2.38747 | -46.58424 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c03a800-366a-3a3a-bc55-8dea83f8262c | -2.38692 | -46.58758 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d39a87-96f6-3733-b212-700e1d39ebe7 | -2.38636 | -46.59091 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23861637-0ba3-3552-98b9-efa648ec9b39 | -2.3827 | -46.58005 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c4e7ee0-cf54-3a2e-beea-3403f9a04cf1 | -2.31015 | -46.53267 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e9c7490-08a1-361e-9923-757dd1ac2299 | -2.30595 | -46.52504 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 292f722a-5055-366c-b316-c73fff2a2dd2 | -2.3054 | -46.52835 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c483665-a9f7-3c47-8b96-02fda23f80ef | -2.27537 | -46.47935 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ed82060-950c-33a3-b017-ef96aaac050c | -2.27483 | -46.4826 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f56dee-4016-3cc2-bc9a-6f64be13862d | -2.2576 | -46.63375 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbb39b9e-9340-3f64-8e68-65a039eb3019 | -2.25707 | -46.63706 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8f2f0cd-4210-3f14-b8f6-cf71134c3b54 | -2.2511 | -46.67456 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d8bd7e5-32b2-39d9-86ed-8b95930eee3a | -2.24885 | -46.67048 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e132864-f800-3511-987d-cd38bee07b47 | -2.24829 | -46.67385 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68ef92a0-2c7e-3232-b562-9cac3ea3d54f | -2.24735 | -46.66352 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6abe3e-1c29-31e0-9ba1-4c4add9f910c | -2.2468 | -46.66692 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec5e51f-c41b-3045-b61b-230c885da82b | -2.24626 | -46.6703 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbae24b9-ba24-360d-91c3-e6c222c0fb65 | -2.24572 | -46.67368 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae0df18d-9590-3c2d-a5ef-0fccded4f234 | -2.24347 | -46.66964 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2eadc312-36e5-3d12-82b3-be1b2d6b4314 | -2.24291 | -46.67302 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 502b6782-4f4d-3e88-af71-575939bde913 | -2.24185 | -46.61377 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b6bca4c-9036-38ff-9e11-0af929e0a049 | -2.24128 | -46.61713 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 106bda6c-8e36-30a4-a482-6ef87405d735 | -2.24034 | -46.67284 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a39e12c-2449-3ec3-b479-33f4362a642f | -2.17966 | -46.47353 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1882c11-ed82-3226-931b-b21f7f269762 | -2.17911 | -46.47683 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 744b6ba7-cd40-320a-9808-3389fb708beb | -2.17857 | -46.48013 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b6417f62-7a34-3dce-b969-2796f7488ead | -2.17802 | -46.48343 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8257121-3611-3d80-bfc5-d4d25d8ccc7c | -2.17474 | -46.47844 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe2c14ba-3d50-3afd-9032-de2c2446eeb3 | -2.17421 | -46.48174 | 2024-11-03 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3dcf9a12-21a1-3800-bf2f-23503d1ec602 | -2.67243 | -46.74522 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6333ce46-057e-3bb0-a027-95badce9b503 | -2.67185 | -46.74863 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77645efc-3170-32fb-b624-17cf0d410ed9 | -2.67128 | -46.75207 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9d718f-e226-34cd-81e1-8fd335623c3d | -2.6707 | -46.75549 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eef3d3f9-bb99-3e93-a6a8-f9aa5f2e4aa7 | -2.66967 | -46.74498 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ef0f40-b8a2-32d2-beab-925d03856bd3 | -2.66956 | -46.76232 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fc342d4-9edf-3490-8400-8266e6cfe655 | -2.66912 | -46.74839 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170931f1-517c-3964-b63d-3a6260b9d00a | -2.66858 | -46.7518 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd0b057-3f4d-343f-9adc-964cfa8ea120 | -2.66803 | -46.75522 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 003fb3b0-72ef-35ea-a97e-ac2e4902d1e9 | -2.66748 | -46.75863 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ce42013-c08d-3713-aa27-1245f80be7dc | -2.66693 | -46.76204 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34a644a-2362-33c3-bb77-0e4bdac2e7fd | -2.66592 | -46.75114 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c4873f4-7c14-331b-b525-a2ec6617e996 | -2.66534 | -46.75458 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6828f88-b019-32a2-9e00-c29d8fa336da | -2.66477 | -46.75797 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33f9677-6ba9-3a63-a60a-ec8c825a96fe | -2.6642 | -46.76137 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd72c8f-8143-35fb-a2cd-789282b4951e | -2.66363 | -46.76475 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad358d15-5d34-3487-b63d-369a28861b07 | -2.66306 | -46.76814 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d71ad77-62f0-3165-960b-56cfd2441b7d | -2.66266 | -46.75429 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e9629f0-7b9c-349c-91a8-5433f4bdd907 | -2.66212 | -46.75769 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8e426e-4ee7-3baa-b540-1348e92c9a5a | -2.66102 | -46.7645 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82827083-3b98-314c-9699-606a073aace1 | -2.66047 | -46.7679 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2cd6063-3a88-3f35-ac5a-7c293f437e7b | -2.6594 | -46.75709 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6f282b-bcab-30d2-8722-ee68bc287704 | -2.65883 | -46.76049 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 354c88f5-d57f-3297-be1f-7649d9a2f60f | -2.65825 | -46.7639 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06191666-a62c-3f26-9328-41c281b04937 | -2.65674 | -46.75684 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9b11d5-db49-35b6-984d-ce7fb3f8d571 | -2.65619 | -46.76025 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353898c1-1c09-3fde-b170-db3f9d16cf58 | -2.65564 | -46.76366 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1ecb24-cbf5-3eb6-bd06-609ff34f75f6 | -2.65346 | -46.75962 | 2024-11-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a870b769-3438-317f-82e5-d2ab904f5933 | -2.57345 | -47.30823 | 2024-11-03 03:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 872b6dbd-305a-30a5-b73f-ada68763806e | -2.57286 | -47.31193 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79a2cabf-9531-3874-a691-9543b81eff03 | -2.5721 | -47.30711 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3e1d515-e0d6-3b77-b1ee-76bdbc42a57e | -2.57148 | -47.31079 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85013580-c380-369b-8de7-d125dc0c5d3a | -2.57086 | -47.3145 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73bfd198-6a5d-334a-a537-979b8232228c | -2.56787 | -47.30733 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca14554-6b87-3b3b-8398-e3a3cd54240e | -2.56727 | -47.31107 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74719f29-6fa6-3932-b6a9-c0a5ec457baa | -2.56666 | -47.3148 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a67be99e-7d44-3f6f-95a8-18ee66655c9a | -2.56606 | -47.3185 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 301d7060-15e5-38a2-bc20-79175c7bedb1 | -2.56526 | -47.3137 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00d6dc34-6a5e-33ef-bb37-eb2cfd20337e | -2.56463 | -47.31739 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74ba854e-3759-340c-810c-b7162385d25f | -2.56097 | -47.27928 | 2024-11-03 03:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
