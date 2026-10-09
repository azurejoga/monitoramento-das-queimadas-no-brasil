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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1b156d0-a9e6-3ac9-bfd8-4cca86e1220b | -5.9682 | -55.34731 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 940a88b6-4150-3367-9240-8da3bf8ee8f0 | -12.24174 | -57.09859 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a97aec2-5ca1-32d8-9652-e4bed9201305 | -12.02066 | -43.49089 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62af3732-1975-3aa0-9100-3913738d22a7 | -8.73242 | -45.13816 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 313d9ae2-c627-35ef-9b6f-bb1b05246ce6 | -7.18612 | -52.61845 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20ced204-69a7-3bb0-ae6a-aca59acaf0ed | -6.041 | -53.48722 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90a70de4-293c-3cf2-9a75-d7390b5c5fa1 | -12.2081 | -57.10263 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdb049bb-5b93-3a2b-ab20-2bbb7165cc22 | -7.75445 | -54.95332 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e339cdf7-6446-3032-913e-4258f05bfffb | -7.23762 | -45.99984 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 879afe20-f2d0-3039-966c-2e828db5f178 | -10.46923 | -47.8601 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e2fd654-7c9b-3330-8574-3358bd734a10 | -6.09739 | -55.69844 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74131627-fe18-3483-924c-47f05940c2ef | -11.24323 | -46.30541 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 786049c1-4e31-38ae-a885-0382edfda3f8 | -12.21955 | -57.13511 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c53ecc22-afc9-36b1-b9e3-93ebb660380d | -13.40818 | -39.79727 | 2026-10-09 04:27:00 | NOAA-21 | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6b77f0c9-aa2b-3bbe-b8df-fc2af6a920af | -10.85114 | -59.11714 | 2026-10-09 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f2f763-a10c-3c81-8ce8-640c5f0adc69 | -10.88984 | -48.51097 | 2026-10-09 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3a39262-9c86-3407-ad63-05b2849a33d2 | -6.45609 | -55.49411 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c645bda-622c-3b4a-963f-77fd93e97e79 | -7.04981 | -45.43105 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca0a9f66-4628-3cdb-9a3c-b11c1f512ab6 | -9.86585 | -44.87159 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2e1161a-b0cc-3941-86bb-b689589c08d9 | -6.49831 | -55.31605 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee20f9e7-1f77-3e3c-bf76-f8e1869fda31 | -12.21876 | -57.13223 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08d185c7-7229-39a5-b262-bc4b356f53e9 | -11.7286 | -46.73598 | 2026-10-09 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62191371-6e2f-3d0d-934e-2df45a1ef825 | -11.0159 | -45.43239 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0fcfe866-e555-3203-8243-a3cd7eff74c3 | -11.60985 | -43.71388 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12226576-e8d0-3390-891b-0d53d696aee0 | -10.28349 | -43.93596 | 2026-10-09 04:27:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94e21190-930e-36d8-9764-938bdd13f06c | -9.29367 | -47.4345 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08e7c6b6-c63c-3929-8f5a-1066101589b4 | -8.17524 | -54.72587 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ab27eab-f0e2-3610-b1a2-160e39e38d5d | -8.32352 | -45.01277 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b7e8386-974a-36ba-acd5-050319886880 | -11.11856 | -44.00607 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 766cfb87-d554-3741-81cb-25836c9f67b7 | -7.3774 | -44.02962 | 2026-10-09 04:27:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e8959f5-8503-3a86-b4b8-99be06528992 | -8.22618 | -46.40442 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d2dac1f3-1524-32f2-ae3d-482ef71ec583 | -11.00499 | -45.41145 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5432c59b-2b1d-3e5e-aec8-7be739495e12 | -7.29764 | -46.16212 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e2cbbed-7a9b-3ae7-b3a2-a30bc6eced8f | -8.98842 | -47.5386 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dbc0a65-78a3-3fd7-ab2e-8c30b279700e | -6.00094 | -53.4998 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 451b8f6a-28f3-315d-a18c-052f83666fe1 | -11.19379 | -45.29447 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b0d0cb8-344c-3d64-b510-fdbf09fbee18 | -11.13551 | -47.69228 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9394328a-5e5b-3404-8181-b62c00fb63fb | -8.73868 | -45.14291 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f7be853-d483-3c96-9260-b358187550cc | -7.47852 | -42.84222 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9c0c01e-5563-382e-b791-d871362fd7ea | -10.75105 | -46.59357 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c5c52af-bb0c-3851-8130-6cc8b826a436 | -8.72227 | -45.15935 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72e5203d-beea-3c3e-8ed0-93f265f797c8 | -13.6375 | -44.41993 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f502a4c-28f3-334d-a5ea-9d1120220acf | -12.22172 | -44.69677 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c436ab12-3ea4-3298-8de5-8fc9fc4cb3bf | -11.2139 | -45.25396 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c325b935-1224-380f-9e7b-9c86c29a8164 | -11.61428 | -43.7098 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a9b398f-434a-34bc-ae42-9f71e7339cc5 | -13.26382 | -43.99854 | 2026-10-09 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7ba0d8b-443b-37f2-a825-6c9d93ba50ba | -5.88621 | -53.62328 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64665120-f67a-3824-abbd-ba4c43bf5b3b | -6.85848 | -52.83665 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68112043-59a7-3263-b41f-febe421a3668 | -7.51561 | -45.7637 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5acb67ad-619e-3192-b83f-630847f63a15 | -13.5552 | -49.15266 | 2026-10-09 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08ff6a37-5991-3f7b-bfaa-5e6899b767bb | -7.29817 | -46.15865 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfdb6ceb-93fa-36ac-9ff2-c50a45b45ab0 | -11.08845 | -45.15193 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80661ce5-4ed1-3004-95c0-bbf606ef88f6 | -9.22488 | -45.65849 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cbb1fb8-0060-390c-be7b-6a48ca373dfa | -8.59378 | -44.00317 | 2026-10-09 04:27:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f33de03a-1cbc-39c2-b569-553635920f8d | -11.7676 | -43.53094 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6209f57a-3246-30f6-9b61-c1126c1f1671 | -11.59923 | -43.70789 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b58877a-abfc-32e0-a0d5-c57b15cb81a0 | -8.91225 | -45.22607 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 06dffc3c-db7f-36b8-9953-4f0a18bf241c | -5.96327 | -55.37549 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cff6a31c-bae4-3167-a319-6aadc6bff340 | -8.9004 | -45.23557 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4975f1-9a35-34f4-bfc1-4039f048bfa1 | -7.61759 | -46.53582 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4fee003-5944-3c3b-9ca5-75ae5fe11c8a | -8.67787 | -47.08693 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10b4af27-7268-3039-a79b-9018d10d26bf | -12.22724 | -57.08876 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1a82fb24-f00e-3924-981c-89a84a76bde5 | -8.90272 | -44.93789 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b41c5eb0-6d2e-3db4-8b39-e37de23bc7af | -12.21865 | -57.11071 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1692bc5d-3e29-34d2-9bc4-c7d3550fd45b | -7.48669 | -42.83873 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 94d4ea4b-de5f-3f33-87e6-3326adccd123 | -12.21406 | -57.10018 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f92003c-2aa7-30e7-a9ea-dc0ef35c7595 | -9.04803 | -47.74122 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ab8732f-ee76-3571-9106-6aa1b0edea68 | -9.29642 | -47.4385 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb04a35e-59ce-36bd-a70d-f1d8a9108cab | -5.71813 | -53.49534 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ee707c90-43d2-38d1-99bf-3925e8efd0c8 | -12.02809 | -43.43782 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0aca080d-7f42-3cbe-81bc-6295b9b7d792 | -6.49425 | -55.30885 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5028e29f-090a-33c4-927d-64f85c9c92ca | -12.00152 | -43.48833 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6de2bbfa-2d63-3fc1-b4b2-686219163b2e | -11.20654 | -49.41714 | 2026-10-09 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00fb0efc-97fa-3ffb-a5bc-70c4cf136d97 | -13.1963 | -54.37054 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0394c2b9-e436-3eb9-ba77-d2805630cccd | -7.40742 | -44.76191 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9453ee19-e15c-3b0e-9943-13b4ec8e5863 | -12.21716 | -57.0895 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f34caf94-6cbc-37f2-ad15-75be7487fa83 | -8.90711 | -45.21391 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f195113-2683-316f-b3fa-27834aa1acf9 | -11.46351 | -43.38266 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c08a36d9-8762-3a00-8f80-d22215a3aa00 | -11.98049 | -57.61793 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 400c40df-6792-3b1a-9a5d-30de644fd650 | -12.20933 | -57.10204 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f38f220-9bc1-3acd-883b-bd7a00b476c0 | -14.43965 | -43.93129 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b34e8c12-4975-3729-8bfb-19e3c30febce | -10.69976 | -47.77951 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d69d0c55-72a1-3aac-b226-a7dfba1ce724 | -11.20919 | -47.71837 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5e40ca6-40b5-3910-b4e6-fb0d92481a96 | -11.50984 | -48.9549 | 2026-10-09 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd2a2d4d-f531-3dfa-a359-91bbac90a16b | -8.73644 | -45.15772 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e179e813-740d-3128-a5fc-6b9e8ee0f1b1 | -11.19808 | -47.61646 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e86e8b8-fb5e-32a3-b0ac-3330e0baec49 | -8.90316 | -45.21709 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1fbccb52-b637-33aa-ade8-e1a5473d7c91 | -13.16105 | -54.33443 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d63a0310-25ec-3cdc-afe4-71adda088b7e | -11.48432 | -54.61651 | 2026-10-09 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee1ef122-eedd-3376-8e63-380609878d5b | -7.50842 | -45.76619 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0206bf09-53cf-30e4-820b-0de6f24c274e | -13.15804 | -54.35135 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2b30265c-a120-3beb-b35d-9a30d3ca160b | -11.91071 | -46.56717 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36cb171d-84ff-3ab2-b8dd-454269b84cb3 | -7.41424 | -44.76299 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6cf1d9a2-8aef-3194-9080-6394988ea282 | -9.88932 | -50.49053 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e890f954-a525-348b-a90d-e3e9b14c133d | -11.07298 | -44.0883 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33148479-d33d-313f-922c-175577af562c | -11.84327 | -43.59738 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2604b848-542e-3565-a4aa-326836cbfdc6 | -14.43898 | -43.9362 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deeb5343-dde6-388c-9815-e4f573434d88 | -13.85155 | -42.64956 | 2026-10-09 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d69681f-9f20-36c0-afb2-fabb7c2c8e3c | -6.11002 | -52.71452 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c8a9c95-5e1c-3228-b0e6-08225e25e267 | -7.90464 | -54.71933 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README103.md)
