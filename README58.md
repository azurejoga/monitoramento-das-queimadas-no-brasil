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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a822bc6-ec37-3e90-b33b-36e14bec0611 | -9.81992 | -49.57071 | 2025-10-24 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 1bd717af-52f4-3041-8a93-408e810db900 | -8.55176 | -48.26431 | 2025-10-24 12:19:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef6d9b85-e1ac-33ee-bd99-c54ab366ca37 | -12.07934 | -46.43332 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| efb60349-7f0e-3474-a173-8a9981f20058 | -12.63566 | -44.1404 | 2025-10-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8e995409-102d-3fb7-ae7c-a4aaaecc778e | -8.11868 | -47.04129 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 07880768-09dd-32e1-8d76-e8e2f0f2f7b8 | -8.0067 | -49.71717 | 2025-10-24 12:19:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bf80ea55-a55d-3bee-b00d-f4f4cde3b228 | -9.21585 | -48.59041 | 2025-10-24 12:19:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c1af4183-e16a-3a0a-830d-d592569479bb | -14.69867 | -52.83016 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c8e6ae9e-e491-3139-8de9-ba11cf8cc90c | -10.61954 | -42.31241 | 2025-10-24 12:19:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 154.2 |
| 65a04d13-fb11-34d5-87e7-3c0eef4b18bf | -10.54056 | -50.18808 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 34be6d3c-8415-3c90-8e97-732e7670c301 | -11.35696 | -49.79016 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a727c4f4-7474-3312-8f3b-b31425b8b17d | -8.24516 | -47.18418 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0576aa3-27c8-35a5-a52a-b61bcc21a800 | -12.36815 | -51.46336 | 2025-10-24 12:19:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2ace5302-4cf8-3100-9616-b65194ea6126 | -12.10915 | -46.70636 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 1280e4dc-5b93-3de0-abbb-e24b7624be9b | -12.18317 | -49.43889 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| effb21ab-b28f-3f10-8b88-d52e63c285b0 | -12.11068 | -47.02422 | 2025-10-24 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7802ee23-6f65-368e-879c-0dba0566fe0f | -9.59199 | -46.91841 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| fa8f7c67-0ca1-3ddf-8e3d-bf2ef741b700 | -13.33511 | -47.9661 | 2025-10-24 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3a3f111b-42da-3641-b976-0497d979d4c0 | -8.17209 | -47.04886 | 2025-10-24 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e3e286f9-5b98-3910-9456-211a41295630 | -9.98306 | -47.74471 | 2025-10-24 12:19:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e7f468db-2b2c-327c-955a-ba368555dbbf | -12.11053 | -46.69634 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d1a5db20-7088-314a-871b-b19ae3247a48 | -17.24741 | -48.1074 | 2025-10-24 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7295e4d2-2b1d-3b9d-8736-c652c6a29475 | -13.9207 | -48.39382 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f8ca044-80e5-3594-87f1-b9ad6ea8a0c8 | -14.74201 | -46.60674 | 2025-10-24 12:19:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f2314023-cee5-3595-8532-a9093e15d2dd | -10.64906 | -47.85526 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 457bd262-6d20-35c6-a494-392322669f7d | -13.92198 | -48.38464 | 2025-10-24 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5b3a5d3e-d8eb-39d9-b752-39e43318e772 | -9.56221 | -49.62817 | 2025-10-24 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e046a86d-52cb-34ae-9075-22af8a15b23f | -13.27634 | -47.98882 | 2025-10-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aae1e37e-a3eb-3e92-8b46-299a8dc1c70d | -11.00612 | -47.81097 | 2025-10-24 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9eb98505-208f-36ae-86cb-0ded7a26d2be | -7.65936 | -47.67894 | 2025-10-24 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 14464a94-fd3e-3a36-b68e-43ef10ac4798 | -10.87966 | -48.053 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 825b5142-a32a-3bc4-b607-90e36eaeafe2 | -15.23122 | -47.9056 | 2025-10-24 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d75a3148-a63a-3295-bf3f-9e571716403b | -8.73926 | -45.83696 | 2025-10-24 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 23f08b99-7349-381a-80fd-39b447b19c9a | -10.53431 | -50.16743 | 2025-10-24 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 958949f7-842c-3948-ad25-615ac87194bc | -10.94644 | -50.38309 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 82ae0780-ce95-3566-be00-c25765f00313 | -10.99263 | -50.37662 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 66fd0352-1774-30d9-822c-88eb4a8ab89d | -9.11296 | -46.05185 | 2025-10-24 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 682abc50-4573-31b3-9ad7-35e31c4c4d90 | -9.25591 | -45.3628 | 2025-10-24 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 94a79ecd-3b3a-352c-9784-9a8389d52b5f | -7.4931 | -47.02979 | 2025-10-24 12:19:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 78eaba44-edcc-3c92-bdb2-c04e41ae7a72 | -9.82129 | -49.56144 | 2025-10-24 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 31b4b013-d763-3f85-9564-ceb5d0c5d5fa | -13.12984 | -47.11367 | 2025-10-24 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ec3f9d7-3480-334b-92e2-ca85dcdfa07d | -9.62348 | -46.89143 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9dceed06-2e61-303c-a80d-1249abd87e29 | -15.1352 | -47.9347 | 2025-10-24 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 520122ca-8c12-3ebe-b30b-cd7775181cc0 | -7.46365 | -49.39946 | 2025-10-24 12:19:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5ce3ea22-9883-3748-9925-d7a541b77d84 | -7.77762 | -45.39907 | 2025-10-24 12:19:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 64cc4d14-aa3b-30a9-8431-8784752126c3 | -12.13232 | -46.72554 | 2025-10-24 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9f6fb2be-7d52-310a-bd5f-99de9ffec2d3 | -11.57916 | -49.53511 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ba9fca3d-354c-396e-8da6-d32972b666df | -11.34471 | -51.44611 | 2025-10-24 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 01b64dd4-c313-385d-9dd9-3027350f9bac | -8.65915 | -44.79517 | 2025-10-24 12:19:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d52387c8-ef6d-3d2c-9c7c-1148d016cd05 | -12.16545 | -49.43628 | 2025-10-24 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1af74eb9-8c33-3787-9a92-5bdeb6b3bfec | -9.55871 | -46.69386 | 2025-10-24 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 77b4dffe-15c5-3a3e-856e-cd2c1d0801e1 | -10.55942 | -48.9966 | 2025-10-24 12:19:00 | TERRA_M-T | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9bd98e09-400e-3b01-aad9-69e52f6e3b78 | -15.36007 | -42.90705 | 2025-10-24 12:19:00 | TERRA_M-T | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ee7e6ba7-4bc5-3492-ad71-298fbfe5023b | -10.93503 | -48.05804 | 2025-10-24 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f432cd94-6c7d-33d6-a9f9-b9713bfb55c0 | -10.97056 | -50.27409 | 2025-10-24 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b6a3fc79-5b78-3a32-b361-c60801a97648 | -7.5547 | -47.37213 | 2025-10-24 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 590eda3f-f69c-391e-be97-d47b6a8e7bfb | -9.25929 | -46.46273 | 2025-10-24 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 07c14ce0-ad86-3de8-8ff1-f581103cbd9d | -12.067 | -46.4189 | 2025-10-24 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ea8c6c75-5f7b-3591-b6d5-3f8ec238bc62 | -10.9387 | -50.3835 | 2025-10-24 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fe8eccb7-fbe8-3add-b971-401c5b546042 | -15.1405 | -43.8014 | 2025-10-24 12:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 279eab11-9519-3d16-b373-a20fbd043413 | -12.7786 | -47.3752 | 2025-10-24 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a9351bec-634d-3df0-baab-4979ad0f3f97 | -11.9635 | -49.1858 | 2025-10-24 12:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cfe3d443-d471-3a33-8b93-da1b2085ef15 | -10.9577 | -50.3815 | 2025-10-24 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c2bdaa70-3a84-36c4-878e-d5693001d65f | -22.46169 | -51.58979 | 2025-10-24 12:21:00 | TERRA_M-T | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 935ba664-81ba-3cc9-9583-b3d99ac69d85 | -23.41038 | -46.82895 | 2025-10-24 12:21:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 1fa30a50-692f-3ea7-9037-1e2f6ec4d08d | -21.38725 | -51.36666 | 2025-10-24 12:21:00 | TERRA_M-T | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| d02278fc-8e23-30b6-861e-4433c95eadd5 | -18.46099 | -44.43431 | 2025-10-24 12:21:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cb09b9d5-ab9a-3fec-b0e5-70e9b80a4ef8 | -23.3629 | -47.51436 | 2025-10-24 12:21:00 | TERRA_M-T | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 969d9b08-770c-31a7-a9a1-15b1c5650960 | -21.90486 | -47.04184 | 2025-10-24 12:21:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 91bbdf73-03a3-314b-8356-a7261c23be79 | -22.87917 | -46.35945 | 2025-10-24 12:21:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 8b6969b4-8ab5-3816-828f-049a7fd6bae4 | -24.81832 | -50.22663 | 2025-10-24 12:21:00 | TERRA_M-T | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 34c43e96-d31e-3fad-8444-b8bf2a66bb8b | -23.15569 | -47.03398 | 2025-10-24 12:21:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| c7b6db1c-33f2-31dc-8eaf-9883ccd261b2 | -18.91149 | -48.18745 | 2025-10-24 12:21:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3edcd84a-7848-3303-99a7-d33b3c1b9359 | -21.23499 | -45.76036 | 2025-10-24 12:21:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 87896ba2-226b-3f9c-9231-ad0470d69e28 | -18.57122 | -51.31424 | 2025-10-24 12:21:00 | TERRA_M-T | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 33bf6567-83ca-34fb-90a2-6f88906bd680 | -25.00485 | -49.37572 | 2025-10-24 12:21:00 | TERRA_M-T | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 7a261ec7-a34a-3248-af2a-89d4497e7fa4 | -19.02448 | -49.24905 | 2025-10-24 12:21:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cde77b2f-c42f-324d-82cb-f067c5e137e0 | -18.45287 | -44.44537 | 2025-10-24 12:21:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 03023270-b991-37e0-a2c1-a9a706a536b5 | -22.46029 | -51.59937 | 2025-10-24 12:21:00 | TERRA_M-T | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 3a0e6ff1-b501-3f25-a3ec-aab6bea4732d | -23.26516 | -46.59221 | 2025-10-24 12:21:00 | TERRA_M-T | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 2ce18b3a-49f5-35b0-98c4-08741c2c28b4 | -18.45492 | -44.42772 | 2025-10-24 12:21:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 34.3 |
| f5ed9f64-cc01-3aa4-a09b-c40e5880f9d9 | -18.45907 | -44.45197 | 2025-10-24 12:21:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8c225b87-f115-3f4f-84a2-604afbf87e2a | -22.3106 | -49.0247 | 2025-10-24 12:21:00 | TERRA_M-T | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96131ad1-237d-34e0-9733-a182e33bef71 | -19.0798 | -50.92787 | 2025-10-24 12:21:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bd2ce549-aa85-3b20-a759-1d95b6f774d9 | -19.76316 | -44.64125 | 2025-10-24 12:21:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 8273a7bf-0f20-3284-af4b-f67085f61a43 | -18.80979 | -48.26008 | 2025-10-24 12:21:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 43ffeb83-5e9f-3713-aab2-e4387a85c420 | -18.05417 | -52.23059 | 2025-10-24 12:21:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b33a9e9c-1882-3cd8-bc58-622b5dea74c0 | -19.18487 | -50.77852 | 2025-10-24 12:21:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 87164a45-6622-37c0-8c6a-4c9e3fa2e63a | -19.28863 | -49.33635 | 2025-10-24 12:21:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 473946c9-e1d2-3f77-988d-b09d0d8ba6b3 | -18.91011 | -48.19776 | 2025-10-24 12:21:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 87bc1f7d-e4e7-38da-ab06-9ab65896702c | -22.14948 | -44.82536 | 2025-10-24 12:21:00 | TERRA_M-T | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| bff2a76d-fdfe-39f0-8a03-46d934acb92f | -19.32643 | -50.12237 | 2025-10-24 12:21:00 | TERRA_M-T | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 691b5716-b650-32a0-9145-132ed64e03cc | -24.81698 | -50.23668 | 2025-10-24 12:21:00 | TERRA_M-T | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 97fa0d39-5049-34bf-b7d1-0da9e385f2b9 | -29.59977 | -51.74456 | 2025-10-24 12:23:00 | TERRA_M-T | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| fda8d9bc-3d4c-36d6-8440-554f0b8f0853 | -26.63978 | -48.69867 | 2025-10-24 12:23:00 | TERRA_M-T | BARRA VELHA | SANTA CATARINA | Brasil | 4202107 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 417c8de0-1a16-3ca6-9b67-7b6fc449d567 | -29.55036 | -50.49092 | 2025-10-24 12:23:00 | TERRA_M-T | ROLANTE | RIO GRANDE DO SUL | Brasil | 4316006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1033e865-377d-3356-bddd-dff34502dd89 | -29.03176 | -51.17757 | 2025-10-24 12:23:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3183183f-44d6-3ab2-9b97-3c9a8d02281f | -29.59837 | -51.75491 | 2025-10-24 12:23:00 | TERRA_M-T | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3470275b-f9e2-356a-bf3e-fc1db6052835 | -26.80542 | -51.04405 | 2025-10-24 12:23:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 34d4308b-3cb9-315b-8cf1-ddbe7e480e91 | -26.88409 | -51.21393 | 2025-10-24 12:23:00 | TERRA_M-T | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |


[Clique aqui para ver as próximas entradas](README59.md)
