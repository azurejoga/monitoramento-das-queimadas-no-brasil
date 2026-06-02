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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3efb7129-a696-348d-9d64-5a305e1140fc | -11.5943 | -47.44145 | 2026-06-02 04:00:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 966506a5-b6a7-3914-b1ce-16df0628ae66 | -11.7954 | -47.33862 | 2026-06-02 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab803163-4cfa-3f41-baf4-862b69d61da7 | -16.58523 | -45.88023 | 2026-06-02 04:00:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9241b8b4-2439-3b75-a65b-2ee15a3b2194 | -10.03726 | -51.68169 | 2026-06-02 04:00:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb7b02c8-cec2-39e6-9ed5-1bfcd256f795 | -12.29851 | -47.90738 | 2026-06-02 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8cf3160f-49b5-34ee-a585-9ee38e9305e5 | -10.49567 | -52.13462 | 2026-06-02 04:00:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b40a8b7c-d78c-32e0-a2e7-98bf4148b09d | -12.01289 | -49.27617 | 2026-06-02 04:00:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f8140981-86c6-3c39-bbc8-aa076fc361d4 | -13.95644 | -46.1861 | 2026-06-02 04:00:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6614102-a51b-3170-8e7d-a331a7e5e77c | -12.29764 | -47.90508 | 2026-06-02 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ef8ff16-057b-3a40-ae42-7926dc535869 | -12.51208 | -48.2766 | 2026-06-02 04:00:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 029acd54-d290-3785-91c4-cf9f2677cb2d | -18.39747 | -51.45528 | 2026-06-02 04:02:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| febc7607-ed23-30ba-8729-832b346f6c00 | -18.79182 | -50.92357 | 2026-06-02 04:02:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 17b1a5d9-d225-3350-9345-3efe7d145cf8 | -18.2959 | -47.04663 | 2026-06-02 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b17b5ea2-600f-3d04-af70-e163e35ff6fb | -19.69459 | -44.92724 | 2026-06-02 04:02:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af837295-d211-3a37-817b-d6c597e71343 | -18.87315 | -41.96481 | 2026-06-02 04:02:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f9393934-bc6f-3b25-a30f-5aa71b0b04c3 | -21.81381 | -49.12686 | 2026-06-02 04:02:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ab110ee1-0c8e-31b6-b3e3-48d5339520e2 | -19.17951 | -47.3551 | 2026-06-02 04:02:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf01218b-a181-321c-82f7-d076568cfddc | -21.70149 | -48.41513 | 2026-06-02 04:02:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43855f3-44c4-3590-bca5-17725363e9a5 | -19.59037 | -45.21592 | 2026-06-02 04:02:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7db53d21-eaf5-3506-857c-c3cceeb9de70 | -18.39833 | -51.45127 | 2026-06-02 04:02:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a9fa593-386a-354b-8b13-1a3146ad7c9b | -21.81034 | -49.12094 | 2026-06-02 04:02:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 695702ff-3edb-3b27-8385-7eb3f50b0136 | -21.43664 | -49.92913 | 2026-06-02 04:02:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| f16e03ca-cdbd-37ea-9181-ebba71795a56 | -17.83698 | -42.6153 | 2026-06-02 04:02:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 98aab9ba-6c99-3215-83b1-0e2a18fefcf0 | -19.68784 | -43.75528 | 2026-06-02 04:02:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeedd67f-0350-3c61-87bb-f21f6776b37f | -18.07811 | -50.59089 | 2026-06-02 04:02:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5dec19c-34d8-3977-b7a8-a525cadb39b8 | -21.55104 | -48.59882 | 2026-06-02 04:02:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 82d0d770-37af-3bea-aad7-ac57cc82da66 | -19.16471 | -40.7025 | 2026-06-02 04:02:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bf79a09-08b1-31c8-ae50-913c2a2e86a4 | -19.90163 | -44.04829 | 2026-06-02 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bffcf185-eeb4-3a70-b4ef-3db2dfe60433 | -20.28875 | -50.95965 | 2026-06-02 04:02:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 802e8f80-760e-3cae-b2b3-ae2e0e80fcf1 | -18.68434 | -42.83977 | 2026-06-02 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c23a6353-0f04-3aa1-bac2-c608e88ee354 | -20.19925 | -50.75888 | 2026-06-02 04:02:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3081e5c7-dcb6-3e0a-9fd6-3d8995143403 | -21.70234 | -48.41087 | 2026-06-02 04:02:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aab844a5-13bd-3d0f-8669-40e8e6d11d13 | -18.79111 | -50.92691 | 2026-06-02 04:02:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f074d63c-b9ac-39dd-b410-a47537c8de1d | -22.78922 | -49.34012 | 2026-06-02 04:02:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21d70bb5-21d7-380c-8414-e70fa75f986f | -21.54578 | -48.60243 | 2026-06-02 04:02:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b001c31-c49f-33e7-b249-13cf4445790e | -21.44135 | -49.9303 | 2026-06-02 04:02:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 8ecb4fee-9b49-37db-aa20-f43540a1d820 | -19.68992 | -43.75269 | 2026-06-02 04:02:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9ec80d-1e73-3656-aeaa-561295274f77 | -19.17874 | -47.35907 | 2026-06-02 04:02:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f811a879-fca8-3e98-a5d0-6dcc08211d60 | -19.68855 | -43.75122 | 2026-06-02 04:02:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53479368-57c4-336e-9015-ab7de8944212 | -21.43775 | -49.92376 | 2026-06-02 04:02:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| eca5f2b1-ebd9-3c11-a6f8-89802ba6bc2e | -22.94947 | -50.43991 | 2026-06-02 04:02:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b09cfde-adf3-3fdc-9df0-0c7f855b0f08 | -22.7916 | -49.33875 | 2026-06-02 04:02:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92d4f50e-6128-3840-9f2d-0e7522e86897 | -20.1986 | -50.76202 | 2026-06-02 04:02:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 163434e6-22fd-3c7e-8675-cace5fd5d219 | -20.19644 | -50.75786 | 2026-06-02 04:02:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7448c7f2-d989-345c-8c09-8464c479e89d | -21.80936 | -49.12579 | 2026-06-02 04:02:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4edba766-9bd7-33e2-94df-b13bf0421e24 | -19.18293 | -47.35995 | 2026-06-02 04:02:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f661a042-ee2d-3c4e-97a9-36cb33844e2d | -22.94473 | -50.43886 | 2026-06-02 04:02:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ad344d0a-b993-377b-8d49-50607312a2b6 | -18.29173 | -47.04575 | 2026-06-02 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 248a6c0b-908e-356a-88e0-0611f54a1d1e | -20.19577 | -50.76097 | 2026-06-02 04:02:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2bb567dd-f037-30ac-8e92-723c2ab7493f | -23.81635 | -48.71087 | 2026-06-02 04:02:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b0bf03a6-80fc-3794-9927-350c0660e947 | -21.27444 | -48.61562 | 2026-06-02 04:02:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53108fd7-fb16-303f-9731-de30b00a2f58 | -21.44246 | -49.9249 | 2026-06-02 04:02:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| cd067da8-99a5-3abb-bec3-0a7b0e4fc24a | -19.68924 | -43.75673 | 2026-06-02 04:02:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b43a72fd-f935-3e35-a0e2-aedad5e23b53 | -5.28937 | -43.95218 | 2026-06-02 04:46:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07a9fb1b-5f27-3fa2-b9c6-cb471aab5fa1 | -6.76821 | -45.02649 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b8f6d5b-6a39-3575-a057-63c60922e6d3 | -11.79883 | -47.33812 | 2026-06-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8d3077d-50fa-3f48-8383-58ee643f3b2a | -7.50524 | -54.99909 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75a684ee-ace4-37b8-8d05-edba3ba5eec6 | -9.89328 | -52.44221 | 2026-06-02 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f03337c9-173e-32c6-aaa7-2f1a58b9b49b | -6.60971 | -47.54226 | 2026-06-02 04:46:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 420fec5a-7f69-368f-b4e4-23675611aa6f | -11.33284 | -47.20136 | 2026-06-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a76f4125-e5e6-3d90-950e-8a083bb5d839 | -8.12615 | -45.9002 | 2026-06-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| abbdb696-7557-389e-876c-df6ce72006e2 | -9.4558 | -51.82798 | 2026-06-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9981b77f-32e1-30f0-9827-f566f9552e9e | -8.69703 | -49.07144 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a60fa11-054e-31ef-859c-5fd14202d47d | -6.99548 | -42.87826 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4d012b5e-6ed8-35ab-b337-8cb4f370d819 | -11.5922 | -47.44048 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2be99c3-1d66-3dc7-a325-67cba0940c46 | -11.58756 | -47.44502 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68544a59-8a45-32c4-aea1-05419b744738 | -10.98432 | -48.60021 | 2026-06-02 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06a98f6f-4773-3e69-a7d0-309b87b691bb | -11.58828 | -47.4399 | 2026-06-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65de63a9-667c-3f24-b99a-0de8bb558615 | -7.50371 | -55.00812 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a80cea55-0193-33ff-ac83-b52d0d16ddd7 | -8.68951 | -49.07421 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1473ca73-c5e4-364a-ad36-029f01144676 | -9.93288 | -48.01143 | 2026-06-02 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa36ef8-c6d6-3457-859b-6918cc919b11 | -10.03764 | -51.67495 | 2026-06-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69579e03-1866-3df2-b1e6-c2edfada9df4 | -8.75605 | -50.23782 | 2026-06-02 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e30347f-d489-3785-913e-4dc92cc04764 | -10.03931 | -51.68591 | 2026-06-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e07737d2-0a0f-3eb3-9931-2d0e213e164e | -10.59955 | -53.4713 | 2026-06-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7640632-7511-3662-aa30-4f6ae220ca87 | -6.98969 | -42.8834 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b2f85bb4-4ba6-3296-bad5-be839fc80b36 | -10.69813 | -49.61061 | 2026-06-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c238eaad-4ba0-3a24-b0bd-bfbee378acc8 | -9.11776 | -46.88812 | 2026-06-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11707ad8-e1f6-3a98-ad2f-fe5380b5efed | -8.98333 | -51.23309 | 2026-06-02 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f164e6e-99b8-31d4-bfeb-87ab7fa05282 | -8.72596 | -47.98276 | 2026-06-02 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27450151-5434-3dee-9f67-7776a764d2a0 | -9.37212 | -50.54423 | 2026-06-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bdc8718-c36a-3e58-86a4-5d01801c2b9b | -9.20467 | -58.06422 | 2026-06-02 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ea9d297-29fc-36b4-8451-4e92df16e439 | -8.97982 | -47.98559 | 2026-06-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fb85b81b-50d7-3057-84db-5d14b8dbe5bc | -5.3756 | -48.54645 | 2026-06-02 04:46:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1625cc07-b808-3b74-863e-17d19e987694 | -6.99009 | -42.8805 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eb7b3eb2-deba-38a4-aa88-a8a74091b8ef | -9.1922 | -58.05754 | 2026-06-02 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57587277-aa3f-37c8-8d90-7a76f31bae95 | -7.50897 | -54.99968 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18de3f90-feec-3a5e-8556-acbf9e65deb2 | -6.38916 | -44.17379 | 2026-06-02 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07c40b17-c2ee-3b6d-ba2f-83d18fb677de | -6.76393 | -45.02583 | 2026-06-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 358b0ec1-0c44-3d77-a855-2815db2f3760 | -5.61204 | -37.52891 | 2026-06-02 04:46:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d13058fd-5317-3be5-bdce-dee15ef1a597 | -9.58818 | -49.11303 | 2026-06-02 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7c6330b-e68d-3052-bc38-0e30a84dfa57 | -9.40189 | -47.36864 | 2026-06-02 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f69d3beb-832f-3dad-8043-b3587d4a9991 | -10.74927 | -46.907 | 2026-06-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8dd9803-56c5-363e-8772-8f288b5a0ef5 | -10.87972 | -51.63792 | 2026-06-02 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8795acd1-10f3-3460-b770-80a804f4f558 | -8.70282 | -49.08022 | 2026-06-02 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ecffe2f-630f-329b-bd3a-665ba05c3793 | -9.2135 | -58.06575 | 2026-06-02 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 225e506c-0355-399a-a0d1-73777de1fa5d | -6.99088 | -42.87469 | 2026-06-02 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 305f9782-9ffb-39e5-beeb-a51a4451fce0 | -7.50695 | -55.00135 | 2026-06-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65fe1a82-5f71-3a1a-ab89-5ac06c112309 | -10.03877 | -51.68939 | 2026-06-02 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff289115-73e9-39c8-a7a7-a531b1f05234 | -8.60407 | -45.92398 | 2026-06-02 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README4.md)
