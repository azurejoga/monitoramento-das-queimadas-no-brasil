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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cd638c-8f67-39c8-9c96-8ee4acdf44f1 | -11.64312 | -48.60493 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a85ba7a8-8c98-3fff-b038-46e427f4c2c1 | -10.53439 | -47.92961 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b83c9b5-832d-3cc9-8249-4efa76506d9f | -9.35394 | -50.74194 | 2025-11-15 04:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89b54e24-be61-3f28-84d8-19029c0c21a8 | -12.77342 | -46.958 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a84856e-8260-3906-b16c-82d44a802aa5 | -11.17669 | -47.45885 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fed0f7ee-07ae-3b8a-9318-e265517e8cc3 | -12.00847 | -46.767 | 2025-11-15 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83d48414-be33-3a7a-a650-1dfa989afb02 | -11.85153 | -49.22666 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7492f333-f188-394d-afed-a09f5e340311 | -13.32915 | -42.50216 | 2025-11-15 04:27:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1bd06e5-ec2f-3e8a-b82b-8916fcd56226 | -9.7186 | -48.89976 | 2025-11-15 04:27:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 760f9c07-47bc-357a-857b-91aff06a9c84 | -13.89693 | -42.89753 | 2025-11-15 04:27:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3a18f6e9-6b2b-324c-a10c-07d48ce17822 | -10.93005 | -48.70213 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bac81f7f-d93f-3cbb-9a82-457aeac77855 | -12.56459 | -43.96036 | 2025-11-15 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d116c31-f874-3a7e-a384-7efd22a720ff | -16.30401 | -43.80858 | 2025-11-15 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad09efc7-d761-3399-950d-09a2af49d027 | -12.36716 | -43.69872 | 2025-11-15 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efe83299-721b-320e-9e7b-eb1308387834 | -12.02669 | -43.72924 | 2025-11-15 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04009fc7-8b04-3c0f-a7b0-b80fbe7b4a80 | -12.90806 | -45.10584 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46349a0c-bbfc-3e09-a61f-f94b65dbb922 | -12.39542 | -48.10778 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd40122c-7c21-3504-9d5d-105f0969b831 | -10.37969 | -47.7494 | 2025-11-15 04:27:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1bc5a11-6efd-326c-af9f-ff76827a1efd | -12.0403 | -43.74054 | 2025-11-15 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f16ee6fa-fcd5-337a-96ec-852e59c4a2ee | -14.97218 | -46.57865 | 2025-11-15 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6284a6f-f9f4-399f-b2c5-5667b2c9719c | -14.65506 | -46.56844 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9495c15-062e-3fee-a603-ed8abee99d74 | -13.3298 | -47.37475 | 2025-11-15 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f916923-c9a0-3760-a26f-2e9634cbb1e1 | -15.47008 | -43.19103 | 2025-11-15 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea1bcef8-d6d0-38f5-aa0c-397029a28a71 | -17.24489 | -42.66462 | 2025-11-15 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 49e411dc-3539-3a52-8f89-b31dba03e544 | -12.23852 | -49.39363 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 892ff0ab-305b-32a8-8829-eafb14535c52 | -12.80327 | -46.4542 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b1c654-8e44-367f-8554-f9ef2f00b917 | -9.93025 | -47.83877 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b84c6ab-94bd-3415-8396-7da7301fb6d3 | -12.8154 | -48.56287 | 2025-11-15 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac1f8c66-a9e5-3697-8de2-24c69f59475b | -10.34729 | -48.91874 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7517856e-b5b4-33ec-a93c-15aa97c848a7 | -11.04699 | -47.65675 | 2025-11-15 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 478de25c-feb5-300c-9f73-5eecaf38c1cb | -12.23974 | -49.38618 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab2c7b00-3420-31b5-bb30-044619d35219 | -12.38708 | -48.11734 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85751bd0-05f6-39a3-9be1-60b4e8e2e50e | -14.23792 | -44.25313 | 2025-11-15 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8b4286c-62cd-3694-973f-ab9ff83305b3 | -10.66728 | -49.3634 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2ad4be-acd2-3176-9fa1-45576ce9ba82 | -9.67999 | -47.89596 | 2025-11-15 04:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dac835a-0687-38d3-a8be-291e5c661188 | -14.94878 | -47.50808 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fba6a41c-9f6e-3dc1-b68b-b2237db8cd2b | -10.33434 | -49.63871 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0583f69-c198-3862-ae2b-55ae9b8e20f1 | -11.59358 | -45.12594 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 158e1bfa-d7c1-3bfc-9a6b-9ded8e3a6857 | -11.97852 | -44.6504 | 2025-11-15 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea39151a-720b-3e60-b0d8-d7c118d66c53 | -11.80238 | -48.07604 | 2025-11-15 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6d94794-4e73-3d03-8934-e59c6608dbdc | -12.81001 | -46.45512 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bf55184-03d4-3af5-88c7-a19457b8ab8f | -10.57381 | -44.81373 | 2025-11-15 04:27:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cf64912-d8ff-37a4-ba24-ce44440af088 | -15.45569 | -39.2383 | 2025-11-15 04:27:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5163c9e-fac2-359e-ad24-d959a62998b8 | -12.79444 | -48.82077 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35903357-10af-3cb4-8e71-97f50a4ab1bb | -10.70746 | -44.06874 | 2025-11-15 04:27:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfbbcb85-1397-360a-94d8-a384de1895fd | -11.84995 | -49.21495 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f6d5fe84-9958-3458-b7cf-0bcb315bc784 | -11.1142 | -48.34114 | 2025-11-15 04:27:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fa0f3e9-f5b5-38cd-abd1-5c0459d1de0e | -13.81489 | -55.2354 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a650061c-1df5-32d0-97ba-4263ccb58233 | -12.78509 | -46.75079 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c98d4df-fb94-35fa-9f20-fa0b87a8cd95 | -12.7246 | -44.55478 | 2025-11-15 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bd3bb51-540c-3383-8d86-0347fc21764e | -12.66015 | -46.74534 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1935edbc-de4b-3e6c-8465-1800dfd1ff65 | -17.58384 | -46.68142 | 2025-11-15 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7a153e8-dc7d-3f93-b152-cf289c2b6c93 | -12.52823 | -49.59653 | 2025-11-15 04:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f90f81f7-c2c2-354c-8da6-83134a925db3 | -13.54496 | -43.72393 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e16a245e-ec2d-3dad-9fd7-36045c2e54d6 | -14.27405 | -46.26417 | 2025-11-15 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8617c697-1544-3ab4-b0de-05280c1943c6 | -12.9707 | -48.8429 | 2025-11-15 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba94ffb7-68f8-348c-a98f-dd7c0371e959 | -10.44926 | -47.33379 | 2025-11-15 04:27:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffd222da-55a4-3c22-8fb5-57dbc1d0f8e0 | -12.42521 | -47.89952 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 129dde15-6ea6-3a22-be88-549115ce8f2c | -12.41196 | -48.11055 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cc6d720-d06c-399d-8d0d-c994f5626436 | -13.35293 | -43.74508 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0c30492-9b27-376d-b0ee-f4e9286938e1 | -17.27164 | -42.65992 | 2025-11-15 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 390a109e-29f8-3c3b-ab9f-1bd06793196a | -11.32263 | -48.52567 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c5e454c-814e-3297-89fa-b65bf0c13f70 | -17.57636 | -46.68426 | 2025-11-15 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec809583-a325-39f3-9c45-f4bff9cbc540 | -15.34628 | -47.87757 | 2025-11-15 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91eb26eb-4340-38d8-bac5-1520dddb189b | -12.5999 | -48.33788 | 2025-11-15 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14ad24d4-2bdc-32fb-92c0-50de02a2f772 | -11.3049 | -48.50793 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b471cba8-f72c-3f1c-9f3d-3525e852536f | -12.43737 | -47.88708 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a3072f-3d55-3065-87b7-830c3110f8d7 | -11.6437 | -48.60133 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5df4cc24-4e06-3fc4-ae1d-942b1b88625e | -17.16115 | -43.08275 | 2025-11-15 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 380b33b5-7810-3231-9766-556f893fe473 | -11.67617 | -44.74113 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1f3bc35-ae99-31f1-b235-35ee161ddefa | -10.383 | -47.74994 | 2025-11-15 04:27:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc301d69-7e86-341a-b251-e50d3995eded | -10.68676 | -45.1758 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52a6c9e6-e026-3d4c-9b02-4be6a18ab11d | -10.54085 | -47.99584 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552832c1-091b-3644-876f-8e09fd308942 | -10.33718 | -49.64322 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0623b7e-c6c1-36a8-8604-c99d31b8031d | -10.25781 | -47.08117 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dffe8d99-4cb7-3e14-baa3-0fa6a91e489e | -10.87211 | -44.68367 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc70b648-dbba-3577-b206-69d2d6aec861 | -13.29063 | -44.20136 | 2025-11-15 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7b83b74-2fff-3dca-8e61-667584fff06e | -13.48801 | -46.72092 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39becfc0-d805-38c0-9d23-649c98fe8a7d | -15.14706 | -43.65187 | 2025-11-15 04:27:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 53a83eab-156c-3e87-b236-4a3bbd8d589a | -12.65626 | -46.74839 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62bd4121-7007-344e-8c26-0928ce678ca3 | -11.99661 | -47.12709 | 2025-11-15 04:27:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a8c8a3-9d57-3085-99e3-c76d2127e797 | -10.98767 | -47.72956 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a085fe49-c1a3-3c96-a2ec-1e4ac7ddf616 | -11.3277 | -48.51546 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9bac789-e866-34c0-b74d-cffc71878f36 | -13.48857 | -46.7173 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06a2a900-f6f5-3535-9ccb-f96c6b6c4b20 | -11.46461 | -48.50507 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8132e13b-49f8-3e1f-860a-27f40a518c9d | -10.35008 | -48.92299 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64f1b994-b0b8-3b71-b719-3d7f0e0e490b | -11.7063 | -48.39845 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 785392f8-9a00-36ea-95bb-78b781e7d0e9 | -17.29647 | -46.82589 | 2025-11-15 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55af6a4a-9c5b-3a76-be76-1bb825794895 | -13.35999 | -43.71962 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1af3f14d-0beb-3536-b2c5-f68956f20555 | -9.82635 | -49.77184 | 2025-11-15 04:27:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f9aef04-8bed-3588-b021-f26a6d0f23a6 | -14.46329 | -52.90218 | 2025-11-15 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2f58f2-6246-34aa-8b76-f22e549bd2f3 | -12.95465 | -51.61266 | 2025-11-15 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96ca13d8-0c06-375a-b6c4-0eec67c457c9 | -10.34449 | -48.91449 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57ceaf34-caeb-3784-a3e2-e490f3bf48db | -11.00508 | -45.27041 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a238931-7afb-3ffb-8417-17a48310955c | -12.83967 | -46.44118 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 862be41d-514b-3257-a17f-2627503f393d | -12.75634 | -43.65081 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfd68e43-6d95-3216-828b-33c387767f4e | -9.83848 | -49.04647 | 2025-11-15 04:27:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e5777b2-2012-3fb7-b8bb-29a3a8d534ee | -11.81498 | -45.28454 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e99a365f-9d43-313f-8de2-63bf0b3da210 | -12.77064 | -46.95394 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaeba6e3-3b2e-3412-8bab-b418ee3789fb | -10.71107 | -44.06929 | 2025-11-15 04:27:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README49.md)
