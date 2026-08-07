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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ec7661f-c6fb-32a4-906f-9c4301c5a978 | -13.77261 | -47.1798 | 2026-08-07 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e635336-141c-37be-a51f-6972b8b1230a | -11.28619 | -45.46101 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01b12927-cf24-3323-b647-f50edca143c9 | -14.27509 | -45.29636 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6536894e-708b-3550-8bd8-dad75340b454 | -11.13886 | -44.46768 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c832348e-0c3c-3397-bd3d-b249cfdaf991 | -16.17275 | -47.88441 | 2026-08-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 260fa376-21fa-3646-883f-3cec7f89b627 | -14.44389 | -53.33904 | 2026-08-07 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baac557b-6486-3e8c-a5e3-270d93b1eb49 | -13.54362 | -43.70217 | 2026-08-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24712a1-284f-3fa1-9dc3-f40c760d40d6 | -12.58912 | -46.90518 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 189709b3-d069-312b-bc8a-24d30fc8c1c8 | -11.14305 | -54.90708 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bb2c7aa-e1ef-35ae-8a14-6b47eb1042f0 | -11.13986 | -44.4832 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ed0fcc46-0539-36c0-a505-4e6ff5baee49 | -12.74302 | -44.45459 | 2026-08-07 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abedc44-85c3-3a93-b758-823039f43582 | -11.13806 | -44.49441 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e659872a-9ef5-305f-ad4b-7857cfc5e3a3 | -11.46401 | -44.56676 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67cd1fb2-2e23-37c1-89ce-bf233f7fd2eb | -14.73549 | -47.13372 | 2026-08-07 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb06f2a4-4241-3850-b558-5337b58bb268 | -14.42028 | -45.6758 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2811283-be14-30af-a865-2480c7495f41 | -17.121 | -43.29864 | 2026-08-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af853675-fb69-372e-b239-6acb18fd6cb2 | -17.46065 | -47.15423 | 2026-08-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0158159a-6a86-3541-be7e-cddbd120ef68 | -16.69278 | -51.36831 | 2026-08-07 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e6e6fb8-e159-3351-b4a5-77d1b2f5dd3c | -12.55903 | -46.94636 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88d52b10-6bc5-3927-b2c9-0de4070f5268 | -11.14207 | -44.49123 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b6da7a-0351-327f-9122-6fc343cb794d | -11.32339 | -45.21234 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 014fd19c-66c2-3181-b7f1-2d07cc083180 | -15.11236 | -53.59587 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29cf0af7-aeb4-340b-ae96-d04368163501 | -13.82623 | -53.72258 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31a0856a-860b-3647-a20a-b850da26da3e | -14.42221 | -45.6641 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c80a67e3-a84e-3d7a-93cf-3b652e476bc0 | -13.54418 | -43.69862 | 2026-08-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9796d41c-a6e4-393a-81d0-3f7104f0c0f7 | -14.35095 | -54.90869 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2035a7e2-7eaa-3fe0-b7c8-4f6a8fb55c40 | -11.28266 | -45.4604 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be6d24d0-6999-356d-af78-dea1d7679108 | -17.58855 | -41.30224 | 2026-08-07 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| f9f79ca4-662a-3ace-8010-c1ac817c0325 | -11.12149 | -54.90631 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 519a73cc-4334-3e77-a894-9c1cae8af791 | -11.18451 | -54.86533 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1e122bd-c904-3810-854e-79289b817f4c | -11.47362 | -44.57219 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc349992-78ba-3071-8d20-cf997a750265 | -11.14728 | -44.48059 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 43362f60-8459-394f-8586-4ce26042793c | -13.93584 | -47.36082 | 2026-08-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f85027-e587-3110-85a5-bb60b07ba5a8 | -11.13149 | -54.89875 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 140a0fd2-dee1-3f3c-9532-e032786527d9 | -14.4231 | -45.68029 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a81d5a1a-08dc-35c0-a63c-65bd1667931a | -14.42093 | -45.67189 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2498f16-cbc7-323f-8625-f34cb27503c0 | -11.46403 | -44.56334 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 553c6a63-4c4f-3e26-ad39-a98267361f70 | -12.57492 | -46.89809 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f08787ad-eb5e-3211-952a-b6c940a0484f | -13.68981 | -51.97462 | 2026-08-07 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1864f5b6-8339-36f8-a108-2af575a83e1b | -14.27571 | -45.29256 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf2b0d99-cf1b-33e3-825f-920b7415dc33 | -11.13421 | -54.90899 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 697dcbc6-f3f4-3d04-928f-9623ab65c5e2 | -16.67258 | -49.14456 | 2026-08-07 04:10:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0249921-821d-38ad-931d-8ba5c87eb17f | -11.4166 | -47.26145 | 2026-08-07 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8dd50f4-5ca8-343f-a1d2-22f7a5698445 | -12.55448 | -46.95037 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61b38c2d-9f66-3b4e-9301-0f5ac8b20178 | -13.82136 | -53.71747 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06d5cdd2-b48c-39d7-abe2-199a15a180cd | -14.43256 | -45.6659 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e221ec7-31f9-34e5-b6e0-a45c928a1728 | -11.79265 | -40.92539 | 2026-08-07 04:10:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f771f224-4551-3e72-b48b-9b193219cdfe | -11.15009 | -44.48487 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a66fad23-5329-3a5e-9c92-91d2682e3404 | -15.90138 | -48.01128 | 2026-08-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a367c175-338d-3e11-8bdb-d17bd7eb0d11 | -14.35037 | -54.91837 | 2026-08-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71e81d2c-c379-3386-9d7a-da9334d3f8ae | -17.45897 | -47.15775 | 2026-08-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 677f1d88-2dae-387f-b61b-344631e372a1 | -15.59193 | -43.73866 | 2026-08-07 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91fdc52e-c0ad-3cdb-8ca1-bf7e77057ffa | -12.5944 | -46.90394 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f2b9160-256f-3343-bb76-10b557e28eaf | -15.09409 | -52.76542 | 2026-08-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eee75116-b5f7-3273-add2-e9b0b01a251d | -11.15515 | -44.47781 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 178861e5-e436-307f-9daf-bc8f26ac67ed | -11.13361 | -54.88827 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b350e46-8403-381d-bc0d-ba7a0cc8d11d | -11.12931 | -54.90947 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f14a8313-c1d2-3b05-a590-00d8f4554774 | -13.6236 | -54.67172 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c688d53-b402-32ac-8eb5-7f36c27cf2b0 | -11.13255 | -54.89348 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd8c420f-9fc6-3b5d-9ab2-16685de7d97c | -11.13866 | -44.49068 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5074c09-8ec7-3879-902d-676cf40c8d1e | -16.73487 | -43.02283 | 2026-08-07 04:10:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fd0c375a-931e-3148-a3eb-2d9c2daf1cf4 | -13.62444 | -54.67493 | 2026-08-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85399b56-2add-33b5-aa36-82c545c24cdd | -11.4696 | -44.57536 | 2026-08-07 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a33e191-fd53-39f3-be6f-b3d5b28dcd0b | -16.17192 | -47.88912 | 2026-08-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b37773d-1ef1-357a-b4e8-9ca141e6af47 | -17.99601 | -45.87749 | 2026-08-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0072ed9b-4eaf-31ce-9f9d-d8a3b63848f5 | -15.08087 | -53.55444 | 2026-08-07 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a324d88-2fbf-3d45-9712-c6ff84af32a8 | -12.48598 | -50.36912 | 2026-08-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0309f75-9370-38dd-af90-d32ad4db2f43 | -11.14567 | -44.46883 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c61e9e1-8cf4-34cd-bb5d-9bac02677357 | -14.27292 | -45.28819 | 2026-08-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba0d9d31-8e96-38f6-9b1d-e67e7c242b71 | -14.44383 | -53.34243 | 2026-08-07 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a20db818-24b7-300c-8224-acc9d2c4f675 | -12.87432 | -52.81953 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f50a2fa2-a103-3300-88a0-e54d05032c9b | -14.42783 | -45.67308 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dabffa0d-adcf-368e-a637-8054657cc8dc | -14.4263 | -45.66082 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73d471e1-600b-3b99-8072-59200f140b04 | -15.8975 | -48.00798 | 2026-08-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 427f5727-00a6-3b8d-8c05-75318ae4bcd4 | -11.13314 | -54.91449 | 2026-08-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 198d0980-4fca-3b42-9dc2-7a1bd197e215 | -11.09001 | -47.80075 | 2026-08-07 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac2d4e73-85ab-3c65-b641-181b40b86823 | -12.86889 | -52.81845 | 2026-08-07 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f939e804-bbb1-3ab9-8550-fd6034b3c687 | -11.086 | -47.79995 | 2026-08-07 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c817b5d2-2c1b-3585-a172-52613f1459de | -14.42374 | -45.67639 | 2026-08-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ded097a3-ce1b-3530-af66-d8f85a492a3e | -11.30334 | -44.81993 | 2026-08-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32783c11-7908-3104-a96c-70ff8b27c792 | -12.55281 | -46.96022 | 2026-08-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33297df8-1898-3834-b13b-4c11055ed76d | -22.90435 | -43.46552 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74621280-ae1d-3351-bccf-b4ccd99071ad | -20.90301 | -40.79613 | 2026-08-07 04:12:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 170f006a-36b1-3585-8b8b-623aebdbe537 | -22.91539 | -43.31454 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0ff365cd-2228-3636-b982-61822f3d1550 | -22.90337 | -44.915 | 2026-08-07 04:12:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bf3502f-1740-34ac-8d65-4a2c25714176 | -18.14631 | -47.97968 | 2026-08-07 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f955db09-9f65-3330-8cfd-135bf0c577ca | -23.55092 | -47.17643 | 2026-08-07 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71ace794-e24c-34d1-b050-abca5de17294 | -22.71592 | -43.82642 | 2026-08-07 04:12:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c11575ae-de11-34d7-bc48-b72e4d437f01 | -19.50389 | -45.2849 | 2026-08-07 04:12:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dbeb427-5103-315a-85f1-459d9e2e7591 | -19.3921 | -40.26346 | 2026-08-07 04:12:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4d953f2-70aa-3e68-897f-b0a59a44a94e | -20.56914 | -42.20984 | 2026-08-07 04:12:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b5d5c341-22a7-305d-956c-4d5770381c80 | -20.05339 | -41.97408 | 2026-08-07 04:12:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e0581fc2-c4d1-30ab-b11a-833ee92619e5 | -20.24829 | -46.90409 | 2026-08-07 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f885852-4efc-376d-86a6-cd8526db6e38 | -20.39132 | -49.31239 | 2026-08-07 04:12:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f8b10f69-acff-3613-aa0c-99040016c35e | -22.71317 | -43.70135 | 2026-08-07 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b7af7166-7a6e-3901-a6df-0f6adbfc12ef | -18.00749 | -47.14154 | 2026-08-07 04:12:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d3a50e6-925f-3228-be36-c6c879d27ca5 | -22.45828 | -43.13363 | 2026-08-07 04:12:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52d8ef43-23cc-39ad-a22f-d20020da9e37 | -19.71127 | -48.13208 | 2026-08-07 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f8cf033d-8418-3922-8411-c936ab5e9ea1 | -18.00751 | -47.14275 | 2026-08-07 04:12:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aadbbc5-4b57-320b-bb06-4f442a20d3d6 | -18.15283 | -47.98575 | 2026-08-07 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README12.md)
