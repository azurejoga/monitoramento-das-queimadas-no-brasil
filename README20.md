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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 442bd3e7-9e31-339a-b884-08971814ecac | -7.39326 | -44.87675 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cb8048d-ab19-365a-9e38-817b10f98f65 | -6.55416 | -49.50858 | 2025-08-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f116b1c-c85f-37fc-aa64-c961f1767e73 | -3.44197 | -48.96783 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb1c558-9cde-33e2-8282-f2db31c89c7f | -6.90633 | -45.2073 | 2025-08-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb08ba7b-7c47-37e6-bb34-4c4b05da3f4a | -4.99834 | -45.32569 | 2025-08-15 04:02:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb7190f3-2c26-3e22-b361-9c52f078c658 | -9.2176 | -45.33577 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e063aa0e-8ee6-3598-8da0-437285088f13 | -9.00507 | -48.72663 | 2025-08-15 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 695aeab8-8083-3515-be92-361480e8bfa5 | -6.60953 | -43.89074 | 2025-08-15 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b9deaf1-6d32-3fe9-8cdf-f867eeb16d0b | -5.76336 | -46.66823 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 554a9fd1-928c-35c4-bb45-fbae589e07d5 | -4.70942 | -47.44796 | 2025-08-15 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27fc99b2-8190-370e-8256-f6628a94a64e | -11.92403 | -43.44057 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 765a412f-16b7-39ff-b0d1-50c3fac0a727 | -5.6021 | -45.38228 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f537c94-9611-336f-9a48-50e3de70cd0e | -8.3209 | -45.01781 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efc59e60-f4c6-383d-80bd-f132150794c1 | -5.22637 | -43.19212 | 2025-08-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca244131-f6dd-3ba5-98bd-1f71988f1d00 | -9.81309 | -47.75926 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31119a39-67f3-3eaa-9b86-49eb1017ef3b | -7.89723 | -42.12296 | 2025-08-15 04:02:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 942895dc-33b8-3cfa-8d3f-8a3586684f2a | -5.32914 | -44.98787 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48e3013c-cfcc-3d0b-9e6b-9704879ef2ae | -7.01995 | -44.30046 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5a813e8-70f0-36d0-b921-689b9e5d0810 | -9.83636 | -47.8118 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f5b0d45-173f-3d91-96ad-088890e91385 | -9.03515 | -40.51799 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 994dbbb1-e888-31f3-904a-b63da5218a64 | -5.76261 | -46.67274 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3f88abcb-027d-3934-bf48-0825219816df | -5.75886 | -46.66747 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7d252c7-9ab7-345b-8567-df31bc677530 | -6.93703 | -44.56694 | 2025-08-15 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ab38fe-d6e4-3f55-bda9-3aa14b52e70d | -8.31244 | -45.01324 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e06872a-9065-32a2-9f11-3ce2767aaa65 | -8.52411 | -43.29971 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14d0af40-552c-3e15-84fc-d40a1b509c51 | -5.54892 | -45.36992 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 602cab93-9add-366e-940c-ec9716f729b9 | -8.31389 | -45.02855 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ef4fcb8-2f96-3a46-a6c0-ac9ab087e459 | -3.42791 | -49.04997 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b33290e1-474c-3543-8cee-df5b616a1905 | -7.1511 | -44.39948 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14bcf92f-61c0-38d9-9071-efc3b0975132 | -7.40043 | -44.85802 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c34c55-17b0-308d-a87c-e846beabed3b | -7.85724 | -48.23372 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5166ca7a-ca1c-3370-9857-06ef0343aef9 | -7.38771 | -44.88593 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6e84f07-db77-350e-8109-8a2405126181 | -4.66747 | -48.8693 | 2025-08-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abf15799-ecb3-32dc-9d65-3b34ec046ae9 | -5.22274 | -43.19152 | 2025-08-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e74542d-00c1-3dab-bafc-c0ae49e52640 | -7.38383 | -44.88518 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6156118-349a-3e5b-a9e1-bb13b31ae3e8 | -7.4479 | -49.2454 | 2025-08-15 04:02:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff5585b9-8a2e-3f5d-920c-319f615579ed | -8.19142 | -42.26026 | 2025-08-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9c40027-f9c9-3e30-82b0-d835e682cc8f | -5.54829 | -45.3736 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64d45620-2325-3ff3-a87c-d5dbcbeb3621 | -6.91091 | -45.20456 | 2025-08-15 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7d8b883-303f-3424-bfe9-0de2a2b59983 | -7.14729 | -44.3989 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cca75264-e6d4-3f0f-8f62-06e111b7162c | -9.85286 | -47.82437 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6411822b-5179-3bd8-8666-a28fca1fdc2d | -9.03846 | -40.51852 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0fa736bb-7d16-311d-8332-e03808210cd0 | -6.55475 | -49.50517 | 2025-08-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bfefddb-14da-3a77-8911-c240e73d8729 | -9.18725 | -45.32548 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 97adc05f-dc67-313b-8823-458e1c279966 | -9.55485 | -40.3257 | 2025-08-15 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fc002540-94a8-3d4c-8605-f3cbe9548522 | -9.19421 | -45.33177 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 747e1fd8-869c-368a-bd13-d3f44ae1cf86 | -8.19481 | -42.26082 | 2025-08-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e688b0a3-25c9-36ad-b38f-6224dafd9dbb | -9.03076 | -40.52443 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a55f324b-d379-314f-9b34-829c558a5c80 | -9.14802 | -40.92807 | 2025-08-15 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a867e821-f365-389e-9e0d-5b95564cdb50 | -7.3855 | -44.87529 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a119e57-0496-3282-aa35-91f3337a0895 | -7.39243 | -44.8817 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4658e791-11fd-311e-ad51-56225726e775 | -5.26735 | -43.58945 | 2025-08-15 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7f2fa9c-f77d-3fdf-8bc2-d0fe8df0ad8d | -9.84172 | -47.80803 | 2025-08-15 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5b6f593-c2c8-388e-a2de-00c0c3c87367 | -8.19422 | -42.26451 | 2025-08-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9528da0a-8524-32f5-b166-6905b1c70027 | -8.52189 | -43.2912 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a9b3d5c-c620-373f-9a5f-e04a93d1cfac | -4.77402 | -45.31826 | 2025-08-15 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 346d238b-2d60-3cfd-ad8f-b1f47eec4bf6 | -11.92746 | -43.44115 | 2025-08-15 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baa87be8-591b-39a1-afe4-b45ecfdfbf00 | -5.75811 | -46.67196 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 020516ff-65ff-31e4-903b-f3d680c01ac9 | -8.52698 | -43.30426 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f47cc941-4cc4-39d5-8b20-0b05efaae538 | -4.66277 | -48.86479 | 2025-08-15 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2473c4df-9cf3-3a0f-a75c-2514a9fe7758 | -9.03022 | -40.5279 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3191fabc-d78f-3919-baf0-f2cc60834c09 | -8.5195 | -43.32759 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b4ab473-a1cc-3409-ac4c-bcaa5562e946 | -7.3996 | -44.8629 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b961852-b411-3f72-9809-e13b7a6d56df | -7.73995 | -43.97834 | 2025-08-15 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 982edde1-6573-30f7-b8cf-080bdbfb2169 | -5.36217 | -41.24517 | 2025-08-15 04:02:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 105369a4-58bc-3660-b15c-f9a5e9ecbb63 | -5.54668 | -45.36956 | 2025-08-15 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f11c0b89-88af-3206-bf91-46dfc984eb94 | -7.86785 | -48.22996 | 2025-08-15 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 277de735-f788-34e5-b8b0-d16b34c274bd | -8.51597 | -43.32702 | 2025-08-15 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7ae437f8-fd36-39b3-b324-1ff66a37233a | -6.09158 | -44.61367 | 2025-08-15 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac8c1c39-8ad4-32a7-bd06-2440a5f8a563 | -7.07891 | -44.94953 | 2025-08-15 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d4b59e4-a565-3a67-a8b9-e4434b1e98dc | -5.54314 | -42.66343 | 2025-08-15 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83506307-4890-3e14-beb5-0e73c1decf88 | -5.78572 | -43.60628 | 2025-08-15 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e10cfd4-6e3d-3914-9c32-1448a37889ef | -9.039 | -40.51504 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb4cc5c3-2ea5-34de-b905-71f31b4342d5 | -5.11856 | -42.79689 | 2025-08-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d00bc62-5667-35cd-b508-f22aaae4a4fe | -7.14649 | -44.40371 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20c7b938-31db-3ece-a4e3-8d971118e7f9 | -6.96328 | -43.86234 | 2025-08-15 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 838dd1c0-882f-36c7-84a7-30a65c525135 | -6.33798 | -42.79697 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9905d84-b254-390b-a2b9-86ddcae0165b | -4.98121 | -41.71511 | 2025-08-15 04:02:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f71669a8-6ec7-390e-a964-0974af2eaaa6 | -6.30647 | -39.39352 | 2025-08-15 04:02:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4d8f55ce-8ae0-3c4a-ae99-d8e27debc331 | -10.53652 | -42.5523 | 2025-08-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 64cc2793-0cb3-3933-8a4e-3bbc96a94693 | -4.2263 | -47.22051 | 2025-08-15 04:02:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14fe9b11-853c-32d2-9f04-69e40af55ad7 | -5.76539 | -46.6679 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 99d579c2-74cd-3c6f-83be-95f00a1c41ba | -8.29082 | -44.99956 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93e7ec62-6e41-3bd9-955c-a242fb7c0232 | -7.02598 | -44.28726 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89916f5a-9465-3814-bba5-a3c523900c5f | -10.36104 | -50.81087 | 2025-08-15 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23b39725-350f-3b50-b850-54ba8d7c678c | -10.9678 | -49.56911 | 2025-08-15 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d0ac681-f442-3b5b-b063-dfacad6e74dc | -7.42801 | -44.58563 | 2025-08-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37f1a204-6cc4-388f-95e1-d04418e336f9 | -7.38298 | -44.89016 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b075fcdf-1c68-3bc5-8c5e-ceeb5a6e8c52 | -7.02071 | -44.29581 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c99a3f9-be24-33f6-9287-c4f85e7edaaa | -6.3402 | -42.80559 | 2025-08-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e7599ba-308f-327c-9474-f79fb3b6f9a4 | -5.86157 | -44.74164 | 2025-08-15 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95d9af88-af65-32ff-91dc-75fbf759a252 | -3.99053 | -47.83422 | 2025-08-15 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06c7709e-5aff-3a76-b331-31dff11ae562 | -7.39714 | -44.87749 | 2025-08-15 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bca5a82-4d8b-3c9d-a525-35fe5fae5cce | -9.18641 | -45.33043 | 2025-08-15 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 894b2ead-1818-3c0d-a96b-4c2a21eb41eb | -3.44629 | -48.97033 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14658f4a-ff0f-309e-8531-26922d8a27d2 | -7.73935 | -43.97681 | 2025-08-15 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b903bfb3-d2d0-3d40-bb49-afe5c6d83e6e | -5.54766 | -43.89808 | 2025-08-15 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 787e364a-9313-387d-ae95-17ba7e8d6a46 | -7.16073 | -40.4152 | 2025-08-15 04:02:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6c30d095-d362-3e82-a4a4-5ed0dbfc82c2 | -3.42853 | -49.04632 | 2025-08-15 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06e74567-65fc-3732-b150-a9881f050a70 | -9.03792 | -40.52199 | 2025-08-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README21.md)
