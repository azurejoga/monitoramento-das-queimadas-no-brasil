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
| 3a2590df-c7e5-3c89-b1fb-a778336ac9cf | -8.62735 | -50.03752 | 2025-07-03 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e265d4e-2e47-3a3f-907e-7ce2a14d2f91 | -6.46488 | -43.72684 | 2025-07-03 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1d124ca-04fa-369d-bf5c-0525af3283c7 | -7.43878 | -44.46509 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 520045b4-40aa-38fa-851f-82d26898cb8b | -5.91623 | -43.44612 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 10115ad8-7344-3c5c-8aab-397415865b5f | -7.56659 | -43.99675 | 2025-07-03 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b2f127d-6ace-3232-a308-aaf52db6b792 | -7.19638 | -43.59205 | 2025-07-03 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc09f31b-ad7f-336e-b05b-59327467f237 | -7.09172 | -44.39094 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb408e8e-9d14-3c96-b848-90910b203a10 | -5.65353 | -46.59479 | 2025-07-03 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3758835-b05e-3800-ad85-f20817b657d6 | -7.09362 | -44.37924 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 841c57ad-bac1-3717-b52b-81fd05953b83 | -6.96341 | -42.87954 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 02b50149-7f03-3e73-a4ae-e55449b7b37a | -7.22952 | -43.07131 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 8f1f2b2d-a551-3e8e-bb88-55b1aac0452c | -6.72136 | -43.18084 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 284bc0a0-18a7-3b0e-9611-29da13fa71a4 | -6.58766 | -43.0421 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebc081ce-4544-306e-9bd6-33391e892d50 | -6.95278 | -42.88515 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| b68a2844-d1b4-3f3a-bdbe-d8644ea9254a | -5.72623 | -49.1036 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ee80a4a-3650-352e-ac1f-210676eec767 | -5.72054 | -49.10798 | 2025-07-03 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fc62eec-fe7a-31fc-bd7e-2beca646320c | -6.00611 | -43.73982 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 050fad23-e336-3dac-b63b-3750e971c4fc | -4.02831 | -48.0629 | 2025-07-03 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b45259e-4342-3c5e-b5fa-a31b6143157b | -6.96285 | -42.88307 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 50f2c125-94fe-34db-bb1c-61fac2db6a63 | -5.99638 | -43.73441 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ea0b745-9202-31d2-8f7a-005d37506625 | -7.20269 | -43.08897 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b036ef58-9802-3122-adde-e01a1d88ba41 | -6.6096 | -43.89626 | 2025-07-03 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ebe30a7f-3269-347d-a69e-f7da47b961ef | -6.58823 | -43.03851 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a569b4a-ed13-3106-813b-5cca2432e7c1 | -6.0049 | -43.74732 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99209e1b-30b8-3b66-a824-b53e194212da | -9.20904 | -45.33943 | 2025-07-03 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0135719-57e7-3458-8f8a-803a0a8b803f | -6.96895 | -42.88767 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b35456a0-61fa-39f6-b314-25083264d82f | -6.3 | -43.68103 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 68df2a62-1907-3f2c-8900-25805a9d9b92 | -6.72193 | -43.17724 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac163876-eee7-3de4-a258-41cd479e8c39 | -7.85519 | -47.87797 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71fdaa5c-cbbe-310a-b2c0-88321df430fd | -6.28972 | -43.67939 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d448fcf1-df4d-3d69-b0e1-0fa4f3d4a171 | -6.70126 | -43.15556 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d783a2d1-a2d2-3f92-b602-4da0edf8218d | -6.96057 | -42.87914 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 96b87db1-a7e6-341d-a95e-a73b60f22156 | -6.69503 | -44.06268 | 2025-07-03 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76d96037-bc5e-3659-8aa8-628df4d75be4 | -9.69021 | -48.33142 | 2025-07-03 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe38cd4d-e525-3716-bb09-59aa55699f46 | -9.80694 | -48.38644 | 2025-07-03 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1867c252-f04c-31da-ad04-b4aceff23ed6 | -7.23343 | -43.06828 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| ee83f29f-5e1e-34ff-91cb-cc1745f0f5b5 | -9.87284 | -48.45535 | 2025-07-03 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4c45f9-d63c-353f-923f-705e7a16a2ef | -5.39665 | -43.24722 | 2025-07-03 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c5d5e9e1-5ba7-3330-b558-c33775ddc2dd | -7.25958 | -44.33677 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd36096-b96f-3977-909c-247abbe3c46b | -4.03289 | -48.06362 | 2025-07-03 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e6a1e0c-a442-3201-ad6b-003706dc3e8e | -6.90964 | -43.04962 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7cde1c6-1e2b-3c1d-ac75-cd21c803438e | -6.65475 | -43.37101 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d54c9327-4912-3b36-91db-d0e71cc2adfb | -6.72654 | -43.14849 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c753aa0-749f-3720-a27c-906ab2fb23a2 | -7.86302 | -47.88336 | 2025-07-03 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebca3c43-8960-3e82-875e-244a1fde153d | -6.00206 | -43.74302 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 832ed7c8-0d37-37dc-84c1-8320c9c22215 | -7.20603 | -43.0895 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb98d932-7d27-3363-b046-76124c154833 | -6.60613 | -43.03404 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd28bfcb-568b-32a7-9c24-bda080f90374 | -6.59158 | -43.03904 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7979e3d2-21b6-37b9-b3d8-d744bc82939b | -6.73141 | -47.37723 | 2025-07-03 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c62ebb53-7834-32dd-90f7-8e19df3f88fd | -6.18282 | -42.61014 | 2025-07-03 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fd659856-6525-3738-a57b-a1f720f33cc4 | -7.23064 | -43.0642 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 18af3d94-6af6-3f59-b4b3-6e2647056468 | -8.43552 | -49.20477 | 2025-07-03 04:08:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 539c8851-4f9f-354c-9f83-1eedfb8b02b8 | -6.96618 | -42.8836 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 326c7c2a-fd48-3ec0-89d9-3ef71adb0610 | -6.97065 | -42.87707 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7cb5d5ab-b437-3c28-9e35-22797f871b26 | -7.1982 | -43.09558 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b28b8324-9ed3-3139-9992-480753075172 | -7.4593 | -43.08203 | 2025-07-03 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e18f2dd8-0da7-356c-8ca2-e1b377107826 | -6.21048 | -43.36061 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e3490b1-89eb-3a99-892f-8f59e9407f2b | -9.73035 | -49.05925 | 2025-07-03 04:08:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7d669b5-51b9-329d-952d-04ce0d598c84 | -6.69021 | -43.16878 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.1 |
| eb63429a-e389-3ad1-bd83-aa5b64b7d6ec | -6.02424 | -49.23074 | 2025-07-03 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f18267fe-3121-33b9-ad17-f30d09187042 | -6.69248 | -43.15443 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 05d70936-b721-3096-97a1-41b56d76769e | -7.06056 | -44.36176 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4e77966-41bd-31f9-8787-08846e077aec | -6.28911 | -43.68314 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| bc5d4c43-a2e8-33dc-b8a7-7d52154425a5 | -9.79569 | -47.75045 | 2025-07-03 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9287a119-198a-3579-b0f8-9c318082b6f2 | -5.99516 | -43.74195 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c4fa45e4-6a23-330f-a40e-4d2634b721ef | -7.19763 | -43.09914 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 74118321-acfb-3264-989d-dd822553b905 | -6.96952 | -42.88414 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15815479-23a4-3196-bee9-35f3ef0ac55d | -6.69978 | -43.15191 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9ace9a76-2c03-3f26-b5cd-af8d549ea3f8 | -6.29032 | -43.67565 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff8389b5-e0cf-3572-aaf3-dd4e006ebcf3 | -6.60164 | -43.04066 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1cb0864-0002-39ce-b4db-3d144e932105 | -8.10555 | -39.59637 | 2025-07-03 04:08:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 75914f20-a9b1-3da1-a995-467a9c00b2a9 | -6.59772 | -43.0437 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97984417-f36d-304f-8043-171c21cd5a34 | -10.08521 | -47.9883 | 2025-07-03 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5603cf9e-ca61-3260-8840-e387b48efe67 | -7.00672 | -43.80856 | 2025-07-03 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3e452db-304b-3a69-b73e-5dbfd575507a | -6.72251 | -43.17365 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a1688a2-2b0c-3095-a7f9-1cbaf6d75512 | -5.92049 | -43.48489 | 2025-07-03 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c5fcdc2d-cba6-3d4c-a602-fb4a0ff2fc2b | -6.00671 | -43.73606 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f60368fd-b0d8-3251-96ad-9f5f8f8143f4 | -6.69641 | -43.15137 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d63d0e67-3a4b-30f5-8932-66558b4ae4a7 | -6.72318 | -43.14797 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27cf3655-b118-3789-8d70-70b2e276034a | -6.00551 | -43.74356 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 969f3c56-794c-3305-9d6f-b1a3d578acc8 | -9.83099 | -48.37395 | 2025-07-03 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab342e41-4d1d-3e8d-a0f4-a2f4de1710de | -5.9938 | -43.7366 | 2025-07-03 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c2911da7-785e-35ec-8cd2-f026a7a56f88 | -6.9793 | -42.8798 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 05107c44-6f60-3e2b-84e3-4f66ca7513f1 | -7.2222 | -43.0447 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 68c3305e-8b9f-3335-a449-14d9b4089f3f | -6.9605 | -42.8816 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 291.1 |
| 16fa3763-acdd-35d5-b0c1-948a2d7ac790 | -6.9416 | -42.8834 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| efcd9b5c-9aa8-381c-9bc8-015871e8947e | -6.2945 | -43.6659 | 2025-07-03 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a9744336-e730-3e56-b147-ec985e5124f3 | -6.9607 | -42.858 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 3ddcc186-814a-3c98-8e45-ae553b7aefd1 | -6.2943 | -43.6891 | 2025-07-03 04:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 997eaeae-3306-359f-8ce7-c5ff76b8a8ae | -6.9602 | -42.9052 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 5c722a77-ad4f-349e-9e6b-6c84ca940ed6 | -7.2219 | -43.0682 | 2025-07-03 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 43783a6c-0162-3ce6-968f-0f1f1e88f397 | -11.6588 | -44.5974 | 2025-07-03 04:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3a5f1dbe-2973-32ba-ace4-eb350740f1bf | -16.29506 | -49.95187 | 2025-07-03 04:10:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9094484a-7c88-3611-8fcc-7b15cb293971 | -10.82448 | -48.36288 | 2025-07-03 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf706413-bd3e-3989-bd29-825e33365514 | -11.65063 | -44.59954 | 2025-07-03 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 87a17156-a151-3a30-86e6-bf29542bc45b | -14.50051 | -43.80725 | 2025-07-03 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f4fccf-0e54-3d9e-8056-e61c67442978 | -13.94768 | -46.3718 | 2025-07-03 04:10:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f2caf3d-7cf5-3d2e-ae8a-8d397df2e155 | -11.56464 | -47.45728 | 2025-07-03 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d698eee-ac24-35a8-ad3e-505b4e96018d | -12.55124 | -43.95411 | 2025-07-03 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56d932fa-a43e-3ecc-b32e-a60d9a878c30 | -13.28384 | -43.19332 | 2025-07-03 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README11.md)
