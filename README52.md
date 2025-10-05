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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb921916-1194-3b6f-bbed-781e04f26845 | -7.71945 | -42.55886 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e270ba6b-03d7-3a88-b534-de1c8a6b7565 | -7.06166 | -42.78524 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfbcc7a2-4501-3dd9-8d47-b1e79d8778f1 | -6.32205 | -41.62819 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75774154-8e4b-3c4e-a166-f1f632e0600f | -8.91821 | -46.06582 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e571a090-0099-35ff-81ee-4722aee039c6 | -5.47589 | -42.79324 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6f2169c4-db5e-3034-ab65-578ec493810d | -7.47923 | -43.03207 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3c834459-3487-393b-b6ce-fe5b485253b3 | -5.78859 | -45.78296 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac29b475-ef1b-3783-8f72-75b84811b1ad | -7.15858 | -37.10909 | 2025-10-05 03:53:00 | NOAA-20 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 233a9f6a-c265-3a0b-900b-dc1763d0b9cc | -8.12841 | -44.12171 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069d083e-4a5e-3c15-ae65-f6035b032a78 | -10.39031 | -45.39991 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6801b7ec-dd73-330b-a777-e9062dc7402b | -10.39762 | -45.40928 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 47531534-d994-3785-be79-eb375f34a3ff | -6.69917 | -43.8774 | 2025-10-05 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e0203a6-b688-3df4-986b-125ba656cccc | -5.66493 | -42.748 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| efd4e084-599d-3be1-b30f-289b90084402 | -5.5499 | -42.66476 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 945619fa-cd15-306f-8adb-b321c615aa7e | -4.6837 | -46.82629 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6031ed45-e90c-377c-a3b6-07c201e90f8c | -7.03699 | -42.76607 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bcf2eccb-feef-3d16-8af7-ff20757228e3 | -5.96064 | -43.51471 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0e51464-5923-3a67-9d5a-a43601e6aff0 | -5.83151 | -43.3605 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82fa7179-e3b9-3d61-b9a6-395e760fe47f | -5.98332 | -44.35988 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690b7bb4-3ce6-352b-b927-6e53c5419af9 | -10.63922 | -46.3057 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 426773cd-0cd0-35aa-bde2-cb6a3f68284e | -7.74068 | -42.5481 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06711b0c-2842-3cb2-ade4-598ee721b584 | -6.70599 | -42.16506 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7791e56f-6c16-3368-81a1-83268098448a | -9.32539 | -45.66447 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 66ca6eee-815e-3294-be5d-42a7daf2b574 | -7.74071 | -42.52453 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3299db3-64ac-38eb-b428-60829784ca2f | -6.42551 | -44.46758 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31422a8f-6809-30ae-ba49-361a1ef40256 | -6.7262 | -42.15923 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 083327e2-6385-3a4d-9fca-e31bb376609c | -6.35916 | -43.91137 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e2971ef-bd50-3c43-982b-776864da0f28 | -5.91673 | -42.90046 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88a95c39-d7f2-37d4-8d38-714e5d58667c | -6.13874 | -44.63876 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6639e38c-9b2c-3252-9f4e-b6cadbd94286 | -14.582 | -52.4573 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0a56272-5765-3239-bc48-25201755fa5b | -13.14461 | -50.92797 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54250670-15c6-3606-a1b0-4e3204923e92 | -15.26442 | -44.12447 | 2025-10-05 03:55:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a960d12a-8b02-325e-8910-022604496875 | -14.58733 | -52.46346 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8474fd16-8a06-3cd6-93c5-0467572bad91 | -11.85686 | -44.94835 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e6c2da8-38e5-317c-894f-45ec7613dd7d | -11.77841 | -47.5554 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa7f8fdc-8af4-3da7-94c7-6a6244dd710a | -14.33718 | -45.86262 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ceffbea-2204-34ad-85a3-b8bcecae6c3b | -11.797 | -46.81941 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9489b1b8-0846-36dd-b0a1-584d83225203 | -15.36699 | -47.97698 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c45abeab-b0a7-36aa-8698-ea68549e1210 | -18.552 | -41.58059 | 2025-10-05 03:55:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a3dfb02-8a77-369b-bfdb-41e1c87cadc9 | -15.31631 | -47.32358 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddbddbc7-dfce-3373-83c3-af354a64e155 | -12.40995 | -45.15866 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 216497dc-ebc2-3e16-bd66-b8a0e37ca630 | -11.80343 | -46.84895 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06b7684b-77ac-3a3a-a537-ada1dfe33251 | -13.02621 | -42.45406 | 2025-10-05 03:55:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5be35407-b3db-304f-ad1b-6bf1888f18d0 | -11.69618 | -47.49647 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3741a7f-af64-386b-bbf4-6493dc7e9b8c | -12.45 | -44.74097 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ccfd7e1e-349d-3a52-8b77-78b1a9ad8e9b | -11.09072 | -47.74793 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a86bd553-d0da-35ba-a665-8bb42c0af1c7 | -14.68368 | -48.33833 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02b96d7b-0769-3942-aed6-9d3c9ad33ed1 | -13.74101 | -48.07797 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a345ea4-a513-3034-b6f7-b4294ec51c66 | -11.25432 | -47.7856 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc71e40-a97c-3f43-96ab-5fdbcb0da728 | -15.71084 | -46.27825 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4aec030-c6fd-3ea2-82af-46aac79d8d74 | -10.83511 | -46.58075 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3f3b510-72ec-3df1-9ba0-1ede67866f3e | -14.41711 | -46.18229 | 2025-10-05 03:55:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4c67245-4ffc-3c0e-b780-1fdb43bc5852 | -15.54851 | -46.84402 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 821259f3-ec0b-39e2-8cc5-50ddf77ee9d2 | -12.10393 | -43.452 | 2025-10-05 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74580583-334f-3587-be9c-2896e4f3b804 | -12.14111 | -50.93098 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 54c22e92-348f-3d45-9233-7dd6f9dbd53b | -13.28645 | -47.62085 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 501627d5-98b0-3e9a-8cc7-d49172a3bc87 | -12.13603 | -50.92504 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f3e6c92-57a9-3c28-ac0a-c2972e68a488 | -14.66455 | -48.30653 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f20fa325-dc53-36a8-ac17-19c3bd11a2d3 | -14.74689 | -48.40611 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41226a74-8a40-34e9-be10-62af8ca1c8a5 | -13.09952 | -47.85674 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1492e0a-94ed-3830-8384-f84cf0d9ef07 | -14.68748 | -48.34482 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a94d7cc-3846-3af3-9c18-a17c47c82e58 | -10.99825 | -46.51729 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 817af8d4-feb3-35b6-b35e-3bd8192e4a61 | -12.88524 | -47.28718 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b99d3f5e-75dd-3510-9a75-14148ab14f86 | -11.81504 | -45.0627 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85e13341-cfdd-3851-928a-1c4c5e6c3c03 | -11.715 | -45.35322 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bab5b32-5a47-3567-9c2f-b2bc21bedc31 | -13.27596 | -47.62371 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0705796-4c54-339e-bcdf-507b117d90b4 | -11.77824 | -47.93747 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c9c6e2-e9a6-34df-97cb-00c1ee1e28ca | -14.88271 | -48.26329 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f51c60c0-14c9-323f-a8a7-507dc3a68229 | -14.45987 | -46.33437 | 2025-10-05 03:55:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc89312-d3a7-36e6-a7bb-33ebdef16ce5 | -11.78438 | -47.55075 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d48f9be7-d507-3d6a-8b3a-8b2242257386 | -13.43059 | -47.27389 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bfb2c97-d73a-33ee-b504-1b3223ae734b | -12.5505 | -48.16388 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b1029e7-896a-36a5-98c8-c3cac954c252 | -15.87189 | -46.25452 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a364697-167e-397e-b2e8-1722c9093efa | -13.25208 | -47.23313 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63a9385c-da7f-34e4-b9fa-ef78273b0129 | -13.66525 | -43.36781 | 2025-10-05 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9dfed88-8b4d-34b4-b77a-c8060abb5ece | -13.28756 | -47.61507 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fa2225f-911e-3214-b73d-ec397dd28d0a | -11.1273 | -47.91474 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08dd3f21-6ba3-3e83-bf95-245ab1b9c420 | -15.98374 | -50.91985 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f3b7e25-e555-3a7f-9d9a-1618e77d2131 | -15.78143 | -49.09503 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d113e46-1334-346d-ab93-c420fee2759d | -16.75252 | -43.9696 | 2025-10-05 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bdaa0ed4-be9e-347d-a2d0-3fcda360e419 | -10.57353 | -48.71971 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 855c6b93-dabb-318b-9b32-1c2bae5ae027 | -13.2453 | -47.81846 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ed16bdc-1520-3196-a306-18216323bcb9 | -12.89457 | -47.31609 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45c7d3bf-9c7f-3566-a33c-a5de9447e21e | -11.14649 | -47.9247 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4707b6ac-85f0-3b42-9d3d-41e245b73da1 | -13.10156 | -47.87276 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a46fd4d1-0bbd-3e54-9521-3f009fa94d10 | -12.889 | -47.29327 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60427d42-9622-3212-91b5-33b7ac9c2135 | -15.291 | -47.32884 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbf1fc3b-079e-3374-9096-436a626ebe1c | -15.80184 | -46.27995 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18665ddc-0562-3378-9948-95045eca3fa7 | -11.82599 | -45.09728 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e95b3d7c-a925-3caa-9bf8-4d4561d5f462 | -13.29656 | -48.12536 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32324d00-031c-3402-b31c-32f239ccadf1 | -13.34931 | -47.57703 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0cb9638e-3b5e-37aa-af68-28c580235544 | -15.22974 | -49.30177 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97197ef0-222b-314c-828f-8fd36258d8ef | -11.49211 | -46.78611 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1dfaddeb-441d-3a06-a004-d626eafc36e6 | -12.921 | -47.30539 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64584dc2-72cf-35ba-86de-2d15dffa5f1d | -12.70208 | -45.86103 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 851e4d9b-c123-39b1-a0fa-f3ad35ac18df | -13.31397 | -48.08711 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70a3b6e9-b7c6-36b7-a693-1a1970c22db1 | -11.81919 | -45.06343 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6d7cb20-1f25-3ec7-99eb-9fc117866d7e | -11.67098 | -43.90194 | 2025-10-05 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 342f4b38-e81b-379f-b018-8b0f4ad0a1ed | -14.57168 | -48.34697 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 108a7553-b011-3ecb-8f07-0c3e5b231de9 | -11.0946 | -47.75489 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README53.md)
