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
| 0b19d2fc-aaf8-3525-8f5b-3698e17ed768 | -9.33029 | -37.84076 | 2025-03-15 03:55:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 272fb592-0331-3103-9acd-ca8775f16e15 | -12.71453 | -46.29063 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b09b80da-d5a1-338f-a832-cda925b802c2 | -10.58003 | -45.14636 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 954a4943-82c3-3cbd-9497-3e829ee9249b | -10.57152 | -45.14482 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2929483c-1cb9-3852-b538-dce4b346cbda | -12.15724 | -45.48182 | 2025-03-15 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ae41507-c587-372f-9d8b-7866269f52d3 | -6.20402 | -48.05053 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3dc6acd-c23b-3bb4-9428-a306c88d8690 | -9.3342 | -37.8377 | 2025-03-15 03:55:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bf8c695-8a91-3e60-ae10-efb782a0fc46 | -8.44733 | -43.86379 | 2025-03-15 03:55:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 564fe541-3f98-3d5f-9b63-2c1de862e2e6 | -12.15623 | -37.95618 | 2025-03-15 03:55:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2e1836ae-5cf6-3fc7-b1bb-16b6b9c26233 | -9.1435 | -37.67236 | 2025-03-15 03:55:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4d7b4d6-d9fa-3320-ad88-c634db0bbdde | -10.57081 | -45.14883 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2dc94557-159e-37fe-8726-1a5d62df4c00 | -10.57577 | -45.14559 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ac34097e-5776-34d1-aa88-c5dc77fc65e2 | -9.33084 | -37.83717 | 2025-03-15 03:55:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b6677af-13b2-33a5-836e-9f7ab573095f | -11.88253 | -46.94411 | 2025-03-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 569c2036-7132-3658-aa28-3a78c6408ba3 | -12.71964 | -46.28776 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6aacabde-5529-32f5-977e-ea78f3f6e358 | -11.79119 | -46.64738 | 2025-03-15 03:55:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a88e1e8-e6d0-3ec4-9f5a-7ddf1cf8d3b4 | -10.57648 | -45.14161 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2440f0ab-f2a4-3fd1-9ebc-9ff90e34e936 | -9.71679 | -37.64867 | 2025-03-15 03:55:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5ce0660-db46-3012-ae03-cd0b3088f2aa | -6.96856 | -42.7431 | 2025-03-15 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 459cc8d7-712d-3372-ba42-33163dca9537 | -7.05219 | -44.39168 | 2025-03-15 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67da6428-0eca-3237-a844-634dedcce00b | -8.32816 | -39.71012 | 2025-03-15 03:55:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e79b7bd-a1b1-306f-8414-eabd5f7740bb | -8.10859 | -43.13914 | 2025-03-15 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aaeb2ed2-aac5-31c0-84f3-60e89ce8d353 | -10.60404 | -45.10955 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d45f5bd6-f904-3fdd-9d8b-f0ce995977b5 | -14.13339 | -41.69189 | 2025-03-15 03:55:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f11bcc1-ff9f-3ce6-a658-ba6f661f27a1 | -9.09495 | -40.43507 | 2025-03-15 03:55:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 3fc4f6ce-7401-34f7-bec6-3ac3e4633313 | -12.71617 | -46.28866 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a83bb99-537a-379f-890d-59f40d9076e3 | -12.71803 | -46.29643 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a99b36a-3568-3b4a-88c3-949422aee14f | -7.24819 | -44.77208 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 549f99b8-0028-3e43-9cea-e7293d3f2bb0 | -9.82526 | -40.56819 | 2025-03-15 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 783468c1-0111-3652-9caa-4ff66864dbb8 | -7.24332 | -44.77758 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21d10031-cbc2-3b51-b8ba-663af1fda097 | -7.24745 | -44.77629 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02a37f88-7613-3134-baff-f1043a508868 | -6.19418 | -48.04122 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fde3cf3f-da5b-3636-8508-568a90ac3330 | -9.82187 | -40.56763 | 2025-03-15 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 77de516c-ed47-324a-8727-b540a606828e | -12.86098 | -38.36679 | 2025-03-15 03:55:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7f65dcbf-f8e3-3794-b543-b89bed702a31 | -12.71883 | -46.2921 | 2025-03-15 03:55:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f50a10e4-e10a-3a63-b637-7c5f48b11a67 | -7.24261 | -44.78181 | 2025-03-15 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe3b8d9-a834-3e4d-9d4a-beb425024586 | -7.06142 | -44.38928 | 2025-03-15 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e3c141b-fc93-381a-beb4-dfda49ee9064 | -6.2004 | -48.03847 | 2025-03-15 03:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f1e5f30-5646-3bc2-b8e7-244f4315fed7 | -10.60896 | -45.10644 | 2025-03-15 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 13180e77-97ef-32a4-8818-56808a58be07 | -17.91734 | -43.39082 | 2025-03-15 03:57:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47f5d8b4-5e3d-301b-9af5-7e94bb0f4563 | -18.03928 | -39.92595 | 2025-03-15 03:57:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf093f05-7bff-318f-88ea-a9a60bf70ea2 | -17.37755 | -42.48309 | 2025-03-15 03:57:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed7b9e70-8836-3099-9a88-4ff824e869bf | -15.26358 | -51.4704 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22a12980-75c1-3d07-ae2b-34f906716531 | -16.07645 | -53.75034 | 2025-03-15 03:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0f71f9-51bc-36b8-bdd7-a7bf20fb54b9 | -19.70578 | -44.76987 | 2025-03-15 03:57:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 711c28f6-de98-3ca1-946e-1bf474f4769e | -19.83901 | -40.08149 | 2025-03-15 03:57:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a234b3c4-ea5e-326f-b9be-ea763365baed | -20.55354 | -45.97884 | 2025-03-15 03:57:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87ff7191-53a8-3ba3-b338-33b7de7f87ca | -17.09365 | -43.80346 | 2025-03-15 03:57:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72841090-c769-3000-b722-c10aedb38ff2 | -16.07285 | -53.75509 | 2025-03-15 03:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6cc9d88-c700-3e21-9b4b-8557139956c2 | -18.97606 | -46.97002 | 2025-03-15 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4334b794-bebe-3209-b400-6ac456f8b34b | -17.91387 | -43.39012 | 2025-03-15 03:57:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8aa5a030-9859-353c-8e96-0dd0a96c2783 | -15.25929 | -51.47716 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 959080d5-f9b5-34c4-bcad-f4a8a5b4a67c | -20.766 | -45.57518 | 2025-03-15 03:57:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b73a2c1d-bcff-3f0f-978e-b7be708e66e3 | -17.5941 | -43.19962 | 2025-03-15 03:57:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1399ff53-46ba-3c94-8faa-de8e254406c5 | -19.5465 | -39.77277 | 2025-03-15 03:57:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 665ceb22-05fa-3023-ab73-436fb8c192f9 | -19.54317 | -39.77322 | 2025-03-15 03:57:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cd9ffbae-4b85-3aa5-b787-c2e303b837d8 | -20.76343 | -45.57261 | 2025-03-15 03:57:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8df54353-676c-383f-88d2-63d6357bd5e2 | -20.90012 | -43.82 | 2025-03-15 03:57:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 61c8cc79-bc08-3190-bd82-a4e927dac4b2 | -15.2617 | -51.47924 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f79bc10-760b-3aee-acbd-99a6ae905c7e | -20.76483 | -46.76921 | 2025-03-15 03:57:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65f6671a-0360-3a10-abaf-a81ee167e67a | -18.46636 | -39.94077 | 2025-03-15 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72a0ba74-4a57-31f6-a1c9-5e049c98b51e | -19.70514 | -44.77169 | 2025-03-15 03:57:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7e21b603-ca03-3732-888b-3f52c3c0de1c | -20.76713 | -45.5734 | 2025-03-15 03:57:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 228ed078-dbcc-3329-9999-2236830580d2 | -17.3862 | -42.66053 | 2025-03-15 03:57:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42ab3e4a-9902-33d1-be82-b33db3903ad2 | -15.36143 | -39.76212 | 2025-03-15 03:57:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f729847b-c3c7-37e0-a3a7-6ed4db3b6e4b | -20.83979 | -44.85906 | 2025-03-15 03:57:00 | NPP-375D | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 84cfed01-df7f-3f0f-a896-7e1c4d3364c5 | -16.06849 | -53.75474 | 2025-03-15 03:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa6043b9-c6b5-329a-abfe-4cf9da5a8f47 | -15.60436 | -42.33367 | 2025-03-15 03:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dae64ea9-a91c-36e7-8e40-25aa4ade71a6 | -17.77799 | -42.80749 | 2025-03-15 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22c2715e-fa6a-3ad2-83be-c7c5883dd63f | -16.34822 | -43.69778 | 2025-03-15 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fc47665-3790-3b07-b019-64bc789ca0c4 | -16.07511 | -53.75624 | 2025-03-15 03:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40da6691-6df2-3035-aafa-ec1acc1b1db1 | -16.07415 | -53.7492 | 2025-03-15 03:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94e9c436-4eca-3720-b9dc-7da8fd459639 | -17.15203 | -41.40504 | 2025-03-15 03:57:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 168f3a60-ac0b-3af4-8cf5-0696188cd00b | -18.9768 | -46.96605 | 2025-03-15 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5906233e-80f1-3433-b6ef-d09a25ae70cf | -15.26518 | -51.47845 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3be79b3a-ba3b-3c1c-83fb-525459a7ca93 | -17.7814 | -42.80811 | 2025-03-15 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2603ccb4-2c5f-3749-9125-fdc2d700362b | -15.91427 | -43.91284 | 2025-03-15 03:57:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e736ba93-0ea1-385a-9d35-aaaf1ea531bb | -19.83448 | -40.11187 | 2025-03-15 03:57:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2cc25f22-bba2-33b0-b72a-324fbe8254f1 | -15.60779 | -42.33428 | 2025-03-15 03:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0654b858-1535-3031-b90f-6360eac8fe06 | -15.26264 | -51.47481 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09c3a887-56a2-3537-8f23-d77e60cca35c | -15.26609 | -51.47403 | 2025-03-15 03:57:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51828e1b-70ae-3ac3-9a46-dbe1fdc829a6 | -18.97811 | -46.96504 | 2025-03-15 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 390c21ce-c1c0-398f-9ced-0e68b9873256 | -15.68221 | -41.58142 | 2025-03-15 03:57:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b90157c-5be7-3e21-88e7-91d8c70db081 | -20.7638 | -46.76781 | 2025-03-15 03:57:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b7dec98-d187-36ce-a451-332a4c973282 | -17.59577 | -43.19878 | 2025-03-15 03:57:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38a6c795-09cf-323d-9651-bdb7f07649c0 | -18.97735 | -46.96898 | 2025-03-15 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7aa6722-212a-3121-817a-a2b24ebdf6b9 | -17.43818 | -42.62256 | 2025-03-15 03:57:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 330faac8-5179-3d34-8707-dec05a08da2a | -19.54375 | -39.76938 | 2025-03-15 03:57:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 277ce798-b6e6-3c35-af9c-8e1928f18754 | -17.51588 | -40.62754 | 2025-03-15 03:57:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbe7295d-f6c4-3dec-8350-567041410a5d | -19.54707 | -39.76893 | 2025-03-15 03:57:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0d6ca30e-f234-3734-86ef-8bd589a6478a | -22.53946 | -48.81434 | 2025-03-15 04:00:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0ba2a2f-4e4c-39c6-bcbf-a6dc18e40ea1 | -22.92181 | -45.41335 | 2025-03-15 04:00:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c09064a7-2433-3148-8d7b-94161053b65f | -22.78638 | -43.75848 | 2025-03-15 04:00:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f284f841-36b8-360c-b66b-277f33d02a2f | -22.54022 | -48.81219 | 2025-03-15 04:00:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08e799f2-86d5-3a78-882f-be21d4784c06 | -20.99541 | -51.79284 | 2025-03-15 04:00:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e913e75-a38d-3e5d-b0b3-961927042dfb | -23.30725 | -51.34077 | 2025-03-15 04:00:00 | NPP-375D | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2d52e18f-1402-3abc-bb73-a2f9155defa1 | -23.31049 | -51.34205 | 2025-03-15 04:00:00 | NPP-375D | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bbaabac6-fc10-392c-bdc8-c147af86bd70 | -31.71911 | -53.32703 | 2025-03-15 04:02:00 | NPP-375D | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 08490d4c-723c-3f19-ad5f-48ca6db8a58b | -6.20499 | -48.05112 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a069429-c516-3da2-be53-6c7bd73a1897 | -9.25786 | -47.03402 | 2025-03-15 04:17:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
