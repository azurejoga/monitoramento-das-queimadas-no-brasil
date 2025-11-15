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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a00bf55e-16cc-39b7-af4c-a96c9afd4887 | -10.71045 | -44.06767 | 2025-11-15 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54530495-6554-3697-a960-f8e942e2c59c | -9.14152 | -47.76497 | 2025-11-15 04:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 453f9f4c-38d6-3177-9ff5-206d58286fbb | -9.86317 | -44.71434 | 2025-11-15 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c3ba1ab-ffc2-3bbb-83e8-302a3bcc58c5 | -12.99481 | -49.79957 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0aca647-1ce0-3ba3-9d57-ad73425c469f | -13.77818 | -44.33519 | 2025-11-15 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b2f22bb6-6de4-3734-ab30-221cc7e1132b | -7.53178 | -47.20581 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcfc155e-7ac2-36ad-8bba-0e8d307aa4b5 | -10.1815 | -44.38804 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db3f2926-4828-3a2e-8b16-3a734fe72fd0 | -10.66919 | -44.4849 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b9295a7-0aa0-3773-a11d-a7a32c2f51a3 | -11.91927 | -46.20942 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef4525f8-7a9c-3db0-ae9b-13b6717879c1 | -11.66302 | -48.46631 | 2025-11-15 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb2860d-5558-304d-bae1-c3c783aa6449 | -12.67489 | -46.76585 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a68990d5-805f-3587-b49d-67bdd8128fb1 | -10.70942 | -44.06908 | 2025-11-15 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd571a5a-9d25-3797-b189-443f9c6abd51 | -9.93818 | -44.93213 | 2025-11-15 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcd3d1c0-df4c-3719-971b-63e2013ed050 | -7.87588 | -48.40823 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1dd07e8c-1230-3e8f-bcf1-9e4ee5a379e9 | -7.39244 | -48.649 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaadc6b6-e075-3ef7-9ade-45583e182bd7 | -11.3287 | -48.51495 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 895c199b-9a6a-32a1-a1ef-a6d3bd4d78de | -11.96195 | -44.9558 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f67f333-8d84-3899-9eb0-b64b16b6a5cd | -12.65705 | -46.74729 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb73deb4-769f-36c1-90bc-4216e3bdcc3c | -8.90176 | -47.89803 | 2025-11-15 04:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19eb4020-0c17-3d77-8999-433cb78f0b5d | -11.32388 | -48.51193 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e2cafd4-39c6-3ecf-83ab-10e6ed337427 | -10.87129 | -44.68238 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b115efbc-56fe-39e2-ad32-3d9c1879eb9c | -9.12288 | -43.95001 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51e56631-0474-378d-9516-208942502524 | -10.70163 | -44.49518 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69fa395b-001d-3f6d-805f-e77b0826bae4 | -10.69495 | -44.51218 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fd7a28b-10b7-31e6-b9c5-7836f5e2d766 | -10.17029 | -49.31584 | 2025-11-15 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87514b3d-4979-3a3b-b7a8-cb29fc9d296b | -11.32668 | -48.52344 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 482135ff-38ed-318b-8368-1b79aaa1cb53 | -12.85079 | -46.43254 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94a3309d-b29f-3d67-a815-a0ab9ff74215 | -9.80693 | -42.21301 | 2025-11-15 04:06:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b21572a7-29b0-380b-8e8a-5d00834a48ba | -10.35127 | -48.91971 | 2025-11-15 04:06:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9c5bb48-51d9-3edd-aa19-a71acbacdcab | -11.85394 | -49.22177 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82c3a190-7f21-3f48-a399-ebb9cc42c7fe | -8.74448 | -48.31485 | 2025-11-15 04:06:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb739aa4-6c60-336e-8f78-fd3ad10310d5 | -11.32475 | -48.50714 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ce3d84b-373e-3dc3-ab3b-8c9b8763cdfa | -9.81582 | -44.22606 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 405535c5-062b-3ab9-8122-1de5bde64081 | -12.75832 | -43.6515 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d52224f1-60e5-38c2-a512-e8f00faaa309 | -8.89704 | -47.89721 | 2025-11-15 04:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf11eb9a-ee0b-35a6-9978-94e9de578423 | -13.89663 | -42.89924 | 2025-11-15 04:06:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e026dbd4-6390-34d9-ac99-ce105b7f2846 | -8.541 | -49.58662 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55106718-f1cd-34b1-9a04-2031699bb3b0 | -10.44878 | -47.33479 | 2025-11-15 04:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2884f34-cc17-3227-a5d5-cec902e273e5 | -10.10882 | -40.89485 | 2025-11-15 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 179cb9b5-a31b-3f2a-82a0-3edfa3d76a92 | -12.80632 | -46.44976 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c086ba9-820d-3c64-ace8-260354b06310 | -11.96484 | -44.96145 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79b4299a-bb87-3fce-9aba-6b38f1fc6397 | -11.71584 | -48.86985 | 2025-11-15 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e42203a3-7bf8-3ff8-925f-e197e04865f1 | -10.73293 | -47.38094 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08088566-1994-3e09-90a8-4a4ce0211eeb | -12.92533 | -43.08958 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a692ad9-d0a9-3507-b6f3-2a9f63e25e7b | -9.85188 | -44.16985 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b3e965-3733-374f-b0b1-e0a38a9436f2 | -11.32007 | -48.50609 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23aef931-dbb2-3cba-bf9a-b9e0365c4927 | -12.2392 | -49.38898 | 2025-11-15 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ec56010-244a-3fe7-a1be-06b5e547503d | -12.7542 | -43.65478 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c3b6e26-c514-3ae2-b29e-1bd07ac8a19c | -11.74308 | -45.32975 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cc94c10-7d23-3b8a-890e-6df610a00206 | -12.8387 | -46.43074 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc9c424e-0a36-3d57-89d2-9f88471ec081 | -12.67555 | -46.76215 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 993c9610-7d66-3596-8a30-438f47f77990 | -7.88182 | -48.40359 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 537a8668-5944-32dc-87b0-359b65ad74e7 | -12.76114 | -43.65598 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 517eec55-e180-3d29-b9f2-cf9910d7c838 | -10.05443 | -45.35117 | 2025-11-15 04:06:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea3c29e-2dce-3a25-a135-a0303d605199 | -11.00955 | -44.64029 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 865b1fe5-8d9d-3637-b2d7-609fdb761dfc | -9.66254 | -43.89795 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7816a2e1-c927-39fb-9e29-5f50a7b504ed | -8.53783 | -49.58809 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91780a64-3eac-3146-aab8-580bde7f7e81 | -10.44785 | -45.07232 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6529744-a8cd-3320-8ae1-47fdf765ce56 | -12.68243 | -46.77109 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4e5e67c-c13b-36f8-8373-63a1a990844d | -12.66802 | -46.75694 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6d0961-9ee8-341a-b6c8-96cd87a52f8f | -10.70233 | -44.51352 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc268180-e9d8-32d9-b82c-65d869ad4f00 | -13.52931 | -43.41491 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ef84c64-5af7-31f4-ad66-bc9d4ce2a40e | -7.05961 | -48.3219 | 2025-11-15 04:06:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c6ff7f5-98dd-3ec9-b4ae-5fbd61d050e6 | -9.01358 | -44.18145 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 544f0cc8-93b8-32ce-9377-a903f1b02347 | -8.74352 | -48.32027 | 2025-11-15 04:06:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dcb9925-e743-3b6d-a61e-623c17a0cae2 | -9.44271 | -44.86882 | 2025-11-15 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 430699bc-6ea0-3eb4-b8f0-a2e922e3a583 | -12.67899 | -46.76661 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e8e7acad-e29a-38e7-813c-e85d27cbfa61 | -13.68491 | -42.99602 | 2025-11-15 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d656f348-20fc-3c21-b970-fc3a9284ab8c | -7.26571 | -48.02898 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 515fe640-945b-3aec-a76c-1c54631c93c6 | -9.09745 | -47.78579 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72668604-12e4-375c-a391-359665c95d12 | -12.79217 | -46.38574 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c4a7fae-c859-3e9c-ba69-0195ce38f3fa | -9.11848 | -43.9538 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 699e81cc-e597-3cd1-9f99-39a92abf2dba | -11.80244 | -48.07383 | 2025-11-15 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77f51d23-8746-39c9-8bb3-fcd257438bf7 | -10.93032 | -48.70438 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d349cb98-eb58-3777-a779-96078291e840 | -7.53343 | -47.19628 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b46c429-c9b7-3b1b-ac37-05f519d75872 | -8.15665 | -43.80742 | 2025-11-15 04:06:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abedbe5a-d9a4-3e9c-a87d-95832d45048c | -8.32636 | -45.41271 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 710943ef-84dd-3eda-a022-c47e85e58c91 | -11.39429 | -49.19946 | 2025-11-15 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e495118-2aa6-30c7-8cad-0ea534237b82 | -11.32113 | -48.52924 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80eb485d-8bbb-38d1-be13-a5f7ebe25005 | -11.84922 | -49.21272 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| b1e6a32f-dcce-3d91-a4f2-d84c96b98a16 | -11.47455 | -41.98895 | 2025-11-15 04:06:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7350120-306a-31a0-9ab0-87e0c02f192b | -10.33634 | -49.64226 | 2025-11-15 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c57b230-5dc8-3243-8923-499da7dd15c3 | -10.62495 | -44.5871 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe5b45b8-560b-37c0-ae35-9891c17e35b0 | -12.62353 | -42.3926 | 2025-11-15 04:06:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3b9316d-27bc-3a0c-86e7-f850579d22c6 | -10.42369 | -44.94931 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22dfb040-e669-3ea5-8d4c-fbac75826d94 | -8.65152 | -45.45778 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32936df9-a5f7-39b3-b090-6f5c126d52d1 | -9.85939 | -44.71371 | 2025-11-15 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e34084c7-925f-3b06-9958-4a1f308a458b | -11.85011 | -49.21528 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c4b64a59-f014-3c9d-8c3a-ea0ded7b4b53 | -8.99872 | -44.17907 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ef42089-6894-3cf8-8f47-423b95055f63 | -9.7266 | -46.34143 | 2025-11-15 04:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99bd39a0-539d-3bf6-8da1-38af0641a09a | -10.70308 | -44.50909 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 558299ac-1515-3856-ad4d-558d7ce9452e | -9.71867 | -48.8954 | 2025-11-15 04:06:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bba8aea9-0525-3dd9-a0e8-1f577b51ff5d | -11.84522 | -49.21433 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| fd462c48-aaf3-3a9a-b103-1d6bc9a8aebb | -13.80713 | -43.19083 | 2025-11-15 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f5563e5-df58-3079-8534-14481d17966d | -11.67914 | -44.73979 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f70c7e5-9b72-39a5-91f1-24fc315aec39 | -11.75376 | -45.33619 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9db62d41-24c5-3506-a905-1ce9cbdbdd41 | -13.29123 | -44.20022 | 2025-11-15 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4354bd2-7e58-3580-8751-115ebb6b2b76 | -7.2138 | -47.98057 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc73dc5d-4ef5-3eb8-b700-c639063aea12 | -9.66205 | -45.36957 | 2025-11-15 04:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81b8f37a-9330-3403-b2db-860feb2c85fc | -11.71113 | -44.44685 | 2025-11-15 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
