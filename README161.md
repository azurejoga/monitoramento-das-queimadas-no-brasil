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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec24ef7a-0065-3801-ab8e-e0bbcfffb8b7 | -10.64231 | -53.68882 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1889373e-3240-332b-8f83-053bf6d9ea09 | -10.64174 | -53.69292 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ce299ec-4d1f-39dc-8e0a-b3e9c831c067 | -10.63856 | -53.68411 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37df3a3d-7612-3b34-a774-960f9ccb5050 | -10.63798 | -53.68823 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f194741-64ba-3b26-a52c-36e4faf73772 | -10.63741 | -53.69232 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1345d874-df4f-32f4-87f7-9ea3c6514363 | -10.63717 | -53.66251 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9146e98f-8525-3380-8951-2de2578ff347 | -10.63309 | -53.69169 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5efc779c-503d-32cf-8423-c1b73c4d99d9 | -10.22303 | -52.70272 | 2024-10-03 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d66b33-23a3-313b-b375-d0557a6ea82a | -10.21843 | -52.70204 | 2024-10-03 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02cc0eb0-2aa3-3aa5-a67a-35799651a3e3 | -10.66844 | -53.70331 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c05cde53-80f6-35da-a0b3-160291b24c79 | -10.66788 | -53.70744 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b21dde-74ab-3c1f-b427-8f058bc3f99e | -10.66467 | -53.6986 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32ad93b6-f4ff-393d-9084-b89f11ab13e2 | -10.66411 | -53.70277 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4333cc50-9666-3d14-8734-2b8dd57544b9 | -10.66033 | -53.69804 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 475c2fd7-1903-3e00-9e74-a08d7b14a8fb | -10.65977 | -53.70219 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20a76c0a-6706-3c3d-9b42-49a23577f5eb | -10.656 | -53.69747 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a170273c-08cc-3838-8ae6-d4bd8f313878 | -10.65544 | -53.70161 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9baae28-7262-3fdb-b0b1-eeef6afb9dc1 | -10.65489 | -53.70575 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4164cd0-3438-325e-aef0-7afde227d5cb | -10.65474 | -53.69463 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f2a225-8d1f-3e1f-af13-f37697ac48c6 | -10.65434 | -53.70988 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0abf64c2-7c40-3fdf-a045-32891a6d0a4b | -10.65415 | -53.69877 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 259afb53-d783-31c5-a2d0-78a2952d155c | -10.65378 | -53.71401 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddaa6a2b-e58a-3509-9f07-478e0bddd5f2 | -10.65357 | -53.7029 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f34a35b-6f95-370c-8683-6230dc1ae79e | -10.65298 | -53.70702 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c8d066-8175-306c-9a48-fd81f2cac36f | -10.6524 | -53.71114 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88ee8126-26b7-32b7-a25f-2421d0fbef46 | -10.65182 | -53.71527 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f5f72c-f63a-397e-8a81-02a69c73e798 | -10.65166 | -53.6969 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c70fe72c-e046-33c3-abc1-08ac5e79f3ca | -10.65111 | -53.70103 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a59ba04-67aa-3f24-8598-633860ffe0b4 | -10.65056 | -53.70517 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e1c82d2-9a08-3268-9ef5-e1b0eef011e8 | -10.65001 | -53.70928 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 507dda71-a2e7-323c-8d8c-bac9a5aa9c41 | -10.64982 | -53.6982 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa9dd99e-6dce-3947-a128-109380675a7c | -10.64946 | -53.71341 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f89d40-4ee5-39ee-9c3e-e16d276b1ccf | -10.64924 | -53.70234 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c03ab51-5667-3db5-9929-08c1e76cf1e6 | -10.64866 | -53.70645 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d03e6ce5-7e3a-34c5-a97e-dc17d8794b63 | -10.64808 | -53.71055 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5078af69-1dcf-316e-b701-7b408eea053d | -10.64733 | -53.69632 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf87c817-f068-3b29-83c1-574b026e6050 | -10.64678 | -53.70046 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aaa3ccf-c371-3d20-9bca-bb5279947ac7 | -10.64549 | -53.69764 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821245ca-a9bf-36f7-9860-17b95fcb508a | -10.64491 | -53.70175 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fd68c5f-53a2-372b-b033-ec55b3fcd211 | -10.643 | -53.69573 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1842b740-6592-35fc-a70c-c8266e17974d | -10.64245 | -53.69984 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdd0b93-767f-3727-9fcb-8d4493483f87 | -10.6419 | -53.70396 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b42d572-5a07-3ce5-bad8-e623a9bac9c6 | -10.64116 | -53.69702 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8ae2ad-2560-3eb6-bc65-ea952f2f1729 | -10.64058 | -53.70113 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5636f546-a244-3f2b-83fe-9e66f5d5dd18 | -10.64001 | -53.70525 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7addbb9f-b3dd-34d2-ac81-ef7dd9a356fc | -10.63684 | -53.69641 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d6d2ef6-3e08-3358-a621-53371c5bd18b | -10.63626 | -53.70052 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45906eb1-6713-3857-b934-ac5bbc986b6f | -10.63251 | -53.69579 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bfeca740-a8bc-3ca1-b363-05a7239a4c1a | -10.63194 | -53.69992 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b29da3e1-e5fd-33f8-b5ae-b485a1e8ad51 | -10.62819 | -53.69518 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 391f7bf0-9ad2-35d2-b9ae-8d32bc3da12c | -10.62761 | -53.69932 | 2024-10-03 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e71a92c8-3d6c-3b29-a0b2-2c9936eaa8fd | -11.08236 | -52.52531 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa3f2e58-0748-3b4e-bb91-47c643e4617b | -11.08169 | -52.53037 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfca05cb-84db-3750-af50-c81ee3f9c6b8 | -11.07763 | -52.52475 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3b5f2e1-8c2c-3075-8db6-f38b27d98eb4 | -11.07697 | -52.52977 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a90b4b6f-75fb-3ad6-8edb-4f358f907f6a | -11.07225 | -52.52911 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21c24a89-26d0-3f53-b4d1-2bdc8883d51d | -11.0682 | -52.52346 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6026c7e7-50e9-3d0a-beb2-117de0dd2a26 | -11.06754 | -52.52842 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9285dfb7-9b26-3237-ae8d-f6746ef0af8b | -11.06348 | -52.52275 | 2024-10-03 05:16:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c15b02d0-617d-348a-94db-05abdb561d3e | -12.67042 | -54.08258 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e67ffd1e-09ee-3dd8-915f-4b303cdee8fe | -12.66663 | -54.07779 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29c7d043-8346-3d62-af41-f5f6b1675fb4 | -12.66015 | -54.05972 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14774f81-ebd1-3331-9d87-697e291d05a9 | -12.6596 | -54.06395 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f66d9367-e037-3b55-ac35-eeb3b8ae0b17 | -12.65905 | -54.06816 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 200a4506-00cb-35af-bf9e-65142470b483 | -12.65581 | -54.0591 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fa586ce-e15b-3892-9205-5be271cac28c | -12.65525 | -54.06334 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6067d6-798d-3bab-97f4-a7e3b2f6c039 | -12.65471 | -54.06755 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2523292f-99fc-37de-bf07-097f82f04dce | -12.65416 | -54.07175 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 154b8716-c223-3cc2-89d6-df3081a2b096 | -12.65091 | -54.06272 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d787f6eb-100e-3829-afda-f4bb80b55ad8 | -12.65036 | -54.06693 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91c9c82b-1e14-3d06-a6cb-b81dbf10b5a5 | -12.33673 | -54.09923 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 711ccb8f-537e-3fee-96e2-c29facef6646 | -12.33406 | -54.0861 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 852b4c48-350d-33fe-b3fc-1e1b18a01d01 | -12.33351 | -54.09029 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fec4efc-3742-3f37-b380-a52ec06f7b06 | -12.33296 | -54.09447 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f018dfac-6b27-31c1-9f3c-8f1575754889 | -12.32919 | -54.08968 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccb7510e-292d-38e0-a03b-fc5dfacb8e4e | -12.32488 | -54.08906 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b7028a-c4a5-36f3-ae36-c3c4854b4388 | -12.32433 | -54.09325 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b3f80e5-0f81-30ee-8fa9-640a9f2924cb | -12.26908 | -53.99884 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0b7d6d9-cd99-37b3-98e2-d6016aa92f05 | -12.26476 | -53.99815 | 2024-10-03 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a45937f3-c32d-3f65-b351-fc9d56f7fe43 | -12.61192 | -53.49559 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd5d0c1-fb67-3617-9d4f-999ebfd4a8ef | -12.61003 | -53.49781 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dcbb11f-edad-390e-9949-f8df9a9dbe92 | -12.60741 | -53.49496 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 000ed21d-f652-3b88-80e2-4351e32abb07 | -12.60552 | -53.4972 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 185095e9-4640-3118-97f6-46f5c43025d7 | -12.56928 | -53.13573 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a53b4ff7-5350-305b-9295-f5431b2c7d7c | -12.56466 | -53.13505 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| deb13cec-e34c-3d55-9a0d-29a1d0e39d67 | -12.56403 | -53.14001 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 411105f3-9dd5-3082-b290-85aaf4689e8e | -12.56049 | -53.13681 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b71fc83e-0d2e-3f66-ae07-d41dd0f0b6af | -12.55941 | -53.13933 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dc088e4-3db9-3457-b035-ae91cef85c31 | -12.55587 | -53.13616 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c1a33e2-adae-39dc-931e-31d1af3d7a28 | -12.5552 | -53.14111 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b984b8a-4c52-3bfc-a245-6f65fb0fad47 | -12.55479 | -53.13868 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9788279-ff5c-307b-8766-6386514b7669 | -12.55058 | -53.14049 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23578677-96cb-336a-9255-543841c08b25 | -12.55017 | -53.13805 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5557505b-80fe-3449-bfbf-4df250be86c7 | -12.54596 | -53.13988 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8b809b-6936-3051-af4a-13093b2e53cf | -12.54555 | -53.13743 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffd29cfc-1d80-3531-a494-727d4b8c2891 | -12.54133 | -53.13931 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61dcd945-4363-375f-9073-c124e7491910 | -12.54092 | -53.13686 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 273ff6e7-1bb9-3680-805e-85fdd5b5ecb8 | -12.54062 | -53.10935 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb2a769d-83e9-3ff4-a0f2-aac41fbf913f | -12.53998 | -53.11415 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8db185bf-54cc-3599-a0af-dd6492a4635f | -12.53599 | -53.10873 | 2024-10-03 05:16:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README162.md)
