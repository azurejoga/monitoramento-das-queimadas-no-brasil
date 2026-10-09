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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b283783-7273-376d-88d0-fcaccf7a8f3b | -11.58412 | -43.6527 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a660ae2-5219-31cd-ad8c-3e6c8938c6d0 | -7.81865 | -44.56853 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4f8db2c-9d2e-31f5-b352-109afe8402b9 | -11.57874 | -43.69041 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d725ff3-7198-3e63-8fe7-0b06abf95977 | -6.3221 | -55.33137 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 963ec587-f725-314e-b1f8-dcc84fbc9867 | -9.77744 | -44.78297 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2747307-168f-35a4-923e-f0766a3e0b91 | -8.07873 | -45.63717 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7373314b-fb93-3dce-bfa8-7d8c1e72cd66 | -14.1811 | -48.66343 | 2026-10-09 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d189fe19-dcf6-3eda-84bf-41462603bb78 | -11.08091 | -44.08505 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f866633-9b8b-3e6d-a360-19f44358c43c | -13.88627 | -43.82481 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ac2fa0-3060-3b32-b895-6564ade0d3df | -13.15823 | -54.3252 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52ae3517-6dc5-38a8-998b-5b4a22cbff49 | -11.0978 | -45.6569 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f0f483-c410-3ef4-9f44-e39fa832557b | -8.98961 | -45.90864 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5504abdc-ee4a-394b-a754-8c472c8e6b8c | -13.17111 | -54.36143 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d0a1732c-4aaf-36ae-b2bd-4e8d808f6e0b | -11.26651 | -46.2647 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62619c3d-51ee-3cb6-b39d-147278973ed3 | -11.25367 | -45.24834 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce1ebdb8-ce75-33fe-9562-08e5eb1a472d | -8.41103 | -46.94142 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea9cc686-8ab3-3213-a85a-a465d862b3e7 | -11.75981 | -44.95831 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1df4ed21-d800-3147-86fe-37fb66bb4d00 | -8.9688 | -45.15117 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bff19b7-8b6b-3bbb-8cf2-c61110976e2b | -6.48778 | -55.30821 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32cecf73-0aec-3d0d-816d-e238fc9b059e | -5.96878 | -55.34402 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b1eb14-0494-3d88-9452-c1094a7c4976 | -8.73192 | -45.16459 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 230f12cf-b2ed-390a-8b29-07a9344c3625 | -12.00043 | -43.46804 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6001b40c-cf4e-3a57-acba-2e645b5c5287 | -13.11803 | -46.33088 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b4af58-67bb-3fd9-a26f-b6d0814c8d2c | -10.28397 | -43.93478 | 2026-10-09 04:27:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 053a9ce9-f593-3818-bd59-85288f8d53ef | -11.78078 | -45.54111 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f92f2ef-bd32-3dfd-ad5b-f0e7bbf19d00 | -7.5817 | -45.64392 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5632ec70-bbd3-3d76-8e20-cd1f506a5a64 | -11.9984 | -43.4827 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0554d730-086a-3527-821a-608b47d66da5 | -12.22459 | -57.10825 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e6bb7793-6a42-3dc0-9a59-23eaa82d7451 | -8.33948 | -49.12849 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da15f6dc-a979-312a-9763-620a3892712e | -6.00175 | -53.49499 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b027b3f9-7b82-3d7a-9ccb-166e180b166e | -6.01259 | -53.48697 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b30917ab-5068-368c-a61d-126eccdfc4b7 | -11.86801 | -43.55849 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 390aec91-61da-3f36-a922-c926889ac2c5 | -10.73506 | -52.02893 | 2026-10-09 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 976e46a7-da77-3b00-82ab-6d9955aecf90 | -8.29829 | -45.73633 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63abf9d6-f500-3dc8-96c4-d8d10a0d6382 | -6.44419 | -55.04049 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02eba0cd-fb12-3692-9d86-eacd5472806d | -8.72116 | -45.16674 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 304c5a53-72f4-3a65-9c71-d489b0964e90 | -13.16986 | -54.31001 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f8f1d9-ed66-3c5d-8e4a-f91aa7f976a4 | -8.84197 | -45.42967 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7909c44-24f2-3503-9db3-58909225cf36 | -9.43469 | -44.60878 | 2026-10-09 04:27:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3e3ff0e-4710-34bd-ab58-6e1c3cd7b95c | -11.19845 | -45.31071 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ab79625-eff7-3ee9-a9e2-00c2a03262bf | -14.448 | -43.92748 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55b43507-1562-3c93-884b-acdecfdf3164 | -11.18062 | -45.31192 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c452ca7-cb62-3fcc-9a8a-b28c665be937 | -6.38984 | -55.25801 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1a502fd-cbb2-359f-8a48-2faec018abbe | -12.23584 | -57.10081 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9ba17dd4-a60e-31de-b14a-9104f1169c10 | -5.94732 | -55.34328 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c168997-8a59-343c-9722-3f9b105035c8 | -11.19676 | -45.32215 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4624967-3791-38d1-b0fd-15c242f25ccb | -5.95202 | -55.34724 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe561bbb-7988-3641-b099-2b395015f711 | -13.99822 | -48.76442 | 2026-10-09 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1296bacf-49af-37f1-8b67-01681efff1fe | -7.40685 | -44.76564 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f85bb873-d25f-374c-a447-a4c213d31ef5 | -12.24239 | -57.09526 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fba654d8-cc9f-3220-a5a6-d9f68060cf5e | -9.87048 | -44.8644 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24b24c90-e8aa-3adf-9260-3cda3f1af367 | -9.27992 | -47.43588 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1429d1ef-9a76-3502-8332-4ad4554fd476 | -11.76418 | -46.77066 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 390c6f48-cfaa-33b4-bbe8-4999b410e724 | -6.3874 | -56.2253 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62edc7e2-f56b-357c-9888-76ae2c3db07a | -12.21653 | -57.09286 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d382663-3b37-3752-9d10-27754f370104 | -13.03215 | -46.81192 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad25baf-b3a3-3cc0-b257-4ff439c1ee3c | -13.1644 | -54.32523 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6adc66bc-f551-3edd-bb75-ecd8b01e6b26 | -8.9083 | -45.22924 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c827b56-b9a6-3081-a280-e419b71745d0 | -9.28047 | -47.4324 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 953d3c48-7492-3777-8c5f-d61b1c1cf141 | -9.30251 | -47.46441 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55ba039f-aac6-3bd0-bb74-716b5cb30785 | -11.25156 | -46.29561 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e728067e-bfac-30f9-ac81-eae6865b8474 | -11.76222 | -45.48035 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59bd2cc4-cc2f-385a-ba4b-37f548832e47 | -8.52721 | -49.44681 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bdc3abe-275c-3d62-a2c5-a9148ab3aa4b | -11.40041 | -47.585 | 2026-10-09 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4bc65744-303a-3980-98c7-b5232fe8b9f9 | -9.68142 | -48.84996 | 2026-10-09 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ffc593c-0a8b-382c-a2e2-3526ff923ba0 | -10.99199 | -47.80119 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c79a2603-e5af-374e-8dab-3235fe938a09 | -13.63319 | -44.42374 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0364c57f-5c29-38bd-bd9b-17dfe027ac65 | -11.09678 | -47.63253 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69deb127-6955-3194-9e5a-5d7528dc10be | -9.69094 | -58.09385 | 2026-10-09 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f147de58-67ed-3a1b-bfce-7ff775397473 | -11.65942 | -43.69525 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb6f8da5-2fb6-3ff9-97df-a0daadc06cbc | -9.88572 | -50.48988 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0da7c645-47c2-3edd-844f-e0ed13788ba9 | -10.73419 | -52.03386 | 2026-10-09 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13036bd5-eea5-3d86-ab01-6890a9d241a5 | -11.78695 | -46.79985 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e40ee1ec-5fb3-3a49-bdbf-e8d97824c8a9 | -11.26316 | -46.26416 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c769f163-0713-35de-a34e-04f38dce55c1 | -8.7279 | -45.14507 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a99ff905-9eae-350a-9931-07e8beae835a | -11.23061 | -45.23667 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2683dd70-cf86-3a49-8b32-4b91217dfd9d | -7.27896 | -46.17342 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27c8d7b3-bd6b-3d1e-b37c-de15fa7ee5e1 | -9.8699 | -44.86826 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53417d4d-44e4-3794-b369-56404eef42b9 | -6.48613 | -55.2945 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eed8be72-a4eb-3a01-adeb-3b6c3be571db | -6.1268 | -55.7062 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d0bcd19-9226-3702-b3e7-8feda96c0e1c | -9.87784 | -50.49276 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7ddf180-9207-374c-8e52-9839d389d5c5 | -9.56789 | -46.83432 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6de9404c-f07a-3b41-a375-91b4406b37da | -7.58712 | -47.03358 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c841470-458a-367b-ae86-b8b83bdd83af | -9.89482 | -44.79645 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1e4fd4-2730-3964-be07-f9f522ab09f4 | -11.11685 | -47.78954 | 2026-10-09 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53e77982-7d11-3d81-bfc5-2cd682510d42 | -9.45199 | -45.85932 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56d05677-f894-3cc6-9cbc-6850f4c6a5e2 | -11.65696 | -43.68549 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd5bb6ee-5ef9-34e1-9634-3225dce0c082 | -11.79134 | -46.77124 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9b8325b-6e4e-3c6a-8821-cc0ea26176c9 | -8.06512 | -45.64194 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 388f986c-0313-3499-be63-44ca4dfa9359 | -5.95914 | -55.36817 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90d4198c-43cd-33e3-82c9-a22555dd64fe | -11.25659 | -45.18105 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e4d229e-41da-3ca3-8e35-ddc045f0853a | -11.07361 | -44.08397 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57d0a9f6-d005-3617-9e4d-63b030701f9f | -13.38705 | -46.68813 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 401f9899-f287-34c7-a3b7-4eaa7e1f3da4 | -6.42703 | -55.19804 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e11fb95-94c8-3f0b-ad8b-e6851f72c394 | -13.16596 | -54.31683 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d62f0a2-563d-35b4-9cfc-1f9cb22dcfd2 | -11.09086 | -44.04211 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa332597-1f7b-3396-b972-c7057aa7842c | -6.50291 | -55.32024 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca691871-7553-35b5-beb2-21d7cac7c4b7 | -11.22658 | -45.24 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e92c029-f192-3a30-911a-8a563efdb900 | -8.28385 | -45.74139 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d78a4fd6-3d39-3224-97c7-0e1c23d190b9 | -6.11672 | -55.70083 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README101.md)
