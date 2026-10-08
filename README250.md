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

## Dados Diários - Página 250

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7d6a1b7-cb37-3ce4-b572-8d81dff38445 | -3.94436 | -40.71854 | 2026-10-08 15:44:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1d6dc959-51b3-39cf-aef2-87cb716cdcbd | -3.85779 | -44.11331 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9195145b-eee7-3097-bf5c-5672bee6638d | -3.20726 | -44.37817 | 2026-10-08 15:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5f3f68ef-7860-3f6b-ac42-986d54a2134a | -3.90895 | -44.38575 | 2026-10-08 15:44:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 28e61143-05b2-3338-a455-b64f70777070 | -4.13905 | -43.2076 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9b9fb8a-12df-3c8a-8a7f-c8f3c78a989c | -1.67618 | -47.84299 | 2026-10-08 15:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| aba40b46-381d-3d75-9f21-79ca826d2f70 | -3.33086 | -42.92137 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 063de136-55f0-3947-97bd-b033ff40e201 | -3.36747 | -43.38047 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b443c4f6-4d25-3b5b-8c8a-d8f15616dd47 | -3.51861 | -44.31639 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 33e2337c-87aa-3d58-840d-b3a7a03bd9df | -4.38696 | -43.95395 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f0457fd6-8243-33dc-8075-1dc192b364ad | -4.85171 | -44.08955 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a14f1f6d-a23c-3fb2-aea2-ef57dc5e8473 | -4.65485 | -44.85821 | 2026-10-08 15:44:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c8cc52e-bcf3-3566-a7a1-43ffe74da94d | -4.09193 | -44.13197 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5f0ce2be-90ce-3076-95fd-f0cd5fe53260 | -4.7494 | -42.59754 | 2026-10-08 15:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 87a20b3c-97c3-349b-960f-30c308ef3e41 | -4.34092 | -43.15916 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 030dd494-5bed-3d02-bbc6-b4227b600234 | -3.20724 | -42.9557 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36d693db-df1b-3813-bca5-612c39e9c70e | -4.38639 | -43.94999 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6586d358-c9f7-3cb2-8bd7-5036a861d019 | -4.76504 | -42.66813 | 2026-10-08 15:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7c497bc-8410-3376-8324-3f429d45dafe | -3.8532 | -44.12218 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| c80dd79c-a0dc-34c0-8085-1582fdf587bb | -4.50637 | -42.09301 | 2026-10-08 15:44:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b837294-b447-3e27-b934-eeeafde9b019 | -4.09362 | -44.103 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cf7599a6-582b-36f9-8a03-46308f1a8e90 | -1.92804 | -45.23586 | 2026-10-08 15:44:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e1621ab2-b582-3fa3-9ff7-6a7dc8a50074 | -4.19717 | -44.81938 | 2026-10-08 15:44:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa9ffad4-711f-397d-b5e5-3b53bd4e5a12 | -2.88106 | -45.76174 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e7434cb8-534f-3030-949e-2bf98f1d240a | -3.70341 | -40.34356 | 2026-10-08 15:44:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c02860a0-5364-3e6d-b9c1-1e873143813f | -4.3349 | -43.79293 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 39a68953-cb2b-3177-a147-f5e784bccbdd | -3.32993 | -42.91492 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6eb6f36d-0907-3274-b823-910249ac885d | -4.65381 | -44.85569 | 2026-10-08 15:44:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a5476e2-c17c-3046-bfa3-6fa18ad2dfcf | -3.16041 | -43.73409 | 2026-10-08 15:44:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23ac7443-7b62-3b74-bb9b-179d567d5e37 | -4.15387 | -43.19493 | 2026-10-08 15:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ea01f995-2538-396a-9ed2-63644703f0fc | -4.0942 | -44.10701 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a31065fc-997f-3197-9154-49295ceecbdc | -3.36202 | -43.38116 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5e10124d-8edd-3cda-8222-4224e7d6694b | -4.19343 | -38.73772 | 2026-10-08 15:44:00 | NOAA-21 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| e314dea9-1632-387a-99d6-ad62afe33da3 | -4.44352 | -41.47641 | 2026-10-08 15:44:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2da1373b-21f1-3003-a9cc-92c3da7b8fc4 | -3.26672 | -42.95855 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| ff460bc8-26b5-3de1-a18b-194af073f572 | -3.26231 | -42.53709 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a12e2232-59b6-3b83-907b-703b3b6f7c95 | -4.19396 | -38.74127 | 2026-10-08 15:44:00 | NOAA-21 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| d6464948-40d8-3dcf-a295-f9f1bb7b7ff7 | -3.22657 | -40.03327 | 2026-10-08 15:44:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 6aa9e47f-c337-3413-a54b-e058ff079249 | -2.99748 | -43.28106 | 2026-10-08 15:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38c066c5-ab3d-3638-b2da-bd1dc6282b60 | -3.81457 | -44.59838 | 2026-10-08 15:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fae3c5e9-c4a6-3559-8451-9b7e27aad350 | -4.35194 | -43.79079 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b992c7e-3098-3fa0-b911-1433f95961a0 | -3.73206 | -39.52846 | 2026-10-08 15:44:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ce245d17-9eb0-3d1a-91c4-8a25969cdd18 | -3.46771 | -45.11006 | 2026-10-08 15:44:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 129ff36a-2426-31e1-ae43-8a93b4b38359 | -3.76705 | -44.35043 | 2026-10-08 15:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| a63061e2-7f56-33b0-9f1e-82f02f314f2b | -2.92417 | -46.72658 | 2026-10-08 15:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 44baf566-4789-3f67-ba99-a723847c0284 | -3.52461 | -44.31505 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bf1401d9-8708-3fce-b3ca-69bc0d7448d6 | -3.27613 | -44.20495 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5fd70ec1-57e7-345c-812d-b971a165a254 | -5.09225 | -46.19764 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 3950f3fd-0128-3bc3-ad5d-0a8a57069bb5 | -3.70528 | -46.01812 | 2026-10-08 15:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1b8571b4-4054-396f-b751-b37086fc2de4 | -4.09479 | -44.11109 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4081a2fb-6bdb-3a5a-8558-99660be28cce | -3.01833 | -43.34752 | 2026-10-08 15:44:00 | NOAA-21 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2605d672-8fca-30de-9931-7539a3cfe167 | -3.85838 | -44.1174 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 981ea1ed-573a-346f-aa5d-f08b01696b27 | -3.21301 | -42.95823 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e15bbd92-2fdb-3edd-9a7d-f53231509c0c | -4.19494 | -44.46971 | 2026-10-08 15:44:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db984646-3621-3c22-86ed-e0d3ed367db4 | -3.3304 | -42.91814 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfc58c42-554c-354a-883d-568dfb3c38e4 | -3.39702 | -40.24849 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ad4b0264-4224-3d7b-a03b-b0d459ebf990 | -3.26486 | -42.94587 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 564eb540-05cb-33f7-a70c-5c638fcb44fa | -3.5042 | -44.79305 | 2026-10-08 15:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f1b1e2cc-1f1f-3116-8492-d2dd4b6f03ad | -1.52862 | -47.94871 | 2026-10-08 15:44:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8785cc89-9db3-34cd-9355-c381da310c7e | -3.5009 | -44.2727 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ec304227-d6a6-3e2f-89db-498dfb7bf49a | -4.08319 | -44.11226 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 2e15f903-6628-36ba-9544-5379e53432a2 | -3.52983 | -44.31013 | 2026-10-08 15:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff5856f2-9c20-3d2e-836e-7857bf201769 | -3.18129 | -42.59172 | 2026-10-08 15:44:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a93ded84-56f6-362f-b167-a37df67ccab7 | -3.76881 | -44.36275 | 2026-10-08 15:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2505feb7-3415-382e-a977-0b729f1ea172 | -2.97714 | -47.34044 | 2026-10-08 15:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ddab3a1f-9396-37f8-b474-2cf69a1bc9c3 | -2.99749 | -41.42816 | 2026-10-08 15:44:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 092afcd5-a3b6-3eb6-b54d-98f8ee995206 | -3.20773 | -42.95895 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61b0bae2-9572-3a58-bc23-7c3bcc25f389 | -3.29881 | -44.6814 | 2026-10-08 15:44:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74778a12-b4d1-381a-8e07-8c6c6da502b1 | -4.69178 | -42.90266 | 2026-10-08 15:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e6e20e9-a57e-3657-a9ac-010afaed076a | -4.62694 | -42.7551 | 2026-10-08 15:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 46ddd5e5-9bd1-3939-8ddf-2d07e4788f7c | -3.79066 | -41.66853 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 4b0a29c1-d6bd-31e3-b4f8-6a5c82987d79 | -3.78792 | -41.67184 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 08fec3b7-ffa1-3051-8262-f08418fb85f5 | -4.83951 | -43.33749 | 2026-10-08 15:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 47b85113-59ef-37e0-834b-a3684edf1dd1 | -3.1981 | -43.37351 | 2026-10-08 15:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9d40ee65-aa90-305e-973a-7f679eebbdcb | -3.6312 | -44.80769 | 2026-10-08 15:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69161abf-d63b-3ab9-91ab-4ebe8becad90 | -5.13127 | -46.02233 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 3a725073-864c-30ab-aadd-e617cec80363 | -3.3069 | -44.65416 | 2026-10-08 15:44:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86c09ec5-3a3b-31aa-a543-4cedbc8bfac9 | -3.78225 | -41.66722 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 0d359190-4649-3e79-bb71-b31fff016b27 | -3.38773 | -42.21441 | 2026-10-08 15:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e6923988-a778-3f44-a473-3d123ba9bcb7 | -3.3473 | -42.49205 | 2026-10-08 15:44:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef5f9055-19e9-3f51-a7aa-2e4337b53998 | -5.09376 | -46.20821 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 0043a93c-3871-3cd1-a9ea-a96ced81246c | -4.76457 | -42.66488 | 2026-10-08 15:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bf9e8186-2a6f-314a-b131-7b72ffa87c1e | -3.78656 | -41.67462 | 2026-10-08 15:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 6c7a38dd-e6d2-39e4-b51d-6549e31a04e6 | -3.40511 | -42.80658 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d5d8f369-c9ae-39b7-9240-818f98b3e339 | -3.90109 | -44.12836 | 2026-10-08 15:44:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 12085738-830f-3071-93de-53ca5857cdb2 | -3.50714 | -43.83033 | 2026-10-08 15:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a917180c-dd1e-3f8c-874d-b0411fd8455e | -5.13289 | -46.02361 | 2026-10-08 15:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 8a4320a5-6cab-30a5-9863-28822ceffe49 | -4.3812 | -43.95457 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62f2edb9-eb63-35eb-8673-61b7665ca062 | -4.16406 | -43.34384 | 2026-10-08 15:44:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e11b6864-ee1c-3beb-8db2-85a0c73d044f | -3.14969 | -43.04071 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a402ddb5-86cc-37a9-9280-4a56df35d7e2 | -4.59416 | -43.58774 | 2026-10-08 15:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cc3adf94-8519-358c-a05f-89238e4062ec | -3.20684 | -44.37954 | 2026-10-08 15:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c0285c83-148c-31b8-9887-0c0a04a0acb5 | -4.22171 | -42.28371 | 2026-10-08 15:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e0492262-0703-3bc9-a149-6b9035b9f81d | -2.99562 | -41.42666 | 2026-10-08 15:44:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a55b4e15-1bbe-3cf1-9bfe-437217a2641a | -4.35364 | -43.80272 | 2026-10-08 15:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 289c086d-1b64-3f07-aff9-dff2d860773f | -2.87474 | -45.76251 | 2026-10-08 15:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9967ab8c-ba69-3f7a-8873-6eee2ce694ee | -5.093 | -46.2029 | 2026-10-08 15:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 9cd6f591-2f10-3869-9bba-ba6382528358 | -3.70002 | -40.34712 | 2026-10-08 15:44:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| bf3303de-32ba-3ef2-9cec-75b7afa47aba | -3.27294 | -43.03776 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2166d815-5ef6-3fb4-bebc-730a9ad8b09a | -3.20871 | -42.96544 | 2026-10-08 15:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README251.md)
