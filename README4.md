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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93a072cc-0ddf-36d6-8804-956c1328e0bc | -7.35289 | -49.83085 | 2026-06-06 04:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a23cb417-1838-393d-9d2d-25cedce82350 | -5.2993 | -47.24225 | 2026-06-06 04:04:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3ca6c88-bb60-3e26-9b59-abf7ca2af983 | -6.98566 | -42.87807 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| efeb6adb-feb5-3755-a852-8fc99dad5441 | -5.74112 | -43.95965 | 2026-06-06 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bac72d-eb42-334f-b68b-c1769abb84c5 | -6.04838 | -47.89384 | 2026-06-06 04:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d166c3d2-b2ef-3567-99f4-e5216455e4de | -6.45054 | -44.56826 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b3daad7-506a-3e19-b6d3-731dd63528b7 | -5.8121 | -43.79322 | 2026-06-06 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 700c4e13-85bb-361b-86af-dbc270371459 | -6.9866 | -42.88102 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9f0bb3e9-a8f2-3543-a1bd-277c218049b9 | -5.80734 | -43.79627 | 2026-06-06 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 591f6d7f-b976-3097-8ed2-7fe93dd34443 | -5.9269 | -43.48134 | 2026-06-06 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f112d9f-c1cb-3659-abaf-b0be886cd37d | -5.34727 | -45.18576 | 2026-06-06 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b7f2355-d1bd-37fc-8b7d-80df7c0e3a39 | -7.00604 | -43.86163 | 2026-06-06 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b81984b-7141-3c46-be59-e3aa837df295 | -8.45836 | -47.00056 | 2026-06-06 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 606589ce-9b46-3ee3-998e-e05985b3e622 | -6.99424 | -42.77803 | 2026-06-06 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62d16d42-f815-3697-85c4-117b7ec0df9b | -6.85515 | -44.96827 | 2026-06-06 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 883081eb-caf3-3ed5-891c-8f07be0adcd4 | -6.98741 | -42.87632 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55a0d281-def4-3cb1-b85f-4767070e2036 | -5.44683 | -44.8166 | 2026-06-06 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 032c020b-a196-3102-ba3b-083fd0ef854c | -5.72361 | -45.04093 | 2026-06-06 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe51e308-d222-33e7-81e3-16c15f7cef11 | -6.05382 | -47.89476 | 2026-06-06 04:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b42197ad-1c1c-3654-b17a-aab5c23b36d8 | -6.98196 | -42.8851 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 98233919-a9f0-3832-871f-3f7e5c364808 | -5.80796 | -43.79256 | 2026-06-06 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 309c381a-49c2-3a92-8955-966800b574ac | -10.52025 | -42.37244 | 2026-06-06 04:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 71e10e92-bc73-3561-a58e-d17945cc616d | -13.30673 | -43.76783 | 2026-06-06 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb522ea-b557-32f5-8178-c4b658450d9d | -15.17894 | -41.81297 | 2026-06-06 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 23354037-7985-32b0-bd87-0fd90369d656 | -12.06554 | -48.43004 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa7d4b27-bc7a-3048-a503-af9bc5529430 | -8.99944 | -47.43746 | 2026-06-06 04:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfc3da5a-fbdf-31b9-bea7-7eb72dd6e4c5 | -15.31588 | -41.89713 | 2026-06-06 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63b6658e-d378-302c-8b88-828fc7068ffd | -12.511 | -46.26578 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bcb7fbb-08d8-3a88-9db2-7e31c7abe734 | -14.69678 | -41.36025 | 2026-06-06 04:06:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 588efca1-29e2-31b8-aaac-42ef9769e3d5 | -11.1201 | -45.13972 | 2026-06-06 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4603c156-5763-35ee-bf07-29cb0e4170d6 | -14.38004 | -45.56351 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24ff712-cd8d-31fe-a6f9-ba9e9001fcbf | -12.50074 | -46.29731 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94932eb3-315a-3f65-b8db-c6a629306915 | -13.97801 | -40.90631 | 2026-06-06 04:06:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9dbd6362-8403-3432-9b93-3d2581d6dfa9 | -14.22813 | -45.80682 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 060f06b9-52bd-3188-9524-07b5d73ccdd0 | -12.06612 | -48.42702 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaa97411-ce03-3cac-8b04-bf98bb7cd3a9 | -12.06171 | -48.07723 | 2026-06-06 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 92328ea6-7421-3cb7-9351-7230f62775d4 | -12.52291 | -46.27472 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64f809b3-261e-30d9-aee2-ab2b9fc5943b | -12.50788 | -46.30772 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 372ea02f-cb72-3cd9-ab02-216d0f216ad3 | -8.93122 | -45.67628 | 2026-06-06 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffcb0c00-8999-3217-8af8-6d5355d3e2ad | -12.51541 | -46.29118 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa7a4ee5-bef5-3098-919e-f86706fec0a5 | -12.50399 | -46.27951 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c18af2c7-a076-3fa7-8ee9-9b904fe8c240 | -12.0706 | -48.43108 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad6c5c31-d38f-37e6-8f7e-1bc8ddefe798 | -10.81216 | -44.3024 | 2026-06-06 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad268be9-3082-3668-a702-a7b520761469 | -12.50431 | -46.30255 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c488db2-9cd4-3054-881f-455745cd0383 | -9.08827 | -50.61411 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34281ee1-6aac-3a8c-8ac3-f0957ef5b767 | -12.06665 | -48.07827 | 2026-06-06 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2bdde700-8877-310d-84c9-d29050bc3c90 | -12.00444 | -45.35473 | 2026-06-06 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d24932e3-2f7e-3c8b-971d-aff00278d989 | -9.37308 | -50.54407 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e39a733-a512-398b-a823-66622f806cda | -9.37422 | -50.5394 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3513e0d-6db3-39c4-a87f-5c41b09b841e | -12.00512 | -45.35094 | 2026-06-06 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d36e35cc-d203-3dfd-8a9e-d505a932b14e | -9.07224 | -50.60536 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 034cec9e-74a2-3c11-91ec-9831338d49ee | -12.50947 | -46.299 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9da08461-d620-3677-80dc-4d13de0e0d57 | -8.86637 | -50.19478 | 2026-06-06 04:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c2194be-b8d1-307e-98ef-c3c996955fc9 | -14.23156 | -45.81136 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbb640c5-0f56-3100-a67c-199490a14030 | -14.22195 | -45.79403 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1cf71ca-d72b-3925-b367-1102cdbf4325 | -11.56125 | -52.8014 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44e51cd9-d8c8-31d7-b2b0-5ef39fe1cda2 | -9.923 | -48.00356 | 2026-06-06 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f0001e1-a707-378f-b4aa-99358e93f4a8 | -14.22538 | -45.79855 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e910831a-0627-335c-bb2a-c5e8a9455c22 | -12.50752 | -46.28493 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86c52663-a5c4-3e65-ae23-61d6bd1057e6 | -9.90084 | -47.48186 | 2026-06-06 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcd52f88-4d1f-3474-b6d7-70555a5f670d | -12.52371 | -46.27031 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1affb2e2-1932-3d3c-92cc-d22b6549d59f | -12.51383 | -46.29985 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e59686b-8e68-31cd-b52d-0a003008a618 | -13.40089 | -46.60334 | 2026-06-06 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fdeee9ae-4553-3a8f-b671-b4ea1cbea212 | -12.49639 | -46.29642 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 918550b5-4a00-3174-8e3c-089543c69462 | -14.23894 | -47.9748 | 2026-06-06 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1ede04e-df7d-3d8d-9949-8171a705e321 | -12.50234 | -46.28854 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3917af5b-5d99-350b-9993-80a70962462b | -9.07689 | -50.60712 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6309315-8ec2-3b76-bf94-a213f821bd87 | -14.24356 | -47.97633 | 2026-06-06 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be41c52a-59ad-3b9d-8690-196aa2a06c6d | -12.49798 | -46.28775 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 537cf642-210c-3f71-92a3-4a3758aa5ddd | -12.49718 | -46.29211 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dc301b98-e669-3d69-8cd7-8fad6af080b5 | -12.00858 | -45.3555 | 2026-06-06 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76eba913-5421-3b1a-bf01-76a60a5da9b9 | -11.0376 | -44.3205 | 2026-06-06 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d28d07d-a2d4-310c-9b0d-9979cc8d8bd5 | -12.5051 | -46.29818 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f74e35d-bbe6-3a37-bed2-9215b425ec1d | -9.37331 | -50.54401 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18865101-e9e0-3860-b34c-b4eeae11e711 | -11.04154 | -44.32123 | 2026-06-06 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a243e70f-b2d5-3856-86e6-3f309d430636 | -11.47175 | -47.98875 | 2026-06-06 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e792e3-e9a4-3500-a4e0-29ff5ea2f5e1 | -9.09618 | -50.60612 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b092e0ab-990a-32b4-986a-02e34979d058 | -12.38625 | -48.12797 | 2026-06-06 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39670914-9ff8-3b92-a603-4f92db5858f7 | -11.54915 | -52.7924 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7df039b1-5532-3402-b24e-762cf09ff88b | -12.50316 | -46.28407 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b129bafe-8803-3272-969b-956b34fa11f3 | -8.86722 | -50.19029 | 2026-06-06 04:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c58615ac-cde8-37c2-bdf2-58a1446e0367 | -11.54788 | -52.79851 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 566e3ee6-a2c8-3135-88f3-626f2cbb51b9 | -8.93043 | -45.68074 | 2026-06-06 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23d33306-0542-348b-ae5a-6a493ae89540 | -12.00926 | -45.35171 | 2026-06-06 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c0883b9-2a69-372b-891d-3852f2068c89 | -12.06376 | -48.42636 | 2026-06-06 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f362b0b-d5a7-33dc-9cc9-fd99e468dc9f | -12.51019 | -46.27026 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d57b9a-282d-3002-bdb0-18eda9e38da0 | -14.2288 | -45.80312 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| edec0fc0-a507-3960-8c31-98abf83b3fd7 | -11.46678 | -47.98777 | 2026-06-06 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27b72611-1c8f-3a6b-8d40-6de8f1a88c3f | -9.07782 | -50.60233 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6efbbf83-cfee-3bec-aff8-3c11cdf4fd8f | -15.31527 | -41.90083 | 2026-06-06 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03306f39-7163-37b8-a723-e832d5c2fcb7 | -12.50154 | -46.29294 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ffa5449b-881d-39f3-922c-135a76add79f | -12.0608 | -45.98751 | 2026-06-06 04:06:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cfebec1-85df-35c9-b622-f3884647b7a0 | -12.52644 | -46.28014 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4132a0a6-c4b3-3c25-b6c1-306e9f9a8cc8 | -11.55583 | -52.79386 | 2026-06-06 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7177dfea-045f-30a3-a7a0-03cee1a963f3 | -9.09529 | -50.61074 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b89b3bf-adfc-3380-9662-e7cc929dd0e0 | -12.92725 | -43.618 | 2026-06-06 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae04337c-c890-30a0-830a-b2e19425f892 | -14.3807 | -45.55989 | 2026-06-06 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61cc4524-e5ae-392b-af22-a291b06781f2 | -12.50491 | -46.2745 | 2026-06-06 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46332727-5185-32d0-b377-ffacb112840a | -9.07837 | -50.60658 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb4c6de8-b26c-392e-a08e-3529865e5e4a | -9.08916 | -50.6095 | 2026-06-06 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
