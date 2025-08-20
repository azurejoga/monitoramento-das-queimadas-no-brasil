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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a340cb35-3320-3359-b7a6-df7835577ee6 | -2.37977 | -47.6636 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b669d44-0171-3cd0-95da-612409dc0659 | -2.5878 | -51.92247 | 2025-08-20 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf8459e3-7cea-35f0-9ab4-273a72ae4f55 | -3.88307 | -54.21238 | 2025-08-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d157b39-936c-3cce-b758-93d234eae1fc | -3.04074 | -49.43755 | 2025-08-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fa67ab2-dfca-32ac-8ec8-bb4d13e94914 | -6.94723 | -42.87885 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 2b30a604-7990-3fc8-abb8-a1c59b2ad6e7 | -5.88195 | -46.50654 | 2025-08-20 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cedd1d21-70f0-3129-b26f-7a8d309383ee | -5.78123 | -43.89765 | 2025-08-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85aa3ebf-eb4c-302c-a4ed-8b4d9cb2f124 | -3.36119 | -43.35872 | 2025-08-20 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f35ba01c-f299-3a56-88a1-bcc9f96058cf | -6.37032 | -43.2705 | 2025-08-20 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06d30724-2846-39a0-97f4-dd01bd39b816 | -3.81794 | -41.57503 | 2025-08-20 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21773d63-ac06-3c13-8ae0-8a913b4c58ce | -4.90937 | -43.23571 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb6a2328-e3d5-3f8d-8921-ccde9a2f7a4e | -6.0706 | -44.11803 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c9ac18e-f37b-3bcc-b03d-c00a42592bb1 | -6.61825 | -43.88387 | 2025-08-20 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3845878b-6772-3868-8e73-8d0c1e398edc | -2.77414 | -48.59741 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5266f19-79ff-3d27-80f9-4b844155a34a | -5.98751 | -42.8245 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e5889112-d20e-30ce-be36-c88059880b6c | -5.87882 | -48.11765 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 832ceb2f-7052-30fd-a7c4-f1d442a77806 | -5.40542 | -45.18888 | 2025-08-20 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edfe9967-fafa-31ff-a347-ea36de98f3e9 | -4.48207 | -43.90148 | 2025-08-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 462addb2-e37f-3279-b573-0551fd25cce3 | -6.9541 | -42.87492 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 8022d9c5-4cbd-3746-a793-94b274f78250 | -2.91689 | -48.2987 | 2025-08-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 721f2c39-f6af-375d-9e3d-2ee8d59b8c61 | -5.87766 | -48.12577 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43f9be1f-4542-33a2-b8f1-076b1ddb05a1 | -6.85586 | -43.61228 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d1ff270-7589-35fa-83bc-fabdc7412323 | -3.64871 | -48.32814 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5855ea75-0d69-37e2-af48-802e4068028a | -4.17223 | -42.03002 | 2025-08-20 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bbca2af4-fd83-3e73-8826-da470cb12642 | -4.60611 | -43.32799 | 2025-08-20 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 508c441f-9d8e-358a-b930-fb64480bce49 | -5.78507 | -43.61452 | 2025-08-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a48d742-d846-3de3-97db-aed14793207c | -5.63226 | -43.3969 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35bb2c58-8280-37e4-bdad-fb8a4fa0cf00 | -3.98424 | -43.24252 | 2025-08-20 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d060df6d-2884-322b-b4fb-2a15bccf9b95 | -4.02231 | -48.06281 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fdb72d9-cf29-3a56-9f79-b775a03fbf53 | -4.42982 | -47.75964 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f61571e-419c-3161-8da0-59819e31522e | -3.99062 | -42.52129 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5ce50690-cccf-31bc-88c7-bae1c1cc5839 | -6.94979 | -42.87488 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| cbe07557-e251-38fc-99d9-6db855ec18ac | -6.317 | -43.7509 | 2025-08-20 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 35ee3bd1-f84c-328d-b141-f38ac530dbd7 | -5.87289 | -50.14845 | 2025-08-20 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf2bf937-5d4e-375f-bb4b-31840bf1b4f6 | -6.51766 | -45.46743 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d10b691-7b3f-39b4-9774-bedc582091df | -5.88284 | -46.50579 | 2025-08-20 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cf11c1f-edde-3faa-94a5-d624759b79f8 | -3.48353 | -47.67891 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d7ea978-771c-36e9-a14e-f67a1fad0223 | -3.97432 | -42.50446 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73f391b9-796c-3112-822b-95bbe45bb44d | -2.77669 | -48.59476 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f93b3d9-023b-3984-a1f4-e51dedfd62dd | -6.01098 | -42.83268 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2dcd0d93-f276-3f87-aaec-f56c19a4eafd | -4.16897 | -42.03186 | 2025-08-20 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2dfbad9b-eb8c-3c02-aade-b29b7a9a856e | -5.99059 | -42.84379 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8afcfdb-abd8-3968-877a-3e0adfb502ae | -6.57713 | -44.47603 | 2025-08-20 04:55:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c47308-e743-3f37-8138-ba2e73023793 | -6.61938 | -43.87561 | 2025-08-20 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e650378-c961-3cb3-9774-fa05fcea95cb | -4.60024 | -43.32713 | 2025-08-20 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b06776e-49c5-3213-846b-fb525324b29b | -4.87501 | -47.75664 | 2025-08-20 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe2da03-4fa3-3a39-8a0f-2e4933ca03c6 | -5.66377 | -43.50509 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e3c81b7-d976-33da-ac2b-6f9aca61da2c | -2.38458 | -47.66027 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d65dcbbc-4fb0-3f01-9d7e-0bd922f5a6be | -3.7468 | -53.80621 | 2025-08-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95355c60-a594-3653-8e04-383191570de0 | -5.78566 | -43.61022 | 2025-08-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ecf014a-fae0-3cba-a1fc-0457e9db8da1 | -3.2298 | -46.79847 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dfe2b78c-0353-3796-b917-10238b010ae7 | -5.37401 | -50.89621 | 2025-08-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 199f2463-f530-3adf-8448-fb094579c0a2 | -3.74028 | -48.93117 | 2025-08-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95148a2e-3281-3b04-b087-99979c50ff97 | -4.871 | -42.71092 | 2025-08-20 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 697f924b-8d85-3426-a327-2d8f06f53063 | -3.38634 | -47.60758 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 897d9cec-bbf9-3528-9aaa-e0a32d518fb5 | -2.90522 | -48.2932 | 2025-08-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ae074ce-147f-3db8-b027-176c57b21d20 | -3.23504 | -46.79452 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1b76e454-2bdb-3b4e-988a-54d112503bbc | -3.4819 | -51.19027 | 2025-08-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e62048da-2adb-3b75-9e5e-513d1bca3d47 | -6.04941 | -44.14535 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0311a503-8c92-3a71-b407-ce75c333c345 | -4.4255 | -47.75889 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 967dea33-1af0-3d53-8328-b6b392458c48 | -6.00598 | -42.82318 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0c66ba8-1d23-3311-8c6e-c10d12c7a2f0 | -3.96751 | -42.50825 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79e28d4f-c646-31f2-8c9c-b645a608b066 | -3.39666 | -46.90704 | 2025-08-20 04:55:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 310797b5-d401-3ade-b9e4-d3a44f893009 | -4.42654 | -54.81171 | 2025-08-20 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 263efcf9-f12f-348f-8a95-6c6a625e99b5 | -6.94358 | -42.87384 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 9541aa7e-6311-3806-bcb4-655b1325e5f8 | -6.23556 | -46.24085 | 2025-08-20 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f70beee-b9b5-38ad-b359-a52640814f54 | -6.1705 | -46.14869 | 2025-08-20 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 368bdb27-8355-36ca-8fbd-582de9fc6ff7 | -3.05192 | -47.01854 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72385240-fb31-347d-8732-ebaf2a13c94f | -6.07008 | -44.12175 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1de0607-8dfb-310b-9aa5-3ef3e5fa8c83 | -3.81953 | -41.56433 | 2025-08-20 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8dc9799-043a-3679-b6d5-422279d9b581 | -5.64055 | -43.38087 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3daf882-eafa-3d69-a497-c3221d9db16e | -5.79095 | -43.61522 | 2025-08-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b0c10d7-17cc-3434-91f0-3fe54b355ec9 | -5.65853 | -43.5094 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a4bfeb5-96aa-3b8a-bc31-a8e8b6e764e7 | -5.87228 | -48.11728 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6bc6dca-845b-3fa1-9284-2ecf53b53c08 | -5.87021 | -48.11622 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 860788b2-b960-30b6-8cc8-1fc1f9c12372 | -4.87712 | -42.71185 | 2025-08-20 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb1ee36-271f-38d5-9877-daf3c2d2c169 | -3.48539 | -51.19081 | 2025-08-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4371e194-dbbd-3882-9f96-cf8101426411 | -4.43103 | -47.75135 | 2025-08-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 925108ed-f3c6-3559-a3b1-bf686bc37803 | -6.6188 | -43.87982 | 2025-08-20 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bf5c0a87-7719-3873-932e-148fbba10553 | -3.65476 | -48.45219 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b06a3020-8a8e-3dba-85ef-ffa9ffd82190 | -4.17603 | -42.02784 | 2025-08-20 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8718b78b-7adc-311c-8052-503c9e9a26ba | -6.0566 | -45.05438 | 2025-08-20 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48a705ff-9254-3edf-b87d-5c874a5dc4b8 | -6.0054 | -42.82742 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e906b11-ad59-3e54-9f4a-1d6f11ea7de8 | -3.51007 | -48.44606 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9177624-4765-3945-960c-292c437a3f07 | -3.35667 | -43.3578 | 2025-08-20 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2986255-92bb-3c76-b791-dc8e3c61a9a2 | -2.90466 | -48.29682 | 2025-08-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c66d9e3b-70f7-3edc-86cf-3cad4642f955 | -4.31071 | -48.09907 | 2025-08-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5158b06e-646a-3b2e-b909-ab5715a04301 | -5.65913 | -43.50523 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 119b34b8-de45-36a4-b438-96dc19a983bb | -2.384 | -47.6642 | 2025-08-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39139c88-644d-3551-a3c7-ff0275cb0249 | -5.87452 | -48.11692 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01cfdc97-4896-3865-8d76-960514919015 | -3.53745 | -53.56165 | 2025-08-20 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db5b5f92-9e81-3ea8-b9de-edf6a4c01879 | -6.86354 | -43.60025 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24a23fd0-b45d-3278-b199-720af4d31ae7 | -5.99364 | -42.82567 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7db60bd-8aab-3497-8a5c-6de6db777859 | -4.64537 | -43.12379 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33b71a01-f58b-3537-a943-98ceb573e3eb | -3.83843 | -47.73672 | 2025-08-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3651b37-e55a-34f2-bcdc-8665a6f90a0a | -5.99984 | -42.82634 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 015d871a-e065-307e-aa17-4bbe8c04d1a7 | -6.17123 | -46.15082 | 2025-08-20 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e58c14b9-bf7f-3547-9a6a-86ee246e8a47 | -6.02537 | -44.35952 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d1b1e7-ae8d-3211-ad2c-5c3afb17168a | -6.44872 | -45.49769 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6c78c65-714b-39a7-a83a-90e6a146f6fc | -2.90874 | -48.29742 | 2025-08-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
