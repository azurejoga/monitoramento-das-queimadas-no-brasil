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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4c74d72-c5f7-3ecd-a2aa-9a9dfa3df529 | -8.4669 | -44.5445 | 2026-09-17 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 5adcab86-3511-3a28-8506-6fe799dcdbea | -12.4343 | -50.79 | 2026-09-17 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 16ab8951-1842-3817-8146-732a7de578e0 | -7.5661 | -42.656 | 2026-09-17 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 51cb45c2-c533-3372-98c4-30a0f3398dbd | -8.6892 | -44.8648 | 2026-09-17 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b27bfc18-6c5a-3274-83df-3f81eaf061e7 | -11.8069 | -58.1759 | 2026-09-17 12:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| b063b170-b7eb-3743-afcd-3205f49820b6 | -7.0349 | -44.6625 | 2026-09-17 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 797512bd-bc9a-3073-a13b-62cda35c8b0c | -10.8305 | -46.1796 | 2026-09-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 1d08102b-95d3-37cf-affd-c75cccf5f0af | -7.3666 | -38.9837 | 2026-09-17 12:30:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 242.7 |
| 8c0eab4c-0552-38a3-b566-78e8cb04f154 | -13.6531 | -45.97 | 2026-09-17 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| aba3c210-a43f-325d-be2a-9cec27b2fc7a | -7.0164 | -44.6413 | 2026-09-17 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 506712d6-7fc3-351e-b75e-7a540d7680cb | -7.0161 | -44.6642 | 2026-09-17 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 370.2 |
| 1ce44cc3-b881-31b1-8d16-0be6ae36b645 | -12.3085 | -47.9539 | 2026-09-17 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 1e87e77f-dc2e-3a53-9c07-a6f78d22ea3f | -10.8308 | -46.1569 | 2026-09-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 745001d7-6964-3d37-ae0a-0092b9adb6da | -8.4666 | -44.5675 | 2026-09-17 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| eac552c2-56b8-3b71-83d8-28e202487a25 | -10.8118 | -46.1594 | 2026-09-17 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 2d463fd1-4fb1-3545-8d9f-db71de541d84 | -7.6402 | -44.3303 | 2026-09-17 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 71149dde-0bef-3842-baeb-1288195a14e2 | -11.8941 | -47.5876 | 2026-09-17 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 46348043-f19c-3904-bb0a-c282ecc67610 | -9.8694 | -48.3814 | 2026-09-17 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 58e7d1cb-a38d-3055-8dd6-636644ec0feb | -10.8189 | -50.8436 | 2026-09-17 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8b7d78d1-aa11-3e0f-9611-cbe9b26d4ebb | -12.5097 | -50.845 | 2026-09-17 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d36d2514-b615-3351-be54-7eec97da58c3 | -9.8319 | -48.3636 | 2026-09-17 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 054ab9ec-b8c3-38b8-88c4-1d485599fb73 | -8.475 | -46.8943 | 2026-09-17 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f6dd0635-cf2a-3fc9-ad52-609d4528c0f0 | -7.6402 | -44.3303 | 2026-09-17 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 6772c85c-74f6-33f8-9ab7-10d50ece72ce | -7.0352 | -44.6396 | 2026-09-17 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e778cc81-c021-3ee6-96a3-cad01a293e2c | -8.475 | -46.8943 | 2026-09-17 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 61dbd190-b95c-3157-a2b5-32160525a03e | -14.1742 | -45.1407 | 2026-09-17 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1a78c1fb-ce3d-37ee-92c1-ce20aef874cd | -10.7999 | -50.8455 | 2026-09-17 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 9d99b763-7936-3a1f-87a0-41adbc9512a5 | -12.5289 | -50.8427 | 2026-09-17 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 95480c63-6fa9-376a-91b0-4c0062864f5b | -12.3085 | -47.9539 | 2026-09-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 0a14ff20-5d54-3328-b929-b10a6e00004b | -9.8697 | -48.3595 | 2026-09-17 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ecd6be8a-ecff-308d-aabd-23fadcb5b11a | -11.8069 | -58.1759 | 2026-09-17 12:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 798c81ef-36dd-36ba-a01a-82e9576cad9b | -11.4853 | -45.7737 | 2026-09-17 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 444e3ab4-191b-37eb-9a1e-ad43760faf87 | -10.8118 | -46.1594 | 2026-09-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| d3d7b123-6ff4-3d1d-8a0a-f8baddec867c | -7.6591 | -44.3284 | 2026-09-17 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 42173e81-55bb-3a67-9f0d-b50c45cdf44a | -12.5094 | -50.8664 | 2026-09-17 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c1138f14-505a-3997-baaa-b03f44027bb9 | -11.3625 | -44.0347 | 2026-09-17 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5098f441-3861-3394-bdb1-eeefa90c0293 | -7.0161 | -44.6642 | 2026-09-17 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 376.4 |
| 69b71031-5148-3726-85f3-8fb7c0983c2b | -12.4333 | -48.4897 | 2026-09-17 12:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c984124a-b1f8-3090-8454-c259ec36acb7 | -9.8319 | -48.3636 | 2026-09-17 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3a1011e3-2352-315f-93b2-e2e5d183ac79 | -12.4343 | -50.79 | 2026-09-17 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 12226195-f923-3f72-99f0-01a944dc098f | -10.8308 | -46.1569 | 2026-09-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| a430fe36-dd36-3853-a7cf-711ece9d5620 | -7.8221 | -44.8632 | 2026-09-17 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| fdc18381-bdca-3321-9fe7-103be8a7baa5 | -9.8694 | -48.3814 | 2026-09-17 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1aa81636-c01b-3037-b575-89985889e160 | -13.6526 | -45.993 | 2026-09-17 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 776a9300-5df8-3185-bda0-e1c16d3081b0 | -10.8189 | -50.8436 | 2026-09-17 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 307a7ffa-b897-3fd5-a472-9569003a1ec1 | -12.6635 | -50.7835 | 2026-09-17 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 891efe3f-dd31-30db-98c5-5da4c249c376 | -8.4669 | -44.5445 | 2026-09-17 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 35ed167f-476a-37b8-ae59-4379cac6668f | -8.6892 | -44.8648 | 2026-09-17 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 77db6645-b2c8-3b1f-9a8c-1d786ca7bc28 | -7.0349 | -44.6625 | 2026-09-17 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 6c324441-2e39-3637-8bb8-1f4de61a6c75 | -7.0164 | -44.6413 | 2026-09-17 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 58d24e10-6d33-387e-a73b-5c64d221056a | -13.6531 | -45.97 | 2026-09-17 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 7e644dcc-c752-3699-ad9e-d80ef11fa70b | -12.5097 | -50.845 | 2026-09-17 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d968830b-93b0-3f4f-868c-ba9349f9041d | -7.8221 | -44.8632 | 2026-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| edf1d164-7198-3d7f-8f2b-dd7c9f433670 | -7.0084 | -43.6497 | 2026-09-17 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 5345f0e7-f247-311d-a949-18d3cf4b6b72 | -10.8305 | -46.1796 | 2026-09-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8337efcd-dc44-3cfa-9d4f-fcc86de01af1 | -6.9896 | -43.6514 | 2026-09-17 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 63dbe61e-ecb1-3a88-9a57-9a6c250f9405 | -7.8033 | -44.8651 | 2026-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| db7f814b-3fc5-3f22-956b-d61cf2cb53ce | -11.8941 | -47.5876 | 2026-09-17 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d24012da-66ea-317f-99ef-c0e7aa873111 | -12.3085 | -47.9539 | 2026-09-17 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f8f767b0-2997-330a-a63c-914231484d67 | -10.8189 | -50.8436 | 2026-09-17 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 207.6 |
| a0e65d64-49a0-3683-b16d-6bc174f3e86e | -12.4333 | -48.4897 | 2026-09-17 12:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 97eeea73-e09b-31ef-907e-c785180222bd | -7.0164 | -44.6413 | 2026-09-17 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| d523d924-b979-3b1c-b218-e9a71dce7a06 | -9.852 | -46.9046 | 2026-09-17 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 5c967c6d-5869-32cb-a15b-cb0dc20cac6b | -9.8694 | -48.3814 | 2026-09-17 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8ebcf54e-2408-36c1-87cf-ef95b5dfa57c | -10.8118 | -46.1594 | 2026-09-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 83459a95-1762-33e6-985b-af21442c24d8 | -12.3568 | -50.8634 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 28bf2c1c-35f1-3ee5-9f2b-c48af4f8d4df | -10.8757 | -50.8376 | 2026-09-17 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6de1a625-ae65-3f00-b12d-7062c762935a | -13.6531 | -45.97 | 2026-09-17 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0b14af9e-0889-3ea4-a47e-07a7d35c72c5 | -10.8308 | -46.1569 | 2026-09-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 267.9 |
| dc8f8050-cd4e-3e0b-a763-6fdcff2a8d52 | -12.5094 | -50.8664 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e65e2bae-c48c-3618-af97-6a9ee2dcf7dd | -7.0161 | -44.6642 | 2026-09-17 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 314.7 |
| 82ebcaa4-a20c-362b-ba12-ab3a1ec27988 | -8.8459 | -45.8713 | 2026-09-17 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| a6447c8d-1a27-30d9-9996-bb96e76ddd7b | -6.9898 | -43.6281 | 2026-09-17 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9e5a642f-2668-396d-8f81-7d92d418bc49 | -7.0349 | -44.6625 | 2026-09-17 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 995a5bd9-000a-3eb4-b55d-7d1cc8f7afc3 | -14.1552 | -45.1208 | 2026-09-17 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ff060fd6-1f39-39dd-ba79-d3f3f2a6e259 | -10.8192 | -50.8223 | 2026-09-17 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f109f726-7ec2-3e0a-bee0-770835beb811 | -7.3938 | -44.492 | 2026-09-17 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7bc8d12c-c141-3a02-b590-91ddc623155d | -9.8517 | -46.9269 | 2026-09-17 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 2e9eda29-fcce-3fcd-a041-619145a655cc | -9.8319 | -48.3636 | 2026-09-17 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f8cf2eda-4dbc-3097-b55f-fc77a02c6d91 | -14.1547 | -45.1442 | 2026-09-17 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| a08597e2-75dc-3922-b54a-7e65d923f868 | -8.6892 | -44.8648 | 2026-09-17 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5bde6068-b264-31cf-817a-0d0169ca7fd6 | -10.7999 | -50.8455 | 2026-09-17 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 290.8 |
| f34cbd7d-ffee-357c-a4fc-9d56c0ddf8eb | -12.4343 | -50.79 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e038ff5e-d000-34c5-8c02-6a865e39177b | -12.3964 | -50.7731 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6b959c69-1843-35dd-b173-16dd3bffa817 | -10.8312 | -46.1342 | 2026-09-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a8179d93-ffbe-33e2-854a-056b80fee542 | -8.8647 | -45.8693 | 2026-09-17 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| b5981de9-a23b-3102-951f-d1b4d58610c9 | -7.3669 | -38.9584 | 2026-09-17 12:50:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 202.1 |
| ab61141a-2bb0-38ea-b267-9fc1c8dd5470 | -7.0352 | -44.6396 | 2026-09-17 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| aeebb071-266b-3f84-8689-c6ed0327f685 | -11.8069 | -58.1759 | 2026-09-17 12:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 9630fc8b-582f-3db3-b6ec-2e50406b6bb9 | -12.6635 | -50.7835 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 02b460de-dbee-39a6-91d3-8713c7281a58 | -9.8697 | -48.3595 | 2026-09-17 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e6f7e18a-8b7c-3a3d-a584-58db6c29e484 | -12.6816 | -50.8455 | 2026-09-17 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| bb33b026-c0ff-3869-9be6-0c17a5e45335 | -12.7243 | -48.2734 | 2026-09-17 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| be35d2cf-5d74-3b46-a539-40732edef369 | -8.8647 | -45.8693 | 2026-09-17 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 71ac2021-9a13-3f52-b821-b65c18c0c022 | -9.8697 | -48.3595 | 2026-09-17 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 54e23df9-6e3f-305c-8929-65efa160e245 | -11.3467 | -47.2361 | 2026-09-17 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 2befb024-9d16-3510-8bbf-0c0f1a1dd400 | -12.5094 | -50.8664 | 2026-09-17 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| adea25d9-a968-3725-b535-bb76ff3fa4cc | -12.3568 | -50.8634 | 2026-09-17 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b9ca14d0-e122-3c33-97dd-d02d3777dfe6 | -10.8308 | -46.1569 | 2026-09-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 2c8558ff-e31f-3565-a5f8-cca3aea241ed | -9.8319 | -48.3636 | 2026-09-17 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |


[Clique aqui para ver as próximas entradas](README88.md)
