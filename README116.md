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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eccc3f8b-6775-37f8-a4e5-37eaffca2074 | -5.8292 | -45.3729 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1a691eff-ac80-307f-bc0e-91763e2b46ae | -5.7154 | -45.5613 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| fa9df31c-e713-31d3-b215-d95f7142cdd0 | -8.8842 | -45.822 | 2025-09-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 1892630c-7c0f-32e4-b1ce-d4427e05a051 | -9.1373 | -49.6659 | 2025-09-03 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e97cdf92-1a2e-3b7c-92ab-6ba9dc929e33 | -11.8537 | -51.4106 | 2025-09-03 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| eb390765-e488-3c9f-b0f0-fd14a0f3bff3 | -8.0197 | -44.1072 | 2025-09-03 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9137cdca-78f2-3ac9-a109-9c9a58e9dad7 | -11.0181 | -51.5001 | 2025-09-03 13:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 4ee487c5-a413-38ad-9337-81d974c0121e | -7.5998 | -46.2185 | 2025-09-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0a1c7bbd-6536-3b96-8c83-20ab195110cf | -15.0254 | -50.071 | 2025-09-03 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 36c8794e-8e6c-3e01-b233-342a8205d71b | -15.1771 | -52.356 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 8e7711d0-5e21-3278-8c2a-bd9015b19c1e | -6.0699 | -45.6259 | 2025-09-03 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 41b58f22-b4f0-39f9-bb1c-560750bf664d | -7.5157 | -45.3478 | 2025-09-03 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 94f0d1c7-949d-3de5-aa57-0445dcbefa03 | -8.0203 | -44.0608 | 2025-09-03 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7097c774-48ea-3ac9-9016-20336ebb2fa5 | -10.4853 | -50.346 | 2025-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1de76e4f-8b54-3e48-9774-a6ebbb7f2195 | -7.4969 | -45.3495 | 2025-09-03 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 3768cd4f-acd7-34d2-8a00-4dbcfbcc4e51 | -6.2489 | -42.592 | 2025-09-03 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 6ab6412a-f168-353e-8ec2-c15f93ff3ad7 | -6.3502 | -45.6498 | 2025-09-03 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| d29bff75-8451-33ad-9ba0-d96cbc433a73 | -8.0796 | -45.3617 | 2025-09-03 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 376.5 |
| d5cfce2f-1ef8-3eb3-8135-1eaab60d6fb6 | -11.6647 | -57.3533 | 2025-09-03 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 432f722f-5e0d-382e-8fb2-d29afa7f3bc9 | -16.8532 | -49.6196 | 2025-09-03 13:30:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| aeea28f9-1532-3351-8e6b-da8b7c62a013 | -8.3644 | -48.3116 | 2025-09-03 13:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 586618bc-6736-3073-8549-2792c1a6e08a | -6.7595 | -45.9095 | 2025-09-03 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8a23e407-3164-3f52-8efa-6698cb9d42c1 | -7.5302 | -47.4443 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 53f18e06-63ef-3a8d-b430-2c9b6a251e72 | -10.9524 | -50.7658 | 2025-09-03 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| de272051-e3cc-3916-91a3-a3f252b41450 | -5.8297 | -45.3051 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2a3243da-cdbc-3dbc-832a-1ddcae288794 | -9.7613 | -49.4337 | 2025-09-03 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| cf962c84-c3b9-321d-b3d1-25a8dce1a0ff | -11.3901 | -43.5602 | 2025-09-03 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| f99fd23b-7ba6-3ca2-b54f-32133c1d29b1 | -7.484 | -44.8272 | 2025-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d121b6c2-6527-340a-9251-1e877171378b | -6.204 | -43.3241 | 2025-09-03 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 67af1a4a-bbff-367e-b097-44fb8edd924e | -8.8839 | -45.8446 | 2025-09-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c6e7342b-b6d3-3d42-bc6a-0c8e9d504bcb | -15.0258 | -50.0491 | 2025-09-03 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f51efe0d-d7f8-3b6b-967d-9c5c20938d5e | -16.3145 | -52.9628 | 2025-09-03 13:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e3875a0b-6f5d-325b-959e-0c3ee892e034 | -11.3897 | -43.5839 | 2025-09-03 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3a211b09-4774-3ea6-8154-c88b3c56b038 | -14.0703 | -44.5508 | 2025-09-03 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9d7433cc-235f-33e4-9719-903a0b67c4d6 | -9.7615 | -49.4121 | 2025-09-03 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6f47cfc0-d9b3-3abd-b279-90cdcc56d7fc | -14.5801 | -48.0398 | 2025-09-03 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c03eaeb7-1a01-3fa0-b07c-fc2b63696c20 | -6.35 | -45.6723 | 2025-09-03 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ec0056a0-4229-309e-837c-0c6088d999bf | -6.0784 | -44.6961 | 2025-09-03 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| efb21557-3b97-3312-947f-e15a8397873d | -5.7181 | -45.2453 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 305.0 |
| d8fd16de-5f1f-3879-8c57-1a4cdaf114d0 | -12.824 | -48.06 | 2025-09-03 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e67d9e32-3f9f-31ce-878d-3c5e8e4b7e30 | -6.7407 | -45.911 | 2025-09-03 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c308cc96-9a39-3953-a2ab-00636178cdd3 | -8.0794 | -45.3844 | 2025-09-03 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 42e3f641-2494-3f99-8fdb-b4958d81f89f | -10.0932 | -54.7667 | 2025-09-03 13:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| c539dc8a-f518-3519-856b-b20415f062a7 | -5.8455 | -45.6421 | 2025-09-03 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 202.3 |
| d04e0cca-b0ff-3d1e-8004-71978863775a | -12.7926 | -47.6638 | 2025-09-03 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b1a3c9d3-01a8-3d79-8548-03ef8d6abb91 | -6.7928 | -44.4776 | 2025-09-03 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5199cb24-3828-3e29-a76a-8b5de9cdc428 | -11.3893 | -43.6075 | 2025-09-03 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 8a246958-948f-3c61-a921-46a480c2f2b6 | -6.6982 | -48.4035 | 2025-09-03 13:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c253ea18-95b8-37ed-8981-e03498c81066 | -5.7183 | -45.2226 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| bedeaa6e-343f-3477-85b7-909ce0efc919 | -8.8845 | -45.7994 | 2025-09-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f9aa89f5-58d3-39e5-96d9-e05e538a4f2b | -11.672 | -52.168 | 2025-09-03 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 183.2 |
| e80d6ac1-2584-321d-9cd8-fbea74d4a02b | -9.6232 | -47.0416 | 2025-09-03 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9e063b56-0d0e-37ef-a48d-a349009caaea | -11.1224 | -44.6521 | 2025-09-03 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c5da9e78-8823-38a0-a4ed-ec0cba7fce8e | -7.4842 | -44.8043 | 2025-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 285a6b1f-73b5-37d3-9e23-270f7c49ab8b | -8.8653 | -45.824 | 2025-09-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 6c01129c-3eac-3602-b80c-503a320570ae | -9.7427 | -49.414 | 2025-09-03 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bb9fe88f-1bea-3225-8561-f00e1f672df2 | -11.6165 | -52.0689 | 2025-09-03 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 7f9a5a59-dbb1-3c3f-93ea-e185ed7099e6 | -9.402 | -48.0585 | 2025-09-03 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 82d76261-b5e8-33e0-8fcb-d6f139493885 | -9.6229 | -47.0638 | 2025-09-03 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| f1007e74-40e8-3aae-9094-35688231a80d | -15.1221 | -48.1527 | 2025-09-03 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bf41754f-15a8-3b72-ab57-76d08c886993 | -15.1576 | -52.3586 | 2025-09-03 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 17c1e1ca-da59-37e3-90b9-4dea85a94fa1 | -8.2006 | -49.5559 | 2025-09-03 13:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 59fd18bf-71bf-31f5-a73e-58421cf0b7f0 | -12.793 | -47.6415 | 2025-09-03 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a69b02e4-1ef2-32b8-8427-28756ec1b2ea | -5.7152 | -45.5838 | 2025-09-03 13:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 445f8822-279b-30f5-8a67-c244422b99ac | -9.6226 | -47.0861 | 2025-09-03 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| d23dd3a5-a066-3ce4-bc7b-9d801f04a06f | -6.1234 | -45.9139 | 2025-09-03 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8e46faea-3b54-31e8-a809-4a4a94415b64 | -11.6836 | -57.3518 | 2025-09-03 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 456b1878-8416-314a-8f5f-9baf45b42e6e | -6.797 | -44.0859 | 2025-09-03 13:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7262f8ca-cda4-386c-8200-ea428903b61f | -11.8533 | -51.4318 | 2025-09-03 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ff2b4a72-82e7-3880-a670-9e2f9deb2466 | -10.1454 | -46.265 | 2025-09-03 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1eab8a9a-6941-3e86-b643-997bf12f49c2 | -10.9326 | -50.8316 | 2025-09-03 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 848f8c8a-38f2-3d06-b1b9-06026943417d | -8.3832 | -48.3099 | 2025-09-03 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b60947c4-db88-3322-9c6b-cc4b72ec9bcc | -6.0699 | -45.6259 | 2025-09-03 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 39ad8df7-b837-368f-b43d-88a68a8bfe57 | -9.9235 | -45.885 | 2025-09-03 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3a03ad11-407b-3554-9858-58125f2ffbc2 | -8.8839 | -45.8446 | 2025-09-03 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 031d7adc-4f16-3b08-8eaa-f19f9374f682 | -15.0254 | -50.071 | 2025-09-03 13:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ef96651a-3154-3982-bc10-f15383b9e3c3 | -5.7154 | -45.5613 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| a82a4704-a13b-319b-bfbe-349b4f42b8b6 | -5.7152 | -45.5838 | 2025-09-03 13:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f8a61a4d-92e5-3b3e-a528-90b47231db2d | -7.4842 | -44.8043 | 2025-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d0ec1b25-6729-3fab-afcf-913b3146ae25 | -9.1373 | -49.6659 | 2025-09-03 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 433d002c-d4ea-3351-93a6-6be718c78eb9 | -10.4816 | -53.6527 | 2025-09-03 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 34f0b726-176d-3b01-b971-7c13f45b615e | -6.3687 | -45.6709 | 2025-09-03 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e52ca812-a1e6-3ab4-9c90-59dc42079b63 | -6.797 | -44.0859 | 2025-09-03 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fa4b85fd-d5a8-3636-876e-0695a7f75410 | -6.0291 | -46.0103 | 2025-09-03 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 693865e9-db4c-3052-b31b-265b680f79f7 | -14.4075 | -53.2803 | 2025-09-03 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 32ef752c-e07a-34f7-b247-13e019450407 | -11.3901 | -43.5602 | 2025-09-03 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 91e23994-d02a-3fe3-8c1a-9d7915e7e437 | -10.0932 | -54.7667 | 2025-09-03 13:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| b9c9852b-28ba-3744-9e50-5b82581450fb | -7.5157 | -45.3478 | 2025-09-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| df8d5642-a616-3c8d-adc4-b2cf6faa27bc | -6.35 | -45.6723 | 2025-09-03 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 3f6a6eca-7149-3465-904a-4bec6ff4a140 | -6.7967 | -44.1091 | 2025-09-03 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1a413a88-b473-3b59-9be5-1d24977a2a84 | -11.8708 | -51.5357 | 2025-09-03 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 3c780ecc-dbdb-32f3-9ab0-85c62f49f584 | -9.7427 | -49.414 | 2025-09-03 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f574c714-7689-366e-b3e4-5e032f28d6b7 | -13.5162 | -47.0393 | 2025-09-03 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 1ef493e0-d177-3505-8e6f-c4eaaa1b82a8 | -7.4966 | -45.3722 | 2025-09-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| f208e152-14ef-396d-ace1-24f2f6769a60 | -10.9136 | -50.8336 | 2025-09-03 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e923bce4-efe7-3820-8137-07703f147726 | -11.8843 | -50.6197 | 2025-09-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 3f47f099-b9cf-3ee3-ae65-5463e5f9d33b | -11.6836 | -57.3518 | 2025-09-03 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| d3fe6ae9-bb28-3ba5-931b-f4724627635f | -6.7407 | -45.911 | 2025-09-03 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6cb34d4d-77be-356c-9cdb-a42db1839b48 | -11.8537 | -51.4106 | 2025-09-03 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| f00df042-a4cf-3677-a4cc-c26a1a868a57 | -8.0608 | -45.3636 | 2025-09-03 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |


[Clique aqui para ver as próximas entradas](README117.md)
