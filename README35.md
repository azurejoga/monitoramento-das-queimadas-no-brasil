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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6df1706-ecce-38c0-92e3-5dbaa188d28e | -2.07254 | -46.84229 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5226ec13-8a1a-31b6-8de4-fed344252779 | -2.06973 | -46.83815 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9397aa27-0752-3bf7-9202-d94ddc9da462 | -2.06916 | -46.84177 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 061397cf-dfd7-37fe-bf43-0afa1a67dcaf | -2.05727 | -46.89537 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 870f46c5-79f6-3d92-b398-8601646906ed | -2.0567 | -46.89897 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c839cc81-0d16-36e5-b9a8-f6ef117a2d95 | -2.02026 | -46.21436 | 2024-10-21 04:36:00 | NOAA-20 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b0a38f7-7c0d-32fa-be93-4fa495f83fa7 | -2.01901 | -46.24513 | 2024-10-21 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16be1a58-3935-37fa-9910-444b09b43865 | -2.01739 | -46.21004 | 2024-10-21 04:36:00 | NOAA-20 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 74fa623d-65de-3270-b2bd-41da9383b2bb | -3.54979 | -46.40854 | 2024-10-21 04:36:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e75f3289-91f7-3dd9-b733-c0d204c6e292 | -3.2353 | -46.50989 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3954340e-ace2-3593-b3b6-8171b2aa3c4b | -3.23184 | -46.50936 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8615ac7-fa0a-3b7a-b92a-e245d70cde98 | -2.51923 | -47.34976 | 2024-10-21 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feae2d6a-48ca-36c0-a680-bf7bd4052f75 | -2.51906 | -45.98488 | 2024-10-21 04:36:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d513ddac-2e52-3366-abc9-77bbecc1e9cd | -2.51588 | -47.34924 | 2024-10-21 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2e1242e2-7015-3106-95f4-e9ca8dd9e1e7 | -2.51555 | -45.98434 | 2024-10-21 04:36:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48e4e49-57ad-3f9d-a310-cc0da835a68b | -2.49943 | -46.04167 | 2024-10-21 04:36:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c18df95d-d6a4-3f10-84ce-d166c0207dce | -2.43897 | -46.90201 | 2024-10-21 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da4e7980-7b00-345c-98f8-106f12ead67a | -2.3028 | -46.627 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 285ed0a7-188e-393c-9db1-0ebca32de34a | -2.30223 | -46.63068 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9146146d-6760-3833-95f9-8f3479065857 | -2.29939 | -46.62647 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf9e9af8-9963-3e4d-9773-f3a08f60c0f8 | -2.26846 | -47.07872 | 2024-10-21 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 314022a9-c2e3-312b-a67b-baf074cc3913 | -2.26743 | -46.74181 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec6a5807-fa52-36dd-ae3f-7430df4344c8 | -2.26686 | -46.74546 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5669f9c-69d1-37c3-aec9-84914d1351f1 | -2.26661 | -47.07829 | 2024-10-21 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b1fc1c-4919-3099-a8c3-fb6d5ca95c4a | -2.26403 | -46.74129 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f90941-80f7-3b29-a716-c54402dbf0cb | -2.26344 | -46.76735 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70a6ff5d-0c3c-38c9-b674-cfea54d52c1e | -2.26287 | -46.77099 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c316fb6e-0f62-3fc8-adb9-cf1f50829306 | -2.2612 | -46.7371 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4e96081-6ed5-36f8-a762-898c026a2a26 | -2.26063 | -46.74076 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d94808f-6cdd-377a-820e-6406fca9f667 | -2.25948 | -46.77047 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 070714c2-5f81-3925-9f55-9d20c893ed3b | -2.24872 | -46.77255 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec4ba80-16eb-3714-b494-a5a7bf2e31d1 | -2.24023 | -46.78242 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acdf613c-0e3c-394a-a14b-f2fe80746888 | -2.23796 | -46.70727 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17bb5bc7-d6dc-398a-b9b8-b7df17d4241f | -2.18631 | -46.72213 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71a5904f-db8a-3572-8ad8-b07e02006aef | -2.18574 | -46.72577 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 159c237f-bb82-310b-b69d-b7ebb4afb418 | -2.18516 | -46.72942 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 473b7ac4-30de-37e5-a8ee-17cbb73b5e21 | -2.18459 | -46.73307 | 2024-10-21 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68aa2a36-282e-31c0-a473-399dbd779ef6 | -2.15044 | -47.06055 | 2024-10-21 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22e7c2d6-a4cb-32a6-9286-bb48b18419c3 | -2.14708 | -47.06003 | 2024-10-21 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee6f8419-c5c5-3cb9-b2cc-abbc8a2fc9aa | -2.95832 | -47.36626 | 2024-10-21 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 352c2cbf-017e-3fbb-a8e6-882c071d0999 | -2.63888 | -46.54053 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d003b7-e9d0-3a54-bb25-09ee857c3c18 | -2.59815 | -46.12745 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb6022d0-cf42-305d-b61a-279601e84c94 | -2.55716 | -47.34099 | 2024-10-21 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d12370c9-17e7-343f-b023-ac6af75292cb | -2.55101 | -47.3003 | 2024-10-21 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17a08e78-136e-3080-895b-96bc2fb5e244 | -3.09763 | -45.94227 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d9e426-1c41-3173-b0ae-d2bf68d43e7c | -3.09739 | -45.94352 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5a9cd3-1a8c-3633-b96e-49c9ab0d0055 | -3.09703 | -45.94624 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbb3202-8e8d-34a4-b5d3-33b13958ddd2 | -3.09677 | -45.94748 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7744f8-df29-337e-8a94-662854c487d4 | -3.09323 | -45.94695 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca95d470-4cb7-3097-b481-5dc4ec91b997 | -3.09289 | -45.94969 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296de133-7074-34c1-a45e-2f07913ab959 | -3.09261 | -45.95092 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 886e70b9-6149-32c9-b35c-8edc3dfa93a0 | -3.09229 | -45.95365 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463fdcbe-b61e-3497-9a62-ebd4dd4e16a9 | -3.08907 | -45.95039 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88ca7d92-9906-35b6-8415-190f24731784 | -3.08845 | -45.95436 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ccd61b-46a2-34d9-8fdd-127950091bf0 | -3.08556 | -46.55329 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 897d5826-1434-3409-ae49-96f92d75c7c6 | -3.08429 | -45.95778 | 2024-10-21 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d70a241-2006-3532-b1dd-ed3814d8db7d | -3.91003 | -46.4493 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 421df32d-90ca-33cd-a15d-bb7ccb6684ac | -3.83332 | -46.47334 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acd0a2c9-edfa-3b29-a454-19f22aa75a66 | -3.82984 | -46.47285 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd24c4ed-7fe7-38c8-b17d-fb906423cd95 | -3.8297 | -46.92766 | 2024-10-21 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe013f39-c552-30be-a363-6b58af77159f | -4.44627 | -46.44335 | 2024-10-21 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2175b2f3-69ff-330a-8870-aa0b988ef450 | -4.44568 | -46.44725 | 2024-10-21 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0021e40d-52e7-3ee7-a134-1e7864d45851 | -4.35601 | -46.60472 | 2024-10-21 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 398f3d6a-0f33-3d48-a95f-95ebca9e00f2 | -4.19277 | -46.79826 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 341cba64-fb15-3019-bec9-613b43672c8b | -4.17328 | -46.78733 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75a5cc67-ea92-3022-acfe-8e9468cb501d | -4.16926 | -46.79057 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16d78f4a-0506-3c90-b7c8-7edac1f8a8fc | -4.14455 | -46.49851 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec20c45f-4993-3ef9-ae6d-cf247642e9a8 | -4.14224 | -46.49033 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a97fe1e7-fb0d-3d6f-a178-1eebaa447bd2 | -4.14165 | -46.49414 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9518501b-c368-3e13-a76b-74e2aa2f8ac6 | -4.13875 | -46.48981 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba486d19-7c70-3ff3-a90a-06b039eaccce | -4.1267 | -46.86544 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac9fd81-2c3a-3898-8743-5a7e497d4a92 | -4.12328 | -46.86485 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fd0069-ebaa-3ef3-b293-6bb1549e7a29 | -4.06878 | -46.65303 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef499a6-1453-3039-b7aa-caba4882fe6d | -4.92735 | -46.84848 | 2024-10-21 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc95571a-7a3c-3386-b8f8-10c24ded693c | -4.55716 | -46.68536 | 2024-10-21 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b88a07-cf25-30fb-b001-51ae74416f71 | -4.32206 | -47.32429 | 2024-10-21 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b4d56e4-dab4-3b91-9a84-a67c735fb0ff | -4.01005 | -47.32482 | 2024-10-21 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87f9752f-2a2b-3c22-a33e-24d1e4661607 | -5.00417 | -47.65319 | 2024-10-21 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e5e16dc-61ea-364b-abe6-a65a145171eb | -5.00362 | -47.65679 | 2024-10-21 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 652ebfef-72e2-3b34-b8ac-7a706fc88702 | -5.00236 | -47.65342 | 2024-10-21 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea9bb6f0-018e-3699-93a0-7de0b24bfd22 | -5.00179 | -47.65701 | 2024-10-21 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66b68585-0a0a-3343-99d3-96f2cfc09ad5 | -1.80547 | -48.49728 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12eca09-b09d-385f-832b-ee405dd21f79 | -1.61377 | -47.46888 | 2024-10-21 04:36:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 743be84a-e1ce-3a71-98f8-718da5b0bdc1 | -1.39695 | -47.61647 | 2024-10-21 04:36:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e1d83b0-f64d-3140-9530-2f9a7d5c08ac | -1.32953 | -47.95915 | 2024-10-21 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fef337e3-2fb4-3ba9-98f3-1c8a831352d4 | -1.25415 | -47.37759 | 2024-10-21 04:36:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2f2f05a-3709-37b1-9a9a-8d749b912c72 | -1.25082 | -47.37708 | 2024-10-21 04:36:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5a92073-a2f6-3997-9f81-2732a81a3e85 | -1.02202 | -48.0763 | 2024-10-21 04:36:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a47382d-787b-3fd2-b6e6-c3dfe06e9f40 | -2.1147 | -48.11039 | 2024-10-21 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05b8377-27f4-381b-a034-5f4e049d8c00 | -2.04038 | -48.40787 | 2024-10-21 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a8f26cb-e2c8-3b4a-99bc-3b5c45535444 | -1.97636 | -48.68602 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fbf4cb9-296d-3a11-9f0f-5e2244078b8e | -3.1095 | -48.63165 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e88f7bb-fcc7-3705-976f-d0d4359ca8e1 | -3.10027 | -48.66889 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468ba1a4-6299-38f5-b60b-5cec8022109c | -3.46077 | -47.67131 | 2024-10-21 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dc0be0a-0264-35e4-a93f-dc22cf5a1a29 | -3.34094 | -49.01971 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c754d5c-8880-3814-8fba-76aadbac783c | -3.33818 | -49.01575 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6c24f8-9132-3f8d-8ef2-b7d61d19ffa1 | -3.29593 | -49.06906 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec87cca4-6770-37f5-b055-dfa16b43c342 | -3.2216 | -48.6108 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 704fbaa1-7ac9-38e7-9c7d-97520ae9d3cc | -3.22106 | -48.61423 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf8d4b7-cb1d-3b01-8c7f-54944ea3b8b3 | -3.2183 | -48.61029 | 2024-10-21 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
