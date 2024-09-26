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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63df26fc-a6da-313c-95fb-1305b25e11e8 | -10.4896 | -51.2075 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc1060f-08a6-34bc-bf09-980360abccf8 | -10.4913 | -51.214802 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c55778de-7bda-329f-a87a-62329e8e7bdc | -10.4929 | -51.222 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 214da7c3-51ff-3536-a369-829f56c7f5fc | -10.4652 | -51.236198 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68d2104a-83b2-34ee-9eca-3fdd46915ca9 | -10.4669 | -51.2435 | 2024-09-26 00:55:55 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5566e540-4172-3b06-a2a2-ce0dea850f2a | -11.1522 | -54.3619 | 2024-09-26 00:55:55 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a85be218-2e86-36e2-8583-53552aa72bc3 | -12.8219 | -62.648399 | 2024-09-26 00:55:55 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd21422d-0fa5-36fd-97f7-7052e2165105 | -12.8264 | -62.672798 | 2024-09-26 00:55:55 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37ce2faf-989a-3c83-9548-aa298b38e66d | -8.7087 | -54.7881 | 2024-09-26 00:55:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 06b0d21f-4b48-334a-a20e-0d98b3a0d609 | -10.1546 | -49.9804 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11d51d0e-e54e-3d47-a6d3-cd34bf51e595 | -10.1565 | -49.988499 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0e4434-1f40-36d0-ab8b-1eb0c335a4e9 | -10.1584 | -49.996601 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5829ed82-4290-382c-b2f4-557be31d2498 | -12.8123 | -62.6502 | 2024-09-26 00:55:56 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd55e0e-b18c-3420-9adc-bcc6144a3072 | -12.8168 | -62.674599 | 2024-09-26 00:55:56 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4f672f54-5cae-3f34-8bc2-8d75fb57bce0 | -10.1468 | -49.990799 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4c42637-52a3-336f-ad88-c3aea9653ff6 | -10.1487 | -49.998901 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5230131-23a9-3e95-bbd2-ef18e157c13e | -10.1505 | -50.007 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a806b16-6d5e-3a2e-b970-861ee20ae959 | -10.1407 | -50.0093 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cc18a2d-8861-329b-abe5-d3ff586bccbb | -11.1955 | -54.7514 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f486c80e-7dad-3a12-a527-636ee7a1f351 | -11.1972 | -54.758999 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5a09f1a-f53e-30ff-a4a0-4532d46584e9 | -11.1988 | -54.766602 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57ec1ac7-e50b-3d07-95fd-1416819d3190 | -11.2004 | -54.7742 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab3c56a-51b0-3ffb-8879-de4f23a7684c | -11.2021 | -54.781799 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f87a5058-b75d-3c22-80ac-488e029a106a | -11.1857 | -54.753502 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb75d6b3-172d-3205-a794-3d0c409ff01c | -11.1874 | -54.761101 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e90b1a20-ea1d-33b9-a1a1-2d595ed011c8 | -11.189 | -54.7687 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2c87ed9-57e6-34ab-8d8b-e33eb7d37dfa | -11.1906 | -54.776299 | 2024-09-26 00:55:56 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f10eea44-2f7b-3fc4-90c9-f5881c8f8a08 | -10.1077 | -50.000099 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20d33653-c779-3425-b4e1-a525d77b9d5d | -10.1096 | -50.008099 | 2024-09-26 00:55:56 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9e39d46-8617-3f44-a2c7-97381704cc99 | -8.8098 | -58.2172 | 2024-09-26 00:55:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 74c96352-471c-3dbb-a96b-ba3d63169f00 | -8.8284 | -58.2161 | 2024-09-26 00:55:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 72e6dfd2-ed62-30dd-9d15-9d770111f24e | -8.9244 | -67.1889 | 2024-09-26 00:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 88d3bf97-01aa-3c92-bc96-397a519df43f | -9.0468 | -61.4325 | 2024-09-26 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| baa8e6bf-23b7-3d16-870c-60d0853224c1 | -9.0361 | -67.0376 | 2024-09-26 00:55:58 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3e8ab175-4e2f-38da-86f6-7b4759f27609 | -9.0657 | -61.3743 | 2024-09-26 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5f09b67a-93ba-30cb-88c5-9a716a6f86ff | -9.086 | -61.1245 | 2024-09-26 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1b220546-29cc-3639-a7ad-52f4acc73207 | -9.1046 | -61.1237 | 2024-09-26 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 071ff0ab-3521-3001-b83f-1b7c3ae39690 | -11.4884 | -56.756699 | 2024-09-26 00:55:58 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2b1591-e8de-398c-b276-3d4699d61339 | -11.4904 | -56.766201 | 2024-09-26 00:55:58 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7eaac112-1f71-3927-b050-661e60f12037 | -11.4924 | -56.7757 | 2024-09-26 00:55:58 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37732e94-737b-33e2-989b-bf0c9c4ae6aa | -9.1535 | -65.5634 | 2024-09-26 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c9ecc857-d537-3244-906f-08f6f2bf262a | -9.1349 | -65.564 | 2024-09-26 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| d614336c-d468-32d9-b9a1-9f1d68778e96 | -9.135 | -65.5453 | 2024-09-26 00:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5d770008-3502-346d-9aa1-45e39bd53f66 | -10.7819 | -53.563099 | 2024-09-26 00:55:59 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2276403-8b26-359a-8360-55404edc08ed | -9.6015 | -50.1566 | 2024-09-26 00:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 86a5fca1-972e-381a-8512-c04bd8f9cb43 | -9.6018 | -50.1352 | 2024-09-26 00:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| f43887be-ad5f-33cb-b105-328e5032058a | -9.6149 | -57.7568 | 2024-09-26 00:56:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 171cdbe5-aea0-3ecd-b0d5-61e02d02d031 | -9.8776 | -50.164799 | 2024-09-26 00:56:01 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd3274a2-bd5e-3473-ad47-e0306451b9b0 | -9.806 | -53.5664 | 2024-09-26 00:56:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c4495074-0338-3eb8-b3c5-6e1a4d1c77dc | -10.413 | -52.921299 | 2024-09-26 00:56:02 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78429690-4c4b-323f-a017-71b801a05add | -10.4145 | -52.9282 | 2024-09-26 00:56:02 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fff4c1bf-6ea2-3e6c-b4b8-b7b49619b031 | -9.8083 | -68.8152 | 2024-09-26 00:56:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 59bfdec1-deb3-307e-936c-9565ca96629c | -9.8269 | -68.8148 | 2024-09-26 00:56:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 546f1e08-1739-38c7-8310-c9c0d8385ab8 | -11.727 | -59.269901 | 2024-09-26 00:56:03 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42e7ce1e-de6f-32ca-a073-5981dd06428a | -10.4542 | -53.291401 | 2024-09-26 00:56:03 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a31f8d00-5aa0-34ee-a5ea-5d284333bf2f | -10.4558 | -53.298302 | 2024-09-26 00:56:03 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a513389a-acee-3c1d-bae2-1daf63de4771 | -10.4573 | -53.305302 | 2024-09-26 00:56:03 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e797ad4-cb4b-3693-ae9c-647c210003a9 | -10.446 | -53.300499 | 2024-09-26 00:56:03 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f04455ed-c794-343e-bbbc-f0a6713e9b91 | -10.4475 | -53.307499 | 2024-09-26 00:56:03 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc095362-1c7d-35e3-a907-6d51914662ed | -10.9611 | -55.762299 | 2024-09-26 00:56:03 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 154eacba-c0af-34e8-8d52-95de470ef820 | -10.0506 | -68.5875 | 2024-09-26 00:56:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 46.1 |
| e2688a3c-91c9-38b7-8cde-0877a44145f7 | -10.5883 | -54.2267 | 2024-09-26 00:56:04 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd8d5bb-1116-39a7-8acc-376ff126d021 | -10.5899 | -54.234001 | 2024-09-26 00:56:04 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91c3e381-52e1-337d-b884-8507c1cf3b17 | -10.3713 | -58.9056 | 2024-09-26 00:56:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ccf97413-1434-3f93-b7fa-e11fca99b6ed | -10.283 | -53.0308 | 2024-09-26 00:56:05 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67b6492a-1f4d-39a1-9c35-0ab6cd8fc162 | -10.2845 | -53.037701 | 2024-09-26 00:56:05 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e849a777-379d-3f0e-9fdd-7b0c10487649 | -10.2861 | -53.044701 | 2024-09-26 00:56:05 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65795af9-5ecf-350c-8e48-c5441ec1a358 | -9.5911 | -50.1306 | 2024-09-26 00:56:05 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| befe90cc-bebb-3afd-98d2-7c92cb959f9b | -9.593 | -50.138699 | 2024-09-26 00:56:05 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4388ef-3d53-39b2-8e92-c1a02e981e86 | -9.5968 | -50.1548 | 2024-09-26 00:56:05 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 777edf0f-79d6-3d02-a683-9ba27a59c1a2 | -9.5813 | -50.1329 | 2024-09-26 00:56:05 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 806a7379-80a8-3699-a57c-8b3242ac01f9 | -9.5832 | -50.140999 | 2024-09-26 00:56:05 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba24c0ee-789d-3825-a480-daf3ec7c2598 | -10.3882 | -67.8737 | 2024-09-26 00:56:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a1f2e272-b647-304e-b716-b46a88523faa | -9.5516 | -50.1824 | 2024-09-26 00:56:06 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f702d15a-00b2-3d4c-b6d2-5a4175537a22 | -9.5535 | -50.190399 | 2024-09-26 00:56:06 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04b7f25-1be7-39d4-ab3c-7ce47df54ffd | -9.5455 | -50.200699 | 2024-09-26 00:56:06 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91795645-51b3-3c22-962d-20d415ea1b97 | -10.8915 | -57.4521 | 2024-09-26 00:56:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7dd5d11e-1998-3080-be94-369ce7d288d4 | -10.8917 | -57.4322 | 2024-09-26 00:56:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 97aa2567-17df-3147-be73-032c71fd8eac | -10.9264 | -54.2692 | 2024-09-26 00:56:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| faa5e3bc-5f3f-398b-b934-55e1ef651f4a | -10.9928 | -44.415 | 2024-09-26 00:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 528c1a3a-979d-3064-bdb3-3e7e6aa978d7 | -9.3907 | -50.023399 | 2024-09-26 00:56:08 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28f60e38-9efa-30ce-bb10-7ce022ab3cd6 | -9.3926 | -50.031601 | 2024-09-26 00:56:08 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10eedd23-6360-331a-8c9d-6876cd0ac546 | -10.7638 | -56.376598 | 2024-09-26 00:56:09 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b41d210b-db46-304e-a6bc-437f8a5583b1 | -10.2418 | -54.100101 | 2024-09-26 00:56:09 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a288d62d-5860-3265-82c4-429a92422213 | -11.2034 | -54.7752 | 2024-09-26 00:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 484a5a6e-4120-340c-8bff-dc63c154e470 | -10.2238 | -54.111599 | 2024-09-26 00:56:10 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 885d750a-00d8-3b2b-97af-38146c61f4d4 | -10.2093 | -54.0923 | 2024-09-26 00:56:10 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb5c5d4-83cc-3ab3-9187-898a0fff15df | -10.8974 | -57.402599 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c66aa8d-09ca-3ec9-ba61-dba98a4a8fe7 | -10.8995 | -57.412701 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c633944-31d4-3495-b576-0e438dc75e66 | -10.9016 | -57.422901 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 613fc9bb-c552-321d-bf7c-298ed4848609 | -10.0337 | -53.437 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40213355-3ff0-336d-a581-2f7da5b37cdb | -10.0352 | -53.444 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f62bbd6-25a1-3e87-9c63-8478d76a7f44 | -10.0368 | -53.451 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5546e176-73b5-3aba-8184-12d43551b15a | -10.0383 | -53.457901 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f867f619-c78c-3ab8-af49-7b4a9e1ff3de | -10.0399 | -53.464901 | 2024-09-26 00:56:10 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e40b349-a6de-35f0-8ffe-61a26aafa13d | -10.8897 | -57.414799 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9739788a-da3c-3c21-93f1-8de57f16aa69 | -10.8918 | -57.424999 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7d415cd-4119-32e1-a298-d312e8817d5f | -10.894 | -57.435101 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93a4e14e-07b2-32af-96ae-45571f6afdfe | -10.8961 | -57.445301 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 060c8d3b-294d-39f3-830b-0639b55e7606 | -10.8982 | -57.455502 | 2024-09-26 00:56:10 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
