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
| 0bdaeea5-393f-39f8-95bb-0924861ccca7 | -15.3902 | -55.8409 | 2024-10-02 00:16:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4d2ffc15-fd43-3557-aec0-600c004b301b | -16.612 | -57.2579 | 2024-10-02 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 59870b6c-1565-39e5-999f-3630c9cc2d5e | -16.6124 | -57.2375 | 2024-10-02 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.4 |
| a1fb8340-68ec-3961-87e8-64374c631b04 | -16.6127 | -57.217 | 2024-10-02 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 30d4c8f2-bcfb-37af-8b52-0c30b05def8d | -16.6303 | -57.3376 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 323add79-8a61-3c12-8ae2-582d1604e331 | -16.6306 | -57.3171 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 7cba8b92-9284-3def-b005-8596bafac137 | -16.6319 | -57.2352 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| da2b018a-7bed-33d1-b968-1cd14f1f8265 | -16.6322 | -57.2147 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 3ade8915-1608-32d2-94db-c79f3100f533 | -16.6713 | -57.2102 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 7121f60d-4521-3f5b-8186-636ae550cb22 | -16.6717 | -57.1897 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 6ce09088-04e7-34e8-96db-e93c5ae7eb26 | -16.6868 | -57.4741 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| aac7c366-dddf-3a69-b497-0e379a88b64a | -16.6884 | -57.3718 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 25cdf77e-ffd6-338f-9cca-a0e7559fef9d | -16.6887 | -57.3513 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 6feea97f-eeee-3c54-a04b-2ce2ed9eb15d | -16.689 | -57.3309 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| f2146b4b-349e-3681-904a-e0cf4f6c2a45 | -16.6909 | -57.208 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 0f8e94bc-d35e-3b78-a9c7-51f6aa46cea2 | -16.6912 | -57.1875 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.8 |
| 06736f2e-14e8-3283-8e8f-8c238c703102 | -16.7079 | -57.3696 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.6 |
| b7b4fc14-b4b7-39d4-afdf-5b474f4f8e60 | -16.7082 | -57.3491 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.6 |
| 1f4b6200-6798-3ae0-ad24-9d41465ee613 | -16.7265 | -57.4287 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| c9a86d88-2f19-312e-a438-c074b2ba6a53 | -16.7452 | -57.4878 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 304ac63a-3b10-3f18-963d-19a1dc32f400 | -16.7461 | -57.4265 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| dd684efb-d6d5-35a8-b20f-a81b59dcec3d | -16.766 | -57.4038 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| d5ba24f0-673c-33df-a886-a2dbde70054e | -16.7663 | -57.3833 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 9fa94a62-62d8-32ef-945c-0b538bad7d3b | -16.7666 | -57.3628 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| cbdd887e-d996-359d-b3e9-cee2a0645820 | -16.7859 | -57.3811 | 2024-10-02 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| e61280be-b555-3432-8ca4-6da126e4343f | -16.7862 | -57.3606 | 2024-10-02 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 73c7e886-16e4-324c-8c99-e2deb915804c | -16.8292 | -55.9152 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 135.6 |
| c4e83c66-7973-3103-9f1f-9b3d119d3e7f | -16.8295 | -55.8945 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 191.3 |
| e47df596-9dc6-3b0b-8baf-f23e971cb8d3 | -16.8299 | -55.8737 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| edbb4f13-f970-36f4-ab9d-6caf7a75b0b5 | -16.8234 | -57.4789 | 2024-10-02 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| e57c9131-7450-3dd6-a1ad-fee4c370c904 | -16.8488 | -55.9128 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| c2b39847-4743-3ed8-b730-7d17022c31e7 | -16.8491 | -55.892 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 3f9a451f-aaa6-37b2-875e-da463953e555 | -16.8684 | -55.9103 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 510b9315-782c-3bb7-a6b8-f38537a952e0 | -16.8695 | -55.848 | 2024-10-02 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| cf24c416-c80e-3629-ae33-dc73ff7be00c | -17.0612 | -56.0931 | 2024-10-02 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 69c8191f-6931-3396-ab98-9992131af5b7 | -17.0705 | -56.7114 | 2024-10-02 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 0907fbcc-dc52-31fe-9523-c6ea101baba2 | -17.0709 | -56.6908 | 2024-10-02 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 42ef5772-92d5-34bd-a339-420dfa9a1381 | -17.0902 | -56.709 | 2024-10-02 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 08050884-4f11-30ae-bdea-0984ac98955f | -17.0905 | -56.6884 | 2024-10-02 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| f22fc121-dcc9-326e-bf1f-6178a4b6422f | -19.2317 | -46.8687 | 2024-10-02 00:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6d8a320d-2e07-3f1c-b372-673006d3ed8a | -19.2323 | -46.8452 | 2024-10-02 00:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9cd0bb72-dd6b-397c-ad76-68cab01a2051 | -19.2519 | -46.8641 | 2024-10-02 00:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 137.0 |
| a5193508-3aec-3a1b-ab17-060483cc0b24 | -19.2526 | -46.8406 | 2024-10-02 00:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4fe79f5d-f800-3212-96cb-1b37c8e8120d | -19.7618 | -41.9953 | 2024-10-02 00:16:54 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 4368c798-328f-35f3-8040-4abba144b53a | -19.9719 | -55.4759 | 2024-10-02 00:16:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 069abc08-05ff-3f17-8996-1bdb9561e4b2 | -20.5266 | -46.2783 | 2024-10-02 00:16:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 7c413907-e191-327d-9b65-0d70c941003e | -21.4175 | -50.9759 | 2024-10-02 00:17:04 | GOES-16 | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 00801413-729d-3175-9e0d-0e7d34e68d46 | -21.4381 | -50.9716 | 2024-10-02 00:17:04 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| 033ab371-42ca-3a76-84fa-87912fcd6bb6 | -21.6275 | -50.796 | 2024-10-02 00:17:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 17412ad3-cd47-3b04-8909-a7a76cc14976 | -22.9277 | -43.7243 | 2024-10-02 00:17:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| bc00a90f-8fc3-391d-9530-a3e302c54177 | -22.8803 | -45.0842 | 2024-10-02 00:17:11 | GOES-16 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 90a1762b-8ce6-37e6-8c27-baafb6bff51a | -22.9006 | -45.1029 | 2024-10-02 00:17:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.0 |
| 73b81ee4-3920-3232-961b-1a3bc48d5ec7 | -22.9014 | -45.0779 | 2024-10-02 00:17:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.3 |
| 868f8354-a64a-3260-8b7e-49a693a359a6 | -3.128 | -49.4235 | 2024-10-02 00:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5853619d-2784-3f16-aefd-8cd8620bc434 | -3.1465 | -49.4229 | 2024-10-02 00:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8b1e2f4b-65a9-3c86-9cd2-c418b438e054 | -3.2136 | -46.7843 | 2024-10-02 00:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| b39c6a74-7328-3e97-981d-9d7d05094534 | -3.386 | -54.1187 | 2024-10-02 00:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f63f1d22-ca5d-394b-bbca-ed6128efe44a | -4.447 | -42.8889 | 2024-10-02 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2ed55ac2-55dc-3fe7-9551-57f7ed53ab42 | -4.4655 | -42.9112 | 2024-10-02 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 82c0b1b5-128d-39a7-b8af-02951ab9e4bb | -4.4657 | -42.8877 | 2024-10-02 00:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.4 |
| f6ef3e9d-8db2-33bd-960a-5cc6276517ff | -4.4658 | -42.8643 | 2024-10-02 00:25:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 52e71dff-34b9-3dfe-91cf-35868189c8dd | -4.4679 | -48.127 | 2024-10-02 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d4733fbb-6fa8-3719-afe7-7d8e0bf8ae4e | -4.4681 | -48.1054 | 2024-10-02 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b8d55cb8-65ae-36df-8333-541b2898dfb0 | -4.4865 | -48.1261 | 2024-10-02 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ef05b687-c0e8-37c4-94d5-0aa962f52830 | -4.58 | -48.0132 | 2024-10-02 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e3ae6390-37a9-30e5-944c-8c8d8e736385 | -4.9203 | -47.1445 | 2024-10-02 00:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 5e7be2f4-7393-39a7-b214-9ef426c91ecc | -6.1373 | -46.4484 | 2024-10-02 00:25:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 70df4e3e-24ec-3e2a-b990-ef08a57b4cb0 | -7.1796 | -46.9444 | 2024-10-02 00:25:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7e039ac0-c0bb-3809-8eac-47deb29d9412 | -7.7129 | -42.995 | 2024-10-02 00:25:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| a12f1fab-c253-3c08-866a-986d340ee6ac | -7.651 | -67.2009 | 2024-10-02 00:25:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a89fd1cd-148b-315c-9526-1ba264affae4 | -8.205 | -44.365 | 2024-10-02 00:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.4 |
| adead149-05c2-33a5-9ab8-9d2145d1af23 | -8.2053 | -44.3419 | 2024-10-02 00:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 72a729ef-e65b-333d-bccd-071508f72b48 | -8.2239 | -44.363 | 2024-10-02 00:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 22936486-7f06-3330-b3de-919166fe2396 | -8.4643 | -62.7124 | 2024-10-02 00:25:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6e54ffdd-86c6-3ffb-9fa3-7682ec74b7f5 | -8.7601 | -66.618 | 2024-10-02 00:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c77ad7e6-cac0-3457-80be-f51c30ca8d5a | -9.601 | -50.1993 | 2024-10-02 00:26:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 96b30d29-2f84-30a2-92aa-e7231d2506f2 | -9.4753 | -68.5269 | 2024-10-02 00:26:00 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 33.4 |
| c71ebf41-7381-365b-8e3d-08f009580404 | -9.9736 | -36.0362 | 2024-10-02 00:26:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| f78b0e85-538e-3eef-a003-c7ad271a6d5a | -9.5397 | -62.8195 | 2024-10-02 00:26:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 40fc2ca5-5c7c-3143-94f8-eb61ea3fe9db | -9.5398 | -62.8005 | 2024-10-02 00:26:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 115.4 |
| a68c727a-3ac0-3e4f-ac22-ee063dcc847c | -9.5584 | -62.7997 | 2024-10-02 00:26:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7d68585b-5752-3f90-840d-e76f0c51a175 | -9.9366 | -64.9367 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 96935215-da67-3896-a896-b3da7d2a22de | -9.9367 | -64.9179 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 340.6 |
| 35860fc6-f667-313f-9c9a-aa8ac520210f | -9.9368 | -64.8991 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 280.5 |
| 29dd4ae4-f13c-31e9-bcf3-7ebd34202fc5 | -9.9553 | -64.9172 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 184.8 |
| c851d179-d6ba-3ec8-87c6-83f569d764fd | -9.9554 | -64.8984 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 188.7 |
| be9f4213-35d5-393b-a745-72b070dad2a8 | -9.9933 | -64.7654 | 2024-10-02 00:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e04b6c48-3a5a-3034-9890-3224c98d781b | -10.626 | -55.8752 | 2024-10-02 00:26:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6096dcf7-9343-37e2-8126-4092023a8371 | -10.9044 | -50.1304 | 2024-10-02 00:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 56b4f658-62b8-3996-a7ac-4ddcc44bfda9 | -11.884 | -43.8142 | 2024-10-02 00:26:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a17ccdfc-625e-3eed-8490-fef772473587 | -11.6555 | -64.9991 | 2024-10-02 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 285e0fb4-0f34-387d-ac7a-6357385f26e9 | -11.6556 | -64.9802 | 2024-10-02 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 627fe81c-b120-3217-91d2-0f59b463c37b | -11.6743 | -64.9983 | 2024-10-02 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ceaa6ca0-61e4-357d-bb1a-ff09eeacd083 | -11.6744 | -64.9793 | 2024-10-02 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 031858d1-8303-3473-b2fa-d86e5f879f3f | -12.1597 | -50.0501 | 2024-10-02 00:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 638ee757-b400-3743-8971-fabfcae57ccd | -12.4433 | -43.7242 | 2024-10-02 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 825b4957-3ff6-376d-8db2-af1abc00c5da | -12.2946 | -47.6446 | 2024-10-02 00:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 3872104f-6f99-3d05-b450-3c8ad5e6999d | -12.6295 | -63.1225 | 2024-10-02 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 908e5cd9-1c26-38e4-82f8-06ac3283c758 | -12.6484 | -63.1214 | 2024-10-02 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 2ede41af-8347-3e04-b082-14f18713b287 | -12.6486 | -63.1022 | 2024-10-02 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |


[Clique aqui para ver as próximas entradas](README4.md)
