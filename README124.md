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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 350844c3-f58e-3b1e-b2eb-71d34a172600 | -16.9853 | -56.79264 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 342838d9-476a-322f-bdec-d547ce05018c | -16.98408 | -56.80107 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 59e1f779-1cb0-3f77-a3dc-b063851b7859 | -16.98348 | -56.80527 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2214db59-bc90-3cde-86cf-a689ca93518a | -16.98052 | -56.80051 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8c7b2a92-f7d4-3f4d-aa39-b1222f2b285c | -16.97992 | -56.80472 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 63985ce8-0e53-38da-9a55-188cbb0d63ef | -16.97466 | -56.7651 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 9d4251c0-9caa-3b5e-bda3-669fbd7e7d92 | -16.9746 | -56.79098 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 981845f2-1f5c-3bad-b215-b35832de958b | -16.97339 | -56.79941 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b02ffaa3-69e6-3bc5-880a-c1b310ef54ca | -16.97279 | -56.80362 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 671ca64e-0f61-3f5a-9215-1fb51279ad77 | -16.97164 | -56.78621 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2cbd17a7-3705-37f3-bbbf-875754c4a167 | -16.96632 | -56.77245 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 9117459d-cc33-3f6c-8357-448266295605 | -16.96335 | -56.76767 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| e4efd467-6ea0-39b7-9b0c-b1ac9e258964 | -17.1486 | -56.75789 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 3ca25b11-6f8b-3672-92bd-9676a1c14ad7 | -17.14622 | -56.74883 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 8aba3d36-3440-3af9-abe0-2a7c4cd395a6 | -17.12594 | -56.76307 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a355cee8-2385-3d85-b737-b417448789b0 | -17.12474 | -56.74551 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e5c2b6ac-5cb9-38e6-b390-28b308470e10 | -17.12059 | -56.77526 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 58ceaa25-da29-3659-bb5e-833893615cf5 | -17.12 | -56.77951 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e1412e9c-50da-32fe-8e2f-e4049ed0ad30 | -17.1182 | -56.76622 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1ffbcb43-eab9-3c19-b200-e0985f90d020 | -17.11761 | -56.77047 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f3692897-670a-3c4d-94d9-c0a9e93eb1f2 | -17.11699 | -56.74867 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 25ac4834-eecf-36c6-a49c-482365c8116b | -17.114 | -56.74386 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 49ca030d-b634-374f-909f-08a833bd7f64 | -16.98659 | -56.7583 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4749daea-25e3-34e6-adf6-ee299f95bd78 | -16.9818 | -56.7662 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ae6b7d8f-557c-30d4-a723-b8f24eb83009 | -16.98005 | -56.75296 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c8ad6ef7-1929-3b4c-bba2-ecdeb4884cf2 | -16.97884 | -56.76142 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 364d79c7-85c4-3644-a96b-da39bae062ec | -16.96868 | -56.78144 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7bf1092d-a1cd-3654-b60b-3bb9a27726c5 | -16.96813 | -56.75977 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e827d395-c2ea-3d30-a17c-ea3c93418794 | -16.96807 | -56.78567 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 494c5f7b-cde6-338a-9a2f-4ec72ed0b913 | -16.96451 | -56.78511 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad1fe83f-8e3f-32d8-8824-2b477513c538 | -16.95918 | -56.77135 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 4c2a1171-c8f8-3528-98ad-624e5bff916c | -16.86026 | -56.73127 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 90270434-a280-3ff6-bc12-3c09ac263ba4 | -16.85965 | -56.73548 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d02652ed-2fc4-3eb1-b7cf-e01f4c9295aa | -16.85311 | -56.73016 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c671030c-36a8-350c-8d1a-5b53038a8013 | -16.85251 | -56.73439 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 13e54c23-b2af-3cd3-a0bd-ecc560798a33 | -16.699 | -57.17229 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5af70136-d776-3a66-8064-1dc671540eee | -16.69491 | -57.17578 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7b914f27-2d9d-3b8d-bcab-91f4b0ad2280 | -16.84929 | -57.45951 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e4237f40-86e9-3e3d-b0ff-d70db2e68d0b | -16.8389 | -57.45787 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3dc221b1-daa8-3b30-a119-21c13fc70b61 | -16.83602 | -57.45336 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3965354b-713a-37e2-ad34-e781bb8129fb | -16.83198 | -57.45678 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 12232d98-1f67-38a3-906b-463ca5f074e9 | -16.82852 | -57.45623 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 8667e014-e35d-3dce-91bd-283073d2997b | -16.82795 | -57.46018 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 326aeee6-923c-3160-8b27-01138742afdf | -16.82159 | -57.45514 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f3202b6f-9968-3995-862b-ca47576f0ac6 | -16.81871 | -57.45063 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| fce5bc17-4189-39b5-80bb-80a6c377c8a7 | -16.80242 | -57.39127 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 65caa80a-c5d8-3547-8d1f-908ce97a310b | -16.79838 | -57.3947 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 43804997-5562-33fe-a45f-7b66764dbc95 | -16.79639 | -57.39495 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| bfb1ff19-4911-34d4-a699-84e890c6e7e4 | -16.79055 | -57.43458 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5941eaff-36ff-3568-9790-d31647eb713f | -16.78938 | -57.44249 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9a3be1d1-dee3-3375-ad22-f00a8589515b | -16.78817 | -57.46603 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2bca5b01-d7f2-35d8-a4ad-0a494400bba4 | -16.78811 | -57.44175 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a1d656c5-0077-30b4-ad94-c46d73ea13a7 | -16.78761 | -57.46998 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a57b4fda-ff5d-3b28-9196-dfd12a7db913 | -16.78704 | -57.47392 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6df167a9-3218-3942-a8f4-fba057712ee2 | -16.78592 | -57.44194 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3a2e3fc5-9504-35ac-9d01-d2974f3611fd | -16.78472 | -57.47408 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2fa6315-cbcd-3383-9fd0-158c26139eac | -16.78188 | -57.44535 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 340a219a-f039-34e8-848e-e61e32ae52c9 | -16.78065 | -57.50166 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5ff65d0-e488-3f8a-8db6-0efbcdc90030 | -16.77778 | -57.49717 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 436d0140-deac-3038-a693-d2f2b38df737 | -16.77725 | -57.45272 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a596cfe2-013b-345d-9ba4-440c5df1f7dd | -16.77667 | -57.45667 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2e9ea009-cf0b-3ebc-af9b-08f36a234229 | -16.77665 | -57.48088 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e16e52e9-8cf4-3e5c-a854-a4d23213db4c | -16.77493 | -57.4685 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b7e9afcb-65ee-38f5-85f2-6b087a433947 | -16.77432 | -57.49664 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 888a5f4f-b3b0-3fc8-84eb-996ce15618a9 | -16.77374 | -57.50057 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 85a0ea53-b97a-3ff2-a48c-f9d89d81eaa7 | -18.6591 | -57.26256 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 927d0af1-4636-3a78-b5bc-8150ccb01549 | -16.77089 | -57.4719 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 89d4fe6a-de4d-3da1-a749-699c4d41f496 | -16.76915 | -57.48373 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| abcda648-470a-39f3-82d3-d8de1ad3a71d | -16.76857 | -57.48767 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1c0b4e2d-8122-3ab1-bf3e-c02207a1a88f | -16.76801 | -57.46741 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1bdeb75f-129d-3edf-bc04-36074549beaa | -16.768 | -57.49162 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 53721511-7c08-3c6a-a1b2-1f6d8f9c6c81 | -16.76513 | -57.46293 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5c28d8d0-5c74-3e41-8b44-aab033f6afad | -16.76512 | -57.48713 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 18acdca9-9353-3418-9384-ca61d6a75b97 | -16.76455 | -57.46687 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e0fb2f40-9ef0-3c03-a10d-f23686917b12 | -16.76454 | -57.49107 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 20bb3657-0aeb-379e-b7a2-b8ba31a50973 | -16.76396 | -57.495 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| e8120b2f-9452-3f62-b488-fafce294c4f0 | -16.76168 | -57.46238 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9bde2a4e-715e-3ade-b0b4-61364f8aa45d | -16.75764 | -57.46577 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f2953e68-5aa9-34a2-a7dc-3764f8a59dea | -16.75418 | -57.46523 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5084fbcd-1e9b-3bf3-a5e8-eb5c91a4db34 | -16.71557 | -57.46317 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 95e7d1e5-c7d2-34bf-9305-6f2e03653fa3 | -16.71212 | -57.46262 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 80f27a7b-edc6-3838-9111-95ab9787daa6 | -16.71155 | -57.46657 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8d65322f-e106-37f0-a925-3b10c866af53 | -16.71098 | -57.47051 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 93055ad8-d16e-3f8d-8482-37403e968741 | -16.71037 | -57.45024 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1706bfb7-aa9e-3699-8ef6-54e6dcf7859e | -16.70406 | -57.46942 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cfda5a3f-21ea-3ef4-bda2-89d4dd6b8f87 | -16.70175 | -57.46098 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 7af44a10-8866-3c7c-9312-96602532c6c7 | -16.70118 | -57.46493 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f6458ae8-ba8d-34d3-b1f2-08e87ae676af | -16.69829 | -57.46043 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 3954dacd-ff43-3c64-b52f-299d17485c09 | -16.69194 | -57.45539 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4dbb51bd-2d8b-31a8-bcaf-56a850b5aa49 | -16.69137 | -57.45934 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 043d0ffc-fdbd-3bb7-b2f6-98cf1b7eb43b | -16.68962 | -57.44695 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b9455bb6-1051-3db6-a2b0-6448638633c8 | -16.68905 | -57.4509 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 69e947de-31b4-3b01-ad6f-683bc62fc5d0 | -16.68848 | -57.45485 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b7003720-a42d-34c6-a559-d0080ffa8e5d | -18.65852 | -57.26678 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| e7c4e958-874b-3ac2-8cb4-61bac438f219 | -16.68559 | -57.45035 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 28e86e6f-766a-353a-a14e-580a3a7ac033 | -16.68502 | -57.4543 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8d2d5dbe-3796-373b-a7c9-79f54cd81e4c | -16.68044 | -57.46164 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 47c166fc-d83a-3e83-b195-aa0cf364f95d | -16.67987 | -57.46559 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 885b072b-0011-337b-ba9b-7873147a5220 | -16.67661 | -57.47044 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1885e697-e009-3c76-bf9c-c04518a11f5b | -16.67641 | -57.46505 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README125.md)
