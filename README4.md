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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c06f07cb-6c1c-3dbf-ab3a-861ef6e5c79f | -9.605 | -56.928902 | 2026-07-01 01:11:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7cb652f-ead9-31b9-b6a3-5742e335df11 | -21.0951 | -57.4655 | 2026-07-01 01:11:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bdf4653a-ec20-3324-ac1e-9f113828f3fe | -9.0201 | -59.534199 | 2026-07-01 01:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 635fef1c-d2ae-38c2-8bdb-154976bbe4ff | -12.4079 | -58.372398 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61bbd137-78cd-3705-a16f-37e9a8540016 | -11.4132 | -56.069 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1af84da-6695-3873-94f6-835897a8aad2 | -10.6669 | -54.519299 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf64d57-a564-361c-ab6f-25a585393a3d | -9.6014 | -56.914501 | 2026-07-01 01:11:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b49a2b1c-a27a-3913-a597-543a2fa847a9 | -12.4203 | -58.380501 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 991fa96c-d57f-316a-b47a-80529178685c | -9.0299 | -59.531799 | 2026-07-01 01:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2e80dd-3a51-3f9f-a970-8f9c12629183 | -11.9033 | -57.369099 | 2026-07-01 01:11:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b34de85-eb79-30f9-b47a-0f38d8aea03c | -12.413 | -58.3936 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9234a54-2729-35dd-9582-bad774718689 | -10.7627 | -53.540298 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7a181ed-5eda-3141-a1ff-9852fa8c6416 | -9.6949 | -56.0891 | 2026-07-01 01:11:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8da6757a-d5fc-3df1-93da-a9effb373924 | -11.4093 | -56.0536 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b47a9b3e-f8ed-3a08-a594-d98c61def45f | -11.6201 | -59.004398 | 2026-07-01 01:11:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e0623ff-c3e3-34ce-bc56-519f3f6e1c9b | -12.7978 | -54.856701 | 2026-07-01 01:11:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67791d2c-1ee3-3ef3-84eb-4dbe57c1ff6e | -11.0449 | -56.9077 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab8fcc3-a369-3013-9b8f-5cb23c6d9b47 | -11.6323 | -59.011902 | 2026-07-01 01:11:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d907024c-c3fb-3404-8ad9-3dec2f788291 | -10.6817 | -54.5368 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f31d9459-929a-32dc-b10b-8db14faf8c23 | -9.0177 | -59.5242 | 2026-07-01 01:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51176a46-1b0e-30ac-8ca3-52b7c5cc2b0e | -12.4105 | -58.382999 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5db3aed8-a44b-3427-aad8-11077c7908a2 | -10.6721 | -54.539398 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 034d73bb-b7cd-3e1c-80a1-507df8f47ef5 | -9.1726 | -58.067799 | 2026-07-01 01:11:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1df7b12-5057-3037-902c-60d0be495049 | -9.5917 | -56.916901 | 2026-07-01 01:11:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 015c0d0f-8c09-32ef-8101-03fd91de5597 | -11.415 | -56.035599 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3efc75-206d-3a22-bed3-1eab754614c3 | -11.6346 | -59.021801 | 2026-07-01 01:11:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83671d0d-b8f0-3409-b6f0-0430ffc40917 | -11.8401 | -56.948002 | 2026-07-01 01:11:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9aba17d-b56a-33e3-8803-542dfdad0a9f | -10.6573 | -54.521801 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58ab77fd-4b2d-33eb-b1e4-049fadc890ba | -16.362301 | -56.651699 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 297da9f4-4433-3fbb-8954-e2a71ea75492 | -10.6765 | -54.516701 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2840d3d0-a5a2-3fd9-8db1-5d47ad7fa793 | -10.7565 | -53.5168 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b525691-a062-385f-9627-0119db797843 | -11.4229 | -56.066502 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 680b830a-4a3d-34dd-a678-32cc17c2764d | -12.2154 | -56.547001 | 2026-07-01 01:11:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bea9a282-cd16-3f5d-b311-a07eaa38eafa | -16.3496 | -56.642399 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b001e872-330a-3c18-a1f0-fe52863fe88d | -10.1238 | -52.0961 | 2026-07-01 01:11:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd804239-131c-372e-8307-9b997e04dc1f | -9.1696 | -58.0555 | 2026-07-01 01:11:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac3f2b0-bcd6-389a-be2b-745a54c7ec05 | -11.4326 | -56.063999 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 575decda-9082-343d-86db-66e0b0a09b2c | -11.4364 | -56.079399 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd24b435-7d07-3972-91fb-667dcdbbee31 | -16.3556 | -56.666199 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 801979d6-9295-3095-8512-abe5638d4b47 | -12.4228 | -58.391102 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5dc7fd-0f1c-3057-a3b8-60a9697f5c46 | -11.4267 | -56.081902 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7977c111-e6ee-3566-b7de-cb6b8f71f486 | -11.419 | -56.051102 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18c82c48-ca30-3533-9abf-e2bbc1507cd5 | -11.9064 | -57.3815 | 2026-07-01 01:11:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2a1ad96-9825-3499-8f59-97f9e6baf48a | -12.2189 | -56.560902 | 2026-07-01 01:11:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccb0e72b-2192-309d-a222-6e2af468ab6c | -12.4177 | -58.3699 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8d2c97-b251-3448-bfa9-1a7f32e00d2d | -11.4247 | -56.033001 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98694c1c-b341-379f-b2ab-6d277e2630ea | -16.359301 | -56.639801 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8feaab35-3d29-36c6-bdd1-45ec90acf637 | -10.8451 | -56.644402 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52e74055-ed90-366e-97d4-cce707f4975a | -10.0835 | -60.491699 | 2026-07-01 01:11:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85268114-e924-35fb-9b36-b6b4cf35ff98 | -10.1142 | -52.098701 | 2026-07-01 01:11:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac0029f-2320-318a-b127-11dcfc80c693 | -11.6299 | -59.001999 | 2026-07-01 01:11:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d801f4e-b216-3e01-94cd-57ac9fb6f785 | -10.7723 | -53.537701 | 2026-07-01 01:11:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9060aec8-8c39-35b7-a71c-615167f520c9 | -11.4147 | -56.0726 | 2026-07-01 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 204.0 |
| e8e26a43-6f9a-352f-83fd-8577530d49a7 | -11.5528 | -47.4546 | 2026-07-01 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0498a010-b4fa-37ba-8b68-e2379685e244 | -16.368 | -56.6514 | 2026-07-01 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| e9859472-f035-38fc-84bb-285d192f43e9 | -11.4338 | -56.0509 | 2026-07-01 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 616.1 |
| 926b37cc-2444-3e76-a722-62cd5680f450 | -11.4336 | -56.0711 | 2026-07-01 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 690.6 |
| 24a7627c-da65-370c-ae39-0950c3e7f079 | -8.5933 | -48.0069 | 2026-07-01 01:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| fbad2800-2f3b-3d36-8d8d-f3bb668e38d9 | -11.4334 | -56.0912 | 2026-07-01 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| baa9fc6f-aaed-36ea-aba6-2edf4fef7396 | -12.4096 | -58.3865 | 2026-07-01 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ff7fb98e-eeaf-3239-9b31-6b6cd3536438 | -11.5337 | -47.4571 | 2026-07-01 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 4c0c5260-aa22-3f7b-8591-6b5508710e4a | -12.4094 | -58.4063 | 2026-07-01 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2e15d19e-f644-389d-881c-6186e2a54f57 | -8.1254 | -47.8749 | 2026-07-01 01:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0e4c85b7-16d1-39a2-a74b-e6e3bb195107 | -16.3677 | -56.672 | 2026-07-01 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 3e30f7c8-e8eb-3564-b93f-2f5288d9fdb8 | -11.4149 | -56.0525 | 2026-07-01 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 4714236b-ae44-301b-97bc-278a37b66fbc | -12.4285 | -58.385 | 2026-07-01 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| cb4fbf53-5485-3448-b53a-55276ca58d25 | -8.6121 | -48.0051 | 2026-07-01 01:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 41fff5f8-de07-30eb-b3cd-ead6faca2f55 | -10.6784 | -54.5356 | 2026-07-01 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2f4783ae-a426-3654-90b8-8c2524bf0a7d | -5.8058 | -43.7975 | 2026-07-01 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 79e04829-f12e-3cf7-81ca-61cfe7e5d314 | -11.6286 | -59.0169 | 2026-07-01 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6aa7cbee-b560-3f7b-aa6d-d7348286d0fd | -10.1237 | -52.0905 | 2026-07-01 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 941aa509-9f0e-3de3-866b-80cca4271543 | -3.5043 | -48.039 | 2026-07-01 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 97404b0e-cd68-3f79-b758-f6e6166ec5c3 | -10.9205 | -43.0622 | 2026-07-01 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5ba6fe99-ccaa-3e8e-9f7e-77cd12684687 | -12.4094 | -58.4063 | 2026-07-01 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 25202c1e-2ed2-30ed-bc76-0bdf837fc5b9 | -10.6784 | -54.5356 | 2026-07-01 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| a46747d7-2b89-3895-9fd5-5b7e6b78b7bc | -12.7755 | -44.4693 | 2026-07-01 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 500.9 |
| 17e4ee94-b843-339d-835e-0a2ed1087874 | -11.4338 | -56.0509 | 2026-07-01 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 484.5 |
| 98801de0-96c8-3887-9cae-6de95eaa5241 | -17.7114 | -46.8031 | 2026-07-01 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 862942fb-35dc-3776-882b-c99714f03fac | -12.4096 | -58.3865 | 2026-07-01 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 82f45950-e9ca-36c6-9d32-5fce1c258f53 | -16.368 | -56.6514 | 2026-07-01 01:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| ae6755fc-2000-3fdc-acdf-5148cb88ce93 | -9.6037 | -56.9276 | 2026-07-01 01:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3c0eaa8b-a8fe-3f3d-b89d-bfba252bb370 | -11.4147 | -56.0726 | 2026-07-01 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 232.7 |
| b98e2e22-600b-30cc-87ae-d10ca26a0028 | -3.5043 | -48.039 | 2026-07-01 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ff90e094-22c8-341c-986c-3e99afa4856b | -11.4336 | -56.0711 | 2026-07-01 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 747.9 |
| 07a40e4d-355c-36c9-90f7-1ba6809cad37 | -8.6121 | -48.0051 | 2026-07-01 01:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 77e8e639-6d9a-35be-aaef-5be93edc5120 | -10.9205 | -43.0622 | 2026-07-01 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| bb058915-073c-3d0a-b411-1e0b53a12321 | -8.5933 | -48.0069 | 2026-07-01 01:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 7d563aff-a78e-3864-b1ff-aaf1541577a1 | -11.5528 | -47.4546 | 2026-07-01 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 9f9cbe54-5f16-3315-a266-8e2fced0024b | -12.7751 | -44.4927 | 2026-07-01 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1272.4 |
| 457614f2-6240-3588-abd4-80dd4b1ad13b | -12.7746 | -44.5162 | 2026-07-01 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 95cfdc47-9dcb-371a-9e75-4278d64134c1 | -11.4525 | -56.0695 | 2026-07-01 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 61638359-90b1-3157-9077-20c0fed721f3 | -11.6286 | -59.0169 | 2026-07-01 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8b112f17-2fad-3f1a-9031-8244c06c36bc | -10.1237 | -52.0905 | 2026-07-01 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6c2d88bb-5026-3dca-baf5-e28cce3f0d5c | -11.4149 | -56.0525 | 2026-07-01 01:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| fbf9fca8-f693-3b70-8ea8-a06178128875 | -12.7562 | -44.4724 | 2026-07-01 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 1eb972e5-45c1-39be-ad70-358836f0b87c | -10.7654 | -53.5451 | 2026-07-01 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| d4b72416-8db5-3633-91d1-ddcc1ca0d9f8 | -5.8058 | -43.7975 | 2026-07-01 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5df2ab91-6ac5-3da5-bae4-6bcdc1ed7668 | -10.6787 | -54.5153 | 2026-07-01 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c3da4963-ddc6-3bbc-b8ea-bc7a36c2b57e | -12.7557 | -44.4959 | 2026-07-01 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 459.5 |
| 4369d3d1-136f-32e1-bc71-8098af1763f0 | -12.4285 | -58.385 | 2026-07-01 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |


[Clique aqui para ver as próximas entradas](README5.md)
