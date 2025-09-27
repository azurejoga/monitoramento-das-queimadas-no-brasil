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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70cd9366-1650-36ef-bcb1-a28719b1dade | -16.34448 | -45.0412 | 2025-09-27 00:11:00 | TERRA_M-M | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 47c09d1a-a2d2-394f-9365-cab8ba1209c5 | -15.03036 | -47.15626 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 980a211f-5c5a-3e18-99c8-fa83358d1b40 | -10.22834 | -50.27346 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e9bdee0d-15ef-34d6-ba63-c353c44d9d6b | -9.97517 | -43.60651 | 2025-09-27 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8907365-a6cd-3c8b-bb2a-5e2aa0fd5cd6 | -15.11906 | -49.54859 | 2025-09-27 00:11:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 434c44d1-1257-36cc-a996-f767cf343c3d | -11.35112 | -45.01015 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 3b6e0058-a130-3f90-b972-dc33b7a46d8d | -15.05098 | -47.13831 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ccbef716-0016-3446-8e15-c0944544499e | -11.7147 | -44.41568 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9aa4d7ea-e28e-3788-a32d-2f374307796f | -12.09828 | -44.18693 | 2025-09-27 00:11:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e4c1607-3591-37df-8703-1b8bdebbf257 | -12.32082 | -44.68888 | 2025-09-27 00:11:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7c438470-fe6b-35ab-a2dc-0d0c9ca0ea27 | -11.37622 | -44.98662 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24352998-bb1c-35c4-af3a-15799727b316 | -10.92426 | -48.8316 | 2025-09-27 00:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 7bfc6584-08e8-3276-859e-af023ba5490b | -10.93563 | -47.749 | 2025-09-27 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 62f8e56f-7393-3831-a831-09e05a2445b0 | -12.06821 | -46.6358 | 2025-09-27 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d00d43b0-ae2f-3cfc-a663-9b4728a6700f | -10.25089 | -50.26532 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b765c4d5-ef0c-3c20-8536-7fa6c0cd2fcb | -12.30288 | -47.21852 | 2025-09-27 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3f83b01b-594f-34d0-bd78-71b7e6f8e257 | -8.8408 | -46.24429 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a9b6ed83-e719-3dec-b0db-8ae913b2ebdb | -12.27383 | -44.05474 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 30045da5-acd5-3c1d-86bb-b5996bc67139 | -15.11321 | -49.54392 | 2025-09-27 00:11:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 11f38541-654a-3083-9969-9090d26ed3b4 | -11.42761 | -45.01968 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6dce28c1-77db-323a-8e78-4347d06d35e5 | -12.18178 | -40.41056 | 2025-09-27 00:11:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 102d7bb8-2dd3-31b9-8cca-9851758a85d3 | -9.09992 | -48.92041 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e95fbe8d-67d1-39f5-a699-8b21a547e3ab | -8.84545 | -46.24875 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4240f0e1-a4cd-3112-b1c5-bb00e304976a | -8.81483 | -46.26922 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 93a1fe8c-2595-3d12-a241-3765aac33d4c | -11.67581 | -44.46931 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68c9a141-d923-3f2e-8ee3-513e4695c954 | -11.97525 | -47.90987 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 38921878-8e2b-3862-83ae-4219d41caca1 | -9.30474 | -49.00085 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0c746a97-4dee-3d0f-925f-38813e4aaca7 | -8.82302 | -46.25737 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 17734a91-fe10-3c8b-9b17-569df92f57e2 | -11.4329 | -44.98891 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 60cfe7b9-b73c-312f-9f6b-5a3ef2abfbdf | -13.50448 | -47.40473 | 2025-09-27 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8659cccf-6191-3364-9e7b-3707857cf47a | -11.49259 | -43.52765 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed343e0e-67ca-37e6-bd83-1499be069f25 | -11.78302 | -43.76216 | 2025-09-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 2a5f29c9-87bc-3d51-800f-ca5869ffee25 | -11.3803 | -44.9464 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aacdd8b7-d0c8-35cc-b023-3b3d9f700c7e | -11.36958 | -45.00758 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 751d094b-cf8c-3a7a-af8a-43b5b025ca3e | -8.57018 | -42.33665 | 2025-09-27 00:11:00 | TERRA_M-M | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7b6a0105-124b-3004-bf1b-d7aee54fce29 | -15.10683 | -42.47113 | 2025-09-27 00:11:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| b8cb9c1f-21c5-367b-bbce-e31e4e83d3be | -11.36164 | -45.01873 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c7df6024-b71f-3501-86fb-6248fa4ed929 | -15.58672 | -42.41557 | 2025-09-27 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f1586d2b-5922-3b81-bebf-5f352a3df70f | -15.78968 | -43.85003 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 176955ea-6134-30ff-a3ca-7096313665db | -10.9318 | -48.84207 | 2025-09-27 00:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ad719aac-42fc-33f4-9d10-aacc16d81089 | -8.82444 | -46.26799 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| d7070e3e-d523-359e-8442-b0cbe5fb6dfa | -12.06664 | -46.62334 | 2025-09-27 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 16ac6846-07d0-3003-9f99-d8f917adc261 | -13.50616 | -47.41887 | 2025-09-27 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f0629193-447f-334f-96bd-17a46e17f279 | -10.17506 | -49.39312 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 68d6964e-fa8c-34ee-b851-b6bf54afc78e | -11.36829 | -44.99772 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1af69861-1b22-30db-b45c-84ebee8d8e3b | -14.84594 | -45.61646 | 2025-09-27 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2d36f707-a8f8-306e-b017-51ce1bbe0c5d | -15.02049 | -46.97555 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b45aa2f2-8e64-3b38-b9bd-0aafd5c7c990 | -11.65105 | -41.69215 | 2025-09-27 00:11:00 | TERRA_M-M | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 585d0eb4-51ff-3292-aea0-5d0fc0d2e64d | -14.41133 | -44.35792 | 2025-09-27 00:11:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 41fe3ca0-76e6-358f-8b25-0a5efb55697b | -14.95812 | -47.5074 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 5a8f2a89-3a57-326c-ad7a-f084322a4bbd | -11.34461 | -45.01738 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8fa17a99-5ba8-34fc-85e4-4a46f0b3a6cb | -10.90876 | -43.62993 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0599d309-a533-3cf0-b74e-721632db0371 | -10.96228 | -44.50304 | 2025-09-27 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4aac3335-c4a9-396d-b730-f29789543ccc | -14.84737 | -45.62806 | 2025-09-27 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c0d6c964-87bd-3179-a180-ac1d9bb33bf3 | -11.50389 | -43.54433 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4ff0004-d138-3a21-a0db-40597224de26 | -9.96758 | -43.61667 | 2025-09-27 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ad37efca-ba77-32a7-8b09-0dcd8ce18a2b | -9.07905 | -48.03132 | 2025-09-27 00:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 372177da-f649-34b1-b923-76af729b5288 | -11.35906 | -44.999 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e182d595-1f0f-3594-9359-c898a3c2bc85 | -11.71343 | -44.40625 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1a9ff55-6b85-3105-a288-c608cc6a8d08 | -15.02959 | -46.9579 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| face96de-4515-3f85-bbd2-8f48c4998bc4 | -10.22571 | -50.25159 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bd1e499e-d6fe-3568-bd70-7dbf652580f5 | -12.36043 | -44.15038 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78521610-5514-3390-9d4f-a29f0b4180b0 | -11.36035 | -45.00887 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| ae2726e6-378a-388f-b69a-5309abf7c130 | -9.49033 | -40.32119 | 2025-09-27 00:11:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8785afaf-f7b6-35cc-a936-3dafe460e11d | -9.10961 | -48.90232 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 618e212f-2c23-37f7-9838-13f2ff78ec68 | -12.96632 | -46.91508 | 2025-09-27 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7eddcbc8-950f-30bb-bd1f-03b207ef5688 | -11.97334 | -47.89455 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 10ad8e8a-ff08-3cc8-b5af-bb0a4b47dfe7 | -13.14996 | -43.31021 | 2025-09-27 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f84e170a-3832-36cb-aa31-e7c08c222d17 | -10.88215 | -49.41095 | 2025-09-27 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bd563f24-518d-39cb-92ff-8d2a02fb83cc | -15.41937 | -48.20755 | 2025-09-27 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8287c30b-1f19-3057-b2f5-bb5b087d6bed | -10.93734 | -47.7626 | 2025-09-27 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dab7fb3f-a457-3409-8ee5-ab86d5502cde | -9.49224 | -40.32681 | 2025-09-27 00:11:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 09c49d86-b5ef-3c21-8b6c-4ed57e694b26 | -14.88684 | -50.29623 | 2025-09-27 00:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| f865bf33-5029-32b5-8666-16b562400b41 | -10.16753 | -36.37614 | 2025-09-27 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| cf96c726-ff0f-3d19-a98d-09ede84e6b6e | -9.0449 | -45.51782 | 2025-09-27 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b918165c-d6cd-3ebb-b4b5-f8d6f19c43c7 | -15.0286 | -47.14109 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 2f650ff4-e31c-3c89-9488-bda2ab3843a7 | -14.07202 | -48.82753 | 2025-09-27 00:11:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2253c796-a894-3d97-a936-109b2b7de31c | -11.69663 | -44.41823 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56372f1c-7fc0-399e-8cb0-50b23efca88e | -15.55403 | -47.90422 | 2025-09-27 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6ea616a5-e63d-3f6b-b0ac-59500f4d8323 | -10.97724 | -50.72951 | 2025-09-27 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 05a05396-d46d-34c8-8e2f-f016bb730edf | -12.27508 | -44.06404 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 00d0510d-1a4c-3249-85d1-ebf5f306e88b | -12.28279 | -44.05349 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 162854c4-d966-33cd-86b3-354042ccebcf | -9.60573 | -47.56046 | 2025-09-27 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2bab36a6-c94f-30ca-aa0a-62903f58889e | -11.43814 | -44.97272 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 99b74546-5bfc-3052-b408-6afd6986b3c7 | -10.17284 | -49.37452 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| eacff2d3-0dfb-39c0-8534-e88e5d99a4b8 | -13.88239 | -44.24689 | 2025-09-27 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 39e9e6b3-89e7-3b64-bbea-85533c6faea2 | -11.40697 | -43.50924 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5a36ac3a-7d7c-383e-a419-50f7eb3743a2 | -10.32419 | -47.89951 | 2025-09-27 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 17496370-8070-3b7d-852d-af6ae311bb86 | -9.99703 | -44.17564 | 2025-09-27 00:11:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1d62fe75-9a4c-3886-b866-28fabf23b00d | -15.54086 | -44.34319 | 2025-09-27 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 5d734046-47a6-32e4-8ec2-c322acdbf8f3 | -9.0436 | -45.50797 | 2025-09-27 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f911df4d-a7e6-3171-8520-c2ab8534f678 | -10.57227 | -44.07561 | 2025-09-27 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbb181d1-adaa-363c-85cf-070865bedd36 | -14.94659 | -47.50856 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f514c6de-be3d-364f-8b6d-7fb4273ff96e | -11.43939 | -44.98227 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7c44e06d-86f6-3ed8-87c9-b711b22d03b3 | -9.97394 | -43.59761 | 2025-09-27 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bd4567cd-8ead-3355-8f55-b7be259c4e02 | -15.27437 | -46.43657 | 2025-09-27 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8d77d56c-b538-381e-abdb-611790ea311d | -8.81342 | -46.25863 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 1d73af18-242a-3c6f-953a-5e14bcf7f9f0 | -11.98238 | -44.77107 | 2025-09-27 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 797262a0-bf71-3759-a41b-988a28426931 | -11.35241 | -45.02003 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 87de92df-bfba-3eb4-9789-6457d67d6cb0 | -14.87441 | -45.60085 | 2025-09-27 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README4.md)
