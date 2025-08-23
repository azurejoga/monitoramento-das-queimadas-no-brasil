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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2e76da8-bb11-3b80-87b0-edd76c21decf | -7.76288 | -61.0376 | 2025-08-23 05:21:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d15e79-7149-3221-91a4-6ef9730f4d18 | -13.4822 | -46.90334 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85b4b4e0-7183-362e-9e51-9be1ca3e59a4 | -9.19946 | -59.44407 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828569b7-cf21-3042-9584-2db43cc3960a | -9.82499 | -64.27313 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45f94f81-7812-3d6a-b61b-1fe3d0b5e0e6 | -9.51095 | -60.50783 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aed21a95-c26a-3552-b97d-62a046dacab9 | -9.52265 | -60.52072 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af2e0b56-3bd9-3f4f-ab0c-1e596b559cc0 | -9.17074 | -59.60422 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95df97e7-9fcb-3daf-83f7-087d89ff761a | -14.26472 | -58.53484 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6139dc8b-4d7b-3938-8c11-ef4bb2472760 | -13.02433 | -56.83966 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb017bbb-f8cc-3658-9972-c4de650515b8 | -11.1905 | -55.01975 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 751b441c-c5ca-3bae-98f8-0f97c05e052e | -14.25664 | -58.5415 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b87ced4-9db0-3ec8-b92b-090d85715433 | -8.89701 | -62.4314 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 576367a0-8dd5-3c59-89ed-ac0e1bd7f83d | -7.81804 | -63.55665 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2650c4d-1133-3090-a460-68017192df87 | -14.88142 | -47.96462 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4c6bab0-ba1b-31d1-938f-38e071a3d0f1 | -11.6108 | -62.29797 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b933b140-3c35-39fb-8ba3-2214942403e4 | -13.12716 | -46.90237 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11b7bae2-c5e9-3fb2-8621-7f2a400a713b | -13.02498 | -56.83524 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14b908bc-5deb-37da-8b04-0e1a1ed7629f | -9.95719 | -60.19121 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 25a50eba-fa70-35a0-996e-cf63a039126d | -13.4678 | -47.0341 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93e3422e-7749-3375-92ff-e3096dbc5f79 | -14.67181 | -54.87099 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dd1bca5-a86b-3496-982f-0accd521872d | -11.20027 | -55.03721 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84eb99b7-49f5-342b-8474-1fa6828c8401 | -9.15856 | -59.68105 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af97c200-c910-320b-a014-c570f694faf5 | -8.59253 | -62.62171 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f9eea95-f30b-3dfd-b372-02922b49cf44 | -14.94763 | -48.01376 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 395ff167-e1f3-3700-ae37-b3d563b19a5c | -14.66756 | -56.58931 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8202641-4fd6-34b9-8f9a-c26160d667e1 | -9.4634 | -60.37604 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fb0e56a-c3f9-3a4a-af48-83c2aacfdd06 | -13.68593 | -57.75797 | 2025-08-23 05:21:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5acd5a02-ced0-3bd0-a9c4-bb68f7c303fd | -7.56642 | -61.37915 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67c8866e-009c-3cd5-bde2-66df480e7102 | -11.51283 | -50.47463 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 006da97b-e460-38f4-a7f5-9fde021d7ee5 | -9.51594 | -60.51963 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecd0eb6-a436-324c-b456-7a0dd43a6e28 | -9.51023 | -60.55532 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 149e63dc-51d7-3395-ad69-09db62614c0e | -9.15284 | -59.50838 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 964527b4-589b-3df7-9efb-83aaf35928c2 | -9.1713 | -59.70819 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eb06de0-bdae-34ed-aeb5-f425bac5f069 | -9.21395 | -59.63265 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82380002-0309-3d10-b0a3-cc47b5d61a06 | -13.02325 | -56.82141 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d5bac47-90e5-3350-a60e-88d089538380 | -14.66439 | -56.58407 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3c047a8-041a-3995-b477-9046500e4ba9 | -8.59617 | -62.62233 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc42c2b6-d2c0-3883-951f-8f329a1ad2ba | -9.21167 | -59.47467 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f66c52-13bc-33f3-9401-c10419b76443 | -13.38505 | -46.21311 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc9af904-24b2-3259-bdf0-84d81fd5cd20 | -11.31665 | -55.2038 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5617fe-bce5-392f-ac0d-b1d89106e12f | -14.67771 | -56.60039 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f343ee60-db09-389e-a8e4-9b6951c62780 | -9.18736 | -59.62838 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa38db4e-7a58-3323-a9ae-48d54be6c847 | -7.10328 | -59.77603 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b51ed95-cacf-32a8-94e8-acc888f56682 | -15.54909 | -51.69486 | 2025-08-23 05:21:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ff44965-2c16-350a-a4d0-413b05c55d2d | -8.88584 | -62.40476 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f746b2-d643-34b1-aba0-9f28409f7cda | -14.30328 | -58.52446 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bf1ef2d5-9513-3b1b-874b-7e2528777096 | -9.83286 | -64.27454 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 598f76da-b5a1-3d96-b7c8-a1ed116c0751 | -15.69566 | -48.09232 | 2025-08-23 05:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a278b651-d277-3e64-8879-08e57b4039a5 | -9.19891 | -59.44756 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b061e8b3-ea68-3fcf-b02d-120dffecadd6 | -13.12888 | -57.11413 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 366564a8-fd20-35aa-b673-9ff5ea6b9647 | -15.07176 | -48.51206 | 2025-08-23 05:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b4f83cb-a198-3f94-ab0c-5376c301adf5 | -9.24719 | -59.61648 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 493bda66-375c-35ca-b017-c0f77fd4fe7f | -7.43774 | -60.6297 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 677d3661-274b-3e03-890f-2680bb27cfff | -13.45534 | -47.02333 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c646e35-39b9-36d9-8899-21ee0c045251 | -14.62397 | -54.84034 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f63a74f-f023-3341-bcce-a413cf023aea | -12.70831 | -48.10112 | 2025-08-23 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6dab1ca4-9004-31b0-b0ab-57bb67ea9b47 | -8.87728 | -62.41186 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b9910e-545e-3514-83c7-f01031a3aeff | -9.20943 | -59.44566 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb2e7c8-8f7e-36b7-bb5f-f9c8cce6c3b9 | -14.73572 | -56.03076 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2de7133b-8304-39dd-9009-ff417bdfa63b | -14.67324 | -54.92426 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89c4a6b8-54cc-3fb6-bd60-858acc2891ba | -8.89976 | -62.43267 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69595e3e-90d6-3c40-8f4d-236bb49aa8af | -9.17962 | -59.65577 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40586e49-84f4-3985-928d-4ca9ac0f4e42 | -9.18128 | -59.66678 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 166d393a-8fcd-3598-9aa9-e5519e4f1279 | -9.16963 | -59.61121 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4787552c-471a-386c-b024-0de859474a73 | -9.18183 | -59.64178 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaa28164-8a82-3c93-8015-e1717b0237e6 | -7.29972 | -59.62374 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9463e8a7-c7e4-3032-9c9d-35362ca55358 | -9.25212 | -59.62437 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d4abfd3-74bd-3e24-9338-fd391af1cc66 | -9.26008 | -63.34324 | 2025-08-23 05:21:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c582620c-e0e4-3544-bed4-6a014699e9f6 | -14.75526 | -55.40602 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b19ce84-3331-35a2-b73d-8e83d59a7a92 | -9.95053 | -60.19013 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8449aa58-a9a6-39e1-82e8-1e3d2ee538df | -12.70133 | -48.10495 | 2025-08-23 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9edceb3c-516c-3814-982f-42fce0ff9bcd | -13.03275 | -56.87461 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27631c7d-d990-3feb-a52a-328a0f12ba5e | -8.88944 | -62.40536 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbfab45-7dd9-3c3e-9ef4-96975872513d | -9.21542 | -60.78426 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae0f0f3-db9f-3ca2-976a-f2472911d88e | -15.02451 | -54.8877 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63f3ad1b-a4a9-395f-8a29-ea82377633fb | -14.67605 | -54.87159 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5914ce2-e23d-31e7-bee1-e0d40de6e093 | -14.92096 | -47.32328 | 2025-08-23 05:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aab4a4a-b8a0-391b-86df-dee61726d67c | -9.22828 | -59.75316 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76bcd8fb-f571-31cc-a9cd-ce37a922cd86 | -9.25101 | -59.60986 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab2636fa-f6df-3c95-bad2-1200d66ff19a | -14.28433 | -60.38385 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6d2f697-4ee8-306f-9a7c-c1452f2229a3 | -13.03642 | -56.87518 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 459f7442-ad04-386a-be69-4f081fbded07 | -9.95831 | -60.18418 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dd05e4ef-b60a-3959-891b-728e6a0ec23c | -9.15852 | -59.50914 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 392f42c9-f40d-3121-8637-2d56bc478c5d | -9.20113 | -59.45507 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f6648e0-31b9-3c3e-a316-5451e28a205a | -8.65959 | -51.27919 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91c5a738-07cc-327a-9fbd-8bb405f842ae | -7.73315 | -67.07355 | 2025-08-23 05:21:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef7fc99b-4014-3652-b4fb-50a22e022bdc | -14.37971 | -52.05917 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acd3dc27-fb4b-3c29-9439-b21cccf7f117 | -7.05806 | -59.82291 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06d0e80-b346-30cc-b27f-a85979403ec8 | -13.38169 | -47.51935 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f06e6ead-04e0-3c8c-845f-1acb5ec8ee90 | -10.41078 | -57.68106 | 2025-08-23 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0823d8b-8a24-3799-a6a3-5638f7d2bc8b | -14.66384 | -54.86589 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba6eca6d-6565-3cd2-a69f-a0a687febb47 | -8.89683 | -62.42791 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ab0500-65e1-35d7-afb3-a601601db210 | -14.66013 | -54.86133 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2cf7c30-5431-3235-889d-0f82d05f0419 | -7.62584 | -63.48386 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6107e63-3f1b-3236-a9db-a6a79b3871e1 | -13.37619 | -47.50703 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c202d0bf-7b5d-3a82-bf80-46a135b1680f | -12.94178 | -46.30596 | 2025-08-23 05:21:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d53a8212-14d5-38ee-94d2-aa6a2ae03922 | -9.52479 | -60.55037 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21dcc7ec-5d25-382f-a702-b392bdffeff1 | -14.61344 | -54.85464 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b210cee4-83b9-3ecd-afa7-d04474ddd9d4 | -9.21222 | -59.47118 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2697f01-707e-38fe-b63f-5f0c060b61c3 | -14.82807 | -47.95859 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
