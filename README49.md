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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03c18273-df61-3f4f-845e-9adcc3a2ed90 | -5.18383 | -46.19831 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75c98a23-8e89-346f-9640-cd55f443700c | -5.18273 | -46.20009 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 902f77f8-367c-39f1-b1a2-e839cea75447 | -7.88021 | -45.42439 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77650a6e-2868-357c-9e69-b761ab89055c | -7.59088 | -46.85177 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65a22b0b-c5ab-38df-8e6f-b57566b28c07 | -7.46863 | -46.71339 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1ae7d3d-a496-33a9-be83-6676239003a0 | -7.46826 | -46.71024 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94998d46-53c1-3e46-9d42-3c6ee18dcd4a | -7.46755 | -46.71552 | 2024-10-28 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad5b3f98-f5d6-3bfe-8dd3-266814642eba | -9.00026 | -46.75784 | 2024-10-28 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a5244fb-bcf2-3080-973a-f1c0ca92bcbb | -8.99534 | -46.75721 | 2024-10-28 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a2f701-61c7-3ac2-93a5-addc2ec67f70 | -7.95561 | -46.54111 | 2024-10-28 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8f4cc84c-0687-3a14-a742-39c1d76a7cd5 | -2.05374 | -46.53214 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5276b4f-a0a3-3103-9e35-daa7eac671c2 | -2.03566 | -46.31374 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787da76b-a128-39ef-be31-64cd15bc059e | -2.03504 | -46.31234 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7dcac08-44a6-314b-8c67-1958ec2f8f7d | -2.0311 | -46.31301 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2a5c02-62bd-3d61-8496-160ee9531e09 | -2.02976 | -46.31626 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a5e37e1-3def-3d5a-9eb9-6a30fb91596f | -1.76723 | -47.01979 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d529177-6772-367b-bba6-e07829a5556b | -1.76659 | -47.02391 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82395d4f-b05d-30be-ac39-d6450ad1c08a | -2.55247 | -47.31821 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b7dbd22-f467-3f76-8a4d-47612ecc809e | -2.55187 | -47.32222 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38f17853-9b6e-3b07-99b3-7105fee60a98 | -2.54524 | -47.36651 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e21652b6-5867-390d-aae3-801ef3135d85 | -2.53743 | -47.22604 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b21489c-75fd-3554-a842-4fa411ecea97 | -2.53571 | -47.22368 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d915982-aab7-355c-8178-33ca781de5ba | -2.51788 | -47.35183 | 2024-10-28 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 786262bf-3af6-3e88-996f-8e4cfae91b70 | -3.17043 | -46.60718 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17cde66f-5287-352d-b18d-89a706f3d6cd | -3.16975 | -46.6118 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f4f91c9-6984-31ba-97b5-945baa75546a | -3.16931 | -46.60887 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c4909cd5-0726-3230-af1c-7817e80c58ca | -3.16588 | -46.60645 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 322e72b2-3d3c-31c0-ae3f-008f9907b7d6 | -3.16521 | -46.61109 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c23ae96-a2ed-35f9-9e36-ae28445577eb | -3.16476 | -46.60815 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 078365c5-0c3d-3d0f-944d-d2ac25ea9906 | -2.40955 | -46.7054 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a20c044-1138-339c-a292-1f50a70d5e4f | -2.4089 | -46.70982 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bc31bd4-ca51-3672-8d92-ee3486df1459 | -2.40672 | -46.70346 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de00271c-e800-3825-ab91-e1d75ac9e962 | -2.40574 | -46.7003 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daebd92e-e81a-33ea-9cee-8a4b160f2ebb | -2.39736 | -46.7262 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdff6178-00c3-3e0c-9ce0-a2897069ff0a | -2.32857 | -46.64599 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d752222-c643-3740-b405-3af702593be5 | -2.32476 | -46.64086 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810588f9-b28a-353f-94b1-2ba3e718ae38 | -2.32013 | -46.47608 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3919d4e2-6673-3f7c-96f5-6b829e20251f | -2.31785 | -46.50105 | 2024-10-28 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4f89a87-f531-3f14-bf42-08d0eaca2eb8 | -2.31698 | -46.66235 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ada17673-352e-32cb-ab27-c16edf2e5ba4 | -2.31632 | -46.66679 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e950236-1c2f-3308-bcde-094272bc729a | -2.31184 | -46.66611 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d021ec76-1c85-366e-98dd-d7df62dda514 | -2.30738 | -46.66541 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c38379f4-506c-34fd-8017-01cf61875124 | -2.30357 | -46.66027 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd304f3b-2b2b-33b5-b117-e66b65556172 | -2.2949 | -46.75614 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abc3a4fc-5e58-3941-a575-056ec3782a2d | -2.29363 | -46.75812 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c857b809-5125-3892-a79e-cf3f91c86308 | -2.29286 | -46.65207 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38c0cf4d-5352-3603-9bff-69539b0ab05a | -2.29182 | -46.74675 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7538b38a-5961-3cc0-b145-a2f1b76a15b8 | -2.28978 | -46.75982 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95191577-5077-3ed4-921b-bf8391f76c34 | -2.28919 | -46.75746 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4823afe-ce0e-3db3-87d5-593e7e58d1cb | -2.28907 | -46.64696 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c29a3e5-16a7-36cc-99c3-bf61546dc62e | -2.28839 | -46.65139 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edfaa6d4-c417-3148-a907-437df4062eef | -2.28738 | -46.74606 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17e7fc78-6126-3e01-b4de-0ea9bd4da126 | -2.28534 | -46.75915 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e3b8e43-18dc-3804-bb27-4a665016dfd3 | -2.28433 | -46.13133 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99bfbfc1-f1ba-3a0e-a1ef-7da3b34e4df1 | -2.28391 | -46.65071 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f01db970-ccac-37ee-a9e0-4ddb5d66192f | -2.28013 | -46.64555 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8e41e56-022b-349e-9675-56c02f7cff84 | -2.27002 | -46.77011 | 2024-10-28 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51f2871b-8cc3-3874-8a9f-aa2a0fa7b858 | -2.25077 | -46.25554 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7779205-44cd-32e2-a2f7-03e4b128f2c2 | -2.24617 | -46.25486 | 2024-10-28 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a616112-1bf6-3c66-a72b-9fb931e574c1 | -3.45518 | -46.32796 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdacdeba-4320-3464-a0cf-75b00ea338b9 | -3.45446 | -46.33287 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc24fd69-8fd6-35d2-b4c5-77a636cd1fa8 | -3.4066 | -46.3142 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d6fd706-7be2-393c-936e-34203fd33693 | -3.40587 | -46.31903 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de592dc2-c088-3f79-a343-86cc9fc20d10 | -3.40514 | -46.3239 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36b826fe-8ef3-3ad5-920d-c40cc84b3fc4 | -3.40121 | -46.31834 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75e783c3-55e6-36d1-b8f6-a334465b67f1 | -3.39535 | -46.35728 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf1b8bf7-dfed-36db-8aff-e9ae5b988ee4 | -3.27483 | -46.21762 | 2024-10-28 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 692ecce9-b67b-3662-bc5b-7c04e3bfebc5 | -3.27015 | -46.21687 | 2024-10-28 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6b8fd6e-8496-3250-902a-6f80deb8f219 | -3.24083 | -46.01493 | 2024-10-28 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f21cbc41-1f1f-328e-9bfc-cf11da8ce1fb | -3.23686 | -46.00909 | 2024-10-28 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f03e7a3-ad2c-3e32-8126-bbb5458e230a | -2.72876 | -46.69093 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 836d11cc-4c7f-3c7b-8791-0fece0bd0cd3 | -2.72685 | -46.68812 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4743f80b-7b7b-37ca-bcf2-5ae951bf2e5d | -2.7262 | -46.6926 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e35f0460-ac66-3530-848a-e1975be9f745 | -2.72426 | -46.69026 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2542f67-2b0c-3b41-b7f2-68e2248619b8 | -2.71977 | -46.68959 | 2024-10-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 132badb4-8fd9-3c6b-8e95-66bfc4d94b3e | -4.96461 | -46.49212 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 110138a3-6042-3354-93fd-1c3bafe6068d | -4.9639 | -46.49697 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00b5e93e-bdf0-3acb-aeff-57362376bd52 | -4.9018 | -46.8604 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee4fe235-aa9f-34d0-b815-353ed8fe2f18 | -4.88806 | -46.85815 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32859fa9-fc3b-397b-a83e-4b7633785413 | -4.7733 | -46.39218 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 215fdf3a-eb4a-3cf4-8add-c430381b4ef2 | -4.77257 | -46.39714 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b45a6a20-1ef6-3ef4-87da-e8dd02f2ab6c | -4.77187 | -46.40193 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2da00a7-a928-33ec-a9da-d933736a1af6 | -4.76859 | -46.39127 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 70e69559-03de-351d-836b-7adec19f67bf | -4.76786 | -46.39627 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5948899f-2961-3d72-9437-1de44a3e3a1b | -4.76716 | -46.40112 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0ebfcbcf-289e-38da-837d-086802743c3b | -4.76316 | -46.39539 | 2024-10-28 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0e59bf0b-7c21-3caf-9ecd-0e2d3a527f0e | -4.74147 | -46.80271 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1afe1a6-f856-3665-8c9c-9968221aa994 | -4.73757 | -46.79738 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71f23b9c-2316-39fa-b013-54a9051c4bbc | -4.73689 | -46.80195 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dfcfd6e-0152-3757-bfa9-e052475493c7 | -4.69193 | -46.85272 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e38b5c5-c9d3-3485-baa2-455cd4152cb2 | -4.68319 | -46.66034 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ea72ec9-ae50-33cf-88e5-5789d1144fb3 | -4.68181 | -46.66152 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9b2083c8-622e-32fe-9ca6-8f6a6ce855e6 | -4.67931 | -46.65466 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 561dcae4-7ae3-3733-99b5-4cdf6420b42c | -4.67856 | -46.6596 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f6864f43-9eca-33bb-a102-a1a08078b419 | -4.67789 | -46.65582 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5ebb84ce-c45f-31c0-bb94-308b059db42c | -4.67718 | -46.66077 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cc749edc-e674-33f2-9a70-87051be0a47d | -4.67468 | -46.6539 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d74ca556-23fd-3896-aa97-6fb779ab1aa6 | -4.67393 | -46.65885 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b841b0c8-c398-3b02-ad6a-04d0053ef732 | -4.67326 | -46.65504 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77cdda4e-dcbe-3104-a70b-91cdeed66039 | -4.67255 | -46.66002 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
