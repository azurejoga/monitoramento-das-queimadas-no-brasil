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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31392ecd-78f4-3e31-83f9-cc38f4e8f2cb | -7.1902 | -44.36505 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a450047-0194-3a74-8c56-5f8483b2e5d0 | -7.53122 | -43.94928 | 2026-08-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe565cce-fbbd-3fa2-b614-78c85d268c39 | -7.39709 | -42.86935 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 857d3e17-f849-309d-b9e7-81fd682c292f | -7.72127 | -46.22004 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ff78c12-e9a1-3352-bc5b-d88917d8554f | -8.35869 | -45.97793 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 89732504-0f3c-3a59-859e-1e33fc40ae00 | -8.60454 | -45.41088 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0842af29-8875-3e1f-bcbe-4d695d624087 | -6.04419 | -43.86615 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dff3b33f-afd4-3e7f-b215-dd466d7550f1 | -6.95341 | -39.7279 | 2026-08-12 04:14:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f78caa4a-f1d6-3700-beb9-226b3f432e90 | -3.8482 | -49.09119 | 2026-08-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d82010c4-dcb8-3540-bbd1-663314c0ba02 | -3.02958 | -48.4111 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 474fd9d8-129d-3fab-ba0c-4a7521cac053 | -6.54449 | -43.12511 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f299d727-8862-3913-a342-c8a874a4855d | -7.39207 | -42.85787 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e227ec44-dad8-3800-9b31-3f06437d843d | -8.07759 | -46.52393 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6f4345a-2a28-376a-8937-a49652045832 | -3.23951 | -49.46043 | 2026-08-12 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12dda8a1-59a3-3c14-863e-2c81352cff00 | -5.73986 | -44.50058 | 2026-08-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c34ba04c-0828-3ed2-a18a-46856dd82927 | -7.01324 | -44.6212 | 2026-08-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d39d4bf8-8d3d-3ee4-bbf0-58bf52672d11 | -4.66402 | -37.78374 | 2026-08-12 04:14:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf72008e-f8ca-37e1-a491-b7981f7d21db | -7.9187 | -45.10954 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66438adf-d036-33d0-bd9d-68b87ca206e1 | -6.97205 | -41.47603 | 2026-08-12 04:14:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c182035d-4b0f-3e8b-9be9-33bf7840da04 | -6.54333 | -43.11078 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f35b69a-374d-3eae-98cf-ea4821640a6b | -7.38545 | -42.85684 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7be7e7e-a23d-371d-acb7-7d6ed01bafc6 | -3.01368 | -48.84367 | 2026-08-12 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8246f05-d080-3633-8abf-42540a7bcfd1 | -7.3738 | -42.84434 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c7ff0b1-33d3-3b59-9222-40f9cf226d93 | -8.07826 | -46.51987 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 526e273b-5898-3655-887f-2f88e5e41696 | -8.48749 | -45.41853 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5055fb7e-d0b7-3b21-91af-9a2680508174 | -8.07548 | -46.52052 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc8e4a85-5212-363f-b6ce-387883cfcf81 | -2.84959 | -49.54382 | 2026-08-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f643008-4c04-3604-8635-acefe63feaba | -8.63002 | -45.85956 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c12d6ca2-fe37-3eb6-9355-7986facde246 | -6.54887 | -43.11871 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37b0e3e5-09b2-324a-9225-339ecd3e09ef | -7.61328 | -42.74614 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cced5657-c511-35c7-9182-bbd4fde1daef | -5.80443 | -43.63882 | 2026-08-12 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae42b074-dd47-3109-ad4c-802675fb89d2 | -3.48867 | -50.05263 | 2026-08-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 626eba24-9b36-3a72-8499-b1be45574d19 | -6.88986 | -41.9468 | 2026-08-12 04:14:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 845b79d9-d9be-3d3b-ab36-8c445a539071 | -7.45784 | -46.14332 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e2fc5ca-005e-3079-9d3e-8c63ffd2e172 | -7.61382 | -42.74264 | 2026-08-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b67db167-252a-3927-a6fe-e13b52d64f7d | -2.79181 | -49.52751 | 2026-08-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8a86907-99ac-36ca-b0df-e205a82329dd | -7.94853 | -44.98785 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4ee60c1-c4c6-3bcc-95b8-79706395b656 | -4.76834 | -41.7986 | 2026-08-12 04:14:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ddb4ed57-c32e-344a-90fb-e4db836fb63e | -6.05029 | -43.87069 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79631ac-a658-3c5a-826e-ccd847022973 | -3.43352 | -49.48407 | 2026-08-12 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66482a6f-cced-33b9-8b33-3aa6ef54421c | -8.49089 | -45.41912 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3476948-fc2e-3eb9-88c6-2c2d320cdb17 | -8.60074 | -45.39128 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11d159f0-1774-3f54-8324-a248f60a21b2 | -8.3748 | -46.39596 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b297de81-22af-3017-9c8d-bc153166922b | -6.54833 | -43.12217 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| abaf8d3a-0c56-35b4-bdd9-8de39ade7dad | -2.42156 | -51.83774 | 2026-08-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac46b0e2-6242-3411-80b0-74c1f23b3c07 | -8.07256 | -46.51588 | 2026-08-12 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 788079c2-32e2-397a-96e7-df3b3c0d6baf | -8.63873 | -45.84952 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d9b73f3-d500-31c9-92a6-a66f15b9451d | -7.19298 | -44.3691 | 2026-08-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8115fd0-6714-3714-83ac-6f1b5701257f | -6.99643 | -42.64617 | 2026-08-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 65e87a3b-4193-3354-b2b2-1730dbdd425f | -2.68846 | -48.21171 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fe85f4a-0d98-3b64-beb1-3380e66b9732 | -7.00137 | -42.63624 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ac251b2d-3d24-3f4c-935f-24723620516e | -6.54995 | -43.11181 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48b31034-8f43-3e4e-be65-1224f4a00e1d | -7.00752 | -44.83089 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d69fa7bf-e152-3c97-bc08-8c1080fe8c5b | -6.39536 | -38.90922 | 2026-08-12 04:14:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 042bc967-f16f-356a-b646-e78b22e82b91 | -7.39523 | -45.10884 | 2026-08-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 821f2480-4631-390d-bcb1-883e320404f4 | -7.45848 | -46.13935 | 2026-08-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c5381c2-f67b-3f8c-95bc-7c975b2823be | -7.74949 | -45.02274 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a16594-52d6-3cad-883e-73831be68d22 | -2.41674 | -51.83692 | 2026-08-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cdaa43e-62ed-30d1-9940-6982742f08bf | -6.04032 | -43.86912 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7cccbed-e354-334c-9ea3-12766a4af491 | -7.38267 | -42.85284 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da1fb8bf-da85-37f1-8a45-32b6439f4661 | -2.85038 | -49.53897 | 2026-08-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44a1ec41-f0e1-3d22-b055-1e23d3818c6f | -7.00029 | -42.6432 | 2026-08-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 81bdb8eb-aecf-38d7-a546-ec526b156626 | -6.54779 | -43.12562 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5441ca16-b915-3ed6-9dd8-7ddf596036f2 | -8.4835 | -45.42163 | 2026-08-12 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5df915d2-388b-3982-9021-e35f2e08395f | -8.78117 | -45.79504 | 2026-08-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1096efb9-79ea-3542-ab86-b2d76dca8722 | -6.54556 | -43.1182 | 2026-08-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e709b90d-7465-3393-8ecc-c739d8873c46 | -6.04751 | -43.86667 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d91ca94f-7cfe-30f2-9a1d-1ae9f91d2963 | -7.39655 | -42.87283 | 2026-08-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da3d1218-3103-36d4-b5d2-30e9bd36411b | -7.9215 | -45.11374 | 2026-08-12 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c648ea7-9f6e-35b6-b725-9625447b9c16 | -3.23963 | -49.46165 | 2026-08-12 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76e84d58-c8d1-3b64-b2f7-3a3867bb091f | -8.63813 | -45.85326 | 2026-08-12 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a4b8be9-6fc3-3974-ab6f-65bf7e029fd0 | -2.6858 | -48.20685 | 2026-08-12 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45bec85e-b3bb-3b4f-aa10-1be60547bf8b | -6.04696 | -43.87017 | 2026-08-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 673cf7e3-1d37-35cb-9ae3-19c0bba85b95 | -5.73592 | -44.50364 | 2026-08-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09a44ec5-5412-3d5d-9688-8e2305e98054 | -13.90449 | -53.8248 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e378ab70-ed3e-3b87-93e7-04ab95fcbd86 | -13.89092 | -53.78519 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 97f4c865-4ac2-3af8-8579-e9d24b492784 | -11.60434 | -54.65173 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c75d186d-af77-30ef-adb3-24c8cac7cf2b | -12.03292 | -47.79955 | 2026-08-12 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e434229-13f2-3eb2-b1e2-36b43a8d7e9b | -15.29887 | -48.87805 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef458e78-4e23-3c5a-9412-c6a18ead537a | -13.90446 | -53.79762 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c1f1b3c-c713-36f8-b87c-76d77022e932 | -13.83252 | -53.82919 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7df72fd-af66-3341-b6c4-ad5788c693fc | -15.28565 | -48.8667 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44327eb8-db2b-3f2e-8681-1b5af1960737 | -11.93253 | -47.36275 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94625c44-3151-3429-9f6d-aedbe88abb8e | -12.10307 | -47.189 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e3e8aba-aa39-3344-a9c8-58f8dcc73cde | -13.89242 | -53.832 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0627b566-c4db-3f67-8f9a-5f0080133927 | -11.95285 | -46.38171 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6fa8b3ff-5aee-31fa-abe8-bb9442903aa1 | -11.9855 | -46.37523 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d121fd75-c7b3-3061-a01c-10c9f8f503b5 | -10.09668 | -46.21541 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 402906c6-2d7d-329a-b792-1810b17290f5 | -9.15842 | -48.8328 | 2026-08-12 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28f6a550-a20d-3fef-be85-019f709fa719 | -11.46892 | -44.56068 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bf3ee16-0a30-3161-8370-3d01292b0c7c | -14.98907 | -46.59364 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4368a644-e0b3-32f7-a54d-21d15b52e901 | -13.85883 | -53.83121 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d74cb3-d331-3b32-ab0b-e9cd642343c1 | -14.83534 | -52.61739 | 2026-08-12 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e250352-62fb-33c4-8407-d523e4351453 | -11.82889 | -51.83969 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec87b72e-9e19-31b7-9167-e32feec3f246 | -14.5188 | -49.29719 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19bf6f12-1b17-33de-9ea2-e5b06bf0b168 | -15.30292 | -48.8719 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b34d1656-c91d-33be-9bd1-aacf4d8dbeb5 | -13.8563 | -53.81644 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f96532c-e283-37ce-9bf7-85f27de8a9e4 | -10.22713 | -45.91104 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d4aa480-a1f4-38ca-a125-fd5bdcdf8213 | -14.52256 | -49.2981 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e308aeeb-a572-3948-8452-c0d62b579c12 | -11.95565 | -46.38607 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README10.md)
