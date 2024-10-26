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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05146bc0-ebd0-3b21-9d77-944aa9cf1bfb | -1.74524 | -52.32413 | 2024-10-26 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cec27d2c-d63c-30bc-9ac2-d9156f0527e5 | -1.69816 | -52.71301 | 2024-10-26 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6b0889f7-310d-3b1e-bdd6-1541c9e085bb | -1.65126 | -53.24578 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f36616ad-b0b7-3ae2-ada4-b6fdf6110b48 | -1.59641 | -53.30811 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 62eda473-e14c-310d-aa11-ae6059bbf057 | -1.5786 | -53.31062 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e0fe7044-dbed-3180-99b4-8ad4aed61042 | -1.53913 | -47.29767 | 2024-10-26 01:09:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 1773c276-8ead-3273-a034-a63f7048faec | -1.5369 | -47.28183 | 2024-10-26 01:09:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 447d00d5-70c2-3b5e-a37e-4eac60bd4c16 | -1.41071 | -52.10284 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0d627b3-1192-3422-a747-5ce5644c48b7 | -1.38335 | -55.84904 | 2024-10-26 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 90719fc9-70bd-3508-a0c2-d213cdb22484 | -1.38177 | -55.83746 | 2024-10-26 01:09:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c55293ee-acc4-3122-99b2-782bab2108ac | -1.35518 | -55.49559 | 2024-10-26 01:09:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 618cc636-8ac9-3e7b-86b0-e5e1a575aba3 | -1.35467 | -54.61776 | 2024-10-26 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 98d6c2d0-72b5-3187-8176-1d32110cf9a0 | -1.35331 | -54.60798 | 2024-10-26 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 46b00f5e-3263-3dd6-9395-555a31e03aa1 | -1.34534 | -54.61903 | 2024-10-26 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fe72270b-7168-34ea-8067-cdc5c7683984 | -1.34397 | -54.60916 | 2024-10-26 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 73b12790-2b3c-3273-b3c9-7f2cb9c4d86b | -1.26995 | -52.94716 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ccd5dcb5-eaf0-3927-8ce9-0c3370d31aba | -1.186 | -53.67097 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5720e7a7-2a8c-369a-8e14-ec1e8c2dcbcb | -1.18475 | -53.66196 | 2024-10-26 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 43acbce0-edcd-301c-9bec-7edaae5765eb | -1.18091 | -53.90147 | 2024-10-26 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1977346a-a2f5-355e-84d1-511e3cbc25bc | -1.08245 | -53.6549 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 38f89d9d-517d-3641-8ddc-062f3b72c8cc | -1.08121 | -53.64592 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 08e5dee1-fb95-3647-8135-6531aff3c917 | -1.07475 | -53.66523 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dcc25062-ff6e-3915-b800-d9fccd297b73 | -1.0735 | -53.65618 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8992dd6e-9e4f-306c-94de-c28ab1c25360 | -1.06583 | -53.67238 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ce165b32-663c-35d9-b2c1-2bcccab98f99 | -1.06455 | -53.66328 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8b6ffa2b-ccc7-3abe-9a2f-6676790444f0 | -1.05966 | -47.6503 | 2024-10-26 01:09:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3cad7bf2-3e96-3f66-bd6f-7af482f1e32d | -1.05952 | -47.64144 | 2024-10-26 01:09:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 629ad9e5-bbf4-308a-a715-4ae867691063 | -1.05746 | -47.63521 | 2024-10-26 01:09:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 632042b9-d835-3537-954f-9c28bb9eb7e1 | -1.03546 | -53.52063 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af52c3b1-c879-3a82-ab2e-ceab6eb71ac2 | -1.0342 | -53.51165 | 2024-10-26 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dae12c7-4508-3080-b5a0-14099c2de67d | -1.01898 | -48.08044 | 2024-10-26 01:09:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b0c6067b-473b-31dc-8d03-dfb37657db70 | -1.01692 | -48.06633 | 2024-10-26 01:09:00 | TERRA_M-M | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 147fdad5-da87-36bd-afb3-071ace139ccc | -1.01584 | -48.07197 | 2024-10-26 01:09:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 57dc3363-a187-3a81-8ae3-9820bb92475c | -0.88746 | -47.89146 | 2024-10-26 01:09:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8a619d8c-312e-35f9-8d09-e57484cede38 | -4.54207 | -50.97259 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4b851e0-107c-3d29-9f29-558543d0383a | -4.48912 | -42.91041 | 2024-10-26 01:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 0fb7355c-7e51-38f7-82ce-37a50b6e7c92 | -4.48329 | -42.90586 | 2024-10-26 01:09:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 16a3b93b-6b24-30c6-9890-d65bd50682e1 | -3.48341 | -43.32665 | 2024-10-26 01:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7444f826-2a7c-3f53-ad8a-420190541600 | -3.47237 | -43.33368 | 2024-10-26 01:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| db0fae92-904b-3f48-ba5c-25505bb1d1c0 | -3.46793 | -43.32892 | 2024-10-26 01:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 3402246a-747e-3a13-aa3b-dc11f72856be | -3.4679 | -43.30305 | 2024-10-26 01:09:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b9834ac7-1ec6-3ece-9587-b2461747e083 | 3.64277 | -51.28499 | 2024-10-26 01:09:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 021c9cc6-cbbe-3f08-ae34-8f453e61c7ab | 3.64138 | -51.29512 | 2024-10-26 01:09:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3ab060bf-1d6a-33e8-92fa-2384180bcf39 | 3.3846 | -51.29209 | 2024-10-26 01:09:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4703508-cb71-3e2d-8caa-e81a43e4a962 | 2.79047 | -50.92794 | 2024-10-26 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3e2d0571-ca75-33b1-be4a-5790533e3a0f | 2.78903 | -50.93827 | 2024-10-26 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0e6cd5ac-3477-3e52-996f-a45cd318b832 | 2.31329 | -50.76703 | 2024-10-26 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b9ae4e1-db9e-3bef-9451-1653627e7fb0 | 2.30373 | -50.76569 | 2024-10-26 01:09:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f9409ed-2042-3ed7-859b-1443a2c57ce6 | 1.79415 | -50.45338 | 2024-10-26 01:09:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4808bc1-7a66-3e36-a4b5-dc86e02e3faa | 1.79269 | -50.46407 | 2024-10-26 01:09:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f7400ee2-7997-3f90-bc94-c912271a2ae0 | 1.57071 | -55.64391 | 2024-10-26 01:09:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a9b4f30-67d9-3724-85ad-10ab6b25a7c5 | 1.33075 | -50.89532 | 2024-10-26 01:09:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fad33fcf-827b-3b61-a2da-21839977ab03 | 0.6189 | -51.89671 | 2024-10-26 01:09:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ef2a4d1d-2165-37d0-926c-f3e307fa3576 | 0.31232 | -50.99535 | 2024-10-26 01:09:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27cbff7a-400a-3771-8c03-7e2420fd47af | -6.437 | -49.89747 | 2024-10-26 01:09:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b5c94a73-9254-3c9b-bc72-9136a369eb40 | -6.40747 | -50.79619 | 2024-10-26 01:09:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7fdb30e-4134-389f-b08e-8e6e6c270083 | -6.28489 | -47.82798 | 2024-10-26 01:09:00 | TERRA_M-M | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bfcfbcf8-9abf-3bd7-8884-7bb114ce391f | -6.22591 | -50.8802 | 2024-10-26 01:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0395b31e-54a9-326f-b2ab-b010b5a0d10c | -6.22465 | -50.87128 | 2024-10-26 01:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| daa1d2a2-2b7e-31cc-8cae-1a68ada9db89 | -6.19354 | -50.85419 | 2024-10-26 01:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2aa1a763-1042-3c0e-918b-8a23e0200df8 | -6.18466 | -50.85546 | 2024-10-26 01:09:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 413fc9e1-63f2-3cf2-8acf-f0c930e780af | -5.84769 | -47.28518 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| df51c617-d6c5-3fd3-b58e-57f05f0fbd57 | -5.84155 | -46.24225 | 2024-10-26 01:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23aaa157-7171-3bff-b3c7-f610c4965cf0 | -5.83363 | -47.18944 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6586906-15d1-3a89-9f93-8ae7fdf5fbdd | -5.75595 | -47.04432 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bf946b2d-34b9-3386-9474-2335986070ee | -5.7538 | -47.0301 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6ade55f5-aa90-32c9-96c3-54bd6f8e2303 | -5.75281 | -47.03661 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| a99cb4f8-e1d6-3ae5-9be4-0492c71e609b | -5.75068 | -45.5639 | 2024-10-26 01:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 54e9ec6c-f15a-3c1b-ac16-c332dda054e5 | -5.74277 | -47.03184 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0b492a54-5c0e-3a1b-8817-79855c641727 | -5.71912 | -47.1139 | 2024-10-26 01:09:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1b8da758-7ce7-37f0-b6db-bd85077c87cb | -5.70733 | -45.02894 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| fe957a73-73a2-36ed-a153-64780a889819 | -5.70649 | -45.01369 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 982dfa43-3a88-3c6e-b4c7-205052b99802 | -5.69424 | -49.3408 | 2024-10-26 01:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f17b6bb3-8e89-3439-a742-4cb4d9b4a298 | -5.66053 | -49.10418 | 2024-10-26 01:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 9fd951e9-1da1-3f82-bdbf-3e7e70390975 | -5.58037 | -45.31102 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b17bf815-e71c-3683-927d-eabced646a14 | -5.58003 | -45.30526 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 977eb681-6da5-3f6d-870b-bb9eba1b532f | -5.57037 | -45.32671 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 51952305-e0c9-38ac-9dde-f916450c67d1 | -5.56765 | -45.31297 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 50db418f-29d4-3d17-8b99-ed6c3a84df9b | -5.5673 | -45.3072 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5c9ce244-b849-3e70-a96d-299245a338bd | -5.56319 | -44.34325 | 2024-10-26 01:09:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c7c12342-bec7-3c18-b459-104940784ce4 | -5.56013 | -47.04264 | 2024-10-26 01:09:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c32e47a7-a486-380c-a446-767dfefb6763 | -5.55789 | -47.02801 | 2024-10-26 01:09:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 008fadc3-6205-352b-9590-ed987d763c8b | -5.55734 | -47.03481 | 2024-10-26 01:09:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 36390092-8095-3551-9713-4cfbbeb4f307 | -5.55523 | -47.02028 | 2024-10-26 01:09:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| de9ed003-88f8-334c-8353-d707aa6fac57 | -5.26004 | -49.52721 | 2024-10-26 01:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 17cc7390-15f7-3447-b70a-1685afe8dc23 | -5.25862 | -49.51724 | 2024-10-26 01:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0a9541ff-5ffe-3c06-b5a7-20e2cbe8841f | -5.25755 | -55.96546 | 2024-10-26 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ee544db9-6d3f-3d0e-a6fe-f4889df60c64 | -5.25447 | -55.97166 | 2024-10-26 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6c085b63-9ff0-31e4-9aec-8320de9f6ec7 | -5.24934 | -50.69307 | 2024-10-26 01:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| e4197714-9e50-3af9-9d27-4912c119672d | -5.24676 | -55.96687 | 2024-10-26 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7c2bd4ba-a70a-3b14-b6f6-7e770c5c291e | -5.21624 | -48.22155 | 2024-10-26 01:09:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 4ecc92ef-c8f7-3166-9ab6-4925ff75b7ae | -5.20606 | -48.22306 | 2024-10-26 01:09:00 | TERRA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 774ad2a7-8fd1-384d-8552-7d491041e9a8 | -5.2036 | -45.3349 | 2024-10-26 01:09:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5e5efffd-90d6-398d-871a-14df2eb48af8 | -5.20299 | -45.32938 | 2024-10-26 01:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7801ee88-56fd-30ec-8a5f-c59cf555e7d9 | -5.11549 | -47.38939 | 2024-10-26 01:09:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 980b561d-76dc-33c2-a0af-b0c3584a069c | -5.06873 | -50.58593 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| da71e80e-82c2-31ec-aa52-c9e17ed53b55 | -4.92744 | -45.86529 | 2024-10-26 01:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dcc9608a-b7a4-365b-be23-4b3bf9a2e477 | -4.91797 | -45.8611 | 2024-10-26 01:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 55634d01-18a9-3e65-a168-922a96571f84 | -4.91512 | -45.86708 | 2024-10-26 01:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f8047169-f5de-37a3-b78a-22b6be54ce17 | -4.91252 | -45.84937 | 2024-10-26 01:09:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |


[Clique aqui para ver as próximas entradas](README13.md)
