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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae637de6-4dc6-3696-9f07-0e5beb4d0442 | -5.2933 | -47.92762 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56905164-97d3-34e0-9862-fb819c2c60fb | -4.40574 | -48.94426 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44cce6b2-b504-321e-b352-3e91ebdfcef8 | -5.86878 | -41.23172 | 2025-10-17 04:49:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3d50f3d-3468-3713-97b9-72855891b104 | -4.39161 | -43.39355 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7efd74e-23ae-3541-8f1d-25ee592c51fa | -7.46723 | -42.14603 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a48377a-d05a-3e4c-84f2-5404b38ed623 | -7.32457 | -44.16167 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2543d3df-df30-3749-b3f7-07086b64e100 | -4.36936 | -48.70847 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 859bc53c-cfdb-30c2-9361-45fdcb525770 | -7.20489 | -45.37802 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb442c1-c472-377a-8f9e-3e0f3661568f | -5.24486 | -50.95736 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69a346cb-0bbd-3a08-8b00-1f3742d9d479 | -3.23626 | -45.97956 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a1ee267-8e99-32e7-838e-85bff8823b3b | -5.90044 | -44.7436 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c0daba7-6039-38a5-b7c2-bb243c3f1147 | -4.3299 | -49.45648 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57c87377-d33c-3aed-a27e-df55256095c8 | -5.31721 | -42.94544 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e989dac4-4796-3302-a347-96cea98ad1c0 | -6.88735 | -43.98896 | 2025-10-17 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90c03678-cdcd-39e8-94e8-99fe3e0294f0 | -4.93914 | -47.07811 | 2025-10-17 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bacf61d5-dce4-342e-afb0-77e10cd3c622 | -5.89078 | -43.89997 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef6d4476-53d5-3e6f-9063-2e32ca1954d1 | -3.65523 | -50.26755 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9962c8b0-0a30-301b-baa0-69e6aefc3892 | -7.45558 | -42.15118 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cea119a7-a211-3c86-9b73-ce000c70b359 | -5.49172 | -51.17076 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 94068849-ff75-31cb-bcf7-98bd4828138f | -2.73132 | -49.38976 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c75d19c1-0a18-3e8a-a9c4-0faf4f03be49 | -5.46334 | -44.64109 | 2025-10-17 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b1bc775-61cd-37e8-82a8-f9a8dc0ccddd | -3.24496 | -45.97799 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1748395b-a788-3e43-b157-4c4c0891d254 | -3.51629 | -52.49026 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3402255-5adb-3658-8f5b-d5f17762f3c5 | -6.27409 | -52.62962 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44704e1c-a416-395a-a50b-067a4722bd52 | -3.97786 | -42.49407 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a289c033-1d86-373f-8a38-2cbf17bdfb26 | -4.51898 | -50.41024 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85b0e35d-b439-3f30-afe2-4fea1609fb3c | -3.54151 | -49.00624 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04818430-5c2d-3371-9aba-2ae80323de99 | -6.75374 | -42.37774 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| befa24ab-3797-3cd1-a447-253cf621369d | -6.14084 | -41.72354 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6384c6c1-f6b9-39d0-969f-c146cb5a3160 | -3.98273 | -42.49265 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4a36fc8d-d5dd-3782-8c99-6e1e6256c92a | -4.01254 | -47.42003 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8357664a-56c3-39dc-8e36-034698beee77 | -6.2978 | -45.53079 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2000e107-becb-36f8-ace5-0b1d4b20179b | -3.23702 | -45.97476 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e3cd6d1-f265-3e76-8672-506e789a2da3 | -5.24054 | -49.23074 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d4b79c-3712-3393-adf0-0aeb4ec5e8e6 | -2.73467 | -49.39028 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 954934df-78ad-358c-a42c-6284be2b303a | -7.61848 | -47.8379 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f55129e3-0c19-364a-8e69-ad227e414e2e | -6.37833 | -41.47311 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1250c334-1e7a-35f9-9f0f-8e25893801a6 | -7.3561 | -46.98766 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93119764-cd04-3328-a53b-c460930fb6e8 | -6.29415 | -45.52652 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 899de09e-2364-3825-ab2b-97f12956eb2f | -6.5346 | -55.05222 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4969243f-9b79-3537-b7ae-d56dfe3e1e7a | -4.10845 | -48.01954 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806ff23b-f409-3a9d-8b9a-6ec1117f5faa | -2.87797 | -50.73339 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b81c0e8e-e6b2-357a-983b-06e98c869ae8 | -7.79204 | -44.93388 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d424f2-debd-37be-9e35-e77b7fc89fda | -2.74303 | -48.31269 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3307b342-0c3d-39a5-80ae-0acf949cb5bf | -3.99993 | -43.27812 | 2025-10-17 04:49:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59af13c7-09e9-3492-933a-5399cb50a01a | -2.4227 | -48.59477 | 2025-10-17 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d16215b4-0ca3-31f3-8f6c-c5083bb78574 | -2.71355 | -49.4157 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a3e8d9b-9a8c-3360-b300-6ed9745b5368 | -5.09563 | -45.42857 | 2025-10-17 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c70d6b8-4af6-3dcb-9e18-d31c05bcb404 | -3.61101 | -48.9172 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03751476-a51f-3495-9d9e-ad067a87bc75 | -8.19206 | -43.31808 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0857e3c0-fe96-3fc1-afb9-530797ed6e26 | -3.24091 | -45.97534 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9cf9c687-ce76-3338-9ab3-1eea80b1de80 | -2.88408 | -50.7379 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6202a174-b119-3225-a39b-8c004d2ff937 | -8.15953 | -44.00309 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0715f097-0594-3164-9f51-cb0ea142d5e2 | -4.1433 | -47.65735 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93b15dbd-4e55-35aa-83a3-f23f64956b4a | -6.13894 | -41.73721 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee25ae8b-6da3-39ca-8ea9-5e1f135f364e | -7.46955 | -43.93045 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48978395-803c-3b2f-8eb2-c06a0d03cd20 | -6.3065 | -44.72199 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ede8219f-3539-33ec-9f53-97dc616928da | -2.73746 | -49.3943 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d102fc40-e59d-30fd-9283-9ef0c77ade95 | -7.75367 | -42.50587 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c70d6cef-411f-3673-834d-6c2ca38d233c | -6.76737 | -42.85085 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| afdb64b7-5b7f-38e7-b376-35cc25837dc1 | -2.97729 | -49.22279 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 613c3365-fc1d-354a-bfaa-dfefafe3ef76 | -3.27068 | -53.25496 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2cea6a4-939f-32d2-bac1-17f223ea2720 | -6.71173 | -44.37452 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e4a2bec-8666-3bd2-b4e5-7f274ca17686 | -6.20808 | -41.75671 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c58949d-242c-39e3-8886-0095c42d9758 | -6.99674 | -46.99159 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| efb3214f-9bf1-3760-8681-75190aa9436c | -6.42633 | -44.03669 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 274c5be4-c336-3114-81f1-ab361d44c65f | -5.26206 | -50.97783 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af863d9d-14d7-3683-bf5d-b67abc02f20e | -6.40089 | -41.50549 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c98e476d-0d15-38c4-a087-00e449fe9620 | -6.42722 | -44.72116 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0cb0547-02ea-3087-9fee-62dd79af2a83 | -7.4163 | -44.76432 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93c36323-4464-34a6-a47b-95a844a01ce9 | -4.38829 | -43.38963 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae76b82f-9c74-370f-b66c-67c62a5f5b08 | -5.50577 | -47.30266 | 2025-10-17 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6e3d2f7-65e2-38e1-ba01-cb4774a3bd96 | -6.29725 | -45.53444 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d97e5c7e-6729-310c-94dd-f0d144713ec8 | -7.1085 | -44.73394 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836df3ba-32f9-32ea-908b-c45295e548b1 | -6.9999 | -46.99688 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 164c2a93-284a-31ff-8d90-60a5e65c6ca9 | -6.23854 | -44.97105 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8e0cd4b-c2c6-3a78-8f5f-1d8a20584f74 | -2.44386 | -49.36981 | 2025-10-17 04:49:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e18788be-114c-33c7-901f-ae0be6c3a216 | -2.74246 | -49.38431 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caf9c97b-9d37-3b21-9592-2c95d0ea720b | -5.61033 | -42.68225 | 2025-10-17 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ffa116db-ed0f-3eb6-8b42-d0219868cfb1 | -5.01009 | -44.6781 | 2025-10-17 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cf43a95-e297-30cf-8634-55b7305b3ab6 | -2.59887 | -51.34521 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6db0c2a7-af3a-31d6-abb1-11632f9e38bd | -3.47374 | -49.92003 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 476229c7-ca04-3a58-a6c4-97727a150786 | -5.07262 | -44.00849 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8db9a40a-0369-3f96-ad15-3928bdfbc74b | -5.72273 | -44.5126 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4bd6012-8c5c-33bd-94ae-cc50bcfb04ca | -5.25874 | -50.97731 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 367625d7-4c9e-3aec-a90d-7220cd740f28 | -8.25561 | -43.33895 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78b775c2-3f63-30d9-b539-eb41ca53f417 | -5.20793 | -46.19673 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11609a14-40b0-3993-b7c6-42b3d95da114 | -7.09628 | -44.26091 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f06d6a-c413-3e09-8491-dffcd1c0f14f | -5.24208 | -50.95338 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ca583e0-eb8a-3920-b8c4-5906e8524104 | -5.85179 | -42.34186 | 2025-10-17 04:49:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4234e3f8-6a9c-37bf-866b-241fce8e44fd | -5.88604 | -44.74987 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47083d8a-f7cd-3d07-9145-7c912f979e39 | -6.74256 | -42.53009 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98f83ed4-652a-3855-8e1a-3853d35f7d34 | -7.17075 | -42.52084 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1055e3c3-a776-3893-a48f-a1572d094315 | -3.23466 | -45.96441 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 028cc12c-a479-3482-9c70-e4533d71535c | -4.89493 | -47.63751 | 2025-10-17 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ebb4a7-77d0-3fcf-9593-b8dbb470507d | -3.54095 | -49.00985 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78107e27-97aa-38cb-b225-6ee82bcb0490 | -3.84748 | -52.08372 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e05f560-c2f4-38ca-b38e-ff47491945dc | -7.68204 | -44.63095 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ed71c58-c958-3b2b-9e20-6f3d2f09c51e | -4.70821 | -49.62011 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf3beb23-f871-30c0-8959-882e6980b8dd | -7.44953 | -46.84407 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README83.md)
