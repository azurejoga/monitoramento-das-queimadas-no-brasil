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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 102aada5-5f57-35ed-845a-c05885a597d0 | -10.13207 | -58.2205 | 2025-06-21 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5882653b-5919-3684-b68d-2381f6ddc752 | -7.15703 | -43.20902 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d483c853-0345-339a-8278-2ecfce34d3fd | -9.47387 | -57.82708 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e475fbb-4fe6-3056-99a7-e5ebcf779637 | -10.47445 | -47.0313 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebb055bc-61d2-36dc-9318-33950818578e | -9.47881 | -57.81949 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb468786-0e63-3db6-99c8-0c7ad985d6e9 | -10.50749 | -47.58276 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c88e69-e27c-3e5f-8f1a-c490beb6bdfe | -10.15592 | -48.98864 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aecf6c86-3b6a-39c0-92e5-346ae35f7389 | -8.70601 | -50.04706 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3051dcd3-a278-391d-b5ec-66e38979d106 | -10.45381 | -47.03386 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 785c081f-b907-37fd-83bd-a7f4b4971eb0 | -9.35505 | -57.01254 | 2025-06-21 04:59:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 486c326d-8a48-352a-8cf6-18b8fd277e2b | -8.50453 | -47.44556 | 2025-06-21 04:59:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e79a53f-66ac-3bfb-89fb-5dcf9366f1af | -9.09808 | -50.03318 | 2025-06-21 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f435fed7-c73c-3810-91d3-f396aa74c834 | -7.28189 | -49.99168 | 2025-06-21 04:59:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a016229-4503-366a-9d75-c0152f30cc97 | -8.98178 | -49.86785 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d79f6e90-73cc-3e1f-90a5-37a15fdc1c6d | -10.15158 | -48.98799 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4551bfcd-b4cf-37f1-9f92-c3b3391c3071 | -10.29887 | -57.13706 | 2025-06-21 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1402b04d-de98-3432-8ae1-36e1ebcd47e8 | -9.5991 | -56.28394 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e17c2160-45dd-35dd-b9a1-93088b32b695 | -7.22401 | -43.07036 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5eea7dd7-b76f-357d-a806-2516432487f7 | -9.09883 | -50.02799 | 2025-06-21 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57ea5299-6a91-3165-a5fd-587e664c3d5e | -9.37058 | -62.04429 | 2025-06-21 04:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b367f83-137a-3343-bd26-315821b0a1f6 | -7.97576 | -55.29523 | 2025-06-21 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb880e39-6a37-3196-b474-acf6bb1a43ee | -11.25733 | -47.82343 | 2025-06-21 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12ac52fa-a265-3931-93ec-9c1531c784b9 | -10.5274 | -47.58033 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f579e8ac-c143-364d-a5b8-73080a32d5f0 | -10.86261 | -53.75514 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45623b86-f1fd-3389-bd7b-b56e6a97f6ee | -9.47318 | -57.83117 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| efb04e55-d33e-30cd-bc36-d0c12a0366e8 | -9.91671 | -59.91042 | 2025-06-21 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3ab9633-26d6-3847-ba9e-edf69ce4c36f | -10.44309 | -47.03817 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60bd5c31-209d-39fb-af09-08fee0db9eb4 | -10.86489 | -53.763 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2ca2d9-6b0e-3e3c-80b8-1de9b00b7d1e | -9.09958 | -50.02284 | 2025-06-21 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20e58727-44d5-3d8c-b46b-88aa8e00883f | -9.48123 | -56.07974 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7195533-6ec2-3802-b60d-18df8ba3834a | -9.48459 | -56.0803 | 2025-06-21 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d55504a-78af-3b21-aca9-fdddb4fd0488 | -12.26537 | -44.59999 | 2025-06-21 04:59:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e92701f-02d6-36a2-876a-a32bb98873cb | -9.01809 | -61.21978 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1adc79-b4ff-34bc-97c6-cb91896daa1f | -8.70205 | -50.04649 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34664fb9-98a0-3363-b0b4-9c5352b5ade2 | -7.27172 | -45.3642 | 2025-06-21 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3039ff9d-6dcd-3d3d-90c9-ec627e01e30e | -8.19762 | -47.7729 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5a128d7-1d50-3eb0-befd-d77fe1191e5a | -9.45902 | -57.84983 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e41e0ae-9e29-39a3-93aa-9b1c1660001f | -8.01767 | -47.66062 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01703d7b-c243-3c4a-9d47-3800245503d8 | -9.47524 | -57.81889 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ec3f2bf-377f-3b05-a90f-f0cccdef4d67 | -10.15438 | -48.99001 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e7caad3-d81b-350d-acf6-f02d1259b9ff | -9.26583 | -57.81913 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b76a89-0fe0-3ea9-9c99-bbb4835c94ac | -8.00781 | -47.66394 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69acd974-a462-3eee-a4f6-fa5eebcdfa72 | -10.15497 | -48.98589 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c09d136-9168-340e-be95-4ea117a59103 | -10.5178 | -47.57891 | 2025-06-21 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ae953d8-c1fc-33e7-b839-225ad3e8a5ed | -8.18357 | -47.77351 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccbcff75-7e9f-3124-ba7f-c99874548abc | -10.95296 | -49.25655 | 2025-06-21 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efc386da-bdf6-3906-96f9-bea39ab94d8f | -9.45683 | -57.84103 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6340c7-888f-3056-b9bc-29ca3412dc5a | -11.20683 | -47.83757 | 2025-06-21 04:59:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83c3b5ec-e538-37be-8801-5bb8788427c5 | -9.26263 | -46.92964 | 2025-06-21 04:59:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44dfe2a4-ab1a-340b-94a2-8b6ac3dc7828 | -9.47744 | -57.82769 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89bc27c2-2f4b-3fb7-9dcf-6377e3fb223f | -10.47368 | -47.03712 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc1cf2bd-4810-3f37-af48-abcd3378bcc7 | -11.28502 | -46.65216 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0be0672-0f85-343d-afbe-bc5a89183135 | -9.33146 | -47.8276 | 2025-06-21 04:59:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eea964e6-6980-3123-bb00-68b0277095d0 | -9.47469 | -57.84407 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 51b063d7-e97c-381e-a638-0e743476a0d3 | -8.01241 | -47.66463 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16334ede-9117-36e4-8dde-ccb81dd2886b | -8.73527 | -47.98893 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c876b95b-7d17-3c5e-8acf-8f8ff01a469f | -11.79595 | -49.5237 | 2025-06-21 04:59:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a7da65-fe51-376b-8e10-429e07177eb8 | -9.47455 | -57.82298 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4f3c79a-0e38-3695-9266-2532e03678c7 | -8.18323 | -47.77558 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7c8ec26-cb97-3c86-922e-55d843f76494 | -7.86977 | -47.8837 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1849cd9-e8d9-311c-aeff-fe807c05c205 | -10.36913 | -57.50687 | 2025-06-21 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1428d9f4-6438-3a0e-9c6d-b19c99af1148 | -9.01657 | -61.22839 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08fa3e90-2b9f-3f54-8f5c-425fd7d271b3 | -9.48351 | -57.33366 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b78dcb12-3a34-3a86-816f-4f2bb22dbb9a | -8.37153 | -46.97208 | 2025-06-21 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61d412cc-63fe-3e79-9534-dd9de2c89974 | -8.18289 | -47.77818 | 2025-06-21 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8479b187-958c-3a14-a6b3-ab0519ae5ea3 | -6.02148 | -48.21012 | 2025-06-21 04:59:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b757cd-b51c-3f17-8f41-6251f48edf7a | -9.48032 | -57.83242 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df64f59e-46aa-35df-8316-e950cb2eba13 | -8.70498 | -50.04427 | 2025-06-21 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6101b68f-e024-38cc-8ab9-eb6b4bc94b73 | -10.58376 | -46.93079 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79febaa3-af90-34d1-b8da-46c99ff2b78e | -10.9603 | -49.57148 | 2025-06-21 04:59:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d05b456-19e6-37cc-bdba-b1ca3175c556 | -10.13568 | -58.22111 | 2025-06-21 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f83c5087-365c-3c71-8cd2-b2fb09d5e744 | -11.10438 | -46.68725 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 62f08054-b1ee-33c8-bed2-141baf7c2356 | -7.22958 | -43.07605 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 068c3e9c-feb6-3f41-95e2-ef419596d35c | -9.2577 | -46.92889 | 2025-06-21 04:59:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| decc423b-c9c8-34f7-ad2b-ccb995e798c9 | -11.14472 | -53.93751 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edace858-dd3e-3b35-a4f0-f0b9c19bc630 | -10.86829 | -53.76352 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93b9006-9ead-3bf0-9fc7-71eb0a0b8ff9 | -10.37161 | -57.50745 | 2025-06-21 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd7b94e-a791-36b8-be2e-9b0372b87d5c | -11.93871 | -48.42428 | 2025-06-21 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 091458e5-256f-383f-8771-c449899dceca | -9.39599 | -63.2642 | 2025-06-21 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a71382fa-bf72-39d5-848f-425a940f01f6 | -11.17323 | -46.6562 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b143aa20-9fab-3a3a-9720-49a370a024ba | -9.02615 | -61.22562 | 2025-06-21 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69b4b6b-9e9d-33f8-9d14-ce51d5c7da58 | -7.21459 | -43.06244 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b8ed0423-5498-3dbe-a173-0d76e6ca9fa1 | -7.21783 | -43.06935 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a78ebf4a-38e5-3766-950c-73a82074f68a | -11.2854 | -46.6492 | 2025-06-21 04:59:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75789aca-08a5-3403-ac25-d56a20158f5b | -8.3852 | -55.444 | 2025-06-21 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b604162-f9eb-31e4-8eee-481ed418afe3 | -12.25884 | -44.60367 | 2025-06-21 04:59:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b64a46-9d73-35ad-922e-476788b691eb | -10.02947 | -54.32279 | 2025-06-21 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f4ffa61e-a529-3a89-b875-0e18e0d6a8c4 | -9.26132 | -46.90766 | 2025-06-21 04:59:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45a56d6f-37d6-3abc-aa89-44c2098803ed | -7.23583 | -44.67693 | 2025-06-21 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9516f31-abb7-344e-85dc-ee4b92549dc3 | -10.15102 | -48.99213 | 2025-06-21 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d525898d-25a9-3b57-9183-e80858ea7325 | -9.9207 | -59.91116 | 2025-06-21 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f350821a-d59a-385d-9acf-de70e2dd4955 | -9.47675 | -57.8318 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56bb10bc-77b3-3cef-9855-622720171378 | -11.93797 | -48.42103 | 2025-06-21 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bd568cb-8872-3b20-847d-a3fae5e6a4ec | -10.52368 | -53.62096 | 2025-06-21 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ad61754-05c4-3639-9170-30099ab6969b | -11.17282 | -46.65934 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e93f7f7-402c-37d6-85c9-a2e3b5e0851a | -11.17364 | -46.65308 | 2025-06-21 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ef86eab-9ae1-3da0-b92c-e79aa7325232 | -7.23019 | -43.07135 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 77753aff-276f-3a78-a4b1-249813c6736c | -10.84986 | -53.76888 | 2025-06-21 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7915aa06-88ce-30f5-8dfc-1756c2e8c9d6 | -9.46398 | -57.8422 | 2025-06-21 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ebf3a8f-3a73-3863-88cc-20b95c7c5b37 | -7.15766 | -43.20439 | 2025-06-21 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
