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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b55d57e-77cf-314a-bd60-89bd65a2ee38 | -3.65772 | -60.62682 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22c1232d-9319-32e8-9d03-54474db5651a | -3.66337 | -60.6238 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47bd8f06-a07c-3394-be6d-9ba0079287a9 | -3.6644 | -60.60634 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5e752eb-f4ce-3b92-8692-b3ee0c6d70f3 | -7.88661 | -72.35834 | 2026-10-07 05:42:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0c49ca86-e1b2-3b41-994e-c88c77092562 | -9.51459 | -54.73986 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b08901c-fe51-30f9-97e0-1199020ae8c5 | -5.67796 | -53.48777 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d95a03e-7f4f-3273-b208-75eca57dc74c | -10.85361 | -50.65766 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb18363e-e127-3c17-8503-79121a104dc3 | -9.33588 | -63.67872 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb857a2e-fce8-3ccc-82e0-a681b0263d51 | -10.84924 | -50.65722 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e3c93c3-161a-36d7-9242-67f55ddb52ac | -8.96905 | -65.44226 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5db8cc5b-29ec-3f70-bb67-83bf6aa9ee94 | -3.66616 | -60.62783 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f766990-98f5-3ec3-8e20-4a54a4c4c7ba | -7.95472 | -71.3401 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e84d95b5-1217-3ede-862b-cf8073851347 | -7.75852 | -70.72977 | 2026-10-07 05:42:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf66241-9a7b-3222-805c-238d54f4c2bb | -8.15462 | -64.07338 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4dd8fe-eecf-3330-b4c2-3371c5c89788 | -10.85513 | -50.66363 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 656b0040-b9ab-3722-bebf-825c7a143d1d | -5.9548 | -55.3483 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 674ea580-67af-33dc-840c-285b36d6365b | -4.75433 | -55.65636 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c37e7be-ff22-30ed-af21-a0fa46b24960 | -9.0707 | -65.48322 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c864c9d-d901-3361-863e-f562f3b3f614 | -9.14111 | -65.41197 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f5f0a6-ecc6-37ed-a438-1dec092f9beb | -4.7693 | -55.67498 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93230935-bdde-3385-a7dc-7222442449e3 | -7.43936 | -73.20066 | 2026-10-07 05:42:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75476f6e-b39e-32ea-8565-6b24b4b6d897 | -4.53929 | -54.98322 | 2026-10-07 05:42:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffcd68c5-8875-397a-9b9d-f3f8c2bffc84 | -5.97883 | -55.38131 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc70e194-aade-3ce9-a403-fdbd4b1c0948 | -6.44357 | -55.02625 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8bc6f28-22bb-3236-bc32-322b9586ee58 | -3.66282 | -60.6273 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a75bc42f-d07c-3614-8374-d5b979ddd24a | -8.83212 | -62.4218 | 2026-10-07 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8102bf7c-13ef-3410-a924-e9c73ef31f9a | -7.18343 | -52.61441 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 544dcecf-c658-335d-b73f-99a4adbae352 | -3.66051 | -60.63084 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53507428-b95c-3f81-942a-1877452d704a | -5.97711 | -55.38357 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b45969f4-4d8f-338c-9e4b-80247a43f983 | -4.54382 | -54.9839 | 2026-10-07 05:42:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4d95edf-d6a9-33ff-b113-e7f734888ac0 | -7.26861 | -72.99735 | 2026-10-07 05:42:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be9635db-632a-3304-893c-a91ba640a08d | -6.00202 | -53.50195 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb0f3cb5-f041-3e87-9ba0-b9cd2e1e4b13 | -6.15488 | -51.73247 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22f8c7a-f439-3750-9af7-28e2af95f853 | -3.67712 | -60.5361 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4fbf26de-88d5-3d33-8701-2044bb076230 | -4.42179 | -55.7536 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7ebd1e5-8240-36de-9903-349427d97a4e | -8.53558 | -55.374 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d6604af-a479-3e03-bb77-af794690665c | -7.881 | -72.35725 | 2026-10-07 05:42:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f64fa8d6-40fa-3f6a-85c7-4fdaa238538d | -3.59641 | -61.62986 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7c7ed0e-863f-3a70-9a0f-9f49f729f8e1 | -8.59995 | -67.04501 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1e90990-e6fd-306e-8235-d60073e3e5ac | -6.40716 | -52.71533 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55412ba2-ed45-36e8-93f3-8b7a18e60ef6 | -5.89548 | -53.63938 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c8c926d-3eec-34e0-8669-f60eeaeff97e | -8.83267 | -62.4183 | 2026-10-07 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e0de5d8-5de7-3ab8-9028-b76646f1893d | -8.27981 | -50.26984 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6597b3b-e187-3dd7-861d-a71c3f2fd5df | -8.28633 | -50.27074 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf49ec38-9c70-3623-8b6a-939edccb4830 | -9.10719 | -65.35263 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf3a9401-e2f1-3315-b9ce-9168b278b118 | -8.0198 | -70.92518 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f2ff49-c27c-3172-b64d-01b3bb31ce5b | -8.82879 | -62.42127 | 2026-10-07 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 463aa73b-7dd5-3c80-a3eb-8a33e16c741d | -8.97261 | -65.44286 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abcf520c-41eb-300a-b440-ebe03706df13 | -9.11074 | -65.35322 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95b8d544-5393-3bdd-a366-ba632baf2a3b | -4.0596 | -59.82869 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 647e7ddc-ddc7-3903-8bd3-754abe49e99b | -4.41747 | -55.75319 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 351d982d-8576-3273-a9e4-94b78fce85ac | -3.89605 | -59.33225 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4df0b290-2fa6-3134-a533-dcee5a5b3315 | -4.57176 | -54.95126 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd7921a4-1fc9-3dfc-9aef-087e55ff971b | -3.58643 | -61.62829 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2131ced-b5be-3bd5-9c4a-278ee555a0dd | -9.05348 | -65.48571 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee366391-4bf8-3c7d-b979-cac96a665d46 | -3.66227 | -60.6308 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd96c450-9413-3813-b5ca-c74349c5a78c | -3.66447 | -60.61679 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66003b98-78c8-3a8b-9bbc-82a9dffa265a | -9.27006 | -50.66403 | 2026-10-07 05:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec770ae9-bb72-3a2a-b5e7-74466e7919c5 | -7.18239 | -52.62187 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71a3520d-f7a2-312d-8dc2-62bbbe9bc4ba | -9.3334 | -63.41613 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f948624-22be-3060-b7ba-5374450d8b1d | -5.99652 | -53.50382 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13d6ffbc-7a2c-37c5-af58-ef03be78c77e | -7.88731 | -72.35452 | 2026-10-07 05:42:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8f33b6f9-a66f-3165-93a8-c14f0fd0812b | -8.54205 | -67.00758 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c6f01b4-a607-33bc-9539-5b8e63bfa5a2 | -4.76244 | -55.66145 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b994fc4-5da4-332b-872e-3e605f07d672 | -10.85297 | -50.66327 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed89b2e2-74c9-30c1-82a8-c5bc82dcba70 | -8.99992 | -65.72206 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cd483a6-02b4-32dd-a35b-e422b1072a57 | -6.14909 | -51.73171 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfddb166-ccb3-3154-a966-a2f3f0dd5641 | -5.68304 | -53.48867 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25efe530-bfec-3cb5-be78-22b3efca9c13 | -7.74858 | -54.94412 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e3562e-b4e8-3739-9f02-a85f02af2b90 | -8.15001 | -64.08017 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48275027-00f9-3e05-8d59-9c1175aa5132 | -10.47775 | -50.4223 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e484473-a730-3383-afa6-70ebd6d33525 | -4.37958 | -59.90369 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d1a473-298d-377b-9e0b-cc0e65c40191 | -8.15121 | -64.07281 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1103f42f-2797-3e36-af84-16fe03400f66 | -6.00714 | -53.50272 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc2a3778-a41e-325d-9f44-94cc582da744 | -10.4878 | -50.42322 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd6dc5d9-18a9-39f6-8135-3ee6988271fb | -7.03157 | -71.7477 | 2026-10-07 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c36787-3e79-37ff-aa65-4c29e615f299 | -8.92747 | -64.30363 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb66ae95-4d01-3c66-b1a9-cccbb941cb27 | -4.06244 | -59.83289 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fac59dd4-2fed-39bc-8939-ac2d5745f244 | -5.97821 | -55.38559 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5992c56c-b3e2-367c-ad2c-b543e3b89507 | -7.95005 | -71.33597 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dc5b328-79cc-3780-890a-1bbabc1e9ce7 | -8.28563 | -50.27623 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f18a8298-eead-3f19-81d1-71f8389d505e | -4.7699 | -55.67092 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0239c97-c386-3d99-9f47-6251ba8ce490 | -3.69277 | -60.54575 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4365e957-89a6-33b3-a1ac-db0c9c01ab7c | -9.10298 | -65.35604 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26b8272c-90f8-3087-aea0-fd3082f1d736 | -3.89663 | -59.32846 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24be0c5a-6234-3ce2-a1b7-663c3444604b | -6.20993 | -52.83593 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daeb173f-54d0-335d-b951-5e69ba3c4585 | -6.95026 | -62.94168 | 2026-10-07 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505a0c96-8f81-354e-ada6-b401c9e3a5f3 | -9.13689 | -65.41542 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52fcb71e-eed8-3e7a-a90c-86ebe970a620 | -8.01999 | -71.0698 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62183124-44ac-39a4-83cb-4eb888e287c3 | -4.7973 | -55.72434 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f1c348-fbae-3439-b7e2-cec110a53758 | -3.97536 | -59.33597 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51c0a6d-0a08-33a2-bf20-e7cde65fd734 | -3.80962 | -60.47005 | 2026-10-07 05:42:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1160247-6de7-3592-aea3-5ba52ee42c23 | -7.89714 | -54.72312 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c9c93d8-5bb0-38fc-a91e-9bfcf6d76b5e | -3.66218 | -60.62034 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445452c0-44c8-31a4-bf70-0daf08bfbae0 | -9.29753 | -63.74571 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab165c11-ffbc-39ed-bcad-faf5fdcd25eb | -8.5991 | -67.04994 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33c5bd30-4c0f-3325-b1e3-47267eefbaae | -6.44424 | -55.02144 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0881bf5a-759b-3165-9ed3-86ad57bd6a61 | -3.67552 | -60.53619 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85f722de-7bec-3490-b77f-f592e1ff189e | -6.21532 | -52.83662 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4b3faac-8b2d-3c43-9b2a-4866db5b23a8 | -9.26933 | -50.66316 | 2026-10-07 05:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README113.md)
