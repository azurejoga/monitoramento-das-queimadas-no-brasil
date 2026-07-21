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
| 50b8a122-3c39-3011-9102-293bea0370cc | -4.77124 | -41.79727 | 2026-07-21 03:40:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cacfba7a-2f4a-3bc2-b361-4b2eca4cc824 | -6.31066 | -43.65956 | 2026-07-21 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6224ec14-5712-31c2-ba49-2ccbb4243bb6 | -4.65758 | -42.42135 | 2026-07-21 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52fadfb3-e78a-3b47-8b3b-470749c7b62b | -3.5209 | -42.69868 | 2026-07-21 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32947baf-47ff-398b-86b4-f52464cc8f1f | -5.74496 | -43.26912 | 2026-07-21 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58a45e17-f960-3114-bdf3-36ebd5ecb666 | -6.43832 | -35.45707 | 2026-07-21 03:40:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49ba42ee-512f-34c7-988a-a6267a8e5e35 | -4.65815 | -42.41806 | 2026-07-21 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7ca7833-6418-36d4-b725-d59a43882bc3 | -6.31131 | -43.65594 | 2026-07-21 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be5db6a-599f-3899-a68b-ac1a16043300 | -6.42506 | -43.71992 | 2026-07-21 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bd67fcb-81a3-36f7-83ce-44c433e7e53d | -4.77176 | -41.79428 | 2026-07-21 03:40:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 06dbde10-998e-32a7-b17c-88577becd779 | -4.16118 | -43.09488 | 2026-07-21 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f6236c-ee45-3ae3-8878-0fbfc6fca81d | -5.74431 | -43.27282 | 2026-07-21 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65a3d256-26df-351f-87dd-5bcdfe9c7ac6 | -4.30311 | -42.32439 | 2026-07-21 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7672dc4a-51ae-3a18-8f61-2aadec8e5bce | -4.77227 | -41.79131 | 2026-07-21 03:40:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4c4863d6-4eec-3032-89e8-7a7b96ffb743 | -6.30641 | -43.65105 | 2026-07-21 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 47f46c82-c354-39b0-a1ab-a9f6da429b8f | -4.65357 | -43.22412 | 2026-07-21 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36ef9d15-a688-33ee-9b4f-145380ba166f | -3.52023 | -42.70177 | 2026-07-21 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7ab194-aeee-383d-956c-17122a92d21d | -4.16054 | -43.09866 | 2026-07-21 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05a6d1e6-ba31-31fc-bd18-41bb3da00bb3 | -11.38951 | -47.50061 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19e0800d-8e73-34d0-98e4-12d667ee5686 | -13.5541 | -46.11419 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31bc6649-bd77-3866-abea-f8eafaf320d4 | -11.90987 | -43.84771 | 2026-07-21 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7679e79-887e-36cf-9aab-5f14085ec725 | -7.83402 | -47.11178 | 2026-07-21 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e28d04d8-f3d1-3f1a-8fc7-00b03ae2ca47 | -12.52319 | -48.25814 | 2026-07-21 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5203391-c8e6-3077-bdde-0710910b82d1 | -12.45708 | -46.52082 | 2026-07-21 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af74834c-ecd6-33dd-b219-b0293f053b90 | -12.13564 | -48.25551 | 2026-07-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a1af42b-5dbc-3758-8b46-49aaee0cfbfb | -11.38426 | -47.49318 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efd35948-7e61-3090-a438-453418822561 | -13.3091 | -45.13766 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 977e0e0f-f4e3-3a72-b011-410ea3967ee4 | -12.45802 | -46.51614 | 2026-07-21 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8071198b-bae5-3e5b-94a5-eaa774e16718 | -13.30769 | -45.14165 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| a7df5e58-c089-3d90-879d-7a61dbb43516 | -13.3138 | -45.13937 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b8640c38-2d35-397f-927d-aacd7533edf2 | -12.69536 | -45.32825 | 2026-07-21 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee43f053-2255-3999-8825-bb65f9716d30 | -10.74177 | -44.84074 | 2026-07-21 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 482f5181-a904-3ba2-aab1-1afde920c3fd | -11.36911 | -47.50095 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d8e36d9-fe7b-3467-a2f4-657f3af60fbc | -13.30298 | -45.13681 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 2cb66ac4-5800-3d06-a720-2ba0253e4640 | -13.307 | -45.14523 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 69a5de9d-7e18-340e-a354-88f4bf99670a | -11.34447 | -47.99307 | 2026-07-21 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c131595f-d44c-3a98-bb4a-39f8fbce54c7 | -10.74251 | -44.83688 | 2026-07-21 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f01e8494-148a-3e28-8ab8-3cf2294d81c5 | -13.25863 | -42.46677 | 2026-07-21 03:42:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa021c29-7268-3808-98dd-c96b17e12022 | -13.56611 | -46.11416 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08080864-71f1-34df-a203-a0a82451d780 | -13.30227 | -45.14041 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b873f134-eb85-3e36-8346-398cdcaed510 | -13.30982 | -45.13408 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 018ebcc3-1f60-376b-8e36-98c595ab43d0 | -13.30438 | -45.12962 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 4bc589d8-aef1-3dad-9466-14e9f8434c64 | -13.31049 | -45.12734 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 14703134-a6c2-39ab-b8fa-0577b6eca9c2 | -13.55461 | -46.11166 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b605dd01-7d03-375f-b912-bb245a583da0 | -11.33939 | -47.99754 | 2026-07-21 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9b54aec-9093-3dd2-af41-ff2cb00ba582 | -12.45896 | -46.51149 | 2026-07-21 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b8cab4f-0841-343a-aeee-4fb9d1b77020 | -13.55378 | -46.11578 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c60f1ec-211d-354d-9450-fd79f699d77e | -11.39576 | -47.5032 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c700bb93-1037-33e3-bf2a-941504f996a2 | -12.1344 | -48.26151 | 2026-07-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bc2936e-0b64-3c3c-b183-578decf4f84a | -13.31451 | -45.13893 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 3d1dc323-7565-3964-9798-f7f3aa6b84d8 | -13.30508 | -45.12606 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a96b4f45-7c8a-3438-aec2-7446e3e4d5dd | -13.56645 | -46.11251 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd2566c4-3bda-3675-8a40-cd58a8b1e92a | -13.3145 | -45.13578 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e8a02d4-f658-3ecf-bff0-a7a24488fddd | -11.34326 | -47.99905 | 2026-07-21 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 544e4ffa-3414-330a-9ad4-646ecbabc33a | -12.66298 | -48.2043 | 2026-07-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c232f86-a095-3fc2-9afe-99744b46a2f0 | -13.31311 | -45.14294 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 20769a23-2ee7-3754-91e9-cc40a22d7895 | -12.51658 | -48.25647 | 2026-07-21 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbd6a890-4935-3a2f-82c6-62f2193f4842 | -12.65639 | -48.20272 | 2026-07-21 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b70c33e9-e2a6-3d6a-9379-97265473a615 | -12.52445 | -48.25217 | 2026-07-21 03:42:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56216c6e-96e9-3361-95e5-2e4a8ed65187 | -13.69592 | -45.19792 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4de8a414-6b56-3e46-98aa-84c2faa79f47 | -12.13639 | -48.26436 | 2026-07-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d495cf98-5e34-38d1-b6a9-8e0bd9362378 | -13.30368 | -45.13321 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 00804537-ef32-3722-b141-6c38639afac2 | -13.5656 | -46.11666 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e00716db-19c2-32e2-8f2e-5a6b6d402809 | -13.69523 | -45.20135 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13ad8fc0-687c-3a96-addd-7be92fa24828 | -11.91047 | -43.84456 | 2026-07-21 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbc3328b-4b57-3262-afd7-0c2023d56f26 | -11.3461 | -47.99884 | 2026-07-21 03:42:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ebcd0dc-a281-3148-9911-b16065f2eb66 | -11.37436 | -47.50843 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d7713a8-4e6f-3dd7-869c-aedab9cf5f72 | -11.37025 | -47.4954 | 2026-07-21 03:42:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9374ab19-9386-33ee-b839-bb19eaaaba3b | -13.31118 | -45.1238 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6d1035d9-8914-368a-b9ea-56cf0861b99d | -11.82972 | -44.77527 | 2026-07-21 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daf4ebbf-6ba5-366e-a72d-a364254879b3 | -11.83575 | -44.77346 | 2026-07-21 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce4367a1-751a-31c5-9c4b-106add830513 | -13.3152 | -45.13222 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9499a62a-47c8-3d65-aab7-45c9b3c4ffad | -13.31523 | -45.13536 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| ec3ddc75-9ede-3968-89b2-cf4339693817 | -13.30837 | -45.14122 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 923d80cf-27c7-3a27-afe8-f4dba09eb9fb | -13.30839 | -45.13808 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 1e3d8a6c-5a79-316e-9ba8-257e7349cecb | -10.37662 | -48.32679 | 2026-07-21 03:42:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54da5a33-313b-3ddf-b757-1861cbd565f4 | -12.13769 | -48.2583 | 2026-07-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 450fd064-d791-3b52-b427-29d9063388da | -13.31127 | -45.12696 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 681f2af6-b0ea-31e1-8411-49a554f7376b | -13.31379 | -45.14249 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e787fe5e-c250-3ef9-8c5d-eb1a71d47dae | -13.30765 | -45.14479 | 2026-07-21 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6b86371b-ae21-3378-b6e6-924bb0d87f87 | -16.02095 | -43.04186 | 2026-07-21 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2540f85-8044-3cfe-a874-a94e06837ad8 | -17.58362 | -47.5104 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a555244c-25b3-32f0-b8be-85d06a71d1e0 | -20.36117 | -46.61072 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52a8fde-753f-3082-8abb-58b6ff3609b0 | -14.86476 | -41.58746 | 2026-07-21 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 93cd057f-07af-353b-8608-c6add018f94c | -17.46198 | -47.15434 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c724b640-d162-30c2-ad52-5f6b0d3612d7 | -17.4622 | -47.15698 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9984838-6417-34f5-945d-14e715b06dec | -14.86521 | -41.58464 | 2026-07-21 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4a54d87-1778-38d5-937c-088572fa4e70 | -17.46405 | -47.14853 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3499f2b2-4c99-3e55-a802-451f104b15fe | -19.72417 | -46.16935 | 2026-07-21 03:45:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41dd59e5-fe20-35b9-8451-20d4d17a5e96 | -19.18813 | -47.36255 | 2026-07-21 03:45:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a76f24f-4087-3e75-817a-2e657640fe67 | -20.40264 | -46.49328 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 183fb421-cae9-3bfb-a39d-1204489185b0 | -17.5806 | -47.50247 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba85f742-dd8b-30c6-9d81-35fab1faa077 | -17.46313 | -47.15275 | 2026-07-21 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e472dfbd-fc63-34cc-a2a7-dbf7f7931276 | -20.42934 | -46.46977 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69d8953c-a7ec-3c42-8d47-910a1584eeb2 | -17.86487 | -50.51608 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 371147df-974f-3bed-8b7f-d8c4a2810dcf | -20.37464 | -46.59897 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eaedcf71-77fc-31c1-8844-6e7b81be8edd | -17.5846 | -47.50599 | 2026-07-21 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 407776be-6e54-3b58-9a8d-2d1b66fcac45 | -17.86645 | -50.50935 | 2026-07-21 03:45:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 5fbd2801-ee87-33cc-8b3c-0574fdb8520b | -21.35999 | -41.95315 | 2026-07-21 03:45:00 | NOAA-20 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44215602-4727-34ff-b93c-6becfd15ec2f | -20.37555 | -46.59468 | 2026-07-21 03:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
