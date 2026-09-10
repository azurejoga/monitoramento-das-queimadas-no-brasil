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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec9dcb29-b750-3238-a66b-b79d72151eb2 | -11.3316 | -45.78205 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9316be34-adea-3903-a3f4-14fb596e2b9a | -9.78518 | -49.17619 | 2026-09-10 04:27:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0af01003-ca91-354c-8268-7b02e30251b5 | -8.08754 | -54.84513 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb50d142-46a6-3ddb-8ba8-a0fcad0423a2 | -11.85306 | -44.87059 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1a793f9-a91a-3359-9700-26ffa7bc8d53 | -13.43879 | -43.83336 | 2026-09-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a5c1dd1b-93f0-3fb1-9946-42edde14e779 | -15.30024 | -42.52867 | 2026-09-10 04:27:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df46e937-880d-3c31-84ae-29fcb0f0c091 | -10.23701 | -45.18561 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ce1ad62-8fad-3d06-b2dc-a24e741a542a | -11.06793 | -54.51366 | 2026-09-10 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66da3c54-6e24-3110-9220-6b38a07b8c6d | -10.66634 | -46.05829 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 952c4ef9-210c-38d0-adfe-b7ec90878334 | -10.06705 | -45.46701 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44cb8d90-9c5d-3a8e-a19d-0a07d92dca96 | -10.46383 | -44.94979 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 742aff0c-2ad8-3afa-ad89-cabce027c242 | -12.85397 | -44.33704 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 37d41783-de9e-3768-89c0-4ac4695a93c4 | -10.67191 | -46.00179 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 054a95f6-edda-3543-aa4b-66105ddb4817 | -12.20571 | -49.39421 | 2026-09-10 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f86bda1-4b50-355a-97e7-854d08b82cd0 | -11.8508 | -44.86282 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50783edb-1794-32a3-95b4-edd68bf1bf1c | -10.23536 | -45.2178 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d5395f6-2511-3536-b4e2-4c38eb34f6bb | -14.11613 | -44.01336 | 2026-09-10 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddf7d991-3e8a-3da1-9500-54c50fcc0063 | -13.75683 | -49.71088 | 2026-09-10 04:27:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d53c2ddd-eaa5-32fb-b714-edb20fba1a36 | -12.83165 | -44.34522 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aff47e2f-3a5b-3f8c-8c54-74b4acfd52fb | -12.78175 | -44.8128 | 2026-09-10 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e510f8da-dacd-3f1c-9b9d-867465991957 | -10.27435 | -45.20594 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2cbb164-8e83-3a9d-acb7-a267708bdd0b | -10.73388 | -45.91177 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a83ebbd0-7e4d-3b58-b293-c52224b20d6e | -10.06982 | -45.47102 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42353be4-e90a-3370-8572-75bf418c4db5 | -10.72782 | -45.90719 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f7cacf8-1c97-36a6-aaf6-9b0cd31a1d1c | -12.74828 | -48.37173 | 2026-09-10 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b61f604-fed9-3498-8d5f-7ed2557c0a9e | -11.21316 | -49.93821 | 2026-09-10 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0621868-104b-3c4a-939e-7a51bf188346 | -10.66525 | -46.04375 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ea08ddac-6ea5-38f1-9a44-60da5e83c282 | -9.78578 | -47.0528 | 2026-09-10 04:27:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e5387c6-afa3-3298-941e-33621095bb9d | -8.08412 | -54.86349 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36ac717e-570f-36cb-af9e-ce8d45b26bf8 | -10.67412 | -45.9878 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a31d63bf-71fd-3720-b7ef-370f09391026 | -10.23203 | -45.19565 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7007b19a-4d67-37f4-86a9-a5b7a6304a6b | -12.83508 | -44.34577 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a014e2c3-eeaf-3b28-8b5b-0920f40e67ae | -14.521 | -44.90338 | 2026-09-10 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc974d8-d3a7-38f9-aec3-18ff9b7b8e3f | -10.77026 | -45.96063 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d40fb76-9ad6-3a8e-bc8f-65df1db21469 | -10.49695 | -45.28064 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bdaad25-9ea4-3a75-8516-a267a6ec70f7 | -10.67357 | -45.9913 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 901530d8-752b-3553-8024-da7225c742e3 | -10.42076 | -45.11695 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8267c95f-17bd-3333-b1ad-54d0d48cfbd8 | -10.25693 | -45.23205 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 421da97a-2b83-3427-9d55-1b7f104fcdbd | -10.06926 | -45.47451 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fc55a5a-955f-300b-a544-3e58c28dcd2a | -9.68753 | -48.37276 | 2026-09-10 04:27:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c935cdd6-6268-352d-9047-7fef105908fb | -10.26135 | -45.20391 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4c8458e-4a79-3051-a292-84c310f12042 | -11.43381 | -45.15093 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c34015e3-019c-375b-93b0-788e915fe6e8 | -12.83852 | -44.34631 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14c5558d-31c1-3006-973b-2fd588f33a8b | -14.90143 | -44.6785 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee377a77-9df0-3000-aec8-4abd7c1434d6 | -12.8471 | -44.33597 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| dcdf6933-4f5a-3db7-bc20-b8d8025091eb | -10.82617 | -49.45201 | 2026-09-10 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00083adc-77ce-3dc6-b0b7-d2a38d8c809a | -9.78242 | -47.05223 | 2026-09-10 04:27:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1f28b7b-9239-30ba-acdc-ed575ea3d43c | -10.4964 | -45.28415 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6e7ef82-bfe0-3ed9-9458-b75c06993327 | -12.78232 | -44.80912 | 2026-09-10 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62c6df11-ee98-3f6b-b1fc-d0d3b451a9f4 | -10.22708 | -45.24888 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee05a1e5-36e4-3082-862e-98af8ca91664 | -12.84023 | -44.33489 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 57059a0a-d1dd-3ae5-b149-13ad038f4617 | -10.76476 | -45.95264 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8aee8b0d-4b56-3e77-b70e-0d1dea7294f2 | -10.73277 | -45.91876 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c952209b-790f-35df-af5b-d47f9256639a | -12.85454 | -44.33323 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 064a9405-81bc-3550-8a60-a6d740b486da | -12.83623 | -44.33816 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b35162ac-9b69-39f9-b997-9d84639c7d15 | -13.44171 | -43.838 | 2026-09-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9a7cc1c7-15a8-3564-932f-0dc5651386dd | -10.25914 | -45.23961 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f863936e-59e0-35e0-8725-f101b9af0eaa | -12.05629 | -48.16368 | 2026-09-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ece86e7f-719c-3c75-9622-68812236f128 | -10.25638 | -45.25717 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e50d629d-6dee-3b1d-aebb-c07e9998ed22 | -10.23096 | -45.31068 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25557209-a5cd-3e1b-90dd-e96a8b930318 | -12.8534 | -44.34085 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 67b15538-2583-3a8e-a364-1934db8bf8c7 | -10.23314 | -45.1886 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88bb1535-d167-3abe-ada8-5b2a4b650d08 | -12.64196 | -47.08863 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| acba9212-34a0-3151-9979-228720c1d6be | -11.4366 | -45.15501 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58e184ab-cfc8-3cad-aefa-f3049e6b0f51 | -10.75374 | -45.9365 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10f81e2a-a0eb-3ccf-ad54-6ec0f4f56cc3 | -8.08687 | -54.84873 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60486d3f-467b-3ed1-9d10-817aa5097808 | -11.21124 | -46.34851 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b671139-8a76-3583-9f49-c93a0ef7abaf | -10.55215 | -46.07204 | 2026-09-10 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84679f29-08d5-335e-a36c-0c4c7c4884f8 | -12.85282 | -44.34465 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 91ddf7d3-c48f-3ad7-a081-1fdad7b701ba | -12.83566 | -44.34197 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1017083f-dbb8-3cc4-b7c8-4c7daf35502f | -11.48345 | -49.69294 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ac21d6f-9099-3652-9ac0-ff0d83838e77 | -11.43938 | -45.15908 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8288f2ec-2cab-3d9e-ad6d-3e0192b32a84 | -11.85586 | -44.87474 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2659caef-9306-3b7b-9966-2653e3e96d8d | -12.83222 | -44.34142 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 839e6a23-93d7-3858-b8bf-4fc29552f64f | -10.27438 | -45.22757 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57e649d4-aa7f-3e8d-b33f-90d5952d0b39 | -12.85625 | -44.34518 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 3fbd1c49-558e-3281-bbdf-3251d92a028c | -14.91187 | -44.67133 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad1d4871-44ea-39da-8afd-e6975865855e | -11.34466 | -49.25034 | 2026-09-10 04:27:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4f471fc-6df6-354d-ba70-73d77a96d251 | -13.36328 | -41.33832 | 2026-09-10 04:27:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| bb69bd0d-4c70-32fd-a8bb-c97e0ce8a8d9 | -12.65194 | -47.09029 | 2026-09-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9352dd61-7faf-32d2-991f-4fc68b7bb208 | -11.20793 | -46.34797 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 636f19b7-fcc0-33b9-86da-1ae7f5e5b5e8 | -8.08817 | -54.84174 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a249d645-2dcc-3244-8b3e-ff5ad3356148 | -11.33105 | -45.78556 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8ab57e8-eb84-3aad-b5a4-a89c6f3aeda6 | -14.90382 | -44.67802 | 2026-09-10 04:27:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f466590-d7ec-3e0e-a0dd-166485e2757b | -13.81469 | -42.17601 | 2026-09-10 04:27:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 491a1602-b810-34d0-80dc-aed458cdfe82 | -11.8497 | -44.87004 | 2026-09-10 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca9db083-bf04-3a6e-8d2a-23c91e824fe7 | -12.83337 | -44.33381 | 2026-09-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0bf09ee6-5df8-369b-a0bc-a6c2bd4c9762 | -14.85063 | -48.17917 | 2026-09-10 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd5c412-e2a7-34c8-8599-438a44357591 | -10.23314 | -45.21025 | 2026-09-10 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fa45151-4ea2-3c17-b3ce-3112a191fe7c | -10.55543 | -46.0941 | 2026-09-10 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 702ef7b3-a168-37d2-81fc-a6768ba1de02 | -15.08248 | -43.11631 | 2026-09-10 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ae6cc9c-4bc1-3989-9069-ccebe7d2eeb7 | -10.07534 | -45.47906 | 2026-09-10 04:27:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bca51e2-1112-306b-a8b6-1cbf2ad10841 | -12.64757 | -42.29929 | 2026-09-10 04:27:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03ec264c-26e6-31ec-bcc4-1ad4c641d2d6 | -12.20498 | -49.39845 | 2026-09-10 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0618ca36-fac8-310c-9456-07974620c5bb | -10.75978 | -45.96252 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd1c9460-dc10-326d-8356-c0b610ebddb6 | -10.73333 | -45.91526 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61898e41-0720-3373-a61e-eff68f5428a0 | -10.77245 | -45.96816 | 2026-09-10 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 948a715b-d57c-3ca7-800e-0b8b29ab8000 | -16.3578 | -45.06347 | 2026-09-10 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 294a37dc-269c-3c9b-958c-6214b0820e79 | -8.08618 | -54.85243 | 2026-09-10 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f40c12d-fe2d-3c6d-99ff-13afcd8c9f77 | -15.78651 | -43.56512 | 2026-09-10 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README29.md)
