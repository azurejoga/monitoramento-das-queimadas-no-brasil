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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b59fff97-ecc1-3ebc-9547-cdd28c855f05 | -11.20506 | -51.23665 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 32315ac1-6c9a-3610-bb5b-a68a1b1c22d3 | -8.60311 | -54.71913 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0a12a12-2204-3802-a218-fbbc9fa6bd5b | -11.76956 | -54.51663 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab6ed4ce-705d-367e-ba04-6687f42135a1 | -9.22496 | -51.53258 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f244825b-404b-3a83-ae59-56566f5601c4 | -11.81418 | -47.20121 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f6c925e-70a0-332a-a7f5-2d512d4f6a73 | -9.23159 | -51.55594 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ed596c9-769b-3e7f-9b9a-06a068f45810 | -9.66305 | -55.08673 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f98797ce-5c32-37cc-8075-ac8391d0930e | -13.46024 | -54.01906 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1e758f0-0975-3cc2-bc72-edd398e33f38 | -8.59651 | -54.7804 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ec2a7c5-aaae-31b1-8922-32031040eaaa | -11.20895 | -51.23367 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e5bd894-150b-3eb0-92e2-18b2624733d4 | -14.17394 | -52.82132 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 020691bb-a87b-3301-a950-3e22efa80369 | -14.89179 | -52.59886 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85fc5175-9c6d-367c-9a1d-104a995c8e98 | -10.50426 | -64.52424 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 73d7207d-bb30-32c6-9bef-cdf017b1f150 | -14.93052 | -52.60139 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b115f492-8cf9-3727-92c5-f85bab77e739 | -11.51446 | -58.51408 | 2026-08-28 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 698280d9-f084-30de-8f20-8e3b5497f2b6 | -9.45489 | -51.71095 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce40208-2707-3cdb-8a0c-bf92e789fc3b | -10.92669 | -50.53744 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eac1fae4-071b-314e-9a29-f01311bafd47 | -8.59126 | -54.76375 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5272909e-e51f-3ee8-88b3-34bead50d3c5 | -8.94684 | -62.39576 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172d56c8-075c-3037-84f0-15a20b518207 | -9.21471 | -51.55311 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1a6bf1-1920-3a26-b5bd-ae0e03c6d52a | -11.21753 | -53.99761 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 327bfe82-33a0-3f79-909d-0fc4bdd2f25e | -8.77392 | -49.94747 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf9c075-e020-3196-9453-746da2852908 | -10.4986 | -64.51579 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 68c4fa2c-a8ae-39bc-b65c-950b1c1750ec | -8.94815 | -62.38889 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0939cc87-c966-3b6d-abfe-2c1a131ac25a | -8.94019 | -50.77002 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf09f19-6d0c-3a5f-9eec-5666f8361fed | -10.78616 | -54.02702 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e26efe8-919b-3be2-b679-06cf8df8df0d | -8.77785 | -50.07325 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6add0354-e937-39a0-ac87-da3e88230e84 | -11.53898 | -45.51322 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56b36d72-a07f-3612-8501-168b562ce98f | -14.40103 | -53.05546 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b86c9e94-9e7d-3ac6-aa1f-398f6c7151ff | -8.09426 | -51.65401 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2fc7b4e-fa83-3bd1-bcd4-05db189e879f | -8.5877 | -54.78417 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b1cce04-c437-3cf5-bbcb-afc9eb6bf985 | -12.4321 | -43.41654 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 82ccde38-7c7f-36b4-b402-6ec9b109b803 | -8.59609 | -54.75945 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0ea2ffe-8d42-342f-9462-476e3facf157 | -8.55152 | -54.71832 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7820578a-b301-3b84-8feb-70d3de43edc3 | -12.7663 | -44.2672 | 2026-08-28 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09523e50-5845-3f73-b528-8e1820cfc02f | -11.48822 | -45.11564 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff07b091-2214-3a7f-a45d-56efa23b2aef | -13.4246 | -51.86977 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 370a00fd-8100-3412-94bd-7c63ec48809f | -10.75789 | -54.04662 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3c6b4db-2790-3a12-bba9-a01e739627c5 | -12.77655 | -46.44487 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a45c9f0a-28d6-306e-8f09-af2d3c2278fd | -11.97609 | -45.49155 | 2026-08-28 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6017a8c-9496-3123-871b-60cb1eccfba6 | -8.80552 | -50.04908 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad3709d9-861a-35c7-8fb7-7e96971f99ba | -8.21916 | -54.95951 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26c5a348-aba6-3b00-8d49-8adc6ffd626a | -14.42481 | -53.37445 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ab1d69e-3f44-3f43-a4b4-bbf15011685f | -11.76509 | -54.52043 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24f20bc1-f494-36d6-b37e-7cd55e52c0c1 | -11.19619 | -51.22793 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2d95b63d-2345-37c0-a92f-5a3b2e3e8d28 | -11.46606 | -46.94739 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c00516e-7719-3985-b33b-3bf6168d3a7e | -12.77976 | -46.45046 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7275a0c0-1061-3521-9291-cf3c78b31095 | -11.21721 | -54.00407 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e514aec8-6c3e-39ee-ae86-8c797e64dded | -11.23137 | -54.0045 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a75100d-0487-3c46-be89-f65bc55bdaae | -11.53333 | -45.52369 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3645b4c8-9bb9-38ea-bc19-245b185236bd | -10.99527 | -49.62844 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 483fab9e-49ef-36d9-8022-a5cec662cff4 | -11.67262 | -50.46693 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 636b22bb-5196-3b63-a9f6-09d0741e3edc | -9.16245 | -49.974 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0f64cc4-aaa6-3144-a7a2-e8cca41b5beb | -10.77289 | -54.03814 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d01756f-cbd5-3187-9bf4-a7fa0817ee7d | -12.23672 | -50.57589 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cad06d18-c165-302f-92e1-cbeec9052924 | -10.75641 | -54.03289 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c64d5743-a202-3bfb-ab87-ac930b705bcc | -14.58588 | -53.16419 | 2026-08-28 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f180985-a864-3f87-947c-3ce8e3fbbec3 | -12.28939 | -50.58809 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5b0254a-01c4-3f3d-86a9-914299fd5093 | -12.42799 | -43.41078 | 2026-08-28 04:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 74b375a2-d00d-386d-af02-331f69c29051 | -14.97379 | -52.59 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 639d398d-c25a-3fbf-a2a1-3b3b85a24293 | -10.55044 | -50.48017 | 2026-08-28 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3bead75-f94a-3fc8-bf9e-88ecd1169fe9 | -11.57124 | -45.54725 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c6a3332-66bb-30d4-8de3-03bc83caa4b3 | -14.14777 | -52.83209 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0accdaf9-b802-3d13-92e3-9d60a713d247 | -13.41104 | -51.40692 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1b818a56-6d5b-3822-8451-ed5c73b1de12 | -11.9802 | -45.49218 | 2026-08-28 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15d46e30-08ca-324c-9957-9f89fb2dedcf | -15.5254 | -41.92954 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9a3626c5-53f3-3481-a786-dc2f8aed94a7 | -11.37619 | -45.14659 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ac0001d-63cb-37a6-87ff-84b2dac41502 | -12.69341 | -48.43096 | 2026-08-28 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72bf04c0-dd35-30c7-9a5e-0d0bb04d0f24 | -6.75137 | -55.68548 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22d3b13c-f967-3c40-b2ee-5e9076ab843d | -13.47468 | -57.04462 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e843bf1-ca56-3f46-b6d9-d875fd2c50d7 | -9.22834 | -51.53311 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f95a392-8e5d-3588-b6b8-48de85b4b3d8 | -14.89515 | -52.59944 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b12d977-62cb-3a38-b5a9-de5e9097421e | -9.22366 | -51.56211 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e0d84f1-55d5-327d-a264-15d80f669d31 | -10.87948 | -50.5192 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e321fc5-c4c2-3cbf-8ef3-8207e3ac5a5d | -8.79334 | -50.03997 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42c7d13d-4c33-34df-8361-c256b7a3d272 | -11.01295 | -45.07724 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd51a47a-b862-3544-9b78-6c1389bb1a8d | -10.78867 | -53.99811 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99b4a70d-190b-3d68-9daf-fb8f91e188d1 | -14.88111 | -52.60082 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0336cd45-bed1-3000-a571-2a72ba75c11a | -9.46218 | -51.5815 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d48c8d88-d9c4-324f-80b0-be90db35d4dd | -11.47095 | -46.209 | 2026-08-28 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 073a723b-b4eb-30c0-8d8a-258547a23bdd | -8.78117 | -50.07378 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60daa7cc-25c3-32af-a01d-ca004ff12b09 | -9.21412 | -51.55678 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeb265b2-0196-32c6-b125-32fa6fa56587 | -11.00368 | -49.66275 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae5ce1a8-c331-3938-b9b4-bea67cb63dad | -14.94119 | -52.59947 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a61d0ef6-fb17-354c-af78-9d4f920d82d8 | -12.78369 | -46.45094 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3dd9364-58e7-36fc-ad8f-4238a279d7d9 | -8.95223 | -62.40242 | 2026-08-28 04:51:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64789153-29df-39b4-850f-fef9d404cb96 | -8.11472 | -51.65742 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17eb43af-66bc-3588-91a3-6878dc618ed1 | -10.96441 | -50.29848 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ca3599f-cf46-362f-9b1e-1df8ce242fc5 | -10.0636 | -46.94132 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab04666f-0568-3385-bead-f58fd4d118e0 | -11.28025 | -54.02632 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c1e6a00-6fd8-395b-b4f0-8a09f099f3a3 | -8.59065 | -54.75122 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 232255a9-91df-3e56-b0f3-78408244323f | -14.29633 | -47.16345 | 2026-08-28 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98122232-64fb-3662-88c4-d8a0fda7f02c | -11.27806 | -54.01708 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b6a5924-a014-3ef9-909f-10531a5b7093 | -8.78172 | -50.07029 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e799d52-3110-339e-899b-b3ff6258d3f9 | -9.61853 | -55.11974 | 2026-08-28 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ea833413-0209-3d55-8bc4-e24a312f07d0 | -12.25724 | -50.5756 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 90303906-e093-33a5-8298-327b3fc2defe | -10.38946 | -61.24322 | 2026-08-28 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 836c0c3a-6f84-3a0d-a27a-570788909330 | -8.55546 | -54.71904 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d90da5e2-1bc6-312b-add4-d49769586420 | -14.40041 | -50.12266 | 2026-08-28 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2a2de97-8559-38e1-873e-5c1f58ae17ef | -14.40825 | -52.58818 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
