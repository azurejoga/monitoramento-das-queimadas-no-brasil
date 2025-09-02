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
| c87646ea-fa87-347b-90ad-883b5497a74e | -10.80115 | -46.33875 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17286bab-ecc4-3585-9e48-c100d6f2a628 | -15.02489 | -42.15127 | 2025-09-02 03:51:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80190c21-5025-38f6-a934-1c47c3de87c5 | -10.26315 | -47.52268 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56219bbf-a7d1-39b6-9620-73514f5ac767 | -11.67623 | -52.18693 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| adbe3fad-5850-3831-a3cd-67c0d91e1ea2 | -10.04551 | -48.1495 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8325dc41-3eb3-391d-8105-413059f9ddac | -8.45899 | -47.36572 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 781d8676-050e-3618-98d0-02c9cd9c1372 | -7.38405 | -47.04867 | 2025-09-02 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08a7b148-fa2b-3ab2-85df-1bb5dd7797cb | -8.46338 | -47.36858 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b18fc0f0-2a98-3bbf-a053-693760598ff2 | -11.02876 | -46.85576 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c38e5b-6294-36f0-8927-76160fe33620 | -7.88488 | -45.18175 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afb80e88-b288-3978-bb64-22a0d800ce16 | -11.66864 | -52.17753 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 39a39163-308d-3461-8a9f-2309d2b24a26 | -9.47548 | -47.61022 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f94f351d-fc9f-3104-b131-aea5d2061987 | -9.72404 | -48.95797 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15c14e6b-edfa-35e0-9610-71b4b485c1bf | -15.02297 | -42.14848 | 2025-09-02 03:51:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| af8e72fa-7df9-3700-a140-a8d66126f6b4 | -11.37404 | -43.56856 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 970d5298-1aa5-37ef-a983-78a7793bef33 | -11.0892 | -44.63856 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 544c3ed4-1a61-36f5-9e25-e4f1ac89994c | -12.76035 | -44.41346 | 2025-09-02 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b3b6df0-159b-3a98-ade2-fd4a69c05666 | -10.04664 | -48.11265 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbaa7d79-e6ae-3c2c-9694-720b89469b4d | -7.69694 | -50.27998 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dab211a7-73fa-3002-a192-39c31a962471 | -11.01948 | -46.8469 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c00bb738-817b-3772-be3a-754b79db170e | -9.96891 | -46.41308 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48bbf61e-3d4d-3326-8a4e-76dce3268ea6 | -8.45479 | -47.35672 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c8b657d-7cdf-3602-a54e-02e794bcfa8c | -7.99186 | -46.47643 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30ea1860-0b11-3e9f-aefe-d8dea944b372 | -12.7672 | -48.08695 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecde0fa6-abae-3a84-9ae7-61e47878141e | -11.96334 | -45.79984 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff7e9267-5d77-385c-9d15-cf358545482a | -10.26876 | -47.52359 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aee24f8-950d-3538-8f1b-52baad797009 | -11.67521 | -52.21777 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| a62d55b6-0a4a-33cc-bcd1-978c90bf7267 | -12.80734 | -48.05824 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50c767f8-352b-3b9e-9986-f72bdf2218b9 | -11.97463 | -45.87506 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 11de174b-34bb-36e3-923e-3b13ead76968 | -13.31623 | -46.83099 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6399c749-efca-3382-af00-d0387fc0fe49 | -12.88625 | -48.17361 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95aea8a0-1106-3545-9fee-55e1084db2bf | -9.48051 | -47.60911 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c29f7a81-42bb-38ab-a470-8cc765c0511e | -12.97867 | -48.10715 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7cc138d-37eb-3054-94aa-5fb3d5b9d317 | -11.79918 | -46.40401 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 83d6b64b-67be-329e-8ce8-06252ae302e7 | -7.84688 | -46.74183 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd5e417b-24f7-35c1-bf0e-7ee6648b3933 | -11.65581 | -52.16735 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9245a3c-ed89-3475-b13f-e77ccfcf1e01 | -11.67018 | -52.17017 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa668250-f000-3ec0-a0ee-0cb29e6e597c | -10.75686 | -49.57072 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3dfc294-c581-389c-8b59-7e933dd430c0 | -14.48746 | -45.94213 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ba510bc-f22b-3e84-80a8-78d18251fddb | -7.98505 | -44.05444 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb8cf28e-fbf1-3808-9567-f1cd1f601a04 | -10.29249 | -47.52047 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffb9f85a-d9fa-334e-95fd-94dc5996a5ac | -11.65116 | -52.18942 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 88ff4551-7061-31d6-b844-b0b3eb5a6ad7 | -7.71443 | -50.26343 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acc335c-55fc-3f08-8132-ddd829eceab5 | -11.91314 | -46.6782 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9954eed0-e4c5-3a45-9b59-1b2e39a1b5bc | -12.61994 | -48.1811 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| db0e0e5f-532d-3ef9-a62a-a07c76a73892 | -11.67828 | -52.20305 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| bddae3c3-4587-3ada-bdb4-9dc3628f7db5 | -11.90308 | -46.67514 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d91caa6f-9e9e-35dd-ba01-b3057830cfaf | -12.86008 | -48.05219 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2752b98a-a02d-3df4-8789-4355d6d6de2f | -13.72317 | -46.9362 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249ae912-2e89-3a5b-b0e1-06fc56673722 | -11.0248 | -46.84767 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dce5d26-51c2-3040-9c10-588eedabc3b7 | -14.71734 | -46.74877 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4791fac3-c9dd-3ba9-86ae-bc0d51d8a2ee | -11.86418 | -46.71191 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f9ef6c6-b32c-37e8-b8eb-4e5daaeb6417 | -14.73462 | -46.74732 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2994f0c5-3125-3851-bc36-1191488af369 | -7.61151 | -46.03561 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f81b0b91-6551-3861-8f3d-ac1079a18213 | -12.80661 | -48.06194 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd369cb3-74ab-3ced-afa7-1b8b83775e6f | -11.10572 | -44.65123 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c386989-cd69-37cb-8d0e-d3233cb4f10c | -12.99603 | -48.10644 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13373fb0-5e24-3b39-be33-ab1b5efb8ac4 | -11.66241 | -52.20724 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 4ac14aac-d4d4-3e26-a726-1d2878104acc | -13.28388 | -46.88869 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 605ee24f-17d2-39da-bc59-08d54f403762 | -10.25869 | -47.5263 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf01b2d0-bfa4-3329-b1a0-776772d2573a | -12.88301 | -48.16077 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bdacb3d-71cc-3e04-a61d-40bfd479b177 | -7.84336 | -47.15016 | 2025-09-02 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 802f6560-a51b-3f25-8640-450816b06362 | -11.64704 | -52.17343 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ce51c89b-acf4-3f37-8c16-3005a02c79f4 | -8.87481 | -45.77718 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 041109fe-c1cf-3fb2-9857-cb550400ae6b | -7.53443 | -45.35651 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 052bf80f-bd1b-371d-b289-cec7859ff649 | -9.10909 | -46.05199 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 377c4b65-3c39-3b0c-848d-99e3f49f804b | -8.46835 | -47.37368 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14e18e94-8f0c-3dd1-bcf9-5792876742f8 | -14.59141 | -48.05722 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4aaa89cc-aaca-3425-b7d9-60716e2a7928 | -7.70431 | -44.60884 | 2025-09-02 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f036b83-e4dd-35f1-a691-90ea1b426059 | -11.65927 | -52.22219 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 18dc16c4-0df6-3083-a1eb-ab038e91e5aa | -13.48508 | -46.92561 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd71976-b5cf-3d32-ae0f-3c9b6f986a8e | -12.78311 | -48.09374 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0658d014-0fd2-39f4-b922-58b92ba34192 | -13.71813 | -46.93513 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7d068a7-b5ac-30e9-b1a9-25fc46ed2a84 | -7.78053 | -45.44907 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb85ba4e-24aa-3b4f-8be4-79cf712b22ee | -11.65365 | -52.21321 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| b3859b0b-b084-37de-a76b-87b90728972a | -10.83155 | -47.45558 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 456c4ee1-5475-3fcb-9f74-ad46d7a168a9 | -7.97842 | -46.45827 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b83ab159-77bf-391a-9c90-f84e93340bc3 | -7.6327 | -46.552 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55a7ac63-a7b2-3ebe-8ac8-2ec8d4c09dbd | -8.8823 | -47.97379 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed2471c9-bdff-34c5-b364-1916d3c98a53 | -11.97363 | -45.88052 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6af2aa65-c76e-321f-a3ca-1e8b357c68ea | -15.02566 | -42.14692 | 2025-09-02 03:51:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f2abf4f-b184-306c-b4e2-1358593d8bef | -11.13613 | -46.34549 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fafe332-c7f4-3b32-9069-982f7211bd58 | -14.05176 | -44.55188 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59bfff7a-160f-357e-823b-fb8675516aa0 | -14.61227 | -48.03646 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1b45e47-86e9-3fb3-b5ce-b7b581513134 | -10.05132 | -48.15069 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 995d6a9d-4af0-3e09-b11a-7befa5acfd3f | -11.64807 | -52.20408 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 52f9c069-109c-31a4-ba6d-783e5d703e91 | -11.97058 | -45.88089 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c96e1119-ec7c-394a-ad7c-39e26db5b111 | -7.70836 | -45.01645 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cb7d4e6-e47c-3786-9fdb-f1888c5b643a | -13.70025 | -46.87569 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bcc50e4-5921-3644-b62e-4a0b5e51292a | -10.05265 | -48.12038 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d91e5361-28eb-312e-b031-9964eeb2068d | -8.8681 | -45.78496 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32b959d2-5bd0-39af-adea-7e52ea6bb7af | -8.1269 | -45.03775 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 985a4ce1-e1d9-3e64-b1bb-57fbb9beef6e | -9.29064 | -47.10262 | 2025-09-02 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959ae88d-9cce-30f4-8ede-323acc912c1b | -14.04983 | -44.54985 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 735a7298-f024-32b1-b6b1-f0a1dcdfe70b | -12.61276 | -48.18826 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9edada80-ea6c-3c2e-a29b-1d4dc4b28ddb | -11.10202 | -44.64566 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd482b82-0e58-318d-9ef7-5a311b26b186 | -7.567 | -45.2343 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ea80dfd-4712-3208-bdf7-75a28c961289 | -11.82283 | -51.54202 | 2025-09-02 03:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c9dff960-97ec-3001-a452-19b9c05e6dd7 | -13.69486 | -46.9313 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8750b23d-f272-36f3-88f1-ee5ef2a21cde | -7.49034 | -47.88271 | 2025-09-02 03:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README24.md)
