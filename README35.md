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
| 38288276-ddbb-33be-96e4-ed54e1348f56 | -3.76632 | -59.33942 | 2026-08-30 04:32:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c732b41b-4a57-3f77-a2e5-a4cb196e48dd | -7.94309 | -52.44871 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7685177-0724-357b-ba28-a6886f88cdf6 | -7.6089 | -45.84443 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f74e124-354b-3c8b-8e22-38a3dcc3d7d1 | -6.78015 | -55.6825 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc87142d-63cc-3bb9-8e4d-32f488a0069d | -7.75286 | -44.75793 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2243d07c-925b-32a3-bee0-e987467d8a86 | -6.16044 | -57.79229 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f21d581f-fe7e-3f1f-8df8-0be7c6c95958 | -3.69234 | -51.99575 | 2026-08-30 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c716a1f-1029-3895-982b-224dac3e4633 | -7.04517 | -42.20426 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 58f23e01-661c-3f66-b7dc-cea52415bd51 | -7.51767 | -55.33528 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b9d0142-2845-35c0-8098-1c6d35f87b89 | -4.96477 | -55.83789 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72dc5dd9-2129-3d4c-bffc-634702ad8db6 | -6.64314 | -53.1854 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c004e81-6efd-3234-bfa7-e4691acbb162 | -6.93361 | -55.70344 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9444a4e-369b-32ca-a368-c16cceb01aba | -6.76807 | -55.66661 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e950820-fd68-300f-bef9-c389d7acd8c4 | -3.3702 | -49.53333 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43ca391a-17c5-3c42-8dcd-6c97173df7d6 | -4.2725 | -48.65978 | 2026-08-30 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 895bd85b-4d2c-3432-b498-db3c6c6ef41a | -7.09871 | -42.21727 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| be83e075-8edb-3424-ab78-ad0c4051e921 | -5.53645 | -46.60186 | 2026-08-30 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 598dc027-2704-377b-a399-b550acbf632a | -9.31492 | -40.22044 | 2026-08-30 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| d2d81dc2-5c28-3609-b37e-320b5c1b4648 | -7.95367 | -44.26992 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 183cdf7b-592d-3c68-abac-7e7aafe84bee | -6.67173 | -52.85597 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ac4f3cd-1feb-3be9-a727-00408e87cba6 | -3.42259 | -50.26889 | 2026-08-30 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7be0159c-a440-3c90-b898-85f9762b5326 | -6.87802 | -42.88457 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a33f8e5c-9225-3362-b0b3-7ca116cebb03 | -7.61373 | -44.84416 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea5565e-bf92-3677-9e3a-df8546c3944f | -7.94725 | -44.26491 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9910307-4f94-3977-8fe8-bd00546abb9e | -6.85943 | -41.67831 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6fd2c3d1-d565-3d2d-894d-221228f22301 | -5.96582 | -57.6836 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4678f074-8283-3516-9479-13a97cbedea8 | -6.84961 | -42.87132 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 83910563-ca11-3092-8d9b-00c81959503a | -2.5427 | -48.24456 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcdec877-1fa1-3ce3-b421-3c963a0bfb06 | -7.99623 | -46.51452 | 2026-08-30 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9edaf2-549d-3b29-8d4e-941e615bb4ec | -6.90907 | -59.48726 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e18d7b27-07d2-37a2-b5a2-ad63e08009dd | -6.34526 | -44.09945 | 2026-08-30 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 771f65c4-c70a-3193-8cd6-9a977ffb7b06 | -6.53872 | -55.1059 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38f04d77-2d3d-35b0-8a72-073336b7118a | -6.92891 | -55.69915 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7e6c1bf-4b06-3c8b-b491-d63b20444e1e | -4.95864 | -55.84045 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8ef6615-30f7-3d97-8d74-83d24070527e | -5.21588 | -45.53476 | 2026-08-30 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eafa159f-f8ef-3fc3-bd9a-bd9a73571d07 | -7.21801 | -42.75905 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c27a10d-ca3b-3bcc-a5dd-8fa652bd82f2 | -6.16656 | -57.7934 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b2ef43f-c95a-3d98-aa8e-c55fba0e8426 | -5.88537 | -46.11581 | 2026-08-30 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b870e607-fa01-3f77-bd1d-d0e2ee621660 | -6.7861 | -55.64954 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1633cc0-9c21-38af-bb0f-96cecb8dd4e1 | -7.39025 | -49.53637 | 2026-08-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b6dbb6b-6e78-31ec-8c4e-04e8a8ae7a45 | -7.21732 | -42.76361 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98132640-89ae-301c-a5c2-c88cf4281bbf | -7.21493 | -42.75394 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58db64d8-8a87-3462-a7f4-b7d367845cf8 | -4.26875 | -48.66014 | 2026-08-30 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c1fe1dd-4dcd-3bf2-b439-5c1cc76cd143 | -8.14005 | -45.46756 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9618f4de-bbfc-3e2a-b87d-9cd12c9ec5ef | -8.13837 | -45.47832 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54ee2044-1847-3cea-b576-e89a86fba5a2 | -8.13501 | -45.47776 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c11f4db5-39d2-33e8-9df0-ac0fdba74d72 | -7.21125 | -44.01744 | 2026-08-30 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97d385ba-d5bb-30fa-b680-257150260b88 | -7.1307 | -43.16306 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e805a47-27bc-3199-a1bd-de1341fc084d | -5.89651 | -57.7527 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbbbbea9-7b97-39e0-b4f6-2102d0bde0aa | -6.93712 | -55.71445 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9606e81-fd84-3a7a-b625-50d6ade4776b | -8.13949 | -45.47115 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc4373e6-9ee4-3737-a24c-3e14aa031045 | -4.96348 | -55.84534 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9bd48d04-fb94-3867-a651-dca6f04b7bf1 | -7.00487 | -59.65834 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc4812c7-9740-307f-a0e2-f386e5ea3218 | -4.68864 | -55.66516 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f1b80e0-f9c6-3359-8bf4-06213ad04bf9 | -5.88253 | -57.75981 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee078988-ae84-3526-8618-a563af64c4c1 | -7.12563 | -44.31217 | 2026-08-30 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d95de00-f579-3a35-9960-a13ccd454207 | -5.89865 | -46.13913 | 2026-08-30 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 581ef028-ecc0-3442-b341-39e9c8ad3622 | -6.85547 | -59.47707 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24139af4-35ae-370d-ac33-93fcddd6701f | -6.26052 | -55.42162 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0676e187-3836-3380-8e01-2b2b9ee6d297 | -7.27902 | -49.83944 | 2026-08-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de7e19fc-2f18-3966-8a1c-09210a3b7335 | -8.34518 | -45.64653 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 801d60cc-c23d-3492-b4c9-33e7d9e2453b | -6.15013 | -46.952 | 2026-08-30 04:32:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cb6bb62-8ef7-3616-b3ab-75c5685f237a | -7.61715 | -44.84467 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ac96032-38c2-32fe-9c31-3698b0d5d325 | -5.75554 | -51.68473 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee7afac-ac3c-3383-ad37-665e0d4a1acf | -1.20335 | -54.21012 | 2026-08-30 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4c6eb0-507a-36a1-af79-57142fc94dab | -6.86649 | -41.65857 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c1fb6c9-5b6b-35ce-a467-cf1616921b23 | -6.78485 | -55.68674 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9c95281-b780-33f7-ad75-ba62f79ba19f | -1.99976 | -44.79982 | 2026-08-30 04:32:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c0160f7-c28c-3ff2-a641-f278c8dfb2be | -2.47951 | -46.85587 | 2026-08-30 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 933b98bd-7f20-344a-a4f2-71aaeccbcc9a | -5.52436 | -44.38274 | 2026-08-30 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea5a9342-aa3d-3a9f-bb20-cabe70a6db83 | -8.75666 | -50.46913 | 2026-08-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2956d9da-8ac4-3a12-9e5c-611c0e892258 | -6.76863 | -55.66341 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a63402-5b1b-3871-a8b3-7045af1eb962 | -6.78669 | -55.67655 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 331e69dd-7787-34a3-b51f-57c6658bd51c | -3.18437 | -48.02073 | 2026-08-30 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c533f6e5-43bd-3331-a211-e69f66b85ce2 | -7.51819 | -55.33238 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8feeb6b9-d1a5-31a6-aaec-44f66ffd109e | -6.7631 | -55.65598 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dba8644b-efa1-32a3-bb20-54a98d92195d | -5.4873 | -57.14703 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 864df1f9-31cb-30a6-9cc1-ecf2f44cca85 | -3.48585 | -54.66146 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e45d94cd-9d0f-3a8f-9d24-ed02f5ce270e | -8.75646 | -50.46734 | 2026-08-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58d238b-9290-3078-90d6-55b0cd339a66 | -5.95886 | -57.68695 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 078d3fca-31de-336e-acc1-7e9e83441bf0 | -7.49069 | -45.38617 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d567bed-e953-3cff-897f-4aa21eb3cd3f | -2.01924 | -52.10915 | 2026-08-30 04:32:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 594191cf-f5c6-3695-bd60-b96640ed9346 | -6.86782 | -43.94752 | 2026-08-30 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0909273b-2b13-3501-9c32-eb4a3e85525c | -7.27539 | -49.83894 | 2026-08-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58bc3a5d-133a-3140-87eb-aa5669e187cc | -6.96924 | -45.41501 | 2026-08-30 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90b058f7-8c6e-30fa-a38b-f369d6726f03 | -6.92511 | -42.67522 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca6c5016-5138-331c-814e-974227b72509 | -7.25563 | -45.39003 | 2026-08-30 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fa35748-4147-3d9e-a457-2f1e2d6d2f30 | -2.00308 | -44.80033 | 2026-08-30 04:32:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a22ffd8-93a7-36b7-93e2-4894c5d73df2 | -6.90958 | -51.16306 | 2026-08-30 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc5ffd1f-fef4-3ba7-a207-5975086b40eb | -6.22594 | -55.62135 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5164724b-97b6-3dbc-ae7c-86dcdc53cd3e | -7.51981 | -55.32334 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb0c52c9-7d71-36dc-8619-f212bc407de1 | -6.86497 | -41.66866 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e18ab338-474a-3bb4-98d4-11b37d4b2e44 | -6.70753 | -47.7978 | 2026-08-30 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 398e9ad0-6e0a-3906-bb57-332bd4866703 | -6.86394 | -41.67549 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 628dc575-7f2d-3727-8a99-f3eed43e0a02 | -5.50086 | -44.01412 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc940f5-1ebb-34bb-898a-287a7b88d040 | -5.88704 | -47.72598 | 2026-08-30 04:32:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53e5cfeb-4288-35d7-9872-2957545db07e | -9.46831 | -45.62671 | 2026-08-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4de9a633-bfc4-32cd-bbe7-31fbe44047a2 | -6.86844 | -41.67272 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8ae64ed3-9632-38d2-8028-1c27edb708e3 | -6.85839 | -41.68518 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8b063bba-eb4c-379e-801d-8734b65172a4 | -7.41423 | -49.74547 | 2026-08-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README36.md)
