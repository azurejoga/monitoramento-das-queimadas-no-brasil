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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89bbcfec-8c07-3f21-9f16-56e6dafc50a2 | -9.58797 | -54.59133 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f74306b9-b5c2-3374-a46d-a06f9e5a150f | -10.62064 | -48.59891 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6db44169-7c66-3c8c-bb74-ead8459ed5ba | -11.51131 | -43.53555 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d914bd63-d4ef-3eaf-b128-d486c2034845 | -13.32323 | -48.15024 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed1897a-1361-31ff-a691-74b804b3123a | -14.72418 | -48.26701 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bb50579-8b40-3459-a329-c97aec5d9538 | -11.19606 | -47.19891 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ddfeaf3-f4cf-36ff-8547-1e264e76bb8d | -9.13101 | -50.77615 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 589ad20a-d2e5-3d26-868e-26d5d123b940 | -11.81574 | -44.9723 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cff6b830-d106-3957-a8ab-fa1f51173af3 | -13.55978 | -47.27689 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 005f95cf-e5a0-367d-a84b-7679cc0892d3 | -11.43158 | -43.4994 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8ab2745-730d-38c8-b775-0e84a4b5bcfa | -11.68675 | -46.85136 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93bba70-4e0d-330a-9e1e-7d4c2390fc45 | -16.08536 | -51.04081 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77e8b523-8451-3584-b3e5-d3aed4fb3147 | -10.84582 | -45.41259 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69ce238c-b50b-37aa-ac8f-ad5e496b8b46 | -12.75513 | -46.88606 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 16dc8e26-43e4-3337-8540-1ab12432c28e | -8.71573 | -50.0519 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3e63670-e19e-3cf3-b6d6-4ae096fef97b | -13.33802 | -47.86958 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6648b9ad-5448-37d7-860d-124e0401ce98 | -11.84541 | -45.00174 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e29c7713-64ef-368d-9b95-6c4bbe613ec5 | -11.42442 | -43.50489 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80b14f86-977a-3f42-b7e3-211378743167 | -12.66216 | -46.87291 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eea8870-5a2f-360f-b735-b9eae63341e6 | -11.59358 | -45.03721 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2716353a-4a76-320d-a0d2-e38ad5a79be4 | -9.41669 | -47.33186 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17036907-a2ea-37ec-a142-3ac99cc73d67 | -14.35948 | -47.13248 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b30982e-bbf7-3668-b306-019b2ce41dfa | -11.22206 | -47.74335 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f2ee4d-98e1-3859-a944-11c864c01ec9 | -10.91128 | -46.56588 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92ea103c-1269-3bde-9b06-d45f56900084 | -16.22055 | -48.8099 | 2025-10-01 04:51:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71914904-0964-39ce-810f-808f08eea595 | -15.31475 | -46.40808 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1107eb78-7b0c-3d14-9cc9-9a6a5ff5f661 | -11.0513 | -47.81964 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c71ed73a-dac0-378b-a201-9b293157df1c | -15.23634 | -48.7388 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4e7646c8-dc6a-3a7f-9717-ce714acf497d | -16.37483 | -47.04872 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0bcdd57-2568-3952-9ad6-9b123e68e066 | -15.41117 | -47.0525 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 629b967f-07e3-3830-8b76-af3e427a4ed2 | -13.81763 | -47.49826 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92e6bd56-3bee-389a-9eb7-d247f841b058 | -10.91111 | -46.56323 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d6c6afa-a20f-3010-a1aa-303ccbb3537a | -9.32068 | -50.62635 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef560554-11f4-3551-ac62-c9efcab67a2e | -14.52822 | -53.11769 | 2025-10-01 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84921ab5-b181-3d25-ac82-e26abbc15a71 | -16.24318 | -44.06263 | 2025-10-01 04:51:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bbbeb1a-7794-3028-8435-4995a8f412b2 | -13.77654 | -48.32264 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8c6d6c83-84ab-3c87-a788-6e44381b6959 | -14.60973 | -48.31554 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b20d6770-3da7-30c3-b996-be9e6fbcccd4 | -14.01956 | -44.81065 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf2a730c-a0fd-386e-bde2-0ac0a5cb56d1 | -15.38116 | -49.19646 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 662c5c15-8ecf-3a56-8817-cac1f75718f2 | -12.17914 | -45.049 | 2025-10-01 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68f9fb25-3dbb-3e5f-b65a-8e514ee6332e | -11.09857 | -47.71819 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9914962c-cb7e-39dc-9670-38e2dba0bfc1 | -9.47947 | -45.50209 | 2025-10-01 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80904953-809d-3a10-b36e-b15b66b8c2ce | -13.41654 | -48.19649 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9cd434a-f307-3aad-a339-9b141704a4bf | -12.37671 | -47.1716 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 325273f4-e56c-37ed-8844-39c157ddceea | -15.22991 | -50.0875 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad662376-39fb-3d68-9b0f-7afdc0c8df1a | -15.35471 | -47.08253 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 730280a4-194a-3e0a-b24c-de217c3a0d3f | -16.01676 | -50.87585 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d18c2f-7e5f-3fa4-93c4-ba7ec2c53da8 | -14.54465 | -48.23295 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4d6f149-54f8-3dd6-963b-22bbe3a0a1c7 | -9.76752 | -57.01136 | 2025-10-01 04:51:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5691a15-4d80-3fe0-b30c-aeca75648a0a | -11.56719 | -50.18892 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86e99511-2d88-31ff-b640-210bcf10b259 | -14.65723 | -48.13479 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be2b3992-4ebf-3dd9-a9ad-bced6f8e8e22 | -16.2016 | -49.99716 | 2025-10-01 04:51:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5af9ea3e-26f8-3c24-9b05-9fccbb14a0ab | -12.24627 | -47.82125 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2b722eb-83d7-3186-a8e0-d0a53a341e6e | -9.43259 | -54.70958 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b496588f-40c5-3d15-b4a0-1b118cfcc80f | -14.49218 | -48.44606 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 710239e8-921f-3198-8bed-65cada8f7906 | -14.36777 | -47.13335 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca9066ec-e25d-31a2-8f1f-f0bd0159416e | -13.91945 | -48.10328 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b5da605-85d5-3455-b12c-0eac0fbba237 | -13.57328 | -47.5971 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2847c099-a45a-3ab9-8a0a-39f559535d96 | -10.07094 | -50.28699 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84a6c05b-731f-3169-a3e2-3a7d01d94caa | -11.46527 | -45.09496 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 512d1988-0e61-3ae2-aaa7-66c7d36523a9 | -12.84225 | -46.8744 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 420c240f-5551-3c6e-bae3-af8847c600e6 | -15.15237 | -48.00714 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 649bc9e5-a132-3b2d-8d75-101120c70c8d | -13.91621 | -48.09768 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b512100f-596f-3eca-94e2-bde563157e28 | -11.2758 | -47.81072 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b64ba3e2-259a-3a5a-964c-2d8bbb83d23d | -14.75157 | -45.77846 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ffd3a8e-bf42-3b51-ad32-8030b23fa184 | -14.59495 | -48.21857 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a46348fb-1b7b-3aa0-b043-e33a0ee6bff1 | -9.56901 | -54.58116 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2dff032-7ea4-3b73-9443-8371008a0a18 | -13.75853 | -47.93433 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 009405dc-9f76-3a7c-b856-5a15588d5174 | -12.77243 | -46.91573 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c153c79c-f4f2-3ccb-b450-1fa2826c2686 | -11.2648 | -47.20862 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca6f4001-fee4-35c6-8704-74ebdc0b6b37 | -14.3943 | -46.21354 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2ad9551-af13-32f9-8806-e8b427e41a22 | -15.23817 | -49.721 | 2025-10-01 04:51:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07f5e51e-7f12-38ab-84fc-566efe58f66e | -11.84339 | -44.98099 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 010528e5-992f-319b-9710-cd6dc661164e | -13.38409 | -48.08441 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e47089d2-a5e8-35f6-a76f-be5bc7161d1b | -12.82007 | -56.55668 | 2025-10-01 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| badcaf54-7336-3796-b211-d4826816c0da | -13.7716 | -51.22682 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a32f74f5-c092-3176-8ed7-b783ed24b77f | -11.82847 | -44.9486 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f56895bf-c5b0-3d3c-bd1f-0433c82520a8 | -11.76551 | -46.87231 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87426786-a57d-350b-9f11-965c4c43d488 | -16.19857 | -49.99227 | 2025-10-01 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7fc1ae1-7202-3dd2-bdff-c5e51cb3bb6c | -10.72914 | -48.17937 | 2025-10-01 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54486d80-c967-3d8b-a447-b02b2fc533ee | -9.44146 | -45.48635 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00fa1ced-db06-39c6-92d9-9d453a1b505b | -10.4868 | -49.36595 | 2025-10-01 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 642a1bfb-8029-3106-a5e7-0f9bea5e4e1e | -13.32782 | -48.14592 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19dc89a4-5599-344e-a05c-59d3b7ff7205 | -14.23656 | -49.79303 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a41da73-8b1a-3f50-bf74-e5664501e22e | -12.1543 | -47.76931 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a545050b-8642-34f1-888f-810369650c28 | -13.41584 | -48.20155 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a374244-66a8-33be-9a3f-7730ccde8360 | -10.48949 | -51.51917 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6781955b-d8bd-3039-898c-5a47d1214ade | -12.69934 | -48.5693 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f798538d-ca51-3096-b2a6-e9c17f3d30e6 | -9.40032 | -54.70415 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44318ff7-6cf8-3d31-8373-0fd4f888b4d7 | -15.77324 | -43.70128 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 702297be-e26d-3d55-9327-e9da01010151 | -11.79236 | -47.5996 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 606ba004-c19b-33aa-8cd5-4dd60f2ffdbd | -12.91894 | -47.16304 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c703bb7e-a5e4-36ab-9aca-004c27eb50d9 | -13.33091 | -47.83271 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba27d3ce-c999-3ea7-aa62-75027ac1ae7e | -13.33242 | -48.14157 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5c455da-bda5-30b1-8961-e547a6041352 | -16.02319 | -50.88086 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569f8508-f152-3a04-a74a-6cc0fff4fd29 | -13.10533 | -47.0256 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af04de34-9eb9-323c-88a5-98e8f3cc2a10 | -12.42545 | -50.18128 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69712678-a12e-3e4f-8f08-9b57cd9391bf | -14.52766 | -53.12125 | 2025-10-01 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee977c0d-d2d7-3481-9c55-dc396e1f5924 | -14.98267 | -50.76861 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de3f996a-626d-314d-a998-85be57d4255a | -11.14911 | -54.12113 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README99.md)
