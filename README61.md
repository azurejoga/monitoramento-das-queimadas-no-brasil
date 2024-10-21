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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aae307c6-d456-35ca-96eb-4523429993fd | -12.50193 | -63.2915 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 222afd80-8389-3ed9-8f7d-e6ad27c75384 | -12.50176 | -63.18733 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4e45f10-64f0-32de-b887-b240311f1b4b | -12.50147 | -63.30277 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d24396dc-d4ec-33d4-9f44-c04baf1b2bd5 | -12.50118 | -63.19182 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 321e846b-d0c4-3afa-be50-8a4ada59d735 | -12.50079 | -63.30031 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a946a27e-def8-3657-8427-3da32381e4a1 | -12.49945 | -63.28455 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe283c1d-38c0-3245-b651-fcb9147f4da6 | -12.49885 | -63.28895 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f67fb14-5060-37a8-80c8-a0f8fa1bf1b2 | -12.49881 | -63.18946 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f6acdce-0601-31f9-9e3c-974a954ed310 | -12.49824 | -63.29335 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a390e5f-9e61-3b74-9aeb-7b75e4fdd9af | -12.49807 | -63.28646 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a48fb669-4020-38b4-bc83-0ee34a221f7e | -12.49749 | -63.29087 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1001ea8e-e5b8-3b29-975c-57594220f592 | -12.49501 | -63.28394 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1387cd78-6f0f-3233-8939-927b15ad0d50 | -12.4942 | -63.28142 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf76cedc-2541-3519-9d56-db2d7cea109e | -12.49363 | -63.28584 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d21482a1-f8de-3538-937f-68443b8d97c8 | -12.49057 | -63.28332 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abb53dbd-19be-3e9b-b802-1881650622a6 | -12.48919 | -63.28521 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb8b80f-7190-352d-a392-b49aea368575 | -12.4854 | -63.1876 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27c33cf5-931c-3589-8ad5-78850cefb46b | -12.4848 | -63.19208 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b9ea425-174e-3c54-8d49-e67355ad843b | -12.48239 | -63.20993 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b26565a2-c78d-3993-abda-4f606c7e160f | -12.48094 | -63.18697 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e8627c27-6b66-3a5b-8c58-d3372a026969 | -12.48033 | -63.19145 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fcfb6a29-d96d-3807-8693-e22a099a2c09 | -12.47853 | -63.20486 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 663bfa08-21fa-39f9-9e73-6286dec0b053 | -12.47587 | -63.19083 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1e6f9e1-4f26-384b-a5a1-db0d713aba96 | -12.47527 | -63.1953 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 114c6ba1-c4a9-3634-a907-d77ee9fb7e23 | -12.47314 | -63.24489 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 667cb75b-f08e-3b1f-9480-9986be89244c | -12.46869 | -63.24427 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d79911b8-9e70-39a4-bc91-361e492f8f48 | -12.45794 | -63.05034 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eaff557a-f047-3616-9d66-2529bd447759 | -12.45343 | -63.04973 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 053616ad-d586-3b00-ac8a-63093ba44377 | -12.43777 | -63.02892 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c21ac95-a4ae-3c4c-9312-19f4d0a96176 | -12.43717 | -63.03352 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 736b69fe-e4f4-3973-ae5d-119e0a4294e2 | -12.17823 | -60.68417 | 2024-10-21 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9859eb42-6677-3cc5-a158-36c5eaaf139c | -12.17781 | -60.68745 | 2024-10-21 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaaf28c-8626-386c-895c-a9c184e503c1 | -12.1774 | -60.69072 | 2024-10-21 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 371ea20e-32b6-3dbc-8423-f8ebb933e664 | -12.17329 | -63.32082 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67ed2bb8-a3ca-3151-a4c5-59fcbae21ff8 | -12.00826 | -63.51258 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c205bc47-302d-377b-a568-a457e86baf56 | -12.00769 | -63.51674 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b28e976e-307d-3fdb-91f4-269ef4f1ebae | -12.00392 | -63.51196 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1748a09-90df-3619-8d7d-282e252191ed | -12.00335 | -63.51613 | 2024-10-21 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e73eef-e414-3911-a218-bd325f930e77 | -11.94195 | -63.18198 | 2024-10-21 05:55:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20d6a76f-cccd-38bb-b5ed-fd380da61432 | -11.86851 | -56.88263 | 2024-10-21 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4d18354-9518-3c47-9aef-ccf570e23d41 | -11.86247 | -56.8761 | 2024-10-21 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b13ddea2-25d1-37c0-8bbe-6d48b09286ad | -11.50721 | -60.73137 | 2024-10-21 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98fefe71-274c-3833-a0e8-d44ea09b522b | -11.50679 | -60.73465 | 2024-10-21 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b847139-5bf7-374d-87f7-a74b97528b4a | -10.53291 | -62.61945 | 2024-10-21 05:55:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01743f59-c980-3394-9d8a-d906911f1893 | -10.52903 | -62.61426 | 2024-10-21 05:55:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58775847-1f46-3b69-80bf-5111b2449595 | -10.52839 | -62.61883 | 2024-10-21 05:55:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bc7f2e0-dbe6-3e53-928c-bfe5f741ffe7 | -10.20617 | -64.83632 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 208891b2-886c-39a4-bdca-bfe38dc5e958 | -10.20547 | -64.84119 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6c4d2610-d4fa-3616-a008-f7b46e66d4f7 | -10.2023 | -64.83573 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db636a1b-ad4a-3e35-b79f-7255d02ec44c | -10.20159 | -64.84061 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3f5e3ef-a3e1-359a-b810-1a5584ffe97e | -10.20089 | -64.84548 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88cc2976-fcc9-3b95-8083-c0868ed5d80a | -10.19771 | -64.84001 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9acff732-430d-3f1b-9744-6c5884fdc2c9 | -10.10007 | -64.31267 | 2024-10-21 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50ea074c-ff94-3711-900c-0cb0dd730ea6 | -10.04625 | -68.15761 | 2024-10-21 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b132fc5-eca2-316a-aa2b-f31a9ea59803 | -19.55846 | -56.62216 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bf57a111-743f-3373-a632-b6223b9aec52 | -19.55111 | -56.62149 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 04418506-8cd0-347a-9d12-405348ae4ece | -19.54937 | -56.64499 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2b393ec9-7eac-35f6-b4d7-2d9b8d033d17 | -19.54927 | -56.63942 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9a318e4f-74e3-31e5-a441-8be1c300d902 | -19.54864 | -56.64724 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b240f020-9cd9-3fab-896e-35e60c1c0a8d | -19.54203 | -56.64432 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b3430d58-a285-3163-be94-332e2b0996e7 | -19.54194 | -56.63878 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ba2fa911-5167-3ba4-b233-b285b7736631 | -19.54131 | -56.6466 | 2024-10-21 05:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ccce7ba4-c897-3e10-a35b-569edff643cb | 1.83264 | -50.50092 | 2024-10-21 05:59:00 | AQUA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fdc83cb8-3e63-3c4b-8392-52fff5a6f92a | 1.83073 | -50.48812 | 2024-10-21 05:59:00 | AQUA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 31.1 |
| b08059ea-3bbf-310b-b1fe-ce3ee7227a72 | -4.02849 | -51.0019 | 2024-10-21 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2555fcd5-a32e-3789-889b-7559629f2269 | -3.79585 | -52.31878 | 2024-10-21 05:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b60e84f8-dae2-3391-94cf-5f0ae0d90f9a | -3.76965 | -53.40193 | 2024-10-21 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 124ec13c-7e43-30da-a841-1fcbdada8cf3 | -3.68216 | -53.80259 | 2024-10-21 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9c329b33-8e3c-33e4-9cc2-c3ea7cc86bad | -3.68114 | -51.83362 | 2024-10-21 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9c6b99f9-8433-33f6-a82e-3b98295a58c3 | -3.67936 | -51.84613 | 2024-10-21 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3c05729c-4082-3be5-91bb-423cfd1ed1c0 | -3.60669 | -50.57463 | 2024-10-21 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 061c8d7b-0484-39b4-8555-0c49f6b3e948 | -3.55421 | -50.30222 | 2024-10-21 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8bbf0710-f124-3040-8e12-ff447722eb16 | -3.55081 | -51.37971 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fbdd4a9a-9438-3879-9277-997b6aef9e43 | -3.54714 | -51.37374 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be1e27a0-f0a8-390d-a29e-bab6fa2de904 | -3.54514 | -51.38724 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d49b7fdf-dd39-318c-b02b-c7f07cc3f741 | -3.41935 | -54.27198 | 2024-10-21 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cffb13e6-9ef2-3b8a-a776-64d32c189b6f | -3.38586 | -50.67147 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5aea4800-0a74-33d2-9d32-f4c47dc024d0 | -3.26258 | -53.77916 | 2024-10-21 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e8e03f6d-4f84-3232-9aba-606b19f31480 | -3.22301 | -51.25333 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6e819f74-d777-3df2-8c6d-e34d30c2ab03 | -3.20884 | -50.78626 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 92686886-3bbf-373e-b2b0-335fc5e97af2 | -3.20674 | -50.80087 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5d271805-da98-3380-9b12-d2ea5229cdbd | -3.13309 | -54.27747 | 2024-10-21 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 821830e1-5aaf-3e3c-8a6d-b39e48b95e66 | -3.11775 | -53.11971 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 424332b4-9239-3102-9e96-0efc6cc70c6d | -3.11228 | -54.16513 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a321654-69e7-3ec8-a138-1ca70830d7f4 | -3.1109 | -54.1744 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a4c4dd46-5617-371c-95b9-1c9396db8c41 | -3.11031 | -54.2402 | 2024-10-21 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce9b5ba9-66f0-3068-88e1-b96dba9d2d04 | -3.10953 | -54.18359 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e295674-8ab4-378c-9d75-4e65763bebaf | -3.10824 | -53.11834 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b146d953-e178-39b7-9859-c48c38299432 | -3.10675 | -53.12868 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 264c5676-e2d6-3c6d-bc5c-661dcafd7779 | -3.10323 | -54.16381 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 8950adc7-9bb2-31c2-a0dc-5492ec5ad84f | -3.10184 | -54.17311 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 265.9 |
| 4c4bf9a3-248d-3fc1-a29e-d72877a80b6e | -3.10047 | -54.18235 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| b5b8e91b-8478-3912-a600-ff3596b6abc5 | -3.09556 | -54.15318 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| f4326d10-5e54-3930-9baa-6f0e3d469c81 | -3.09491 | -51.27155 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f9f2f8ca-7e60-3da8-a935-7d5f33e8a444 | -3.09417 | -54.1625 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| f303ab3d-baac-3f1b-8408-a77334beeef5 | -3.09279 | -54.1718 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 343.5 |
| 27ba8dc0-225d-3134-b391-7f3c4d73f9ff | -3.09142 | -54.18106 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ad312709-81b2-332d-8da8-ebee0781c581 | -3.09059 | -51.27774 | 2024-10-21 05:59:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a3e83847-b0c5-3d4b-8fc0-db5132483c80 | -3.08649 | -54.15191 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b884ddd6-81c1-3a0b-8a5a-21cb72cc9159 | -3.08512 | -54.16117 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |


[Clique aqui para ver as próximas entradas](README62.md)
