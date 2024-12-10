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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9551351-8b4f-390e-83d0-3e9255f40577 | -3.37257 | -42.32656 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bead708b-307d-302e-b7ac-bddfc6113c84 | -4.24547 | -41.92904 | 2024-12-10 03:34:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b44d8b7d-e352-3238-bb0d-0f7e804e72d8 | -3.85326 | -40.44518 | 2024-12-10 03:34:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 00daddbc-8f73-334c-90fc-3cf63f90c37c | -2.7784 | -45.00129 | 2024-12-10 03:34:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8e8bec9-7998-3c71-8984-80c11fd8da2a | -3.37317 | -42.32306 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa626427-ca6b-3775-b983-6a2d51f3163e | -3.23038 | -42.43419 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e46d500f-76ba-3651-8627-fdc2fbc20634 | -3.23591 | -42.43498 | 2024-12-10 03:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4daae831-6b33-3ff2-8cab-ef638328f190 | -3.97218 | -45.62135 | 2024-12-10 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0df2d800-0b4f-3e01-ada4-cb638e075bf5 | -7.44305 | -37.51283 | 2024-12-10 03:36:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 06daddcb-52b8-3922-9f3b-b7f44106fbe0 | -7.13815 | -38.9062 | 2024-12-10 03:36:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff29e059-16f4-3a76-91ee-4e88ae9f02bc | -7.87799 | -35.1504 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1c16f344-5105-375f-82d6-96ab38eab553 | -6.33955 | -43.4383 | 2024-12-10 03:36:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b165fba-6ca8-3310-aa0a-b11c09b300a8 | -6.83757 | -44.38537 | 2024-12-10 03:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0c90a41-c42a-37aa-96e1-136c1f129a05 | -6.91502 | -43.51068 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41f90157-a2a9-3ece-928e-3a4f857d4b27 | -5.29058 | -44.91667 | 2024-12-10 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 542adbd6-82ee-3842-bc31-b96ebe80aa8d | -9.08176 | -35.70333 | 2024-12-10 03:36:00 | NPP-375D | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4a08e85-60be-3e69-b866-3344ec221875 | -6.91994 | -43.51536 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 74aabb71-2359-3be7-a000-053525960a9a | -10.2431 | -36.49361 | 2024-12-10 03:36:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd01699f-7c56-3852-8eb5-dba111f46496 | -4.50361 | -44.32546 | 2024-12-10 03:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f327bfe4-6f32-3166-b4c0-2cae690c0dc9 | -6.91111 | -43.52048 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26111c21-6193-3fac-9b31-c946aca6b3e1 | -7.74809 | -35.26261 | 2024-12-10 03:36:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99064d72-aa87-3b78-90a6-c0c675f9b613 | -6.83172 | -44.38403 | 2024-12-10 03:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 792ee59b-632c-377e-9980-43c4bae7c9cb | -5.70924 | -46.55096 | 2024-12-10 03:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bb239ee-6d9f-3540-9dd4-2fe98072cdd2 | -7.85986 | -35.19898 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a5eabcd2-1441-33b0-81b1-712e76488bf3 | -10.71399 | -37.60393 | 2024-12-10 03:36:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2993ae3f-2a07-3e51-a1f4-44c4ebdcc643 | -7.96359 | -40.02236 | 2024-12-10 03:36:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ff01806-9f97-3a60-9d47-0e06a2dc3cb1 | -6.91871 | -43.51033 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ac1eca61-1985-31f7-9638-e814d4697642 | -7.47628 | -34.845 | 2024-12-10 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba1e5c3f-0e71-3be2-a359-5c8cb2d4933a | -5.84887 | -39.04422 | 2024-12-10 03:36:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef8c716e-9eae-3363-aac6-6ab2e9c89100 | -6.91929 | -43.51907 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c5fd3f2-3ac8-340b-8ee4-a6c736910a6b | -10.45581 | -44.88768 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd9c2442-c794-336b-96aa-10840afd205b | -5.34997 | -39.34903 | 2024-12-10 03:36:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abc6e066-5553-30db-b203-6bb51a20301c | -9.93491 | -36.45488 | 2024-12-10 03:36:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4e4b9ff9-b5c1-3477-8424-9c98c03ed2dc | -10.45368 | -36.77742 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c160eee-7be3-3f51-bbd6-1cbde90fd97b | -6.92059 | -43.51165 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 438a2be9-cca0-3987-b9ac-f6b9b1697d9b | -6.91736 | -43.51773 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2430ec70-20bb-33d3-bc33-80eee97e06c3 | -8.35473 | -35.33711 | 2024-12-10 03:36:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b61aa80f-1db0-30c9-b8bc-2ea89d25bc5b | -5.62429 | -44.84013 | 2024-12-10 03:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d25fa88a-a720-3934-97fe-9ade794b2d56 | -9.04091 | -36.10979 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66aa455a-2485-38b5-9f39-ad87de69d078 | -9.0399 | -35.70388 | 2024-12-10 03:36:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 735738d6-846c-3d65-a311-93e352895033 | -8.07418 | -34.9773 | 2024-12-10 03:36:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ffb19f17-6e3d-3cbf-becd-058617fd57b3 | -6.96101 | -42.99268 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b30d32f4-0cbb-300f-bbc5-52fbf7197eed | -6.58774 | -38.45049 | 2024-12-10 03:36:00 | NPP-375D | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9622a565-f9ce-3121-8e4e-961a081679af | -6.26288 | -43.56262 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5a6c69f-ebe9-36b9-bce6-a5a7cb439b90 | -10.45506 | -44.89159 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 102635e3-bdd3-3034-a162-19da39080392 | -9.76156 | -36.21015 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 1c023a7b-0ec3-3b6c-9acf-883629eb8eff | -6.73778 | -38.5411 | 2024-12-10 03:36:00 | NPP-375D | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 032a06dc-09fa-385c-bf3c-d7d081e74edc | -9.41381 | -36.00547 | 2024-12-10 03:36:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f6c7d75b-0d4d-38fa-9b84-078bcfd53808 | -9.07837 | -35.70277 | 2024-12-10 03:36:00 | NPP-375D | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8da68c4f-f01c-3a36-a191-9f7ba0e6c840 | -6.25789 | -43.55791 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5618ce0-1e97-3a6b-9c9b-2dc74e699c4b | -8.88556 | -41.10551 | 2024-12-10 03:36:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c39ad22a-609f-3af7-9f4e-9c568499b4fe | -5.68693 | -37.35647 | 2024-12-10 03:36:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3a0b20b9-c480-3811-98a1-ca65eaf79f65 | -8.4789 | -40.68902 | 2024-12-10 03:36:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d673f91-1672-3b9e-975a-61da3f9ad11c | -9.76035 | -36.21763 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 5dc74ee3-eaf6-32ef-a866-e5458927c37c | -7.89168 | -42.44536 | 2024-12-10 03:36:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b48b7177-af3a-334c-88f9-fa26ebc73ded | -8.88099 | -41.10466 | 2024-12-10 03:36:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c13d87c-dba3-39a0-9529-d3a38f57cc0b | -10.45997 | -36.78255 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 57054256-ead2-3056-9304-11dbaa00c08d | -9.03931 | -35.70754 | 2024-12-10 03:36:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f048d7c9-d2aa-3caa-8389-a0222c2e6a27 | -9.70699 | -36.17806 | 2024-12-10 03:36:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 394ba433-4c41-32c3-9524-181f84058fab | -7.86266 | -35.20311 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bde5bcce-e8c4-34b9-8aa9-63e6be01d14e | -9.76377 | -36.2182 | 2024-12-10 03:36:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a41a2c8c-23a5-3c10-80ff-9a7753ff2e98 | -6.16335 | -35.27641 | 2024-12-10 03:36:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1200a05d-e676-3c26-aa16-b5bac7fabef8 | -5.49828 | -39.46036 | 2024-12-10 03:36:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 583218b0-3c0f-3da4-a7ce-493a9f6f1f89 | -6.9046 | -47.83999 | 2024-12-10 03:36:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1629dc2d-3a21-3cd4-b3ed-c6817509a0c8 | -6.90816 | -43.51713 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7860ac8-3e78-3141-9225-98202765cf84 | -6.91179 | -43.51678 | 2024-12-10 03:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05a2ce56-8c81-3988-8c22-46f3bb1bc03a | -4.55937 | -43.30607 | 2024-12-10 03:36:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2649d4a1-0b31-33d5-9f1c-752880ea993b | -9.75753 | -36.21331 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 682a55a2-c02f-37d6-be44-dac7dc9bad4b | -10.44957 | -36.78064 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20822f7b-6830-3adb-945c-4b4f2d85f926 | -7.74867 | -35.259 | 2024-12-10 03:36:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e842c73d-ca3c-34ca-9d31-11ef7b551458 | -6.90326 | -47.84701 | 2024-12-10 03:36:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4ecf5ff8-851a-3e07-9eeb-95691da746dd | -8.57419 | -35.62164 | 2024-12-10 03:36:00 | NPP-375D | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b131f7fc-2be7-3c26-aec1-6d86725e69b8 | -10.44364 | -44.88926 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13e3aaab-8389-33b7-9fc1-43c585f54344 | -6.97238 | -42.99098 | 2024-12-10 03:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 02ed2ae5-2bbb-3e3d-8e4a-cee94c7c236c | -6.40201 | -35.20494 | 2024-12-10 03:36:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| fddc548f-edd3-309a-b338-d4a7bc2b3a9f | -7.33235 | -35.06689 | 2024-12-10 03:36:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d6a2dba6-766c-3794-b26e-60ab449140c9 | -10.37337 | -36.37905 | 2024-12-10 03:36:00 | NPP-375D | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f54b07c-48db-3950-95a9-7efdd2ddef52 | -10.45932 | -36.78643 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae31890b-bb70-3429-aa2b-4c067b6f2c0d | -10.50626 | -44.93435 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4589176-3132-3171-a855-2440911399da | -5.71606 | -46.55224 | 2024-12-10 03:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2a30242-7222-3b07-84f3-6bc6db478789 | -5.70948 | -46.55027 | 2024-12-10 03:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b988cd4b-02d7-3d36-890f-c15c48a9c44d | -11.19092 | -38.1507 | 2024-12-10 03:36:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef127ded-93f0-361b-9e37-21fbbf763866 | -10.45239 | -36.78514 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef058f9e-09b8-3828-93cc-0fbf423018fa | -7.75205 | -35.25954 | 2024-12-10 03:36:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f2f646fc-adce-3518-8550-bca37d46ebf5 | -5.57719 | -45.2085 | 2024-12-10 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2026f375-c5f6-3a65-a9a7-b8291896bef4 | -10.44936 | -44.89038 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24e165a8-c218-3670-9bbb-1158a96ffd97 | -10.50701 | -44.93041 | 2024-12-10 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3c589bd-92f3-3dfa-9788-2bfe52eca84d | -11.18991 | -38.14848 | 2024-12-10 03:36:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c3647f0-5ec2-392f-993e-207900404ec4 | -9.17191 | -35.70626 | 2024-12-10 03:36:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70ab7d53-4ec6-3cf2-b106-041c8f13df82 | -8.36838 | -37.36068 | 2024-12-10 03:36:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd0e11e7-58ee-373c-9cc9-0ec469767f56 | -9.76498 | -36.21072 | 2024-12-10 03:36:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f93ae9f-88d2-3b08-a2ad-bf3ad894f0ae | -10.4995 | -36.69448 | 2024-12-10 03:36:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9700ddac-7615-3564-b6d3-3c1a4b2ad302 | -6.25976 | -43.56052 | 2024-12-10 03:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffc47eb9-ff7f-3d76-ae5d-4288ddd3dc38 | -10.75064 | -37.83277 | 2024-12-10 03:36:00 | NPP-375D | SIMÃO DIAS | SERGIPE | Brasil | 2807105 | 28 | 33 | nan | nan | nan | Caatinga | 5.3 |
| df16217f-3233-33cb-9366-8d6a4910ca36 | -7.88716 | -42.44122 | 2024-12-10 03:36:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50b6a08f-dda9-3eee-afcb-f0bd1c001e60 | -9.76781 | -36.21503 | 2024-12-10 03:36:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 10c9b68f-d050-3fb7-8354-0aeee797452c | -6.43341 | -39.70518 | 2024-12-10 03:36:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3ae61333-01bd-3139-87d4-bd4fb558ef61 | -10.45868 | -36.79028 | 2024-12-10 03:36:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 71d588bb-abe9-3d8b-9200-500e0d55542e | -7.9227 | -35.20129 | 2024-12-10 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bd525f53-ed71-3fd4-a29f-5d8148365aea | -5.68619 | -37.36102 | 2024-12-10 03:36:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |


[Clique aqui para ver as próximas entradas](README11.md)
