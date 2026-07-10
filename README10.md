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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd293fc4-63a1-37b3-9fe3-57fafdeccf00 | -12.15805 | -57.2237 | 2026-07-10 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d318019-29cc-333f-9ad3-f9078ec6ad1c | -8.82868 | -48.33077 | 2026-07-10 05:10:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60b50857-f25c-3345-8e81-e120008cfb03 | -13.27183 | -45.14393 | 2026-07-10 05:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8032146-79b5-3bfa-8749-52da73a2128c | -12.84837 | -44.35192 | 2026-07-10 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14023d40-bccb-3011-9f51-17123b36671d | -12.49541 | -43.76512 | 2026-07-10 05:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2438b6d0-c5e6-375f-83a1-73ae55e9062b | -12.45141 | -49.58552 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b682802b-f765-3deb-9c07-f28cdfe3fc31 | -10.12541 | -50.1843 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d917254-1a00-3a80-97eb-2e7f3ea9d2ce | -13.30482 | -54.34449 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dea1c73-67f3-39e0-8080-df2168cc14f7 | -12.16559 | -59.76062 | 2026-07-10 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ef1e216-55d3-3d92-98ef-6fb50e643c5d | -11.27778 | -55.79193 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd4f18cc-84f7-3622-8931-6e8f7bf7393f | -13.31164 | -54.34558 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99cf7178-aff5-358b-8272-8bdde84c71fa | -10.40438 | -61.21428 | 2026-07-10 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7197c3f8-e156-3f61-b11b-008289f48d0b | -14.08987 | -59.45621 | 2026-07-10 05:10:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e335d817-b712-3f03-8f72-948147f84f8d | -12.50061 | -43.77643 | 2026-07-10 05:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8b71664-461c-3364-acb4-78744a740e29 | -10.6951 | -49.61023 | 2026-07-10 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24d78951-fe47-30ee-8d12-7d01580ea47c | -10.40116 | -61.21492 | 2026-07-10 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 563bd24c-01e2-392f-bb6d-27fe709b7eda | -10.84584 | -45.04136 | 2026-07-10 05:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 281a7768-3138-3071-8fb2-f8f3ddc11759 | -10.85792 | -44.43935 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4d933f9-f726-38f7-b106-375e7719d93a | -13.95257 | -53.90846 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf63107e-3331-39e0-b9a5-3b8f830344c1 | -13.3733 | -54.37415 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a488a66-e3b3-38de-a9e2-bc7b6f1fac9e | -12.50122 | -43.77114 | 2026-07-10 05:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 296f00d1-7792-3dec-a3f2-ce4df6156133 | -11.27666 | -55.79897 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39100022-0c7d-3254-945e-80047a23d866 | -11.46911 | -52.92423 | 2026-07-10 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67eba4e8-2862-3399-afbc-c2b09f37c289 | -9.18904 | -58.06668 | 2026-07-10 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d042579c-13d7-3b0f-aa9c-695ff47b7e98 | -12.45634 | -49.58184 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0bb76bd2-d8fe-3872-ad99-abf342d2a8e1 | -10.40577 | -49.44238 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce1a0187-8023-3b44-9832-a12a6cb2788e | -12.45577 | -49.58614 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0e03a51e-9b02-38b5-bcba-c3a9cc71d73b | -13.27133 | -45.14825 | 2026-07-10 05:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10a141a4-f9e1-3f72-95f7-9700f07d1e19 | -13.36103 | -54.36481 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe3659de-1cc3-3836-906a-4eb504417932 | -9.55694 | -48.68007 | 2026-07-10 05:10:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6fb73d9-21c5-31f9-aca1-87e9ea3dcd7a | -13.37387 | -54.37043 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f85f43-00df-3493-ad49-1e5536fe914b | -14.73473 | -48.19475 | 2026-07-10 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb712f77-bba2-35a4-8911-7c91ebc29d87 | -11.32565 | -54.47235 | 2026-07-10 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4806a4f2-2c10-342b-b3ad-9c33ab914462 | -10.3906 | -56.76717 | 2026-07-10 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9764ec31-a071-3941-8de8-f813971d0b71 | -9.18545 | -58.06607 | 2026-07-10 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cfd134f-caf0-3f86-9117-9e48dc005c6a | -10.15581 | -50.20337 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c504ae8c-fc2b-35cb-9af7-9657a05960c3 | -11.47738 | -52.91728 | 2026-07-10 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a1f07f0-6c83-3044-8167-6443c8a61839 | -13.36727 | -54.36961 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4e2c23a-8eef-3b88-864a-293f191e29c0 | -10.40185 | -61.2109 | 2026-07-10 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7385f5b8-d8ab-39c8-b50f-07f9bcac490e | -11.63755 | -59.01898 | 2026-07-10 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80cc7773-d2da-39de-9d0a-122f8cfc1849 | -13.76297 | -46.26942 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7221734f-5874-3349-9e8d-8b1fbe6c81ab | -11.87829 | -47.67383 | 2026-07-10 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8412c01-290b-3281-a54b-33cbebea02d0 | -11.46049 | -47.605 | 2026-07-10 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cd97475-a1c2-3081-972e-892964d775f9 | -13.75766 | -46.26668 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 903ca70d-a07c-33d7-a755-fae708bc9d5f | -13.30028 | -54.32838 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e5c906a-e6ed-337b-8fb6-8396ce023d53 | -12.35808 | -47.41511 | 2026-07-10 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b286ead3-3e4e-3688-88f2-914a15440f13 | -11.32901 | -54.47288 | 2026-07-10 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc10132b-4b71-3396-a447-a95e6b69c6a5 | -11.27722 | -55.79545 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04137d83-7aa4-3229-97d3-68e1dd7abc83 | -13.35763 | -54.36427 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04796118-b1dc-3750-a404-14b7dcab436c | -10.1553 | -50.20695 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6149673a-3c40-3b8a-b0d7-05abee437a65 | -13.3633 | -54.37278 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af3e35f5-a473-3e12-bec2-3b1471747cc0 | -13.29687 | -54.32784 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a6dc90d-7c42-3624-8809-efa1ca5d3ae7 | -11.87758 | -47.67938 | 2026-07-10 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 918987b9-af8e-37b3-9566-28562ad62198 | -13.29858 | -54.33965 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d2c834-9b82-3a4b-b4d7-36c7b2b54bbb | -8.52507 | -54.75927 | 2026-07-10 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3955268-5d69-35d9-8333-dd735ed1bf5d | -13.36046 | -54.36852 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fd3e27b-32d3-3af9-80be-df070cdb2bef | -11.47678 | -52.9213 | 2026-07-10 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2fb2b7-157c-3874-b65e-5ccd8ecd8a07 | -12.85356 | -58.31184 | 2026-07-10 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc5c85d5-57e0-3f0b-89b2-1a3b644f2190 | -10.69086 | -49.60957 | 2026-07-10 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72127b7b-2dcd-32fe-b1fa-f9a3cc03be57 | -13.75685 | -46.27351 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9ea6c10-344d-31fa-a9e9-d0777d034be2 | -10.15938 | -50.17828 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 068808f6-741f-3e02-b9ed-24ebd8c90452 | -13.36387 | -54.36906 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf54342-fe30-344a-bd5d-83a2efc5b894 | -13.60553 | -56.60031 | 2026-07-10 05:10:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16819b1d-bb60-38bb-a325-d8bcaaeccba8 | -13.75646 | -46.27682 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 473507cb-7f8f-3357-b563-31edb79db937 | -13.75725 | -46.27013 | 2026-07-10 05:10:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b834e61b-0d82-34d8-9887-061a6121d1b6 | -13.36784 | -54.36588 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac217acb-e57a-3e34-a399-e1572a58c689 | -12.4516 | -49.57874 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 260f6236-9930-37cc-a11e-697a17b8581b | -13.37068 | -54.37015 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46f99b04-097b-37cb-a3d9-928f533fdc12 | -10.25969 | -46.38786 | 2026-07-10 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09e2bcc-9228-3e32-aeed-311071ca6d30 | -10.15328 | -50.19203 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c143a2af-4e62-3ea8-97a4-e477118eed21 | -12.44761 | -49.58061 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51572148-d6f0-30f9-8613-3ca48fb628af | -13.35819 | -54.36055 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6b097c0-f4a8-314b-a357-dd37211f5905 | -12.4948 | -43.77041 | 2026-07-10 05:10:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6819407-6678-3ac3-a265-d3b504446e4b | -7.90652 | -55.42989 | 2026-07-10 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35f879d7-483a-33e1-8c8e-fce55cf596cb | -9.16394 | -50.89203 | 2026-07-10 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 815e12ba-1c61-34c6-be07-03177e7493a6 | -12.45101 | -49.58298 | 2026-07-10 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bb9bfbd2-32a9-31e6-958a-512352783b91 | -11.27502 | -55.78788 | 2026-07-10 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fee448de-3f8d-392a-9bca-35a4f3b0c227 | -13.30778 | -43.72278 | 2026-07-10 05:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 979c252c-6554-3d46-84b7-8b659d2cc270 | -13.31427 | -43.72358 | 2026-07-10 05:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bff5fac-0703-3ca5-8e02-c418622475a8 | -10.85212 | -45.03825 | 2026-07-10 05:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da059d61-75f6-3dd6-954d-fd061f082b7c | -12.35302 | -47.41447 | 2026-07-10 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3cc4b956-b413-3261-b461-ccad9e33781e | -12.16642 | -59.75827 | 2026-07-10 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da13fa22-3b3a-364e-a7f1-a27c08f59a06 | -10.8584 | -44.44542 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2981e9c0-dc46-3f42-9b60-1ea5f35f2b5c | -13.29517 | -54.33911 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89aeef27-147b-32e9-8fd4-72af8e02a213 | -14.734 | -48.20061 | 2026-07-10 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac17b21b-8236-3dc2-a053-cc47462955fe | -11.44518 | -47.60714 | 2026-07-10 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97809773-b4f8-3eec-93df-2b6d2f2828de | -12.16563 | -59.76297 | 2026-07-10 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c210e13c-aec4-3448-ac3e-38d17ca53479 | -12.85449 | -58.31099 | 2026-07-10 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ef55b25-aea5-3eff-a184-32a6c25b4df8 | -13.3667 | -54.37333 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cca7e18e-b6e9-3aec-a288-a80264b18e6d | -10.40012 | -61.21356 | 2026-07-10 05:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aa3d4ef-baa6-3eee-bfc4-40554fb4ba89 | -13.37125 | -54.36643 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8adcbae5-ec66-3eed-9584-b53975a43957 | -10.85161 | -45.04226 | 2026-07-10 05:10:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd7fec6b-5bf9-3271-8955-e430f5c84fe3 | -10.83114 | -49.377 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fa07dd7-3752-3847-9bb2-c2e3bcad6b65 | -10.83488 | -49.38174 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0632d90b-5b68-3d20-8110-1a75c08085dc | -9.09577 | -59.40168 | 2026-07-10 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 371899e3-27f2-36a9-b369-a6da5e1f38d2 | -10.12947 | -50.18488 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49c72216-ade1-3c89-a676-44becc6c847a | -12.35227 | -47.42043 | 2026-07-10 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fa686723-5533-35b3-ab62-40864cbadb8e | -13.37011 | -54.37387 | 2026-07-10 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b9ecb4-6c62-3f71-8a00-ed848e8753c3 | -10.85735 | -44.44395 | 2026-07-10 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f89fef17-d03c-3f66-bb6f-784ae8e03c5f | -10.12491 | -50.18789 | 2026-07-10 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README11.md)
