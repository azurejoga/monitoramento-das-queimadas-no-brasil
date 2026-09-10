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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c9de8e-7301-3e20-ad18-def119a761f8 | -14.20302 | -41.60397 | 2026-09-10 04:08:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f4ce612-8d1b-35be-9d6a-bce7e4597e95 | -12.84424 | -44.34807 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c2e671b8-b4c7-3192-9f24-934be901808b | -9.68446 | -43.4781 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6a8bd14-15e9-3771-8633-bd5e063c34d3 | -7.48802 | -45.27542 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e20e05-7e22-3d8a-983c-c9ce907c1ee0 | -7.97849 | -43.97815 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 842bac50-fe35-324d-b0d1-77593b747e3e | -9.77828 | -43.44707 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eb52b5d-9e4a-37a3-a2f8-e0b3babf87c5 | -8.94483 | -44.40355 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 977948db-8596-31b3-ba2a-c895fdb0730b | -12.85759 | -44.34032 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5aa2bb56-8d13-31ed-ac9a-aaa0cb3ac86c | -11.33038 | -45.77728 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da1d75d-c4ba-398f-86e2-a79f1754c68c | -7.97951 | -43.99716 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 136687a1-82bb-3d14-9f04-f68589699de2 | -10.42054 | -45.11896 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd1d2dac-1b8f-3165-a8ca-8c231ce5f7d1 | -13.3624 | -41.33992 | 2026-09-10 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 240bdd02-d533-3905-8f11-2a01d46c5d6c | -10.769 | -45.962 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a89c2c45-faef-30e3-9f2b-5c6acef1a244 | -12.8421 | -44.33746 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 08f6a7f9-632c-3e85-a00b-c814b3fbc593 | -9.7043 | -43.40712 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f910988f-fc17-3939-bb9b-aff43c84cdbf | -7.4933 | -45.27169 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 254666e8-5a05-39d5-a586-13679b56740c | -9.32801 | -45.63287 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b6b1835-07a5-324e-9b37-325cc51d38fc | -8.98398 | -44.97804 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32ccd91d-541d-3e6d-a3ec-1d007a83f521 | -9.69634 | -43.46232 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05060c8d-ffc6-36e5-968b-dfa1809e02f1 | -9.68712 | -43.43867 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1d18924-89bd-3991-af04-55f7aa266dcb | -7.48972 | -43.81483 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 681d7db4-3c09-36df-99ea-3179362fd2de | -7.98044 | -43.98248 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8587c125-41b8-331e-834b-531267caa50f | -12.84297 | -44.33252 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 693d03c0-1cd1-32d3-89f9-f5ac7200d61b | -11.19276 | -42.7893 | 2026-09-10 04:08:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8e295214-7972-338e-b4b0-ae28133fe7bb | -7.5075 | -45.26982 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dcdadcf-cacf-3c91-9999-0148af156bb1 | -13.44416 | -43.83925 | 2026-09-10 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 434c719c-77d1-3129-9543-58054d476b9c | -10.26027 | -45.23893 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 277564f6-3015-3364-8680-b1bcf1e6003f | -7.20573 | -43.62614 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe689d1-0250-3c0d-a874-4c19e092ebeb | -8.24169 | -44.74389 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd70a7c9-5215-3205-b7e9-480db554a656 | -12.85673 | -44.34526 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 2e05f158-1316-3c13-8de8-87b9a93d33b1 | -12.85372 | -44.33959 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c75630fb-3f66-3394-9015-9d8f7038e80c | -12.84685 | -44.33323 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e477f5be-9149-34dc-ad7d-dd2b6f17e91d | -10.73602 | -45.92575 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6968faf1-f0c0-3dc7-a418-0e94d638466c | -13.4404 | -43.8387 | 2026-09-10 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7444667f-09cb-39f9-98eb-30999828f38a | -8.32184 | -45.11219 | 2026-09-10 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b764def-029d-341b-854b-152adca854b8 | -10.27034 | -45.20755 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 074afc96-de39-3af4-abf4-a0d9ddd8d18e | -10.74121 | -45.92238 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6dd9656b-9f76-3a7a-b5f0-09c62b491377 | -9.32271 | -45.63673 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60eb6d0b-f244-3f81-8f91-bb6ff3e791ff | -11.4399 | -45.15599 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b767322c-286d-3f36-b0cc-29047a565b71 | -10.06864 | -45.47538 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcaed516-7285-364e-ab0a-f30f5090092e | -8.94416 | -44.40746 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34f33edf-57b6-3b86-a5a3-725ac1f010e9 | -12.83048 | -44.33536 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 5550ae81-1c39-3687-85e0-f6092ce4e63e | -7.18797 | -43.60846 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49839220-e5e1-3bf6-938e-69b39c99fdc7 | -10.27464 | -45.20813 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 62a76047-c05d-3f1e-bdc8-7033155d8144 | -7.98601 | -43.98347 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ff64b1d-2935-3ab5-aaaa-281e3d62168b | -11.43573 | -45.15525 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72429ebd-0a2a-3590-835e-b77ab28db658 | -10.25479 | -45.23069 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb95f210-9906-3950-be79-e08615198161 | -6.75298 | -45.47768 | 2026-09-10 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cff588f-7ed8-36ca-a0e4-f037f391d665 | -12.17174 | -38.59464 | 2026-09-10 04:08:00 | NPP-375D | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3882164-6d68-3ee2-9804-6c0983b9d49c | -8.31746 | -45.11141 | 2026-09-10 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6338677b-fd22-3004-98bb-a9332aeaf236 | -10.74924 | -45.92874 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a7b0081-ab55-33b2-99f5-1624fff9801a | -12.83736 | -44.3417 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b07444dc-4da4-3031-914a-16284ade8201 | -11.48261 | -42.24294 | 2026-09-10 04:08:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 533de702-72c7-3ac1-b55b-f8d5c8840c7c | -8.24239 | -44.73984 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0c558386-a8a6-3105-ab6b-0c08bf179e03 | -10.07654 | -45.48159 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b6d2675-652f-360a-b904-0aec6cf8073c | -12.8589 | -44.61083 | 2026-09-10 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2484cb25-dcb6-30d6-8724-f56d4577035c | -11.48328 | -42.23893 | 2026-09-10 04:08:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a8ab9633-0117-326d-a4a5-17473bd5da44 | -7.98855 | -43.98424 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd0c5b6d-a05d-367a-921e-d98e5eba624b | -7.19606 | -43.60978 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11167baf-4771-3252-bf84-bea5a98302c3 | -6.71924 | -46.32797 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07fb17c4-936a-33c0-9f70-9fe4f96c2893 | -9.70255 | -43.40405 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 312ac9ab-97d6-32bb-9103-c8c0c2e7bb83 | -7.2045 | -43.6333 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70729c7f-7b5e-33cd-bc7f-7c15529d8822 | -14.20241 | -41.60767 | 2026-09-10 04:08:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c39be7fb-2078-3eb6-ac3b-82dbb04d339d | -8.68713 | -47.98253 | 2026-09-10 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d279d018-b50a-3c6e-af39-7b8ae102a924 | -10.22917 | -45.25113 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f3700b-d5cb-3696-bd07-be78f7817941 | -7.9791 | -43.9745 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6914bd7-3853-3d56-a545-759fcfd0667c | -11.20952 | -46.35063 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b4754b0-21c7-3727-bd3a-647788ad4235 | -8.2353 | -44.75535 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53dd10ca-ac06-37d8-ac7b-4bd2171b8a17 | -11.85273 | -44.86424 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 817604c1-dd5a-38f0-b20a-8b928458e7df | -9.77746 | -43.45189 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 814b26ba-2a09-3249-aeb6-7325271b6bab | -10.75364 | -45.92984 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 532974c9-e029-3f50-8f4e-36d82c860083 | -7.9826 | -43.99419 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2700d43e-3769-3e6d-8f45-e6a5917c49ae | -10.23483 | -45.21876 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b84aae41-df38-3e35-aa0d-14a549974126 | -10.55984 | -46.09949 | 2026-09-10 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 328188c1-fcfb-3c31-874c-14653685878b | -7.98012 | -43.9935 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f572504-7143-33ae-8536-f5e647db24e1 | -12.86284 | -44.61156 | 2026-09-10 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eb16e17-754e-3688-858a-2cb09e671a54 | -9.70511 | -43.4023 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| aa41ed8d-f167-3afc-aae5-6c4a692d93ac | -10.07221 | -45.48066 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a27ba6c-ad96-30fd-9930-d485d9a7a9de | -10.27537 | -45.20406 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3430f426-49d8-328e-852f-9b4416ff5ef9 | -8.68602 | -47.9812 | 2026-09-10 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 694e7c0e-44b5-3672-8bc4-cdb6eb42aa96 | -12.35439 | -48.20239 | 2026-09-10 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5caa3a29-0e05-3b93-b471-cebf04a0e1a4 | -9.71106 | -43.40058 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 233a42aa-8d5c-3a65-95a2-9b40394571dd | -9.7017 | -43.40886 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 67f536bd-06d7-3ad1-bd14-fffd652216d6 | -10.67349 | -45.99174 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b06c0c1-c421-3bf0-b622-7f5a8c84d367 | -10.66644 | -46.05556 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e7961db-6327-352e-8573-b8aecce2b640 | -8.98473 | -44.99942 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f4a698c-c5ee-3aab-a94f-677a1685634f | -7.97788 | -43.9818 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2233117c-fc7d-34aa-9a45-ba06cb84bf29 | -9.33987 | -45.64374 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29c10d29-4a7f-36a4-9889-8a7d08f1b665 | -12.85846 | -44.33539 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5b42ba91-d656-3428-9b64-21b781e693de | -12.63859 | -47.08898 | 2026-09-10 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd435fd2-463a-306d-ac0a-9896b8748118 | -7.97917 | -43.98975 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32be9dba-5a4f-3afa-9238-c683dd8bd7dd | -8.23671 | -44.7472 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c7292292-8a08-3ab8-8d02-2a276c805cbf | -10.26458 | -45.19955 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4eba707-e005-35e5-9b95-bd67ebd89a14 | -10.55027 | -47.11806 | 2026-09-10 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6984b324-f9fa-3633-81ca-a60fc9488fb8 | -10.26249 | -45.20225 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9d3bd30-b860-364f-a200-494983715c02 | -7.4925 | -45.27631 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bd885d6-3810-3c81-970e-02d3163f05f5 | -9.68523 | -43.48037 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7c2ef45-7635-3048-8e74-12759674d87f | -7.75317 | -49.1976 | 2026-09-10 04:08:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b449503-f4b6-3932-8bba-2f662df99725 | -11.33397 | -45.78238 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 792a5818-92c2-352d-b216-a66ac3858ceb | -8.74884 | -47.48808 | 2026-09-10 04:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
