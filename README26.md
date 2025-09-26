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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31c6f978-18d5-369e-8070-c1d60d05915d | -3.63403 | -43.86904 | 2025-09-26 04:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b7024df-b37a-3696-b8e5-40f44b379ba6 | -3.81444 | -41.56059 | 2025-09-26 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1ade14cf-00d1-3d4e-a640-032ff5fa543c | -2.63631 | -48.04027 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e259e67-3af3-3960-9eb2-51583a771214 | -3.69175 | -49.04264 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f46b9e9-e84c-38cb-bf04-b9bb87f6e864 | -2.37874 | -47.71483 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f9682e8-ddde-31b1-8af6-6a6f0b4c2584 | -3.33257 | -50.19835 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 106954fc-1063-357d-8443-4eb0b81d8fec | -3.33142 | -50.20554 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5ed2929-141c-3751-b6ef-a1efef74be28 | -3.17072 | -49.47678 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35585bbd-d46d-3be9-b349-938132ff7541 | -3.4493 | -44.12386 | 2025-09-26 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7076120f-70d8-3bda-9ddb-9d7d57fff411 | -4.78921 | -42.81752 | 2025-09-26 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c392947f-7823-3252-b79b-ae972e0bfbcd | -2.35992 | -48.88995 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b50a816-3748-345a-8faa-366a78162de8 | -2.9176 | -48.63411 | 2025-09-26 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26f9a800-a818-3945-b6b5-57b1bb41b75c | -3.80237 | -47.58306 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eb0a2d3-2aad-3617-b4a1-ebe0105cbf52 | 0.24443 | -51.3012 | 2025-09-26 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fb5d32f-ef18-32a3-b850-7874645f50b9 | -2.79254 | -49.59683 | 2025-09-26 04:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e7c72be-be8f-30ed-aabb-4521f689a61c | -3.62945 | -43.87198 | 2025-09-26 04:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d3b17d1-0651-39d9-93c3-90fcb8bf989d | -4.40051 | -44.08903 | 2025-09-26 04:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77234471-a433-3881-9c7d-13722519fd19 | -4.03579 | -46.93034 | 2025-09-26 04:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e42914d-bab0-3a12-ab30-7764ca36178f | -2.30381 | -48.14876 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 786ff543-d0c4-3b28-970a-a8d6fdff6175 | -3.33471 | -50.25041 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9f2fef5-defd-3759-a8f3-d88ee590c559 | -3.78002 | -48.63486 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6929b92b-fe3a-3b8a-b776-7171ccfd49c1 | -3.80463 | -47.59075 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabf4f3a-3d7a-3ef0-b15f-6198705f63ee | -3.44456 | -44.12827 | 2025-09-26 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 17a4f014-695b-3427-9996-49c89a739ed5 | -3.78057 | -48.6314 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64c1b1f9-1f23-3e21-9912-69fa6924a170 | -3.64683 | -48.32243 | 2025-09-26 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cefc1848-93f2-3086-b1e3-895e02df22f0 | -3.86622 | -43.78344 | 2025-09-26 04:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac206f7e-18dc-3b87-afaa-7fa69ef0589a | -3.80346 | -41.56916 | 2025-09-26 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e8f61df5-444d-3f13-8216-95b83cd3ffcc | -4.17326 | -44.27221 | 2025-09-26 04:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a729736-089a-37ca-9255-7e4e10786035 | -2.69326 | -54.94924 | 2025-09-26 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b810e216-d3c5-30f5-9d75-08df9e40feea | -3.94047 | -47.56741 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a0fc93e-ac1f-3b22-a3d9-66ff871ddb37 | -3.80181 | -47.58665 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f68ab4-6b79-3947-a21a-f37b64b950b3 | -3.68788 | -49.04557 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ba11e0-25af-3710-9691-e7bc404c5189 | -3.51774 | -44.03701 | 2025-09-26 04:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c514f9dd-8209-3859-a0c3-e75813735184 | -2.30164 | -48.14803 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c580f63-8db1-3dc3-a6f4-3ac7b05cafe2 | 0.69161 | -51.46321 | 2025-09-26 04:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112d3de5-b5b4-3175-b2bc-83046b01de4c | -3.49473 | -44.76815 | 2025-09-26 04:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1fb7666-4ba9-359d-8860-62c412fb8738 | -3.72933 | -49.68272 | 2025-09-26 04:40:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6178167b-8c6a-3b29-abeb-c75bcdd82f30 | 0.24511 | -51.30546 | 2025-09-26 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fca7a5a-fbb3-37b6-b698-9ac6c06d54d8 | -4.32068 | -44.29333 | 2025-09-26 04:40:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73700d4a-0b89-3462-ba4d-660cd1049ee2 | -3.33528 | -50.24681 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bce7599f-be24-39e0-bc13-8c3dbbd60d58 | -4.79116 | -42.74311 | 2025-09-26 04:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 445c3330-a660-3aa4-be06-914d0cbfb05f | -3.68842 | -49.04212 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 650d990a-68a0-3f0e-b8ad-48474846a786 | -3.33481 | -50.20606 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a24b254-1fe7-3fde-a8fc-fd51d5586bb0 | -3.77669 | -48.63434 | 2025-09-26 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98333f80-be9f-3978-9fff-b17188915760 | -1.87843 | -48.40429 | 2025-09-26 04:40:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6395b39-0dc8-3bf7-8620-2d333ce1c05e | -3.45327 | -44.12445 | 2025-09-26 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9679b8eb-18d0-3fb6-8b6a-f0254760ecb9 | 2.64703 | -51.01141 | 2025-09-26 04:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e4b7967-fcb1-30ab-8458-d2ad15ca794a | -2.44785 | -49.01709 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d97ab029-f7f6-39d9-bd21-afa3c6ed2b06 | -3.62999 | -43.86842 | 2025-09-26 04:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8589c061-8e01-390b-8717-2327974bb85d | -2.19232 | -54.46768 | 2025-09-26 04:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb04e95f-0891-3498-93c8-77d797895c97 | -3.77947 | -48.63832 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c59f47d-ed08-3476-b464-207f60c91bbd | -2.94216 | -49.3369 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a12212-2420-3e07-83e3-db4ff4c13a27 | -2.69768 | -54.94997 | 2025-09-26 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a1522dd-4d1b-3e8b-9740-dd929f0afc1b | -3.78389 | -48.63192 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf22799-2608-3bde-86a1-3b823b33b364 | -1.08699 | -54.11045 | 2025-09-26 04:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 160f5738-1330-3af2-b0d0-ba636a7ab760 | -2.30435 | -48.1453 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0e771ef-9ba3-36e2-a470-0005123018e0 | -1.09127 | -54.11115 | 2025-09-26 04:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3004773a-4893-36ea-aaef-fe134185538b | -3.44534 | -44.12327 | 2025-09-26 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bd2b2ba2-5c2a-3cf4-b464-4164889da094 | -3.24959 | -46.6053 | 2025-09-26 04:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f50f1e3-245b-3b65-974e-bf3afe6b290c | -1.14993 | -54.22208 | 2025-09-26 04:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 549841a8-228f-3336-9ccb-df286f8f3b4a | -2.9618 | -48.59148 | 2025-09-26 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d62d1fdd-4ea7-337d-b966-0b68ce647fe9 | 1.00906 | -59.51409 | 2025-09-26 04:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad898a95-aac2-3fe4-8850-4fc3b7fdca9a | -2.71846 | -49.1666 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a6f0c34-bf21-343d-924f-9be0dec3ecb0 | -0.46622 | -52.18354 | 2025-09-26 04:40:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e12e927-57eb-31dd-b2ed-766bb3622994 | -2.17093 | -50.43057 | 2025-09-26 04:40:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24259081-7217-3e8c-814d-00b0f51210e1 | -2.71025 | -54.95646 | 2025-09-26 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5a13379-2e1b-3708-9e7b-e487a88893de | -3.94103 | -47.56382 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbf6b479-71c5-3331-b2ff-fba6f5622f3f | -2.92277 | -48.30566 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fac00e29-4426-395a-9965-330c486ad22e | -6.56862 | -43.65697 | 2025-09-26 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 674d4f06-5613-3f18-b7d4-5d8395c4e9b3 | -5.58085 | -48.94946 | 2025-09-26 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee6a3ab5-cab8-396d-96be-bcaa88bcc73a | -9.71139 | -48.25046 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79e15cc6-64e5-3b4a-8267-9e5b6b9d778c | -9.88191 | -47.74666 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 332fff25-1552-3ee5-b47c-1b3b578d4a0c | -5.13894 | -45.38489 | 2025-09-26 04:42:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecd52df5-2ff2-301c-a6ef-08d2ce3e4a39 | -5.6433 | -43.92415 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc89656f-5a56-31d4-a510-c8b1493f32d3 | -6.6104 | -42.93195 | 2025-09-26 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4d50e1a-68ec-3e1a-894b-5f0070eee8d6 | -5.46372 | -43.06819 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cf61011f-052e-357d-a424-cda2e8147148 | -10.40617 | -46.17288 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 933ddd37-0543-36c4-8d47-ec55517d9b08 | -5.18354 | -46.07585 | 2025-09-26 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9e4edc-79f4-3568-94fc-108599086c01 | -4.25605 | -48.59954 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 633cae3a-2be7-31c2-a41f-7888b69ebfcb | -4.74839 | -43.61123 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 599a1c99-5413-3254-8074-060d41770e5f | -9.47195 | -48.23718 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d78d321-c7ff-3f70-826f-3ad8cf438fb6 | -7.44633 | -41.91115 | 2025-09-26 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 27f6124c-074b-333c-8971-b7e729c16aeb | -7.8013 | -46.01764 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d3337dcb-d67a-38de-90d7-fecdad6c192c | -6.99392 | -46.99363 | 2025-09-26 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bce05db-7bde-3d4a-a381-48ee0a56a5f3 | -4.48528 | -47.67662 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ba67617-be37-3e85-ba0c-5b8624d7d1f4 | -4.75256 | -43.61193 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c14df4f6-29f5-3744-9f8c-cd60384bf652 | -7.25095 | -43.01604 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee28f95f-2f86-34bc-8d72-4f9ab1294539 | -5.43021 | -45.14121 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f10e69a6-5eb0-3cf6-b9ac-3848515651d6 | -5.53437 | -43.87855 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea744a29-af98-338b-b114-2432eeb0b565 | -5.73098 | -42.63353 | 2025-09-26 04:42:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9fd205b8-a34c-3a8b-b3ff-845e3a576cba | -4.51097 | -49.06494 | 2025-09-26 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c3bc07a-3d9f-3110-9fe2-ca3348dc822e | -6.25943 | -42.4925 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba89a878-0df2-3fa5-97d9-33cb975e02af | -9.55127 | -47.51939 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a8711d-29b4-3940-87a1-cb4b3e5e7f94 | -6.99599 | -44.70296 | 2025-09-26 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8d21be3-c438-3953-a418-7ef710121d9f | -10.11096 | -45.33271 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 053a9aaa-9bb4-390d-b872-373183e233ea | -5.63857 | -43.92739 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 337b4fac-507d-3a50-91c3-df5913fe7815 | -10.12195 | -45.31335 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaf31477-4ca7-3f20-a17a-23f870ad16b3 | -7.1299 | -42.19645 | 2025-09-26 04:42:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf4743e1-f7a1-3e6c-819e-5855eccb0bf5 | -6.25416 | -42.49628 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d238d11e-911c-3853-a02a-56f80fa45b6b | -5.78186 | -42.76028 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README27.md)
